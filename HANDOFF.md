# Handoff: Abacum DS deck token audit, then the portfolio TODO (session 2026-11-11)

Replaces the 2026-11-05 Perk handoff (still in git history at `a0edd21`). The newer Perk state is in [applications/records/perk-senior-design-systems-designer.md](applications/records/perk-senior-design-systems-designer.md), not in that old handoff.

## Goal

1. Add the January 2024 token audit to the Abacum DS deck before the Perk Depth of Expertise call (60 min video, with a Lead Product Manager, one project end to end; Abax is the lead project).
2. Then work through the "Portfolio" section of [TODO.md](TODO.md).

## Current status

- **Nothing has been written to the deck yet.** The previous session ran in the portfolio repo (`~/Dev/manel-leiva-portfolio`), only looked at the backlog, and stopped so the work could move here, where the deck and writing rules live.
- **Perk call not booked yet.** Slots submitted for Wed 11 to Tue 17 Nov. The record's `next_action`: if no invite by Wed 11 midday, reply in Clare's thread asking for the booking. Today is Wed 11 Nov. Check this first.
- **Submodule pointer is stale.** `portfolio/` sits at `abc67e4`; `origin/main` is at `4cba4d7` (removes the dead `middleware.js`, adds the portfolio repo's `CLAUDE.md`). `main` and `dev` on the portfolio remote are both at `4cba4d7`.
- **Working tree here is dirty from before this session:** `TODO.md`, `applications/active.md` and several `applications/records/*.md` are modified. The previous session didn't touch them. Don't commit them without asking Manel.

## Decisions made (with reasons)

- **Deck and case copy work runs in job-search, not in the portfolio repo.** The deck, `principles.md`, `context/writing-rules.md`, the `memory.md` writing rules and the skills (`no-ai-slop`, `review-case`, `prep-interview`) only load here. The portfolio repo's `CLAUDE.md` imports only `context/portfolio.md`, so a session there misses the writing rules. Live case edits go through `portfolio/` from here.
- **The portfolio repo stays for purely technical site work** (CSS, layout, deploy, branches) if Manel wants a separate session for it. Its rules: `main` is production, `dev` is for preview, merge to `main` only when Manel says so, commit and push only when asked. They are in `portfolio/CLAUDE.md`.
- **Token audit framing:** Abax was shared. Present the audit as Manel's argument inside a team decision, not as his decision alone.

## Tried and rejected

- Working on the deck from the portfolio repo: rejected, because the deck and writing rules don't load there (see above).

## Files touched

- `HANDOFF.md` (this file). Nothing else in job-search.
- Portfolio repo, already pushed: commit `4cba4d7` on `main` and `dev`.

## Next steps

1. **Perk booking.** Check whether the calendar invite has arrived. If not, and it's past midday on Wed 11, draft the reply to Clare for Manel to send. Log it in the record History.
2. **Update the submodule:** `git -C portfolio pull`, then commit the pointer change in job-search on its own. Ask Manel first, because other uncommitted files exist.
3. **Token audit in the deck.** Target: [decks/case-deck-design-systems-abacum.md](decks/case-deck-design-systems-abacum.md), slide 7 (Architecture) or slide 8 (Rollout and governance), as a build. Brief: item 1 in [evidence/figma/deck-and-case-updates.md](evidence/figma/deck-and-case-updates.md). Source: [evidence/figma/abacum-abax-core.md](evidence/figma/abacum-abax-core.md), page "2401 Token audit".
   - The beat: the head of design proposed merging `actionSecondary` into `secondary`. Manel argued it would blur when to use which, and reduce the flexibility to adjust a semantic group. A "⚓️ Decision" note aligned tokens with the alert variants (action, warning, danger, success, each with a secondary).
   - Figma nodes: debate [4775:165](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4775-165), status quo [4786:183](https://www.figma.com/design/UueAtXpFYzKECtUnK18a8B/?node-id=4786-183).
   - Optional extras: naming anatomy board `3608:22036` (slide 7), the Graveyard of 52 deprecated sets (slide 8), 139 primitive and 193 semantic variables, the color-blindness check as a speaker note.
   - Update the matching speaker notes in the deck's "Speaker notes to paste into Figma" section, and Q&A if it fits.
   - Run `no-ai-slop` and `anthropic-skills:humanizer` on the new text. Check for em dashes.
4. **Live case, after the deck:** add the same beat to `portfolio/public/cases/design-systems.html`. Ask Manel before committing; push to `dev` first.
5. **Portfolio TODO, in this order** (findings from the 2026-11-11 review of the live pages):
   1. Modeling Syntax Overview outcome is generic ("reduced cognitive load"). Rewrite it from facts already in the body: days rather than weeks, fewer support requests, unlocked the formula builder autocomplete. The other four Overviews already carry an outcome, so the "Outcome up front" TODO is mostly done. Decide whether to add the ~47% figure to the Abacum DS Overview.
   2. Closing lesson: the two DS cases already end on a trade-off section. Dataset Manager, Modeling Syntax and AI agent end on outcomes, so add one to each. Consider trimming the DS cases (about 1,960 and 2,130 words).
   3. Figma MCP umbrella line in the Remuner DS case. Approved CV wording and limits are in [evidence/experience-facts.md](evidence/experience-facts.md) (around line 346).
   4. Dataset Manager images (start of the visual-rework pilot). Check every frame for customer data and colleague names first.
   5. Decide on the Remuner IC dashboard case versus Reps Letter.
   6. Portfolio PDF. Notion export in its own session.

## Open questions

- Slide 7, slide 8, or a separate slide for the token audit? The backlog says "as a build" in one of the first two.
- Should the ~47% figure go in the Abacum DS Overview?
- Does the old 2026-11-05 handoff still have anything unresolved that isn't in the Perk record? It mentions the "80% of new UI" wording: a grep of `portfolio/public/cases/design-systems.html` found no match on 2026-11-11, so that fix looks live.

## How to verify

- Perk next action: `grep -n "^next_action" applications/records/perk-senior-design-systems-designer.md`
- Submodule in sync: `git -C portfolio fetch -q && git -C portfolio status -sb`, then `git status -s portfolio`
- Deck slides: `grep -n "^## " decks/case-deck-design-systems-abacum.md`
- Token audit landed: `grep -n "actionSecondary" decks/case-deck-design-systems-abacum.md`
- No dashes in the deck: `grep -c "—\|–" decks/case-deck-design-systems-abacum.md`
