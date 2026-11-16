# Handoff: TODO walk-through, steps 1 to 8 (session 2026-11-14)

Replaces the 2026-11-11 handoff (Abacum DS deck token audit), which is still in git history. Its open work, the token audit in the Abacum DS deck before Perk, is still open: see step 8 below and [TODO.md](TODO.md).

## Goal

Go through the "This week" items of [TODO.md](TODO.md) one at a time with Manel, in this order:

1. Figma Base CV: done
2. LinkedIn Kings of Mambo entry: done
3. Dataset Manager deck notes: done
4. Notion deck updates: done, except what Manel still pastes or plays
5. Stripe DS and Bunge: stopped here, one decision open
6. Haddock: Manel says it is done, but the TODO is not updated yet
7. Portfolio PDF: Manel did not know what this item is, so explain it
8. Abacum DS deck: what is still missing before Perk (Tim Archer, Tue 2026-11-17, 10:00)

Manel wants one step at a time, in short STE-style replies.

## Current status

- **Step 1 done.** Figma "CV / Manel Leiva", column "CV BASE" (p1 `2381:432`, p2 `2381:473`) now matches [cv/cv-base.md](cv/cv-base.md). Manel exported the Base PDF and it passes `check-pdf-text --source`. He set Kings of Mambo to "hybrid" himself and wants that never changed again. This is recorded in [evidence/experience-facts.md](evidence/experience-facts.md) (work mode entry), in the cv-base header notes and in Claude memory (`feedback_kom_work_mode_final.md`).
- **Step 2 done.** The LinkedIn Kymco sentence is live without "with a second designer". [context/linkedin.md](context/linkedin.md) is updated.
- **Step 3 done.** Manel pasted the Dataset Manager notes and checked slides 4, 5 and 9. Open question resolved: the FP&A team created customers' connections and datasets, and engineers helped with the initial import, configuration and transformations. This is in the register (Dataset Manager section).
  - Slide 2 on-slide text is fixed in Figma "Dataset manager".
  - Deck source is now v2.2.
  - Manel still has to paste the new Figma 2 note from [decks/case-deck-dataset-manager.md](decks/case-deck-dataset-manager.md). Not confirmed.
- **Live Dataset Manager case:** two lines fixed and pushed to portfolio `dev` (commit `6a9f1c6`). This change is NOT on `main`. Manel has not checked the Vercel preview. The submodule pointer here is not committed.
- **Step 4.** Modeling Syntax deck (Figma `mOXQnVxL9e6XBo8jthv6zB`):
  - Slide 5 is now a two-step build: Figma 5 shows the benchmark with the quote card at opacity 0; Figma 6 shows the quote, with Smart Animate 0.3s ease-out.
  - Notes in [decks/case-deck-modeling-syntax.md](decks/case-deck-modeling-syntax.md) are renumbered by Figma position (1 to 11).
  - Manel has not confirmed that he pasted the notes or played the build.
- **Step 5, stopped here.**
  - Bunge was already `role-closed` on 2026-11-07, so it needs no action.
  - Stripe Product Designer, Design Systems: posting live on 2026-11-14, 47 days silent.
  - Manel messaged Mike Wilson (Product Designer, Stripe, no prior relationship) on 2026-09-28 and got no reply. Manel does NOT want to follow up with him.
  - Owen Williams (Design Manager, Developer Experience and AI) is not on the DS team, so he is a weak target.
  - Everything is recorded in [applications/records/stripe-product-designer-design-systems.md](applications/records/stripe-product-designer-design-systems.md).
  - The DS-team people search is unresolved: web search does not show LinkedIn people lists.

## Decisions made (with reasons)

- **Kings of Mambo work mode is "Barcelona (hybrid)" on every CV.** Manel's final call. Never suggest "on-site, later hybrid" again.
- **EDUCATION heading stays at 2 px letter spacing.** All headings use 2 px; the 2026-11-06 note saying "zero like the others" was wrong.
- **Base CV header breaks after the phone number,** as in the tailored CVs. On one line it wrapped "linkedin.com/in/" badly.
- **Dataset setup credit: "our FP&A team, with help from the squad's engineers".** Never credit engineers alone (Manel 2026-11-14).
- **Modeling Syntax slide 5 is split into a build.** Manel chose this; I had recommended no build.
- **No further contact with Mike Wilson.** Manel does not know him and does not want to bother him.

## Tried and rejected

- `figma_take_screenshot` on a non-active file falls back to an expired REST token and fails. Instead, export through `figma_execute` (`exportAsync` + `figma.base64Encode`), then decode the saved tool-result file into the scratchpad.
- Duplicating a slide with `clone()` placed the copy before the original. Fix the order with `figma.setSlideGrid` using explicit node IDs.
- WebSearch for Stripe DS team members on LinkedIn: no profiles, only job postings.

## Files touched (all uncommitted in job-search)

- [TODO.md](TODO.md): items rewritten for steps 1 to 4
- [cv/cv-base.md](cv/cv-base.md): header note and KoM "hybrid"
- `cv-pdf-to-send/Base/Manel Leiva CV 2026.pdf`: re-exported by Manel. This is the Base, not a sent PDF.
- [evidence/experience-facts.md](evidence/experience-facts.md): work mode entry; dataset-setup answer
- [context/linkedin.md](context/linkedin.md)
- [decks/case-deck-dataset-manager.md](decks/case-deck-dataset-manager.md), [decks/case-deck-modeling-syntax.md](decks/case-deck-modeling-syntax.md)
- [applications/records/stripe-product-designer-design-systems.md](applications/records/stripe-product-designer-design-systems.md)
- `portfolio` submodule: on branch `dev` at `6a9f1c6`, so the pointer shows as modified
- **Not from this session:** `applications/active.md` (modified) and `applications/records/idealista-ux-product-designer.md` (untracked). Probably another session's work. Ask Manel before committing them.

## Next steps

1. Commit this session's job-search changes, but do not commit the submodule pointer while it points at `dev`. Ask Manel about `active.md` and the Idealista record first.
2. **Step 5:** ask Manel whether to mark Stripe DS `stale` now (`/update-pipeline stripe stale`), or to keep it while he searches LinkedIn for a Sail team design manager himself. Then remove the "Decide Stripe DS and Bunge" TODO line, because Bunge is already closed.
3. **Step 6:** close the Haddock TODO item. Manel confirmed "done", and the 12 Nov nudge was sent. Check that [applications/records/](applications/records/) has a Haddock record with a dated `next_action_on`.
4. **Step 7:** explain the "Portfolio PDF text" item. The Flodesk portfolio PDF has no extractable email, because the links are underlined (see memory.md, 2026-10-20). The planned 5 to 8 page portfolio PDF needs contact details as real text. Ask whether he wants to build that PDF now or park it.
5. **Step 8:** Abacum DS deck before Perk, 2026-11-17. Open sub-items are in the Abacum deck item of [TODO.md](TODO.md):
   - play the Smart Animate builds;
   - re-paste notes Figma 1, 9, 11, 12, 16, 23, 24, 29, 30, 32;
   - take the Abax screenshots for slides 2 and 10;
   - check B3;
   - do the token audit (item 1 of [evidence/figma/deck-and-case-updates.md](evidence/figma/deck-and-case-updates.md)).
   Also the short recall session before Perk: one mentoring episode, and vLex scope.
6. Once Manel approves the Vercel preview: merge portfolio `dev` to `main`, push, then commit the submodule pointer here.
7. Mon 2026-11-16: answer Capitole on EUR 40K (TODO item).

## Open questions

- Did Manel paste the Dataset Manager Figma 2 note and the Modeling Syntax notes, and play the slide 5 build?
- Stripe DS: stale now, or wait?
- Manel said the Desktop Bridge is connected to the CV file. The reason was not stated; maybe for step 8 or a later CV job.

## How to verify

- `python3 scripts/check-pdf-text.py "cv-pdf-to-send/Base/Manel Leiva CV 2026.pdf" --source cv/cv-base.md` should print OK.
- `python3 scripts/check-postings.py` shows Stripe posting status.
- `git -C portfolio log --oneline -1 origin/dev` should show `6a9f1c6`.
- `python3 scripts/check-links.py` after any Markdown move.
