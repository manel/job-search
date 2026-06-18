# Case Deck: Design Systems at Remuner

**Best for:** Founding designer roles, sole-designer contexts, early-stage companies that need infrastructure built from scratch.
**Duration:** 25-35 minutes including Q&A. Walk-through aim: 15-20 minutes.
**Lead framing:** Lessons applied deliberately from a larger context to a smaller, constrained one. Every decision was shaped by what I'd watched fail at scale. The production incident that hardened the pipeline is the learning arc, not a footnote.

---

## Slide 1 — Cover

**Headline:** A design system as the sole designer at a startup

**Subheadline:** Remuner, 2024-2026. From fragmented implementation to a production system with CI enforcement

**Speaker notes:**
This is the design systems work I did at Remuner. Context upfront: I was the sole designer. No design team, no design infrastructure when I arrived. The story is about applying what I'd learned at Abacum under tighter constraints, and about a production incident that changed what "done" means for infrastructure.

---

## Slide 2 — Starting condition

**Headline:** Not a bad-looking product. A fragmented implementation.

**Visual:** Diagram or screenshot comparison: the product UI on the left (looks reasonable), the implementation layer on the right (each FE with their own component implementation, MUI defaults filling gaps, zero Figma components).

**Speaker notes:**
When I joined Remuner, the product's visual design was acceptable. But implementation was fragmented: each engineer had built their own component set, with MUI defaults filling gaps. There were zero Figma components. Every screen was a one-off.

The product looked fine. There was no shared contract between design and development. Every screen I designed had to be implemented from scratch by whichever engineer picked it up.

---

## Slide 3 — The constraint

**Headline:** Sole designer. Product work can't stop.

**Visual:** Timeline: 2 FEs at hire, 5 FEs at departure. Single designer icon across the whole timeline.

**Speaker notes:**
Unlike Abacum, where the whole challenge was getting engineering buy-in, here buy-in was straightforward. The team could see the fragmentation. The constraint was purely bandwidth.

Two constraints shaped every decision on the system.

First: I was the sole designer. There was no one else to own the DS work while I handled product delivery. If I spent three months building a design system, three months of product design work wouldn't happen.

Second: the engineering team was growing. Two frontend engineers when I joined, five by the time I left. A growing team without a shared system gets messier faster. Each new engineer would pick up the same fragmented patterns and extend them further.

The system covered 54 component families: generic UI primitives plus a full domain-specific layer for Remuner's product surfaces. All of it built as the sole designer, alongside continuous product delivery. The constraint shaped every scope decision.

---

## Slide 4 — Applied lesson

**Headline:** What I decided not to build, and why

**Visual:** Side-by-side: Abacum token set (broader scope) vs Remuner token set (tighter scope). Annotation: "complexity is debt you pay later." Explicit list of what was deferred on the right.

**Speaker notes:**
At Abacum, the token set grew broad. That created a maintenance problem: the more tokens, the more opportunity for drift, the more decisions needed when a new surface appeared.

At Remuner, I started with a smaller, more constrained set. The principle: start with what you need for current surfaces, extend deliberately. Avoid the trap of building a system for a hypothetical future product instead of the actual one.

The scope decisions came down to five things that were explicitly not built.

Dark mode. The product token collection has a single value mode, no light/dark theming. The product had no immediate need for it, and dual-mode theming would have doubled the maintenance surface from day one.

Elevation and shadows. One level used throughout. Adding a full shadow scale before the product needed it would have been complexity for its own sake.

Motion tokens. No duration or easing variables. Animation wasn't a design priority at that stage of the product.

Grid and layout tokens. No breakpoints, columns, or gutter tokens. Layout decisions stayed in component logic.

A standalone icon system. Icons were handled in a separate file, deliberately decoupled from the core token file.

The comparison with Abacum isn't just "smaller team, smaller system." It's the same principle applied with more confidence: start with what the product actually uses.

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
The token architecture had three tiers. A branding collection with two variables (the two brand colors). A core collection of 417 primitives: the full color spectrum, spacing, border-radius, and raw typography values. A product collection of 189 semantic tokens covering color, space, and domain-specific surfaces: rankings, tiers, progress indicators, table cell spacing, nine data visualization palettes.

The system uses no Figma styles, only variables. Token Studio reads variables directly; building on styles would have created a parallel maintenance track alongside the pipeline. One output path was the right call.

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

That produced a CI pipeline that catches breaking changes before they reach a deploy, drift detection, a W3C token format migration for standards compliance, an HTML preview sandbox, smoke tests, and JSON output for JavaScript consumers.

None of that was in a spec. It came from asking what the pipeline needed to be trustworthy, not just functional. The production incident accelerated work that should have been proactive.

A designer building CI infrastructure with AI assistance is a different kind of ownership than existed before these tools. The brief was precise enough that the implementation could be delegated and validated. That changes what a designer can own technically.

---

## Slide 9 — Governance

**Headline:** Monthly FE meetings as the operating mechanism

**Visual:** Meeting agenda format: progress update, open problems, goals for next month. Repeated cycle.

**Speaker notes:**
Governance at Remuner was simpler than Abacum, because the team was smaller. Monthly meetings where every frontend engineer presented what they'd built, surfaced problems, and set goals for the next month.

This had two functions. One: a regular checkpoint to catch drift before it became debt. Two: it kept the system from being "the designer's thing." The engineers actively operated it; none of them were just consuming a doc I maintained.

The ranking tokens show how this worked in practice. The first implementation used flat names: color/chart/rankingFirst, rankingSecond, rankingThird. As the product's ranking feature matured, those were replaced with a structured ranking/ namespace covering text, background, icon, and border states for 1st, 2nd, 3rd, and "other" positions. The old tokens are still in the file today, explicitly marked for deletion. That's staged deprecation: the signal is visible to any engineer looking at the variable list. The monthly meeting was where we aligned on the removal timeline. The mark-before-delete discipline came from the production incident: nothing leaves the file quietly.

The same pattern applied to components. The Select component was replaced with a new implementation. The old one still exists as a dedicated page labeled "DEPRECATED → Select", kept in place so any engineer still referencing it can find it. Consistent principle across both layers: nothing disappears quietly; it gets marked first.

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
The CTO said this during a review session, unprompted, after the audit had been running for several months. It reflected product-wide change. A design system that only lives in Figma doesn't move a product's visual coherence. This comment came from the systematic audit changing how the product actually looked and behaved.

630 variables and 54 component families at departure. The numbers matter less than what they covered. The system didn't stay at generic UI; it grew a full domain-specific layer to serve the actual product.

On the token side: a ranking system with gold/silver/bronze primitives backing structured semantic tokens for 1st/2nd/3rd/other positions. Tier states. Progress indicator states. Table-specific spacing for compact and comfortable density. Nine data visualization palettes with light/default/dark semantic variants each.

On the component side: 21 chart component sets covering bar grouped, bar stacked, waterfall, area, pie, and ranking charts. Card variants named for product personas: Individual/Metric, Individual/Payout, Individual/Ranking, Manager/UsersDetails, Simulator/Card. Widget components split between IC and Manager views. A Tiers component. The AI assistant widget. An email template system. All of it mobile-responsive where the product needed it.

None of this was built to be comprehensive. Each domain-specific component existed because a product feature required it.

Three behavioral signals behind the CTO's comment.

Engineers started referring to tokens by name in code reviews: `color-text-primary` instead of `#2D2D2D`. Hardcoded hex in a PR became a caught violation. The ESLint rule made it structural, not cultural.

A designer joined the team late in my tenure. She built a screen quickly and flagged adjustments when the system fell short. She was engaging with it as infrastructure. That's the signal.

Designers stopped double-checking whether components were connected to the system. If it was in the library, it was correct. That's a different kind of trust than "I think this is probably right." The system had earned enough trust that people stopped second-guessing it.

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
