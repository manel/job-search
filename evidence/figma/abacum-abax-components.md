# Abacum | 💠 Abax Components

File: [7Ast9N5HDQLE1l9kDcqoo3](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3). 55 pages. Counted on 2026-11-09: 239 component sets with 2,464 variants and 394 standalone components. The Graveyard holds 52 of those sets (643 variants), so the live library is about 187 sets and 1,820 variants, plus 286 icons. Full listing: [catalog/abacum-abax-components--7Ast9N.md](catalog/abacum-abax-components--7Ast9N.md). DS story and ownership: [context/design-systems-notes.md](../../context/design-systems-notes.md), [context/portfolio.md](../../context/portfolio.md).

Indexed 2026-11-09 from a full extraction. **Ownership is shared.** Abax was a team library. Per the design-systems notes, Manel owned token architecture, spacing and border tokens, color token cleanup, the Figma variable structure and the library cleanup in Maker Days sprint 1. The head of design owned the color spectrum and font tokens. Other designers owned specific components (cells, colorSelect, search input, menu). Don't claim the whole library.

Page groups: Tokens, Basics, Forms, Communication, Items, Containers, Data, Other. Emoji-marked props (`✏️ text`, `🖼️ icon`, `🔄 content`) signal editable slots. `⛔️` marks deprecated components, `🧪` experiments, `🧹` pages being cleaned up.

## Components by page

| Page | Sets / variants | What's there | Link |
|---|---|---|---|
| 📚 Components overview | | Overview layout with to-dos ("Matrix may work better here") | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=738-10387) |
| 0.1 Hover, Elevation, Spacing 🪦 | 2 / 13 | Indentation, divider margins | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=8456-54576) |
| Icons | 286 icons, 184 with search keywords | Finance-specific icons (freeze, forecast, budget, formula, operators, decimals) | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=8169-52511) |
| Avatars, Badge | 6 / 83 | Integration logos (37), people, initials | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=15937-21334) |
| Button | 2 / 112 | button (100 variants), splitButton; description gives copy rules ("Replace with action as specific as possible: Save, Replace, Overwrite") | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=8324-53357) |
| IconButton, FAB, ToggleButton, Switch | 10 / 148 | Checkbox, radio, expander and dropdown buttons; experimental switch | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16725-146876) |
| Tabs, Breadcrumb | 3 / 18 | | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16632-154392) |
| Chip | 10 / 231 | Mapping, color, status and workflow chips; a variable-chip experiment; old and new chip side by side | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=10922-92270) |
| Forms: formBuildingBlocks, input, select, filePicker, monthPicker, colorPicker | 18 / 343 | `inputSyntax` (44 variants, multi-line with line counter) for formulas; select, multiSelect, autocomplete; month picker with presets and selection counter | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16739-4584) |
| Communication: Tooltip, Alert, Snackbar, EmptyState, Helper, FormulaHelper | 10 / 38 | FormulaHelper shows function syntax and parameters; real error copy ("Unable to get data inside the first row of this table...") | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16339-1489) |
| Items: basic, action, select, stepper, form, event, comment | 41 / 142 | `event` page has 23 sets covering every notification and activity type (invites by role, mentions, dataset created/updated/deleted, mapping); stepper `scriptItem` used for transformation steps; contextual menus for spaces, models, versions, datasets | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16651-132084) |
| Containers: Menu, Toolbar, Dialog, Topbar, Navbar | 27 / 122 | Menu with formula functions and syntax chips; formulaPopover; module builder toolbar; activity panel; comment dialog | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16712-12287) |
| Table | 17 / 293 | Cell types: column header, number (40), row header, text (48), date, chip, avatar, formula, action; variance backgrounds; selection; skeleton | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=1745-5821) |
| Chart 🧹 | 17 / 147 | Bars, combi, lines, area, waterfall, pie | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=8458-56881) |
| Space 🧹 | 16 / 52 | Document blocks for Spaces: headings, text, lists, tasks, callouts, KPI card (WIP), file, embed, table | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=2124-40) |
| 5.2 Documentation | 1 / 4 | Spec-sizing and label helpers used for component docs | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=10782-132447) |
| 5.5 Screenshots | 16 nodes | | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=11411-114679) |
| 🧰 Helpers | 2 / 47 | Component tracker, non-existing variant, placeholder, aspect-ratio spacers | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=12515-162449) |
| Graveyard | 52 / 643 | Deprecated old button (96 variants), old tabs, old chips, old cells (syntax, variable, mapping), dataset cards per integration | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=12675-214010) |
| Template, Thumbnail | | | [open](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16235-55229) |

## Image sources

| Use | Node | Link |
|---|---|---|
| Deprecation in practice: old vs new | Graveyard | [12675:214010](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=12675-214010) |
| Formula input as a DS component | input page | [16739:4584](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16739-4584) |
| Table cell system | Table page | [1745:5821](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=1745-5821) |
| Notification and activity model | event page | [16651:132084](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=16651-132084) |
| Component tracker | 🧰 Helpers | [12515:162449](https://www.figma.com/design/7Ast9N5HDQLE1l9kDcqoo3/?node-id=12515-162449) |
