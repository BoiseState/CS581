# W1–W9 Sequencing Plan — Jordan Reyes

*Created: Week 1 | Last revised: Week 1*

This plan maps my intended system target to each workshop. All 11 systems must appear at least once across the semester. With 9 workshops, two weeks will pair two systems. I have front-loaded the systems I know least about — I want to encounter RPS and the safety-critical systems while the course material on regulatory frameworks is still fresh (Modules 1–2), not after I have moved on to cryptography.

This plan is not a contract. I expect to revise it at least twice.

---

## Sequencing Table

| Workshop | System(s) | Workshop Theme | Pairing Rationale |
|---|---|---|---|
| W1 | DCS — Digital Control System | Attack surface mapping | Primary affinity; closest to my background; operational core of the plant |
| W2 | TCS — Turbine Control System (revised Sep 9, see log below) | Adversary profile (threat modeling) | Balance-of-plant control reachable from DCS over the Modbus links in my W1 map; gives the adversary profile a pivot path that actually exists |
| W3 | PSI — Physical Security Integration | Protocol security + access control | PSI bridges cyber and physical; natural fit for crypto + access control module |
| W4 | RPS — Reactor Protection System (revised Sep 9, see log below) | RBAC policy + access control | Safety-critical, diode-protected, and the strictest separation-of-duties case on the system list; the access design is the whole analysis |
| W5 | RMS — Radiation Monitoring System | Three-framework incident analysis | RMS sits across Safety/Security/Safeguards simultaneously — ideal for the regulatory triad module |
| W6 | OT-SIEM + ICT-SIEM | Monitoring strategy + supply chain | Natural pair — the two SIEMs only make sense in relation to each other across the air gap; one workshop, two systems |
| W7 | EDGC + SFPCM | Incident response | Emergency Diesel Gen. and Spent Fuel Pool Cooling are both emergency/backup systems; incident response scenarios for both are closely related |
| W8 | PPC — Plant Process Computer | Advanced threats + side channels | Historian as an adversary target; data integrity attacks on process data |
| W9 | SMR I&C — Integrated I&C Platform | Ethics, policy & portfolio synthesis | SMR is the future-looking system; appropriate for the final module on emerging threats and policy |

---

## Coverage Check

| System | Workshop | Status |
|---|---|---|
| DCS | W1 | planned |
| RPS | W2 | planned |
| PSI | W3 | planned |
| TCS | W4 | planned |
| RMS | W5 | planned |
| OT-SIEM | W6 | planned (paired) |
| ICT-SIEM | W6 | planned (paired) |
| EDGC | W7 | planned (paired) |
| SFPCM | W7 | planned (paired) |
| PPC | W8 | planned |
| SMR I&C | W9 | planned |

All 11 systems covered. Two pairing weeks: W6 (both SIEMs) and W7 (both emergency backup systems).

---

## Risks and Uncertainties

- **RPS in W2** — I may not have enough domain knowledge yet for a good threat profile of a safety system. If the W2 material does not give me enough grounding, I will swap RPS and TCS (move RPS to W4, TCS to W2).
- **W6 pair load** — Two SIEMs in one workshop is ambitious. The OT-SIEM/ICT-SIEM analysis is fundamentally about the air gap export, which is a single data flow. I think one workshop can handle it but I may need to narrow the scope.
- **SMR I&C in W9** — The least publicly documented system. I may need more AI search sessions for this one than the others.

---

## Revision Log

| Date | Change | Reason |
|---|---|---|
| 2026-09-09 | W2 changed from RPS to TCS. W4 changed from TCS to RPS. | The `pivot_path` field in the W2 schema asks how an adversary moves from my W1 system to my W2 system. Answering it against my own W1 OT map showed that the DCS-to-RPS path in row 5 is a one-way data diode, outbound telemetry only, so there is no pivot to describe. Row 4 of the same map, the Modbus TCP and serial links to Level 1 devices, is a real path from DCS to balance-of-plant equipment including turbine control. TCS gives me a pivot that exists. RPS moves to W4, where the deliverable is an RBAC policy and the diode is a feature of the access design rather than an obstacle to the analysis. |
