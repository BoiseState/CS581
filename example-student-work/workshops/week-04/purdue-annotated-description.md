# Purdue Model Annotation — Physical Security Integration (PSI)
## CS 581 Workshop 4 | Jordan Reyes | Oct 10, 2026

**System:** Physical Security Integration (PSI)
**Purdue Level:** Level 3 (plant network / enterprise-adjacent)

---

## The topology as the status board shows it

The W3 status board shows PSI as a single tile at Level 3, with active connections to DCS (Level 2) and the OT-SIEM. The architecture page shows PSI as the plant's physical access gateway: it feeds badge events to the DCS alarm system and logs them to the SIEM.

During W3, both peer links were confirmed live — badge events were reaching the SIEM in real time, and the DCS was receiving door-state signals from PSI over the loopback connection.

The HMI at `https://psi.plant.sanctumsec.com` requires Basic Auth before serving the badge event dashboard. A screenshot of the HMI showing a normal shift's badge traffic is included below (no credential values visible).

```
[HMI screenshot: badge event log, Oct 9, 2026, 18:00–20:00 MT]
Entry events: 4 (zones 1, 2, 3)
Exit events: 3
Denied: 1 (zone 4 — Vital Area, maintenance credential)
Auth failures (probe): 2 (CS581-StatusProbe/1.0 — known monitoring agent)
```

---

## Where the board's Purdue levels meet the host's reality

The status board places PSI at Level 3 and draws the boundary cleanly. The host does not enforce that boundary.

All eight plant systems run on one machine and bind to 127.0.0.1. The `psi` account's SSH session can connect to port 5060 (RMS, Level 2), port 5030 (RPS, Level 1), or any other system with a single `nc` or `python3` call. No firewall rule, no network namespace, and no SELinux policy prevents this — checked with `ss -tlnp` and by successfully connecting from `psi` to `rms:5060` during W4 Attack C.

When I asked the AI to annotate the Purdue diagram, it described PSI as "isolated from Level 1 and Level 2 network paths by design." That is what the diagram implies. It is not what the host enforces. I pushed back and asked it to check what an SSH session on `psi` could actually reach, at which point it revised the annotation. The gap between diagram and host is the main finding here.

PSI's physical control path also does not appear on the network diagram at all: the OSDP controller is connected by a serial cable from the lab server to an external device. The diagram shows only the Ethernet connections. An analyst reading the diagram would see PSI as a logging and routing node. PSI also controls who can physically enter the rooms where the other systems live.

---

## Boundary crossings that involve PSI

| Connected system | Protocol | Boundary crossed | RBAC policy says | Host enforces |
|---|---|---|---|---|
| DCS (L2) | Loopback TCP (door-state events) | L3 → L2 | PSI may send alarm signals to DCS; DCS may not initiate | No directionality enforcement; either side can connect |
| OT-SIEM | Syslog over loopback | L3 → monitoring | PSI sends events; SIEM receives only | No enforcement; `psi` can reach siem ports directly |
| OSDP controller | Serial (RS-485) | L3 → physical plant | Only `psi` account via serial script; Supervisor role only for credential changes | Account-level: any SSH session on `psi` reaches the serial port; no role separation |
| RMS (L2) | None designed | L3 → L2 | No policy — connection not expected | Loopback: reachable from `psi` account (verified in Attack C) |

---

## Gaps between the diagram and the host

1. **Loopback reachability.** PSI can reach every other system on the host. The diagram shows only DCS and SIEM as PSI peers. The other six systems are equally reachable. This is structural — it is not a misconfiguration that can be patched without moving systems to separate machines or adding per-account firewall rules.

2. **Serial path not on any diagram.** The OSDP controller serial connection is PSI's most consequential path (it controls physical plant access) and it does not appear on the network architecture. Any analysis based on the diagram alone misses the highest-impact path.

3. **SIEM connection is one-directional by convention only.** The architecture shows PSI sending events to the SIEM. Nothing stops `psi` from reading SIEM records or writing to the SIEM's intake ports directly. The separation is a policy assumption, not an enforced boundary.

4. **DCS alarm path is undocumented.** During W3 the DCS received door-state events from PSI. The format and the DCS endpoint that handles these events are not documented in either system's `points.md`. A stranger taking over PSI would not know what the DCS expects or how to verify the signal is working.
