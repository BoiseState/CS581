# Session Log — Workshop 2
## Jordan Reyes | Claude Code | Sep 9–20, 2026

Same rules as W1: dead ends included, in the order they happened.

W1 taught me that the session log is where I catch myself. I am writing this one as I go rather than reconstructing it at the end, which is what I actually did in W1 despite claiming otherwise. That is the first honest thing in this document.

---

## Session 1 — Sep 9 | "Changing my W2 system before I start"

**Duration:** ~40 minutes
**Outcome:** Sequencing plan revised, RPS out, TCS in

My W1 sequencing plan put RPS in W2. I changed it to TCS before writing a single line of the profile, and I want to record why, because the reason came out of the new `pivot_path` field rather than out of anything I knew in August.

`pivot_path` asks how the adversary moves from my W1 system to my W2 system. I opened my own W1 OT map to answer it and looked at row 5:

> Data diode to RPS (outbound only)

I wrote that row myself three weeks ago and had not thought about what it meant for W2. The answer is that DCS to RPS is not a pivot. It is a wall. Telemetry goes out, nothing comes in. If I had kept RPS as my W2 system, my honest `pivot_path` value would have been two sentences saying there is no path, and then the rest of the profile would have floated free of my W1 work entirely.

Row 4 of the same map is different:

> Modbus TCP / Serial links (Level 1 devices)

The DCS supervises balance-of-plant equipment. TCS is balance-of-plant. Same control network, no boundary device in between. That is a real pivot with a real interface behind it.

So: TCS for W2. I logged the change and the reason in `sequencing-plan.md` as the assignment requires. RPS moves to W4.

I want to flag something about this for whoever reads the log. The field changed my plan. I did not sit down intending to revise anything. I sat down to fill in a JSON key, could not answer it honestly, and discovered that the thing I could not answer was the point.

---

## Session 2 — Sep 11 | "The first profile was a Wikipedia article"

**Duration:** ~1 hour
**Outcome:** Discarded

I gave Claude Code the schema and asked for a Sandworm profile. What came back parsed cleanly, filled every field, and was useless.

The problem was the same one I hit in W1 Session 1, wearing different clothes. Every `nuclear_relevance` string said something like "this technique is relevant to nuclear facilities because control systems are critical infrastructure." True, generic, and applicable to any of the eleven systems on the course list. The `system_relevance` fields were worse: they described plausible interfaces on a plausible turbine control system rather than rows on **my** map.

I had handed over the schema without handing over my W1 work. The model had nothing of mine to attach to, so it invented a generic plant and profiled against that.

Discarded the file.

---

## Session 3 — Sep 12 | "Giving it my own map"

**Duration:** ~2 hours
**Outcome:** The profile that survived

Second attempt started differently:

> *"Read workshops/week-01/attack-surface-map-ot.md and attack-surface-map-it.md. Those are mine. For each TTP you propose, the system_relevance field must name a row that exists in one of those files. If a technique has no row to land on, say so instead of inventing one."*

The last sentence did the work. It gave the model permission to fail on a field, and a failed field is information.

It used that permission once, on Manipulation of Control (T0831). It told me it could not map the technique to a TCS-internal component because I have not built a TCS attack surface map, only a DCS one. That is correct and I left the admission in the profile rather than smoothing it over. It is the most useful sentence in the file: it marks the exact boundary of what W1 bought me.

**The thing I got wrong and had to fix.** My first pass at `nuclear_targeting_evidence` said Sandworm "has demonstrated intent to target nuclear generation." I wrote that, not the model. I went looking for the source to cite and could not find one. What I actually had was: documented operations against Ukrainian electricity transmission and distribution, plus my own sense that turbines are turbines.

That is an analogy, not evidence. I rewrote the field to say so explicitly, and the rewritten version is longer and less impressive and correct. The gap now also appears as the first entry in `gaps_in_public_knowledge`.

I am dwelling on this because it is the same failure I criticised the model for in Session 2. It produced generic confidence; then I produced specific confidence that I could not source. Mine was harder to catch because it sounded like expertise.

---

## Session 4 — Sep 14 | "Checking the technique IDs"

**Duration:** ~50 minutes
**Outcome:** IDs verified, one corrected

I did not trust the MITRE IDs. Model-generated identifiers are exactly the kind of thing that looks authoritative and is occasionally invented, and a wrong `T0` number would propagate into every later workshop that references this profile.

I opened the ATT&CK for ICS matrix and checked all eight by hand against the technique names, rather than asking the model to check its own work.

Seven matched. One did not: I had a supply-chain technique carrying an ID whose actual name was something else, so I removed that TTP rather than guess at the right number. The ID that ended up on the BERSERK BEAR card (T0862, Supply Chain Compromise) I verified separately when I built the cards.

**The thing that nearly caught me out.** I had been treating the number prefix as the matrix indicator: `T0` for ICS, `T1` for Enterprise. That is wrong. The ICS matrix now carries techniques in the `T1NNN.NNN` sub-technique space as well, so `T1692.001` (Unauthorized Message: Command Message) is an ICS technique despite the `T1` prefix. I had originally written `T0855` for the command-message TTP, which is the older numbering for roughly the same behaviour.

This matters beyond getting one number right. My working rule for spotting a hallucinated ID was "does the prefix match the matrix I asked for," and that rule was never valid. It would have passed a wrong `T1` ID as an intentional Enterprise citation and flagged a correct ICS one as a mistake. The only check that works is looking the technique up.

DarkSide is the one card that genuinely does carry an Enterprise ID, `T1486`, and I have marked it as such in its own field with a note saying why no ICS technique applies. The card shows it labelled ENTERPRISE rather than silently mixing it in with the ICS IDs, because a reader scanning five cards should not have to know the numbering history to tell them apart.

**If you are reading this as an example: verify the IDs in my files too.** I checked them in September 2026 against the matrix as it stood then. Do not inherit my numbers on my say-so, which is the entire habit this course is trying to build and it applies to my work as much as to the model's.

---

## Session 5 — Sep 16 | "Five cards, and the tier rule"

**Duration:** ~2.5 hours
**Outcome:** cards.json plus a generator script

The requirement to span three `actor_type` values is doing more work than it looks like.

My instinct was five nation-state groups, because those are the ones with the good reporting and the memorable names. The rule blocked that, and the two cards I added to satisfy it are the two I learned the most from.

**DarkSide** is a criminal operation with no ICS capability whatsoever, and its ransomware encrypted IT systems only. Colonial halted the pipeline to contain the incident while assessing how far the compromise had reached. CISA and FBI reported no indication the ransomware directly affected OT.

I want to be careful about how I state that, because my first draft of this card got it wrong. I wrote that the OT was "never touched" and that the shutdown happened because the company could not bill. The billing detail is widely repeated and it is not what the CEO's congressional testimony says: the testimony gives containment as the reason. And "no indication of OT effects" is a finding at the time of reporting, not a guarantee that nothing was reached. I had turned a qualified observation into an absolute, which is the exact move I criticised the model for in Session 2.

The lesson survives the correction and is arguably better for it. A group with zero control-system skill produced a national fuel disruption without a control-system effect, because the operator stopped the pipeline to protect it. Nothing in my nation-state cards teaches that, and it is probably the most transferable item in the set for a plant with a business office attached.

**CyberAv3ngers** broke my schema, productively. The group presents as hacktivist and the technical bar was near zero: internet-exposed Unitronics PLCs with default credentials. But CISA attributes the campaign to actors affiliated with the IRGC Cyber-Electronic Command. So which tier is it?

I put `hacktivist` in `actor_type`, because that is how the group presents and operates, and put the attribution in a separate `assessed_affiliation` line so both appear on the card. Those are genuinely two different claims and collapsing them into one field would have buried the more interesting one.

I also had to stop myself inferring capability from the technique. Exposed controllers with default passwords is a low bar, but it bounds the campaign I can see, not the group. The card says that now.

**On the art.** I wrote `make-cards.js` rather than generating images, partly because I wanted the cards to regenerate from `cards.json` when I fix a fact, and partly because I did not want to think about what a threat actor "looks like." The sigils are procedural, seeded from a hash of the actor name, so the artwork is a function of the data and nothing else. Every card carries a line saying the sigil is not a likeness.

I could have used an image generator and the cards would look better. I do not think they would be more honest.

---

## Session 6 — Sep 19 | "Synthesis, and reading Anderson properly"

**Duration:** ~2 hours
**Outcome:** synthesis.md

I will admit this plainly: in W1 I cited Anderson once, in a sentence I could have written without opening the book.

The Insider Threat Investigator lens forced me to actually use Chapter 2, because that role has no other evidentiary basis. A threat analyst has MITRE IDs and CISA advisories. An insider threat investigator has organisational psychology and a set of behavioural indicators that mostly are not observable. The chapter is the whole toolkit for that role.

What changed my synthesis was the material on authority and compliance. My detection opportunities list assumes an analyst who escalates an anomaly. Chapter 2's argument is that people defer to apparent authority and to the expected course of events, which means the analyst who sees a vendor remote-access session outside a maintenance window and assumes there is a ticket somewhere is behaving normally, not negligently. The control I wrote down does not fail technically. It fails because a human being does the reasonable thing.

---

## Reflection — The Card Exercise

Required section. Grounding it in Anderson’s Psychology and Usability chapter (3rd ed. Ch. 3, 2nd ed. Ch. 2) as the assignment asks.

**What the card format added that the sources did not support.**

Certainty, mostly, and a kind of parity. Five actors rendered at identical dimensions with identical fields read as five comparable things. They are not comparable. XENOTIME's card and CyberAv3ngers' card sit side by side looking equally authoritative, and behind one is a US Treasury sanctions action and behind the other is my own guess about how to categorise a group whose self-description and its attribution disagree. The template flattens that.

The MITRE ID does the heaviest lifting. `T0889` in a monospace box next to an actor name looks like a measurement. It is a category label from a framework that is itself a model of adversary behaviour, applied by me, in September, from public reporting of variable quality. Everything upstream of that box is judgement, and the box makes it look like a reading off an instrument.

**Which Anderson’s Psychology and Usability chapter (3rd ed. Ch. 3, 2nd ed. Ch. 2) concepts explain why the card persuades past its evidence.**

Two, specifically.

The first is his treatment of **authority and the cues that trigger deference**. Chapter 2 argues that people comply with signals of authority rather than with authority itself, which is why a uniform or a plausible letterhead works. My cards are letterhead. The monospace type, the framework identifier, the confidence field, the provenance footer: these are the visual grammar of a threat intelligence product, and I produced them in an afternoon with a Node script. A reader who has seen real intelligence products will find mine familiar, and familiarity is the cue.

The second is his material on **how framing and presentation shape what people accept**, the same mechanism that makes a well-designed phishing page work on people who know phishing exists. Knowing that a card is a simplification does not stop the simplification from operating. I built these cards, I know exactly which claims are soft, and when I laid all five out to check the rendering my own first impression was that I had a solid grasp of the threat landscape. I do not. I have five summaries of other people's reporting, two of which I would struggle to defend under questioning.

There is a loop here that I did not expect when I started. The course is teaching me to mark confidence and provenance so that I do not overstate what I know. Then it had me build an artifact whose format overstates on my behalf, using a generative tool that has no concept of restraint, about actors whose attribution is contested and in at least one case formally denied by the accused. The cards are a working demonstration of the failure mode the rest of the course is trying to train out of me.

**What I would want a reader of my cards to know that the cards do not say.**

That the confidence field describes my confidence in the sourcing, not the accuracy of the underlying claim. That two of the five actors are known primarily through vendor naming conventions that do not map cleanly onto government attribution, so the name on the card may not correspond to a single organisation. That `what_this_card_cannot_tell_you` is the most carefully written field on every card and is set in the smallest type on the layout, which is a design decision I made and should probably reverse.

And that I would not put these in front of anyone making a decision. They are study aids. If someone printed my XENOTIME card and pinned it in a control room, the card would not stop them, and nothing in its design would tell them not to.

---

## Time

| Session | Date | Hours |
|---|---|---|
| 1 | Sep 9 | 0.7 |
| 2 | Sep 11 | 1.0 |
| 3 | Sep 12 | 2.0 |
| 4 | Sep 14 | 0.8 |
| 5 | Sep 16 | 2.5 |
| 6 | Sep 19 | 2.0 |
| Reflection | Sep 20 | 1.0 |
| **Total** | | **10.0** |
