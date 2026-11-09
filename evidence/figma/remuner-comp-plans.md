# Remuner | Comp. plans

File: [H8ACDZmMY1kfsUH6Tx8BzX](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX). 96 pages (87 with content), the largest Remuner file. The plan designer, where admins build commission plans: metrics, payouts, tiers, multipliers, matrices, true-ups, min/max, currencies, parameters, ranking, visibility, and AI plan generation. July 2024 to February 2026. Full listing: [catalog/remuner-comp-plans--H8ACDZ.md](catalog/remuner-comp-plans--H8ACDZ.md).

Indexed 2026-11-09 from a full extraction (extraction resumed at page 53 after a Figma freeze; nothing missing). Ownership: Manel's, including the Spanish Problema / Solución notes (confirmed 2026-11-09). **Collaborative pages:** three pages show Manel directing the second designer, Marina:
- "1125 -> Currencies settings": "Marina prepara un flujo para el caso cuando se extiende un plan hacia atrás", a task assigned to her.
- "1225 -> Bulk edit all members params" (exploration): "Manel: Usa un diálogo actual... Mira si un switch encaja mejor", feedback on her draft.
- "0625 -> Improvement of filter input" (exploration): has a component named ".prueba marina".

Customer and CS names appear in problem notes (Matías from CS, Europastry, Idealista, real user handles); remove them before external use.

Page 72 links to a separate file, "Comp.-plans" (`YvW8HEexUsKTwuYNkFxN16`), which isn't connected or indexed.

## AI plan generation (case candidate)

"0226 -> Remu plan generation" ([8052:3024](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=8052-3024)), 422 nodes, the last work before Manel left (February 2026). The page includes:
- A conversational plan builder: Remu asks for the name, description, dates and currency, then offers to add metrics, payouts or multipliers.
- A **payout component model** written as a schema ([8144:5616](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=8144-5616)): applies to [metric], value model flat / tiered / matrix / smart rules, multipliers, true-up, restrictions, min/max. It's worked through a scenario ("Enterprise Growth Accelerator": matrix of revenue × margin, accelerators, company-performance condition, true-up).
- A metric component model ([8209:44516](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=8209-44516)).
- Test prompts in Spanish describing a full plan in one message ("two metrics, A individual and B team... 5% on B with three tiers on A, marginal..."), next to the generated natural-language explanation of the payout (marginal tiers explained "like tax brackets").
- An "Iteration 2.0" section ([8513:21666](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=8513-21666)) with a numbered refactor list: icons plus labels instead of d/f/t/mx, natural-language preview cards with clickable chips, payout-to-metric "used in" links, keeping the plan's existing order.

Per [context/portfolio.md](../../context/portfolio.md): designed end to end, partially built at departure, outcome unknown. Never say it shipped.

## Pages (handoff)

| Page | What it covers | Link |
|---|---|---|
| 0126 -> New plan / plan info dialog refactor | Shorter new-plan dialog; "type of role" field removed; company currency as default | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=7967-74607) |
| 1225 -> Bulk edit all members params | Same value for all members, kept when switching back to individual | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6987-42332) |
| 1225 -> Alerts (overrides, issues) when extending plan | Alerts when changing a plan's period | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6865-13607) |
| 1225 -> Duplicate payouts | Duplicate a payout with or without its metrics | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6749-17861) |
| 1225 -> Frecuency, currency and custom c. | 325 nodes; app-level frequencies, custom currencies, rates, alerts when no rate applies, IC and manager views, default currency; 22 user stories | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6674-76789) |
| 1125 -> Manager feedback metric (Qualitative metric) | Managers score their team as a metric; review period, old vs new flow, IC view, prototype | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6491-137755) |
| 1125 -> Matrix payout | Payout from two tiered metrics in a matrix; IC view | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6187-126344) |
| 1125 -> Tiered metric targets | Targets with tiers; IC plan and dashboard views | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5968-518662) |
| 1125 -> Show/hide names from ranking | Privacy control on rankings | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5848-62555) |
| 1025 -> MAX/MIN vs statements | Mutually exclusive settings | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5711-11505) |
| 1026 -> Empty targets/parameters warning extending a plan | Extending a plan left targets empty silently; alert plus list of what to fill | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5668-19079) |
| 1025 -> Weighted of weighted metrics | Nested weighted metrics; also fixed button/title mismatch and old components | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5530-193812) |
| 0925 -> True-up payout / plan (regularización) | True-ups across plans; indicators in designer and preview | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5434-101624) |
| 0925 -> Multiplier dialog validation | | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5402-167794) |
| 0925 -> Plan's MIN/MAX with different metric frequencies 2 | Tabs per frequency; unsaved-changes rules | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5335-36355) |
| 0925 -> Copy to future periods in parameters | | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5240-172274) |
| 0925 -> New comp.plan dialog refactor | Plan creation "too long and confusing": split plan setup from metrics | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5146-154714) |
| 0925 -> Edit closed periods - user flow rules for CTA | CTA naming and enable rules | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5136-389775) |
| 0825 -> Order and visibility of metrics | Ranking shown by value or % of target | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5848-137822) |
| 0825 -> Update of items and plans | Showing recalculation in progress on plan pages | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=4839-222599) |
| 0725 -> Smart rules (tiers for items) | Commission rates by item attribute (deal type) with rules and conditions; simulator | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=4683-208238) |
| 0725 -> Metric labeling system | Global metrics shared across plans for dashboard widgets | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=4539-53247) |
| 0625 -> Hide tiers chart, Improvement of filter input, Remove param naming, Show filters on metric cards | Designer refinements: OR filters via autocomplete instead of ";" typing, parameter naming logic, filter chips on cards | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6988-52437) |
| 0525 -> Tiers parameters, Plan designer Icon tooltips | Parametrised tier limits and values per user and period | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6988-52437) |
| 0425 -> Metric direction | | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=3547-4158) |
| 0325 -> Metric ranking options, fields & filter refactor, currency units | | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6988-52437) |
| 0225 -> Metrics visibility | Show in IC dashboard, in plan, items table | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=3087-41400) |
| 0125 -> Settlement payments offset, Ranking order | Payment offsets; tie rules | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6988-52437) |
| 1024 -> Metric dataset selector | | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=2852-39283) |
| 0924 -> Regularisation payouts | | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=2777-84477) |
| 0824 -> Comp plan & Payout min/max, Add ranking from an existing metric | | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6988-52437) |
| 0724 -> Plan users with dates, Payout & metrics order, Payout corrections (multipliers) | Manel's first months: users joining mid-plan ("Robert joins in May and is added to a yearly plan"), card ordering, multipliers | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6988-52437) |

## Pages (exploration, notable)

| Page | What's there | Link |
|---|---|---|
| 1125 -> Currencies settings | 1,772 nodes, the biggest page in the Remuner set: custom currencies from plan creation and from settings, conversion rate tables and log, frequencies, multi-currency widget; collaborative (see above) | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6516-118928) |
| 0825 -> New comp. plans dialog refactor | 842 nodes; guided creation flow ("Great! Your plan is live. Now, let's define payouts and metrics") | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=4909-62123) |
| 0925 -> Payout/plan regularization | 464 nodes; current flow, exploration, components, a real-user case | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5308-46030) |
| 0825 -> Introducir tiers parametrizados en masa | 433 nodes; mass duplication and editing of tiers | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=4880-617) |
| 0724 -> Payout corections (multipliers) | 405 nodes; status quo plus three proposals | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=1-10) |
| 1125 -> Target achievement vs difference | Three proposals (toggle, selector, radio) for showing % vs absolute difference | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5978-558485) |
| 1125 -> Qualitative metrics | Concepts and two versions of manager feedback; rating scales | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6243-61218) |
| 1125 -> Matrix payout (double tiered metrics) | Revenue × gross margin matrix; IC view | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=5974-69879) |
| 0725 -> Smart rules (tiers for items) | Naming exploration for the feature, example rate table | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=4487-90260) |
| 0725 -> Lógica editor de planes | "Save plan" actually recalculated the plan; rename options for Save and Exit | [open](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=1-11) |
| Remaining exploration pages | Earlier versions of the handoff pages above | see catalog |

## Image sources

| Use | Node | Link |
|---|---|---|
| AI plan builder: conversation | Section 1 | [8107:42588](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=8107-42588) |
| Payout component model and scenario | PAYOUT COMPONENT | [8144:5616](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=8144-5616) |
| Iteration 2.0 of plan generation | Iteration 2.0 | [8513:21666](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=8513-21666) |
| Guided plan creation | Proposal - New comp. plan user flow | [4969:252961](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=4969-252961) |
| Matrix payout | Matrix payout | [6086:16256](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6086-16256) |
| Currencies | Currencies 28/11/2025 last update | [6570:44415](https://www.figma.com/design/H8ACDZmMY1kfsUH6Tx8BzX/?node-id=6570-44415) |
