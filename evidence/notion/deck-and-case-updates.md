# Deck and live-case updates from the Notion export

Backlog of edits to the three Abacum case decks and their live cases, from the Notion export ([README.md](README.md)). Companion to the Figma backlog, [../figma/deck-and-case-updates.md](../figma/deck-and-case-updates.md). Every item cites the Notion page; claims are recorded in [../experience-facts.md](../experience-facts.md) (Abacum section, 2026-11-09). **Status 2026-11-09:** A to C and the deck items applied to all three deck sources. Figma updated for on-slide text in "Dataset manager" (slide 5 footers, slide 10 Next time) and "Abacum DS" v2 (squad names, proof body, sync card and footer, outcome stat). Not in Figma yet: speaker notes (paste by hand), the Design Systems backup B3 timeline (no slide built), and the Modeling Syntax deck (no Figma deck exists). Live cases not checked. Manel confirmed: the first test round was internal FP&A; squads were Actuals, Engine, Reporting, Futures and Collaboration.

Decks: [Dataset Manager](../../interviews/decks/case-deck-dataset-manager.md), [Modeling Syntax](../../interviews/decks/case-deck-modeling-syntax.md), [Design Systems at Abacum](../../interviews/decks/case-deck-design-systems-abacum.md).

## Resolve first (risk before the next presentation)

### A. Dataset Manager: were the "three customers" customers?

- **Deck now:** slide 5 footer "Three customers, real configuration tasks on the early flows"; Figma 7 notes "The most experienced user led his company's FP&A team and had used Abacum for over a year". [context/portfolio.md](../../context/portfolio.md) names the participants as Maria, Eduardo, Guillermo and Oriol.
- **Notion:** those four names appear on "Feedback - FP&A" (`Research/Dataset creation flow`) and "FP&A testing outcomes" (`Research/Data Transformation`), Abacum's internal FP&A team. Oriol shows up elsewhere as the FP&A voice ("FP&A (Oriol?) - Weekly", "Bring FP&A challenges (Oriol)") and in 2024 owns Productboard work. "Led his company's FP&A team and used Abacum for over a year" fits the head of Abacum's own FP&A team, which configured datasets for customers.
- **Customer sessions that do exist:** two task-based sessions with customer users, 27 July and 4 August 2022 (Manel's notes "Dataset creation flow - Ulug / - Nerea").
- **Ask Manel:** were the three internal FP&A specialists? If so, the finding gets stronger, not weaker: the people who configured datasets for customers every day hit the same language problem. Proposed wording: "I tested the early flows with our FP&A specialists, who set up datasets for customers every day, then with customer users." Fix the deck footer, Figma 5 to 7 notes, the Q&A "three sessions" answer and the portfolio.md participant line together.

### B. Modeling Syntax: "a problem nobody had ticketed"

- **Deck now:** lead framing "I found a problem nobody had ticketed"; slide 3 notes "No ticket; it showed up in support calls".
- **Notion:** "Improve Syntax Usability" was a named Engine initiative by March 2023 ("Top Issues on Engine", with affected customers per issue). The April 2023 modeling-frustrations survey (co-owned with the researcher, 15 responses) ranked "actuals and version syntax are different" fifth of seven at 27%.
- **What was Manel's:** going below the usability layer to the functions themselves: the 37-function audit, 15 inconsistent functions, the benchmark, the grammar rules (owner of "Consolidate Abacum functions", January 2024).
- **Proposed lead framing:** "Syntax usability was a known problem. I traced it to the functions themselves and made the case to fix the grammar before adding more UI on top." Slide 3 notes: drop "No ticket".

### C. Design Systems at Abacum: three wrong details

- **"Quarterly"** (slide 4 notes, Figma 11): Maker Days ran about every nine weeks (DS retro, "Team and system needs"). Say "Abacum's regular Maker Days, every nine weeks".
- **"Over eight months" / "8+ months"** (slide 8, slide 12 stats, Figma 16, Figma 30): the design library weekly ran from 15 July 2022 to 22 March 2024, about 20 months, and Manel started it. Say "every week for almost two years".
- **"Tokens and the first Abax Button reached production in that one week"** (slide 5, Figma 12): the tokens were already in production (repo since November 2022, font and spacing tokens March 2023). The October 2023 week produced the Abax workflow and the first Abax components. Say "With the tokens already in production, the first Abax components shipped in one Maker Days week."
- **Check:** slide 2 squad names (Integrations, Engine, Reporting, Collaboration, Admin). In 2023 to 2024 Notion uses Actuals, Engine, Reporting, Planning/Futures; earlier Data I/O, Collab, Insights. Confirm which five.

## Dataset Manager deck

- **Slide 2 (Context), add concrete pain:** "Integration Coffee Session" (August 2022) lists who did the work: FP&A Support created customers' connections and datasets from the back end, customers followed step-by-step Notion instructions to add an integration, customers double-checked numbers in Excel, and FP&A checked the back office to see whether data had synced. One line on the slide: "Customers couldn't create a connection or a dataset themselves. Our FP&A team did it in the back office."
- **Slide 5 (Testing), sharper findings** (Manel's session notes; Data Transformation tests):
  - Both customer users read the transform syntax `IF ... THEN` backwards (language finding, fits the Excel point).
  - "Select data type" was read as "select a dimension" by every tester; "Measure" was not understood ("Connect is what confuses me the most").
  - Mapping one value at a time didn't scale: "When you have a mapping with a hundred lines you don't want to do it line by line."
  - A customer: she wished Abacum were "smarter" so she didn't have to map everything.
  - A customer couldn't delete a broken dataset and had to call support (fits the guardrails slide).
  Use quotes without names.
- **Slide 8 (Guardrails), stronger setup:** "Dimensions problems" (Manel's) ranks "renaming dimensions ends up deleting formulas in modules" as a high-severity issue, with evidence. Use it as the problem line above the dependencies dialog.
- **Slide 10 (Outcome), "Next time":** the squad did define a metric in late 2022: a customer autonomy coefficient, the share of successful dimension actions customers completed without FP&A (Data I/O Q4 2022 OKR draft). The honest gap is that no after-number reached Manel. Option: "Next time: the squad had defined an autonomy metric; I'd make sure we reported it after release." Keep the 0.44 baseline and the targets off the slide (register boundary).
- **Backup, the follow-up:** dimension rename with impact shipped in Engine (January 2024), designed by Manel, after interviews with four internal implementation and FP&A colleagues. The ordering problem worked through in that ticket (sorting cities breaks the country order) is a good whiteboard example.

## Modeling Syntax deck

- **Cover:** "Abacum, 2023" becomes "Abacum, 2023 to 2024". The work ran November 2023 (syntax popover) to March 2024 (handover); the benchmark is dated 8 January 2024.
- **Slide 3 (Problem), real examples** from the function audit (37 functions, 15 inconsistent):
  - `JOIN other_dataset_column FROM OTHER_DATASET ON dataset_column = other_dataset_column`
  - `TEXTSPLIT ( text_column, delimiter, position_to_keep )`
  - `ALLOCATE Variable_A BY Variable_B`
  - `DISTRIBUTE_MONTHLY (dimension, start, end, measure) FROM DATASET`
  - `FX measure FROM base TO quote AT date WITH criteria`
  Visual: two or three of these side by side with "parameters outside / inside / clause style" annotated.
- **Slide 4 (Making the case), fills the [NEEDS YOUR STORY]:** syntax wasn't users' top complaint (fifth of seven in the April 2023 survey), so the case had to rest on cost and on what it unblocked. The consolidation page argues: shorter learning curve and fewer documentation look-ups; easier reading of nested formulas; one parameter structure so filters can combine, which "unblocks eventually translating them into UI (e.g. filter popover, parameter preview)"; simpler grammar for engineering. The squad's risk review rated the consolidation "no usability risk" and syntax filters "high risk", so the low-risk foundation went first. Confirm with Manel that this was his argument before using it.
- **Slide 5 (Investigation), now sourced:**

  | | Excel | GSheets | Pigment | Causal | Abacum |
  |---|---|---|---|---|---|
  | Case | Upper | Upper | Upper | Lower | Upper |
  | Parameters | Inside () | Inside () | Inside () | Inside () | **Outside** |
  | Word separator | None, "." for sub-functions | Mostly none, "." | Mostly none | Mixed | **Mixed "_"** |

  Customer call (13 December 2023): got used to the formulas "after spending like several months with your implementation team", and asked for the experience to "look more like excel". No name.
- **Slide 6 (Decision):** add "." for sub-functions and the JOIN redefinition (dataset, its column, your column) as concrete rules; Abacum Script conventions: UPPERCASE names, lowerCamelCase parameters, `[optional]` in brackets, Excel or GSheets names and parameters where a function exists there.
- **Slide 7 (Engineering):** two working sessions with one back-end engineer (15 and 29 January 2024); the work was broken into 13 tickets for iteration 1 and 15 for iteration 2 (iteration 2 moved FROM sources into parameters).
- **Slide 9 (Outcome):** parameter preview shipped after Manel's handover (confirmed 2026-11-09). Optional "what came next" line: the March 2024 "Future of syntax" prototype (dot-triggered dimension, period and version filters, parameter preview, an expert mode for keyboard users), a vision piece, not shipped.
- **Q&A, "How did you prioritise?":** "Syntax UX opportunities" scored ten problems with ICE, impact defined as adoption by finance users who didn't model yet. Highest: understanding which variables a formula uses (150) and understanding and fixing syntax errors (120).

## Design Systems at Abacum deck

- **New slide or backup, "A year of groundwork before Abax"** (timeline, all Manel-owned unless noted):
  - Jul 2022: colour-token roadmap at the first design library weekly
  - Nov 2022: colour-token MVP, tokens on GitHub so designers could change product colours without FE (FE built the pipeline)
  - Mar 2023: font and spacing tokens, Button on tokens, font styles cut from 23 to 11, designers able to change four token groups instead of one
  - Jul 2023: all-hands, about 250 tokens and 100+ icons
  - Oct 2023: Abax team sprint, first Abax components
  - Nov 2023: spectrum palette, styles to variables (with the head of design)
  - Jan 2024: colour rollout for accessibility
  This answers "how did a system nobody asked for get time" with dates, and makes slide 5 accurate.
- **Slide 3 (Business case):** date the all-hands (7 July 2023) and use Manel's line from the script: Abax "is not just a library of components, it's a cross-discipline team". Numbers at the time: about 250 tokens deployed, more than 100 icons.
- **Slide 4 (Investment choice), richer decision:** the standing team structure was its own decision ("Team setups"): a permanent DS squad was preferred but too expensive, so a distributed core team (one FE, one designer) with work spread across squads was chosen. The DS retro named the costs: little support outside design and engineering, last-minute planning, contribution on extra hours, Maker Days too infrequent for steady progress. Good Q&A material for "what was hard".
- **Slide 8 (Rollout):** date the governance cards: issue-report categories, feature-flag release plan and slot components were presented on 28 July 2023; the exploration vs implementation libraries proposal on 30 June 2023.
- **Slide 9 (Measurement):** the Metrics page lists the planned measures: MUI vs Abax component counts, components migrated, new Abax components, global vs used tokens, component instances, and disabled lint rules (`eslint-disable-next-line abacum-io/prefer-abax-component`). Tracking was manual "for the time being". Consistent with the slide; adds the lint-disable count as a measure.
- **Slide 12 (Outcome):** replace "8+ months of weekly library sync" with "a weekly library sync for almost two years". Add "font styles cut from 23 to 11" as a concrete library result if a fourth stat is needed.
- **Slide 13 (Remuner bridge):** the spectrum palette (rebalanced brightness and saturation, accessibility fixes, styles to variables, Manel's PR #4112) is the precedent for the Remuner HSL normalisation.
- **Q&A, "What would you do differently?":** Vision 1.0 itself flagged "focus shift from infrastructure to production": text input, select, autocomplete and menu were still undocumented when the team had to stop building token infrastructure and start shipping components.

## Live cases

- **/cases/dataset-manager:** same participant question as A. Check the live copy for "customers" in the testing section once Manel answers.
- **/cases/modeling-syntax:** check for "nobody had ticketed" or "no ticket" wording (B). The benchmark table and the customer-call fragments can go into the research section.
- **/cases/design-systems:** check for "quarterly", "eight months" and "one week" wording (C). The groundwork timeline fits as a short "before Abax" paragraph.

Not checked: the live case pages themselves; this backlog is built from the deck sources and [context/portfolio.md](../../context/portfolio.md).
