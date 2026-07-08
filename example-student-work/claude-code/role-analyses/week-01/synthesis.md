# Layer 4 — Synthesis Note
## Week 1: Foundations

**Student:** [Your Name] | **Date:** Week 1
**Roles analyzed:** NRC Regulator · Plant Cybersecurity Manager

---

## What my Layer 1 read surfaced

Security engineering is fundamentally about economics and incentives, not technology. The nuclear regulatory framework (RG 5.71, NEI 08-09) formalizes this into a compliance program — but compliance programs and adversarial security are not the same thing. I noticed early that licensees define their own critical digital asset scope, creating a circularity in the protection framework.

## What the LLM synthesis added

More precise articulation of where Anderson's attack surface and defense-in-depth concepts map to specific regulatory constructs. It made explicit what I had only intuited: that RG 5.71 is a framework document, not a technical standard, which means the technical rigor lives in the appendices and NEI guidance — one level removed from the regulatory obligation itself.

## Where the two roles diverged

The NRC Regulator and the Plant Cybersecurity Manager are reading the same Anderson chapters and the same regulatory documents, but they are solving different problems with them.

**The regulator** is asking: *What can I observe, measure, and enforce?* Anderson's economics argument is useful because it explains why regulated entities need external pressure to invest in security. The regulator reads RG 5.71 as a set of verifiable commitments. The CDA scope is something they can inspect. The defensive architecture is something they can evaluate. But the regulator's tools (inspection, enforcement) work on documented plans and observable configurations — not on the gap between those documents and actual adversarial resilience.

**The plant manager** is asking: *What can I actually implement in this environment?* Anderson's framework assumes design freedom the plant manager does not have. Legacy systems, safety primacy over availability, 18-month patch cycles, contractual vendor access requirements — these are constraints that don't appear in the regulatory framework and that Anderson's general framework doesn't address. The plant manager reads the same documents and finds them useful for budget advocacy and workforce framing, but routinely incomplete for operational decision-making.

**The divergence is not a disagreement — it is a gap.** The regulator and the plant manager are not arguing about security principles. They agree on them. The gap is between the regulatory ideal (a Cyber Security Plan that addresses the required controls) and the operational reality (a plant with fixed attack surfaces, constrained patching windows, and safety requirements that sometimes override security controls).

## The operational question the divergence raises — that neither Anderson nor the regulatory documents answer

**Who resolves the conflict when a security control and a safety requirement point in opposite directions, in real time — and what happens when a single cyber incident implicates Safety, Security, and Safeguards simultaneously?**

Anderson doesn't address this because his framework treats security as the primary design constraint. RG 5.71 acknowledges the safety-security interface but defers to the facility's documented procedures. NEI 08-09 assumes the conflict has been pre-resolved in the Cyber Security Plan.

But the plant manager is right: you cannot pre-resolve every scenario. During a plant event, an operator may need to take an action that violates a documented security control — not because they are malicious, but because the operational situation requires it.

This problem is even harder than it appears from Anderson alone, because nuclear operates under three distinct regulatory frameworks that a single cyber attack can implicate simultaneously:

- **Safety** (10 CFR 50): Did the attack affect a safety function? NRC-NRR is the authority. Notification under 10 CFR 50.72 may be required within hours.
- **Security** (10 CFR 73 / 73.54): Did the attack constitute a cyber attack on a critical digital asset? NRC-NSIR is the authority. Notification under 10 CFR 73.71 may be required.
- **Safeguards** (10 CFR 74 / IAEA): Did the attack compromise nuclear material accounting records or enable diversion? NRC-NMSS and potentially the IAEA are the authorities. Different reporting requirements, different timelines.

Three frameworks. Three NRC offices. Potentially an international body. All triggered by one attack, simultaneously, with a facility in active incident response.

Neither Anderson nor the Week 1 regulatory readings address this coordination problem. RG 5.71 is a Security framework document — it does not discuss Safeguards. 10 CFR 74 does not discuss cyber attacks. The IAEA Computer Security guidance (NSS-17) addresses the international dimension but not domestic inter-agency coordination.

This is not a theoretical problem. It is the central challenge of cybersecurity in the nuclear domain — and it is the question this course is designed to prepare you to reason about, even if no document currently answers it completely.

---

*Committed to secondary-repo/role-analyses/week-01/synthesis.md*
