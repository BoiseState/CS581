# Layer 3 — Role Rotation: NRC Regulator
## Anderson Ch. 1–2 + RG 5.71 + NEI 08-09 through the lens of an NRC cybersecurity inspector

**Prompt used:**
> You are a senior NRC cybersecurity inspector preparing to conduct a 10 CFR 73.54 inspection at a licensed nuclear facility. Re-read the following material — Anderson's Security Engineering Chapters 1–2, NRC Regulatory Guide 5.71 Sections 1–3, and the NEI 08-09 Executive Summary — and take notes on: (1) what these documents tell you about what to look for during an inspection, (2) where the regulatory framework may be insufficient to catch real security failures, and (3) what questions you would ask plant personnel that the documents don't explicitly prompt you to ask.

---

## What these documents tell an NRC inspector to look for

**From Anderson Ch. 1 — economics and attack surface:**
The economic framing is directly useful for inspection. If security is about raising the cost of attack, then an inspector is asking: has this licensee made the attacker's job harder, or have they just documented that they intend to? The attack surface concept maps directly to the CDA scope — inspectors should verify that the licensee's CDA determination is defensible, not self-servingly narrow. An operator who has defined CDAs in a way that excludes obvious candidates has either made a legitimate engineering argument or has optimized for compliance cost.

**From Anderson Ch. 2 — psychology and insider threat:**
The cognitive bias framework gives inspectors a lens for evaluating the human elements of the Cyber Security Plan. Specifically: does the licensee's security awareness training address automatic cognitive processes (which Anderson says are what actually get exploited) or just conscious rule-following? A training program that tells employees "don't plug in unknown USB drives" without addressing why they might — the availability heuristic, authority compliance, social proof in a team setting — is insufficient.

**From RG 5.71:**
The inspection framework. Inspectors verify that:
- The Cyber Security Plan exists and has been approved
- The defensive architecture implements the required network separation
- CDAs have been identified and are protected per the plan
- Incident response and training programs are in place and tested

**From NEI 08-09:**
The implementation detail that makes the plan concrete. Inspectors compare the licensee's actual implementation against the NEI guidance, noting where they have deviated and whether they have documented a defensible basis for deviation.

---

## Where the regulatory framework may be insufficient

1. **The CDA scoping problem.** The licensee defines their own CDAs subject to NRC review. An inspector can challenge a CDA determination, but the burden of proof is ambiguous. A sophisticated licensee can construct a defensible argument for a narrow CDA scope that nevertheless leaves real attack vectors unaddressed. The regulatory framework doesn't give inspectors a definitive methodology for evaluating CDA completeness.

2. **Compliance vs. security.** Anderson's core argument is that security is an economics problem. The regulatory framework creates a different economics: compliance is required, security beyond compliance is optional. A licensee who has invested in a defensible Cyber Security Plan that satisfies inspection criteria may have optimized for compliance rather than for raising the attacker's cost. These can be the same thing, but they are not required to be.

3. **Legacy system treatment.** RG 5.71 was issued in 2010. Many nuclear plants have instrumentation and control systems from the 1970s and 1980s. The regulatory framework has provisions for systems that cannot be practically modified, but the inspector's ability to evaluate whether a legacy system exemption is truly necessary or merely convenient is limited by technical complexity and inspection time constraints.

4. **The insider threat gap.** 10 CFR 73.56 addresses insider mitigation, but Anderson's Chapter 2 suggests the threat is primarily cognitive and social — not addressed by background checks and access controls alone. An inspector can verify that an insider mitigation program exists and is documented. Verifying that it would actually detect a sophisticated insider is a different question.

---

## Questions an inspector would ask that the documents don't prompt

- Walk me through how you determined your CDA list. What systems did you evaluate and exclude, and what was the basis for each exclusion?
- Has your defensive architecture ever been tested against an actual intrusion attempt? If so, what happened? If not, why not?
- What happens to your security controls during a plant event? Show me your procedures for a scenario where normal security controls conflict with emergency operating procedures.
- Tell me about the last time an employee reported a potential security concern. What happened?
- Who made the decision about which legacy systems are exempt from full CDA treatment, and what was their technical basis?
- How does your training program handle the scenario where a trusted insider — someone with legitimate access — begins acting against the plant's interests? What would you actually see?
