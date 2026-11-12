# Abacum Figma index: Dataset Manager and Dimensions

Source material for the Dataset Manager case (deck, portfolio, interview answers). Page and node links open in Figma. Built 2026-11-09 through the Desktop Bridge; page lists are complete, highlights are from the pages searched that day, not every page. Page names start with the date as YYMM (`2202` = February 2022). A ✅ prefix means shipped or handed off; 🔒 means locked.

Full page-by-page indexes for every Remuner and Abacum file, built 2026-11-09 from a complete extraction, are in [figma/README.md](figma/README.md). This file stays as the Dataset Manager story view.

Ownership: all notes and designs are Manel's unless marked otherwise (confirmed 2026-11-09). The PM at the time was involved in scoping. Claim limits live in [experience-facts.md](experience-facts.md), "Dataset Manager".

Link pattern: `https://www.figma.com/design/<file key>/?node-id=<id with - instead of :>`.

## Best images for the story

| Story beat | What it shows | Link |
|---|---|---|
| Before | Back-office JSON schema, "Non-interactive display of backoffice syntax?" | [2201 -> Manage](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1503-90555) |
| Framing | Four "How might we" notes, "Self-service means activation" | [2201 -> Manage](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1503-90555) |
| Scope cut | User-action list with mapping and functions struck out | [image 16](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1506-79953) |
| Sequencing (restraint) | Architecture board: Mapping now, Transforming later | [architecture](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1506-92495) |
| Sequencing | Constraints: contextual sidebar, order of mapping steps | [constraints](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1506-92505) |
| Interim language | Transform panel with SQL-like formulas (`JOIN RATIO FROM ... ON`, `'Global' if ...`) | [transform - history 30](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1506-132731) |
| Interim language, shipped | Transform list with SQL-like steps | [transform - history 76](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2915-129484) |
| Mapping | Column settings: type, auto-map, dependencies count | [connect / column selected](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2813-116108) |
| Guardrails | "Dimension 'Suppliers' used in" dialog | [connect / column selected](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2813-117330), [Mappings](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1511-49988) |
| Guardrails | Impact warning, "Accept impact on 3 table filters" | [2207 -> Dimension dependencies view](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1390-42242) |
| Final language | Formula box with formula library (DATEDIFF) | [Marketing asset](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6451-70052) |
| Final language | Formula library: expander, list, content | [Formula library](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6358-100820) |
| Process | Kickoff, design review, handover checklists | [Formula library](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6358-100820) |

Code dates from `~/Dev/webapp`: DSM formula builder v1 2023-09-20 (ACTS-958), syntax check 2023-10-16 (ACTS-1030), editor autocomplete 2023-11 (ACTS-1179).

## Dataset manager (case deck)

File: [Dataset manager](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh) (Figma Slides). Source text: [decks/case-deck-dataset-manager.md](../decks/case-deck-dataset-manager.md).

| Slide | Content | Link |
|---|---|---|
| 1 | Cover | [1](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-42) |
| 2 | Context: dependency loop | [2](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-82) |
| 3 | Early flows | [3](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-83) |
| 4 | Research findings | [4](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-84) |
| 5 | Diagnosis: vocabulary map | [5](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-85) |
| 6 | Strategic pivot | [6](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-86) |
| 7 | Decision: SQL vs formulas | [7](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-87) |
| 8 | Delivery strategy | [8](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-88) |
| 9 | Final product | [9](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=1-89) |
| (skipped) | Old final-product slide | [-](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=34-28) |
| 10 | Outcome | [10](https://www.figma.com/design/ufLGMlcTQvBxZrHT2dS1eh/?node-id=20-4) |

## Abacum | Dataset manager - Exploration (Backup 27.3.23)

File: [rg5IG7leRJXbj8HP93Jnsk](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk). Explorations from January 2022 to March 2023.

| Page | Notes | Link |
|---|---|---|
| 2201 -> Manage | Scope, Notion links, user actions for tickets, HMW notes, architecture and constraints boards, two vision versions, short-term flows | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1503-90555) |
| 2202 -> Transform | First transform syntax; drafts like `Sum people_cost from cost_dataset`, `join ratio from other_dataset on ...` | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1506-79925) |
| 2202 -> Upload a new dataset | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=455-106195) |
| 2203 -> Disable buttons | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1214-219132) |
| 2204 -> Transform v2 | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1506-79926) |
| 2204 -> Transform v3 | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2014-133360) |
| 2204 -> Data loads tab | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1617-124167) |
| 2207 -> Dimension dependencies | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1754-124878) |
| 2208 -> Preview transformations | Includes the table-filter impact warning | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=1869-129836) |
| 2211 -> Delete dataset | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2102-137006) |
| 2211 -> Download dataset | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2110-140869) |
| 2211 -> Auto-sync | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2130-145300) |
| Auto-sync prototype | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2698-255028) |
| 2212 -> Async saving | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2195-166405) |
| 2212 -> GSheet Plugin | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2203-169369) |
| 2301 -> HRIS dataloads | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2522-197763) |
| 2301 -> HRIS dataset | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2541-201267) |
| 2301 -> Manually sync data | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2647-220017) |
| 2302 -> Rules, updates, data | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2765-262238) |
| 2302 -> New dataset flow | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2902-272463) |
| 2302 -> Delete data | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2957-273439) |
| 2302 -> Preview newly created columns | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=2993-279924) |
| 2302 -> Consistency | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3000-283213) |
| 2303 -> Schema flow | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3038-283299) |
| 2303 -> Dataset loads -> months | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=3150-415387) |
| Graveyard | | [open](https://www.figma.com/design/rg5IG7leRJXbj8HP93Jnsk/?node-id=330-77832) |

## Abacum | Dataset manager - Implementation

File: [jf2hsBYAPS9ilnauvYHWDR](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR). Handoff pages from February 2022 to March 2024; most have Jira frames, user stories and a design tracker.

| Page | Notes | Link |
|---|---|---|
| 🔒 2202 -> Manage dataset 1 | Early manage flow, JSON code window | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=421-19214) |
| 🔒 2202 -> Manage dataset 2 | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=547-43483) |
| ✅ 2202 -> Create | Create dataset, data types, column mapping | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=629-34356) |
| ✅ 2202 -> Transformations | First shipped transformations; "CURRENT SYNTAX" spec, planned JOIN; MVP frame | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=975-50656) |
| ✅ 2203 -> Auto mapping | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2601-129828) |
| ✅ 2205 -> Transformations v2 | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2303-114141) |
| ✅ 2205 -> Auto mapping v2 | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2398-128492) |
| ✅ 2207 -> Dimension dependencies | Column settings with dependencies; "used in" dialog | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2812-114540) |
| ✅ 2208 -> Actions & autocomplete | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2878-119546) |
| ✅ 2208 -> Data loads inside manager | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2900-122937) |
| ✅ 2208 -> Transformation preview | Transform list with SQL-like steps | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=2915-128806) |
| ✅ 2210 -> Create dataset without financial option | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3148-127690) |
| ✅ 2211 -> Delete dataset | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3314-134036) |
| ✅ 2212 -> Async saving | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3407-141636) |
| ✅ 2212 -> Auto-sync HRIS | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3525-144255) |
| ✅ 2302 -> Auto & manual update, update history | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=3764-151862) |
| ✅ 2303 -> Activity | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=4546-159595) |
| 2309 -> Transformation improvements | Formula box: toolbar, dialog, formula library, syntax help, column autocomplete, name validation, unsaved-changes dialog | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6355-99626) |
| 2311 -> Rename datasets, sync range | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6758-33601) |
| 2311 -> Reorder transformation steps | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6698-31745) |
| 2311 -> Manual adjustments | Row types, warnings and errors, column filters; whiteboard photo | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6568-6036) |
| 2403 -> Dataset details | Status quo, flow, specs | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=7779-15905) |
| 2403 -> Dependencies | Status quo, flows, specs | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=7871-19377) |
| ➕ Template | Handoff template | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=6897-159294) |
| 🪦 Graveyard | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=4794-162667) |
| Cover | | [open](https://www.figma.com/design/jf2hsBYAPS9ilnauvYHWDR/?node-id=56-20286) |

## Abacum | Dimensions - Exploration

File: [nNcePMVjBVUayV8oI5EmsZ](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ). Explorations from 2020 to February 2024; 2023 onwards belongs to the later dimensions project.

| Page | Notes | Link |
|---|---|---|
| 2011 -> Mappings (Dimensions) | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1208-29739) |
| 2021 -> Mappings (Dimensions) | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1208-33664) |
| Input | Team message on "how are we mapping nowadays" walkthroughs; Notion link | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=903-9102) |
| ⭐️ Vision | Dimension relationships, templates, "where used" ideas (Feb 2022) | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=367-15363) |
| ✏️ Concepts | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=729-49194) |
| 2203 -> Disable buttons | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1208-50104) |
| 2206 -> Mappings name | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1307-39419) |
| 2207 -> Dimension dependencies view | "Used in" dialog, impact warning, error copy | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1390-42242) |
| 2208 -> Dimension library | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1602-48014) |
| 2209 - Unmapped dialog box | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1673-49403) |
| 2210 -> Dimension library concepts | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1815-57925) |
| 2210 -> Dimensions table view | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=1889-61347) |
| 2210 -> Concept flows | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=2014-89303) |
| 2305 -> Dimensions vision & iterations | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=2755-107196) |
| 2306 -> Mapping vision | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3120-136648) |
| 2307 -> Mapping & Dimension vision | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3294-208944) |
| 2309 -> Delete dimension | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3349-71176) |
| 2309 -> Rename dimension items | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3364-100743) |
| 2309 -> Update dimension items from upload | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3400-1107) |
| 2309 -> Reorder dimension items | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3419-1657) |
| 2310 -> Show relationships when uploading a new mapping | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3465-30240) |
| 2401 -> Rename dimension items WORKSHOP | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3755-2334) |
| 2401 -> Dimension page new layout | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=3983-273654) |
| 2402 -> Dimensions management dialog | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=4160-76433) |
| Graveyard | | [open](https://www.figma.com/design/nNcePMVjBVUayV8oI5EmsZ/?node-id=729-49191) |

## Abacum | Dimensions - Implementation

File: [6c5Iwbr9X5FdhaDj0GD81O](https://www.figma.com/design/6c5Iwbr9X5FdhaDj0GD81O). 2024 handoffs; not part of the Dataset Manager story.

| Page | Notes | Link |
|---|---|---|
| Hand-off template | Specs, flow, design tracker, MUI component list | [open](https://www.figma.com/design/6c5Iwbr9X5FdhaDj0GD81O/?node-id=1890-28388) |
| ⏳ Dimension library | Create, edit, delete and rename dimensions and items; "used by" placement | [open](https://www.figma.com/design/6c5Iwbr9X5FdhaDj0GD81O/?node-id=729-49194) |
| 2402 -> Rename dimension items | Happy path, errors, refresh | [open](https://www.figma.com/design/6c5Iwbr9X5FdhaDj0GD81O/?node-id=1890-16604) |
| 2403 -> Dimension resource page | User stories, status quo, flows | [open](https://www.figma.com/design/6c5Iwbr9X5FdhaDj0GD81O/?node-id=1936-6406) |
| Graveyard | | [open](https://www.figma.com/design/6c5Iwbr9X5FdhaDj0GD81O/?node-id=729-49191) |
