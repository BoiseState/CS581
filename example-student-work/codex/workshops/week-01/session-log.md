# Session Log for Attack Surface Map

## Initial Prompt

The initial task prompt asked Codex to build a structured attack surface map for a generic US nuclear power plant using only publicly available information. It required three layers: IT (Corporate), OT (Operational Technology), and Physical/Cyber Intersection. Each layer needed a table with Component, Role, Threat Vectors, and Notable Gaps, followed by a layer summary. The prompt also required documented incidents to be flagged separately from general architectural knowledge.

The first expected output shape was a straightforward set of three tables. The risk with that initial shape is that a model can make the table look complete while silently implying facility-specific knowledge it does not have.

## Changes Made and Why

I changed the map to emphasize what cannot be known from public information. The "Notable Gaps" column was written to prevent the table from becoming a fake assessment. For example, instead of saying an engineering workstation is vulnerable in a specific way, the map identifies generic threat vectors and then states that actual workstation hardening, access control, and media procedures are facility-specific.

I also added a separate "Documented Incident Flags" section. This was necessary because Stuxnet and Davis-Besse are often invoked in nuclear cyber discussions, but they are not the same kind of evidence. Davis-Besse is relevant to nuclear plant support-network risk. Stuxnet is relevant to industrial-control attack patterns, but it should not be treated as evidence about a specific US commercial plant's exposure.

Finally, I expanded "What This Map Cannot Tell You" into a real limitation section. The most important missing inputs are CDA boundaries, data flows, installed vendors and versions, control implementation quality, operating constraints, human behavior, and consequence analysis. Without those, the map is only a generic orientation tool.

## What I Would Do Differently Next Time

If I ran this session again, I would start by asking for the instructor's preference on citations and source style. I would also build a small source matrix before drafting the table, separating regulatory guidance, industry guidance, and incident evidence. That would make it easier to audit which claims come from assigned readings and which come from outside public examples.

I would also produce two versions of the map: a student-facing overview and an inspector-facing checklist. The overview would explain the categories, while the checklist would list evidence needed to convert the generic surface map into an assessment.

## Domain-Knowledge Observation

The readings made it easier to notice when the model output risked sounding too confident. Anderson's distinction between safety and security highlighted why human workarounds and adversarial behavior belong in the physical/cyber layer. RG 5.71 and NEI 08-09 made the CDA determination process stand out as the real boundary-setting step. Without that domain knowledge, I might have accepted a generic IT/OT table as complete even though it could not support any facility-specific conclusions.
