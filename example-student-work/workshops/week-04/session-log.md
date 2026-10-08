# Session Log — Workshop 4
## Jordan Reyes | Claude Opus 5.5 (Cowork) | Sep 28 – Oct 14, 2026

---

## Session 1 — Sep 28 | "Designing the RBAC policy"

**Duration:** ~90 minutes
**Outcome:** Draft RBAC policy written. Pushed back twice to replace generic controls with host-specific mechanisms.

**Prompt used:** "I need to write an RBAC policy for PSI. The system uses OSDP/Wiegand for badge control and has a web HMI with Basic Auth. Seven roles: Plant Operator, Supervisor, Cybersecurity Manager, Maintenance Technician, Vendor/Contractor, Emergency Response, IT Administrator. What should the policy look like?"

**What happened:** The first draft was completely generic — "access shall be restricted to authorized personnel," "multi-factor authentication shall be used for sensitive roles." None of it described what PSI actually does or what the host can actually enforce.

I pushed back: "The host uses authorized_keys for SSH access and Basic Auth for the HMI. There is no sudo. The OSDP controller is accessed over serial. Rewrite the policy to describe what the actual enforcement mechanisms are, not what they should be."

The second draft was better but still claimed the HMI enforced role separation on endpoints. I tested this manually: sent a POST to `/access/grant` using an operator credential and it went through. The AI had assumed endpoint-level authorization existed because I had described a Supervisor-only policy for that action. Assumption was wrong; I verified it was wrong.

Final policy revised to say what the mechanism is and what it cannot enforce. The "What This Policy Cannot Enforce" section came from this session.

**What the AI got wrong:** Assumed stronger controls than exist (Basic Auth → role enforcement on endpoints). Had to test to find the gap.

---

## Session 2 — Oct 9 | "Running Attack A — insider test"

**Duration:** ~60 minutes
**Outcome:** Attack A completed. AI initially misread the SIEM output. Caught and corrected.

**Prompt used:** "I'm going to run the insider attack from my W2 threat card. I'm going to grant maint-03 access to zone 4 using an operator session. Then I want to check what the SIEM logged. Help me interpret the SIEM event."

**What happened:** After running the curl command and checking the SIEM, I pasted the event record. The AI said: "The SIEM logged the event and attributed it to the operator user, which allows you to trace the action to the authenticated session."

That is wrong. The SIEM says `identity: operator`. The whole problem is that "operator" is a shared account — it does not trace the action to a person, only to whoever knew the credential. I pointed this out.

The AI revised: "You're correct — the `identity: operator` field names the account, not the individual who authenticated with that account. This does not satisfy the non-repudiation requirement in RG 5.71 Rev. 1, Appendix B, §B.2.10 because the record cannot rule out any person who knows the shared credential."

That revision is right and went into the adversary-test write-up.

**Lesson:** The AI was inclined to frame a partial log as sufficient attribution. "It logged the action" is not the same as "it logged who did the action."

---

## Session 3 — Oct 10 | "Running Attack B — supply chain via CSV import"

**Duration:** ~75 minutes
**Outcome:** Attack B completed. Unmonitored serial import path confirmed. Policy updated with compensating control.

**Prompt used:** "I want to do the supply chain attack. PSI imports credentials from a CSV file that gets pushed to /home/psi/data/hr_credentials.csv. I can replace that file and run the import script. Walk me through what would happen and whether the SIEM would catch it."

**What happened:** The AI predicted the SIEM would catch it because "any access control change should generate an audit event." I asked where in the code that event would be emitted. We looked at `import_credentials.py` together — it writes to the OSDP controller over serial and prints to stdout. No SIEM call anywhere in the script.

I ran the attack. No SIEM event. The AI had assumed an audit event would exist because the action was significant. That assumption is exactly the kind of error a security analyst gets wrong in a real system: things that *should* be logged often aren't.

Compensating control added to the RBAC policy: the import script now logs to an append-only file that the Cybersecurity Manager reviews weekly. Not as good as SIEM coverage, but implementable without hardware.

**What the AI got wrong:** Assumed audit coverage exists for significant actions. Real audit gaps are usually in the paths nobody expected to matter.

---

## Session 4 — Oct 11 | "Running Attack C — pivot with Ava"

**Duration:** ~2 hours (including coordination with Ava)
**Outcome:** Pivot completed. SIEM logged it. Policy revised to add PSI→RMS prohibition and compensating control.

**Prompt used (after agreeing the path with Ava):** "We're going to connect from psi to rms on port 5060 and write to Modbus register 3. Can you write a pymodbus script that does a FC16 write of value 0 to register 3 on unit 1?"

**What happened:** The AI wrote the script. It worked on the first try. The SIEM event on RMS showed `identity: PSI`, which was exactly what I was looking for — confirmation that the updated `_peer_seen` check would fire on this event.

The interesting part was what happened after I wrote up the result. I asked the AI whether the RBAC policy needed to cover this path. It said: "The RBAC policy doesn't need to explicitly cover this because it's an unexpected path — there's no design intent for PSI to reach RMS."

I pushed back: "The policy doesn't cover it, but the attack shows it's possible and the SIEM already flagged it. That gap should be in the policy whether or not there was design intent." The AI agreed and helped revise the policy to add the explicit prohibition plus the SIEM alert.

**Lesson:** The AI treated "not designed for" as the same as "not a policy concern." These are not the same thing. The attack revealed the gap; the policy needs to close it even for unintended paths.

---

## Reflection

**What worked:**
- Asking the AI to read actual files (the import script, the SIEM schema, `authorized_keys`) before making claims about what the system could enforce. Every useful correction in this workshop came from pointing at a concrete file and asking the AI to explain what it actually does.
- The W2 threat cards were useful starting points for framing each attack. Having written the hypothesis about the actor and the TTP made it easier to ask the AI what evidence to look for.

**What did not work:**
- Asking the AI general questions about what "should" be logged or what "should" be enforced. It consistently answered with what a well-designed system would do, not with what this system does. The gap between those two answers is most of what W4 is about.
- The AI on Session 2 framed partial attribution as sufficient attribution. That took one correction. On Session 4 it framed "unintended path" as "not a policy concern." That took another correction. The pattern: the AI tends to resolve ambiguity in the direction of "things are working correctly." The useful question is always "show me where in the code that is enforced."

**What I would do differently:**
- Start with the actual code and config files rather than a description of the system. Every time I described PSI in the abstract, the AI made assumptions. Every time I showed it the actual script, it gave useful analysis.
- Run the attacks earlier in the week. I started designing the policy on Sep 28 but did not run attacks until Oct 9. That compressed the revision time.

**Time spent:**
- Reading (W4 assignment, RG 5.71, NEI 08-09, NIST SP 800-82): ~3 hours
- AI sessions: ~5.5 hours across four sessions
- Writing and editing (policy, annotation, adversary-test, runbook): ~4 hours
- Partner coordination (Ava): ~30 minutes
- Total: ~13 hours
