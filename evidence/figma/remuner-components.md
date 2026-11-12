# Remuner | 💠 Components

File: [N1rTYgkJ4cNvcYZL3BsqzU](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU). 63 pages, one per component. Counted on 2026-11-09: 161 component sets with 1,438 variants, plus 171 standalone components. Of these, 183 are public; names starting with `.` or `_` are private building blocks. Only 11 components carry a Figma description. Full listing: [catalog/remuner-components--N1rTYg.md](catalog/remuner-components--N1rTYg.md). Case source: [decks/case-deck-design-systems-remuner.md](../../decks/case-deck-design-systems-remuner.md). Foundations: [remuner-core.md](remuner-core.md).

Indexed 2026-11-09 from a full extraction. Ownership: Manel's. Page order: Logo, then Components, Form elements, app-level patterns (Appbar, Email, Navigation, Subheader, Tiers, Widgets), Utilities.

Property naming follows a consistent pattern: boolean `has*` and `is*` props (`hasLabel`, `hasInfo`, `isFilled`), plus `state`, `size`, `type` and `orientation`. Dialog, Popover and BottomSheet use slot components ("Replace with component or local component").

## Components by page

| Page | Sets / variants | What's there | Link |
|---|---|---|---|
| Logo | 3 singles | RemunerLogo, RemunerMark, RemuScoreLogo | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=0-1) |
| Avatar, Avatar Group | 2 / 12 | size, content | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=10-426) |
| Icon | 1 / 4 | icon swap, hasTooltip, size | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=1876-15382) |
| Banner, Alert, Snackbar | 3 / 12 | type, actions, icon, close | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=370-2804) |
| Button | 1 / 130 | type, state, size, leadingIcon; private `.focusRing` | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=11-463) |
| IconButton, BulkActions, SplitButton, FAB | 4 / 58 | | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=795-5270) |
| Chart | 21 / 222 | Lines, grouped, stacked and waterfall bars, area, pie, progress pie, ranking chart; bar sizes built as variant grids | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=22-4139) |
| Chip | 5 / 81 | Chip (60 variants), FrequencyChip, RankingChip, ChipCardDetails desktop and mobile | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=212-37646) |
| Cards | 23 / 73 + 29 singles | Domain cards for incentive plans: individual metric, payout, operations, ranking and average cards, desktop and mobile; manager and admin team/plan views; card tree | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=12-485) |
| Progress Bar | 8 / 72 | progressBar/Metric (40 variants) with pacing, min, max and restrictions; pace indicator; ranking lines | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=2263-6893) |
| Slider | 1 single | | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=653-7428) |
| Dialog + Compositions | 11 / 42 + 20 singles | Dialog (12 variants, slot-based); compositions for payout, metric, tiers, multiplier, weighted metric, restrictions, true-up payout, new-plan dialog, freeze-period copy | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=372-4861) |
| Popover + Compositions | 3 / 9 + 3 singles | Notifications and sharing popover contents | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=1117-807) |
| BottomSheet, Divider | 2 / 5 | Mobile sheet with slot | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=806-4081) |
| Table | 10 / 102 + 6 singles | Cell types: text, chips, header, actions, icon, number, avatar, status; mobile transaction list; `.TableOld` kept | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=26-14450) |
| Tabs, Menu, ActionsMenu, Tooltip, Pagination, Step | 6 / 17 | | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=626-8031) |
| ListItem, ListPanel | 11 / 66 | Default, input, single and multi select, create; list panels | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=1124-1231) |
| Remu | 6 / 14 | The AI assistant widget: content types, header, footer with suggested questions, saved chats; sample answers in Spanish about commissions and bonus progress | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=3521-3) |
| Form elements | 18 / 400 | Autocomplete (48), Checkbox, Color Picker, Date Input (32), Date Picker, File Input, Radio, RadioGroup, Select (131), Segmented Control, Switch (32), Textarea (32), TextField (36); a deprecated Select kept on its own page | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=411-6524) |
| Appbar, Navigation, Subheader | 6 / 23 | Desktop and mobile | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=137-47) |
| Email | 1 / 10 + 7 singles | Email template system: header, footer, slot, disregard message, icons | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=2434-3474) |
| Tiers | 3 / 13 | Tier blocks (marginal, capped), tiers indicator | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=2653-1017) |
| Widgets | 16 / 83 + 17 singles | Dashboard widgets for managers (by group, payouts, user, period, ranking, members) and ICs (metrics, earnings, payments, personal target); skeleton; empty CTA | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=1366-242) |
| Utilities | 2 / 16 + 44 singles | Note, Spacer, cursors | [open](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=24-4983) |

## Image sources

| Use | Node | Link |
|---|---|---|
| Scale of the button system | Button page | [11:463](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=11-463) |
| Domain components, not only primitives | Cards page | [12:485](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=12-485) |
| Progress with pacing and restrictions | Progress Bar page | [2263:6893](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=2263-6893) |
| Data viz components | Chart page | [22:4139](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=22-4139) |
| AI assistant widget | Remu page | [3521:3](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=3521-3) |
| Email template system | Email page | [2434:3474](https://www.figma.com/design/N1rTYgkJ4cNvcYZL3BsqzU/?node-id=2434-3474) |

Documentation lived across Notion, Figma and Storybook (Manel, 2026-11-09), so the 11 Figma descriptions are only part of it.
