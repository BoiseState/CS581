# NRC Regulator Perspective

## 1. What to Look for During a 10 CFR 73.54 Inspection

As an inspector, I would look first for whether the plant has a living Cyber Security Program rather than a static compliance binder. The required program should identify Critical Digital Assets tied to safety, security, and emergency preparedness functions, document the CDA determination process, and show how defense in depth is implemented through architecture, procedures, monitoring, access controls, configuration management, incident response, and compensating controls.

I would ask for evidence that the plant understands dependencies, not only named systems. A CDA inventory is useful only if it captures data flows, maintenance interfaces, support laptops, removable media pathways, vendor access, time synchronization, backup systems, engineering workstations, and interfaces between lower and higher security levels.

I would also inspect whether implementation matches the licensee's own program. That means sampling assets, walking down network boundaries, reviewing change records, checking access lists, examining training records, and testing whether incident response procedures are current enough for the actual operational environment.

## 2. Where the Framework May Miss Real Security Failures

The framework may miss failures created by bad classification. If a plant excludes an asset from CDA status because the function looks indirect, but the asset can influence engineering configuration, operator awareness, or recovery, the formal program can be compliant while the real attack path remains exposed.

The framework can also miss human and economic failure modes. Anderson's readings make clear that attackers exploit workarounds, authority pressure, urgency, and usability friction. RG 5.71 and NEI 08-09 address training and program controls, but an inspection that focuses only on documented controls may miss informal practices such as shared local accounts, untracked portable media, or maintenance shortcuts.

Legacy systems create another inspection gap. Compensating controls can be valid, but they can also become a place where risk is accepted without enough operational testing. The regulator has to distinguish between a control that genuinely reduces risk and a paper justification for an unmodifiable system.

## 3. Questions for Plant Personnel

- "Show me a recent example where the CDA determination process changed because engineering found a new dependency."
- "Which cybersecurity controls create the most operational friction, and what workarounds have staff developed?"
- "How do you verify that vendor maintenance tools and temporary connections are removed or returned to a known state?"
- "Which legacy assets cannot be patched, and how do you test that compensating controls still work?"
- "If a trusted insider wanted to make an unauthorized but subtle configuration change, where would detection most likely occur?"
- "What plant state or outage activity creates the highest cybersecurity workload?"
