"""DEMO HMI — CS 581 W3 reference build.

Basic auth is REQUIRED this week. An unauthenticated request must return 401,
and the status probe checks exactly that.

Two things to notice while you copy the pattern:
  * Basic auth replays the credential on every single request. There is no
    session and no lockout. That is why the W3 assignment calls it the weakest
    thing that beats nothing.
  * hmac.compare_digest, not ==. String comparison leaks timing.
"""
import asyncio, hmac, os
from functools import wraps
from flask import Flask, Response, request, render_template_string
from pymodbus.client import ModbusTcpClient

USER = os.environ.get("HMI_USER", "operator")
PASS = os.environ.get("HMI_PASS", "")
NAMES = ["pump_1_speed", "pump_2_speed", "header_pressure",
         "supply_temp_c_x10", "return_temp_c_x10", "flow_total_lpm"]
UNITS = ["rpm", "rpm", "kPa", "degC x10", "degC x10", "L/min"]
app = Flask(__name__)


def auth_required(f):
    @wraps(f)
    def w(*a, **kw):
        h = request.authorization
        ok = (h and hmac.compare_digest(h.username or "", USER)
                and hmac.compare_digest(h.password or "", PASS))
        if not ok:
            return Response("authentication required", 401,
                            {"WWW-Authenticate": 'Basic realm="DEMO service water"'})
        return f(*a, **kw)
    return w


def read():
    c = ModbusTcpClient("127.0.0.1", port=5901, timeout=3)
    try:
        if not c.connect():
            return None
        r = c.read_holding_registers(0, count=6, device_id=1)
        return None if r.isError() else r.registers
    finally:
        c.close()


PAGE = """<!doctype html><title>DEMO Service Water</title><style>
body{background:#0f1115;color:#e6e9ef;font:14px ui-monospace,Menlo,monospace;padding:26px;margin:0}
h1{font-size:18px;margin:0 0 3px}.s{color:#8b93a3;font-size:12px;margin-bottom:20px}
table{border-collapse:collapse}td,th{padding:6px 14px 6px 0;text-align:left}
th{color:#8b93a3;font-size:11px;text-transform:uppercase;letter-spacing:.5px}
.v{font-size:16px;font-variant-numeric:tabular-nums}.u{color:#8b93a3;font-size:11px}
.err{color:#e0574d}.n{color:#8b93a3;font-size:11.5px;margin-top:22px;max-width:62ch;line-height:1.6}
</style><meta http-equiv=refresh content=5>
<h1>DEMO &mdash; Service Water System</h1>
<div class="s">Purdue Level 1 &middot; Modbus TCP 127.0.0.1:5901 &middot; reference build, refreshes every 5s</div>
{% if regs %}<table><tr><th>point</th><th>value</th><th>register</th></tr>
{% for n,u,v,i in rows %}<tr><td>{{n}}</td><td class="v">{{v}} <span class="u">{{u}}</span></td>
<td class="u">4000{{i+1}}</td></tr>{% endfor %}</table>
{% else %}<p class="err">Modbus server unreachable on 127.0.0.1:5901</p>{% endif %}
<p class="n">This HMI asked you for a password. The Modbus service behind it did not, and could not:
the protocol has nowhere to put a credential. Anything that can reach port 5901 can write a coil.
That asymmetry is the finding of Workshop 3.</p>"""


@app.get("/")
@auth_required
def index():
    regs = read()
    rows = list(zip(NAMES, UNITS, regs or [], range(6))) if regs else []
    return render_template_string(PAGE, regs=regs, rows=rows)


@app.get("/healthz")
def healthz():
    return {"ok": True}
