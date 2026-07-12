# Attack Surface Map — Digital Control System (DCS)
## CS 581 Workshop 1 | Jordan Reyes | Sep 8, 2026

**System:** Digital Control System (DCS)  
**Purdue Zone:** Level 2 — Supervisory  
**Regulatory classification:** Critical Digital Asset (CDA) under 10 CFR 73.54  
**Representative implementations:** Westinghouse Ovation, ABB System 800xA, Yokogawa CENTUM VP, Emerson DeltaV

---

## Three-Layer Attack Surface Map

### Layer 1 — IT (Corporate / Level 4)

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| Vendor remote access tunnels | Vendors require periodic remote access for maintenance and updates; typically VPN-gated | Supply chain compromise of vendor credentials; malicious update package; vendor network pivot into plant | No public standard for how nuclear plants authenticate vendor remote sessions under RG 5.71 | `inferred` — RG 5.71 Section 3.1.5 addresses vendor access; specifics are implementation-dependent |
| Corporate Active Directory / identity federation | Enterprise identity system that may share authentication infrastructure with plant engineering workstations | Credential theft from corporate network used to pivot to plant-side accounts; pass-the-hash attacks | The boundary between corporate AD and plant-side identity is not defined in any public document I found | `inferred` — NIST SP 800-82r3 Section 5.2; ICS-CERT Advisory ICSA-21-336-02 |
| OPC-UA gateway to historian (PPC) | Data bridge from DCS to Plant Process Computer; exports process data upward to Level 3 | Historian exploitation used to reverse-engineer DCS process states; malformed OPC-UA packets pushed back into DCS namespace | OPC-UA security profiles (Sign, Sign & Encrypt) are optional — many deployments leave encryption disabled | `documented` — ICS-CERT Advisory ICSA-22-172-06; Dragos Year in Review 2023; NIST SP 800-82r3 |

---

### Layer 2 — OT (Operational Technology / Level 1–2)

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| DCS controller nodes | Execute control logic for reactor coolant flow, feedwater, turbine bypass; deterministic real-time operation | Firmware manipulation; logic injection via engineering workstation; controller DoS causing uncontrolled process deviation | Controller firmware authenticity verification is not mandated under 10 CFR 73.54; vendor-dependent | `documented` — Stuxnet post-mortems (Langner 2011); ICS-CERT ICSA-14-178-01 (Siemens S7 analog); NIST SP 800-82r3 Section 6.2 |
| HMI stations (operator consoles) | Operator interface to DCS process data; alarm management; manual setpoint entry | Malicious HMI update; display manipulation to mask process anomaly from operator (the Stuxnet playbook); keylogger on HMI OS | HMI operating systems in nuclear plants are often Windows versions that are end-of-support; patching is constrained by CDA change control requirements | `documented` — NRC Information Notice 2010-05; ICS-CERT Advisory ICSA-18-240-01; NEI 08-09 Rev. 6 Section 4.3 |
| Engineering workstations (EWS) | Configuration and programming of DCS controllers; only path to modify control logic | Primary lateral movement target — if you own the EWS, you own the ability to push logic to controllers; removable media (USB) is a common initial access vector | EWS are often dual-homed or connected to corporate network for update purposes; this directly contradicts the defense-in-depth architecture | `documented` — ICS-CERT Advisory ICSA-20-051-01; Dragos XENOTIME threat group reporting |
| Modbus TCP / Serial links (Level 1 devices) | Low-level process communication to sensors, actuators, and field devices | Modbus has no authentication; a system on the same network segment can read or write process values; spoofed Modbus writes can send false setpoints | Modbus was designed in 1979 for isolated serial links; its continued use in networked environments is a known unresolved problem across all ICS sectors | `documented` — NIST SP 800-82r3 Section 6.2.4; ICS-CERT Alert ICS-ALERT-11-343-01 |
| Data diode to RPS (outbound only) | One-way information flow: RPS status reads reach DCS but no commands can return; physical enforcement of information boundary | Diode hardware failure or misconfiguration creating bidirectional path; supply chain compromise of diode firmware | Physical data diodes from vendors such as Owl Cyber Defense are considered highly reliable; the threat is implementation error during installation, not the diode technology itself | `inferred` — NRC NUREG/CR-7151 (data diode analysis); Owl Cyber Defense product documentation |

---

### Layer 3 — Physical / Cyber Intersection

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| Control room physical access | DCS operator consoles are in the protected area; physical access controls are the last line of defense | Insider threat: credentialed operator with physical access can take manual actions the DCS cannot log completely; coerced operator | Insider threat detection for operators with legitimate access is addressed in 10 CFR 73.56 (personnel access authorization) but behavioral monitoring in real-time is not standardized | `documented` — NRC NUREG-2058; 10 CFR 73.56; Anderson Ch. 9 (Psychology of Insider Threat) |
| Removable media (USB, maintenance laptops) | Primary vector for introducing malware into air-gapped or semi-isolated DCS networks | Infected USB used during maintenance window; vendor maintenance laptop already compromised before site entry; unauthorized media bypassing controls | Many nuclear sites have USB port controls but enforcement during maintenance windows (when ports must be opened) is operationally difficult | `documented` — Stuxnet (USB vector); ICS-CERT Advisory ICSA-17-164-01; NEI 08-09 Rev. 6 Appendix D |
| DCS cabinet physical access | Controller hardware, I/O modules, and field wiring terminations are in control cabinets in the plant | Direct hardware manipulation: logic card swaps, I/O module substitution, hardware keyloggers on serial links | Physical tamper detection on DCS cabinets is not uniformly required; varies by plant design basis | `inferred` — NRC RG 5.71 Section 4; IAEA NSS No. 17-T (physical protection of digital I&C) |

---

## What This Map Cannot Tell You

This is the section I did not expect to be the most useful part of the exercise.

**What the map does not know:**

1. **Which DCS vendor this plant actually uses.** Ovation, ABB 800xA, Yokogawa CENTUM, and Emerson DeltaV each have distinct vulnerability histories, patch release cycles, and vendor remote access architectures. The threat vectors in Layer 2 apply generally, but the specific CVEs, the specific firmware versions with known issues, and the specific EWS OS versions are all vendor-dependent. Without knowing the vendor, this map is a generic architectural sketch, not a facility assessment.

2. **Whether the OPC-UA gateway has encryption enabled.** The map flags this as a notable gap because many deployments leave it disabled. But a specific plant might have it enabled, which changes the threat model significantly. This is the kind of thing you learn from a site walk-down, not from public sources.

3. **The current patch posture.** Nuclear plants operate under a CDA change management process (NEI 08-09 Section 4.3) that can make patching a multi-month process requiring NRC notification. A plant running a DCS controller on three-year-old firmware is in a different threat position than one that has current patches. This information is not public.

4. **How the insider threat program is actually implemented.** 10 CFR 73.56 requires personnel access authorization programs. What those programs look like operationally — how behavioral anomalies are detected, how access rights are reviewed — varies by plant and is not public.

5. **The actual network topology.** The Purdue model is an idealized reference architecture. Real plants have OT networks that evolved over decades, often with connections and legacy systems that do not fit the model. The data diode to RPS may have a maintenance bypass that is only opened quarterly. The EWS may or may not be on the same VLAN as the historian gateway. None of this is knowable from public documents.

**The honest conclusion:** This map is a starting point for a conversation with a plant cybersecurity manager, not a deliverable to an NRC inspector. It is useful for identifying what questions to ask. It is not sufficient for assessing whether a specific plant is secure.

This is what the "Confidence & Provenance" column is for. Every row where I wrote `inferred` or `theoretical` is a row where a real assessment would need facility-specific information I do not have.
