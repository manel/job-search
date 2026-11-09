# Abacum | Dataset manager - Exploration (Backup 27.3.23)

File: [rg5IG7leRJXbj8HP93Jnsk](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk). 29 pages (26 with content), about 2,700 top-level nodes. Explorations for the Dataset Manager from January 2022 to March 2023. Full listing: [catalog/abacum-dataset-manager-exploration-backup-27-3-23--rg5IG7.md](catalog/abacum-dataset-manager-exploration-backup-27-3-23--rg5IG7.md). Handoffs: [abacum-dataset-manager-implementation.md](abacum-dataset-manager-implementation.md). Story picks for the case: [../abacum-figma-index.md](../abacum-figma-index.md).

**This is a March 2023 snapshot.** The live file, [abacum-dataset-manager-exploration-live.md](abacum-dataset-manager-exploration-live.md) (`SX7z0Cp4IMIw8RmNyrsI5G`), continues it to February 2024 but has dropped the 2022 pages, so keep both.

Indexed 2026-11-09 from a full extraction. Ownership: Manel's (confirmed 2026-11-09). Questions on the canvas are attributed to "Julio", Manu and Dave (engineering and product); "Manuel" is an engineer.

## Pages

| Page | What it covers | Notable content | Link |
|---|---|---|---|
| 2303 -> Dataset loads -> months | Information architecture for a dataset as a resource: schema (transformation, mapping, preview), months, transactions, updates, activity, usage | Status quo, Option A vs B, Round 1, analysis, prototype, Round 2: a tested iteration | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3150-415387) |
| 2303 -> Schema flow | Setting up a dataset schema: encoding, region, header row, ignored columns, column types and formats | Benchmark of ClickUp and Causal upload flows; an "Outreach" section | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3038-283299) |
| 2302 -> Consistency | Icon and element consistency experiments | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3000-283213) |
| 2302 -> Preview newly created columns | Data pipeline made visible: raw, ingested, processed, mapped | Minimum, better and ultimate solution side by side; SQL-like formulas in the transform panel | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2993-279924) |
| 2302 -> Delete data | Deleting data for a time period | User story; month and transaction views; 165 nodes | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2957-273439) |
| 2302 -> New dataset flow | Status quo vs Option A (quick fix) vs Option B (modal wizard) | Full connector list by category (ERP, accounting, HRIS, BI, CRM, spreadsheets) | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2902-272463) |
| 2302 -> Rules, updates, data | 446 nodes, the largest page. Dataset overview, update rules, sync history, notification hub, resource panel | 100 notes; Proposal A vs B; upload requirements | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2765-262238) |
| 2301 -> Manually sync data | Manual sync for HRIS and transactional datasets: current month, past periods, file upload | Proposal to merge three actions into one modal | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2647-220017) |
| 2301 -> HRIS dataset, HRIS dataloads | One frame each | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2541-201267) |
| 2212 -> GSheet Plugin | Google Sheets plugin to push data into Abacum | Benchmark, Plugin UX v1.0 and v2.0, settings and data sidebars, error handling; open questions on shared sheets and concurrent users | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2203-169369) |
| 2212 -> Async saving | Early version of the handoff | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2195-166405) |
| 🙋🏻‍♀️ Auto-sync prototype | Prototype for a user test: daily, weekly and monthly schedules, date pickers | A test script on the canvas: tasks ("set up a recurrent sync for Allocations and Metrics weekly on Fridays at 9 PM...") and questions to probe | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2698-255028) |
| 2211 -> Auto-sync | 505 nodes. Scheduling rules (new data vs refresh old data, quarter close), notifications on error | 92 notes; whiteboard photo from December 2022 | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2130-145300) |
| 2211 -> Download dataset | Download raw vs processed, button states while processing | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2110-140869) |
| 2211 -> Delete dataset | Dependencies check modal before delete | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2102-137006) |
| 2204 -> Transform v3, 2204 -> Transform v2 | Adding new columns typed as measure or dimension | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2014-133360) |
| 2208 -> Preview transformations, 2207 -> Dimension dependencies | Dependencies modal (same frames on both pages) | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1869-129836) |
| 2204 -> Data loads tab | File and synced data loads | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1617-124167) |
| 2203 -> Disable buttons | 3 frames | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1214-219132) |
| 2202 -> Upload a new dataset | Creating a dataset from scratch and uploading to an existing one | The back-end schema validation errors, copied verbatim ("Schema contains no defined measures", "Formula {formula_name} is of an undefined type"); questions challenging tech limits ("Do we really need to upload a file to set up integrations?", "Can we kill the types?") | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=455-106195) |
| 2202 -> Transform | First transform panel: actions, autocomplete, drag, SQL-like formulas | 136 nodes | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1506-79925) |
| 2201 -> Manage | The framing page: scope, HMW notes (dataset level and column level), cases for when customers update datasets, architecture and constraints boards | Already indexed in detail for the case | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1503-90555) |
| ⚰️ Graveyard | Contextual-menu column actions (rename, split, map, disable), early error copy | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=330-77832) |

## Image sources

| Use | Node | Link |
|---|---|---|
| Framing: HMW notes and scope | 2201 -> Manage | [1503:90555](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1503-90555) |
| Back-end errors users used to get | 2202 -> Upload a new dataset | [455:106195](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=455-106195) |
| Minimum / better / ultimate solution | 2302 -> Preview newly created columns | [2993:279924](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2993-279924) |
| Benchmark: ClickUp and Causal | Schema flow sections | [3041:286886](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3041-286886), [3041:286939](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3041-286939) |
| Usability test script and prototype | 🙋🏻‍♀️ Auto-sync prototype | [2698:255028](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2698-255028) |
| Tested iteration rounds | 2303 -> Dataset loads -> months | [3150:415387](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3150-415387) |
| GSheet plugin v1 vs v2 | Plugin UX sections | [2216:180758](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2216-180758), [2269:171568](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2269-171568) |
