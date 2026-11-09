# Abacum | Dataset manager - Exploration (live file)

File: [SX7z0Cp4IMIw8RmNyrsI5G](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G). 23 pages, about 3,800 top-level nodes. The working exploration file for the Dataset Manager, January 2023 to February 2024. Full listing: [catalog/abacum-dataset-manager-exploration--SX7z0C.md](catalog/abacum-dataset-manager-exploration--SX7z0C.md). Found and indexed 2026-11-09.

**How it relates to the backup.** [abacum-dataset-manager-exploration.md](abacum-dataset-manager-exploration.md) ("Backup 27.3.23", `rg5IG7…`) is a snapshot taken in March 2023. Compared frame by frame on 2026-11-09:
- **Only in the backup:** all 2022 pages (2201 Manage, 2202 Transform and Upload, 2203–2212, GSheet plugin, Auto-sync and its prototype). Use the backup for the 2022 story.
- **Shared pages (2301–2303):** same content. The only difference is that note and step labels were swapped to newer label components. Exception: "2303 -> Dataset loads -> months" was trimmed in the live file (37 nodes vs 182), so the backup has the fuller version. The live Graveyard is empty.
- **Only in the live file:** 11 pages from April 2023 to February 2024 (below). This is the formula-box, manual-adjustments and dependencies work.

Ownership: Manel's (confirmed 2026-11-09 for the Dataset Manager files), with three limits:
- Another designer, Carol, has her own sections on two pages ("Carol - Exploration", "Carol - suggestions summary", "Carol / For implementation"). Don't claim those.
- "Collab" is a review page: the head of design (Julian) and another designer (Joel) critique Manel's dependency designs.
- "? -> Brainstorm" lists four participants (Luisa, Manel, Julian, Ignasi).

## Pages only in this file

| Page | What it covers | Notable content | Link |
|---|---|---|---|
| Collab | Review page for the dependencies toolbar and detail view | Critiques from the head of design and another designer ("Separate dataset vs version specific information?", "Are the icons necessary?") | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=6220-17780) |
| 2402 -> Details/Dependencies | 657 nodes; dataset and column details plus incoming and outgoing dependencies | 19 sections: user insights, relationships taxonomy, Approach 1 vs 2, "1 dialog" vs "separate dialogs", 3 options for the dependencies summary, "details conundrum" v1 and v2, prototypes; user story "see where my text columns are used, so I can adjust syntax" | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=5526-19040) |
| 2312 -> Transformation QA | QA of the shipped formula box against real transformations (screenshots from 1 Dec 2023) | Typing layer, transformation and dataset manager QA; short-term vs long-term fixes; syntax highlighting | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=5436-26319) |
| 2309 -> Transformation improvements | **The framing for the formula box.** Status quo, five user problems written on the canvas, inspiration, toolbar, alternative layouts, formula help, modal UI, formula library, formula structure, syntax highlighting, saving and feedback, autocomplete flow | Problems: "Users have to learn unintuitive and inconsistent nomenclature", "Users can't intuitively write formulas", "can't easily work with long formulas", "can't easily read and understand syntax", "On small screens, users can't see the dataset preview" | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4386-192873) |
| 2308 -> Manual adjustments | 1,120 nodes, the largest page; editing dataset rows | User scenarios as sections (create a commission column, remove start-date strings, adjust an FX rate, edit a row); "How to access the adjusted data?", version control, critiques; Carol's sections | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4242-30384) |
| 2308 -> Rename column, usage, UI improvements | UI cleanup and dataset/column details | Rule on canvas: "The chip represents a mapping, not a column type!"; "Re-use the same vocabulary!" | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4220-17205) |
| 2306 -> DSM concepts | Formula preview with sources and "used by" | | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=3949-172674) |
| 2306 -> Easier bulk month selection | Month picker: status quo, Round 1, Round 2, proposal, flows, prototype, benchmark (MUI, Ant) | Carol's variants and "For implementation" section | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=3936-172184) |
| 2304 -> Transformation improvements | Earlier quick fixes: identify columns created by transformations, errors in the list | "Should we right-align numbers like in finance tables?" | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4478-152762) |
| 2304 -> Update, download, delete | Update dialog with month presets; rules for when Sync vs File upload shows | | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=3457-143697) |
| ? -> Brainstorm | Research follow-up workshop: short vs long term, HMW notes ("HMW allow users to know what actions are available?"), use cases | Participants listed on the board | [open](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4213-17153) |

## Image sources

| Use | Node | Link |
|---|---|---|
| The five user problems behind the formula box | 2309 page, Status quo | [4386:192874](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4386-192874) |
| Formula structure and help | Formula structure / Formula help | [4453:139939](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4453-139939), [4400:104620](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4400-104620) |
| QA against real transformations | Example transformations | [5436:26320](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=5436-26320) |
| Dependencies: user insights and options | User insights / 3 options for dependencies summary | [6043:16227](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=6043-16227), [6043:17089](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=6043-17089) |
| Manual adjustment scenario | Create "Commision" column | [4627:7910](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4627-7910) |
| Research follow-up workshop | ? -> Brainstorm | [4213:17153](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4213-17153) |
