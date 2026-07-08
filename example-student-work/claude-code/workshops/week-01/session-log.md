# Session Log — Workshop 1
## CS 581 · Week 1 · Nuclear Plant Attack Surface Map

**Tool:** Claude Code | **Model:** claude-opus-4 | **Thinking:** extended, high effort
**Date:** Week 1 | **Duration:** approx. 45 minutes

---

## What a session log is

A session log is not a transcript dump. It is a record of your prompting process: what you asked, why you asked it, what worked, what didn't, and what you would do differently. It is graded independently from the artifact because the artifact shows what you produced — the log shows how you thought.

A good session log makes your reasoning visible to someone who wasn't in the session. A bad session log is a paste of raw chat output with no annotation.

---

## Session narrative

### Starting prompt — too broad, revised immediately

**Prompt 1 (initial, too broad):**
> Tell me about nuclear plant cybersecurity.

**What happened:** The model produced a generic overview that covered the same territory as a Wikipedia search. No structure, no depth, no nuclear specificity beyond the obvious. This was a calibration prompt to see what the default output looked like without direction.

**Decision:** Restart with the structured prompt from the curriculum document, adding one modification — I asked it to flag anything requiring facility-specific knowledge rather than just producing a generic map.

---

### Prompt 2 — structured, with role and output format specified

**Prompt:**
> I am a graduate student in a nuclear cybersecurity course (CS 581 at Boise State). Based on publicly available information about nuclear power plant architecture, NRC regulatory guidance (particularly 10 CFR 73.54 and RG 5.71), and the ICS/SCADA security literature, help me build a structured attack surface map for a generic US nuclear power plant.
>
> Requirements:
> - Cover three layers: IT (corporate), OT (operational technology/ICS), and Physical/Cyber Intersection
> - For each layer: key components, threat vectors, notable security gaps
> - Use markdown table format with columns: Component | Role | Threat Vectors | Notable Gaps
> - After the three layers, add a section called "What This Map Cannot Tell You" — what information would I need from the actual facility to convert this generic map into a real assessment?
> - Flag anything where you are drawing on specific incident knowledge vs. general architectural knowledge
> - Do not invent facility-specific details

**What happened:** The output was significantly better — structured, layered, and differentiated between architectural knowledge (general) and incident-specific knowledge (Stuxnet, CRASHOVERRIDE). The model used extended thinking to work through the OT layer systematically before producing the table, which was visible in the reasoning trace.

**What I did with the output:** Reviewed it against my Layer 1 notes and Layer 2 LLM synthesis from the reading assignment. Found two gaps:
1. The model hadn't addressed the historian server as an IT-OT bridge explicitly — it was implied but not named
2. The Physical/Cyber Intersection layer was thin — only two components initially

---

### Prompt 3 — targeted refinement

**Prompt:**
> Two things to add:
> 1. In the IT layer, make the historian server more explicit as an IT-OT bridge — it's the most common pivot point and should be called out by name, not just implied in "data aggregation systems"
> 2. The Physical/Cyber Intersection layer is thin. Add UPS network management, HVAC/building management, and emergency diesel generator control interfaces. These are documented attack surfaces in ICS incidents and are specifically relevant in nuclear plants.

**What happened:** The model incorporated both additions correctly and didn't over-generate — it added the requested components without inflating the other layers. The UPS network management card note correctly referenced the documented vulnerability history without hallucinating specific CVEs (it said "documented history" rather than citing a specific one I couldn't verify).

---

### Prompt 4 — "What This Map Cannot Tell You" section

**Prompt:**
> The "What This Map Cannot Tell You" section is important — it should be the part that demonstrates analytical honesty. Expand it. Include: actual network topology, historian configuration, vendor access specifics, patch status, CDA determination scope, physical/cyber separation specifics, and insider threat profile. For each item, explain WHY you need it — not just that it's missing.

**What happened:** This is the prompt that produced the most value. The model's expanded "What This Map Cannot Tell You" section surfaced the CDA scoping issue (from my Layer 1 reading) as a gap, which validated that the reading assignment had actually prepared me to evaluate the model's output rather than just accept it.

**Key observation:** I would not have known to ask for the CDA determination as a gap if I hadn't done the Layer 1 and Layer 2 reading. The reading assignment isn't supplementary — it is what gives you the domain knowledge to evaluate and improve the model's output.

---

### What I would do differently

1. **Start with the structured prompt.** The calibration prompt (Prompt 1) was wasted time. I should have started with format and role specifications from the beginning.

2. **Load the regulatory documents directly.** I described the regulatory context in the prompt rather than loading RG 5.71 and NEI 08-09 as context. Loading them would have allowed the model to draw on the actual language of the framework rather than my paraphrase of it.

3. **Use structured output (JSON) for the tables.** Markdown tables are readable but not machine-processable. For a real compliance matrix or assessment, I would use JSON with a defined schema so the output could be imported into a tracking system.

4. **Add a confidence rating column.** Not all attack surface entries are equally well-documented. A column indicating whether the threat vector is "documented in public incidents," "inferred from architecture," or "theoretical" would make the map more epistemically honest.

---

## What the session log demonstrates to an evaluator

- I evaluated the model's initial output rather than accepting it
- I iterated based on domain knowledge from the reading assignment
- I identified specific gaps and requested targeted additions
- I reflected on what I would do differently — which requires actually thinking about the session, not just producing output

A session log that is just a paste of the conversation demonstrates that you ran the model. This log demonstrates that you used it.

---

*Committed to primary-repo/workshops/week-01/session-log.md*
