# Point map — DEMO Service Water System

Modbus TCP, `127.0.0.1:5901`, device id 1. Reference build for CS 581 Workshop 3.

Addresses below are zero-based as the wire uses them. The `4000x` column is the
conventional human-facing numbering, which is one-based. That off-by-one is a
classic source of confusion and is worth stating explicitly in your own map.

## Holding registers (function code 3, read; 6 and 16, write)

| Addr | Conventional | Name | Type | Units | Range | R/W | Represents |
|---|---|---|---|---|---|---|---|
| 0 | 40001 | `pump_1_speed` | uint16 | rpm | 0–1800 | R | Service water pump 1 shaft speed |
| 1 | 40002 | `pump_2_speed` | uint16 | rpm | 0–1800 | R | Service water pump 2 shaft speed |
| 2 | 40003 | `header_pressure` | uint16 | kPa | 0–900 | R | Common discharge header pressure |
| 3 | 40004 | `supply_temp_c_x10` | uint16 | °C × 10 | 180–580 | R | Supply header temperature, scaled by 10 |
| 4 | 40005 | `return_temp_c_x10` | uint16 | °C × 10 | 180–640 | R | Return header temperature, scaled by 10 |
| 5 | 40006 | `flow_total_lpm` | uint16 | L/min | 0–4000 | R | Total header flow |

Temperatures are scaled by ten because Modbus registers are 16-bit integers with
no notion of a decimal point. The scaling factor lives in documentation, not on
the wire, so a client that does not read this table will report 254 °C.

## Coils (function code 1, read; 5, write)

| Addr | Conventional | Name | R/W | Represents |
|---|---|---|---|---|
| 0 | 00001 | `pump_1_run_cmd` | R/W | Start/stop command, pump 1 |
| 1 | 00002 | `pump_2_run_cmd` | R/W | Start/stop command, pump 2 |
| 2 | 00003 | `bypass_valve_open` | R/W | Header bypass valve |

## Process behaviour

Pumps ramp toward 1750 rpm over a few seconds when commanded. Each running pump
contributes roughly 1650 L/min and 310 kPa. Opening the bypass drops header
pressure to about 72 percent.

Heat rejection depends on flow. Below 800 L/min the supply temperature climbs at
about 0.3 °C per tick; above it, it falls. Crossing 45 °C raises a `process.alarm`
at severity `high`, and dropping back below clears it. Ticks are two seconds.

That coupling is deliberate: it means a write to a coil eventually shows up as a
temperature alarm, so a capture taken over a couple of minutes contains a causal
chain rather than a set of unrelated readings.

## What this model does not represent

Everything that would make it a real plant. There is no pump curve, no cavitation,
no NPSH limit, no valve stroke time, no sensor lag, no redundancy logic, no
instrument failure mode, and the thermal model is a first-order fudge with no
heat load behind it.

An analyst reading a capture from this system could reasonably conclude that
service water responds instantly to commands and that temperature is a simple
function of flow. Both are artefacts of the simulation. The point map tells you
what the registers mean; it does not tell you whether the physics behind them is
worth trusting.
