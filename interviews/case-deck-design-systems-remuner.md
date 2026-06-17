# Case Deck: Design Systems at Remuner

**Best for:** Founding designer roles, sole-designer contexts, early-stage companies that need infrastructure built from scratch.
**Duration:** 25-35 minutes including Q&A. Walk-through aim: 15-20 minutes.
**Lead framing:** Lessons applied deliberately from a larger context to a smaller, constrained one. Every decision was shaped by what I'd watched fail at scale. The production incident that hardened the pipeline is the learning arc, not a footnote.

---

## Slide 1 — Cover

**Headline:** A design system as the sole designer at a startup

**Subheadline:** Remuner, 2024-2026 — from fragmented implementation to a production system with CI enforcement

**Speaker notes:**
This is the design systems work I did at Remuner. Context upfront: I was the sole designer. No design team, no design infrastructure when I arrived. The story is about what decisions you make when you have prior experience to draw on, real constraints on bandwidth, and a production incident that forces you to rethink what "done" means for infrastructure work.

---

## Slide 2 — Starting condition

**Headline:** Not a bad-looking product. A fragmented implementation.

**Visual:** Diagram or screenshot comparison: the product UI on the left (looks reasonable), the implementation layer on the right (each FE with their own component implementation, MUI defaults filling gaps, zero Figma components).

**Speaker notes:**
When I joined Remuner, the product's visual design was acceptable. But implementation was fragmented: each engineer had built their own component set, with MUI defaults filling gaps. There were zero Figma components. Every screen was a one-off.

The problem wasn't that the product looked bad. The problem was that there was no shared contract between design and development. Every screen I designed had to be implemented from scratch by whichever engineer picked it up.

---

## Slide 3 — The constraint

**Headline:** Sole designer. Product work can't stop.

**Visual:** Timeline: 2 FEs at hire, 5 FEs at departure. Single designer icon across the whole timeline.

**Speaker notes:**
Three constraints shaped every decision I made on this system.

First: I was the sole designer. There was no one else to own the DS work while I handled product delivery. If I spent three months building a design system, three months of product design work wouldn't happen.

Second: the engineering team was growing. Two frontend engineers when I joined, five by the time I left. A growing team without a shared system gets messier faster — each new engineer would pick up the same fragmented patterns and extend them further.

Third: the budget was smaller than Abacum. I couldn't replicate what I'd built there at the same scope, and I had to decide up front what that meant for the system.

---

## Slide 4 — Applied lesson

**Headline:** What I decided not to build — and why

**Visual:** Side-by-side: Abacum token set (broader scope) vs Remuner token set (tighter scope). Annotation: "complexity is debt you pay later." Explicit list of what was deferred on the right.

**Speaker notes:**
At Abacum, the token set grew broad. That created a maintenance problem: the more tokens, the more opportunity for drift, the more decisions needed when a new surface appeared.

At Remuner, I started with a smaller, more constrained set. The principle: start with what you need for current surfaces, extend deliberately. Avoid the trap of building a system for a hypothetical future product instead of the actual one.

[NEEDS INPUT: What specifically did you decide not to build at Remuner? The most useful version of this slide names the scope decisions. Something like:
- Deferred: animation tokens (no motion design in scope yet)
- Deferred: elevation/shadow system (used one level only)
- Deferred: full icon system (minimal set first, expanded later)
- Not built: custom chart/data visualization tokens (third-party library handled it)

What categories of token or component were you explicit about not building at the start? What did you defer deliberately?]

This decision came from watching what went wrong at larger scale. Constraint as a design principle, not a limitation.

---

## Slide 5 — Speaking the same language

**Headline:** Tokens exported as Sass variables and utility classes

**Visual:** Token in Figma on the left → exported as both `$color-text-primary` (Sass variable) and `.text-primary` (utility class) on the right.

**Speaker notes:**
The engineers at Remuner used Vuetify as the component framework. Vuetify uses Sass variables. The engineers already thought in Sass variable syntax.

If I'd exported tokens only as CSS custom properties or JSON, there would have been a translation layer. Every engineer would have to map the new system onto the vocabulary they already used. Instead, I exported tokens in both formats: Sass variables and utility classes that matched Vuetify conventions.

This decision came out of the monthly FE meetings. Not top-down. The engineers told me what format made sense for their workflow, and I built to that.

---

## Slide 6 — Pipeline

**Headline:** Token Studio → Style Dictionary → GitHub → Vuetify / Storybook

**Visual:** Pipeline flow diagram. Annotations: which parts came from the Abacum work, which parts were adapted, what was added in Feb 2026.

**Speaker notes:**
The pipeline foundation came from my Abacum work. I brought it in; the engineers adapted it to Remuner's stack (Vuetify, Sass variables). That's the honest version of what I own and what the team did.

The pipeline at this point was functional. But it wasn't trustworthy. What happened next changed how I thought about that distinction.

---

## Slide 7 — The production incident

**Headline:** The token repo was production infrastructure. I didn't treat it that way.

**Visual:** Timeline of the incident: token file deleted → next deploy → app down → file recovered → fix → structural rethink.

**Speaker notes:**
The token repo was a production dependency: token files fed directly into the front-end app. I deleted a file I assumed was a duplicate without checking if it was referenced. It was. The next deploy brought the app down.

The app was down for several minutes. Visible to anyone using it, and to engineering.

The immediate fix was straightforward: recover the file, push a fix. But the structural response mattered more: I'd been treating a production-coupled file like a design asset you can tidy up casually. That was the mistake. The incident made clear that the pipeline needed to be governed as infrastructure, not as a working folder.

---

## Slide 8 — What hardened the pipeline

**Headline:** CI enforcement, drift detection, and a preview sandbox

**Visual:** Before/after: pipeline without guards vs pipeline with CI gates, drift checks, smoke tests, HTML sandbox. The additions annotated.

**Speaker notes:**
In February 2026, I hardened the repo using AI assistance. I'm naming that directly rather than obscuring it: I used Codex to work through the implementation step by step, with an engineer reviewing and merging each stage.

What that produced: a CI pipeline that catches breaking changes before they reach a deploy, drift detection to flag when the token values in the repo diverge from the design file, a W3C token format migration for standards compliance, an HTML sandbox for previewing what a token change actually looks like before it ships, smoke tests, and JSON output for JavaScript consumers.

None of that was in a spec. It came from asking what the pipeline needed to be trustworthy, not just functional. The production incident accelerated work that should have been proactive.

This is also the moment worth naming explicitly: a designer building CI infrastructure with AI assistance is a different kind of ownership than existed before these tools. The brief was precise enough that the implementation could be delegated and validated. That changed what "a designer can own this" means technically.

---

## Slide 9 — Governance

**Headline:** Monthly FE meetings as the operating mechanism

**Visual:** Meeting agenda format: progress update, open problems, goals for next month. Repeated cycle.

**Speaker notes:**
Governance at Remuner was simpler than Abacum, because the team was smaller. Monthly meetings where every frontend engineer presented what they'd built, surfaced problems, and set goals for the next month.

This had two functions. One: a regular checkpoint to catch drift before it became debt. Two: it kept the system from being "the designer's thing." The engineers were active participants in its operation, not consumers of a document I maintained.

---

## Slide 10 — The product audit

**Headline:** Systematic capture of every pattern, running alongside product work

**Visual:** Spreadsheet or Notion view: pattern name, instances found, variants defined, ticket created, fix-now / defer decision.

**Speaker notes:**
Throughout my time at Remuner I ran a continuous product audit: systematically capturing all instances of a pattern across the product, defining the variants and states it needed, creating tickets, and deciding fix-now versus defer-into-an-upcoming-feature.

The deferral judgment is where most of the work was. Not every inconsistency was worth fixing immediately. Some were cheap to fix and high-visibility. Others were deep in an edge-case flow that engineering couldn't afford to touch. Knowing when to defer is as important as knowing what to fix.

---

## Slide 11 — Outcome

**Headline:** "From a 2010 app to a 2020 app" (CTO, unprompted)

**Visual:** The CTO quote large on the slide. Below it: three behavioral signals that produced it.

**Speaker notes:**
The CTO said this during a review session, unprompted, after the audit had been running for several months. It reflected product-wide change, not a Figma library existing. That distinction matters: a DS that lives only in design files doesn't move a product's visual coherence. This comment came from the systematic audit changing how the product actually looked and behaved.

Three behavioral signals behind it.

Engineers started referring to tokens by name in code reviews: `color-text-primary` instead of `#2D2D2D`. Hardcoded hex in a PR became a caught violation. The ESLint rule made it structural, not cultural.

A designer joined the team late in my tenure. She built a screen quickly and flagged adjustments — not because something was broken, but because the system had what she needed and she trusted it enough to say when it didn't. That feedback loop is the signal, not just the speed.

[NEEDS INPUT: One specific product feature or screen that shipped faster, or required less back-and-forth, because the DS components existed. Something like "the [feature name] shipped in two days instead of the usual week because the admin table pattern was already in the system." What's one real example you remember where the DS visibly changed the pace or quality of a delivery?]

One thing I'd do differently: harden the pipeline proactively, before something goes wrong. The CI infrastructure came from a production incident. That's the right learning to take from it, but the timing shouldn't have required an outage to trigger.

---

## Q&A preparation

**"What would you do differently?"**
Harden the pipeline earlier. I treated the token repo as a design asset for too long before I understood it needed to be governed as infrastructure. The production incident accelerated work that should have been built into the initial setup.

**"How did you balance DS work with product delivery?"**
The start-small approach was the mechanism. Rather than building a complete system before shipping anything, I built the minimum viable token set and governance structure, then extended it as product work revealed gaps. The monthly FE meetings kept it from drifting without requiring dedicated allocation.

**"How did this connect to business outcomes?"**
A DS at a startup with a growing engineering team is a velocity investment. Without it, every new feature is designed and built as a one-off, and each new engineer extends the inconsistency. With it, there's a shared contract that reduces decision overhead on every screen. The CTO's comment points to something beyond velocity. The product was visibly coherent in a way it hadn't been, which matters for enterprise sales.

**"What's the difference between what you built here and at Abacum?"**
Scale, constraints, and approach. Abacum: co-led a business case, worked with an engineering team that built the original pipeline, governed across five squads. Remuner: sole designer, adapted and owned the pipeline, smaller token scope by design. The same principles, applied with the constraints of a smaller team and a narrower budget. And a harder lesson learned about the difference between infrastructure that's functional and infrastructure that's trustworthy.
