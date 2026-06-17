# Case Deck: Modeling Syntax (Abacum)

**Best for:** Fintech and data-heavy product roles, roles that emphasize initiative and working across scope, "influence without authority" questions, "decision with no clear answer" questions.
**Duration:** 20-30 minutes including Q&A. Walk-through aim: 12-15 minutes.
**Lead framing:** A structural problem accumulating cost invisibly, no ticket, no right answer in the evidence. The Staff signal is the decision-making process when there's nothing to derive the answer from.

---

## Slide 1 — Cover

**Headline:** A structural problem no one had ticketed — and a decision with no right answer

**Subheadline:** Abacum, 2023. Formula syntax standardization across the modeling layer.

**Speaker notes:**
This case is about a problem I identified, made a case to work on, and solved, without a ticket, without a brief, and without an obvious answer at the end of the investigation. The interesting part isn't the output. It's the process of building enough confidence to make a judgment call when there's no established right answer and the evidence points in several directions at once.

---

## Slide 2 — Context

**Headline:** The modeling layer: the core of how Abacum works

**Visual:** Simple diagram of Abacum's architecture layer by layer: data layer, modeling layer (formulas, calculations), reporting layer, UI layer. Modeling layer highlighted.

**Speaker notes:**
Abacum is a financial planning product. The modeling layer is where the core logic lives: finance teams write formulas to define their models, run calculations, build their plans. This is the part of the product that power users spend most of their time in. When it's well-designed, it's invisible. When it's not, it's a daily source of friction.

I moved to the engine squad (responsible for this layer) after building the Dataset Manager on the integrations squad.

---

## Slide 3 — The observation

**Headline:** Formula syntax was inconsistent across different parts of the modeling layer

**Visual:** Side-by-side screenshots: the same logical concept expressed differently in two parts of the product. Examples of inconsistent syntax patterns annotated.

**Speaker notes:**
The inconsistency was visible to anyone who worked deeply with the product. The same formula concept (referencing a time period, aggregating a value, referencing another model) had different syntax in different parts of the modeling layer. Not different by design. Different because different engineers had built different parts over time without a shared standard.

No customer had filed a specific bug about this. No PM had identified it as a roadmap item. It was the kind of problem that shows up in support calls as users asking "wait, why does it work this way here but differently there?" A tax on every user who built formulas, slowly accumulating.

---

## Slide 4 — Making the case for looking at it

**Headline:** A problem with no ticket needed a case for existing

**Speaker notes:**
Before doing anything else, I had to justify spending time on this. The squad had a delivery roadmap. Pulling design time toward something that wasn't on the roadmap required an explanation.

The argument: syntax inconsistency was a tax that would compound as the product grew. New features built on top of an inconsistent layer would extend the inconsistency further. The longer this waited, the more expensive it became to fix. And the cost was already visible in support volume and in GONG recordings.

Getting head-of-design alignment on this was the first step. Working on it without that alignment would have been the wrong kind of autonomous.

[NOTE: Was there pushback on prioritizing this? If so, name it here and how you resolved it. If it was straightforward to get alignment, say that — "the evidence was clear enough that it wasn't a hard argument to make."]

---

## Slide 5 — The investigation

**Headline:** Competitor benchmark + customer call recordings

**Visual:** Split view: competitor analysis table (left) and GONG call evidence (right). Summary: no competitor had solved this cleanly.

**Speaker notes:**
The investigation had two parts.

First: competitor benchmarking. I looked at how other formula-based products (spreadsheet tools, financial modeling platforms, BI products) handled the same conceptual challenges. Not to copy a solution, but to understand whether anyone had solved this well enough to adapt.

Second: GONG recordings. I went through customer call recordings specifically to find moments where users expressed confusion about formula syntax. Not general product confusion — specifically the moments where a user was writing a formula and expected one syntax to work and found it didn't.

[NEEDS INPUT: One specific paraphrase from a GONG recording. Something like: "One customer said [X] — they had built the same formula twice because they didn't realize the syntax worked differently in reports than in the modeling view. They thought they'd made a typo." This specificity is what makes the evidence feel real rather than procedural. What's the clearest example you remember?]

---

## Slide 6 — No established pattern

**Headline:** Three approaches. None clearly right.

**Visual:** Evidence map with three columns, one per approach considered. Each column: the approach, what it solves, what it costs.

**Speaker notes:**
No competitor had solved this cleanly. That meant the answer wasn't derivable from looking at what others had done. I had to define the options and choose.

Three approaches were on the table.

[NEEDS INPUT: What were the actual competing approaches you considered? The structure would be:
- Approach A: [what it was, which competitor did something like it, what it would have cost users]
- Approach B: [what it was, what problem it solved, what it created]
- Approach C: [what you chose, why it was the least-bad option]

I'm not going to invent these because they're the central decision in the deck. What do you remember from the investigation? Even rough: "we considered standardizing on the syntax from part X, or building a superset that handled both, or just picking the more-used one as canonical."]

The decision couldn't be derived. It had to be built from the evidence: what were users already doing, what change would create the least relearning, what was the smallest intervention that removed the inconsistency. I had to build enough confidence in a direction to make a defensible call, rather than finding an objectively correct one.

This is a different kind of design problem than one that has a user research answer or a best practice answer. It required judgment, not just synthesis.

---

## Slide 7 — Engineering as a design partner

**Headline:** Direct collaboration with one engineer, not through a PM

**Visual:** Two-way collaboration diagram: designer and engineer working on syntax decisions together, not through an intermediary.

**Speaker notes:**
The syntax decisions were made in direct collaboration with one engineer, not routed through a PM or through a formal review process.

Why: the decisions were at a level of technical depth where a PM intermediary would have added translation overhead without adding value. The engineer and I could work through "what does this syntax actually produce in the model" together in a way that required both the design framing and the technical knowledge in the same conversation.

This is a collaboration model I've used before and find more effective for this kind of problem: not handoff, not presentation for approval, but two people working through a decision together with different information.

---

## Slide 8 — What changed

**Headline:** Consistent syntax across the modeling layer

**Visual:** Before/after: the inconsistent examples from slide 3, now standardized. The same concept expressed the same way in each context.

**Speaker notes:**
The output was a standardized syntax specification that covered the patterns used across the modeling layer. Not a redesign of the formula experience. Not new features. A consistent foundation.

The change was invisible to users who didn't already use the product heavily. For power users, the ones building complex models and spending hours in the product, it meant the product stopped asking them to remember two different ways to express the same thing.

---

## Slide 9 — Outcome

**Headline:** A new product capability became possible. Formula writing got cleaner. Support noise dropped.

**Visual:** Three outcome signals, with the editor suggestions project visually first and emphasized.

**Speaker notes:**
Three signals, and I'll name the first two as qualitative recollections, not measured data.

The clearest business outcome: the editor suggestions project. Once the syntax was consistent, it became possible to build intelligent suggestions on top of it, the kind that could predict what a user was trying to write. That project existed because this one had been done. A consistent foundation made the product worth building on. If I'd left the syntax inconsistent, suggestions would have had to accommodate two different syntaxes — which makes the suggestion logic far more complex, or useless in the parts of the product where users needed it most.

Formula writing got faster for experienced users. That's the team's read from the periods before and after. The support channel for formula questions got quieter, not silent, but the repeat confusion questions about "why does it work differently here" stopped appearing.

One thing I'd do differently: document the decision rationale more formally at the time. The syntax spec captured what was decided. The reasoning behind specific choices lived in conversation notes and wasn't easy for new engineers to reference when they needed to extend the syntax later. That documentation would have aged better than anything else I could have left behind.

---

## Q&A preparation

**"How did you decide what the right syntax was?"**
Evidence over preference. I started with what users were already using (the existing patterns, even the inconsistent ones) and looked for the least disruptive way to create consistency. Where there was no clear preference from usage data, I applied learnability principles: which syntax would a new user find most predictable? That wasn't always the one power users preferred, so I had to make calls and document the reasoning.

**"How did you manage this given it wasn't in your squad's roadmap?"**
I made the case to the head of design and got alignment before starting. I scoped the investigation to fit within available time — this wasn't a multi-month project that displaced roadmap work. And I reported out regularly so there were no surprises.

**"What would you do differently?"**
Document the decision rationale. The syntax spec captures decisions, not reasoning. When a new engineer needed to add a new syntax pattern six months later, there was no written record of why certain forms were chosen over others. That's the artifact that ages best — not the spec, but the reasoning behind it.

**"How did this connect to business outcomes?"**
Syntax inconsistency in a formula product is a retention risk: power users are the ones most likely to leave if the core tool is frustrating. And the editor suggestions project is the cleaner business signal — it was funded because this work existed. A new product capability became possible because a structural problem was resolved first.
