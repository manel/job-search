# Abacum | Dataset manager - Implementation

File: [jf2hsBYAPS9ilnauvYHWDR](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR). 27 pages, about 1,500 top-level nodes, 123 image fills. Handoff pages from February 2022 to March 2024. Full frame-by-frame listing: [catalog/abacum-dataset-manager-implementation--jf2hsB.md](catalog/abacum-dataset-manager-implementation--jf2hsB.md). Story-level picks for the Dataset Manager case: [../abacum-figma-index.md](../abacum-figma-index.md).

Indexed 2026-11-09 from a full extraction of every page. Ownership: Manel's (confirmed 2026-11-09). Notes prefixed "Julian:" are review comments from the head of design; "Manuel" is an engineer; "Josep Maria" and "Carol" appear as owners of tasks or copy.

Page structure from 2023 onwards follows Manel's handoff template: Status quo, Flow, Specs, Design tracker (kickoff, design review, handover checklist), user stories, Jira links.

## Pages

| Page | What it covers | Notable content | Link |
|---|---|---|---|
| 2403 -> Dependencies | Column info toolbar with column details and column dependencies (incoming and outgoing) | User stories referencing ACTS-1925; rules: dependencies only on columns mapped to a dimension, internal transformations excluded, one entry per resource; "Assign as" menu by column type; transformation-created columns not editable | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=7871-19377) |
| 2403 -> Dataset details | Info panel showing the source of a dataset (report, view, object, sheet) for every integration | Source fields per connector: HubSpot, Google Sheets, Tableau, Snowflake, Salesforce, Personio, Bamboo, HiBob, Gusto, Workday, Xero, QuickBooks, Sage Intacct, NetSuite, S3; open question "For which integrations can we provide a link to the source?" | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=7779-15905) |
| 2311 -> Manual adjustments | Editing dataset rows in the app: row types (original, excluded, added), row actions, cell states, warnings and errors, column filters | Sections: Cases, Edge case (cells with transformations), Warnings & errors, Column filters, Potential alternative; whiteboard photo; resync and delete-data-load dialogs that preserve manual rows; error copy "Dataset not saved. Resolve 8 errors and try again."; ACTS-1312 | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6568-6036) |
| 2311 -> Reorder transformation steps | Drag-to-reorder and duplicate for transformation steps | Option A / Option B, status quo vs proposal; formula examples using `IF ... IN [...] THEN` | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6698-31745) |
| 2311 -> Rename datasets, sync range | Rename dialog; month picker for sync range | Spec dated 11.01.24 "For implementation": one picker for single, multiple and shift-click ranges, no toggle | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6758-33601) |
| 2309 -> Transformation improvements | Formula box and its support: toolbar, dialog, formula library, syntax input help, column autocomplete, improved helper, column name validation, unsaved-changes dialog | FP&A feedback quoted on the canvas: users can't reference column names because headers are auto-capitalised, and joins need a dataset code users don't know; numbered ideas (highlight error line or word, click a column to insert it, save steps with errors); "Marketing asset" section with DATEDIFF | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6355-99626) |
| ✅ 2303 -> Activity | Activity log for datasets: event types, relative timestamps, status (in progress, failed, scheduled), error detail dialog | Full event list (create, add values, replace, delete, rename, auto-sync, new dimension items, schema edit); upload-with-warnings copy (350/370 rows, unexpected columns, rows with missing dimension values) | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=4546-159595) |
| ✅ 2302 -> Auto & manual update, update history | Scheduled auto-sync, sync range, manual upload, month-level data view with bulk and single actions | 230 nodes, the largest page; schedule presets, 5-schedule limit, 24-month list rule, month error states, prototype flows | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3764-151862) |
| ✅ 2212 -> Auto-sync HRIS | HRIS auto-sync v1 and manual import (Personio) | Flow: hover, sync triggered, processing, error, success; tickets DA-1343, DA-1345, DA-1346 | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3525-144255) |
| ✅ 2212 -> Async saving | Saving progress snackbar (1/3, 2/3) that survives dismissal | DA-1254 | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3407-141636) |
| ✅ 2211 -> Delete dataset | Delete with and without dependencies | Confirmation dialog lists modules and tables that use the dataset | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3314-134036) |
| ✅ 2210 -> Create dataset without financial option | Creation flow when the dataset isn't financial (date required, account not) | Upload 1/3 to 3/3, disabled-button rules | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3148-127690) |
| ✅ 2208 -> Transformation preview | Preview modal before saving transformations | Preview and save disabled with no new actions | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2915-128806) |
| ✅ 2208 -> Data loads inside manager | File and synced data loads listed in the manager | 3 frames | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2900-122937) |
| ✅ 2208 -> Actions & autocomplete | Action history (go back to a previous table state), editing an action, fuzzy autocomplete | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2878-119546) |
| ✅ 2207 -> Dimension dependencies | Where a dimension is used (datasets, modules, tables) from column settings | Modal with expanded per-resource detail | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2812-114540) |
| ✅ 2205 -> Auto mapping v2 | Auto-map values, warning before activation, empty-value assignment, processing error | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2398-128492) |
| ✅ 2205 -> Transformations v2 | Adding new columns from transformations | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2303-114141) |
| ✅ 2203 -> Auto mapping | First auto-map states | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2601-129828) |
| ✅ 2202 -> Transformations | First shipped transform panel: action list, drag and drop with error feedback, action history, autocomplete | "MVP" frame (1440×5640) is a full syntax spec: conditionals, switch, JOIN, FX conversion, copy, sum by month, hardcoded values, string functions, marked "CURRENT SYNTAX" | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=975-50656) |
| ✅ 2202 -> Create | Dataset creation: upload, column mapping (date, account, measure, dimension), data types, date range | "Learnings" note from an engineer on pre-filling types and pre-mapping dimensions; a creation-funnel metrics plan (abandon rate, errors, support requests, button clicks) | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=629-34356) |
| 🔒 2202 -> Manage dataset 2 | Connect and Transform panels with the raw JSON schema code window | Changelog notes: raw vs transformed diff, create dimension from dropdown, auto-map on update | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=547-43483) |
| 🔒 2202 -> Manage dataset 1 | Earlier version of the same | JSON schema; Hack font for code | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=421-19214) |
| ➕ Template | Handoff template: Flow, Specs, Design tracker, user story format | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6897-159294) |
| 🪦 Graveyard | Discarded: card vs top-bar overview, relative-date rules, column type confirmation with bulk confirm or skip, dataset alerts | Head of design and engineer comments on relative timestamps | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=4794-162667) |
| Cover | Cover | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=56-20286) |

## Image sources

| Use | Node | Link |
|---|---|---|
| The starting point: back-office JSON schema in the code window | dataset / transform / expand code window | [547:43484](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=547-43484) |
| First syntax spec, all functions on one board | MVP | [980:56203](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=980-56203) |
| First shipped transform panel | transform - history 51 | [975:52609](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=975-52609) |
| Creation flow with required columns | connect / default | [630:36807](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=630-36807) |
| Measurement plan for the creation funnel | measure | [687:47537](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=687-47537) |
| User feedback that drove the formula box work | Syntax input help | [6358:121454](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6358-121454) |
| Final formula box | Marketing asset | [6451:70052](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6451-70052) |
| Error handling for invalid column names | Column name validation | [7542:34479](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=7542-34479) |
| Row-level editing rules | Cases: Row types and actions | [6586:315904](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6586-315904) |
| Sync schedule and month-level data | dataset manager | [4795:173926](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=4795-173926) |
| Activity log status quo | Status quo | [4715:168288](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=4715-168288) |

Screens show real-looking customer data (company names in formulas, connector IDs). Blur or replace before external use.
