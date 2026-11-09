# Remuner | Datasets

File: [567oKEE7i0ktL73emiSdCL](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL). 40 pages (32 with content), about 2,600 top-level nodes. Data sources and datasets for incentive calculations, August 2024 to December 2025: Excel and CRM sources, field formats, formulated and conditional fields, links to plans and parameters, errors and system alerts. Full listing: [catalog/remuner-datasets--567oKE.md](catalog/remuner-datasets--567oKE.md).

**Duplicate file:** [VMALBdcCPmY2jhEl4C3tQM](https://www.figma.com/design/VMALBdcCPmY2jhEl4C3tQM) has the same name and is identical: same 40 pages, frames, sizes, text and node IDs (diffed 2026-11-09). It's probably a re-import. Use 567o.

Indexed 2026-11-09 from a full extraction. Ownership: Manel's, including the Spanish "Problema / Solución / Specs" notes (confirmed 2026-11-09). A second designer, Marina, appears on two exploration pages. On "0525 -> Parameters view on dataset card" she posts proposals and Manel replies with direction ("the horizontal version works better... try icon plus number for each type"). On "0625 -> Data source fields dialog logic" there's a note addressed to her. Treat those two pages as collaborative work with Manel reviewing. "Test Marina 1" elsewhere is a sample user name.

Most pages open with a Problema / Solución / Specs note in Spanish, which gives each feature a written problem statement.

## Pages (handoff)

| Page | Problem it solves | Notable content | Link |
|---|---|---|---|
| 1225 -> Dataset & integration errors | Failed syncs and calculations were invisible | Email and in-app notifications ("Salesforce integration sync failed"), editing datasets with integration errors | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=3416-22956) |
| 1125 -> Hide datasets for earnings obfuscated roles | Roles that can't see earnings could still see the datasets behind them | Per-role dataset hiding | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=3153-163724) |
| 1025 -> Dataset processing state | Excel uploads took time with no feedback | Reuses the plan-recalculating pattern; tooltip "Your Excel file is being processed. 56% loaded." | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2967-24683) |
| 1025 -> Multiple conditions | Conditional formulas couldn't nest or hold several rules | Rule table modelled on Smart Rules, with an Else row; partial saves allowed | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=3032-72957) |
| 1025 -> Dataset fields format | Numbers or dates read as text, causing calculation and alignment errors | Edit popover with a type segmented control (date, number, text) and format options | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2949-15053) |
| 0825 -> Add plan on parameters tooltip list | Couldn't tell which plans a dataset's parameters fed | Plans shown green (active) or orange (expired) | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2803-8895) |
| 0725 -> Archive datasets | Unused datasets cluttered the list | Archive from card and list view; disabled when in use; confirmation | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2762-25076) |
| 0725 -> Datasets in list form | Card view didn't scale | Table view with filters, hover tooltips for plans, formulated fields and parameters | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2604-6365) |
| 0625 -> System alerts of critical changes | No warning before changes that break live plans | Alerts for deleting fields, editing filters or integration, changing or duplicating user mapping IDs, deleting a dataset | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2536-12970) |
| 0925 -> Disable object selection if dataset in use | Objects assigned to plans could be changed and lose configuration | Disabled with tooltip "This object can't be changed because it's used in a plan." | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2835-2321) |
| 0625 -> Data source selector | Dialog allowed CRM and Excel at once | One source per dataset; source locked once linked to an active plan | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2439-307672) |
| 0525 -> Parameters view on dataset card | Parameters on a data source weren't visible | Card with counts and tooltips per type | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2389-1102) |
| 0325 -> Link params to dataset | Linking plan parameters to a dataset or an Excel template | | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2236-9886) |
| 1024 -> Group by: formulated field | New column grouping fields for metrics | User story | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2132-8372) |
| 0824 -> Update Excel file | Replacing a dataset's file | Pre-populate matching columns, internal backup before update, first sheet default | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2039-1963) |

## Pages (exploration)

| Page | What's there | Link |
|---|---|---|
| 1125 -> Obfuscate dataset | Role editor with dataset visibility | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=3127-4068) |
| 1025 -> Dataset & integration errors | 102 nodes; problem: datasets stuck "in progress" with no feedback; rules for which datasets trigger alerts (not archived, last update over 24h) | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=3040-80650) |
| 1025 -> Show excel file loading | Current flows from production screenshots (6 Oct 2025), five status proposals | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2918-288621) |
| 1025 -> Linked & Nested conditions 2 | 335 nodes; conditional formula builder iterations; benchmark of Notion nested filters, Kayako, Gemini | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2897-90209) |
| 1025 -> Definir formato de datos | Current flow, two proposals, per-type alignment notes | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2872-10982) |
| 0925 -> Alert dialog for dataset objects | Same problem as the handoff page | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2831-15403) |
| 0825 -> Add plan on parameters tooltip list | Two proposals: dialog with plan link vs tooltip | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2796-9892) |
| 0725 -> Archive datasets | Archive only datasets not in use; alert if active | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2715-3476) |
| 0725 -> Datasets in list format | Column adjustments | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2563-3286) |
| 0625 -> Data source fields dialog logic | Current field-selection logic written out; note addressed to Marina | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2448-5019) |
| 0625 -> Dataset source selector | 114 nodes; locked vs editable source rules; production screenshots | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2408-7739) |
| 0525 -> Parameters view on dataset card | Marina's proposals and Manel's feedback thread | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2383-2) |
| 0325 -> Linked & Nested conditions | 1,081 nodes, the largest page in the Remuner set; five dialog proposals, "search formula on another dataset" (lookup by ID), nested conditions, benchmark, current flow | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2265-4691) |
| 0225 -> Link params to dataset | First version | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2220-5305) |
| 1024 -> Group by | Functions COUNT, MAX, MIN, SUM, AVG, RANK; default value for unmatched rows | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=2118-3826) |
| 0824 -> Update Excel file | Option 1 strict (same structure) vs Option 2 relaxed (remap) | [open](https://www.figma.com/design/567oKEE7i0ktL73emiSdCL/?node-id=1-10) |

## Image sources

| Use | Where |
|---|---|
| Written problem statements per feature | Note frame at the top of each 2025 page |
| Conditional formula proposals side by side | 0325 -> Linked & Nested conditions, "Dialog samples" section |
| Strict vs relaxed update option | 0824 -> Update Excel file (exploration), sections Opt 1 and Opt 2 |
| Guardrails for live plans | 0625 -> System alerts of critical changes |
| Silent failure fixed | 1225 -> Dataset & integration errors |
| Design review with another designer | 0525 -> Parameters view on dataset card (exploration) |
