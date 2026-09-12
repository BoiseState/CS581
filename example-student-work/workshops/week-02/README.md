# Week 2 Example Student Work — Jordan Reyes

Continues the W1 example. Same fictional student, same tool, ten days later.

Read `session-log.md` first. In W1 it was the most useful file in the folder and that has not changed.

---

## What Jordan did differently this week

**Changed the W2 system before starting.** The W1 sequencing plan said RPS. Jordan switched to TCS and logged the revision in `workshops/week-01/sequencing-plan.md`, which is what the assignment asks you to do when a plan changes.

The reason is worth reading because it came out of the new `pivot_path` field. Jordan's own W1 OT map has a row for the data diode to RPS, outbound only. Trying to answer "how does the adversary move from my W1 system to my W2 system" against that row produced the answer "they cannot," which would have left the whole profile disconnected from the W1 work. Row 4 of the same map, the Modbus links to Level 1 devices, is a real path to balance-of-plant equipment. So TCS.

A field in a JSON schema changed the plan. That is the sort of thing that only happens if you fill the field in honestly.

**Left a failure in the profile.** One TTP, Manipulation of Control, carries a `system_relevance` value that says Jordan cannot map the technique to a TCS-internal component because he never built a TCS attack surface map. That admission stayed in. It marks the exact edge of what W1 bought him.

**Corrected himself, not just the model.** Session 3 records Jordan writing that Sandworm "has demonstrated intent to target nuclear generation," going to find the source, and discovering he did not have one. The rewritten `nuclear_targeting_evidence` field says plainly that there is no public evidence of nuclear targeting and that the relevance is architectural analogy. It is longer, less impressive, and correct.

**Verified the MITRE IDs by hand.** Seven of eight matched. One did not, and Jordan removed that TTP rather than guessing at the right number. Session 4 says explicitly that you should verify his numbers too, which is the right instinct to have about anyone's work including an instructor's example.

---

## On the cards

Five actors across four capability tiers: XENOTIME, CHERNOVITE, BERSERK BEAR, DarkSide, CyberAv3ngers.

The two non-nation-state cards are the ones Jordan learned from, and he only added them because the tier rule forced it.

- **DarkSide** encrypted IT systems only. Colonial halted the pipeline to contain the incident while assessing how far the compromise reached, and CISA and FBI reported no indication the ransomware directly affected OT. A criminal group with no ICS capability still produced a national fuel disruption, because the consequence came from an operator's containment decision rather than from a control-system effect.
- **CyberAv3ngers** broke the schema productively. It presents as hacktivist, CISA attributes it to IRGC-affiliated actors, and a `capability_tier` field holds one token. Jordan filed it as hacktivist, set confidence to `assessed`, and used `what_this_card_cannot_tell_you` to say the label does not survive the attribution.

`make-cards.js` generates the SVGs from `cards.json`, so fixing a fact and regenerating keeps the art and the data in sync. The sigils are procedural, seeded from a hash of the actor name, and every card carries a line stating that the sigil is not a likeness. No card depicts a person.

Jordan notes in the log that an image generator would have produced better-looking cards. He does not think they would have been more honest. **Either choice is fine for your submission.** That is his judgement, not a course requirement.

---

## What this example is not

- Not a ceiling. Jordan spent ten hours on W2. If yours goes deeper, good.
- Not the only defensible actor. Sandworm is one choice among many and the profile openly admits its nuclear relevance is inferred.
- Not a source. Verify the MITRE IDs, the advisory numbers, and the dates against the primary sources yourself. Jordan says the same thing in Session 4 about his own work.
- Not a template to copy. If your `pivot_path` reads like Jordan's, you have described his plant instead of yours.

---

## Files

| File | What it is |
|---|---|
| `session-log.md` | Six sessions plus the required card reflection. Read first. |
| `adversary-profile.json` | Sandworm profiled against TCS. 8 TTPs, 5 documented gaps. |
| `threat-cards/cards.json` | Five actors, four tiers. |
| `threat-cards/card-01..05.svg` | Generated cards. |
| `threat-cards/make-cards.js` | The generator. |
| `../../role-analyses/week-02/synthesis.md` | Nation-State Threat Analyst vs Insider Threat Investigator, grounded in Anderson Ch. 2. |
