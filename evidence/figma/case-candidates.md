# Case candidates from the Figma index

Built 2026-11-09 from the full Figma extraction ([README.md](README.md)). For each existing case: what the files add. Then new candidates, ranked by hiring signal. Every claim below is what's on the canvas; outcomes are **unknown** unless the evidence register says otherwise. Check [../experience-facts.md](../experience-facts.md) before using any of it externally.

Local PNGs of the image sources are in `images/[file key]/[node-id].png`. Customer names, emails and real data appear in many frames; blur or replace them before external use.

## Existing cases: what the files add

### 1. Modeling Syntax (Abacum)
Source: [abacum-syntax-implementation.md](abacum-syntax-implementation.md), [abacum-engine-implementation.md](abacum-engine-implementation.md).
- Before/after of the syntax cleanup ("2302 -> Syntax usability": remove `.Current`, dimension blocks, underline incomplete formulas).
- Token-level spec for syntax chips: a direct link from the language work to the design system.
- Engine pages that show the language in use: RAMP framed against the customer's mental model, IF ELSE examples, DISTRIBUTE formulas with expected output per aggregation.
- From [abacum-syntax-exploration.md](abacum-syntax-exploration.md) (late 2023 to 2024): a team syntax workshop with HMW questions and a short-term vs long-term parameter-preview split, a function help popover tested at three screen sizes, every filter operator variant written out to choose one consistent syntax, and a "future of syntax" prototype. The workshop had four participants, so present its ideas as team output.
- Gap: the competitor benchmark and the Gong call synthesis named in portfolio.md aren't in these files, and neither are the 2022–early 2023 syntax explorations (this file is the "current" one). They may live in FigJam, Notion or an older file.

### 2. Dataset Manager (Abacum)
Source: [abacum-dataset-manager-exploration.md](abacum-dataset-manager-exploration.md), [abacum-dataset-manager-implementation.md](abacum-dataset-manager-implementation.md), story picks in [../abacum-figma-index.md](../abacum-figma-index.md).
- New since the first index: the **verbatim back-end schema errors** users used to get ("2202 -> Upload a new dataset"). That's the strongest "before" image.
- A **usability test script** next to its prototype ("🙋🏻‍♀️ Auto-sync prototype") and tested rounds ("2303 -> Dataset loads -> months": Round 1, analysis, Round 2). This is research evidence the case currently lacks.
- A measurement plan for the creation funnel ("2202 -> Create", frame "measure"): abandon rate, errors, support requests.
- FP&A feedback quoted on the canvas that drove the formula box ("2309 -> Transformation improvements").
- From the live exploration file ([abacum-dataset-manager-exploration-live.md](abacum-dataset-manager-exploration-live.md)): the five user problems behind the formula box written as a status quo ("Users can't intuitively write formulas", "...can't easily read and understand syntax"), a QA pass of the shipped formula box against real transformations (December 2023), and a research follow-up workshop. These give the case its problem framing and its "after" check.

### 3. Design Systems (Abacum + Remuner)
Source: [remuner-core.md](remuner-core.md), [remuner-components.md](remuner-components.md), [abacum-abax-components.md](abacum-abax-components.md).
- Remuner scale, counted: 161 component sets, 1,438 variants, 63 component pages, plus domain components (plan cards, progress with pacing, tiers, widgets, the Remu AI widget, an email template system).
- Remuner "before": the legacy SCSS palette dump and the font-size audit (9px to 25px) in Core. Then the OKLCH palette rebuild.
- Abax: about 187 live sets and 1,820 variants; a Graveyard of 52 deprecated sets shows deprecation in practice. Ownership is shared, so claim only Manel's sprint items.
- Abax foundations ([abacum-abax-core.md](abacum-abax-core.md)): two variable collections (139 spectrum primitives, 193 semantic tokens aliasing them) and a token naming anatomy. The strongest artefact is the January 2024 **token audit**: a written debate where the head of design proposes merging `actionSecondary` into `secondary`, Manel argues it would blur when to use which, and a recorded decision aligns tokens with alert variants. It's direct evidence of token-architecture judgement. Explorations ([abacum-abax-core-exploration.md](abacum-abax-core-exploration.md)) add a color-blindness check of the palette and the naming debate.
- Component documentation was split across Notion, Figma and Storybook (Manel, 2026-11-09), which explains why only 11 Remuner components carry Figma descriptions.

### 4. Rep Letters / Agreement lifecycle (Remuner), currently hidden
Source: [remuner-hr-compliance.md](remuner-hr-compliance.md).
- The case's four empty image placeholders can now be filled: Admin v1 vs v2, the template editor with blocks and placeholders, the plan status model, escalation from banner to app block, and the cancel, resend and reject edge cases.
- The status model (calculation + compliance + dates in one indicator) and the escalation ladder are decision-rich. They may lift the case enough to unhide it. Outcomes are still unknown.

### 5. AI Agent (Remuner)
Source: [remuner-dashboard-ic.md](remuner-dashboard-ic.md) ("0425 -> IA coaching", "0925 -> Remu logics", "0925 -> Remu refinement"), [remuner-components.md](remuner-components.md) (Remu page).
- 822-node copilot exploration with 26 components; refinement notes (new-chat screen, wider widget, emojis removed to match the brand); an "AI competitors" section on "0325 -> Dashboard new widgets".
- Sample answers show the structured-answer formats the case describes.

## New candidates

### A. Team dashboard: from low adoption to a default dashboard (Remuner), strongest new candidate
Source: [remuner-dashboard-manager.md](remuner-dashboard-manager.md), [remuner-dashboard-ic.md](remuner-dashboard-ic.md).
- Why it's strong: it starts from usage data, which no current case has. An 8-slide findings deck (June 2025) combines QuickSight retention (68 new managers in March falling to 10 in June; 34% visited once; more than half never passed two visits), user-test notes and a CS interview. The conclusion "useful but not usable" leads to proposals that became pages: default pre-populated dashboard, global date filters, easier drag and drop.
- Supporting depth: the origin exploration (benchmark of Grafana, Kibana, PostHog, Mixpanel, QuotaPath, CaptivateIQ, Spiff), layout grid rules, the widget system, sharing and permissions.
- Manel ran the research and built the findings deck (confirmed 2026-11-09). Adoption was measured after the default dashboard shipped, but Manel has no data (2026-11-09): say it was tracked, never state a result.
- Companion evidence from [remuner-my-plans-ic.md](remuner-my-plans-ic.md) (September–December 2025): rep interviews with verbatim quotes, two personas ("regular plan" vs "complex plan"), hypotheses (too many cards and too much scrolling; too much period navigation), a user test and a first iteration, ending in the "My plans" refactor. The quotes match the dashboard finding: reps live in the dashboard and barely use plan pages. Together they make one research-led story about where reps actually look. Without an outcome it's a strong process case with an open ending; say so.

### B. Guardrails for live compensation data (Remuner)
Source: [remuner-datasets.md](remuner-datasets.md), [remuner-mappings.md](remuner-mappings.md).
- One pattern repeated across features: once data feeds a live plan, the system must stop silent damage. Pages: system alerts of critical changes, source locked once a dataset is active, objects disabled when in use, "delete not possible for mappings being used", failed syncs that used to stay "in progress" now surfacing as errors by email.
- Each page opens with a written problem / solution / specs note, which makes the reasoning easy to show.
- It mirrors the Abacum dependency work (dimension "used in", deletion with dependencies), so the two together show a consistent way of thinking across companies. It may work better as a theme inside an existing case than as its own.

### C. Making incentive logic legible to reps (Remuner IC dashboard)
Source: [remuner-dashboard-ic.md](remuner-dashboard-ic.md).
- Tier tables (marginal, capped, multipliers), inverted tiers for negative metrics ("each additional cancellation reduces your commission"), cumulative-metric payouts explained, the payout calculation tooltip, bonus curve vs multiplier formulas worked out.
- Good for fintech and comp-tech roles. Mostly incremental features, so it's a portfolio section or interview story rather than a full case.

### H. Model relationships: from 15 user reports to a shipped panel (Abacum)
Source: [abacum-engine-exploration-2022-2023.md](abacum-engine-exploration-2022-2023.md), [abacum-engine-implementation.md](abacum-engine-implementation.md).
- A rare full arc with evidence at the start. "Problem #1: 15 users have reported that they would like to better understand the relationships between their modules" (May 2023) leads through sidebar, modal and diagram explorations (five dependency-diagram types, including circular references) to the shipped "✅ Relationship panel" (late May 2023) and the logic panel.
- Its sibling, "Problem #2: 20+ customers asked for bulk actions", leads to the bulk dimension management concepts in [abacum-engine-exploration-current.md](abacum-engine-exploration-current.md).
- Fits roles that value research-led prioritisation. Outcome after shipping is unknown.

### D. Dimensions and mappings (Abacum)
Source: [abacum-dimensions-exploration.md](abacum-dimensions-exploration.md), [abacum-dimensions-implementation.md](abacum-dimensions-implementation.md).
- A full framing board (definitions, objectives, hypothesis, pillars, synthesis, take-aways with change counts), a "cheap intermediary solution vs vision" split, and a rename workshop with a destructive-action argument ("a standard modal doesn't work, because users are used to it").
- Overlaps with the Dataset Manager case. Use it as depth inside that case or for a data-modelling interview story. Several critics and one other designer appear on the canvas, so check authorship page by page before claiming.

### E. Remuner mappings (Remuner)
Source: [remuner-mappings.md](remuner-mappings.md).
- Small, self-contained: entity model, two sketch rounds, a benchmark (Varicent, Flatfile, Visual Paradigm, Boogieboard), then a handoff with 14 user stories. Good as a compact "how I approach a new concept" example. Exploration frames contain real customer emails.

### F. AI plan generation (Remuner), strong if framed honestly
Source: [remuner-comp-plans.md](remuner-comp-plans.md), "0226 -> Remu plan generation".
- Admins describe a commission plan in plain language and the assistant builds it. The design work underneath is a component model for payouts and metrics, written as a schema and stress-tested with a complex scenario (revenue × margin matrix, accelerators, true-up). It also covers generated natural-language explanations of the payout and an Iteration 2.0 refactor list.
- It pairs with the AI Agent case: the same assistant, moving from answering questions to building configuration.
- Limit: designed end to end, partially built at departure (March 2026), outcome unknown. Never say it shipped.

### G. Currencies and conversion rates (Remuner)
Source: [remuner-comp-plans.md](remuner-comp-plans.md), "1125 -> Currencies settings" and "1225 -> Frecuency, currency and custom c.".
- The largest page in the Remuner set (1,772 nodes): custom currencies, conversion rate tables with history, frequencies, and alerts when no rate applies to a period. Fintech-relevant data-integrity work.
- Collaborative with the second designer; check what was Manel's before claiming it.

## What to confirm with Manel

Answered 2026-11-09: Manel ran the June 2025 dashboard research and built the deck; "0624 -> Dashboard new styles" is his; the Abacum workshops (syntax, variable library, dimension ideation) were shared team sessions, with no record of who ran them; Engine "Change switch-over date" is to be described as a rework of the head of design's earlier designs.

Also answered: adoption after the default dashboard was measured but no data survives; Remuner component documentation lived across Notion, Figma and Storybook.

Nothing left open from the Figma index.
