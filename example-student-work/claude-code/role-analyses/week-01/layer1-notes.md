# Layer 1 — My Own Read
## Anderson Ch. 1–2 + RG 5.71 Sections 1–3 + NEI 08-09 Executive Summary

**Student:** [Your Name] | **Date:** Week 1

---

### What surprised me (3–5 bullets)

1. **Security is explicitly an economics problem, not a technology problem.** Anderson opens with this and it reframes everything. Attackers optimize for cost — they don't look for the most sophisticated vulnerability, they look for the cheapest path to their objective. This means defenders who pour resources into technical controls while leaving cheaper human or physical paths open are solving the wrong problem. I expected a chapter on firewalls and encryption. I got a chapter on incentive structures.

2. **Safety engineering and security engineering are fundamentally different disciplines, and conflating them is dangerous.** Safety assumes random failures — you design for statistical likelihood. Security assumes an adversary who actively seeks out your assumptions and exploits them. A nuclear plant designed with excellent safety engineering may still have terrible security engineering because the failure models are different. The designer who assumes "this failure mode is statistically unlikely" hasn't considered that an adversary can deliberately cause that exact failure.

3. **Chapter 2 made me uncomfortable in a specific way.** The cognitive bias taxonomy isn't abstract — Anderson is describing exactly how I make decisions under uncertainty. The availability heuristic (I estimate risk based on how easily I can recall an example) explains why security practitioners consistently underestimate threats they've never personally encountered. A nuclear plant cybersecurity manager who has never seen a cyber-physical attack will systematically underweight that threat. This is structural, not a personal failing.

4. **RG 5.71 is doing something different from what I expected.** I thought it would be a technical standard (like a NIST document). Instead, it's defining a framework — it tells licensees to have a Cyber Security Plan, what that plan must include, and how to demonstrate compliance. The actual technical controls live in the appendices and in NEI 08-09. The regulatory document and the technical guidance are separate products from separate institutions. This matters because it means you can be compliant with the regulatory framework while still having technically weak controls — if the plan says the right things.

5. **NEI 08-09 introduces the concept of "critical digital assets" (CDAs) in a way that immediately creates a scoping problem.** You have to determine what is a CDA before you can protect it. That determination is itself a security-sensitive decision. The executive summary is clear that facilities have significant latitude in making this determination — which means the attack surface is partly defined by the licensee's own judgment, subject to NRC review. This is where the regulator-vs-operator tension I'm supposed to analyze actually lives.

---

### What I'm uncertain about

- How the RG 5.71 framework interacts with legacy systems that predate it (most instrumentation at operating reactors). Do they get grandfathered? Retrofitted? This wasn't clear from Sections 1–3.
- Anderson mentions "security economics" as a field — I'd like to go deeper on this but it feels outside the scope of Week 1.
- The line between a safety system and a security system in a nuclear plant isn't as clean as the reading implies. The reactor protection system (RPS) is a safety system — but compromising it has security implications. Which regulatory framework governs that intersection?
