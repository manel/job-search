# Abacum | Engine - Exploration (Jan 22 - May 23)

File: [dfhfrOUz0sAqruChlOFUCM](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM). 27 pages (23 with content), 2,105 top-level nodes. Modeling-engine explorations. Despite the file name, the dated pages run January to May 2023, named DD/MM ("23/02" = 23 February 2023; "1705" = 17 May 2023). This confirms the DDMM reading of the Engine implementation pages. Full listing: [catalog/abacum-engine-exploration-jan-22-may-23--dfhfrO.md](catalog/abacum-engine-exploration-jan-22-may-23--dfhfrO.md). Later explorations: [abacum-engine-exploration-current.md](abacum-engine-exploration-current.md). Handoffs: [abacum-engine-implementation.md](abacum-engine-implementation.md).

Indexed 2026-11-09 from a full extraction. Ownership: assumed Manel's, with limits. Notes signed "Manel" appear on Ramps. "👭 2303 -> Variable library (WORKSHOP)" was a team workshop. Who ran it isn't recorded; Manel recalls the workshops as shared (2026-11-09). Present their ideas as team output and claim only what Manel took forward. Comments come from Josep (product) on the switch-over date, and engineers (Mike, Adrià) are mentioned on relationships. ✅ shipped, 🟢 approved, 🟡 not shipped, [WIP] work in progress. Tickets use ENGN.

## Evidence on the canvas worth reusing

- "0205 -> Relationships": "Problem #1: 15 users have reported that they would like to better understand the relationships between their modules", followed by the evidence. This led to the relationship panel that shipped ("✅ 3005 -> Relationship panel" in the implementation file).
- "0205 -> Variable bulk actions": "Problem #2: 20+ customers have reported that they would like to do bulk actions", followed by the evidence.
- "23/02 -> Create/edit metrics outside a module": two problem statements (users lack context when creating metrics; users can't build ad hoc metrics without a new module), proposals A–C over seven iterations, and a like/wish/wonder board.
- "23/02 -> Forecasting diff levels": What/Why pairs per capability ("several customers need to forecast at a lower granularity than actuals"), with a 5-step rollout and rules.

Evidence class: user and customer counts as written on the canvas. The underlying evidence frames are next to them but the source data isn't saved elsewhere.

## Pages

| Page | What it covers | Notable content | Link |
|---|---|---|---|
| [WIP] 🟡 1705 -> Add cohort dimension | Marking a dataset column as a cohort; cohort settings | Open questions (more than one cohort per model?) | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2897-456261) |
| 🟢 1105 -> Custom sections (or tags) | Sections in the module builder (ENGN-584, iteration 4) | 216 nodes; full create, rename, drag, delete flows | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2820-384175) |
| [WIP] 🟡 1105 -> Variable description | ENGN-578 | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2820-388345) |
| [WIP] 🟡 1105 -> Relationship in the sidebar | "Sources" and "Used by" in the sidebar, with highlighting in the module | Critique: "If I navigate different variables, I will lose context"; scope question discussed with engineers (in Catalan) | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2820-386955) |
| [WIP] 🟡 1105 -> Edit version formula in spaces | Editing formulas from reports (ENGN-544, "metric centric" iteration 5) | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2820-385565) |
| 🟡 0905 -> Modeling in context | Editing a variable from a Space; session notes from 10 May 2023 listing open technical questions | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2774-361379) |
| 🟡 0305 -> Play pause re-calculations | Auto-save vs manual recalculation, value update alternatives | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2699-347495) |
| 🟡 0205 -> Variable bulk actions | Bulk edit mode for variables | Problem #2 with customer count | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2651-314330) |
| 🟡 0205 -> Relationships | Relationships sidebar, modal, tabs; "general info toolbar inspired by Gdrive" | Problem #1 with user count | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2625-294218) |
| 🟡 2404 -> Calculation time when saving | Progress options while saving: steps, async, line by line, number flips | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2545-270932) |
| 🟡 1904 -> Time modifiers | Typing month references (`.Jan22`) | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2437-164984) |
| 🟡 1804 -> TB / MB merging concepts | 231 nodes; merging the table builder and the module builder; P&L, balance sheet and cash-flow structures | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2365-134660) |
| 🟡 17/04 -> Agg. type in the sidebar | Option A vs B for aggregation type | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2352-131982) |
| 👭 2303 -> Variable library (WORKSHOP) | 505 nodes; team workshop: benchmark (Finmark, Fathom, Runway, Causal, Mosaic, Tableau, Notion and analogies like supermarket shelves), user needs and problems, sketches, playground, outcome | HMWs: "HMW enable users to easily find the variable they're looking for?", "...give users an overview of important company metrics?" | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2119-124499) |
| 🟡 23/03 -> Duplicate variable | Modal vs in-context naming | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1982-103683) |
| 🟡 23/02 -> Create/edit metrics outside a module | See evidence above | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1876-87360) |
| 🟡 23/02 -> Var dependencies diagram | Five diagram types (per dimension, per time period, circular reference) and option D iterations | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1776-78257) |
| 🟡 23/02 -> Forecasting diff levels | See evidence above | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1789-79455) |
| ✅ 23/02 -> Ramps | 283 nodes; RAMP function: problem statements, deprioritised option, iteration 1, relative-time formulas | Manel's notes: "Can we get rid of the variable type selector? I'd go for the platform detecting the values. It adds another layer of complexity." | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1710-73685) |
| ✅ 23/01 -> Switch-over date the module level | Per module vs per version | Product comment arguing for a version setting, to keep frozen forecasts | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1603-13796) |
| 🟡 23/01 -> Hide actuals | | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1603-26833) |
| ✅ 15/01 -> People planning | DISTRIBUTE_WEEKLY, BOMONTH/EOMONTH, new-hire formula | | [open](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1683-63789) |

## Image sources

| Use | Node | Link |
|---|---|---|
| Evidence-led problem: relationships (15 users) | 0205 -> Relationships | [2625:294218](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2625-294218) |
| Evidence-led problem: bulk actions (20+ customers) | 0205 -> Variable bulk actions | [2651:314330](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2651-314330) |
| Workshop: needs, sketches, outcome | User needs/problems / Outcome | [2119:125540](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2119-125540), [2206:129959](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2206-129959) |
| Workshop benchmark | Benchmark | [2119:125422](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=2119-125422) |
| Forecasting at different granularities | Approach 3 | [1820:80540](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1820-80540) |
| RAMP problem statements | problem-statement | [1715:82101](https://www.figma.com/design/dfhfrOUz0sAqruChlOFUCM/?node-id=1715-82101) |
