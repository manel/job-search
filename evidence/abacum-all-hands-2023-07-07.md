# Abacum all-hands deck, 7 July 2023 ("Stoa · Design system")

Source: `Design system.pptx`, 27 slides, supplied by Manel and read 2026-11-16. The .pptx was deleted after extraction at Manel's request; this file and the images in [decks/assets/abacum/all-hands-2023-07-07/](../decks/assets/abacum/all-hands-2023-07-07/) are what remains. Class: confirmed artifact. Authorship of individual slides is not recorded. Slides 21 to 27 carry "ML" markers; don't read that as Manel Leiva without confirmation (a front-end engineer, Manel E., is also named in the deck).

This is the presentation behind the register's "presented at an all-hands on 7 July 2023" entry and the Notion page "DS presentation prep".

## Claimable content

- **Problem framing (slides 4 to 6):** three pains, "Slow decisions", "Repetitive tasks", "Inconsistent UI". Questions designers asked: "What's the hex code for the blue callout?", "Which button type are we using in the top bar?", "Are capitalizing all words in the title or not?", "What does the empty state look like?"
- **Inconsistent UI example (slide 6):** a Modules card (Engine squad, where modelling happened) and a Datasets card (Actuals squad). Same card pattern; different link weight, link size and spacing. Squad mapping confirmed by Manel 2026-11-16.
- **Repetitive tasks example (slide 5):** a hand-made redline spec of an alert component.
- **State of Abax at the time (slide 15):** 250 tokens deployed, 100+ icons available, 16 front-end components of which 3 fully synced between Figma and code.
- **Rituals (slide 14):** design system weekly (1h), design library weekly (1h), front-end syncs if needed.
- **Workflow (slide 16):** GitHub, Figma and the production web app; Storybook demo (slide 17).
- **Vision, Abax 1.0 (slides 18, 21):** basic documentation so the system is self-serve, essential components, defined ways of working. Planned measures: DS adoption (component usage), time to market, time from idea to prototype.
- **Contribution asks (slide 20):** Product, identify components worth adding to the platform and join the next DS Maker Days; FP&A, capture inconsistencies "from small (colors, text formats) to large (different UI patterns for the same use case)"; front-end, join #design-system and the next DS Maker Days.
- **Speaker note (slide 13):** "Abax is not just a group of components, it's a team of people working together to create guidelines, best practices, improving performance, streamlining processes". Matches Manel's Notion script line.

## Not usable

- Slide 3: colleagues' photos. Not extracted.
- Slides 2, 7, 11, 12, 19, 22, 23: industry ratios, quotes, famous systems, generic ROI. No Abacum data; the ROI calculator slide has no figures.

## Saved images

In [decks/assets/abacum/all-hands-2023-07-07/](../decks/assets/abacum/all-hands-2023-07-07/):

| File | Slide | Use |
|---|---|---|
| `inconsistent-ui-engine-modules-card.png` | 6 | Deck slide 3 (Figma 7 to 10), evidence card |
| `inconsistent-ui-actuals-datasets-card.png` | 6 | Same |
| `repetitive-tasks-alert-redline.png` | 5 | Backup: manual spec work |
| `alert-content-anatomy.png` | 10 | Alert copy anatomy: type of alert, what happened, how to solve it. Content-design example (Perk, Tim Archer). Who wrote the guideline is not recorded |
| `storybook-button-2023-07.png` | 15 | Storybook Button guide, July 2023 |
| `storybook-icons-2023-07.png` | 15 | Storybook icon set, July 2023 |
| `figma-design-library-2023-07.png` | 9 | Figma library pages (Comment, Notification): description, construction, elements, examples |

Checked for customer names: the card images show demo names ("Balance Sheet 2022", "Financials 2021").
