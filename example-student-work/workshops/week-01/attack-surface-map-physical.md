# Attack Surface Map — Digital Control System (DCS): Physical / Cyber Intersection
## CS 581 Workshop 1 | Jordan Reyes | Sep 8, 2026

**System:** Digital Control System (DCS)  
**Purdue Zone:** Level 2 — Supervisory  
**Regulatory classification:** Critical Digital Asset (CDA) under 10 CFR 73.54  
**Representative implementations:** Westinghouse Ovation, ABB System 800xA, Yokogawa CENTUM VP, Emerson DeltaV

---

## Layer 3 — Physical / Cyber Intersection

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| Control room physical access | DCS operator consoles are in the protected area; physical access controls are the last line of defense | Insider threat: credentialed operator with physical access can take manual actions the DCS cannot log completely; coerced operator | Insider threat detection for operators with legitimate access is addressed in 10 CFR 73.56 (personnel access authorization) but behavioral monitoring in real-time is not standardized | `documented` — NRC NUREG-2058; 10 CFR 73.56; Anderson Ch. 9 (Psychology of Insider Threat) |
| Removable media (USB, maintenance laptops) | Primary vector for introducing malware into air-gapped or semi-isolated DCS networks | Infected USB used during maintenance window; vendor maintenance laptop already compromised before site entry; unauthorized media bypassing controls | Many nuclear sites have USB port controls but enforcement during maintenance windows (when ports must be opened) is operationally difficult | `documented` — Stuxnet (USB vector); ICS-CERT Advisory ICSA-17-164-01; NEI 08-09 Rev. 6 Appendix D |
| DCS cabinet physical access | Controller hardware, I/O modules, and field wiring terminations are in control cabinets in the plant | Direct hardware manipulation: logic card swaps, I/O module substitution, hardware keyloggers on serial links | Physical tamper detection on DCS cabinets is not uniformly required; varies by plant design basis | `inferred` — NRC RG 5.71 Section 4; IAEA NSS No. 17-T (physical protection of digital I&C) |

**Layer summary:** Physical access is the layer where cyber and nuclear security regulation directly overlap. The control room sits inside the protected area governed by 10 CFR 73.55, which means physical security is regulated independently of the cyber program. The removable media vector is where the two programs intersect operationally: a USB brought in during a maintenance outage passes through physical security before it reaches the DCS. The DCS cabinet is the least-discussed surface in the public literature — it is also the hardest to monitor and the most direct path to controller hardware.

---

## What This Map Cannot Tell You

This is the section I did not expect to be the most useful part of the exercise.

1. **Which DCS vendor this plant actually uses.** Ovation, ABB 800xA, Yokogawa CENTUM, and Emerson DeltaV each have distinct vulnerability histories, patch release cycles, and vendor remote access architectures. The threat vectors in Layer 2 apply generally, but the specific CVEs, the specific firmware versions with known issues, and the specific EWS OS versions are all vendor-dependent. Without knowing the vendor, this map is a generic architectural sketch, not a facility assessment.

2. **Whether the OPC-UA gateway has encryption enabled.** The map flags this as a notable gap because many deployments leave it disabled. But a specific plant might have it enabled, which changes the threat model significantly. This is the kind of thing you learn from a site walk-down, not from public sources.

3. **The current patch posture.** Nuclear plants operate under a CDA change management process (NEI 08-09 Section 4.3) that can make patching a multi-month process requiring NRC notification. A plant running a DCS controller on three-year-old firmware is in a different threat position than one that has current patches. This information is not public.

4. **How the insider threat program is actually implemented.** 10 CFR 73.56 requires personnel access authorization programs. What those programs look like operationally — how behavioral anomalies are detected, how access rights are reviewed — varies by plant and is not public.

5. **The actual network topology.** The Purdue model is an idealized reference architecture. Real plants have OT networks that evolved over decades, often with connections and legacy systems that do not fit the model. The data diode to RPS may have a maintenance bypass that is only opened quarterly. The EWS may or may not be on the same VLAN as the historian gateway. None of this is knowable from public documents.

**The honest conclusion:** This map is a starting point for a conversation with a plant cybersecurity manager, not a deliverable to an NRC inspector. It is useful for identifying what questions to ask. It is not sufficient for assessing whether a specific plant is secure.

This is what the "Confidence & Provenance" column is for. Every row where I wrote `inferred` or `theoretical` is a row where a real assessment would need facility-specific information I do not have.
