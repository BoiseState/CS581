# CS 581 — Nuclear Cybersecurity
## Security for Cyber-Physical & Nuclear Systems
### Boise State University · Fall 2026
### Christopher Spirito · cspirito@boisestate.edu · chris.spirito@gmail.com
### Office Hours: Monday & Wednesday 5–7pm MT · By Request/Appointment
**Location:** Online – Canvas | **Format:** Asynchronous

---

## Course Description

Security is paramount to creating software and systems that operate in high-consequence environments. This course introduces the fundamentals of cybersecurity and security engineering through the lens of the nuclear industry — one of the most regulated, adversarially targeted, and safety-critical sectors in the world.

A defining feature of this course is that **students will use Claude Code as their primary research and analysis tool throughout the entire semester.** Every module, workshop, and assessment is designed around AI-assisted security work — reflecting how practitioners increasingly operate in the field. Students will learn not only how to think about nuclear cybersecurity, but how to work effectively alongside AI tools to research, model threats, analyze systems, and produce professional-grade security artifacts.

---

## Learning Objectives

By the end of this course, students will be able to:

1. Explain the unique cybersecurity challenges of nuclear and safety-critical systems
2. Identify and model threat actors relevant to nuclear facilities and command/control infrastructure
3. Apply security engineering principles (access control, cryptography, defense-in-depth) to ICS/SCADA environments
4. Use Claude Code to conduct structured security research, threat modeling, and vulnerability analysis
5. Analyze regulatory frameworks (NRC 10 CFR 73.54, NEI 08-09, NIST SP 800-82) and map them to real systems
6. Produce professional-quality security assessments, policy analyses, and threat models
7. Reason critically about the ethics of offensive knowledge and AI use in high-stakes security contexts

---

## Required Text

**Security Engineering** — Ross Anderson (2nd and 3rd ed.)
Free chapters: https://www.cl.cam.ac.uk/~rja14/book.html

Additional nuclear-sector readings and primary sources assigned per module (NRC documents, IAEA guidance, academic papers).

---

## The Claude Code Requirement

**Every student must have access to Claude Code for the duration of this course.**

Claude Code is the primary tool for all workshops, assignments, and assessments. This is intentional: nuclear cybersecurity practitioners work with AI-assisted analysis tools, and this course prepares you for that reality. You will use Claude Code to:

- Research and synthesize technical topics
- Build and iterate on threat models
- Analyze security frameworks and regulatory documents
- Draft and refine security assessments
- Explore and explain attack techniques in sandboxed contexts
- Complete open-context exams

**All Claude Code session logs must be submitted with assignments** as evidence of your AI-assisted workflow. You are evaluated not just on the output, but on how effectively you used the tool to get there.

---

## Course Modules & Workshops

The course runs 16 weeks. Each module includes: pre-recorded lecture(s), assigned readings, and a Claude Code workshop that is the primary graded deliverable.

---

### MODULE 1 — Orientation: Security Fundamentals & Claude Code Setup (Weeks 1–2)

**Topics:**
- What is security engineering? The CIA triad in nuclear context
- Threat surfaces: IT vs. OT vs. nuclear-specific systems
- Setting up and orienting to Claude Code as a security research tool

**Workshop 1:** Use Claude Code to produce a structured overview of the attack surface of a generic nuclear power plant. Include IT, OT, and physical layers. Submit your session log and a 1-page synthesis.

---

### MODULE 2 — Threat Actors & Adversary Psychology (Weeks 3–4)

**Topics:**
- Adversary taxonomy: nation-states, insiders, hacktivists, criminal groups
- Psychology of security: cognitive biases, social engineering, trust
- Case studies: Stuxnet, DPRK targeting of nuclear infrastructure, insider incidents

**Workshop 2:** Use Claude Code to build a structured adversary profile for a nation-state actor targeting a U.S. nuclear facility. Include motivation, capability, likely TTPs, and historical precedent. Submit session log + profile document.

---

### MODULE 3 — Cryptography & Protocol Security (Weeks 5–6)

**Topics:**
- Applied cryptography fundamentals (symmetric, asymmetric, hashing)
- Protocol security: where cryptography is absent or misapplied in ICS/SCADA
- Modbus, DNP3, and other legacy industrial protocols

**Workshop 3:** Use Claude Code to analyze the security properties (or lack thereof) of DNP3 or Modbus. Identify specific weaknesses, known exploits, and what a secure-by-design replacement would look like. Submit session log + analysis.

---

### MODULE 4 — Access Control & Identity in Nuclear Environments (Week 7)

**Topics:**
- Access control models: DAC, MAC, RBAC, ABAC
- Authentication in air-gapped and high-assurance environments
- The Purdue Model and zone/conduit architecture

**Workshop 4:** Use Claude Code to design an access control policy for a nuclear plant's digital control system, mapping roles to permissions within a Purdue Model zone architecture. Submit session log + policy document.

---

### MODULE 5 — Economics of Security (Week 8)

**Topics:**
- Cost-benefit analysis of security investments
- Regulatory compliance vs. genuine risk reduction
- Incentive structures in nuclear operators, vendors, and regulators

**Workshop 5:** Use Claude Code to analyze the economics of a specific security control (e.g., network segmentation, software supply chain verification) in the nuclear context — what does it cost, what does it protect against, and who bears the risk if it fails? Submit session log + analysis.

---

### MIDTERM — Claude Code Scenario Exercise (Week 9)

Open-context. Students receive a realistic nuclear facility scenario with an active incident unfolding. Using Claude Code, students must: identify what is happening, characterize the threat actor, recommend immediate response actions, and identify regulatory notification obligations. Submitted as a structured incident report with session log.

**100 points**

---

### MODULE 6 — Physical Protection & Nuclear Security Regulations (Weeks 10–11)

**Topics:**
- Physical protection systems and their intersection with cyber
- NRC 10 CFR 73.54 — cyber requirements for nuclear facilities
- NEI 08-09, IEC 62443, NIST SP 800-82

**Workshop 6:** Use Claude Code to map NRC 10 CFR 73.54 requirements to a specific control system architecture. Identify gaps, compliance risks, and recommended controls. Submit session log + compliance matrix.

---

### MODULE 7 — Monitoring, Metering & Anomaly Detection (Week 12)

**Topics:**
- Continuous monitoring in nuclear environments
- Anomaly detection in ICS/SCADA data streams
- What "normal" looks like — and how adversaries blend in

**Workshop 7:** Use Claude Code to design a monitoring strategy for a nuclear plant's operational technology network. Define what you would log, what anomalies you would alert on, and how you would avoid alert fatigue. Submit session log + monitoring plan.

---

### MODULE 8 — Nuclear Command, Control & Side Channels (Weeks 13–14)

**Topics:**
- Nuclear command and control architecture — cybersecurity implications
- Side-channel attacks: timing, power, electromagnetic, acoustic
- Defense against side-channel exploitation in embedded/safety systems

**Workshop 8:** Use Claude Code to research and explain a specific side-channel attack relevant to a nuclear instrumentation or control component. Describe the attack, the conditions required, and realistic mitigations. Submit session log + technical brief.

---

### MODULE 9 — AI, Autonomy & Emerging Threats in Nuclear Security (Week 15)

**Topics:**
- AI/ML in reactor monitoring and control — security implications
- Autonomous systems and digital twins as attack surfaces
- The role of LLMs in offensive and defensive security operations
- Meta-reflection: what did using Claude Code all semester teach you about AI in security?

**Workshop 9:** Use Claude Code to analyze the security risks of introducing an AI-based anomaly detection system into a nuclear plant's control room. Consider adversarial ML, model poisoning, and the human-machine trust problem. Submit session log + risk assessment.

---

### MODULE 10 — Ethics, Policy & the Responsible Practitioner (Week 16)

**Topics:**
- Ethics of offensive security knowledge in nuclear contexts
- Export control, classification, and what you can/cannot research
- AI ethics in high-consequence systems
- The practitioner's responsibility

**Ethics Paper (due end of Week 16):** A 5–7 page paper addressing: what are the ethical obligations of a nuclear cybersecurity practitioner, and how does the use of AI tools like Claude Code change or complicate those obligations? Must engage with at least 3 primary sources.

---

## Final Exam — Capstone Scenario (Finals Week)

Open-context. A multi-stage nuclear cybersecurity scenario spanning technical analysis, regulatory response, threat attribution, and executive communication. Students use Claude Code throughout and submit a complete incident response package: technical findings, regulatory notification draft, executive summary, and lessons learned.

**150 points**

---

## Assessments

| Component | Points |
|---|---|
| Workshop 1–9 (9 × 30 pts) | 270 |
| Workshop participation & reflection posts | 100 |
| Midterm scenario exercise | 100 |
| Ethics paper | 130 |
| Final capstone scenario | 150 |
| Project & presentation (see below) | 150 |
| **Total** | **900** |

> Note: Total adjusted to 900 to reflect removal of traditional chapter homework. All workshop submissions must include Claude Code session logs.

---

## Semester Project

Students select a real-world nuclear cybersecurity topic and develop a semester-long deliverable using Claude Code. Options include:

- **Threat Model** — Full threat model for a specified nuclear facility type or component
- **Regulatory Gap Analysis** — Comparative analysis of two regulatory frameworks applied to a common scenario
- **Incident Case Study** — Deep technical reconstruction of a known ICS/nuclear cyber incident
- **Security Architecture Proposal** — Design and justify a security architecture for a specific nuclear OT environment

Project proposals due Week 4. Interim check-in Week 10. Final presentation (recorded, async) and written deliverable due Week 15.

---

## Grade Scale

| Points | Grade |
|---|---|
| ≥ 810 | A |
| 720–809 | B |
| 630–719 | C |
| 540–629 | D |
| < 540 | F |

Curves applied only in students' favor. Grades posted on Canvas.

---

## Policies

**Late Work:** 25% per day penalty. Extensions granted for documented circumstances — contact instructor before the deadline.

**Academic Integrity & AI Use:** This course is built around AI assistance — using Claude Code is required, not prohibited. However, you are responsible for everything you submit. Passing off AI output as understanding you don't have defeats the purpose of the course and will be apparent in your session logs and follow-up discussions.

**Ethical Conduct:** You may research and model offensive techniques in this course. Do not attempt to apply any of this knowledge against real systems without explicit written authorization. This applies especially to ICS/SCADA tools and protocols. When in doubt, stop and ask.

**Syllabus Changes:** All deadlines and requirements are subject to change. Students will be notified via Canvas and BSU email.

---

## A Note on Using Claude Code in a Security Course

You are being asked to use an AI assistant to study AI in security, cryptography, threat modeling, and regulatory frameworks — some of the most nuanced and high-stakes domains in computer science. That's intentional.

Part of what you'll learn this semester is where AI tools are genuinely useful (synthesizing regulatory text, drafting threat models, explaining protocols), where they fall short (novel zero-days, classified contexts, current threat intelligence), and how to be a critical consumer of AI-generated security analysis. That judgment is itself a core professional skill.

---

*Last updated: June 14, 2026 — Christopher Spirito (cspirito@boisestate.edu)*
