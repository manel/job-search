# Notion index: Abacum

Index of Manel's Abacum Notion export at `~/Desktop/Abacum (Notion)` (outside the repo), built 2026-11-09. It covers the Design and Product workspaces, the Abax design-system workspace, Manel's personal notes, his 1:1 log with the head of design, and research. Videos were skipped. Images, PDFs and spreadsheets were counted but not opened.

Three layers, same as the [Figma index](../figma/README.md):

1. **This page:** what the export holds, where Manel's work is, and what it adds to or contradicts in the register.
2. **[catalog.tsv](catalog.tsv):** one row per unique page (title, parent database, owner or author, date, word count, path). Search it to locate a page. It leaves out the hiring and candidate databases, onboarding pages, and the 1:1, PDP and feedback pages.
3. **The export itself:** read pages with `scripts/notion-index/totext.py` (see Re-running).

Deck and live-case edits drawn from the export: [deck-and-case-updates.md](deck-and-case-updates.md).

Paths below are relative to the export root. Long Notion IDs are dropped from page names.

## What the export contains

- 7,751 files: 5,134 HTML pages and 2 Markdown, 330 CSV database exports, about 2,090 images, 81 videos (skipped), 39 PDFs, 15 spreadsheets.
- 3,913 unique pages. 1,207 page IDs appear more than once because "Abax Design System", "Consolidate Abacum functions" and their "-md" folders are repeat exports of the same pages.
- Date range of Manel's material: January 2022 to the March 2024 handover. Research reports from 2021 predate him.
- Out of scope, not indexed: the 1:1 log, PDP pages, career-level pages and feedback notes (Manel, 2026-11-09).
- Authorship comes only from database properties (Owner, Author, Designer, Created by). Plain pages carry no author. 218 unique pages name Manel Leiva as owner; 188 of them are design tickets.

**Two Manels.** A front-end engineer, Manel Escuer, owns pages too and appears in the Abax material as "Manel E." or "the other Manel". Filter on "Leiva". The DS retro line "Not having Manel E." and the July 2023 presentation's "Now the other Manel will explain" refer to him.

## Confidentiality

Internal reference only. The export contains customer names, employee names, a staging login in "Design library weekly" (25 November 2022), candidate databases with emails and evaluations, and a research-participant list with emails. None of that is copied here and none of it goes into external material. Live copy follows the usual rule: roles, not names.

## Folder map

| Top folder | Unique pages | What it is |
|---|---|---|
| `Design/Design` | ~1,900 | Design team hub: design tickets (756), UX debt database, customer research, Maker Days, rituals, hiring, onboarding, OKRs |
| `Design/Product` | ~1,000 | Product hub: squad docs (531, mostly a PM's Engine docs), design debt, archive |
| `Design/Engineering` | ~250 | Engineering chapters, Maker Days engineering initiatives, squads, courses |
| `Abax Design System` (+ `- md`, and copies under `Design/` and `Consolidate Abacum functions/`) | ~400 | Abax workspace: vision, metrics, roadmap, team setups, design library weekly, components, QA, Abacum Script |
| `Abax Frontend` | small | FE-side docs: `@abacum/design-tokens`, Storybook stories, adding components (engineer-authored) |
| `Notes` | 42 | **Manel's personal notes** (April 2022 to March 2024): research sessions, design-system notes, talk scripts |
| `Research` | 15 | Dataset creation flow and Data Transformation tests (2022), dimensions and mappings, syntax |
| Root pages | 6 | Dimensions problems, Design Solution Challenge (1:1 relationship), Engine H1 and H2 2023 plans, Product roles, Syntax UX opportunities, Consolidate Abacum functions, UX principles |

## Key databases

| Database | Rows | Manel's share | Use |
|---|---|---|---|
| Design tickets (`Design/Design`) | 756 | 188 owned, April 2023 to March 2024 | Weekly task log; the dated record of his Engine-period work |
| Squad docs (`Design/Product`) | 531 | 1 (Error messages framework, July 2023) | Engine PM's problem docs, plans, KPIs |
| Components (`Abax Design System - md`) | 163 | 2 (Button, FAB, shared with another designer) | Pre-Abax Figma library; another designer is credited on 128 |
| UX database (UX debt) | 153 | 15 authored | Dataset Manager and formula debt and ideas |
| Abax components (Roadmap) | 131 | 1 (File picker) | Abax 1.0 component roadmap with design and implementation cost |
| Maker Days initiatives (Product, Design) | 91 | 7 owned, 2 collaborator | See the Maker Days table below |
| Design collab backlog | 82 | 16 owned (tied highest with one other designer) | Design collab sessions he hosted |
| Sprint 1 tickets (Abax Vision 1.0) | 50 | 18 owned | Abax team sprint, autumn 2023 |
| Abacum functions | 37 | Built under his initiative | Inventory of formula functions and consistency |
| Insights repository, Research reports, Research projects | 33, 32, 106 | Research owned by the researchers | Pre-2023 research is mostly the researcher's |
| Notes (Manel) | 42 | All | Personal notes |

## Manel's material by topic

### Dataset Manager and integrations (Integrations / Data I/O squad, 2022)

| Page | Date | Location | What it shows |
|---|---|---|---|
| Data Transformation (+ 4 user tests, FP&A testing outcomes) | undated, 2022 | `Research/Data Transformation` | Prototype test of the Manage / Transform / Connect / Map panels (Figma "Data I/O / Exploration"). Notes in Catalan and Spanish. Participants appear to be the internal FP&A team (the outcomes page is titled FP&A). Findings: "Connect" and "Measure" unclear, "Select data type" read as "select dimension", hide vs show columns, bulk mapping upload, mapping depth, no save button |
| Dataset creation flow: Feedback - FP&A, Feedback - Tech | 2022 | `Research/Dataset creation flow` | Four internal FP&A reviewers; engineers' answers on the data model (date column mandatory as index, first 100 rows as sample, CSV and Excel only) |
| Dataset creation flow - Ulug / - Nerea | 27 Jul and 4 Aug 2022 | `Notes` | Manel's notes from two task-based sessions with customer users (tasks 0 to 4: spot column, create dataset, add a formula column, create dimensions, delete dataset). Both read the `IF ... THEN` wording backwards; Measure vs Dimension and Financial vs Custom type confused; one created dummy formulas until the dataset existed; one had to call support to delete a broken dataset |
| Integration Coffee Session | August 2022 | `Design/.../Customer research/Coffee Sessions` | Interview guide and sessions on customers' integration setup; framing: FP&A handles integrations, aim to cut FP&A time and raise customer autonomy |
| integration flow, Julie - Integrations upgrade, Auto-sync | April to November 2022 | `Notes` | Integration-selection flow notes, auto-sync questions |
| "Data I/O Q4 OKRs (Draft)" | 5 Oct 2022 | `Notes` | Squad OKR draft: customer autonomy coefficient on dimension actions in live orgs 0.44 to 0.9; FP&A Ops hours per live org 9h to 4.5h a month; mapping actions done in the UI 0% to 50%. Author not recorded |

### Dimensions and mappings (2022, then Engine 2023 to 2024)

| Page | Date | Location | What it shows |
|---|---|---|---|
| Dimensions problems | undated, no owner | root | Mental-model analysis (hierarchical mappings vs flat in users' minds), severity-ranked issues with evidence, opportunities by confidence level. Ownership unconfirmed |
| Mappings & dimensions workshops | 14 Oct 2022 | `Notes` | Insight summary: users want to model without thinking about dimensions; object-library idea |
| Meeting with Oriol | 2 Nov 2022 | `Notes` | Manel validating the new unmapped-items flow, dimensions table view and auto-sync with an FP&A colleague |
| Baha / Luisa - Dimensions & mappings | Sep and Nov 2022 | `Notes` | Manel's discovery questions to internal FP&A and research |
| Rename dimension items, communicate impact & manage concurrency | 5 Jan 2024, Done | Design tickets | Owner Manel. Problem, earlier squad framing (July 2023), Causal benchmark, ordering problem worked through, validation with the PMs (September 2023) |
| Manage dimensions items and levels | 5 Feb 2024 | Design tickets | Owner Manel. Customer cases plus interviews with four internal implementation and FP&A colleagues (6 to 8 Feb 2024) on adding, deleting and renaming levels |
| Prep handover | 18 Mar 2024 | Design tickets | Owner Manel. Marks "Finalise rename dimension items NEW FEATURE DONE"; lists what was open (edit hierarchies, add or delete levels, bulk dimension management) |
| Dimensions & mappings (Research) | 2021/22 | `Research` | Manel's hiring design challenge alongside other candidates' (his Figma "Notion - Tags" file); not product work |

### Modeling language and syntax (Engine, 2023 to 2024)

| Page | Date | Location | What it shows |
|---|---|---|---|
| Consolidate Abacum functions | 17 Jan 2024, 24 Q1 | root and `Consolidate Abacum functions` | Owner Manel. Problem list, 15 inconsistent functions with syntax, impact rationale, a December 2023 customer-call quote |
| Abacum functions (database) | | `Design/Abax Design System/Abacum Script` | 37 functions: domain, mandatory and optional params, syntax, consistent yes/no, forecast |
| Abacum Script (coding conventions) | January 2024 | `Abax Design System` | UPPERCASE function names, lowerCamelCase params, `[optional]`, parentheses style, adopt Excel or GSheets naming. Manel's ticket "Finish first iteration of Abacum Script" (5 Jan 2024) |
| Syntax UX opportunities | 2023/24 | root | Ten HMW opportunities scored with ICE; impact defined as adoption by current non-modelers |
| Improve syntax popover flow & testing; Syntax UX; Finalise syntax proposal & user test; Formula parameter preview; Standardise modeling function params | Nov 2023 to Jan 2024 | Design tickets | Owner Manel. Popover structure across object types, syntax input component, parameter preview, syntax helper benchmark and collab session |
| Variable library concept testing | Apr to May 2023 | Design tickets | Co-owned with the researcher: research structure agreed with Manel, customer interviews, synthesis with Manel and the PM |
| Proto: Future of syntax + Syntax proto | 7 to 13 Mar 2024 | Maker Days, `Notes` | Owner Manel. Vision prototype (readability, dot-triggered dimension, period and version filters, parameter preview, expert mode) and his demo script |
| Syntax, Syntax Research Results | Aug 2021 | Research reports | The researcher's study, before Manel joined |

### Abax, tokens and Maker Days

Maker Days ran about every nine weeks. Manel's initiatives in the Product and Design table:

| Cycle | Initiative | Role | What |
|---|---|---|---|
| V1, 17 to 23 Nov 2022 | Launch a design system MVP | Owner | Colour tokens on GitHub so designers could update product colours without FE; hardcoded colours replaced by FE. Targets only (for example 95% fewer colour inconsistencies) |
| V3, 9 to 16 Mar 2023 | Create the first DS component | Owner (1 designer, 2 to 3 FE) | Font and spacing tokens, Button rebuilt on tokens, Storybook docs. Manel made the tokens and migrated library components; FE replaced hardcoded values |
| V4, 25 to 31 May 2023 | Roll out Design system component changes | Owner (1 designer, 3 FE) | Specs for tabs, toggle buttons, inputs, selects, chips, dialogs; tokens added to library |
| V5, autumn 2023 | Abax Vision 1.0 team sprint | Sprint 1 tickets owner | Variants and properties nomenclature, component descriptions, apply tokens to library, font tokens, semantic colour tokens, excess-token clean-up; head of design on colour and table font tokens; FE on ESLint, Storybook, ways of working |
| V6, 9 to 15 Nov 2023 | DS: Component roadmap; DS: Spectrum color implementation; DS: Storybook template | Owner (head of design collaborator on two) | Abax 1.0 roadmap by priority and cost; new spectrum palette connected to functional tokens, styles migrated to variables; one Storybook template |
| V7, 18 to 24 Jan 2024 | DS: Colors tokens (and others); DL: Library cleanup | Owner; collaborator | Colour rollout for accessibility, unused-token and naming check; library clean-up led by another designer |
| V8, 7 to 13 Mar 2024 | Proto: Future of syntax | Owner | See syntax above |

Other Abax pages:

| Page | Date | Location | What it shows |
|---|---|---|---|
| Design systems | 26 Apr 2022 | `Notes` | Manel's first proposal: split libraries (tokens, core, icons, per-squad), export to FE, notes from DS practitioners |
| Design System MVP | 12 May 2022 | `Notes` | MVP description written by Manel; colour POC done with FE; pipeline: GitHub as token source of truth, GitHub Actions, Figma Tokens plugin JSON, token-transformer, Style Dictionary, Rollup, published as `@abacum/design-tokens` for the MUI theme |
| Design system questions - Lucas | 23 May 2022 | `Notes` | Interview with an outside DS practitioner before starting |
| Design library weekly | 15 Jul 2022 to 22 Mar 2024 | `Abax Design System` | About 57 dated meetings. Manel hosted 79 agenda items, the head of design 76. 15 Jul 2022: Manel's colour-token roadmap, actioned to get the head of design's approval and set up a design and engineering meeting. 30 Jun 2023: exploration vs implementation library proposal. 28 Jul 2023: issue-reporting categories, form-elements release plan under feature flags, slot components for dropdowns and dialogs. 17 Nov 2023: spectrum colours, semantic variables, library on variables |
| DS presentation | 7 Jul 2023 | `Notes` | Manel's script for the all-hands Abax introduction after the head of design: two weekly rituals, "around 250 tokens deployed and implemented", "more than 100 icons" |
| DS presentation prep | 2023 | `Abax Design System` | Storyline, Manel's and the head of design's notes on FE concerns |
| Vision 1.0, Team setups, Team and system needs, Metrics, Why a design system | 2023 | `Abax Design System` | Team docs, no author recorded |
| Maker days initiative Q42023 | 15 Nov 2023 | `Notes` | Manel's recap script: Abax roadmap, spectrum palette (brightness and saturation rebalanced, accessibility issues fixed, styles to variables) |
| Deploy tokens to design env | 29 Nov 2023 | `Notes` | Manel's own command log: bumped `@abacum/design-tokens` 0.0.76 to 0.0.81 on `design-tokens/new-color-spectrum`, updated Playwright snapshots |
| Abax tasks, Abax QA | late 2023 | `Abax Design System` | 10 of 13 tasks Manel's (Storybook template, first usage data point, select tickets); QA issues he reported |

### Team process

| Page | Date | Location | What it shows |
|---|---|---|---|
| Designers ❤️ Engineers | 12 Sep 2022 | `Notes` | Manel's talk script on designer and FE collaboration |
| STOA presentations | Apr to Jul 2022 | `Notes` | Titles only |
| Design rituals, Design roles & responsibilities, UX principles | 2023 | `Design/Design`, root | Team docs; author not recorded |
| Squads research | Nov 2023 to Apr 2024 | Design tickets | Researcher's weekly log with squad designers; Manel's dimension work (internal feedback, then heuristic evaluation; UserTesting trial) |

## Findings

### New claimable facts

Proposed register entries. Each needs Manel's confirmation where marked before it goes into [experience-facts.md](../experience-facts.md).

1. **Squad switch date.** The design ticket "Engine onboarding & tasks" is dated 30 January 2023. Fills the "squad-transfer dates unknown" gap. Class: artifact.
2. **Abacum tenure.** Handover ticket dated 18 March 2024. Consistent with the Figma index (January 2022 to April 2024). Class: artifact.
3. **The Abacum token pipeline started as Manel's MVP.** He wrote the MVP description (May 2022), presented the colour-token roadmap at the first design library weekly (15 July 2022) and owned the first Maker Days design-system initiative (November 2022). The pipeline itself (GitHub Actions, Style Dictionary, Rollup, npm package) was built by FE. This strengthens "brought the Abacum token-pipeline foundation into Remuner": the foundation was a pipeline whose design-side MVP he led. Class: artifact. Boundary: say "I proposed and led the design side; engineers built the pipeline".
4. **Sustained Maker Days ownership.** Owner of a design-system initiative in V1, V3, V4, V6 (three) and V7, plus the V8 syntax vision, November 2022 to March 2024. Class: artifact. Boundary: Maker Days goals were targets; no results recorded.
5. **All-hands presentation, dated.** 7 July 2023 (ticket "DS STOA presentation", 3 July). His script states around 250 tokens deployed and over 100 icons available. Supports the existing business-case presentation entry. Class: artifact (his contemporaneous internal statement). Boundary: "about 250 tokens" as said at the time; not a later count.
6. **Spectrum palette, a second palette rebuild before Remuner.** November 2023 to February 2024: broader palette with rebalanced brightness and saturation, accessibility issues fixed, colour styles migrated to Figma variables, tokens shipped through the repo. Manel owned it with the head of design; he bumped the tokens package himself (29 Nov 2023) and his PR #4112 (5 Feb 2024, "design tokens new colour spectrum") is on master. Class: artifact plus git. Useful as precedent for the Remuner HSL normalisation story. Boundary: no contrast figures recorded; head of design shared it.
7. **Governance practices, dated.** Issue-reporting categories, form-elements release under feature flags and slot components (dropdowns, dialog) all presented by Manel on 28 July 2023; exploration vs implementation library proposal on 30 June 2023. Dates the July 2026 CV-base claims and the Select slot example. Class: artifact.
8. **Design library weekly, full span.** 15 July 2022 to 22 March 2024, with Manel hosting about as many agenda items as the head of design (79 vs 76). Class: artifact. Boundary: the register says Manel "introduced" a weekly design-system meeting; the log shows the weekly existed from his first months, so don't claim he founded it unless Manel confirms.
9. **Dataset Manager customer sessions.** Two task-based sessions with customer users on 27 July and 4 August 2022, notes in his own Notes, plus an internal FP&A prototype test of the Transform / Connect / Map panels. Findings he can cite: users read `IF ... THEN` backwards, confused Measure with Dimension, couldn't delete a broken dataset without support. Class: artifact. Confirm with Manel that he ran the sessions.
10. **Dataset Manager success metric existed.** The Data I/O Q4 2022 OKR draft defined customer autonomy as the share of successful dimension actions customers completed without FP&A, with a 0.44 baseline and 0.9 target, and an FP&A Ops target of 9h to 4.5h per live org a month. Class: artifact, draft. Boundary: author not recorded and no result exists. Externally, describe the metric, not the numbers; never imply the target was met.
11. **Dimension rename shipped.** Manel's handover marks "rename dimension items" as a finished new feature (March 2024), and he gathered input from four internal implementation and FP&A colleagues for the levels follow-up. Ties to the Figma "Dimension dependencies" pages. Class: artifact (his own status mark). Separately, webapp commit #2304 (2 Dec 2022) added a `confirmed_dimension_impact` field, which suggests an impact confirmation step shipped in 2022 (inference; check before claiming it is the "Accept impact" design).
12. **Function consolidation authorship.** Manel owned "Consolidate Abacum functions" (Q1 2024), the 37-function audit and the Abacum Script conventions. Supports the live case's audit claim. Class: artifact.

### Contradictions with repo files

Status 2026-11-09: 1 to 4 corrected in design-systems-notes.md; 5 resolved by Manel (shipped); 8 recorded as a register boundary; 6 and 7 stay as notes.

1. **[context/design-systems-notes.md](../../context/design-systems-notes.md), "Two sprint formats were evaluated ... Maker Days used the latter".** Not a contradiction (revised 2026-11-09 after reading Vision 1.0 in full). The two sprint durations are in Vision 1.0 (August to September 2023) for the Abax team sprint, which ran in a Maker Days week in October 2023 (retro 17 to 20 October; Abax Button, Select, Tab, Tooltip and Chip enter the lint rule 10 to 11 October). "Team setups" is a separate question, the ongoing team structure: permanent DS squad preferred but too expensive, distributed core team (1 FE + 1 designer) chosen, Maker Days alone, DS sprints and a DS weekday marked not recommended as the standing setup.
2. **Same file, "the full token system shipped during the week".** The token system predates that week: colour-token repo and MVP in November 2022, font and spacing tokens with the MUI Button on tokens in March 2023, styles to Figma variables in November 2023. What the October 2023 week produced is the Abax workflow (nomenclature, descriptions, ways of working, Storybook) and the first Abax components, Button among them. Say "a year of token groundwork, then the first Abax components in one Maker Days week".
3. **Same file, "weekly cadence ran from at least July 2023 to March 2024".** The log runs from 15 July 2022.
4. **Same file, Maker Days as a "quarterly initiative".** The DS retro says Maker Days happened every nine weeks and that contribution ran on extra hours with little product support. Minor; say "every nine weeks" or "regular".
5. **Live modeling-syntax case: "The resulting language moved all parameters inside parentheses ... standardised function naming".** In Notion the consolidation is a Q1 2024 proposal, listed in the March 2024 handover together with parameter preview and the syntax helper. At the webapp's last local commit (3 April 2024), formula metadata still uses `DISTRIBUTE_MONTHLY` and `COUNT_STARTDATE`, not the proposed `DISTRIBUTEMONTHLY`. So the standardisation was probably not live when Manel left (the mocks may be stale, and the grammar sits in the back end). Highest-risk item: confirm with Manel, then reword the case to "proposed and documented" unless he knows it shipped.
6. **Register, Dataset Manager "three test participants".** Notion shows two customer sessions in July and August 2022 plus internal FP&A testing; no round of three is visible. Not a contradiction, but the count is unverified here. Ask Manel which round the three were.
7. **SQL nuance.** The researcher's August 2021 syntax study found SQL "the easiest to read and use because it is explicit". The Dataset Manager account says users could write the logic in Excel but not in SQL. They are different studies (reading vs writing, 2021 vs 2022), but expect the question if an interviewer knows the earlier work. One customer in July 2022 also said he knew Python and SQL.
8. **Component-library scope.** The pre-Abax Figma component database credits another designer on 128 of 163 components and Manel on two. The register's "worked on ... component library" is fine; don't let it read as "designed the component library". His library work is tokens, nomenclature, descriptions, clean-up, the roadmap and specific components (Button, File picker, Avatar, Chip, ChecklistSelect, Select and Menu).

### Gaps and questions for Manel

Answered by Manel 2026-11-09 and recorded in [experience-facts.md](../experience-facts.md):

- Function consolidation and parameter preview shipped after the handover. Contradiction 5 is resolved: the live case stands; the webapp mocks predate the release.
- Manel ran the 2022 Dataset Manager customer sessions and agreed the method with the researcher.
- Manel wrote "Dimensions problems" and "Design Solution Challenge · Breaking 1:1 relationship".
- Manel started the design library weekly (fact 8).
- Departure: company-initiated; Abacum reduced the team to extend its runway.

- The three test participants were Abacum's internal FP&A specialists; customer sessions came second (Manel, 2026-11-09).
- Squads were Actuals, Engine, Reporting, Futures and Collaboration.

Still open:

- Who configured datasets before Dataset Manager: the register says the Integrations engineers; the August 2022 coffee session says FP&A Support. Ask Manel before changing deck slide 2.
- No adoption numbers anywhere in the export: the 47% codebase share and the Figma health-score script do not appear. The Metrics page says tracking was manual "for the time being". The register's reconstructed figures stay recollection.

### Not read

- Full text of: Abax Design System overview (2,579 words), Roadmap, Component properties naming convention, Abax Frontend pages, Engine H1 and H2 2023 plans (searched for Manel only), Design Solution Challenge (first part read), Error messages framework, Syntax usability evaluation (April 2023), the Engine PM's squad docs, UX debt rows.
- PDFs, spreadsheets, images, videos.
- The hiring and candidate databases (excluded on purpose).

## Re-running

Scripts are in [scripts/notion-index/](../../scripts/notion-index/). Run with `python3 -I`, keeping outputs out of the export folder:

```
python3 -I scripts/notion-index/inventory.py "$HOME/Desktop/Abacum (Notion)" /tmp/inv.json
python3 -I scripts/notion-index/catalog.py /tmp/inv.json /tmp/pages_dedup.json evidence/notion/catalog.tsv
INV=/tmp/pages_dedup.json CAP=4000 python3 -I scripts/notion-index/totext.py "$HOME/Desktop/Abacum (Notion)" '^Page title regex'
```

`inventory.py` keeps the first 200 characters of each page in its JSON, so that file stays out of the repo.
