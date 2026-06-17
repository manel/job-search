# Case Deck: Design Systems at Abacum (Abax)

**Best for:** DS-titled roles, staff-level interviews, roles that ask about cross-functional influence and working without mandate.
**Duration:** 30-40 minutes including Q&A. Walk-through aim: 18-22 minutes.
**Lead framing:** The business case, not the components, is the story. The interesting decision was building the argument before anyone asked for the system, framing cost in engineering terms rather than design terms, and designing the governance to outlive the person who built it.

---

## Slide 1 — Cover

**Headline:** Building a design system no one asked for

**Subheadline:** Abacum, 2022-2024. From scattered components to a company-sanctioned initiative across five squads.

**Speaker notes:**
I'm going to walk you through the design system work I did at Abacum. The framing upfront: this story isn't primarily about component design. It's about how a design system gets adopted at a company that didn't have one, when no one gave you a mandate to build it, and when the people you need to convince are engineers who have legitimate reasons to be skeptical.

---

## Slide 2 — Context

**Headline:** Five squads, one growing product, no shared foundation

**Visual:** Simple diagram: 5 squads (Integrations, Engine, Reporting, Collaboration, Admin) around a product core. Each with their own component implementations marked.

**Speaker notes:**
Abacum is a B2B financial planning product. Complex data modeling, multi-user workflows, finance teams as end users. When I joined the integrations squad in early 2022, there were five product squads building independently. There was no design system. Every squad had its own implementation of buttons, form fields, modals. The product worked. But inconsistency was accumulating across every surface.

---

## Slide 3 — The real problem

**Headline:** Inconsistency wasn't just a visual problem

**Visual:** Side-by-side screenshots of the same UI pattern (a button, a table cell, a dropdown) implemented differently across two squads.

**Speaker notes:**
You could frame this as "the product looks inconsistent." That's accurate. But that framing doesn't get engineering buy-in, because it sounds like a designer preference.

The real cost was operational. Every squad was maintaining their own version of every component. When something needed to change, it had to change in five places. Bugs that were fixed on one squad reappeared on another. A typography update, a color change, a behavior fix to a Button: five separate implementation tasks, with a real chance they'd land slightly differently on each squad. And from a customer perspective, inconsistency signals immaturity. It creates a perception of a product that isn't quite finished.

That second framing was the one that mattered for building the business case.

---

## Slide 4 — Nobody asked for this

**Headline:** No mandate. No ticket. A choice about whether to wait or act.

**Speaker notes:**
There was no initiative to build a design system. No PM owned it. No engineering team was allocated to it. I was on a product squad with regular delivery commitments.

The decision was whether to treat this as someone else's problem or to build the argument. I chose the second. Together with the head of design, I started building a business case (not a design brief) that we could present to engineering leadership.

---

## Slide 5 — The business case

**Headline:** Framing the cost of not having a system

**Visual:** The actual presentation or a close recreation: inconsistency screenshots on the left, annotated as "these signal immaturity to customers." Engineering concerns addressed on the right. The counterfactual cost framed in engineering terms.

**Speaker notes:**
The presentation had three parts.

First: evidence of the problem. Screenshots of inconsistencies across squads, categorized by component type. Buttons, cells, menus. Framed not as "this looks bad" but as "this signals immaturity to customers."

Second: engineering's own objections, named before they raised them. We knew the concerns: "side project," "co-prioritization," "squads don't have a platform picture." We addressed each one directly rather than ignoring them.

Third: the counterfactual cost. Five squads, each maintaining independent components. Any change to a shared UI pattern — a typography update, a color rebrand, a button behavior change — had to happen five times independently. Over time, that's not just slower. It's the kind of thing that creates incidents: one squad ships the fix, another doesn't pick it up for two weeks, a third ships a slightly different version. The DS wasn't an investment in aesthetics. It was a cap on a compounding maintenance tax.

The ask was small: get the system selected as a Maker Days initiative, where squads had dedicated time outside regular delivery. Not a full-time team. A quarterly slot to prove the concept worked.

---

## Slide 6 — The win: Maker Days

**Headline:** The DS gets selected as a quarterly initiative

**Speaker notes:**
Maker Days was a quarterly initiative at Abacum where teams competed for dedicated time on non-roadmap work. Getting the DS selected meant converting it from a side project to a company-sanctioned initiative.

That distinction mattered more than I expected. Before Maker Days, working on the DS was discretionary time. After: it had an official slot, competed against other initiatives, and had a formal outcome expected from it. That changed how engineering engaged with it.

---

## Slide 7 — Architecture decisions

**Headline:** Two decisions made early that constrained everything that followed

**Visual:** Diagram of two-tier token architecture: primitive layer (raw values: colors, spacing) + semantic layer (contextual names: color-text-primary, space-component-padding). Below it: MUI component library as base.

**Speaker notes:**
Two decisions shaped the whole build.

First: keep MUI as the base component library rather than building from scratch. Three of five squads were already deep in MUI. Replacing it meant rewriting every component across all five squads — with no immediate product benefit, requiring a level of engineering buy-in we didn't have, and impossible to scope into the Maker Days quarters we were working in. The constraint wasn't just that it would take longer. It was that the ask had to be achievable in increments the team could justify. Building on MUI made each quarter's work shippable.

Second: a two-tier token architecture. Primitive tokens hold the raw values. Semantic tokens hold the contextual meaning: `color-text-primary` rather than `#1A1A1A`. The semantic layer is what lets you change a primitive value without hunting for every usage across the codebase. This came from thinking about what the system would need to stay maintainable, not just what was needed for the first few components.

---

## Slide 8 — The pipeline

**Headline:** Token Studio → Style Dictionary → GitHub → npm → ESLint

**Visual:** Linear flow diagram of the pipeline. Each step labeled with what it does.

**Speaker notes:**
An engineer built the original pipeline. My job was understanding it well enough to reason about decisions within it and to govern what went in.

Token Studio is the Figma plugin that manages the token values. Style Dictionary transforms them into platform-specific formats: CSS variables, Sass variables, JSON for JavaScript consumers. The output goes into a GitHub repo, then into an npm package that squads import. ESLint rules enforce adoption: using a hardcoded hex instead of a token raises a linting error.

The enforcement piece was deliberate. Without it, adoption is voluntary and tends to slip under deadline pressure. Trust is not an adoption strategy.

---

## Slide 9 — Proof: the Button

**Headline:** First component shipped end-to-end in one Maker Days week

**Visual:** Before/after of the Button component, or a screenshot from Storybook. The pipeline diagram with all steps highlighted.

**Speaker notes:**
The Button was the first component we took from design spec through the full pipeline: Token Studio → Style Dictionary → npm → ESLint. We did it in one Maker Days week.

That sounds unremarkable. What it was: proof that the pipeline worked as a system. Before that, the pipeline existed as a design. Afterward, it existed as a fact. That changed the team's confidence in everything that came after. The Button wasn't the important component. It was the proof of concept that made every subsequent component easier to justify.

---

## Slide 10 — Governance

**Headline:** What kept it working for 8+ months

**Visual:** Four-column layout: issue reporting, feature flag releases, weekly sync, two-library Figma structure. Each with a one-line note on what failure mode it was designed to prevent.

**Speaker notes:**
Most DS case studies show the build. This part is what usually gets skipped, and it's where most systems fail.

Structured issue reporting: components reported to a Slack channel, categorized, tracked in Notion. Without this, problems accumulate invisibly until a squad decides to work around the system rather than report the issue.

Feature flags for new component releases: squads could adopt on their own timelines without creating inconsistency during transition. The alternative — releasing a new component and expecting all five squads to adopt it immediately — would have created a period where some squads were on the new component and others weren't. Mid-transition inconsistency is worse than no system at all.

A standing weekly design library sync: keeps decisions from piling up and becoming blockers.

The two-library Figma structure was something I proposed and drove: an Exploration file, prefixed [Experiment], for components under development, and a separate canonical Implementation file for anything production-ready. This prevented the library from becoming a graveyard of in-progress work that no one could tell was ready to use.

---

## Slide 11 — Real tensions

**Headline:** The hard decisions were not in the spec

**Visual:** Three cards: "Component naming debates," "Read-only state (engineers vs designers)," "Deprecated components in search." The third card expanded with the resolution.

**Speaker notes:**
Three tensions worth naming.

Naming debates: consistent naming is harder than it sounds. What one squad called a "cell" another called a "chip." These arguments look trivial from outside but they're load-bearing for adoption. If engineers can't find the component by its name, they build their own.

Read-only state: engineers and designers had genuinely different mental models of what "disabled" and "read-only" meant in the system. Resolving it required both sides articulating their mental model separately, then finding where the actual difference was rather than arguing about the label.

The deprecated components in search is the one worth going deeper on because it had three real options and a non-obvious right answer.

[NEEDS INPUT: What were the three trade-off solutions you identified for deprecated components appearing in search?
Rough guesses at what the options might have been:
- A: Manually remove deprecated components from the library each time one is deprecated (fast, but creates ongoing maintenance burden)
- B: Add a naming convention to mark deprecated components visually, so they appear in search but are clearly labeled (medium effort, doesn't remove the problem but reduces confusion)
- C: Move deprecated components to a separate, non-searchable Figma file (most work upfront, removes the problem at the source)

What were the actual three options? And which did you choose — and why wasn't it the fastest one?]

These are the decisions that determine whether a DS actually gets used. They don't get made by writing components. They get made in conversations.

---

## Slide 12 — Outcome

**Headline:** Five squads, enforced adoption, and a system that ran without me

**Visual:** Coverage diagram — 5 squads marked as covered. ESLint adoption rule highlighted. Storybook / Chromatic screenshot.

**Speaker notes:**
By the end of my time at Abacum, Abax covered all five squads. Adoption was enforced at the linting layer, not on trust. Storybook deployed in Chromatic gave engineering a running reference that stayed in sync with the library.

[NEEDS INPUT: One concrete before/after that shows what the DS enabled. Something like: "New engineers joining could ship their first UI component in a day rather than spending the first week understanding what pattern to follow across five squads." Or a feature that shipped noticeably faster. What's one real example you remember?]

The system didn't require me to be in the room for it to work. That was the outcome I was aiming for: infrastructure that operates independently of the person who built it. If I had left and nothing changed in how the squads worked, the DS had succeeded. If it needed me to maintain it, it was still a side project.

One thing I'd do differently: the naming governance for tokens. The semantic layer was correct, but naming conventions drifted over time as new tokens got added by different people without a clear standard. I'd establish that explicitly and earlier — not as a document, but as a review step in the contribution process.

---

## Q&A preparation

**"What would you do differently?"**
The token naming governance. The semantic layer was correctly architected, but the naming conventions drifted as the system grew and different people added tokens. I'd make naming governance an explicit step in the contribution process rather than a document people read once.

**"How did you handle disagreement in the team?"**
Name the read-only state debate. Two sides with legitimate reasoning. Resolution came from asking both to write down their mental model separately, then finding where the difference actually was, not where they thought it was. The disagreement wasn't about which name to use — it was about two genuinely different models of what the state meant. You can't resolve that by picking a word.

**"How did this connect to business outcomes?"**
Five squads maintaining independent components means a shared UI change happens five times, with a real chance of subtle inconsistency across implementations. The DS doesn't eliminate that cost immediately, but it caps its growth. And the ESLint enforcement means it doesn't degrade over time under deadline pressure. For customers, a consistent product surface signals a product worth trusting — which is a sales and retention argument, not just an aesthetics one.

**"What was your specific contribution vs the team's?"**
Co-led the business case with the head of design. Drove the two-library Figma structure and the governance process. Defined the token naming conventions. I didn't build the original pipeline — an engineer did. I owned what happened inside it: the governance, the contribution process, the decision-making on tensions.
