# Abacum | Syntax - Implementation

File: [u7ZLkxpgFamXpEkr3si18l](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l). 14 pages (11 with content), about 280 top-level nodes. Handoffs for the modeling formula language, February 2023 to January 2024. Full listing: [catalog/abacum-syntax-implementation--u7ZLkx.md](catalog/abacum-syntax-implementation--u7ZLkx.md). Case source: [interviews/decks/case-deck-modeling-syntax.md](../../interviews/decks/case-deck-modeling-syntax.md).

Indexed 2026-11-09 from a full extraction. Ownership: Manel's. 🟡 marks pages not shown as shipped; ✅ shipped or handed off. Tickets on the canvas use the ENGN prefix.

## Pages

| Page | What it covers | Notable content | Link |
|---|---|---|---|
| Hand-off template | The syntax-team handoff template: Specs (loading, overflow, empty, errors, first use, no results), Flow, Copy in context (current vs proposed error and warning copy), Design tracker, MUI list | "Copy in context" section is a reusable pattern for rewriting error copy | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=1630-21561) |
| 2401 -> Formula popover | Function help popover opened from autocomplete | User stories: understand what a formula does, and how it's written, to make fewer mistakes; fallback copy pointing to Abacum Academy | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=1630-21560) |
| 🟡 2303 -> Cohort formulas | Referencing cohorts and month ranges in formulas (ENGN-876, 877, 878) | Iterations 2 and 3: `cohort-N`, `cMMYY`, `mN`; autocomplete options 1 and 2; cohort decay table | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=1443-41036) |
| ✅ 2305 -> Alias in autocomplete, and dimension blocks | Using the dimension alias from Actuals in autocomplete and blocks | Before and after | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=1188-71742) |
| ✅ 2303 -> Aggregations context | Explaining SUM, AVERAGE and FUNCTION aggregation in the module builder | Helper copy for each setting ("FUNCTION ... should be used to calculate rates, for example, Cost / Revenue") | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=1045-61884) |
| ✅ 2303 -> Syntax colors | Spec sheet for syntax chips (variable, dimension, date) with token names | `color/syntax/border/variable`, `color/syntax/bg/dimension` etc.; the DS link from the syntax work | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=870-29268) |
| 🟡 2303 -> Time ranges | Dynamic, fixed and cumulative time ranges (`.t-1:t-3`, `Jan22:Dec22`) | Allowed vs not allowed examples, expected table output per time aggregation (SUM, FIRST, AVERAGE, FUNCTION, LAST), step-by-step autocomplete behaviour | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=706-21302) |
| 🟡 2302 -> Formula relationship | How a formula relates Actuals and Forecast | Two examples | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=618-18366) |
| 🟡 2302 -> Autocomplete couples of objects | Autocomplete suggesting measure + dataset pairs (`SUM(Balance) FROM Financials`) | | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=9-8585) |
| ✅ 2302 -> Highlighting variable relationship | Dashed highlight of referenced variables in the grid while editing a formula | Exact border spec; open task for variables out of viewport | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=504-10189) |
| 🟡 2302 -> Syntax usability | The core syntax cleanup: remove `.Current`, dimension blocks, block deleting dependencies, remove SHIFT, predict next parameter, underline incomplete formulas | 54 nodes, 14 Jira frames; before/after pairs; step-by-step autocomplete flows (SUMACTIVE, `t-1`) | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=510-12665) |
| Cover | Cover | | [open](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=1-8595) |

## Image sources

| Use | Node | Link |
|---|---|---|
| Before/after of the syntax cleanup | Syntax usability page | [510:12665](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=510-12665) |
| Token-level spec for syntax chips | Specs | [870:29331](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=870-29331) |
| Time range rules, allowed vs not allowed | Frame | [719:27762](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=719-27762) |
| Cohort autocomplete options | Autocomplete | [1454:23703](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=1454-23703) |
| Error copy rewrite pattern | Copy in context | [1630:22332](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=1630-22332) |
