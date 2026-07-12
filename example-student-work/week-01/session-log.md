# Session Log — Workshop 1
## Jordan Reyes | Claude Code | Aug 25–Sep 5, 2026

This log documents my AI Coding Assistant sessions for W1 in the order they happened. I am including the dead ends and the mistakes, not just the final prompts that produced good output. The prompting process is what is being graded here, and I want to be honest about what that process actually looked like.

---

## Session 1 — Aug 25 | "The Bad Prompt"

**Duration:** ~45 minutes  
**Outcome:** Almost nothing useful

I opened Claude Code and typed what felt like a reasonable starting prompt:

> *"I'm a graduate student in a nuclear cybersecurity course. Help me build an attack surface map of a nuclear power plant covering IT, OT, and physical layers."*

The response was 600 words of exactly what you'd find in the first three results of a Google search for "nuclear power plant cybersecurity." SCADA systems. Air gaps. Insider threat. Stuxnet. It was not wrong, but it was not useful. It read like a Wikipedia summary written by someone who had read the same Wikipedia summary.

I tried a follow-up:

> *"Be more specific about the OT layer."*

Better, but still generic. It mentioned Modbus and OPC-UA protocols, which I recognized from names but did not actually understand. It mentioned "DCS controllers" without explaining what they controlled or how they communicated with each other.

The problem was clear in retrospect: I was asking a question I did not have enough background to evaluate the answer to. I could not tell good output from mediocre output because I did not know enough yet.

I closed the session and did the assigned reading instead.

---

## Session 2 — Aug 28 | "Reading First"

**Not an AI session — just notes from the readings.**

RG 5.71, Sections 1–3. This took two hours, not the 30 minutes I budgeted.

Key things I learned that I did not know before:
- "Critical Digital Asset" (CDA) is a specific regulatory term. Not all digital systems in a nuclear plant are CDAs — only those that perform safety, security, or emergency preparedness functions. The DCS is a CDA. The employee badge printing system is not.
- The three-tiered defense architecture in RG 5.71 (Tier 1: highest consequence, Tier 3: lowest) maps roughly but not exactly to Purdue model levels. RG 5.71 is about regulatory consequence, not network architecture.
- The "deterministic cyber attack" concept. RG 5.71 asks licensees to assume an adversary with sophisticated cyber capabilities. This is not "someone accidentally clicks a phishing link." This is a planned, coordinated attack by a capable adversary.

NEI 08-09, Executive Summary and Section 1. Twenty minutes.

Key things: NEI 08-09 is the industry's answer to RG 5.71 — how to actually implement a cyber security program. The gap between what the regulator requires and what the industry recommends was immediately visible. RG 5.71 is prescriptive about outcomes. NEI 08-09 is prescriptive about process. These are not the same thing.

Anderson, Chapters 1–2. Two hours.

The psychology chapter (Ch. 2) hit differently after reading the regulatory documents. Anderson talks about how humans systematically underestimate low-probability, high-consequence events. Nuclear regulation exists precisely because of this bias — the NRC does not trust operators to correctly weight the probability of rare events, so it mandates defense in depth regardless of anyone's probability assessment. That is a designed-in response to a known cognitive failure mode. I had not thought about regulation that way before.

After the reading I had a much clearer sense of what I was trying to map and why. I also had specific terminology I could use in prompts.

---

## Session 3 — Sep 1 | "The Better Prompt"

**Duration:** ~2.5 hours  
**Outcome:** The actual attack surface map

Opened Claude Code. Loaded Anderson Ch. 1 and RG 5.71 Sections 1–3 into the context window first. Then:

> *"I'm building a Week 1 attack surface map for a graduate nuclear cybersecurity course. My chosen system is the Digital Control System (DCS), classified as a Critical Digital Asset under 10 CFR 73.54, operating at Purdue Level 2. I've read RG 5.71 Sections 1-3 and NEI 08-09 Section 1.*
>
> *Help me build a structured attack surface map covering three layers: IT/Corporate, OT/Operational, and Physical-Cyber Intersection. For each threat vector, I need a Confidence & Provenance column that labels each finding as 'documented' (specific public source exists), 'inferred' (follows from architecture but no specific incident cited), or 'theoretical' (plausible but no public evidence). Flag anything that requires facility-specific information to assess properly.*
>
> *Start with the OT layer since that's the DCS's primary zone."*

This produced something substantially better. The response identified:
- Engineering workstations as the primary lateral movement target
- The Modbus authentication gap (no authentication by design)
- HMI OS patching constraints under CDA change management
- The OPC-UA historian gateway as an upward-facing attack surface

It also attempted to add a source citation for each finding. Most were correct. One was not.

**The OPC-DA incident:**

The model cited "OPC-DA" (OPC Data Access) as the protocol used for DCS-to-historian communication in modern nuclear plants. I had just read a paragraph in NIST SP 800-82r3 about the transition from OPC-DA to OPC-UA in ICS environments — OPC-UA is the current standard and has replaced OPC-DA in most modern deployments. I caught the error.

I pushed back:

> *"You cited OPC-DA for the DCS-to-historian link. My understanding from NIST SP 800-82r3 is that OPC-UA has largely replaced OPC-DA in modern ICS deployments. Is OPC-DA still common in nuclear plant DCS implementations?"*

Response:

> *"You're correct to push back on this. OPC-UA has substantially replaced OPC-DA in modern DCS implementations, including nuclear. OPC-DA is a 1990s protocol that lacks built-in security features; OPC-UA was specifically designed with security in mind (though its security modes are often not fully enabled in practice). I should have cited OPC-UA. The vulnerability I was describing — unencrypted communication between DCS and historian — applies to OPC-UA with security mode set to 'None,' which is a documented misconfiguration in ICS environments.*
>
> *I will update the map to reference OPC-UA and note that encryption is often disabled in practice. The underlying threat vector is the same; the protocol reference was wrong."*

This exchange is in the tool-selection.json under "limitations." The model made a confident error on a specific technical detail. I caught it because I had done the reading. If I had not done the reading, it would be in my attack surface map.

**Lesson noted and filed.**

---

## Session 4 — Sep 3 | "Filling the Gaps"

**Duration:** ~1.5 hours  
**Outcome:** Physical layer + What This Map Cannot Tell You

I had the IT and OT layers from Session 3. For the physical layer I needed to think about cyber-physical intersections specifically — not just "physical security" in the general sense but the places where physical access creates cyber consequences and vice versa.

> *"Now focus on the Physical/Cyber Intersection layer. I'm specifically interested in the attack vectors that require physical access to enable cyber consequences, or cyber access to enable physical consequences. The DCS controls real-world processes — what happens if an attacker manipulates process setpoints? What physical access enables control system compromise that wouldn't be possible from the network alone?"*

This produced the control room insider threat analysis and the removable media section. The DCS cabinet physical access row was my addition — the model did not spontaneously mention hardware-level manipulation (swapping logic cards, substituting I/O modules). I added it after reading IAEA NSS No. 17-T, which discusses physical protection of digital I&C in a way that made the physical manipulation threat concrete.

**The "What This Map Cannot Tell You" section:**

I asked:

> *"We've built a map based entirely on public sources and generic DCS architecture. What are the things this map fundamentally cannot tell someone assessing the security of a specific nuclear plant? What would a real assessment require that we cannot get from public documents?"*

The model's response was the best thing it produced across four sessions. It listed: vendor-specific vulnerability history, current patch posture, actual network topology versus the Purdue model ideal, and insider threat program implementation details. I expanded and rearranged it, but the structure came from this prompt.

Something clicked in this session that I will try to articulate: the most honest thing in my attack surface map is not the threat vectors. It is the gap analysis. Anyone can make a list of known ICS threats. The value of the exercise is understanding what you do not know and cannot know without facility-specific access. That is the difference between a generic security assessment and a real one.

I did not understand this going into the course. I understand it now.

---

## Session 5 — Sep 5 | "Cleanup and Role Rotation Prep"

**Duration:** ~45 minutes  
**Outcome:** Synthesis note framing

Quick session to ask the model to re-read my attack surface map draft from the NRC Security Inspector perspective:

> *"Read this attack surface map from the perspective of an NRC Security Inspector conducting a 10 CFR 73.54 inspection. What would you flag as incomplete, unverifiable, or potentially inconsistent with the regulatory framework? What questions would you ask the licensee?"*

This produced the framing for my role rotation synthesis note (in the secondary repo). The inspector role asked questions I had not thought to ask: How does the licensee's CDA list map to the components I identified? Has the licensee performed a documented cyber security assessment of the OPC-UA historian connection? Is the data diode installation covered by the 10 CFR 50 Appendix B quality assurance documentation?

These are not questions I can answer from public sources. But knowing what questions an inspector would ask is how I understand what a real assessment would need to include.

---

## Reflection

**What worked:**
- Loading primary sources into context before prompting. Every session where I did this produced better output than Session 1, where I did not.
- Pushing back when something seemed wrong. The OPC-DA error would have been invisible if I had not done the reading first.
- Asking the model what it does not know, not just what it knows. The "What This Map Cannot Tell You" prompt produced better output than almost any other prompt in the process.

**What did not work:**
- Starting with a broad, open-ended prompt (Session 1). The model produces generic output for generic questions.
- Trusting protocol citations without checking them. The model knows that Modbus has no authentication. It is less reliable on which specific protocols are currently in use in which specific contexts.

**What I would do differently:**
- Do the reading before the first AI session, not after. Two hours on RG 5.71 before Session 1 would have made Session 1 useful instead of useless.
- Build a list of specific questions from the reading before opening Claude Code. The best prompts in Sessions 3 and 4 came from specific things I had learned and wanted to explore further, not from open-ended curiosity.

**Time spent:**
- Reading: ~5 hours
- AI sessions: ~5.5 hours
- Writing and editing: ~3 hours
- Total: ~13.5 hours

That is more than I expected for a 30-point assignment. The reading time is not optional — it is what makes the AI sessions productive.
