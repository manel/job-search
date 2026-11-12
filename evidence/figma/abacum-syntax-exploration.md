# Abacum | Syntax - Exploration (current)

File: [VP0lJgP7n6tN4cFRMcZZIG](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG). 7 pages, about 630 top-level nodes. The later modeling-language explorations, November 2023 to April 2024: a team syntax workshop, the formula popover, parameter preview, filters, and a prototype of the "future of syntax". Full listing: [catalog/abacum-syntax-exploration-current--VP0lJg.md](catalog/abacum-syntax-exploration-current--VP0lJg.md). Handoffs: [abacum-syntax-implementation.md](abacum-syntax-implementation.md). Case source: [decks/case-deck-modeling-syntax.md](../../decks/case-deck-modeling-syntax.md).

Indexed 2026-11-09 from a full extraction. Ownership: assumed Manel's, with one limit. The "Syntax workshop" was a team session with four named columns (Mon, Carol, Julian, Manel), so its ideas are shared. Who ran it isn't recorded; Manel recalls the workshops as shared (2026-11-09). Present their ideas as team output and claim only what Manel took forward. Critiques on "Formula popover v2" come from the head of design and a designer (Víctor). The earlier syntax explorations (2022–early 2023) aren't in this file, which says "current"; they may be in an older file.

## Pages

| Page | What it covers | Notable content | Link |
|---|---|---|---|
| 2404 -> Objects preview | Help popover per object type: datasets, measures, variables, dimensions, operators | | [open](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=516-99773) |
| 2404 -> Formula params preview | Showing a function's full structure while typing and highlighting the next parameter | Spec: the selected parameter becomes a chip and focus jumps to the next one; the last parameter closes the parenthesis automatically. User story included | [open](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=514-72689) |
| 2403 -> Filters | Filtering variables by dimension, time and version in formulas | Every operator variant written out (IS, CONTAINS, IN, STARTSWITH and negations) to choose a consistent syntax; user stories for version filters, readability and concatenated filters | [open](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=387-47838) |
| 2403 -> MD Proto: Future of Syntax | 142 nodes, 13 components; a prototype of the next formula editor: autocomplete ranking, object chips, dataset and dimension navigation, filters on variables | Autocomplete ranking questions on the canvas (matching letter first, grouping, "Reddit ranking formula"); hypothesis "I want to start from the dataset -> measure -> function" | [open](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=252-22695) |
| 2312 -> ESC / Enter behaviour | Keyboard behaviour in the module builder | | [open](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=121-46034) |
| 2312 -> Formula popover v2 | 125 nodes; help popover for every function (DATEDIFF, DISTRIBUTE_MONTHLY, CUMSUM, COUNTUNIQUE, RAMP, SUMACTIVE, FX, IF, JOIN), tested at three screen sizes | Critiques from the head of design marked done (✅); open questions on boolean parameters and overflow | [open](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=73-1911) |
| 👯‍♀️ 2311 -> Syntax workshop | 306 nodes; team workshop: context, content and UI of syntax, parameter preview (short vs long term), interaction, building blocks, benchmark | HMW questions ("HMW guide the user to successfully write the syntax?"); one column per participant; a recorded decision that previews must work with autocomplete and in Spaces | [open](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=0-1) |

## Image sources

| Use | Node | Link |
|---|---|---|
| Workshop framing and HMWs | CONTEXT / INTRO | [1:1223](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=1-1223) |
| Short-term vs long-term parameter preview | Short-term / Long-term | [62:3684](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=62-3684), [62:3773](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=62-3773) |
| Benchmark | Benchmark | [57:3043](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=57-3043) |
| Function help popover | Formula popover v2 page | [73:1911](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=73-1911) |
| Filter syntax options | Exploration (filters) | [509:71390](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=509-71390) |
| Future-of-syntax prototype | MD Proto page | [252:22695](https://www.figma.com/design/VP0lJgP7n6tN4cFRMcZZIG/?node-id=252-22695) |
