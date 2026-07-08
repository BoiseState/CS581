# CS 581 — Module 1 Prompt for Codex
## Nuclear Plant Attack Surface Map + Multi-Lens Reading Analysis

Copy this prompt into Codex as a task. Codex should produce all deliverables and write them to the file paths specified. Review and annotate the output before committing — the session log should reflect your evaluation of what Codex produced, not just what it produced.

---

## Task

You are a graduate student in CS 581 — Nuclear Cybersecurity at Boise State University. This is a Week 1 assignment. Complete all four parts below and write each output to the specified file path.

---

## Context: What you have read

You have read the following material this week. Use it as your knowledge base for all deliverables.

**Anderson, Security Engineering, Chapters 1–2 (key points):**
- Security is an economics problem: attackers optimize for lowest cost, so the defender's job is to raise the cost of attack, not achieve perfect protection
- Security and safety engineering are fundamentally different: safety assumes random failures, security assumes an adversary who actively seeks out your assumptions
- The CIA triad (Confidentiality, Integrity, Availability) plus authentication, authorization, non-repudiation define the core property set
- Human cognition is systematically exploitable via known heuristics: availability bias, authority compliance, social proof, loss aversion, anchoring
- Usability and security are often in tension, but poor security UX creates workarounds that undermine the controls themselves
- Security failures are organizational and economic at least as often as they are technical

**NRC Regulatory Guide 5.71 — Sections 1–3 (key points):**
- Nuclear licensees must establish, implement, and maintain a Cyber Security Program (CSP)
- The CSP must protect Critical Digital Assets (CDAs): digital systems performing safety, security, or emergency preparedness functions
- Defense-in-depth and defensive architecture (network separation between security levels) are the primary structural requirements
- Licensees must protect against both external cyber attacks and insider threats
- The regulatory guide is a framework document; technical implementation detail lives in appendices and NEI 08-09

**NEI 08-09 Rev. 6 — Executive Summary (key points):**
- Industry implementation guidance for RG 5.71 compliance
- Introduces the CDA determination process — facilities identify their own CDAs subject to NRC review
- Addresses eight security control families: access control, configuration management, media protection, incident response, physical protection, system integrity, training, and supply chain
- Acknowledges legacy systems that cannot be practically modified and provides for alternative compensating controls

---

## Part 1 — Layer 1 Reading Notes

Write 3–5 bullets capturing what surprised you most in the assigned readings. Focus on claims that would not have been obvious before you read them, and note at least one thing you remain uncertain about.

**Output file:** `role-analyses/week-01/layer1-notes.md`

---

## Part 2 — LLM Synthesis

Synthesize the key technical claims, assumptions, and gaps across all three assigned readings. Then identify: (a) what a standard LLM synthesis would likely add that a first-time reader might miss, and (b) what a standard LLM synthesis would likely flatten or omit. Write this as if you had run your own synthesis prompt and are evaluating the output.

**Output file:** `role-analyses/week-01/layer2-synthesis.md`

---

## Part 3 — Role Rotation (NRC Regulator + Plant Cybersecurity Manager)

For each role, re-read all assigned material from that role's perspective and answer the specific questions below. Write each role's analysis as a separate file.

**NRC Regulator** — answer these questions from an inspector's perspective:
1. What do these documents tell you to look for during a 10 CFR 73.54 inspection?
2. Where may the regulatory framework be insufficient to catch real security failures?
3. What questions would you ask plant personnel that the documents don't explicitly prompt?

**Output file:** `role-analyses/week-01/nrc-regulator.md`

**Plant Cybersecurity Manager** — answer these questions from an implementer's perspective:
1. What is actually useful for your day-to-day job?
2. Where do the frameworks assume freedoms you don't have in a nuclear operational environment?
3. What do you wish the authors of Anderson and RG 5.71 understood about your operating environment?

**Output file:** `role-analyses/week-01/plant-cybersecurity-manager.md`

---

## Part 4 — Synthesis Note (one page maximum)

Write a one-page synthesis that answers:
1. What did your Layer 1 read surface?
2. What did the LLM synthesis add or change?
3. Where did the NRC Regulator and Plant Cybersecurity Manager perspectives diverge on the same material?
4. What operational question does that divergence raise that neither Anderson nor the regulatory documents answer?

**Output file:** `role-analyses/week-01/synthesis.md`

---

## Part 5 — Attack Surface Map

Build a structured attack surface map for a generic US nuclear power plant using only publicly available information. Do not invent or imply facility-specific details.

**Requirements:**
- Cover three layers: IT (Corporate), OT (Operational Technology), Physical/Cyber Intersection
- For each layer, produce a markdown table with columns: Component | Role | Threat Vectors | Notable Gaps
- After the three tables, write a section titled "What This Map Cannot Tell You" — for each item listed, explain specifically WHY that information is needed to convert this generic map into a real assessment
- Flag anything drawn from specific documented incidents vs. general architectural knowledge
- Include a brief layer summary paragraph after each table

**Output file:** `workshops/week-01/attack-surface-map.md`

---

## Part 6 — Tool Selection Evaluation

Evaluate Codex (this tool) against the seven capability dimensions below. Be honest — including about limitations. Use the JSON format specified.

**Capability dimensions:**
1. Thinking & Reasoning Depth — configurable reasoning modes, reasoning between tool calls, reasoning preservation
2. Context Length — how much can it hold and how does that affect this assignment
3. Function Calling & Tool Use — external tools, APIs, scripts
4. Structured Output — reliable JSON, schema conformance
5. Vision & Multimodal — image and PDF input
6. MCP / Tool Integration — Model Context Protocol servers
7. Provenance & Trust — provider, US-based, data handling for sensitive security content

**Required JSON structure:**
```json
{
  "tool": "Codex",
  "provider": "OpenAI",
  "evaluation_date": "YYYY-MM-DD",
  "capabilities": {
    "thinking_and_reasoning": { "supported": true/false, "notes": "..." },
    "context_length": { "tokens": N, "notes": "..." },
    "function_calling": { "supported": true/false, "notes": "..." },
    "structured_output": { "supported": true/false, "notes": "..." },
    "vision_multimodal": { "supported": true/false, "notes": "..." },
    "mcp_integration": { "supported": true/false, "notes": "..." },
    "provenance_trust": { "provider": "...", "us_based": true/false, "notes": "..." }
  },
  "justification": "Why this tool or why not for this course",
  "limitations": ["...", "..."],
  "best_suited_for": "Which modules or task types in CS 581 would benefit most from Codex specifically"
}
```

**Output file:** `workshops/week-01/tool-selection.json`

---

## Part 7 — Session Log

Write a session log documenting your process for Part 5 (the attack surface map). The session log is NOT a transcript. It should include:
- What your initial prompt was and what the output looked like
- What you changed and why (what gap or error prompted the revision)
- What you would do differently if you ran this session again
- One observation about what the domain knowledge from the reading assignment (Parts 1–4) let you see in the model output that you wouldn't have noticed otherwise

**Output file:** `workshops/week-01/session-log.md`

---

## File structure when complete

```
role-analyses/week-01/
  layer1-notes.md
  layer2-synthesis.md
  nrc-regulator.md
  plant-cybersecurity-manager.md
  synthesis.md

workshops/week-01/
  attack-surface-map.md
  tool-selection.json
  session-log.md
```

---

## Grading note

The session log and tool-selection evaluation are each graded independently from the attack surface map. A technically excellent attack surface map with a shallow session log is not a complete submission. The session log and evaluation demonstrate that you engaged with the tool rather than just accepted its output.
