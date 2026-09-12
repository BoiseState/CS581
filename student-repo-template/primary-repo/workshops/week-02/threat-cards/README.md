# Threat Cards — Workshop 2

Five actors beyond the one in `adversary-profile.json`. Stat-line depth, not full depth.

## What goes here

- `cards.json` — the data behind the five cards. Must parse as valid JSON.
- `card-01` through `card-05` — one file per actor, any extension (`.svg`, `.html`, `.png`, `.jpg`).

## Style

Yours. Baseball card, Pokemon card, tarot, trading card, anime, whatever you find fun.

Every card must legibly show:
- actor name
- capability tier
- signature TTP with its MITRE ATT&CK for ICS ID
- a provenance line naming a public source

## How to make them

Ask your coding assistant to emit each card as SVG or HTML. Costs nothing, keeps files small and diffable,
and getting an agent to produce clean SVG is itself a useful exercise. If you already have access to an
image generator you may use it instead. Do not buy a subscription for this assignment.

## One hard rule

**No card may depict a real person.** Original characters, mascots, creatures, emblems, and abstract art
are all fine. Art that presents itself as showing what a real operator looks like is not.

Several actors you will look at are tied to named individuals under federal indictment, including in
CISA advisory AA22-083A on this module's reading list. Inventing faces for them is the one thing this
assignment will not accept.

## Grading

Cards are scored on whether the stat lines are accurate and sourced, not on artistic quality.
A hand-drawn card photographed with your phone scores the same as a polished render if the data is right.
