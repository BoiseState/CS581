# Role Analysis — Module 2
## Jordan Reyes | Weeks 3–4

**Role A:** Nation-State Threat Analyst
**Role B:** Insider Threat Investigator

Both roles are reading my own W2 output: the Sandworm profile against TCS, and the five threat cards.

---

## Role A Perspective: Nation-State Threat Analyst

This role reads my profile and asks one question before any other: what is sourced, and what am I asserting?

It approves of the `gaps_in_public_knowledge` array and would extend it. The entry it cares about most is the first one, that no public source places Sandworm in a nuclear generating station. An analyst writing for a customer who has to make a resourcing decision cannot let an architectural analogy stand in for a targeting finding, because the customer will act on the finding and not on the reasoning behind it.

It would push back on my `capability_tier` field. Tier is a summary judgement that compresses resourcing, sophistication, operational security, and demonstrated effect into one token. Sandworm and XENOTIME both carry `nation-state-tier-1` on my cards, but XENOTIME's known operation failed on a coding error and Sandworm's succeeded twice against live infrastructure. The field cannot hold that difference.

What this role would do with my work: build the collection requirement. Given what I cannot answer from open sources, what would I need to task? For my TCS question that is turbine control vendor identity, firmware revision, and whether the balance-of-plant network is separated from supervisory control by anything more than convention. None of that is answerable from where I am sitting, and naming it is the deliverable.

The role's blind spot, visible in my own profile: every technique I mapped assumes an external actor arriving from somewhere else. My `pivot_path` traces a route from DCS to TCS. It does not consider that the shortest route to a turbine control system is a person who is already authorised to be in front of it.

---

## Role B Perspective: Insider Threat Investigator

This role reads the same two artifacts and finds them almost unusable.

My detection opportunities list is five entries long and four of them assume an unauthorised actor. "Engineering workstation logons outside maintenance windows" catches an intruder. It does not catch the engineer who has legitimate credentials, a legitimate reason to be logged in, and an illegitimate purpose. That person generates no anomaly in any of my detections, because they are not an anomaly.

The role would also challenge my entire framing of `pivot_path`. I traced a network route because network routes are what I know how to think about. The insider does not pivot. They are already positioned, and what changes is intent rather than location. My W1 map has a row for "DCS cabinet physical access" that I rated a lower concern precisely because it requires being inside the protected area, which I treated as a barrier. This role treats it as a description of the workforce.

**Anderson Ch. 2 grounding.**

This role has no MITRE matrix. Its evidentiary basis is the psychology chapter, and two concepts from it do the work.

The first is Anderson's treatment of **authority and deference to it**. The chapter's argument is that people comply with the markers of authority rather than with verified authority, and that this is ordinary rather than foolish. Applied to my detection list: an analyst who sees a vendor remote-access session outside a maintenance window and assumes a ticket exists somewhere is doing the normal thing. My control does not fail technically. It fails because a person behaves the way people behave. That reframes the control from a technical measure into an organisational one, and the fix is procedural, requiring the ticket reference at session initiation, rather than more logging.

The second is his material on **the gap between what security designers imagine users will do and what users actually do under real conditions**, the usability argument that runs through the chapter. Insider indicators in the literature are mostly behavioural: disgruntlement, unusual hours, policy friction. Anderson's point about designing for actual human behaviour cuts against acting on those, because in a plant environment unusual hours describe an outage, and policy friction describes anyone competent enough to notice that a procedure is wrong. The base rate destroys the indicator. An investigator who takes the chapter seriously trusts observable, verifiable behaviour over inferred disposition, and accepts that most insider risk is not detectable in advance.

I will note that I reached for these concepts because the assignment required it, and that I would not have opened the chapter again otherwise. Having done it, the insider lens is the only part of my W2 work that changed what I think, rather than adding to what I know.

---

## Divergence Analysis

The two roles do not disagree about facts. They read the same profile and the same cards. They diverge on what counts as evidence.

The threat analyst's evidence is external and documentary: indictments, advisories, malware analysis, technique mappings. It is auditable, and it is always about someone else, somewhere else, previously.

The investigator's evidence is internal and behavioural: access patterns, organisational conditions, the state of the workforce. It is not auditable in the same way, it is about the people in the building, and it is mostly about the present.

The operational consequence is a fight over where the next dollar goes. The analyst argues for detection engineering against documented TTPs, which is defensible in an audit because every control maps to a named technique and a public report. The investigator argues for access authorisation programme quality under 10 CFR 73.56, supervisory practice, and reducing the number of people with standing turbine control access, none of which map to a MITRE ID and all of which are harder to defend in a compliance review.

The analyst's case is easier to write down. That is not the same as being more important, and the asymmetry in how easy each case is to document is itself a distortion in how plants allocate security effort.

---

## Synthesis

Doing this rotation changed one thing in my actual W2 output, and I want to name it specifically rather than claim a general insight.

The insider lens exposed that my `pivot_path` answer is a network answer to a question that is not only about networks. I traced DCS to TCS across Modbus links because that is a route I can draw. The honest version of that field would also say that the shortest path to turbine control is standing in front of the turbine control HMI with a badge that works, and that no amount of segmentation addresses it.

I am leaving my `pivot_path` as written, because rewriting it now would make the profile look more considered than the process was. But the limitation goes in my W3 notes, and when I build the RBAC policy in W4 this is where I start.

The broader point, which I did not expect: the threat analyst role is the one that makes you feel competent. It has names, IDs, citations, and a framework. The investigator role mostly produces the conclusion that you cannot see what you would need to see. Between the two, the second is doing more honest work, and it is the one a security programme is more likely to underfund because its deliverable is an admission rather than a matrix.
