# Remuner | Dashboard (manager / admin)

File: [D3I7XGCC7WulmGtydRj5aI](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI). 48 pages (40 with content), about 5,400 top-level nodes. The team dashboard for managers and admins, August 2024 to December 2025: widget library, layout grid, sharing and permissions, metric, earnings, items, pending-payments and multi-currency widgets, export, duplicate, and a default pre-populated dashboard. Full listing: [catalog/remuner-dashboard-manager-admin--D3I7XG.md](catalog/remuner-dashboard-manager-admin--D3I7XG.md). IC side: [remuner-dashboard-ic.md](remuner-dashboard-ic.md).

Indexed 2026-11-09 from a full extraction. Ownership: Manel's, including the Spanish Problema / Solución notes (confirmed 2026-11-09). Notes quote Customer Success (Matias, Joana) and an engineer (Ivan). Several problems name the requesting customer (The Hotels Network, Fracttal, Magashops); remove those names before external use.

## The research finding (case candidate)

"0625 -> Team's default prepopulated dashboard" (exploration) contains an 8-slide deck, "Findings of Team's Dashboard" ([slides start at 3784:47263](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3784-47263)). It draws on three sources: user-test notes in Notion, QuickSight usage data, and an interview with the Customer Success team.

- QuickSight: new managers trying the dashboard fell from 68 (March 2025) to 39, 19 and 10 (June). Of the March cohort, about 82% came back the next month and about 53% two months later. 34% visited only once, and more than half never passed two visits. Usage varied by company.
- Conclusions on the slides: useful but not usable; managers used it passively, only if an admin or CS set it up; "76% try it at least once, but more than 50% don't come back after one or two visits"; the barriers were the empty first screen and long configuration.
- Proposals: a default pre-built dashboard that can be edited later, faster customisation, and global period filters. The pages "Team's default prepopulated dashboard", "Global filters by date" (in the IC file) and the drag-and-drop work follow from this.

Evidence class: the figures are on the canvas as Manel wrote them; the QuickSight source isn't saved anywhere else. Manel ran the research and built the deck (confirmed 2026-11-09). Adoption was measured after the default dashboard shipped, but no data survives (Manel, 2026-11-09): say it was tracked, never state a result.

## Pages (handoff)

| Page | What it covers | Link |
|---|---|---|
| 1025 -> Arrange "new dashboard" button | Button position | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4916-36690) |
| 0925 -> Show target on dashboard widgets | Targets on line and bar charts: same target, one target per period, different targets per member | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4758-7432) |
| 0925 -> Calculated (* and /) metrics on widgets | Metrics built by multiplying or dividing two others ("net sales ÷ days worked = € per day worked") | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4740-62386) |
| 0825 -> Widget with pending payments | Status selector (settled, expected, pending) for earnings widgets | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4396-51466) |
| 0725 -> Items widget | Payout, statement, accrual and payment items tables with filters, search and export notifications | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4175-44490) |
| 0725 -> Team's default prepopulated dashboard | Default dashboards per manager type (several teams, multi-currency, one team, one plan) | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3925-24106) |
| 0625 -> Add Members + payments to Split by | New split for CS: members and payouts together, per chart type | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3721-74473) |
| 0625 -> Duplicate dashboard | Duplicate structure without data, for one dashboard per team | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3691-41509) |
| 0625 -> Export full dashboard | One Excel file with a tab per widget | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3636-3681) |
| 0525 -> Widget: Bonus performance | Bonus-only payouts widget with splits and obfuscated values | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3555-8579) |
| 0325 -> Dashboard sharing | Avatar group showing who it's shared with; view, edit, full-access levels | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3504-25521) |
| 0225 -> Widget export | Export as CSV and as image | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3339-44186) |
| 1224 -> Widget multicurrency alert | "Unable to aggregate plans with different currencies", three options | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3246-16339) |
| 1224 -> Widget items + pagination | | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3222-90383) |
| 1224 -> Dashboard images | Thumbnail set for every widget type (library previews) | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3216-10176) |
| 1124 -> Widget menu | Duplicate, edit, delete with shared-view warning | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2813-15116) |
| 1124 -> Widget library | Library dialog, loading, skeleton, empty dashboard | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2799-41334) |
| 1124 -> Dashboard earnings widget | Every option of the earnings widget: split, period, plan, users, comparison, view, AI switch, decimals | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2792-43284) |
| 1124 -> Dashboard metric widget | Metric, pacing, ranking and items widgets; custom period selector | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2712-24891) |
| 1024 -> Dashboard layout grid | Grid rules: max 3 widgets per line, widths 1/3 to 1/1, equal heights | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=1-9) |
| 1024 -> Dashboard resize widgets | Snap to nearest column | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2474-32760) |
| 1024 -> Dashboard drag & drop widgets | Within a line, to a new line, between lines | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2474-33543) |
| 1024 -> Dashboard manager | Create, delete (warning lists who loses access), reorder tabs | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2476-35805) |
| 1024 -> Dashboard permissions & sharing | Invite, permissions, email notification; open user stories | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2478-40354) |

## Pages (exploration)

| Page | What's there | Link |
|---|---|---|
| 1225 -> Reordenar columnas widget items | Column reorder in items widget, Vuetify capability noted | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=5087-11064) |
| 1125 -> Show/hide name of team members on ranking | Plan designer and IC dashboard views | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4938-48581) |
| 0925 -> Show target on dashboard widgets | 364 nodes; every target case (one member, team, same or different target), current flow from production screenshots, critique note | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4740-116367) |
| 0925 -> Add calculated metrics on widgets | 238 nodes; customer Excel example, three proposals for showing the operation | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4625-85584) |
| 0825 -> Widget multi currency | 251 nodes; multi-currency metric cards, customer-specific layouts | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4389-71156) |
| 0725 -> Widget with pending payments | 337 nodes; Prop 1 vs Prop 2, old widget and dialog, widget sizes | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4129-55508) |
| 0725 -> Items widget - it. 2 | Payout, payment and accrual items; static periods question | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4151-153891) |
| 0725 -> Items widget - it. 1 | 866 nodes; table explorations at four widths | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=4053-61843) |
| 0625 -> Team's default prepopulated dashboard | 320 nodes; the findings deck (above), three proposals, real-customer data for one proposal, onboarding copy | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3738-33790) |
| 0625 -> Metric aggregation -> MOVE TO COMP PLANS | Four named problems (same metric from different plans, duplicates within plans, metric list, ...) with user expectation and possible solutions | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3674-60232) |
| 0625 -> Add Members + payments to Split by | CS request quoted, chart variants | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3653-15994) |
| 0625 -> Export full dashboard | CS and engineering input on format | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3627-972) |
| 0625 -> Duplicate dashboard | Customer request, permission questions | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3612-2824) |
| 0325 -> Dashboard sharing | Reasoning for avatar placement next to Share | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3479-40138) |
| 1024 -> Dashboard Exploration 2 | 394 nodes; widget options, library, pacing, ranking, new metric flow, heights | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2603-63859) |
| 0824 -> Dashboard exploration 1 | 917 nodes; the origin of the dashboard: references and benchmark (Grafana, Kibana, PostHog, Mixpanel, and the ICM tools QuotaPath, CaptivateIQ, Spiff, Qobra), visualization, sketch, proposal, filtering, roles and permissions, widgets, empty state, edit flow, prototype, grid, drag and drop, resize | [open](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=1-10) |

## Image sources

| Use | Where |
|---|---|
| Research: retention and conclusions | Findings slides 2 to 8, from [3784:47279](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3784-47279) |
| Origin: benchmark board | 0824 -> Dashboard exploration 1, section "References & benchmark" ([2002:177](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2002-177)) |
| System rules: grid | 1024 -> Dashboard layout grid ([2471:31281](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2471-31281)) |
| Widget configuration depth | 1124 -> Dashboard metric widget ([2712:24892](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=2712-24892)) |
| Default dashboard result | 0725 -> Team's default prepopulated dashboard ([3990:2702](https://www.figma.com/design/D3I7XGCC7WulmGtydRj5aI/?node-id=3990-2702)) |
| Widget thumbnails | 1224 -> Dashboard images |
