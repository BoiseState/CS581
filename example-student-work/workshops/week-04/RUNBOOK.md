# Operator Runbook — Physical Security Integration (PSI)
## CS 581 | Jordan Reyes | Last updated: Oct 14, 2026

This document is for whoever takes over PSI for W5. You did not build this system. The goal is that you can bring it up, understand what every point means, and know what to watch for.

---

## System identity

| | |
|---|---|
| System | Physical Security Integration (PSI) |
| Role account | `psi` |
| Hostname | `psi.plant.sanctumsec.com` |
| Purdue level | 3 (enterprise-adjacent; controls physical access to L1–L2) |
| Protocol | OSDP/Wiegand (serial to controller); HTTPS (HMI); Syslog (SIEM) |
| Port block | 5080–5089 |
| HMI URL | `https://psi.plant.sanctumsec.com` (port 5080, Basic Auth) |
| OSDP controller | Serial on `/dev/ttyS0` from the `psi` account |

---

## Starting the system

```bash
# Start the HMI and event-logging services (user systemd units)
systemctl --user start psi-hmi.service psi-logger.service

# Confirm both are running
systemctl --user status psi-hmi.service psi-logger.service
```

**How to confirm it started:**
- HMI: `curl -sk -o /dev/null -w "%{http_code}" https://psi.plant.sanctumsec.com/` should return `401` (unauthenticated request refused — correct behavior).
- Logger: check `journalctl --user -u psi-logger.service -n 20` for "Listening for OSDP events" within the last 30 seconds.

If either unit fails to start, check `journalctl --user -xe` for the error. The most common cause is a stale lock file in `/tmp/psi-*.lock` — remove and retry.

---

## Stopping the system

```bash
systemctl --user stop psi-hmi.service psi-logger.service
```

Stopping the logger means badge events stop reaching the SIEM. The OSDP controller continues operating independently (it is external hardware). Credentials already loaded remain active.

---

## Point map

PSI does not expose Modbus registers. It exposes badge-event data via the HMI API and via Syslog to the SIEM. The "points" are access zones and credential states.

| Zone ID | Zone name | Physical location | Normal activity |
|---|---|---|---|
| 1 | Control Room Anteroom | Outside the main control room | 5–15 badge events per shift |
| 2 | Control Room | Main control room | 3–10 per shift; outgoing rarely exceeds incoming |
| 3 | Maintenance Corridor | L2 equipment access | High during maintenance windows; near zero at other times |
| 4 | Vital Area | Restricted L1 access | 0–2 per shift; any after-hours event is notable |

Credential IDs follow the pattern `[role-prefix]-[nn]`. Known prefixes: `op-` (operators), `sup-` (supervisors), `maint-` (maintenance), `vendor-` (contractors), `er-` (emergency response). The full credential table is in `/home/psi/data/hr_credentials.csv`.

---

## What normal looks like

A normal 8-hour shift (day shift, 06:00–14:00 MT) produces:

- 8–25 badge events across zones 1–3
- 0–2 zone 4 events (supervisor check-ins only)
- 0 denied events (if maintenance has correct credentials for their window)
- 2 auth failures on the HMI from the course status probe (User-Agent: `CS581-StatusProbe/1.0`) — this is expected and normal

Denial events during non-maintenance periods: investigate. Zone 4 events after 18:00 MT with no declared maintenance: investigate.

The SIEM receives a Syslog line for every badge event within about 2 seconds of the event. If the SIEM shows no PSI events for more than 10 minutes and the plant is operating, check whether `psi-logger.service` is still running.

---

## Known peer connections

| Peer system | Direction | Protocol / port | Notes |
|---|---|---|---|
| OT-SIEM | PSI → SIEM | Syslog / UDP loopback | All badge events forwarded. Format: RFC 5424 with custom structured data for zone and credential. |
| DCS | PSI → DCS | TCP loopback, DCS port 5050 | Door-state alarm signals (zone 4 open = alarm). Format is undocumented on the DCS side — do not break this path until you confirm with the DCS operator what they expect. |
| OSDP controller | PSI ↔ controller | Serial RS-485 on /dev/ttyS0 | Badge reads flow from controller to `psi`. Credential writes flow from `psi` to controller via `psi/import_credentials.py`. |

---

## SIEM and monitoring

All badge events reach the OT-SIEM via Syslog within ~2 seconds.

HMI actions (access grants, revocations, login attempts) are logged by the HMI service to a local file (`/home/psi/logs/hmi-audit.log`) AND forwarded to the SIEM as `event_type: hmi.*` events. The SIEM shows `identity: operator` for all HMI events — this is a known limitation, not a configuration error.

**Known monitoring gap:** The credential import path (serial writes from `import_credentials.py` to the OSDP controller) generates no SIEM event. If credentials are changed via the import script, the only record is the local log at `/home/psi/logs/import-audit.log`. Check this file if you suspect unauthorized credential changes. The Cybersecurity Manager is supposed to review it weekly.

---

## What to do if something looks wrong

**Zone 4 event outside business hours:**
1. Log the time, credential ID, and zone from the SIEM.
2. Check `/home/psi/logs/hmi-audit.log` for any recent access grants to that credential.
3. Check `/home/psi/logs/import-audit.log` for recent import runs.
4. Report to the Cybersecurity Manager before taking any action.
5. Do not revoke the credential without authorization — doing so could lock out someone in a legitimate emergency.

**HMI not responding (no 401 on curl check):**
1. Check `systemctl --user status psi-hmi.service`.
2. If failed: `journalctl --user -u psi-hmi.service -n 50` to find the error.
3. Look for stale lock files: `ls /tmp/psi-*.lock`.
4. Restart: `systemctl --user restart psi-hmi.service`.

**SIEM shows no PSI events for more than 10 minutes:**
1. Check `systemctl --user status psi-logger.service`.
2. Badge events may still be happening at the physical controller — this is a logging failure, not a physical security failure.
3. Restart: `systemctl --user restart psi-logger.service`.
4. If the logger was down during an event you care about, check the OSDP controller's local event buffer directly (serial interface, command documented in `/home/psi/docs/osdp-commands.md`).

---

## W4 attack findings summary (for the person taking over)

Three attacks were run against this system in W4. Know these before W5:

1. **Insider (HMI access grant):** Any authenticated HMI session can grant Vital Area access, regardless of role. The mechanism does not enforce the policy. If you see an unexpected zone 4 grant event, it could have come from any HMI session, including a low-privilege one.

2. **Supply chain (credential import):** The import script runs with no SIEM logging of what it writes to the controller. A modified CSV can add credentials silently. Check `/home/psi/logs/import-audit.log` if anything unexpected appears in the credential table.

3. **Pivot from PSI to RMS:** A script on the `psi` account can write Modbus registers on any other system on the host. During W4 this was used to write a false normal reading to RMS register 3. The SIEM will show a `protocol.modbus` event on RMS with `identity: PSI` — that is the signal. If you see that event type on any system and the source is PSI, it is not expected behavior.
