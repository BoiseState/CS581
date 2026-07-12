# W1–W9 Sequencing Plan — Jordan Reyes

*Created: Week 1 | Last revised: Week 1*

This plan maps my intended system target to each workshop. All 11 systems must appear at least once across the semester. With 9 workshops, two weeks will pair two systems. I have front-loaded the systems I know least about — I want to encounter RPS and the safety-critical systems while the course material on regulatory frameworks is still fresh (Modules 1–2), not after I have moved on to cryptography.

This plan is not a contract. I expect to revise it at least twice.

---

## Sequencing Table

| Workshop | System(s) | Workshop Theme | Pairing Rationale |
|---|---|---|---|
| W1 | DCS — Digital Control System | Attack surface mapping | Primary affinity; closest to my background; operational core of the plant |
| W2 | RPS — Reactor Protection System | Adversary profile (threat modeling) | Safety-critical systems and their adversaries; want to tackle RPS early while regulatory material is current |
| W3 | PSI — Physical Security Integration | Protocol security + access control | PSI bridges cyber and physical; natural fit for crypto + access control module |
| W4 | TCS — Turbine Control System | RBAC policy + access control | Turbine control has clear operator role boundaries; good RBAC case study |
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
