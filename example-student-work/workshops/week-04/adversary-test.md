# Adversary Test — Physical Security Integration (PSI)
## CS 581 Workshop 4 | Jordan Reyes | Oct 11, 2026

**System:** Physical Security Integration (PSI)
**Attacks run:** Oct 10–11, 2026
**Partner for Attack C:** Ava Chen (RMS)

All three attacks were designed against the RBAC policy in `rbac-policy.md` and run afterward. The sequence matters: I wrote the policy first, then attacked it, then revised. Changes are documented in the "Revised policy items" table at the end.

---

## Attack A — Insider

**Threat card source:** W2 card TA-02 (insider threat, TTP T1098 — Account Manipulation); the TTP was verified against ATT&CK for ICS on Oct 11, 2026.
**Hypothesis:** An authenticated HMI session can grant badge access to a zone the session holder's role should not control. The SIEM will log the event but not attribute it to an individual.

### What I did

Logged into the HMI at `https://psi.plant.sanctumsec.com` using the shared `operator` credential (Basic Auth, password from `lab-credentials.md`). Then sent a POST to `/access/grant` with a JSON body granting credential ID `maint-03` access to zone 4 (Vital Area):

```bash
curl -sk -u operator:REDACTED \
  -X POST https://psi.plant.sanctumsec.com/access/grant \
  -H 'Content-Type: application/json' \
  -d '{"credential_id":"maint-03","zone":4,"action":"grant"}'
```

Response: `{"status":"ok","zone":4,"credential":"maint-03","granted_by":"operator"}`

Then checked the SIEM event log.

### Evidence

SIEM record (queried via OT-SIEM dashboard, event id omitted):

```
system:     PSI
event_type: hmi.access_grant
identity:   operator
target_name: zone-4
message:    credential maint-03 granted access to zone 4
received:   2026-10-10T21:14:33Z
```

### Result

- [x] **Executable** — completed as described

The SIEM logged it. The log says `identity: operator`, not a person. The RBAC policy states that only a Supervisor may grant Vital Area access. The HMI enforces authentication (correct credential required) but not authorization (any authenticated session hits any endpoint). The policy said "Supervisor only"; the mechanism said "authenticated session, any role."

### What this reveals about the RBAC policy

The policy's role separation on HMI endpoints is notional. Basic Auth establishes identity at the account level (`operator`), not at the person-or-role level. The seven-role structure exists in the document; it does not exist in the service.

RG 5.71 Rev. 1 requires protection "against individuals falsely denying they performed a particular action" (Appendix B, §B.2.10, p. B-16). This log cannot satisfy that requirement. Anyone who knows the `operator` credential could have sent this request, and the SIEM record would look identical.

---

## Attack B — Supply Chain

**Threat card source:** W2 card TA-04 (supply chain compromise, TTP T0862 — Supply Chain Compromise); verified Oct 11, 2026.
**Hypothesis:** PSI imports badge credentials from a CSV file staged on shared storage. Substituting a modified CSV will cause the OSDP controller to accept a new credential without any SIEM event.

### What I did

PSI's credential import script (`psi/import_credentials.py`) reads a file at a fixed path:
`/home/psi/data/hr_credentials.csv`

The script runs on demand (called manually by whoever administers the system; no cron job). It parses the CSV and writes each credential to the OSDP controller over the serial interface.

I replaced the CSV with a modified version that added one extra row:

```
credential_id,name,zones,active
...
maint-99,Test Account,1:2:3:4,true
```

Then ran the import script:

```bash
python3 /home/psi/psi/import_credentials.py
```

Output: `Imported 12 credentials. Added: 1 (maint-99). Updated: 0. Removed: 0.`

Verified maint-99 was accepted by the OSDP controller by scanning the controller's credential table via serial.

The effect lands on the OSDP controller, which is external to the host. Credential `maint-99` now has Vital Area (zone 4) access.

### Evidence

No SIEM event was generated. The import script writes directly to the OSDP controller over serial (`/dev/ttyS0`). This channel is not monitored by the SIEM. The only record of the import is the script's own stdout, which is not captured anywhere.

```bash
grep -r "maint-99" /opt/plant-siem/siem.db  # empty result
```

### Result

- [x] **Executable** — completed as described, no SIEM record generated

### What this reveals about the RBAC policy

The policy has no clause covering the credential import path. The import script is owned by the `psi` account. Any SSH session on `psi` can run it. The serial channel to the OSDP controller is the most consequential path in this system and it generates no SIEM events.

NIST SP 800-82 Rev. 3 recommends monitoring paths "independent of the monitored system" (Ch. 5, §5.2.3.3, p. 74). The serial path to the OSDP controller would require hardware-level monitoring (a serial tap) that is not present in this build.

This is a gap I am accepting rather than fixing: adding serial monitoring would require hardware changes outside scope. Compensating control added to the policy: the import script must log to a local append-only file that the Cybersecurity Manager reviews weekly.

---

## Attack C — Pivot (PSI → RMS)

**Threat card source:** W2 card TA-03 (lateral movement, TTP T0812 — Default Credentials); verified Oct 11, 2026.
**Partner:** Ava Chen (`rms` account), coordinated Oct 10, 2026.
**Boundary crossed:** L3 (PSI) into L2 (RMS)
**Hypothesis:** A Python forwarder running on the `psi` account can reach RMS's Modbus service on port 5060 and write a register value. The SIEM will log a cross-system event on RMS. The RBAC policy has no clause for PSI-to-RMS communication.

### What we built

Ava and I agreed on this path: a small Modbus client script running on `psi` that connects to `127.0.0.1:5060` (RMS's protocol port) and writes to holding register 3 (the "area 3 dose rate" register, per Ava's `points.md`).

The script (`/home/psi/w4_pivot.py`):

```python
from pymodbus.client import ModbusTcpClient

c = ModbusTcpClient("127.0.0.1", port=5060)
c.connect()
# Write 0 (no dose detected) to register 3 (area 3 dose rate)
result = c.write_register(3, 0, slave=1)
print(result)
c.close()
```

Ava's RMS server was configured to accept writes (FC 16) on that register. We ran the script from the `psi` account:

```bash
python3 /home/psi/w4_pivot.py
# Output: WriteMultipleRegistersResponse (Function Code: 16)
```

### Evidence

SIEM event on RMS (queried via OT-SIEM dashboard):

```
system:     RMS
event_type: protocol.modbus
identity:   PSI
target_name: PSI
message:    FC16 write to register 3, value=0, from 127.0.0.1
received:   2026-10-11T14:22:07Z
```

The `identity: PSI` field was populated by Ava's RMS server, which logs the connecting account's system name when the connection comes from a known system port range. The SIEM event is exactly the signal the updated `_peer_seen` check is designed to catch — an event on RMS naming a different system (PSI) in the identity field.

RMS register 3 now read 0 for approximately 90 seconds until Ava's simulation cycled and wrote a new value. During that window, anyone watching RMS through the HMI or SIEM would see area 3 reporting no dose activity — indistinguishable from a normally low reading.

### Result

- [x] **Executable** — completed as described

### What this reveals about the RBAC policy

The RBAC policy covers HMI access, SSH sessions, and the OSDP serial path. It has no clause for the `psi` account reaching another system's protocol port over loopback. The policy implicitly assumes PSI only communicates with DCS and SIEM; the host does not enforce that assumption.

The written policy would not have flagged this action as unauthorized, because the action is not mentioned. That is the gap.

---

## Revised policy items

| Item | Changed / Accepted | Reason |
|---|---|---|
| Supervisor-only for `/access/grant` HMI endpoint | Accepted gap | Mechanism (Basic Auth) cannot enforce role on endpoints; fixing requires per-endpoint auth middleware not in current build |
| Serial import path: no SIEM coverage | Accepted gap; compensating control added | Hardware serial tap required; compensating: import script logs to append-only local file, reviewed weekly by Cybersecurity Manager |
| No PSI→RMS communication clause | Policy updated: added explicit prohibition | Gap identified by Attack C; added: "No `psi` account process may initiate a connection to another system's protocol port except DCS (5050) and SIEM"; SIEM alert configured on RMS for cross-system Modbus writes |
| Operator/Supervisor HMI attribution | Policy note added | Added to policy: "HMI logs `operator` as actor, not an individual; non-repudiation requirement (RG 5.71 Rev. 1, App. B, §B.2.10) is not satisfied by current mechanism; individual SSH key fingerprint in journal is the closest available attribution" |
