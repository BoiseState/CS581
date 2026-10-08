# RBAC Policy — Physical Security Integration (PSI)
## CS 581 Workshop 4 | Jordan Reyes | Oct 9, 2026

**System:** Physical Security Integration (PSI)
**Purdue Zone:** Level 3 — enterprise-adjacent, but physically controls access to Level 1–2 areas
**Role account on plant host:** `psi`

---

## Overview

PSI is the plant's badge-access gateway. It runs an OSDP controller that governs which credentials can open doors to secure areas, including the areas where Level 1 and Level 2 systems live. The HMI is a web interface (Basic Auth over HTTPS, port 5080) used to review badge events and grant or revoke access. A serial connection from the `psi` account to the OSDP controller is the only path that actually changes badge permissions.

The policy below is written for what the lab host can actually enforce, not for a hypothetical plant. The honest answer is that this system cannot enforce most of what the seven-role model asks for, because all enforcement bottlenecks through one shared role account.

---

## The Seven Roles

### 1. Plant Operator

**Allowed:** Badge in and out of Level 2 and Level 3 areas during shift. Read badge event history on the HMI.
**Not allowed:** Modify badge credentials. Grant access to other personnel. Read Level 1 area logs.
**Mechanism:** SSH key in `authorized_keys` grants the operator access to the `psi` account. Once on the account, there is no further separation — they can use any tool the account owns, including the serial connection to the OSDP controller. This is a gap (see "What This Policy Cannot Enforce").

### 2. Supervisor

**Allowed:** Everything an Operator is allowed. Grant or revoke badge access to Level 2 and Level 3 areas via the HMI. View full badge event history.
**Not allowed:** Grant access to Level 1 areas (Vital Area). Modify OSDP controller firmware or configuration files.
**Mechanism:** SSH key in `authorized_keys`. Same gap as Operator — no separation on the account beyond what the HMI's Basic Auth session enforces. The HMI does not enforce role-based access on its own endpoints; any authenticated session can hit `/access/grant`.

### 3. Cybersecurity Manager

**Allowed:** Read-only access to HMI logs and badge event records. SSH access for log review.
**Not allowed:** Badge credential changes. Active session on the OSDP controller serial port.
**Mechanism:** SSH key in `authorized_keys`. No read-only enforcement exists on the account; this role's limits are policy, not mechanism.

### 4. Maintenance Technician

**Allowed:** Badge access to Level 2 maintenance areas during scheduled windows only.
**Not allowed:** HMI access. SSH access. Modification of any credential or access rule.
**Mechanism:** A badge credential in the OSDP controller configured by whoever holds the `psi` account with Supervisor intent. No time-window enforcement exists in the current OSDP configuration — the badge is either active or not. Time-limited access would require scripting a cron job to call the serial interface, which is not implemented.

### 5. Vendor / Contractor

**Allowed:** Escorted badge access to specific areas during approved work windows only.
**Not allowed:** Unescorted access. Any system account access. Credential self-modification.
**Mechanism:** Same as Maintenance Technician — a badge credential in the OSDP controller. No escort enforcement in software. Escort compliance is procedural only.

### 6. Emergency Response

**Allowed:** Badge access to all areas including Vital Area during a declared emergency.
**Not allowed:** HMI modification. Credential changes.
**Mechanism:** A standing badge credential in the OSDP controller with Vital Area permission active. This credential is always present and cannot be time-limited by the current controller configuration. During normal operations this is a standing gap.

### 7. IT Administrator

**Allowed:** SSH access to the `psi` account for system maintenance (package updates, log rotation, service restart).
**Not allowed:** OSDP controller changes. Badge credential modifications. HMI operations.
**Mechanism:** SSH key in `authorized_keys`. Same gap as all SSH roles — no technical separation from OSDP serial access once on the account.

---

## Purdue Zone Mapping

PSI sits at Level 3 in the Purdue diagram but its OSDP controller governs physical entry into Level 1 areas. This creates a cross-level control path that does not appear as a network connection on the architecture diagram.

| Role | Purdue Level operated at | Crosses boundary? |
|---|---|---|
| Plant Operator | L3 (HMI) | No network boundary; physical boundary to L1/L2 via badge |
| Supervisor | L3 (HMI) | Grants physical access to L1 via OSDP controller |
| Cybersecurity Manager | L3 (read-only) | No |
| Maintenance Technician | L2 maintenance areas | Physical crossing via badge only |
| Vendor / Contractor | L2 (escorted) | Physical crossing; no network path |
| Emergency Response | L1 and L2 | Physical crossing; standing Vital Area credential |
| IT Administrator | L3 (SSH) | No; but shares account with OSDP serial path |

The host has no zone separation. All eight plant systems bind to 127.0.0.1 on the same machine. The Purdue diagram implies PSI is isolated from L1/L2 network paths, but on this host the `psi` account can reach any port on loopback.

---

## What This Policy Cannot Enforce

1. **No separation between SSH roles once on the account.** Any key in `authorized_keys` reaches the OSDP serial interface. The policy says IT Admins cannot change badge credentials; the mechanism does not agree.

2. **No individual attribution.** The OSDP controller logs badge events by credential ID, not by person. The HMI Basic Auth session logs "operator" as the actor. When multiple keys share the `psi` account, there is no way to reconstruct which person took a specific action.

3. **No time-limited access.** Maintenance Technician and Vendor windows are policy only. A badge credential is either in the OSDP controller or not; removing it at end-of-window requires a manual action.

4. **Emergency Response credential is always live.** A standing Vital Area credential that cannot be scoped to declared emergencies is a permanent gap.

5. **No loopback boundary.** The policy covers network-facing controls, but PSI's account can reach RMS (5060), SFPCM (5020), and every other system on loopback. There is no mechanism that enforces the Purdue diagram's implied isolation.
