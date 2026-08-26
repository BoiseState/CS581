# Attack Surface Map — Digital Control System (DCS): OT Layer
## CS 581 Workshop 1 | Jordan Reyes | Sep 8, 2026

**System:** Digital Control System (DCS)  
**Purdue Zone:** Level 2 — Supervisory  
**Regulatory classification:** Critical Digital Asset (CDA) under 10 CFR 73.54  
**Representative implementations:** Westinghouse Ovation, ABB System 800xA, Yokogawa CENTUM VP, Emerson DeltaV

---

## Layer 2 — OT (Operational Technology / Level 1–2)

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| DCS controller nodes | Execute control logic for reactor coolant flow, feedwater, turbine bypass; deterministic real-time operation | Firmware manipulation; logic injection via engineering workstation; controller DoS causing uncontrolled process deviation | Controller firmware authenticity verification is not mandated under 10 CFR 73.54; vendor-dependent | `documented` — Stuxnet post-mortems (Langner 2011); ICS-CERT ICSA-14-178-01 (Siemens S7 analog); NIST SP 800-82r3 Section 6.2 |
| HMI stations (operator consoles) | Operator interface to DCS process data; alarm management; manual setpoint entry | Malicious HMI update; display manipulation to mask process anomaly from operator (the Stuxnet playbook); keylogger on HMI OS | HMI operating systems in nuclear plants are often Windows versions that are end-of-support; patching is constrained by CDA change control requirements | `documented` — NRC Information Notice 2010-05; ICS-CERT Advisory ICSA-18-240-01; NEI 08-09 Rev. 6 Section 4.3 |
| Engineering workstations (EWS) | Configuration and programming of DCS controllers; only path to modify control logic | Primary lateral movement target — if you own the EWS, you own the ability to push logic to controllers; removable media (USB) is a common initial access vector | EWS are often dual-homed or connected to corporate network for update purposes; this directly contradicts the defense-in-depth architecture | `documented` — ICS-CERT Advisory ICSA-20-051-01; Dragos XENOTIME threat group reporting |
| Modbus TCP / Serial links (Level 1 devices) | Low-level process communication to sensors, actuators, and field devices | Modbus has no authentication; a system on the same network segment can read or write process values; spoofed Modbus writes can send false setpoints | Modbus was designed in 1979 for isolated serial links; its continued use in networked environments is a known unresolved problem across all ICS sectors | `documented` — NIST SP 800-82r3 Section 6.2.4; ICS-CERT Alert ICS-ALERT-11-343-01 |
| Data diode to RPS (outbound only) | One-way information flow: RPS status reads reach DCS but no commands can return; physical enforcement of information boundary | Diode hardware failure or misconfiguration creating bidirectional path; supply chain compromise of diode firmware | Physical data diodes from vendors such as Owl Cyber Defense are considered highly reliable; the threat is implementation error during installation, not the diode technology itself | `inferred` — NRC NUREG/CR-7151 (data diode analysis); Owl Cyber Defense product documentation |

**Layer summary:** The OT layer is where process control lives. The engineering workstation is the crown jewel: it is the only system with write access to DCS controller logic, and it is also the most likely to have network connections that violate the intended architecture. The Modbus gap is not fixable at the protocol level — the only mitigation is network isolation, which is exactly what the Purdue model is supposed to provide. The data diode to RPS is the most defensively robust element in this layer; the threat there is installation error, not protocol vulnerability.
