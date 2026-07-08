# Design Systems — Raw Notes (Abacum / Abax)

Source: Notion export from Abax Design System workspace. Extracted June 2026.
Raw intake archive. Distilled into `context/portfolio.md` on 2026-06-12 — read that file first; come back here only for detail the distillation dropped.

---

## Named people (Abacum)

- Julian Kraan — Head of Design. Co-led the DS business case presentation to engineering leadership. Co-led token finalization during Maker Days.
- Cristian Poley — FE engineer. Removed ESLint rules from webapp frontend, decoupled Redux from Storybook.
- Adrià Marzo — FE engineer.
- Manel Escuer — FE engineer. Documented ways of working, contribution processes.
- Javier N. — FE engineer. Timing of Maker Days sprint was planned around his parental leave (September 2023).
- Mon Castel — Designer. Cell components ownership.
- Victor — Designer. colorSelect component, templates and key screens library.
- Carol — Designer. Search input component, checklist select.
- Joel — Designer. Menu component, spaces update.

---

## The business case and organizational friction

The engineering presentation was built around concrete evidence of cost:
- Screenshots of bugs and inconsistencies: buttons, cells, menu elements
- Framing: "half-implemented components aren't understood. Inconsistencies create a perception of immaturity, resulting in lack of trust."
- FE concerns going in were explicit in Julian's notes: "side project, co-prioritization, squads not having a platform picture."
- The case had to address FE skepticism directly — this was not a design team pitching to a receptive audience.

Getting Maker Days selected was the actual win. It converted the DS from a side project into a company-sanctioned quarterly initiative. It had to compete against other initiatives for dedicated time.

---

## Maker Days structure and Manel's ownership

Vision 1.0 defined success criteria explicitly:
- 80% of new UI built from available Abax components
- 100% deprecation of legacy MUI components (where Abax equivalents exist)

Sprint 1 deliverables owned by Manel (from the Notion sprint table):
- Token architecture (variables, Token Studio)
- Spacing tokens (margin, padding, gaps, nomenclature)
- Border tokens (width, radius, style, nomenclature)
- Color token updates and cleanup (get rid of excess tokens, e.g. onAction, onError)
- Figma variable structure
- Apply tokens to component library
- Component library cleanup (attach text styles, spacing tokens, finalize page layouts)

Julian Kraan owned: finalizing color tokens spectrum, font token finalization, semantic color token adjustments.

Two sprint formats were evaluated: small team (2 FE, 1 Design) over 2 weeks running alongside regular sprints, or large team (4+ FE, 2+ Design) in a single dedicated week. Maker Days used the latter.

---

## Metrics framework (designed, partially tracked)

Adoption goals were defined and documented:
- Build any new product with Abax components
- Deprecate legacy UI components

Metrics planned:
- # of MUI vs Abax components in codebase
- # of Abax components migrated from MUI
- # of new Abax components built
- # of global tokens vs tokens actually in use
- # of component instances across the app
- # of disabled ESLint rules (eslint-disable-next-line abacum-io/prefer-abax-component)

Tracking was manual at first due to team size. Tools evaluated for later: Radius tracker, React scanner, Omlet, Segment's dependency-report, Productboard's CSS approach.

This is notable: there was a measurement framework from the start, not just qualitative outcomes.

---

## Governance systems Manel built

- Issue reporting system: structured categories (not working components, naming proposals, component improvements, detaching instances). Published via Notion and a #design-library Slack channel.
- Form elements release plan: new Abax components released under feature flags. Squads identified components to replace and added migration tasks to their sprint backlogs. This avoided inconsistency during transition and surfaced edge cases before full rollout.
- Weekly design library sync: recurring meeting with the whole design team. Manel ran a standing agenda item for discoverability (have you detached? Any variant missing? Any component ready to build?).
- Two-library Figma structure: Exploration file for experiments (components published with [Experiment] prefix), Implementation file as the canonical published library. Manel proposed and drove the decision.

---

## Real tensions and decisions (what made it hard)

**"Focus shift from infrastructure to production"** — documented in Vision 1.0 as a named concern. The team had to decide when to stop building token infrastructure and start shipping production components. Text input, select, autocomplete, and menu all had documentation gaps and incomplete variants when this question came up.

**Component naming discipline** — recurring, contested. "How do we name this component? Dropdown menu? Let's not mix it with the list and toolbar elements." Shows the conceptual work required, not just visual.

**Read-only state** — debated across multiple weekly syncs. Is it a new state, a disabled state, or pre-fill automatic state? Engineers and designers had different mental models.

**Deprecated components in Figma** — a real bug. Deprecated components kept appearing in search results for designers. Manel diagnosed it and proposed 3 solutions with tradeoffs, including the complexity of the "change name + remove instances + re-publish + update files + unpublish" cycle.

**MUI decision** — kept MUI as base layer rather than replacing it. Framed at the time as: replacing it would require rewriting components across five squads with no immediate product benefit. Abax sat on top of MUI, extending and overriding with system tokens and patterns.

---

## Specific copy signals worth using

- The business case slide included: "Well-kept component library → source of truth in components allows for the creation of UX patterns. For users: more consistent elements and interactions. Half-implemented components aren't understood. Inconsistencies can create a perception of immaturity, resulting in lack of trust."
- Maker Days sprint was timed around Javier's parental leave — shows the human coordination work involved.
- The weekly cadence ran from at least July 2023 to March 2024 (visible in the weekly doc). That's 8+ months of active governance.

---

## What this export does NOT contain

- Any data on actual adoption rates or % MUI-to-Abax migration achieved
- Any FE team feedback quotes about the system
- The engineering leadership presentation itself (referenced but not in the export)
- Remuner DS context (separate, not in this Notion workspace)

---

## Remuner DS — notes from conversation

### Starting condition (May 2024)

Product had reasonable visual design (designed by the previous head of design). Figma components: zero. FE implementation: each engineer had built their own set of components independently. Result: color inconsistencies, component inconsistencies, Vuetify defaults filling the gaps, different effects in different parts of the app. The inconsistency came from both sides: the delivered designs were themselves inconsistent screen to screen, and FE implementations diverged with nothing shared to reference. (Correction 2026-07-08: do not frame FEs as the sole cause of the fragmentation.)

Team at start: 2 FEs. Team at end: 5 FEs.

### How the DS started

No Figma components existed, so the first work was building the component library from scratch — not proposing a DS in the abstract. This ran alongside regular product work. A few weeks in, Manel pushed for the 2-tier token architecture and proposed implementing it before moving to components.

Buy-in: easy. CTO and FEs agreed on value immediately. Constraint was bandwidth — couldn't slow product work. This shaped the entire approach: start small, grow incrementally. Lesson directly applied from Abacum (large token set there created maintenance overhead early).

### The pipeline

The token pipeline was adapted from the Abacum setup. Engineers adapted it to match Remuner's stack: Vuetify (not React), Sass variables. Do not overstate original authorship — the foundation came from Abacum. What's genuinely Manel's: the decision to bring it in, the adaptation, and the February 2026 hardening.

February 2026 (final month before leaving): Codex-assisted push to professionalize the repo — added CI pipeline, safety gates, build drift checks, W3C token format, HTML preview sandbox, smoke tests, JSON output for JS consumers. This was significant engineering work done by Manel with AI assistance, reviewed and merged by engineers.

### Key technical decision from monthly FE meetings

Exporting tokens as both Sass variables AND utility classes (similar to Vuetify's own conventions). Reasoning: "speaking the same language" — FEs already thought in Vuetify's class-based system. Instead of making them learn a new convention, the token output matched their existing mental model. This came out of the monthly meetings, not a top-down decision.

### Monthly FE meeting format

Everyone presented progress (even if none). Discussed current and anticipated problems. Set goals for next meeting. Collaborative problem-solving. These meetings were the primary governance mechanism at Remuner — no weekly design-wide sync like Abacum.

### The ongoing product audit

Not a one-time exercise. Ongoing throughout tenure. Process:
1. Review screens systematically to identify pattern inconsistencies
2. Capture all instances of a pattern (e.g. all autocompletes across the product)
3. Define variants, states, behaviors for that pattern
4. Create a Jira ticket, share with FEs, get their input
5. Decide: fix now, or defer if that part of the app has an upcoming feature change

The deferral judgment is important — not every inconsistency was worth fixing immediately. If a section was about to get a new feature, the DS work would be absorbed into that feature's work instead.

This audit practice is what drove the CTO's observation. It wasn't just new components — existing screens were systematically updated.

### The CTO quote

"From a 2010 app to a 2020 app." Said unprompted during a review session, after the component library had coverage and the systematic audit had been running for a while. The quote reflects visible, product-wide change — not just a Figma library existing.

### Concrete operational signals

**Token naming replacing hex (both companies, strongest at Abacum):**
Before: FEs copied and pasted hex values. After: called tokens by name — `color-text-primary` instead of `#2D2D2D`. Easier to read, impossible to get wrong, reviewable in code. ESLint guardrails caught non-system usage at review time.

**Screen built fast (Abacum):**
A designer on the team mentioned she had built a screen quickly because the components were well-built and had the options she needed. She also flagged adjustments needed in other components. Manel captured those adjustments and acted on them. The feedback loop — not just the speed — is the signal worth using.

**Designers stopped double-checking (both):**
Designers no longer needed to verify whether a component was correctly connected to the system. If it was in the library, it was correct. Reduced review overhead.

### Privacy note

No names in the cases. "The head of design," "a designer on the team," "the CTO" — specificity comes from detail of what happened, not attribution.

---

## Answered: open questions

1. **Adoption metrics tracked?** Yes, they were tracked, but the data is not recoverable. No hard numbers available. Own this directly in the case — don't pretend the measurement didn't happen, but don't fabricate figures.

2. **Engineer/designer feedback on time saved?** Yes. Engineers reported saving time by calling tokens and components by name rather than hunting for the right color or pattern. Designers no longer had to double-check whether a component was connected to the DS — if it was in the library, it was correct. No specific named person confirmed for this signal, but it was a repeated pattern across multiple engineers.

3. **ESLint catches in practice?** Yes. The most concrete pattern was hex color values — devs had been copying and pasting hex codes directly. The token system (and ESLint rules flagging non-system usage) eliminated this. It was the most visible before/after: hardcoded hex in code review became a caught violation rather than a shipping inconsistency.

4. **Maker Days output?** The full token system shipped during the week: Figma variables, Token Studio configuration, and the JSON repository consumed by the frontend. The Button component was the first Abax component delivered — the first concrete proof that the pipeline worked end to end. Shipped in one Maker Days week.
