# Abacum | Engine - Implementation

File: [Qm2oEoyLPrWg3cX0bJBWvN](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN). 28 pages (23 with content), about 460 top-level nodes, 770 image fills. Handoffs for the modeling engine (module builder, formulas, variables, dimensions), January to October 2023. Full listing: [catalog/abacum-engine-implementation--Qm2oEo.md](catalog/abacum-engine-implementation--Qm2oEo.md). Related: [abacum-syntax-implementation.md](abacum-syntax-implementation.md).

Indexed 2026-11-09 from a full extraction. Ownership: assumed Manel's. **"Change switch-over date" is a rework** (decided by Manel 2026-11-09): the head of design had designed the feature earlier, so describe it as "I reworked the switch-over date", not "I designed it". On "Change switch-over date" the head of design left a note on the canvas: "Did you check my past designs? Is this a module setting or a version setting?" That reads as review of Manel's page, with earlier designs on the same topic by the head of design. Tickets use the ENGN prefix.

Page-name dates in this file are DDMM, all in 2023 (`2301` = 23 January, `3005` = 30 May, `2310` = 23 October). The Engine exploration file uses the same convention with slashes ("23/02"), and the June 2023 screenshot on the Relationship panel page fits. Corrected 2026-11-09; an earlier version of this index read some of them as YYMM.

## Pages

| Page | What it covers | Notable content | Link |
|---|---|---|---|
| 🟡 2310 -> Order dimension items | Reorder dimension items once, applied across the platform (ENGN-960) | Copy variants for the "applies everywhere" warning, including a set labelled "AI suggestions" | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2755-266216) |
| 🟡 2306 -> Duplicate module | Naming rule for duplicates: "CF (1)", "CF (2)" | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2558-285267) |
| 🟡 2306 -> Delete modules (Iterations 1 and 2) | Delete with and without variable dependencies: contextual menu, modal, error, confirmation | Two iterations kept side by side | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2558-278218) |
| 🟡 2305 -> Custom sections | Organising variables into sections: add, remove (with variables), rename, drag and drop, empty-section error (ENGN-584) | Naming rules shared with variables and groups (limits, reserved names, emojis) | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2309-210280) |
| ✅ 3105 -> Concurrency module changes | What a user sees when someone else is changing the same module: update in progress, completed, can't save | Several rewrites of the "can't save" copy, long to short | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2107-168712) |
| ✅ 3005 -> Split toolbar | Splitting the module builder toolbar into dimensions and settings tabs | Token-level spec | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2106-163239) |
| 🟡 3005 -> Add variable description | Variable description with "Used by" and "Uses" | Critique note: "Update designs" | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2158-179935) |
| ✅ 3005 -> Relationship panel | Panel showing what a variable uses and what uses it, across datasets, versions and other modules; loading skeleton, backend-error empty state, pulse animation | Token-level spec; screenshot dated 2023-06-15 | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2212-186968) |
| ✅ 2505 -> New modules page UI | Modules list: collapsed and expanded groups, search, hover | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2103-162014) |
| ✅ 2305 -> Logic panel | Viewing a variable's formula from the table builder and from Spaces, then jumping into the module | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2085-138213) |
| 🟡 0805 -> Show calculation time | Calculation time per variable with tooltip | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=729-49198) |
| 🟡 0305 -> Auto-save | Auto-save in the module builder: formula change, values update | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1989-130466) |
| 🟡 2304 -> Re-order dimension items | Drag and drop in the dimensions sidebar (earlier version of 2310) | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1926-124238) |
| 🟡 2303 -> Search variable | Find in table and in diagram views: counter, arrow navigation, auto-expand groups, nothing found, long strings | Construction spec (paddings, gaps) | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1831-113459) |
| ✅ 2302 -> Power | POWER function with expected output per time aggregation | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1519-75323) |
| ✅ 2302 -> Change switch-over date | Moving the actuals-to-forecast switch-over date: dynamic vs fixed, drag on the timeline, 3-dot menu | Problem written as two user scenarios: an upload pushes the switch-over date and forecast months show 0s; head of design review note (see Ownership) | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1514-72831) |
| ✅ 2302 -> Ramp up | RAMP function for new hires: relative-time variables, ramp assumptions | Problem stated against the customer's mental model ("Today the RAMP is applied starting Feb 22, but in the customer's mind it should start Jan 22") | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1414-49255) |
| ✅ 2301 -> Show empty values | Toggle per variable | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1436-51088) |
| ✅ 2301 -> Formulas | ROLLING_AVERAGE and ROLLING_SUM | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1403-11522) |
| ✅ 2301 -> Handle references to blank as 0s | Workaround with constants | | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1469-61778) |
| ✅ 2301 -> IF ELSE | Conditionals on actuals, versions and disjoint dimensions | Worked examples: sales bonus over $100,000, new hires per month from an HRIS dataset | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1410-31233) |
| ✅ 2301 -> People planning formulas | DISTRIBUTE, DISTRIBUTE_MONTHLY, DISTRIBUTE_YEARLY, COUNT_STARTDATE for salaries and new hires | Expected output per aggregation; note that FUNCTION aggregation is a known product limitation | [open](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1405-15959) |

## Image sources

| Use | Node | Link |
|---|---|---|
| Dependency visibility in the engine | Relationship panel | [2212:186968](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2212-186968) |
| Formula visible from reports | Logic panel | [2085:138213](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2085-138213) |
| Problem framed as user scenarios | Change switch-over date page | [1514:72831](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=1514-72831) |
| Concurrency error copy iterations | Concurrency module changes page | [2107:168712](https://www.figma.com/design/Qm2oEoyLPrWg3cX0bJBWvN/?node-id=2107-168712) |
