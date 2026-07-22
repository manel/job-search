# Case Deck: Modeling Syntax (Abacum)

**Best for:** Fintech and data-heavy product roles, roles that emphasize initiative and working across scope, "influence without authority" questions, "decision with no clear answer" questions.
**Duration:** 20-30 minutes including Q&A. Walk-through aim: 12-15 minutes.
**Lead framing:** A structural problem accumulating cost invisibly, no ticket, no right answer in the evidence. The Staff signal is the decision-making process when there's nothing to derive the answer from.

---

## Slide 1 — Cover

**Headline:** A structural problem no one had ticketed. A decision with no right answer.

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

**Headline:** Benchmark across four competitors + customer calls

**Visual:** Split view: competitor syntax comparison table (Excel, Google Sheets, Pigment, Causal) on the left, GONG call evidence on the right. Abacum marked as the outlier on both parentheses and naming conventions.

**Speaker notes:**
The investigation had two parts.

Competitor benchmarking across Excel, Google Sheets, Pigment, and Causal. Not to copy a solution, but to find whether there was a consensus. There was: every one of them placed parameters inside parentheses and avoided underscores in function names. Abacum was the outlier on both counts.

Customer call recordings. One call stood out: an enterprise customer's team described spending months with the implementation team just to get comfortable writing basic formulas. They said they wished it felt more like Excel. That's a specific signal: not "this is hard" but "I already know how it should work and this doesn't match."

Together these told me the inconsistency wasn't just internal. It was Abacum diverging from every established reference its users already knew.

---

## Slide 6 — Two options. One obvious loser.

**Headline:** SQL-aligned or Excel-aligned — the users already had a preference

**Visual:** Side-by-side: SQL-style syntax (FROM dataset WHERE condition, external clauses) vs Excel-style (all parameters inside parentheses, no external clauses). User background on the right: finance teams, not SQL developers.

**Speaker notes:**
The core decision was which direction to align with.

Option one: SQL-aligned. Keep the FROM and WHERE style for dataset references, which was already in parts of the product. SQL users would find it familiar. The problem: Abacum's users are finance teams, not SQL developers. The customer call was the signal — they wanted Excel, not SQL. And SQL-style external clauses meant each formula was a slightly different pattern depending on where it appeared.

Option two: Excel-aligned. All parameters inside parentheses, no external clauses, function names as single capitalised words with no underscores. Every competitor did this. Every user already knew it from Excel.

The tradeoff was real: users coming from a SQL background would find the new syntax less natural at first. That's a cost worth naming. But for the actual user base, finance professionals writing financial models, the consistency of Excel conventions reduced the overall learning curve and made complex formulas easier to read and debug.

The decision was also a commitment: we produced the Abacum Script, written guidelines for syntax conventions, so any new function added in the future would follow the same rules without requiring a design review each time. The consistency had to be self-sustaining, not dependent on the team remembering what was decided.

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

**Headline:** Days instead of weeks. Suggestions became possible. Adding new functions stopped being a judgment call.

**Visual:** Three outcome signals: onboarding speed, editor suggestions project, Abacum Script governance. Suggestions project visually emphasized.

**Speaker notes:**
Three signals.

The clearest product outcome: the editor suggestions project. Once syntax was consistent and all parameters were in a predictable position inside the function, it became possible to map parts of a formula to interface elements — inputs, previews, type-aware suggestions. That project existed because this one had been done. With SQL-style external clauses still in place, you couldn't build that: the parameter position wasn't predictable enough to drive suggestions reliably.

The customer signal: new users went from taking weeks to write their first useful formula to reaching it in days. The enterprise customer on that call described months of onboarding support. After the redesign, formula-related support requests dropped over the following quarters. That's a qualitative recollection from the CS team, not a dashboard number, but it was consistent across customers.

The governance outcome is the one that ages best: the Abacum Script. Written guidelines for syntax conventions, produced as part of this work. Any new function added after that followed the same rules without requiring a design review. The consistency became self-sustaining.

One thing I'd do differently: document the decision rationale, not just the decisions. The Abacum Script captured the conventions. The reasoning behind specific calls — why SQL-style was rejected, why single capitalised words were chosen over underscores — lived in meeting notes. When a new engineer needed to extend the syntax, there was no written record of the reasoning, only the output. That's the thing that would have aged better.

---

## Q&A preparation

**"How did you decide what the right syntax was?"**
Evidence over preference. I started with what users were already using (the existing patterns, even the inconsistent ones) and looked for the least disruptive way to create consistency. Where there was no clear preference from usage data, I applied learnability principles: which syntax would a new user find most predictable? That wasn't always the one power users preferred, so I had to make calls and document the reasoning.

**"How did you manage this given it wasn't in your squad's roadmap?"**
I made the case to the head of design and got alignment before starting. I scoped the investigation to fit within available time — this wasn't a multi-month project that displaced roadmap work. And I reported out regularly so there were no surprises.

**"What would you do differently?"**
Document the decision rationale alongside the spec. The Abacum Script captured the conventions. The reasoning behind specific calls — why SQL-style was rejected, why single capitalised words over underscores — lived in meeting notes. When a new engineer needed to extend the syntax later, there was no written record of the reasoning, only the output. The reasoning is the thing that ages better.

**"How did this connect to business outcomes?"**
Syntax inconsistency in a formula product is a retention risk: power users are the ones most likely to leave if the core tool is frustrating. And the editor suggestions project is the cleaner business signal — it was funded because this work existed. A new product capability became possible because a structural problem was resolved first.
