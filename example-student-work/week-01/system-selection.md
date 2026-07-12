# System Selection — Week 1

**Chosen system:** DCS — Digital Control System  
**Purdue Zone:** Level 2 (Supervisory)  
**System type:** Operational

---

## Rationale

I chose the DCS for Week 1 because it sits at the intersection of two things I understand and one thing I do not.

The two things I understand: distributed systems, and the operational tradeoff between availability and security. My fintech background was almost entirely distributed systems work — services that could not go down, where security patches were perpetually deferred because the risk of a botched update outweighed the vulnerability risk. The DCS has exactly this problem, but with consequences that are not measured in transaction failures. That felt like the right starting point — build the attack surface map on a system whose *constraints* I already intuitively understand, even if the domain is new.

The thing I do not understand: nuclear-specific regulatory treatment. The Plant Architecture Diagram shows DCS at Purdue Level 2 with a data diode connection down to RPS and an OPC-UA link up to the historian/PPC. I know what those protocols are. What I do not know is what "Critical Digital Asset" classification means for this system, or how 10 CFR 73.54 constrains the vendor patching cycle. That is what the attack surface map forced me to research.

The affinity rating in the diagram marks DCS as Primary for W1 (workshop theme: foundations, attack surface). That confirmed my instinct. The Module 6 affinity (Primary) is also notable — I am flagging DCS as a candidate for pairing in Week 6 with OT-SIEM, since the SIEM's value is largely defined by what it can see of the DCS traffic.

The system I almost chose was RPS — the safety system. I pulled back because I was not confident I could write an accurate attack surface map for a system I genuinely do not understand the physics of yet. The DCS is the right Week 1 system for me specifically. RPS will be Week 2.
