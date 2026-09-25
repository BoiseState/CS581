# W3 reference build — DEMO Service Water System

A complete, working example of everything Workshop 3 asks for. It runs on the lab
host as the `demo` system, and you can point a client at it while you build yours.

**This is not any student's assigned system. Read it, do not copy it.**

    lab/demo_server.py        Modbus TCP server, point map, process loop, SIEM events
    lab/hmi/app.py            Flask HMI with basic auth
    lab/units/*.service       the two systemd user units
    points.md                 the point map, including what the model does not represent

## What it demonstrates

Every graded check on the Lab Build, and a few things that are not graded but
will save you time:

- Values that actually move. Writing coil 0 starts pump 1, the header pressure
  and flow rise, and the supply temperature then falls. A capture taken over two
  minutes contains a causal chain rather than unrelated readings.
- Basic auth that returns 401 to an unauthenticated request, using
  `hmac.compare_digest` rather than `==`.
- Events posted to the OT-SIEM, including a `protocol.write` whose message says
  the thing worth saying: Modbus carries no identity for the writer.
- A point map that documents its own limits.

## The pymodbus notes that will save you an hour

This was built against **pymodbus 3.15.0**, which is what `pip install pymodbus`
gives you on the lab host. Most examples you will find, including most that an AI
assistant will generate, target pymodbus 2.x and will not run.

- `ModbusSlaveContext` does not exist. It was renamed `ModbusDeviceContext`, and
  that entire datastore API is deprecated and disappears in pymodbus 4. Use
  `SimData` / `SimDevice`, as the reference does.
- `ModbusSequentialDataBlock(0, ...)` raises `TypeError: 0 <= address < 65535`
  despite the message. The legacy path is not worth fighting.
- `SimDevice` takes a **tuple** of four lists in the order `(di, co, hr, ir)`.
  Passing a list of lists raises `simdata=list[0] is not a SimData entry`.
- `srv.context` is a `SimCore`. Its only accessors are `async_getValues` and
  `async_setValues`, both coroutines, and the argument order is
  `(device_id, func_code, address, ...)`. `device_id` must match your `SimDevice`
  id. It is 1 here, not 0.
- Do not wrap those accessors in a bare `except`. A silent failure there means
  your values never move, and "values changing" is a graded check. That mistake
  is how this reference build failed its own check the first time.

## Event volume, which is easy to get wrong

The first version of this reference emitted a sampled read once a minute. Left
running overnight that produced **707 events**, and it was the only system
reporting. Nine systems doing the same would push roughly 13,000 events a day
through a dashboard that shows 150 at a time, and the events anyone actually
needs to see would be buried under a wall of "registers sampled".

It now samples once every fifteen minutes. The rule of thumb:

- **Always emit** state changes, writes, auth failures and alarms. Those are rare
  and every one of them matters.
- **Sample** routine polling. Once every ten to fifteen minutes is plenty to show
  the system is alive and reading.
- **Never** emit one event per protocol transaction. Your server may poll every
  two seconds; the SIEM does not need to know that 30 times a minute.

The ingest API rate-limits at 600 events per minute per system, but that is a
backstop against a runaway loop, not a target.

## Try it

From the lab host:

    python3 -m venv .venv && ./.venv/bin/pip install pymodbus
    ./.venv/bin/python - <<'PY'
    import asyncio
    from pymodbus.client import AsyncModbusTcpClient
    async def main():
        c = AsyncModbusTcpClient("127.0.0.1", port=5901); await c.connect()
        r = await c.read_holding_registers(0, count=6, device_id=1)
        print(r.registers)
        c.close()
    asyncio.run(main())
    PY

The HMI is at `demo.plant.sanctumsec.com`. Ask for the credential if you want in;
the point of it being protected is that you have to.
