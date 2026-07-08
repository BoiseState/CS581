# Layer 3 — Role Rotation: Plant Cybersecurity Manager
## Anderson Ch. 1–2 + RG 5.71 + NEI 08-09 through the lens of a plant cybersecurity manager

**Prompt used:**
> You are the cybersecurity manager at a large US nuclear power plant. You are responsible for implementing and maintaining the facility's NRC-approved Cyber Security Program. Re-read the following material — Anderson's Security Engineering Chapters 1–2, NRC Regulatory Guide 5.71 Sections 1–3, and the NEI 08-09 Executive Summary — and take notes on: (1) what is actually useful for your day-to-day job, (2) where the frameworks assume freedoms you don't have, and (3) what you wish the authors understood about your operating environment that they clearly don't.

---

## What is actually useful

**Anderson Ch. 1 — the economics argument:**
This is useful precisely because I can use it with my plant management and CFO. Security investment is hard to justify when nothing has gone wrong. Anderson's framing — that attackers optimize for cost, so your job is to make yourself more expensive to attack than the next target — gives me a risk-based argument for budget that doesn't depend on predicting specific incidents. "We need to raise the attacker's cost" is a more defensible ask than "we might get hacked."

**Anderson Ch. 2 — the psychology argument:**
Immediately useful for insider threat thinking. The cognitive bias framework explains patterns I've seen in my workforce — not bad people, but people making predictable decisions under pressure. The specific insight about usability workarounds is something I deal with every outage: operators creating unofficial procedures that bypass security controls because the official procedure takes too long during a time-critical evolution. Anderson's framing helps me explain to plant management why this happens and why fixing it requires redesigning the procedure, not disciplining the operator.

**RG 5.71 — defensive architecture:**
The network separation requirements are the most implementable part of the framework. I can build a defensible architecture around them. The challenge is that "separation" is not binary — there are always legitimate data flows between levels (historians, maintenance connections, vendor remote access) that require controls rather than hard separation.

**NEI 08-09:**
The implementation detail is genuinely useful, but it was written in 2010 and the threat landscape has changed. The document's treatment of supply chain is thin by current standards. I use it as a baseline and supplement with NIST CSF and ICS-CERT guidance.

---

## Where the frameworks assume freedoms I don't have

1. **The "redesign the system" assumption.** Anderson's most common recommendation is to build security in from the start — or to redesign systems that can't be secured as-is. I cannot redesign a reactor protection system from 1983. I cannot take a safety system offline to patch it. My attack surface is largely fixed by the installed base, and modifying it requires an engineering change process that can take months and requires NRC notification if it affects a safety function. "Reduce your attack surface" is good advice that I have approximately 15% of the freedom to implement.

2. **The availability assumption.** The CIA triad treats availability as one of three equal properties. In my environment, availability of safety systems is non-negotiable — it supersedes confidentiality and, in some interpretations, integrity. A cybersecurity control that could impair the availability of a safety function cannot be implemented, period. This fundamentally changes which controls I can deploy.

3. **The patch cadence assumption.** Standard IT security assumes you can patch systems on a regular cycle. In my environment, patching a control system requires testing in a qualified test environment, an engineering change, possible NRC notification, and often can only be done during a scheduled outage (which happens every 18–24 months). When a critical vulnerability is published, I have to assess risk against a patching timeline that might be 18 months away.

4. **The vendor access assumption.** NEI 08-09 acknowledges vendor remote access as a control area. What it doesn't capture is how deeply embedded vendor access is in plant operations. For some digital control systems, the OEM has remote diagnostic capability that is a contractual requirement and that the plant cannot unilaterally terminate without voiding maintenance agreements. My "attack surface" includes connections I don't fully control.

---

## What I wish the authors understood

1. **The security-safety interface is the hardest problem and neither document addresses it adequately.** When a cybersecurity control and a safety requirement point in opposite directions, safety wins. Always. The question is who makes that call in real time, and what documentation is required. The regulatory framework assumes these conflicts have been pre-resolved in the Cyber Security Plan. They haven't — because you can't anticipate every scenario in advance.

2. **My workforce is highly competent in the physical security domain and has a documented culture of compliance.** They are not cavalier about security. But they were trained for a physical threat model, and cyber threats are cognitively foreign to them in a way that Anderson's framework doesn't help me address. A chapter on how to retrain a workforce whose mental model of "secure" means badge in, badge out would be more useful than another taxonomy of cognitive biases.

3. **The inspection process creates perverse incentives.** I optimize my Cyber Security Program to pass an NRC inspection. That is not the same as optimizing it to defend against an adversary. Anderson understands that compliance and security are not the same thing. The regulatory framework does not create strong incentives to exceed compliance requirements. My budget is finite and my inspection timeline is fixed.

4. **The threat has changed faster than the framework.** RG 5.71 was written before Stuxnet was public knowledge, before nation-state ICS targeting was documented at the scale it is now, before supply chain attacks became a primary vector. I am implementing a 2010 framework against a 2026 threat. The framework gives me a foundation, not a complete defense.
