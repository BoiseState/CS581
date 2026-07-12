# CS 581 — Nuclear Cybersecurity
## Week-by-Week Curriculum

**Boise State University · Fall 2026 · Christopher Spirito**

---

## The Nuclear Triad: Safety, Security, and Safeguards

Before anything else, this course requires you to hold three distinct concepts clearly separate. In most cybersecurity contexts, "security" is the whole problem. In nuclear, it is one of three co-equal frameworks — each with its own regulatory authority, its own institutional home, and its own definition of failure.

**Safety** — preventing accidents; protecting the public, workers, and the environment from radiological releases. Governed by 10 CFR 50 (reactor safety) and enforced by NRC's Office of Nuclear Reactor Regulation (NRR). The reactor protection system (RPS) and emergency core cooling system (ECCS) are safety systems. Safety engineering assumes *random* failures and designs against statistical likelihood.

**Security** — protecting against deliberate malicious acts: sabotage, theft of special nuclear material, radiological dispersal, and cyber attacks. Governed by 10 CFR 73 (physical protection) and 10 CFR 73.54 (cybersecurity), enforced by NRC's Office of Nuclear Security and Incident Response (NSIR). Security engineering assumes an *adversary* who actively seeks out your assumptions and exploits them.

**Safeguards** — nuclear material accountability and the prevention of diversion for weapons purposes. Governed domestically by 10 CFR 74 (material control and accounting, MC&A) and internationally by the IAEA Additional Protocol and Comprehensive Safeguards Agreements. Administered by NRC's Office of Nuclear Material Safety and Safeguards (NMSS) and the IAEA Department of Safeguards. Safeguards engineering assumes a *state-level actor* attempting to divert nuclear material without detection.

**Why this matters for a cyber course:** A single cyber incident can implicate all three frameworks simultaneously. An attacker who compromises a nuclear plant's digital systems could:
- Disable reactor protection → **Safety** event (10 CFR 50.72 notification)
- Defeat physical access controls to enable sabotage → **Security** event (10 CFR 73.71 notification)
- Falsify nuclear material accounting records to mask diversion → **Safeguards** event (10 CFR 74 / IAEA reporting)

Three separate regulatory frameworks. Three separate NRC offices. Potentially different reporting chains, different response authorities, and different definitions of what "resolved" means — triggered by one attack. No other critical infrastructure sector has this coordination problem at this scale. This course will return to the Safety / Security / Safeguards triad repeatedly; keep it in mind as you read.

---

## How This Course Works

Every module has two parallel tracks that produce two distinct portfolio artifacts:

**Primary Repo** — technical security artifacts (threat models, access control policies, compliance matrices, attack surface maps, monitoring plans, incident response packages). This is the engineering portfolio. It answers: *"Can you build things?"*

**Secondary Repo** — multi-lens reading analyses accumulated across 16 weeks. Each module's required reading is analyzed from multiple organizational role perspectives. This answers: *"Can you translate nuclear security material across organizational functions?"* That's the piece that gets you in the room with a DOE policy team or an NRC inspection preparation group.

---

## The Multi-Lens Reading Methodology

Every reading assignment in this course uses the same four-layer structure. Anderson's chapters are dense — the goal is not passive consumption but active, role-aware analysis.

**Layer 1 — Your own read**
Skim the assigned chapter. Mark what surprises you. Write 3–5 bullets: what are the key claims, what assumptions does the author make, what feels incomplete? This is your unassisted reaction and it matters — it is the baseline you will compare everything else against.

**Layer 2 — LLM synthesis**
Load the chapter (or the densest section) into your AI Coding Assistant. Prompt:
> *"You are a senior security engineer taking study notes. Summarize the key technical claims, assumptions, and gaps in this chapter. Flag anything that would read differently in a safety-critical operational environment."*

Compare against your Layer 1 notes. What did you miss? What did the LLM miss or flatten?

**Layer 3 — Role rotation (always exactly 2 roles)**
Same source, two different reader identities drawn from the list below. Each role asks different questions of the same text. Prompt your AI assistant to re-read the material from each role's perspective. The point is not to generate more summary — it is to surface where the perspectives **conflict**, because those conflicts are where the hard operational decisions live.

**Role List:**

*Safety framework roles:*
- Plant Operator
- Reactor Safety Engineer
- Emergency Response Coordinator

*Security framework roles:*
- NRC Security Inspector (10 CFR 73 / 73.54)
- Plant Cybersecurity Manager
- Physical Security Officer
- Insider Threat Investigator

*Safeguards framework roles:*
- IAEA Safeguards Inspector
- Nuclear Materials Accountant (MC&A)

*Cross-cutting roles:*
- ICS/SCADA Engineer
- General Counsel / Compliance Attorney
- DOE Policy Analyst
- Supply Chain Manager
- Nation-State Threat Analyst

Specific roles are assigned per module based on what tensions are most relevant to that week's topic. When two roles from *different frameworks* are assigned, pay particular attention to where their authorities and definitions of failure diverge — that gap is often where the most interesting operational risk lives.

**Layer 4 — Synthesis note (the secondary repo artifact)**
One page maximum. Answer: What did the role rotation reveal that your initial read missed? Where do the two role perspectives diverge, and why does that divergence matter operationally? This is the document you commit to the secondary repo.

---

## A Standing Principle for All Primary Repo Artifacts

> *A polished model table that does not preserve uncertainty and provenance is a liability, not an asset.*

Every structured artifact you commit to your primary repo — attack surface maps, threat models, compliance matrices, monitoring plans — must carry explicit confidence and provenance markers. A finding stated with false precision is worse than no finding at all in a safety-critical context, because it misleads the people who act on it.

**Required provenance levels for all tabular artifacts:**

| Level | Meaning |
|---|---|
| `documented` | Drawn from a specific public incident, advisory, or named primary source — cite it |
| `inferred` | Follows logically from public architectural knowledge but is not tied to a specific incident |
| `theoretical` | Plausible given the architecture but no public evidence exists — flag it as such |

Add a **Confidence & Provenance** column to every structured table you produce. A table that omits this column is incomplete, regardless of the quality of the other columns. This discipline is what separates a professional security assessment from a sophisticated-sounding guess.

---

## Coding Agent Capability Progression

Each module introduces or deepens one capability from the companion document. By Week 16 you will have used all five in a nuclear security context.

| Weeks | Capability Focus |
|---|---|
| 1–2 | Tool evaluation + basic research synthesis |
| 3–4 | Structured output (JSON threat profiles) |
| 5–6 | Function calling (live API/data queries) |
| 7–9 | Vision & multimodal (architecture diagrams, regulatory PDFs) |
| 11–12 | MCP integration (live threat intelligence, CISA advisories) |
| 13–15 | Full stack: all capabilities in combination |
| 16 | Reflection and portfolio synthesis |

---

## Two-Repo Structure

```
primary-repo/
  /workshops/
    /week-01/
      tool-selection.json
      system-selection.md
      sequencing-plan.md
      attack-surface-map.md
      session-log.md
      README.md
    /week-03/ ...
  /project/
  /written/
  README.md

secondary-repo/
  /role-analyses/
    /week-01/
      nrc-regulator.md
      plant-cybersecurity-manager.md
      synthesis.md
    /week-03/ ...
  README.md
```

---

---

## System Selection — Your Portfolio Target

Rather than analyzing a generic nuclear plant, you will choose a specific system from the plant architecture each workshop and apply that week's analysis to it. By Week 14 your portfolio must cover all 11 systems — nine workshops means some weeks deliberately pair two related systems. You plan your own sequencing from Week 1.

### The 11 Systems

| System | Purdue Zone | Type |
|---|---|---|
| RPS — Reactor Protection System | Level 1 | Safety-critical |
| DCS — Digital Control System | Level 2 | Operational |
| TCS — Turbine Control System | Level 1 | Operational / BOP |
| SFPCM — Spent Fuel Pool Cooling & Monitoring | Level 1 | Safety-critical |
| EDGC — Emergency Diesel Generator Control | Level 1 | Safety-critical |
| RMS — Radiation Monitoring System | Level 1–3 | Monitoring |
| PSI — Physical Security Integration | Level 2–3 | Security |
| SMR I&C — Integrated I&C Platform | Level 1–2 | Emerging |
| PPC — Plant Process Computer / Historian | Level 2–3 | Operational |
| OT-SIEM — OT Security Monitoring Platform | Level 3 | Security |
| ICT-SIEM — Enterprise Security Monitoring | Level 4 | Security |

Use the Plant Architecture Diagram (linked in Module 1) to explore each system: clicking a node shows its Purdue zone, interfaces, and workshop affinity ratings (W1–W9, rated Primary / Strong / Applicable). Use those ratings to draft your W1 sequencing plan.

### 11 Systems, 9 Workshops

With 11 systems and 9 workshops, you cannot do one system per week and cover all 11. Some weeks will target two related systems in a single workshop submission. Suggested natural pairings:

- **OT-SIEM + ICT-SIEM** (W6): one workshop, both sides of the air gap separation — the monitoring systems are most meaningful in contrast with each other.
- **RPS + EDGC** (safety systems): both are Level 1 safety-critical and share regulatory treatment under 10 CFR 50 Appendix B.
- **DCS + PPC** (historian feed): the historian reads the DCS data stream — a single workshop on integrity and tampering covers both.

### W1 Sequencing Plan Deliverable

Your Week 1 primary repo includes two additional files:

1. **`system-selection.md`** — which system you chose for W1, its Purdue zone, and a one-paragraph rationale explaining why
2. **`sequencing-plan.md`** — a table mapping W1–W9 to your intended system targets, with a one-sentence justification per week. *By Week 14 all 11 systems must appear at least once.* Your plan is not binding — revisions are allowed but must be documented in the file with a brief explanation.

---

# MODULE 1 — Foundations
### Weeks 1–2 · Phase 1

**Topics:** Computer Security Overview · Psychology of Security · AI Coding Assistant Selection

---

## Required Reading

**Anderson, *Security Engineering* (2nd or 3rd ed.)**
- Chapter 1: *What is Security Engineering?* — CIA triad, threat surfaces, security vs. safety, failure modes
- Chapter 2: *Psychology and Usability* — cognitive biases in security decisions, social engineering, why humans are the attack surface

Both chapters are freely available at [https://www.cl.cam.ac.uk/~rja14/book.html](https://www.cl.cam.ac.uk/~rja14/book.html)

**Supplemental Primary Sources**
1. **NRC Regulatory Guide 5.71** — *Cyber Security Programs for Nuclear Facilities* (2010): Read Sections 1–3 only (Purpose, Applicability, Regulatory Position overview). This is the foundational regulatory document for everything that follows. You are not reading it for detail — you are reading it to understand *why* nuclear cybersecurity has its own regulatory framework separate from NIST/FISMA.
2. **NEI 08-09 Rev. 6** — *Cyber Security Plan for Nuclear Power Reactors* (2010): Executive Summary and Section 1 only. This is the industry's implementation guidance that maps to RG 5.71. Notice where the regulator's language and the industry's language diverge — that divergence will come up repeatedly.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 1:** NRC Regulator · Plant Cybersecurity Manager

These two roles are chosen deliberately. The regulator reads Anderson asking: *"What does this imply for compliance requirements and what can I enforce?"* The plant manager reads it asking: *"How do I implement this in an operational environment where I cannot take the reactor offline to patch a vulnerability?"* This tension — compliance vs. operations — is the central friction of the entire course.

**Deliverable:** One-page synthesis note committed to `/role-analyses/week-01/synthesis.md` in your secondary repo. Required structure:
- What your Layer 1 read surfaced (3–5 bullets)
- What the LLM synthesis added or changed
- Where the NRC Regulator and Plant Cybersecurity Manager perspectives diverged on the same Anderson material
- One operational question the divergence raises that neither Anderson nor the regulatory documents answer

---

## Coding Agent Workshop

### Part A — Tool Selection & Evaluation (ungraded but required)

Before any technical work, you must select and configure your AI Coding Assistant for the semester. Read the companion document (*AI Coding Assistants in This Course*) in full. Then evaluate your chosen tool against the seven capability dimensions using the following structured format:

```json
{
  "tool": "Claude Code",
  "evaluation_date": "YYYY-MM-DD",
  "capabilities": {
    "thinking_and_reasoning": { "supported": true, "notes": "..." },
    "context_length": { "tokens": 200000, "notes": "..." },
    "function_calling": { "supported": true, "notes": "..." },
    "structured_output": { "supported": true, "notes": "..." },
    "vision_multimodal": { "supported": true, "notes": "..." },
    "mcp_integration": { "supported": true, "notes": "..." },
    "provenance_trust": { "provider": "Anthropic", "us_based": true, "notes": "..." }
  },
  "justification": "Why this tool for this course and for your professional context.",
  "limitations": "What this tool cannot do that you will need to work around."
}
```

Commit to `/workshops/week-01/tool-selection.json` in your primary repo.

---

### Part B — Workshop 1: Nuclear Plant Attack Surface Map + System Selection

**The task:** Choose your target system from the Plant Architecture Diagram (linked in Module 1) and produce a structured three-layer attack surface overview of that system. This is also the workshop where you commit your semester sequencing plan — mapping all 11 systems across W1–W9.

**Capability focus:** Research synthesis + structured output. Practice loading large context (the Anderson chapters + your supplemental readings + system-specific public documentation) and prompting for structured, layered output.

**Deliverables committed to `/workshops/week-01/`:**

1. **`system-selection.md`** — which of the 11 systems you chose, its Purdue zone, and a one-paragraph rationale
2. **`sequencing-plan.md`** — table mapping W1–W9 to your intended system targets, one-sentence justification per week. By Week 14 all 11 systems must appear at least once. Some workshops deliberately pair two systems — plan for this.
3. **`attack-surface-map.md`** — three-layer map of your chosen system:

| Layer | Components | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| IT (Corporate) | ... | ... | ... | documented / inferred / theoretical + source |
| OT (Operational Technology) | ... | ... | ... | documented / inferred / theoretical + source |
| Physical / Cyber Intersection | ... | ... | ... | documented / inferred / theoretical + source |

Add a fourth section: **What This Map Cannot Tell You** — what information would you need (that you do not currently have) to turn this from a public-knowledge map into a facility-specific assessment? This section demonstrates analytical honesty and is the mark of a practitioner rather than a student.

**Session log:** Commit your full AI Coding Assistant session log alongside the artifact. The session log is graded independently — it is evidence of your prompting process, not just the output.

**Prompt to get started (adapt as needed):**
> *"I am a graduate student in a nuclear cybersecurity course. My chosen system for Week 1 is [SYSTEM]. Based on publicly available information about this system's architecture and the ICS/SCADA security literature, help me build a structured attack surface map covering IT, OT, and physical/cyber intersection layers. For each layer, identify key components, likely threat vectors, and known security gaps. Use a markdown table format. Flag anything that would require facility-specific knowledge to complete properly."*

---

## KSA Developed — Module 1

**Knowledge**
- Security engineering fundamentals (CIA triad, threat surfaces, failure modes)
- Why human cognition is a security attack surface (Anderson Ch. 2)
- The regulatory framework governing nuclear cybersecurity (RG 5.71, NEI 08-09) and why it exists separately from NIST/FISMA
- The three-layer architecture of a nuclear facility (IT / OT / physical)

**Skills**
- Selecting and evaluating an AI Coding Assistant against professional criteria
- Prompting for structured, layered output (not prose summaries)
- Multi-stakeholder reading: analyzing the same technical material from different organizational roles
- Producing a structured attack surface map from public-domain information

**Abilities**
- Frame a security engineering problem at the system level before diving into components
- Articulate the compliance-vs.-operations tension that drives most real nuclear security decisions
- Produce artifacts that are useful to a technical audience without requiring facility-specific access

---

## Employer Signal

**Primary repo artifact** signals to a hiring manager at INL, a DOE contractor, or an NRC-regulated utility:
> *"This candidate used an AI-assisted workflow to produce a structured, layered attack surface analysis — the same starting artifact required in an NRC 73.54 cyber security program assessment — and was analytically honest about what they did not know."*

**Secondary repo artifact** signals:
> *"This candidate understands that the NRC regulator and the plant cybersecurity manager are reading the same security engineering literature and arriving at different priorities — and can articulate why that divergence creates operational risk."*

---

---

# MODULE 2 — Threat Landscape
### Weeks 3–4 · Phase 2

**Topics:** Opponents & Adversary Taxonomy · Insider Threat

---

## Required Reading

**Anderson, *Security Engineering***
- Chapter 2: *Psychology and Usability* (continued) — social engineering as cognitive exploitation; authority compliance; the insider threat as a psychology problem, not just an access control problem
- Check 3rd edition for the updated chapter on nuclear and utilities threats; 2nd edition readers should supplement with the MITRE and NRC material below

**Supplemental Primary Sources**
1. **MITRE ATT&CK for ICS** — Technique matrix (publicly available at attack.mitre.org/matrices/ics/). Read the full technique list and filter for the energy/nuclear sector. Focus on: Initial Access, Execution, Persistence, and Impact technique categories. This is the closest thing the field has to a standardized adversary behavior taxonomy.
2. **10 CFR 73.56** — *Personnel Access Authorization Requirements for Nuclear Power Plants* (NRC). Sections 1–4. This is the regulatory foundation of insider threat mitigation in nuclear — notice where it addresses behavior vs. where it addresses access.
3. **CISA/FBI/NSA Advisory AA22-083A** — *Tactics, Techniques, and Procedures of Indicted State-Sponsored Russian Cyber Actors Targeting the Energy Sector* (2022, public). A concrete example of how nation-state TTPs map to the ATT&CK for ICS matrix in the energy context.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 2:** Nation-State Threat Analyst · Insider Threat Investigator

These roles are chosen because they represent the two fundamentally different adversary models this course addresses — and they require completely different defensive responses. A nation-state threat analyst reads adversary taxonomy asking: *"Which actors are targeting nuclear, what are their TTPs, and what does historical evidence tell us about their next move?"* An insider threat investigator reads the same material asking: *"What cognitive and organizational conditions create insider risk, and what behavioral indicators would I actually be able to detect?"* These questions rarely appear in the same document, but they must coexist in any serious nuclear security program.

**Deliverable:** One-page synthesis note committed to `/role-analyses/week-02/synthesis.md`.

The divergence to look for: nation-state threat analysts think in terms of external actors, technical TTPs, and attribution. Insider threat investigators think in terms of organizational psychology, behavioral baselines, and the limits of technical detection. The same Anderson chapter on cognitive biases is read by each role through a completely different lens — and the defensive implications are entirely different.

---

## Coding Agent Workshop — Workshop 2: Adversary Profile

**Capability focus:** Structured output — JSON as the primary deliverable format. From this module forward, most primary repo artifacts are structured data, not prose.

**The task:** Use your AI Coding Assistant to produce a structured adversary profile for a nation-state actor targeting a U.S. nuclear facility. Base this entirely on publicly available information. Do not speculate beyond what open-source reporting supports.

**Required JSON schema:**

```json
{
  "actor": "...",
  "also_known_as": ["..."],
  "attributed_to": "...",
  "confidence": "documented | assessed | theoretical",
  "provenance": "cite specific public report",
  "motivation": {
    "primary": "...",
    "secondary": ["..."]
  },
  "capability_tier": "nation-state-tier-1 | nation-state-tier-2 | criminal | hacktivist",
  "nuclear_targeting_evidence": "...",
  "primary_ttps": [
    {
      "tactic": "...",
      "technique": "...",
      "mitre_ics_id": "T0XXX",
      "nuclear_relevance": "...",
      "confidence": "documented | inferred | theoretical"
    }
  ],
  "historical_precedent": ["..."],
  "detection_opportunities": ["..."],
  "gaps_in_public_knowledge": ["..."]
}
```

Note the `gaps_in_public_knowledge` field — this is where you document what attribution claims exist but cannot be verified from open sources. Professional threat intelligence always separates what is known from what is assessed.

**Prompt to get started (adapt as needed):**
> *"I am building a structured threat intelligence profile for a CS 581 nuclear cybersecurity course. Using only publicly available information and named open-source reporting, produce a JSON-formatted adversary profile for [actor name] targeting the nuclear energy sector. Map their known TTPs to MITRE ATT&CK for ICS technique IDs. Include a confidence level and source citation for each claim. Flag anything that is assessed rather than documented."*

**Output file:** `/workshops/week-02/adversary-profile.json` + `/workshops/week-02/session-log.md`

---

## KSA Developed — Module 2

**Knowledge**
- Adversary taxonomy: nation-states, criminal groups, hacktivists, insiders — motivation, capability, and targeting patterns differ for each
- MITRE ATT&CK for ICS as a standardized TTP framework; how to map observed behavior to technique IDs
- Insider threat psychology: the cognitive and organizational conditions that create insider risk; why access controls alone are insufficient
- 10 CFR 73.56 as the regulatory framework for insider mitigation at licensed nuclear facilities

**Skills**
- Structured JSON output as primary deliverable format
- Threat profiling methodology: separating documented from assessed from theoretical claims
- MITRE ATT&CK for ICS navigation and technique mapping
- Differentiating between external and insider threat intelligence requirements

**Abilities**
- Produce a threat profile that a professional threat intelligence team could read and act on
- Distinguish between what open-source reporting supports and what it merely suggests
- Articulate why the same adversary literature requires fundamentally different responses depending on whether the threat is external or insider

---

## Employer Signal

**Primary repo artifact** signals:
> *"This candidate can produce a structured, sourced threat intelligence profile in a format consistent with how national labs and DOE contractors document adversary analysis — and is honest about the limits of public-domain knowledge."*

**Secondary repo artifact** signals:
> *"This candidate understands that nation-state threat analysts and insider threat investigators are reading the same adversary literature and asking different questions — and can articulate why that divergence requires two separate defensive programs."*

---

---

# MODULE 3 — Technical Core: Cryptography & Protocol Security
### Weeks 5–6 · Phase 3

**Topics:** Applied Cryptography · Protocol Security · ICS/SCADA Legacy Protocols (Modbus, DNP3)

---

## Required Reading

**Anderson, *Security Engineering***
- Chapter 5: *Cryptography* — symmetric and asymmetric encryption, hashing, PKI, key management; focus on where each primitive is appropriate and what breaks when it is misapplied
- Chapter 3: *Protocols* — authentication protocols, session management, where cryptographic primitives fail at the protocol level even when the primitives themselves are correct

**Supplemental Primary Sources**
1. **Modbus Application Protocol Specification V1.1b3** (public, modbus.org) — Sections 1–2 (architecture and framing) and the function code table. Read for what is present: a reliable, simple request-response protocol. Read for what is absent: authentication, encryption, session integrity. The absence is the security finding.
2. **DNP3 Secure Authentication Version 5 overview** — summarized in NERC CIP and IEEE Std 1815-2012 supporting materials (publicly available). Contrast with base DNP3: what security properties were added in SA v5, why retrofitting authentication to a legacy protocol is technically and operationally difficult, and why SA v5 adoption remains limited.
3. **ICS-CERT / CISA advisory on a Modbus or DNP3 vulnerability** — search CISA's ICS advisory archive for a current advisory affecting a Modbus- or DNP3-based system. Read the vulnerability description, CVSS score, and recommended mitigations. This grounds the protocol analysis in a real CVE.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 3:** ICS/SCADA Engineer · General Counsel / Compliance Attorney

The ICS/SCADA Engineer reads cryptography and protocol security asking: *"What can I actually implement on a 20-year-old PLC with 64KB of RAM, no patch window, and a vendor who won't support modifications to the firmware?"* The General Counsel reads the same material asking: *"What are our legal and regulatory exposures if we knowingly operate with documented protocol vulnerabilities, and what does 'reasonable security' mean for legacy industrial protocols under NRC regulations?"*

The divergence to look for: the engineer sees a technical constraint problem (limited compute, no patching, legacy protocols). The attorney sees a liability and compliance problem (documented vulnerability + known risk + no remediation = potential enforcement action). The engineer's "this is architecturally impossible to fix" and the attorney's "we need documented compensating controls and a risk acceptance record" are both correct — and together they define the actual decision the organization has to make.

**Deliverable:** `/role-analyses/week-03/synthesis.md`

---

## Coding Agent Workshop — Workshop 3: Protocol Security Analysis

**Capability focus:** Function calling — querying a live external data source (CVE/NVD database) during the session and having the model interpret the results. This is the first workshop where your AI assistant reaches outside its training data.

**The task:** Choose one protocol — Modbus or DNP3. Produce a structured security analysis covering: native security properties (or their absence), known vulnerability patterns, specific CVEs from the NVD, compensating controls, and what a secure-by-design replacement would require.

**Suggested function calling workflow:**
1. Define a tool that queries the NVD API (`https://services.nvd.nist.gov/rest/json/cves/2.0`) for CVEs matching your chosen protocol
2. Have the model invoke the tool, receive the CVE list, and analyze the results against the protocol's architecture
3. For each significant CVE: what architectural property of the protocol enabled this vulnerability? What compensating control addresses it without replacing the protocol?

**Required output structure:**

```
/workshops/week-03/protocol-analysis.md
```

Sections:
1. Protocol overview (what it does, where it is used in nuclear plants)
2. Security properties analysis (CIA triad — what the protocol provides and what it does not)
3. Vulnerability catalog (CVEs retrieved via function call — minimum 3, with confidence & provenance)
4. Compensating controls (what a plant can implement without replacing the protocol)
5. Secure-by-design requirements (what a replacement protocol would need to provide)
6. What this analysis cannot determine without facility-specific information

**Session log:** `/workshops/week-03/session-log.md` — document your function calling setup, what the NVD query returned, and how you evaluated the results.

---

## KSA Developed — Module 3

**Knowledge**
- Applied cryptography fundamentals: symmetric/asymmetric encryption, hashing, PKI, key management
- Why correct cryptographic primitives can fail at the protocol level (authentication gaps, replay attacks, MITM)
- Modbus and DNP3 architecture: what they do, where they are used, what security properties they were not designed to provide
- CVE/CVSS as a vulnerability classification framework; NVD as a data source

**Skills**
- Function calling: defining and invoking external API tools within an AI session
- CVE database querying and result interpretation
- Protocol vulnerability analysis: mapping architectural choices to security consequences
- Compensating control design for systems that cannot be patched or replaced

**Abilities**
- Analyze a legacy protocol's security properties honestly, distinguishing between "no security" and "security through obscurity"
- Produce a vulnerability analysis that separates what the protocol cannot do by design from what specific implementations have gotten wrong
- Articulate the compensating control tradeoff: what it protects, what it does not, and what residual risk remains

---

## Employer Signal

**Primary repo artifact** signals:
> *"This candidate used live API function calling to retrieve and interpret CVE data — the same workflow used in real vulnerability management programs — and produced an analysis that honestly separates architectural limitations from implementation flaws."*

**Secondary repo artifact** signals:
> *"This candidate understands that the ICS engineer's 'we can't patch this' and the general counsel's 'we need documented risk acceptance' are both correct answers to the same protocol vulnerability — and can articulate what that means for organizational decision-making."*

---

---

# MODULE 4 — Technical Core: Access Control & Identity
### Week 7 · Phase 3

**Topics:** Access Control Models · Authentication in High-Assurance Environments · Purdue Model · Zone/Conduit Architecture

---

## Required Reading

**Anderson, *Security Engineering***
- Chapter 4: *Access Control* — DAC, MAC, RBAC, ABAC; the Bell-LaPadula model and its safety-critical implications; access control matrices; separation of duties; the reference monitor concept

**Supplemental Primary Sources**
1. **IEC 62443-3-3** — *System Security Requirements and Security Levels* — read the publicly available NIST and ISA summaries (the standard itself is paywalled). Focus on Security Levels 1–4 and the concept of zones and conduits. This is the international ICS security standard that NRC guidance references.
2. **NIST SP 800-82 Rev. 3** — *Guide to OT Security* — Section 5 (OT Security Controls) and the Purdue Model reference architecture discussion. Freely available from NIST.
3. **NRC RG 5.71 Appendix B** — *Defensive Architecture* — the regulatory version of zone/conduit architecture for licensed nuclear facilities. Read alongside NIST SP 800-82 to see how the regulatory framework instantiates the technical standard.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 4:** Plant Cybersecurity Manager · Physical Security Officer

The Plant Cybersecurity Manager reads access control models asking: *"How do I implement RBAC in an environment where operators may need emergency access to any system during a plant transient — and where a locked-out operator is potentially more dangerous than an unauthorized one?"* The Physical Security Officer reads the same material asking: *"Where does my physical access control system depend on cyber infrastructure, and where does cyber access control depend on physical barriers I'm responsible for maintaining?"*

The divergence to look for: cyber access control and physical access control are often treated as separate programs with separate budgets and separate regulatory authorities (10 CFR 73.54 vs. 10 CFR 73 physical protection). In practice, every electronic badge reader, every networked door lock, and every camera system is a point where these two programs intersect — and that intersection is frequently under-governed.

**Deliverable:** `/role-analyses/week-04/synthesis.md`

---

## Coding Agent Workshop — Workshop 4: Access Control Policy Design

**Capability focus:** Vision and multimodal input — providing a diagram image and having the model analyze it. This is the first workshop where you give the model something other than text.

**The task:** Design a role-based access control (RBAC) policy for a nuclear plant's digital control system, explicitly mapped to Purdue Model zones. Then use a Purdue Model diagram image to annotate where specific access controls apply.

**Part A — RBAC Policy Document:**

Define the following for your access control policy:

| Role | Purdue Zone(s) | Systems Accessible | Authentication Required | Emergency Access Procedure |
|---|---|---|---|---|
| Plant Operator | Level 2 (Control) | HMI, DCS operator console | Badge + PIN | Supervisor override with log |
| ... | ... | ... | ... | ... |

Include roles for: Plant Operator, Control Room Supervisor, Cybersecurity Manager, Maintenance Technician, Vendor/Contractor, Emergency Response, and IT Administrator. For each: what they can access, from where, with what authentication, and what the emergency access procedure is.

**Part B — Diagram Annotation:**

Provide your AI assistant with a Purdue Model diagram image (search for a publicly available one, or sketch one and photograph it). Prompt:
> *"Annotate this Purdue Model diagram to show: (1) which zones each role defined in the attached RBAC policy can access, (2) where zone boundaries require explicit authentication challenges, (3) where the physical/cyber access control intersection points are."*

Review the annotation critically — does it reflect your policy correctly? Note any discrepancies in your session log.

**Output files:**
- `/workshops/week-04/rbac-policy.md`
- `/workshops/week-04/purdue-annotated-description.md` (describe what the model produced and your evaluation of its accuracy)
- `/workshops/week-04/session-log.md`

---

## KSA Developed — Module 4

**Knowledge**
- Access control models: DAC, MAC, RBAC, ABAC — when each is appropriate and what each cannot do
- Bell-LaPadula confidentiality model and its relevance to safety-critical information flows
- Purdue Model zone architecture: Levels 0–4 and the DMZ; what belongs in each zone; why crossing zone boundaries requires explicit controls
- IEC 62443 security levels as a risk-tiered framework; how RG 5.71 Appendix B maps to IEC 62443 concepts
- Authentication options in air-gapped and high-assurance environments; the emergency access problem

**Skills**
- Vision/multimodal input: providing images to an AI assistant and evaluating its analysis
- RBAC policy design for operational technology environments
- Zone/conduit architecture mapping
- Evaluating model output against a diagram for accuracy

**Abilities**
- Design access control that accommodates emergency operational requirements without creating security backdoors
- Articulate where physical and cyber access control intersect and who governs that intersection
- Identify where a Purdue Model zone architecture breaks down in practice (historian servers, vendor access, legacy systems that span zones)

---

## Employer Signal

**Primary repo artifact** signals:
> *"This candidate can design an RBAC policy for a nuclear OT environment that accounts for emergency access requirements — one of the hardest access control problems in the field — and used multimodal AI analysis to validate it against a zone architecture diagram."*

**Secondary repo artifact** signals:
> *"This candidate understands that the plant cybersecurity manager and the physical security officer are governing the same access control points under different regulatory authorities — and that gap is where the risk lives."*

---

---

# MODULE 5 — Nuclear Context: The Regulatory Triad
### Weeks 8–9 · Phase 4

**Topics:** Safety · Security · Safeguards — Three Frameworks, One Adversary · Physical Protection Systems · Nuclear Command & Control · Economics of Security

This module is the conceptual core of the course. Every other module builds technical skills; this one provides the framework for knowing *which regulatory authority governs which consequence* when a cyber incident occurs in a nuclear environment.

---

## Required Reading

**Anderson, *Security Engineering***
- Chapter 8: *Economics of Security* — cost-benefit analysis of security investment; why regulated entities need external pressure to invest in security; incentive structures between operators, vendors, and regulators
- Chapter on physical protection (check edition) — the intersection of physical and electronic security; why physical security assumptions underpin cyber security controls

**Supplemental Primary Sources**
1. **NRC 10 CFR 73.54** (full text) — the cybersecurity authority. Read every section. This is the primary legal obligation for licensed nuclear facilities and the framework everything else in the Security column references.
2. **NEI 08-09 Rev. 6** — *Cyber Security Plan for Nuclear Power Reactors* — Sections 3–5. The industry's implementation framework for 73.54. Read alongside 73.54 to see where regulatory language translates into specific program requirements.
3. **10 CFR 74** — *Material Control and Accounting* — Sections 74.1–74.19 (overview level). The Safeguards regulatory framework. Read alongside 73.54 to understand where the Security and Safeguards frameworks share jurisdiction and where they diverge.
4. **IAEA Nuclear Security Series No. 17** — *Computer Security at Nuclear Facilities* (2011, publicly available from IAEA). The international cybersecurity guidance for nuclear facilities under IAEA safeguards. Contrast with the domestic NRC framework — the goals are similar but the authorities and enforcement mechanisms are entirely different.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 5:** NRC Security Inspector (10 CFR 73.54) · IAEA Safeguards Inspector

This is the first module where roles from different frameworks are deliberately paired. The NRC Security Inspector operates under domestic US law with enforcement authority; the IAEA Safeguards Inspector operates under international treaty with verification (not enforcement) authority. After a major cyber incident at a licensed facility, both may be present — asking different questions, reporting to different authorities, with different definitions of what "resolved" means.

**The central question of this module:** A cyber attacker compromises the digital control systems at a licensed nuclear facility. They disable a safety system, defeat a physical access control, and corrupt material accounting records. Which framework governs the response — and who is in charge?

The answer is: all three simultaneously — Safety (10 CFR 50), Security (10 CFR 73.54), and Safeguards (10 CFR 74 / IAEA) — with different reporting timelines and different definitions of resolved. Map this in your synthesis note.

**Deliverable:** `/role-analyses/week-05/synthesis.md`

---

## Coding Agent Workshop — Workshop 5: Three-Framework Incident Analysis

**Capability focus:** MCP web reader — pulling live NRC regulatory text to extract notification requirements rather than relying on training data or memory. Regulatory documents change; live retrieval ensures accuracy.

**The task:** Given the following scenario, produce a structured three-framework analysis:

*Scenario:* At 2:47 AM, the night shift supervisor at a licensed PWR notices anomalous readings on three reactor coolant system sensors. Investigation reveals that the plant historian server has been compromised. Forensic analysis (in progress) suggests the compromise may have been in place for 14 days. Two safety system displays have shown incorrect readings during that period. Physical access logs show an unscheduled entry to the protected area server room six days ago by a contractor whose access should have been terminated.

**Required output — structured JSON:**

```json
{
  "incident_summary": "...",
  "framework_analysis": {
    "safety": {
      "triggered": true/false,
      "authority": "NRC-NRR / 10 CFR 50",
      "notification_required": true/false,
      "notification_deadline": "...",
      "notification_recipient": "...",
      "regulatory_basis": "10 CFR 50.72(b)(..)",
      "open_questions": ["..."]
    },
    "security": {
      "triggered": true/false,
      "authority": "NRC-NSIR / 10 CFR 73.54",
      "notification_required": true/false,
      "notification_deadline": "...",
      "notification_recipient": "...",
      "regulatory_basis": "10 CFR 73.71",
      "open_questions": ["..."]
    },
    "safeguards": {
      "triggered": true/false,
      "authority": "NRC-NMSS / 10 CFR 74 + IAEA",
      "notification_required": true/false,
      "notification_deadline": "...",
      "notification_recipient": "...",
      "regulatory_basis": "10 CFR 74.XX",
      "open_questions": ["..."]
    }
  },
  "coordination_gaps": ["..."],
  "immediate_actions": ["..."],
  "what_the_frameworks_do_not_resolve": "..."
}
```

Use MCP web reader to retrieve the actual notification timing requirements from NRC.gov before populating the notification fields. Do not rely on memory.

Follow the JSON with a one-page narrative: *What would a single incident coordinator need to know to manage all three notification obligations simultaneously, given that the timelines, recipients, and content requirements differ for each?*

**Output files:**
- `/workshops/week-05/three-framework-analysis.json`
- `/workshops/week-05/coordinator-narrative.md`
- `/workshops/week-05/session-log.md`

**Midterm Scenario Exercise (Week 10):** Open-context nuclear incident scenario. Students receive a realistic facility scenario with an active cyber incident. Using their AI Coding Assistant, they must: identify what is happening, characterize the threat actor, identify which of the three frameworks are implicated and how, recommend immediate response actions, and identify all regulatory notification obligations across frameworks. Submitted as a structured incident report with session log. *(100 points)*

---

## KSA Developed — Module 5

**Knowledge**
- The Safety / Security / Safeguards triad: distinct frameworks, distinct authorities, distinct definitions of "resolved"
- 10 CFR 73.54 as the cybersecurity authority; NEI 08-09 as implementation guidance
- 10 CFR 74 and IAEA safeguards as the MC&A / diversion-prevention framework
- NRC notification requirements across frameworks (10 CFR 50.72, 73.71, 74)
- Economics of security as a framework for understanding why compliance and security diverge
- Physical protection systems and their intersection with cyber controls

**Skills**
- MCP web reader: retrieving live regulatory text for accurate notification requirement extraction
- Three-framework incident mapping: determining which authorities are triggered by a given set of facts
- Structured incident analysis in JSON format
- Regulatory notification drafting

**Abilities**
- Map a cyber incident to its regulatory implications across all three frameworks simultaneously
- Identify where regulatory frameworks overlap, conflict, or leave gaps
- Articulate what a single incident coordinator needs to manage all three notification obligations

---

## Employer Signal

**Primary repo artifact** signals:
> *"This candidate can map a cyber incident to its Safety, Security, and Safeguards regulatory implications simultaneously — and used live regulatory document retrieval to ensure notification requirements were accurate rather than recalled from memory."*

**Secondary repo artifact** signals:
> *"This candidate understands that the NRC Security Inspector and the IAEA Safeguards Inspector are operating under different legal authorities with different definitions of 'resolved' — and can articulate the coordination gap between them."*

---

---

# MODULE 6 — Defense & Detection
### Weeks 11–12 · Phase 5

**Topics:** Monitoring & Anomaly Detection in OT · Supply Chain Security · Consequence-Driven Cyber-Informed Engineering (CCE)

---

## Required Reading

**Anderson, *Security Engineering***
- Chapter on monitoring and intrusion detection (check edition for chapter number) — what monitoring can detect; the base rate problem in anomaly detection; the cost of false positives in operational environments

**Supplemental Primary Sources**
1. **CISA ICS Security Advisory** — select a current advisory (2025–2026) affecting ICS equipment used in the energy or nuclear sector from cisa.gov/ics-advisories. Read: the affected system, the vulnerability description, CVSS score, and recommended mitigations. You will use this in Workshop 6 via MCP.
2. **NIST SP 800-161 Rev. 1** — *Cybersecurity Supply Chain Risk Management Practices* — Sections 1–3 (overview and key practices). Supply chain is the fastest-growing attack surface in ICS security; this is the foundational framework.
3. **INL Consequence-driven Cyber-informed Engineering (CCE) methodology overview** — [direct PDF from INL](https://inl.gov/content/uploads/2023/06/Consequence-driven-Cyber-informed-Engineering.pdf) · [OSTI 1341416](https://www.osti.gov/biblio/1341416). CCE inverts the conventional security approach: start with the worst physical consequences and work backward to the cyber pathways that could cause them. This changes how you prioritize monitoring.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 6:** Emergency Response Coordinator · Supply Chain Manager

The Emergency Response Coordinator reads monitoring and detection asking: *"What do I need to see, and when, to trigger the right response at the right time — and how do I design alerts that avoid the fatigue that causes operators to ignore the alarm that actually matters?"* The Supply Chain Manager reads the same material asking: *"Where in our supply chain are adversaries most likely to introduce compromises that evade our monitoring — and what would detection even look like for a hardware implant introduced at the vendor?"*

The divergence to look for: the Emergency Response Coordinator wants more signal, faster. The Supply Chain Manager knows that some compromise vectors (hardware implants, firmware backdoors introduced at manufacturing) produce no detectable signal at all within the plant's monitoring perimeter. These are not competing views — they define the boundary of what monitoring can and cannot do.

**Deliverable:** `/role-analyses/week-06/synthesis.md`

---

## Coding Agent Workshop — Workshop 6: Monitoring Strategy + Supply Chain Assessment

**Capability focus:** MCP integration — full web search and web reader for live threat intelligence. This is the first workshop where you pull a live external advisory and incorporate it directly into your analysis.

**The task:** Produce a monitoring strategy for a nuclear plant OT network AND a supply chain threat assessment. These are two separate deliverables that should inform each other.

**Part A — Monitoring Strategy:**

Design a monitoring strategy structured around the CCE approach: start with the highest-consequence physical outcomes, identify the cyber pathways that could cause them, and design monitoring to detect activity on those pathways.

Required sections:
1. Consequence-prioritized monitoring targets (top 3 physical consequences → cyber pathways → monitoring points)
2. What to log at each monitoring point (be specific: what data, what format, what retention)
3. Alert thresholds and escalation paths (what triggers an alert vs. a ticket vs. an immediate response)
4. Alert fatigue mitigation (how do you avoid the boy-who-cried-wolf problem in a 24/7 operational environment)
5. What monitoring cannot detect (be honest about the blind spots)

Use MCP web search to retrieve the current CISA advisory you selected in the reading. Have the model assess: does this advisory affect any of the systems in your monitoring strategy? If so, how does it change your alert thresholds?

**Part B — Supply Chain Threat Assessment:**

For the same nuclear plant, produce a supply chain threat assessment covering:
- Top 3 supply chain attack vectors (hardware, software, services) with confidence & provenance
- Detection opportunities for each vector (where monitoring could catch it vs. where it cannot)
- Compensating controls for vectors that evade monitoring

**Output files:**
- `/workshops/week-06/monitoring-strategy.md`
- `/workshops/week-06/supply-chain-assessment.md`
- `/workshops/week-06/session-log.md`

---

## KSA Developed — Module 6

**Knowledge**
- Anomaly detection in ICS/SCADA: what "normal" looks like in OT and how adversaries blend in
- The base rate problem: why high-sensitivity detection in a low-base-rate environment produces mostly false positives
- CCE methodology: consequence-first prioritization vs. vulnerability-first prioritization
- Supply chain attack vectors: hardware implants, malicious firmware updates, compromised software packages, insider at vendor
- NIST SP 800-161 supply chain risk management framework

**Skills**
- MCP web search and reader: live CISA advisory retrieval and integration
- Consequence-driven monitoring strategy design
- Supply chain threat assessment
- Alert threshold and escalation path design

**Abilities**
- Design monitoring that prioritizes the consequences that matter most rather than the vulnerabilities that are most visible
- Articulate the boundary of what monitoring can and cannot detect — particularly for supply chain vectors
- Incorporate live threat intelligence into a static monitoring strategy

---

## Employer Signal

**Primary repo artifact** signals:
> *"This candidate designed a consequence-first monitoring strategy using the CCE methodology — the same approach used by INL and DOE contractors for high-consequence ICS environments — and incorporated a live CISA advisory into the analysis rather than working from static training data."*

**Secondary repo artifact** signals:
> *"This candidate understands that the emergency response coordinator and the supply chain manager are drawing the boundary of what monitoring can and cannot do from opposite directions — and that the gap between them is where the most dangerous supply chain attacks live."*

---

---

# MODULE 7 — Incident Response
### Week 13 · Phase 6

**Topics:** Incident Response in Nuclear Environments · Zimmerman's 10 Rules for Incident Response · NRC Notification Requirements

---

## Required Reading

**Anderson, *Security Engineering***
- Chapter 1 revisited through an IR lens: when security controls fail, what does the failure look like? What evidence survives? What does an attacker erase first? Anderson's failure mode taxonomy becomes an IR checklist when read backward.

**Supplemental Primary Sources**
1. **Zimmerman's 10 Rules for Incident Response** — the primary source document by Chris Zimmerman (Microsoft). Publicly available. Read all 10 rules carefully; they were written for enterprise IT but the tensions they surface are amplified in nuclear OT.
2. **10 CFR 50.72** — *Immediate Notification Requirements for Operating Nuclear Power Reactors*. Read the triggering conditions and timing requirements. This is the Safety framework notification obligation.
3. **10 CFR 73.71** — *Reporting of Safeguards Events*. The Security framework notification obligation. Compare the triggering conditions and timing to 50.72 — they are different, they may be triggered simultaneously, and they report to different recipients.
4. **NIST SP 800-61 Rev. 2** — *Computer Security Incident Handling Guide* — Sections 1–3 (overview and detection/analysis phase). The foundational IT IR framework. Read it to understand what Zimmerman's rules are responding to — and where the nuclear OT context diverges from it.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 7:** Plant Cybersecurity Manager · NRC Security Inspector

The Plant Cybersecurity Manager reads IR through the lens of: *"What do I actually do in the first four hours — preserve evidence, maintain plant operations, notify the NRC on the right timelines, manage my team, and not make the situation worse by taking an action I can't reverse?"* The NRC Security Inspector reads the same material asking: *"What documentation will I need to see to verify this incident was handled properly, and what would tell me the response was inadequate or that the licensee delayed notification?"*

The divergence to look for: the plant manager is operating in real time with incomplete information and competing priorities. The inspector will review the response retrospectively with complete information. Zimmerman's rules were written for the person in the chair during the incident — but every rule has a documentation implication that the inspector will scrutinize later. Those two perspectives must both be held simultaneously during an actual response.

**Deliverable:** `/role-analyses/week-07/synthesis.md`

---

## Coding Agent Workshop — Workshop 7: Zimmerman in Nuclear Context

**Capability focus:** Full MCP stack — web search for current CISA advisories + web reader for live NRC regulatory text, combined in a single session. By this point in the course, MCP integration should be a routine part of your workflow.

**The task:** Apply Zimmerman's 10 Rules for Incident Response to the nuclear operational environment. For each rule, produce a structured analysis covering how the rule applies, where the nuclear context creates constraints or contradictions, and what the notification implications are.

**Required output structure:**

For each of the 10 rules, produce a section with:

```markdown
## Rule [N]: [Rule Name]

**The rule:** [Zimmerman's original statement]

**How it applies in nuclear OT:**
[Where the rule is directly applicable and how it maps to nuclear IR procedures]

**Where the nuclear context creates constraints:**
[What the rule assumes that is not true in a nuclear operational environment — legacy systems, safety primacy, operational continuity requirements, vendor dependencies]

**Notification implications:**
[If applying this rule generates evidence or reveals facts that trigger 10 CFR 50.72 or 73.71 notification, describe the obligation and timeline]

**Confidence & Provenance:**
[documented | inferred | theoretical — source]
```

Use MCP web search to pull a current CISA ICS advisory. For at least two of the 10 rules, demonstrate how the advisory's recommended mitigations interact with (support or complicate) the rule's application in a nuclear environment.

**Output files:**
- `/workshops/week-07/zimmerman-nuclear-application.md`
- `/workshops/week-07/session-log.md`

---

## KSA Developed — Module 7

**Knowledge**
- Zimmerman's 10 Rules for Incident Response and their enterprise IT assumptions
- Where nuclear OT IR differs: legacy systems, safety primacy, operational continuity, regulatory notification obligations
- NRC notification requirements: 10 CFR 50.72 (Safety) and 10 CFR 73.71 (Security) — timing, triggering conditions, recipients
- The tension between evidence preservation and operational continuity in a nuclear plant event
- NIST SP 800-61 incident handling lifecycle as the foundational framework

**Skills**
- Applying general IR principles to domain-specific constraints
- MCP full stack: live advisory retrieval and regulatory text integration in a single session
- NRC notification obligation analysis from incident facts
- IR procedure documentation for regulatory review

**Abilities**
- Apply Zimmerman's rules while simultaneously tracking documentation obligations for post-incident regulatory review
- Identify where an IR action that is correct from a security standpoint may conflict with nuclear operational or safety requirements
- Produce an IR analysis that is useful both to the person in the chair during the incident and to an inspector reviewing it afterward

---

## Employer Signal

**Primary repo artifact** signals:
> *"This candidate applied Zimmerman's IR framework to the nuclear OT context with specific attention to regulatory notification obligations — the kind of analysis that IR teams at NRC-regulated utilities use to prepare their response procedures."*

**Secondary repo artifact** signals:
> *"This candidate understands that the plant cybersecurity manager and the NRC Security Inspector are reading the same incident from fundamentally different temporal positions — one in real time, one retrospectively — and that every IR decision has a documentation consequence."*

---

---

# MODULE 8 — Advanced & Emerging Threats
### Weeks 14–15 · Phase 7

**Topics:** Side-Channel Attacks · AI and Autonomy in Nuclear Systems · Small Modular Reactors (SMRs) · Emerging Attack Surfaces

---

## Required Reading

**Anderson, *Security Engineering***
- Chapter on side channels (check edition for chapter number) — timing attacks, power analysis, electromagnetic emanations, acoustic side channels; what information leaks from physical processes that cryptography cannot protect; Kocher's timing attack as the foundational example

**Supplemental Primary Sources**
1. **A current academic paper on side-channel attacks in embedded or safety-critical systems** — recommended: [O'Flynn & Dewar, "On-Device Power Analysis Across Hardware Security Domains" (TCHES 2019)](https://tches.iacr.org/index.php/TCHES/article/view/8347) — demonstrates power side-channel attack defeating TrustZone-M isolation on ARM Cortex-M microcontrollers using only the device's own on-board ADC (no external equipment). Directly relevant to nuclear safety PLCs. Open access at tches.iacr.org.
2. **INL/NRC report on AI/ML in nuclear operations** — [OSTI 1847070](https://www.osti.gov/biblio/1847070): INL, "Exploring Advanced Computational Tools and Techniques with AI/ML in Operating Nuclear Plants" (NUREG/CR-7294, 2022). Surveys supervised and unsupervised AI/ML algorithms across reactor operations, predictive maintenance, fault diagnosis, and safety assessments. Open access PDF via OSTI.
3. **NRC NUREG-0800 Standard Review Plan, Chapter 7** — *Instrumentation and Controls* (summary sections, publicly available from NRC). This is the regulatory framework for digital I&C in nuclear plants — the same systems where AI is being introduced and where side-channel vulnerabilities are most consequential.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 8:** ICS/SCADA Engineer · DOE Policy Analyst

The ICS/SCADA Engineer reads side-channel and AI threats asking: *"What does this mean for the embedded controllers and instrumentation I am responsible for securing — specifically, what attack vectors exist that are not addressed by my current Cyber Security Plan, and what would detection even look like?"* The DOE Policy Analyst reads the same material asking: *"What policy gaps exist in the current regulatory framework for AI-assisted nuclear operations — where is the NRC's rulemaking behind the technology — and what would it take to address them?"*

The divergence to look for: the engineer sees a technical reality (side-channel attacks against nuclear instrumentation are theoretically feasible and not currently addressed in most Cyber Security Plans). The policy analyst sees a regulatory gap (NRC's digital I&C framework was written before AI, and there is no current rule requiring AI security assessments for licensed facilities). The engineer asks "can we be attacked this way?" The policy analyst asks "what would have to happen for there to be a regulatory requirement to prevent it?"

**Deliverable:** `/role-analyses/week-08/synthesis.md`

---

## Coding Agent Workshop — Workshop 8: Side-Channel Technical Brief

**Capability focus:** Vision and multimodal (hardware diagram analysis) + extended reasoning at maximum effort. Side-channel analysis requires deep technical reasoning; this is where you set your AI assistant to its highest reasoning depth.

**The task:** Choose one side-channel attack type — timing, power analysis (SPA/DPA), electromagnetic (EM), or acoustic — and produce a technical brief analyzing its applicability to a nuclear instrumentation or control component.

**Required structure:**

```
/workshops/week-08/side-channel-brief.md
```

Sections:
1. **Attack mechanism** — how the side channel works; what physical process leaks information; what measurement equipment is required
2. **Applicability to nuclear instrumentation** — which specific component types (safety PLCs, instrumentation microcontrollers, cryptographic modules) are plausibly vulnerable; what conditions are required for a successful attack
3. **Threat actor requirements** — what level of physical access, equipment, and expertise does this attack require? Is this a nation-state capability, a sophisticated insider, or accessible to a less capable actor?
4. **Current mitigations** — what countermeasures exist; which are implemented in nuclear-grade equipment; what the residual risk is
5. **What this analysis cannot determine** — without facility-specific hardware specifications, what remains unknown; what testing methodology would be needed to assess actual vulnerability

**For the vision/multimodal component:** Find or create a simplified block diagram of a nuclear instrumentation system (a publicly available diagram of a safety PLC or I&C architecture). Upload it to your AI assistant and prompt: *"Identify components in this diagram that may be susceptible to [chosen side-channel type] attacks, and explain what physical location an attacker would need to access to mount the attack."*

Document the model's analysis and your evaluation of its accuracy in the session log.

---

## Coding Agent Workshop — Workshop 9: AI in Nuclear Operations Risk Assessment

**Capability focus:** Full stack — all five capabilities used in combination. This is the most complex workshop in the course; use extended thinking at maximum effort throughout.

**The task:** Produce a security risk assessment for introducing an AI-based anomaly detection system into a nuclear plant's control room. This is not a hypothetical future technology — nuclear utilities are actively evaluating and deploying AI monitoring systems, and the NRC is developing guidance on their use.

**Required structure:**

```
/workshops/week-09/ai-nuclear-risk-assessment.md
```

Sections:
1. **System description** — what the AI anomaly detection system does; what data it ingests; what decisions or alerts it produces; what human actions it informs or automates
2. **Adversarial ML threat analysis** — how could an adversary manipulate the model's training data, inputs, or outputs? What would a successful attack look like? (Use function calling to query for recent adversarial ML research applicable to ICS)
3. **Model poisoning scenarios** — what training data sources could be compromised? What would poisoned behavior look like vs. model drift vs. sensor malfunction?
4. **Human-machine trust analysis** — how does an operator calibrate trust in an AI system they did not build and cannot fully explain? What happens when the AI is wrong during a plant event?
5. **Regulatory gap analysis** — what existing NRC guidance addresses AI in nuclear I&C? Where are the gaps? (Use MCP web reader to retrieve current NRC guidance on digital I&C and AI)
6. **Risk summary** — structured JSON with risk ID, description, likelihood, consequence, current controls, residual risk, and confidence & provenance

**Meta-reflection (required final section):** What did using AI coding assistants throughout this semester teach you about AI in security? Where were they genuinely useful? Where did they produce confident-sounding output that required careful verification? This reflection is part of your graded submission.

**Output files:**
- `/workshops/week-09/ai-nuclear-risk-assessment.md`
- `/workshops/week-09/session-log.md`

---

## KSA Developed — Module 8

**Knowledge**
- Side-channel attack taxonomy: timing, power analysis (SPA/DPA), electromagnetic, acoustic; what information each type leaks and from what physical processes
- AI/ML security threats: adversarial ML, model poisoning, training data manipulation, evasion attacks
- SMR digital architecture: how small modular reactors differ from large light-water reactors in their I&C and cybersecurity profiles
- NRC regulatory framework for digital I&C (NUREG-0800 Ch. 7) and where AI creates gaps
- Human-machine trust calibration in high-consequence automated systems

**Skills**
- Vision/multimodal: hardware diagram analysis for side-channel exposure identification
- Extended reasoning at maximum effort for deep technical analysis
- Full AI capability stack deployment in a single complex analysis task
- Adversarial ML threat modeling
- Regulatory gap analysis using live document retrieval

**Abilities**
- Analyze a novel or emerging threat vector with limited public documentation, explicitly marking the boundary of what is known
- Assess AI system security risks without access to the model's architecture or training data
- Articulate regulatory gaps and what policy would need to address them

---

## Employer Signal

**Primary repo artifact** signals:
> *"This candidate produced a side-channel threat brief for nuclear instrumentation and an AI anomaly detection risk assessment — two emerging threat areas that most ICS security practitioners have not analyzed — using a full AI capability stack and was explicit about the limits of public-domain knowledge."*

**Secondary repo artifact** signals:
> *"This candidate understands that the ICS engineer and the DOE policy analyst are looking at the same emerging threats from opposite ends — one asking 'can we be attacked this way' and one asking 'what would it take for there to be a rule preventing it' — and that both questions have to be answered."*

---

---

# MODULE 9 — Capstone: Ethics, Policy & Portfolio Synthesis
### Week 16 · Phase 8

**Topics:** Ethics of Nuclear Cybersecurity Practice · AI Ethics in High-Consequence Systems · Export Control and Classification · Portfolio Completion

---

## Required Reading

**Anderson, *Security Engineering***
- Concluding chapter (check edition) — Anderson's own reflection on what security engineering has become and what it is still failing to do; read as a provocation, not a summary

**Supplemental Primary Sources**
1. **ACM Code of Ethics and Professional Conduct** — Sections 1 and 2 (publicly available at acm.org/code-of-ethics). The foundational professional ethics framework for computing. Read it against the specific context of nuclear cybersecurity — where does it apply cleanly, where does it strain, and where does nuclear context require obligations the ACM code does not address?
2. **NRC Regulatory Issue Summary 2020-08** (or current equivalent) — *Cybersecurity Event Notification* — publicly available from NRC. This is the regulatory framing of what practitioners are legally required to disclose. Read it alongside the ACM code: where does legal disclosure obligation end and ethical obligation begin?
3. **DOE guidance on 10 CFR 810** — *Assistance to Foreign Atomic Energy Activities* — summary level, publicly available from DOE. The export control framework relevant to nuclear cybersecurity knowledge. What you learn in this course may be subject to export control restrictions when shared with non-US persons or entities. Understand the boundary before you reach it.
4. **A current IAEA or NRC document on AI in nuclear safety** — search for the most recent publicly available NRC staff paper or IAEA TECDOC on AI/ML in nuclear safety-related applications. This grounds the AI ethics discussion in the specific regulatory context you have been studying all semester.

---

## Multi-Lens Reading Assignment

**Assigned roles for Module 9:** General Counsel / Compliance Attorney · DOE Policy Analyst

The General Counsel reads ethics through the lens of: *"What are the legal obligations of a nuclear cybersecurity practitioner, and — critically — where does ethical obligation exceed legal obligation? What does a practitioner owe that the law does not require?"* The DOE Policy Analyst reads the same material asking: *"What policy frameworks are currently missing, and what would it take to create them? Where is the gap between what good practitioners do voluntarily and what regulation requires everyone to do?"*

The divergence to look for: law establishes a floor, not a ceiling. The attorney identifies the floor (legal disclosure obligations, export control rules, regulatory reporting requirements). The policy analyst identifies the gap between the floor and where good practice actually sits — and argues for raising the floor. A nuclear cybersecurity practitioner who meets only legal minimums may still be acting unethically in ways that create risk.

**Deliverable:** `/role-analyses/week-09/synthesis.md` — this is the final secondary repo artifact. Your synthesis should reflect on the entire semester's role rotation work: which divergences recurred across multiple modules, and what do they collectively say about the organizational and regulatory structure of nuclear cybersecurity?

---

## Ethics Paper

**Due:** End of Week 16 · **5–7 pages** · **Minimum 3 primary sources**

**Prompt:** What are the ethical obligations of a nuclear cybersecurity practitioner, and how does the use of AI tools change or complicate those obligations?

Your paper must engage with:
1. At least one obligation the ACM Code of Ethics establishes that applies directly to nuclear cybersecurity practice
2. At least one obligation that nuclear context creates that the ACM Code does not address
3. At least one specific way that AI coding assistants change the ethical calculus — for better or worse
4. At least one concrete scenario where a practitioner could be legally compliant and still acting unethically

You may use your AI Coding Assistant to research, outline, and draft. Your session log must accompany the paper. You must be able to defend every claim and every source in a follow-up discussion.

This is not a summary of ethics frameworks. It is an argument about what this specific profession owes.

---

## Portfolio Review

Both repos must be in final reviewed state by the end of Week 16.

**Primary repo `README.md`** must include:
- A one-paragraph professional summary of what the portfolio demonstrates
- A table of all artifacts with one-sentence descriptions
- The tool(s) used and a brief evaluation of each for this specific course context
- The most significant thing you learned from a session log that wasn't in the artifact itself

**Secondary repo `README.md`** must include:
- A one-paragraph summary of what the role rotation work revealed across the semester
- The role pairing that produced the most useful divergence, and why
- One operational question that the full semester's reading left unanswered

Both READMEs should be written as if a hiring manager at INL, a DOE contractor, or an NRC-regulated utility will read them. They should be professional, specific, and honest about what the work does and does not demonstrate.

---

## KSA Developed — Module 9

**Knowledge**
- Professional ethics frameworks: ACM Code of Ethics; where legal and ethical obligations diverge
- Export control in nuclear cybersecurity research: 10 CFR 810 and its implications for knowledge sharing
- NRC disclosure obligations vs. ethical disclosure obligations
- AI ethics in high-consequence systems: accountability, explainability, human oversight requirements
- The policy gap between current regulatory requirements and good professional practice

**Skills**
- Ethics paper writing: argument-based, primary-source-grounded, specific to professional context
- Portfolio synthesis and professional presentation
- Policy gap analysis: identifying what regulation does not yet require but good practice demands
- Reflective practice: what the semester's AI-assisted workflow taught about AI capabilities and limits

**Abilities**
- Articulate professional ethical obligations that exceed legal minimums
- Apply an ethics framework to a specific scenario and reach a defensible conclusion
- Present a technical portfolio to a non-technical audience in a way that communicates demonstrated competence

---

## Employer Signal

**Primary repo artifact** signals:
> *"This candidate completed a full semester of AI-assisted nuclear cybersecurity work and can articulate what the portfolio demonstrates and what it does not — the hallmark of a practitioner rather than a student."*

**Secondary repo artifact** signals:
> *"This candidate spent 16 weeks analyzing the same nuclear security material from multiple organizational role perspectives and can identify the systemic gaps between legal compliance, regulatory frameworks, and good professional practice — which is exactly the analytical capability that makes someone useful in policy, inspection, or program management roles."*

---

*Last updated: July 2026 — Christopher Spirito (cspirito@boisestate.edu)*
