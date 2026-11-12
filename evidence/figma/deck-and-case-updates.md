# Deck and live-case updates from the Figma audit

Backlog from the 2026-11-09 Figma audit ([README.md](README.md)). Ranked by hiring impact. Nothing here has been applied yet. Decks live in `decks/`; live cases in `portfolio/public/cases/`. The copy is recruiter-facing, so run `no-ai-slop` and `anthropic-skills:humanizer` on any new or changed text. Check every image for customer names, emails and real figures before external use. PNGs are in [images/](images/README.md).

## 1. Abacum DS deck: add the January 2024 token audit

Do this first: it's the deck for the Perk Depth of Expertise call.

**Status (2026-11-11):** applied to the deck source on slide 7 (build steps 2 and 3, speaker notes Figma 14a and 14b, Q&A entry, Don't claim line) and to the register ("Claim (token audit)"). Built in Figma 2026-11-11 (v2 row, positions 14 to 16; no image crop used). The decision note's full secondary family didn't ship: only `actionSecondary` is in the variables. Live case and the "Also available" items are still open.

- **Where:** [case-deck-design-systems-abacum.md](../../decks/case-deck-design-systems-abacum.md), slide 7 (Architecture) or 8 (Governance), as a build.
- **What:** the head of design proposed merging `actionSecondary` into `secondary`. Manel argued it would blur when to use which and reduce flexibility to adjust a semantic group. A "⚓️ Decision" note aligns tokens with alert variants (action, warning, danger, success, each with a secondary). Source: [abacum-abax-core.md](abacum-abax-core.md), page "2401 Token audit", sections [4775:165](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4775-165) and [4786:183](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4786-183).
- **Also available:**
  - naming anatomy board [3608:22036](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=3608-22036), for slide 7
  - the Graveyard of 52 deprecated sets ([abacum-abax-components.md](abacum-abax-components.md)), as deprecation proof for slide 8
  - the variable counts (139 spectrum primitives, 193 semantic tokens)
  - the palette color-blindness check ([abacum-abax-core-exploration.md](abacum-abax-core-exploration.md)), as a speaker-note detail
- **Boundary:** Abax is shared. Present the audit as Manel's argument inside a team decision.
- **Live case:** `design-systems.html` can take the same token-audit beat.

## 2. Remuner DS deck and live case: show the real "before"

- **Slide 2 (Starting point)** of [case-deck-design-systems-remuner.md](../../decks/case-deck-design-systems-remuner.md): use the legacy SCSS palette dump and the font-size audit (9px to 25px in production) from [remuner-core.md](remuner-core.md): [109:906](https://www.figma.com/design/SmHO5c8ExGDaO6r2hDvbHy/?node-id=109-906), [0:1](https://www.figma.com/design/SmHO5c8ExGDaO6r2hDvbHy/?node-id=0-1).
- **Slide 9 (Outcome):** "the library at departure": 161 component sets, 1,438 variants, plus domain components (plan cards, pacing bars, tiers, the Remu widget, email templates). Source: [remuner-components.md](remuner-components.md).
- **Optional:** the OKLCH palette rebuild ([1044:558](https://www.figma.com/design/SmHO5c8ExGDaO6r2hDvbHy/?node-id=1044-558)) as a hardening detail; Key screens ([remuner-key-screens.md](remuner-key-screens.md)) as a one-image platform map.
- **Q&A:** documentation lived across Notion, Figma and Storybook.
- **Live case:** `design-system-remuner.html` gets the same before image.

## 3. Dataset Manager deck and live case

- **Slide 6 (Diagnosis)** of [case-deck-dataset-manager.md](../../decks/case-deck-dataset-manager.md): the five user problems written on the canvas ("Users have to learn unintuitive and inconsistent nomenclature", "Users can't intuitively write formulas", "...can't easily work with long formulas", "...can't easily read and understand syntax", "On small screens, users can't see the dataset preview"). Source: [abacum-dataset-manager-exploration-live.md](abacum-dataset-manager-exploration-live.md), page "2309 -> Transformation improvements", [4386:192874](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=4386-192874).
- **Slide 10 (Outcome):** "2312 -> Transformation QA", a check of the shipped formula box against real customer transformations (screenshots from 1 December 2023): [5436:26320](https://www.figma.com/design/SX7z0Cp4IMIw8RmNyrsI5G/?node-id=5436-26320).
- **Optional, slide 2 (Context):** the verbatim back-end schema errors users used to get ("Schema contains no defined measures", "Formula {formula_name} is of an undefined type"), page "2202 -> Upload a new dataset" in [abacum-dataset-manager-exploration.md](abacum-dataset-manager-exploration.md).
- **Backup or Q&A:** usability test script next to its prototype ("🙋🏻‍♀️ Auto-sync prototype") and tested rounds ("2303 -> Dataset loads -> months"), both in the backup exploration file; the creation-funnel measurement plan ("2202 -> Create", frame "measure") in [abacum-dataset-manager-implementation.md](abacum-dataset-manager-implementation.md).
- **Boundary:** another designer, Carol, has labelled sections in the live exploration file ("Manual adjustments", "Easier bulk month selection"). Don't use them.
- **Live case:** the open TODO "Dataset Manager case images" can now pull from the exported PNGs in `images/jf2hsBYAPS9ilnauvYHWDR/`, `images/rg5IG7leRJXbj8HP93Jnsk/` and `images/SX7z0Cp4IMIw8RmNyrsI5G/`.

## 4. Hidden Rep Letters case: decide whether to finish it

- **What's new:** its four empty image placeholders can be filled from [remuner-hr-compliance.md](remuner-hr-compliance.md):
  - Admin v1 vs v2
  - the template editor with blocks and placeholders
  - the plan status model (calculation + compliance + dates in one indicator)
  - the banner-to-app-block escalation for unsigned letters
  - the cancel, resend and reject edge cases
- **Still missing:** an outcome.
- **Recommendation:** finish it only if a fifth visible case is needed; otherwise use it as an interview story. It competes with the IC dashboard case (see 7).

## 5. Modeling Syntax deck: small additions

- **Slide 3 (The problem):** the "2302 -> Syntax usability" before/after pairs in [abacum-syntax-implementation.md](abacum-syntax-implementation.md) ([510:12665](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=510-12665)).
- **Slide 8 (What changed):** the syntax-chip token spec ([870:29331](https://www.figma.com/design/u7ZLkxpgFamXpEkr3si18l/?node-id=870-29331)) and the function help popover from [abacum-syntax-exploration.md](abacum-syntax-exploration.md).
- **Gap that stays:** the competitor benchmark table and the customer-call evidence for slide 5 aren't in any Figma file. They may be in the Notion export.
- **Boundary:** the syntax workshop (November 2023) was a shared team session; context only.

## 6. AI Agent deck: low priority

- **Slide 6 (Answer anatomy):** sample structured answers on the Remu component page ([remuner-components.md](remuner-components.md)) and the "0425 -> IA coaching" exploration ([remuner-dashboard-ic.md](remuner-dashboard-ic.md)).
- **Close or backup:** AI plan generation ("0226 -> Remu plan generation", [remuner-comp-plans.md](remuner-comp-plans.md)): the same assistant moving from answering questions to building plans. One line only: designed end to end, partially built at departure, outcome unknown.

## 7. New material: rep research (story first, case later)

- **What:** the June 2025 team dashboard findings deck and the late-2025 "My plans" interviews.
  - **Dashboard deck (Manel's, confirmed):** QuickSight 68 → 10 new managers March to June 2025, 34% visited once, "useful but not usable".
  - **My plans interviews:** verbatim rep quotes, two personas, hypotheses, a user test, then the refactor.
- **Why it matters:** together they say reps live in the dashboard and barely use plan pages.
- **Sources:** [remuner-dashboard-manager.md](remuner-dashboard-manager.md), [remuner-my-plans-ic.md](remuner-my-plans-ic.md), [case-candidates.md](case-candidates.md) candidate A.
- **Use first as:** an interview story (research-led prioritisation).
- **As a case:** it strengthens the existing TODO "Remuner IC dashboard as a case".
- **Boundary:** adoption after the default dashboard was measured, but no data survives. Say it was tracked; never state a result.

## Other candidates, interview stories only

From [case-candidates.md](case-candidates.md):
- **Model relationships:** "15 users reported..." through to the shipped Relationship panel (Abacum Engine).
- **Guardrails for live compensation data:** Remuner Datasets and Mappings.
- **Making incentive logic legible:** IC dashboard tiers and negative metrics.
- **Currencies and conversion rates:** Comp. plans; collaborative.
