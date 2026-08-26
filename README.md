```
    ███╗   ██╗██╗   ██╗ ██████╗██╗     ███████╗ █████╗ ██████╗
    ████╗  ██║██║   ██║██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗
    ██╔██╗ ██║██║   ██║██║     ██║     █████╗  ███████║██████╔╝
    ██║╚██╗██║██║   ██║██║     ██║     ██╔══╝  ██╔══██║██╔══██╗
    ██║ ╚████║╚██████╔╝╚██████╗███████╗███████╗██║  ██║██║  ██║
    ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

              ██████╗██╗   ██╗██████╗ ███████╗██████╗
             ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
             ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
             ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
             ╚██████╗   ██║   ██████╔╝███████╗██║  ██║
              ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝

        S E C U R I T Y   F O R   C Y B E R - P H Y S I C A L
                &   N U C L E A R   S Y S T E M S
```

# CS 581 — Nuclear Cybersecurity

**Boise State University · Fall 2026 · 3 Credit Hours**  
Department of Computer Science · College of Engineering  
Instructor: Christopher Spirito

> *Security is not a product, but a process — and for nuclear systems, that process never stops.*

---

## What This Repo Is

This is the **course materials repository** for CS 581. It contains reference materials, example artifacts, and the interactive plant architecture diagram used throughout the semester.

**This is not a submission target.** Your work goes in the two repositories you create in Week 1. This repo is read-only reference material.

- <a href="https://boisestatecanvas.instructure.com/courses/48925" target="_blank" rel="noopener">Canvas Course</a> — assignments, rubrics, announcements, grades
- <a href="https://boisestate.github.io/CS581/plant-architecture.html" target="_blank" rel="noopener">Plant Architecture Diagram</a> — interactive 11-system nuclear plant map (live)

---

## Course Structure

Nine workshops across 16 weeks, each anchored to a system from the nuclear plant architecture. Students select one system as their primary target in Week 1 and apply each subsequent workshop to a system from a sequencing plan they build themselves — all 11 systems must appear across the semester.

| Module | Week | Workshop Theme | Workshop Due |
|---|---|---|---|
| M1 — Foundations | 1–2 | Attack Surface Mapping · System Selection | Sep 8 |
| M2 — Threat Landscape | 3–4 | Adversary Profiling & Threat Modeling | Sep 21 |
| M3 — Technical Core I | 5–6 | Protocol Security & Access Control | Oct 5 |
| M4 — Technical Core II | 7 | ICS/SCADA & Digital I&C Security | Oct 12 |
| M5 — Nuclear Context | 8–9 | Physical Protection & Regulatory Frameworks | Oct 26 |
| **Midterm** | 10 | Personalized incident response scenario (72-hour window) | Nov 2 |
| M6 — Defense & Detection | 11–12 | Monitoring Strategy & Supply Chain Security | Nov 16 |
| M7 — Incident Response | 13 | IR in Nuclear Environments | Nov 30 |
| M8 — Advanced & Emerging | 14–15 | Side Channels · AI & SMRs · Emerging Threats | Dec 7 |
| M9 — Capstone | 16 | Ethics, Policy & Portfolio Synthesis | Dec 14 |
| **Ethics Paper** | — | Personalized ethical dilemma (10-day window, issued ~Dec 8) | Dec 18 |
| **Portfolio Capstone** | — | Integrated executive-level security assessment | Dec 18 |

---

## The 11 Nuclear Plant Systems

Students select from this architecture in Week 1. All 11 systems must appear in the portfolio by the end of the semester.

| System | Abbrev | Purdue Zone | Safety Classification |
|---|---|---|---|
| Reactor Protection System | RPS | Level 1 | Safety-critical CDA |
| Digital Control System | DCS | Level 2 | Safety-related CDA |
| Turbine Control System | TCS | Level 2 | Balance-of-plant CDA |
| Spent Fuel Pool Cooling Monitor | SFPCM | Level 1–2 | Safety-related CDA |
| Emergency Diesel Generator Control | EDGC | Level 1 | Safety-related CDA |
| Radiation Monitoring System | RMS | Level 2 | Safety / Safeguards CDA |
| Physical Security Integration | PSI | Level 3–4 | Security CDA |
| Small Modular Reactor I&C | SMR I&C | Level 1–2 | Safety-critical (emerging) |
| Plant Process Computer / Historian | PPC | Level 3 | Non-safety support |
| OT Security Information & Event Mgmt | OT-SIEM | Level 3 | Security monitoring |
| ICT Security Information & Event Mgmt | ICT-SIEM | Level 4 | Corporate security |

---

## Repo Contents

```
/
├── syllabus.tex              # LaTeX source
├── syllabus.pdf              # Current syllabus (also in Canvas Files)
├── curriculum.md             # Full week-by-week curriculum with readings, roles, KSAs
├── coding-agents-companion.tex / .pdf   # AI tool guidance document
├── plant-architecture.html   # Interactive SVG diagram (served via GitHub Pages)
└── example-student-work/
    └── workshops/
        └── week-01/          # Jordan Reyes — complete W1 submission
            ├── README.md     # Student persona and context
            ├── system-selection.md
            ├── sequencing-plan.md
            ├── attack-surface-map.md
            ├── session-log.md
            └── tool-selection.json
```

---

## Grade Structure

| Component | Points |
|---|---|
| Workshop 1 (System Selection, Sequencing Plan & Attack Surface Map) | 60 |
| Workshops W2–W9 (8 × 30 pts) | 240 |
| Midterm Scenario Exercise | 100 |
| Ethics Paper | 150 |
| Portfolio Capstone | 250 |
| Participation | 100 |
| Practitioner Engagement | 100 |
| **Total** | **1000** |

---

## Key Regulatory References

- **10 CFR 73.54** — NRC cybersecurity rule for nuclear power reactors
- **10 CFR 50** — Domestic licensing of production and utilization facilities
- **RG 5.71** — NRC Regulatory Guide: Cyber Security Programs for Nuclear Facilities
- **NEI 08-09 Rev. 6** — Cyber Security Plan for Nuclear Power Reactors
- **NIST SP 800-82r3** — Guide to Operational Technology (OT) Security
- **IAEA Nuclear Security Series** — Physical protection and cybersecurity guidance
