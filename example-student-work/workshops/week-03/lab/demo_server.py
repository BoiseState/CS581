#!/usr/bin/env python3
"""DEMO — Service Water System.  CS 581 Workshop 3 reference build.

A worked example of everything W3 asks for. This is not any student's assigned
system, so read it, do not copy it.

Demonstrates:
  * a Modbus TCP server with a point map that matches points.md
  * a process loop, so values move and a capture is worth taking
  * events posted to the class OT-SIEM, including one that corresponds to a
    detection opportunity
  * binding to 127.0.0.1 only

pymodbus 3.15 notes, because these will cost you an hour otherwise:
  * ModbusSlaveContext does not exist. It was renamed ModbusDeviceContext, and
    that whole datastore API is deprecated and disappears in pymodbus 4. Use
    SimData / SimDevice as below.
  * SimDevice takes a TUPLE of four lists, in the order (di, co, hr, ir).
    A list of lists raises "simdata=list[0] is not a SimData entry".
  * srv.context is a SimCore. Its only accessors are async_getValues and
    async_setValues, both coroutines, and the argument order is
    (device_id, func_code, address, ...). device_id must match your SimDevice
    id, which is 1 here, not 0.
  * Most AI-generated pymodbus code targets 2.x and will not run here.
"""
import asyncio, json, os, random, time, urllib.request

from pymodbus.simulator import SimData, SimDevice, DataType
from pymodbus.server import ModbusTcpServer

BIND, PORT = "127.0.0.1", 5901
SIEM = "http://127.0.0.1:5090/api/v1/events"
TOKEN = os.environ.get("SIEM_TOKEN", "")
SYSTEM, LEVEL = "demo", 1

# ---------------------------------------------------------------- point map
# Keep in step with points.md. The status probe compares the two.
HOLDING = ["pump_1_speed", "pump_2_speed", "header_pressure",
           "supply_temp_c_x10", "return_temp_c_x10", "flow_total_lpm"]
COILS = ["pump_1_run_cmd", "pump_2_run_cmd", "bypass_valve_open"]

st = {"p1": 0.0, "p2": 0.0, "press": 120.0, "supply": 24.0,
      "ret": 30.5, "flow": 0, "alarm": False}


def emit(event_type, severity, message, **kw):
    """Post one event. A SIEM that is down must never stop the process."""
    if not TOKEN:
        return
    body = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "system": SYSTEM, "purdue_level": LEVEL,
            "event_type": event_type, "severity": severity, "message": message}
    body.update(kw)
    try:
        urllib.request.urlopen(urllib.request.Request(
            SIEM, data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer " + TOKEN}), timeout=3).read()
    except Exception:
        pass


def step(cmd1, cmd2, bypass):
    """One tick. Values must move; a static capture teaches nothing."""
    for k, cmd in (("p1", cmd1), ("p2", cmd2)):
        st[k] += ((1750 if cmd else 0) - st[k]) * 0.25 + random.uniform(-8, 8)
        st[k] = max(0.0, min(1800.0, st[k]))
    running = (st["p1"] > 200) + (st["p2"] > 200)
    st["flow"] = int(running * 1650 + random.uniform(-60, 60))
    st["press"] = 120 + running * 310 + random.uniform(-14, 14)
    if bypass:
        st["press"] *= 0.72
    # heat rejection falls away when flow drops: this is what trips the alarm
    st["supply"] += (0.30 if st["flow"] < 800 else -0.24) + random.uniform(-.05, .05)
    st["supply"] = max(18.0, min(58.0, st["supply"]))
    st["ret"] = st["supply"] + 6.5 + random.uniform(-.4, .4)

    hot = st["supply"] > 45
    if hot and not st["alarm"]:
        st["alarm"] = True
        emit("process.alarm", "high",
             f"Supply temperature {st['supply']:.1f} C above the 45 C limit",
             target={"point": "40004", "name": "supply_temp_c",
                     "value": round(st["supply"], 1)})
    elif not hot and st["alarm"]:
        st["alarm"] = False
        emit("process.alarm", "info", "Supply temperature back within limits")


async def main():
    regs = SimData(0, count=len(HOLDING), values=0, datatype=DataType.UINT16)
    coils = SimData(0, count=len(COILS), values=0, datatype=DataType.BITS)
    dev = SimDevice(1, ([coils], [coils], [regs], [regs]))   # di, co, hr, ir
    srv = ModbusTcpServer(dev, address=(BIND, PORT))

    emit("service.state", "info",
         f"DEMO service water system started on {BIND}:{PORT}, "
         f"{len(HOLDING)} holding registers and {len(COILS)} coils")

    async def loop():
        ctx, last, n = srv.context, [0] * len(COILS), 0
        while True:
            # NOTE the argument order: (device_id, func_code, address, count).
            # Both accessors are coroutines and must be awaited. Do not wrap
            # these in a bare except: a silent failure here means your values
            # never move, and "values changing" is a graded check.
            cur = list(await ctx.async_getValues(1, 1, 0, len(COILS)))
            for i, (was, now) in enumerate(zip(last, cur)):
                if was != now:
                    # a write from anywhere is a write: Modbus carries no identity
                    emit("protocol.write", "high",
                         f"Coil write to {COILS[i]}; Modbus carries no identity "
                         f"for the writer",
                         target={"point": f"{i+1:05d}", "name": COILS[i], "value": now},
                         detail={"function_code": 5, "prior_value": was})
            last = cur
            step(cur[0], cur[1], cur[2])
            await ctx.async_setValues(1, 3, 0, [
                int(st["p1"]), int(st["p2"]), int(st["press"]),
                int(st["supply"] * 10), int(st["ret"] * 10), int(st["flow"])])
            n += 1
            if n % 30 == 0:          # sample reads; do not emit every poll
                emit("protocol.read", "info",
                     "Holding registers 40001-40006 sampled",
                     target={"point": "40001", "name": "pump_1_speed",
                             "value": int(st["p1"])})
            await asyncio.sleep(2)

    asyncio.create_task(loop())
    await srv.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
