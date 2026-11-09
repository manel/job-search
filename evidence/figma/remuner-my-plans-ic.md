# Remuner | My plans (IC)

File: [VupJTyuUY8TbtTYiAozZrF](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF). 38 pages (31 with content), 3,885 top-level nodes. The rep's "My plans" view: plan, payout and metric cards, pacing, rankings, multipliers, mobile, expired plans, the plan details drawer, and a late-2025 refactor backed by user interviews. May 2024 to January 2026. Full listing: [catalog/remuner-my-plans-ic--VupJTy.md](catalog/remuner-my-plans-ic--VupJTy.md). Related: [remuner-dashboard-ic.md](remuner-dashboard-ic.md).

Indexed 2026-11-09 from a full extraction. Ownership: Manel's, including the Spanish notes. "0501 -> Old cards" holds the cards as they were before the May 2024 facelift (inherited; use only as "before"). Customer and user names appear in quotes and frames; remove them before external use.

## The plans-view research (case candidate)

"0925 -> Plans view skteches" ([3757:10576](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3757-10576)), 570 nodes, September to December 2025:
- Two personas built from real users, a "regular plan" rep and a "complex plan" rep. Hypotheses tied to named interviewees: "H1 | Too much cards and scroll", "H2 | Reduce period navigation".
- A Quotes section with verbatim rep quotes ([3876:49235](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3876-49235)). For example: "I go in from the dashboard and access everything from there... I barely use 'My plans'", and "A rep knows perfectly which plans they have, I don't need to see the details". There's also a Metrics section and a benchmark (QuotaPath and others).
- A "User test" section and "Iteration 1" ([4100:66663](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=4100-66663)). Then proposals for one-plan view, multiple plans, multiple-frequency navigation, true-up and max/min explanations, and period closing.
- This leads into "1225 -> My plans refactor" ("remove duplicated info": delete metric cards and fold their details into payout cards) and the "0126 -> Plan details drawer" handoff.

Outcome after the refactor is unknown. Pairs with the dashboard adoption research in [remuner-dashboard-manager.md](remuner-dashboard-manager.md). Both point to reps using the dashboard more than plan pages.

## Pages (handoff)

| Page | What it covers | Link |
|---|---|---|
| 0126 -> Plan details drawer | Drawer with plan details, documents, issues, manual adjustments, period approvals | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=4711-14782) |
| 1025 -> My plans | One vs multiple plans, tabbed payouts, multiple-frequency payouts, plan indicators, manager "view as" | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=4294-83411) |
| 0725 -> Decouple items from cards | Items moved from metric cards into a dialog; accruals vs payments | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3515-65754) |
| 0625 -> Show syncronisation on plan cards | Problem: the last-sync date confused reps at customers with many plans, because it only updates after every plan recalculates | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3542-97639) |
| 0525 -> Expired plans visibility | Showing finished plans across dashboards, plan pages and selectors | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3542-77113) |
| 0325 -> Bonus % | Bonus achievement percentage on the card | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3400-6771) |
| 1124 -> Ranking frequencies | Daily, weekly and monthly rankings; frequencies bounded by the metric period | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3327-18986) |
| 0724 -> Responsive cards (Mobile) | Mobile versions of every card type, notifications, claims, profile | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=2872-36841) |
| 0724 -> Cards with multipliers | Multiplier tabs and simulator | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=2650-12577) |
| 0524 - Card pacing and facelift | Manel's first project (May 2024): pacing behaviour and copy ("Your progress is above your expected pacing..."), restriction and max/min ribbons, tooltips, transactional table, card grid | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=1-9) |

## Pages (exploration)

| Page | What's there | Link |
|---|---|---|
| 1225 -> My plans refactor | Payouts, proposals, concepts; "remove duplicated info" | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=4559-1098) |
| 1125 -> Plan details drawer | Global vs per-period options; true-up formula written out | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=4430-85741) |
| 0925 -> Plans view skteches | The research above | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3757-10576) |
| 0625 -> Decouple items from cards, Show syncronisation on plan cards | Trigger options; sync-date states (before or after 6 hours) | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3496-20064) |
| 0525 -> Expired plans visibility | 459 nodes; "finished" vs "archived" defined (finished plans keep their data; archived ones were never used) | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3542-2) |
| 0325 -> Bonus %, Ranking exploration | Five placement options; ranking colour contrast fix with a contrast test | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3412-2) |
| 1024 -> Ranking frequencies | Selector vs tabs | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3313-23023) |
| 0624 -> Responsive cards | 359 nodes; status quo, a customer demo section, every card on mobile, minimum viewport 360 × 780 | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=2437-49446) |
| 0624 -> Multipliers cards | Benchmark, explanation copy for how the payout is calculated, simulator, a customer demo | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=2418-691) |
| 0524 -> Card pacing and facelift, Metric cards, Pacing benchmark, Customer web screenshots, Card to list of items, Transaction table | The May 2024 starting point: 708-node card exploration, pacing benchmark, screenshots of customers' own tools | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=1-10) |
| 0501 -> Old cards | **Inherited** pre-May-2024 cards | [open](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=2001-39257) |

## Image sources

| Use | Node | Link |
|---|---|---|
| Rep quotes | Quotes | [3876:49235](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3876-49235) |
| Personas and hypotheses | Slide 1 | [3853:24831](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3853-24831) |
| User test and iteration | User test / Iteration 1 | [4100:66663](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=4100-66663), [4105:66673](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=4105-66673) |
| Benchmark | Benchnark | [3869:34620](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=3869-34620) |
| Before: old cards | 0501 -> Old cards | [2001:39257](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=2001-39257) |
| Pacing behaviour | Pacing behaviour | [2001:4123](https://www.figma.com/design/VupJTyuUY8TbtTYiAozZrF/?node-id=2001-4123) |
