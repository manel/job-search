# Case Deck: Design Systems at Remuner

**Best for:** Founding designer roles, sole-designer contexts, early-stage companies that need infrastructure built from scratch.
**Duration:** 25-35 minutes including Q&A. Walk-through aim: 15-20 minutes.
**Lead framing:** Operational leverage as the first designer in a scaling B2B company. Systems thinking applied under real constraints. The production incident is the learning arc, not a footnote.

---

## Slide 1 — Cover [NEW]

**Headline:** Building operational leverage as the first designer

**Subheadline:** Remuner, 2024-2026. One designer, a growing engineering team, and the question of how to create shared foundations without slowing product delivery.

**Speaker notes:**
When I joined Remuner, the company had a scaling problem, not a visual one. Every screen a designer produced had to be built from scratch by whichever engineer picked it up. Each new engineer extended the inconsistency further. The product's quality was bottlenecked by the absence of a shared contract between design and engineering.

My job wasn't to build a design system. It was to create leverage: reduce the per-screen decision overhead, make the engineering team faster at shipping consistent UI, and do it without stopping product delivery.

This case covers how I did that as the sole designer, alongside continuous product work, on a team that went from two engineers to five.

---

## Slide 1-OLD — Cover [SKIP]

**Headline:** A design system as the sole designer at a startup

**Subheadline:** Remuner, 2024-2026. From fragmented implementation to a production system with CI enforcement

**Speaker notes:**
I picked this case because IMO it fits the role you are hiring for. Being a founding designer means being a sole designer from day zero without or with little infrastructure to inherit.

I was the sole designer at Remuner. No components, no tokens, no shared contract between design and engineering when I arrived. Everything in this case was built alongside product delivery on a team that went from three engineers to six.

I'm going to share the process, the decisions and mistakes.

---

## Slide 2 — Starting condition

**Headline:** Not a bad-looking product. A fragmented implementation.

**Visual:** Diagram or screenshot comparison: the product UI on the left (looks reasonable), the implementation layer on the right (each FE with their own component implementation, Vuetify defaults filling gaps, zero Figma components).

**Speaker notes:**
The product didn't look broken. But it wasn't designed with system thinking. The person who built it came from a graphic design background: decisions were made screen by screen, without the foundations that make a product consistent at scale. Visually it held together, but there was no structure underneath.

On the implementation side it matched: each engineer had built their own component set, with Vuetify defaults filling the gaps. Zero Figma components. Every screen had to be built from scratch by whichever engineer picked it up.

The gap was in both layers, not just the implementation.

---

## Slide 3 — The constraint

**Headline:** Sole designer. Product work can't stop.

**Visual:** Timeline: 2 FEs at hire, 5 FEs at departure. Single designer icon across the whole timeline.

**Speaker notes:**
Buy-in was easy. The team could see the fragmentation. The constraint was purely bandwidth.

I judged systemization as the highest-leverage investment because engineering headcount was doubling. Each new engineer without a shared system would pick up the existing fragmented patterns and extend them. The cost of not having a system increased with every hire. Two FEs when I joined, five by the time I left.

The sole designer constraint shaped everything. If I spent three months building infrastructure, three months of product delivery wouldn't happen. So the system had to be built in parallel, not instead.

---

## Slide 4 — Scope, format, pipeline [NEW]

**Headline:** Three decisions that shaped how the system scaled

**Visual:** Three-column layout: (1) Scope — what was deferred vs built; (2) Format — token export format matching engineering stack; (3) Pipeline — flow diagram showing Token Studio → Style Dictionary → GitHub → Vuetify/Storybook.

**Speaker notes:**
Three decisions shaped how the system scaled without getting in the way of product delivery.

Scope: I went tighter than my Abacum experience. Build what the product uses now, extend when it needs more. Dark mode and motion tokens were deferred explicitly. No hypothetical surfaces — every token and component earned its place by being used.

Format: The engineers worked in Vuetify, which uses Sass variables. I exported tokens as both Sass variables and utility classes to match the syntax they already thought in. This came out of the monthly FE meetings, not a top-down decision.

Pipeline: Token Studio, Style Dictionary, GitHub. The foundation came from my Abacum work; engineers adapted it to Remuner's stack. At that point it was functional. The next slide covers why functional wasn't enough.

---

## Slide 4-OLD — Applied lesson [SKIP]

**Headline:** What I decided not to build, and why

**Visual:** Side-by-side: Abacum token set (broader scope) vs Remuner token set (tighter scope). Annotation: "complexity is debt you pay later." Two deferred items listed on the right.

**Speaker notes:**
At Abacum, the token set grew broad. That created a maintenance problem: the more tokens, the more opportunity for drift, the more decisions needed when a new surface appeared.

At Remuner, I started with a tighter scope: build what the product actually uses, extend deliberately. Avoid building for a hypothetical future product instead of the actual one.

Two things were explicitly deferred.

Dark mode. The product token collection has a single value mode, no light/dark theming. The product had no immediate need for it, and dual-mode theming would have doubled the maintenance surface from day one.

Motion tokens. No duration or easing variables. Animation wasn't a design priority at that stage of the product.

Everything else followed the product. Elevation and shadows were built where the product used them. Layout tokens covered the surfaces that needed them. The icon system became its own repository, explicitly decoupled from the core token file so it could be versioned and consumed independently.

The comparison with Abacum isn't just "smaller team, smaller system." It's the same principle applied with more confidence: start with what the product actually uses, and don't pre-build what it doesn't need yet.

---

## Slide 5-OLD — Speaking the same language [SKIP]

**Headline:** Tokens exported as Sass variables and utility classes

**Visual:** Token in Figma on the left → exported as both `$color-text-primary` (Sass variable) and `.text-primary` (utility class) on the right.

**Speaker notes:**
The engineers at Remuner used Vuetify as the component framework. Vuetify uses Sass variables. The engineers already thought in Sass variable syntax.

If I'd exported tokens only as CSS custom properties or JSON, there would have been a translation layer. Every engineer would have to map the new system onto the vocabulary they already used. Instead, I exported tokens in both formats: Sass variables and utility classes that matched Vuetify conventions.

This decision came out of the monthly FE meetings. Not top-down. The engineers told me what format made sense for their workflow, and I built to that.

---

## Slide 6-OLD — Pipeline [SKIP]

**Headline:** Token Studio → Style Dictionary → GitHub → Vuetify / Storybook

**Visual:** Pipeline flow diagram. Annotations: which parts came from the Abacum work, which parts were adapted, what was added in Feb 2026.

**Speaker notes:**
The token architecture had three tiers. A branding collection with two variables (the two brand colors). A core collection of 417 primitives: the full color spectrum, spacing, border-radius, and raw typography values. A product collection of 189 semantic tokens covering color, space, and domain-specific surfaces: rankings, tiers, progress indicators, table cell spacing, nine data visualization palettes.

Variables handled the token layer — color, spacing, and all domain-specific surfaces. Token Studio reads variables directly, so the pipeline was built on variables. Text styles and elevation effect styles (S/M/L) existed alongside the variable system: typography and elevation were defined as Figma styles and consumed directly by components. The two coexisted; the pipeline owned the color and spacing layer, styles owned typography and elevation.

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
In February 2026, I hardened the repo using AI assistance. I'm naming that directly: I used Codex to work through the implementation step by step, with an engineer reviewing and merging each stage.

That produced a CI pipeline that catches breaking changes before they reach a deploy, drift detection, a W3C token format migration for standards compliance, an HTML preview sandbox, smoke tests, and JSON output for JavaScript consumers.

None of that was in a spec. It came from asking what the pipeline needed to be trustworthy, not just functional.

I used AI as an implementation accelerator, but ownership stayed mine: defining the architecture, validating every output, and managing the production risk. The production incident accelerated work that should have been proactive.

---

## Slide 9 — Governance

**Headline:** Monthly FE meetings as the operating mechanism

**Visual:** Meeting agenda format: progress update, open problems, goals for next month. Repeated cycle.

**Speaker notes:**
Governance at Remuner was simpler than Abacum because the team was smaller. Monthly meetings where every frontend engineer presented what they'd built, surfaced problems, and set goals for the next month.

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

## Slide 11 — Outcome [NEW]

**Headline:** Three outcomes. Each in production, not just in Figma.

**Visual:** Three-column layout: Delivery speed | Engineering consistency | Organizational scalability. CTO quote anchoring the top.

**Speaker notes:**
The CTO said "from a 2010 app to a 2020 app" unprompted during a review after the audit had been running for several months. It reflected product-wide change. A design system that only lives in Figma doesn't move a product's visual coherence.

Three concrete outcomes behind it.

Delivery speed. The system covered 54 component families with a full domain-specific layer: 21 chart types, card variants named for product personas, tier and progress states, nine data visualization palettes. Every screen that used those components skipped the rebuild-from-scratch cycle. [NEEDS INPUT: one specific feature that shipped faster because a DS component existed.]

Engineering consistency. Token enforcement via CI and ESLint. Hardcoded hex in a PR became a caught violation, not a shipping inconsistency. Engineers started calling tokens by name in code reviews: "color-text-primary" instead of "#2D2D2D". That shift is behavioral, not cosmetic.

Organizational scalability. A new designer joined late in my tenure, built a screen fast, and flagged where the system fell short instead of working around it. New engineers inherited a shared contract instead of the fragmented patterns that existed on day one.

One thing I'd do differently: harden the pipeline before something breaks. The CI infrastructure came from a production incident. The learning is correct; the timing shouldn't have required an outage.

---

## Slide 11-OLD — Outcome [SKIP]

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

## Slide 12 — For this role [NEW]

**Headline:** How this maps to Factorial's spinoff

**Visual:** Two-column layout: left — operating principles from Remuner; right — how each maps to Factorial's domain (inventory, MDM, ticketing, onboarding workflows, analytics).

**Speaker notes:**
The products are different. The operating model is the same.

You're building a new product in a domain with real operational complexity: inventory management, MDM, support ticketing, onboarding workflows, analytics. The question isn't whether to systematize. It's when, where, and at what granularity.

What I'd apply directly:

Start with the highest-friction workflows first, not a comprehensive system. At Remuner, the domain-specific token and component layer grew from product features demanding it, not from upfront planning.

Systematize repeated patterns. Let the rest stay messy until it earns attention.

Co-design with engineering around their implementation constraints. The Sass variable format came from a conversation with engineers, not a design decision imposed on them.

Build lightweight governance early, before complexity compounds. Monthly FE meetings cost little and caught drift before it became debt.

The founding designer job at Remuner wasn't to make the product look good. It was to make the team faster at making good product. That's the same job here.

---

## Q&A preparation

**"What would you do differently?"**
Harden the pipeline earlier. I treated the token repo as a design asset for too long before I understood it needed to be governed as infrastructure. The production incident accelerated work that should have been built into the initial setup.

**"How did you balance DS work with product delivery?"**
The start-small approach was the mechanism. Rather than building a complete system before shipping anything, I built the minimum viable token set and governance structure, then extended it as product work revealed gaps. The monthly FE meetings kept it from drifting without requiring dedicated allocation.

**"How did this connect to business outcomes?"**
A DS at a startup with a growing engineering team is a velocity investment. Without it, every new feature is designed and built as a one-off, and each new engineer extends the inconsistency. With it, there's a shared contract that reduces decision overhead on every screen. The CTO's comment points to something beyond velocity. The product was visibly coherent in a way it hadn't been, which matters for enterprise sales.

Note: there are no hard quantitative metrics in this case (no before/after build times, no component adoption rate, no regression count). Own this proactively rather than waiting to be asked. The proxy signals are: CTO's unprompted before/after observation, the pipeline reaching production (not just Figma), and the AI product shipping on top of the system. If pressed for numbers, say: "I didn't have instrumentation in place to measure it. What I can point to is what the system made possible — and what the CTO said unprompted." Don't apologize for the absence; frame it as a startup reality and name the proxies with confidence. Flag for future: if the deck is reviewed for a role that emphasises data-driven design, add adoption enforcement data (ESLint rule hits, Storybook coverage) as a proxy metric layer.

**"What's the difference between what you built here and at Abacum?"**
Scale, constraints, and approach. Abacum: co-led a business case, worked with an engineering team that built the original pipeline, governed across five squads. Remuner: sole designer, adapted and owned the pipeline, smaller token scope by design. The same principles, applied with the constraints of a smaller team and a narrower budget. And a harder lesson learned about the difference between infrastructure that's functional and infrastructure that's trustworthy.

**"How does this apply to Factorial?"**
The spinoff context maps directly to Remuner: no prior designer, no infrastructure, greenfield product in a complex operational domain. The difference is I'd apply the same principles faster and with more confidence — and I'd harden the pipeline as part of the initial setup rather than after an incident forces it.
