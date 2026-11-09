# Abacum | Abax Core

File: [UueAtXpFYzKECtUnK18a8B](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B). 10 pages (6 with content), 532 top-level nodes. The token foundations of Abax: color system, typography, spacing, naming convention, and a January 2024 token audit. Full listing: [catalog/abacum-abax-core--UueAtX.md](catalog/abacum-abax-core--UueAtX.md). Components: [abacum-abax-components.md](abacum-abax-components.md). Explorations: [abacum-abax-core-exploration.md](abacum-abax-core-exploration.md).

Indexed 2026-11-09 from a full extraction, including the file's variables and styles. **Ownership is shared**, as with Abax Components. Per [context/design-systems-notes.md](../../context/design-systems-notes.md), Manel owned token architecture, spacing and border tokens, color-token cleanup and the Figma variable structure. The head of design (Julian) owned the color spectrum and font tokens. The token audit page is a written debate between the two.

## Variables and styles (counted 2026-11-09)

- **Variables:** two collections. `_core`: 139 primitives, `spectrum/[hue]/[50–900]`. `product`: 193 semantic tokens, `color/text|icon|border|bg/...`, all aliasing the spectrum. One mode each, no dark mode.
- **Styles:** 247 paint styles and 24 text styles. Text roles: `typography/ui/*` (title, header, section header, default, default active, label, action), `typography/formatting/*` (page heading, h1–h3, body), `typography/syntax/default`, and `typography/table/*`.

## Pages

| Page | What it covers | Notable content | Link |
|---|---|---|---|
| Color system | Semantic token tables per group: general text, background, border, icon, formatting, syntax, charts, tables, cells, variance, form elements; spectrum and chart palette | Each token row shows name, description, alias (`{_spectrum.gray.900}`) and raw value | [open](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=3608-20533) |
| Typography | Font documentation: UI, formatting (Spaces only), syntax, tables | Open task: "agree on space body 16 vs 14, table headers" | [open](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4168-23345) |
| Spacing | Spacing tokens: inset, stack, inline, each XS to 3XL | "Original" vs "Tokenized" comparison; definitions ("Stack: spacing between elements stacked") | [open](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4168-23346) |
| Border | Empty | | [open](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4168-23347) |
| ❯ Naming convention | Token name anatomy: category, concept, property, prominence, variant, state, scale, mode; worked for color, typography and spacing | "Purpose of token: color for semantic colors and spectrum for source colors" | [open](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=3608-22035) |
| 2401 Token audit | 418 nodes. Status quo, missing or mismatched tokens, analysis and proposal per component (buttons, links, inputs, selects, checkboxes, switches, cells) | **A written design debate.** The head of design proposes merging `actionSecondary` into `secondary`. Manel argues against: "These are not secondary texts as they also are interactive... it will add confusion as it's less clear when to use one or the other... less flexibility to adjust a semantic group". A "⚓️ Decision" note then aligns tokens with snackbar/alert variants (action, actionSecondary, warning, danger, success, each with a secondary). A noted Figma limitation: no border token for the unticked checkbox | [open](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4731-289) |
| Exploration 3 | Note: moved to the exploration file | | |

## Image sources

| Use | Node | Link |
|---|---|---|
| Semantic token table (text) | Text tokens | [3608:20540](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=3608-20540) |
| Spectrum primitives | spectrum | [3608:21685](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=3608-21685) |
| Spacing tokens, original vs tokenized | Frame 4 | [4295:53](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4295-53) |
| Naming anatomy | Frame 28 | [3608:22036](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=3608-22036) |
| Token audit: status quo | Status Quo | [4786:183](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4786-183) |
| Token audit: debate and decision | Analisys and proposal | [4775:165](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4775-165) |
| Token audit: missing or mismatched | Missing / missmatched | [4786:222](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4786-222) |
