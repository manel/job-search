# Handoff, 2026-11-19

## Goal

Two threads ran in this session:

1. **Interview fix plan, day 1** ([analysis/2026-11-18/interview-fix-plan.md](analysis/2026-11-18/interview-fix-plan.md)): fix interview conversion by 2026-12-02 (impact, live cases, follow-ups, facts, visual craft).
2. **Visual craft gap** (Perk rejection, 2026-11-18): show visual and interaction craft on the portfolio. This turned into interaction clips (rebuilt components rendered to video) on the Abacum DS case, with a goal of at least one clip per case.

## Current status

- **Live on manel-leiva.com** (portfolio `64c409a` on `dev`, merged to `main` as `f12f901`): three clips on the Abacum DS case (Select, table selection, table density), captions at 14 px `#6b6b78` (WCAG AA) site-wide, favicon (white M on teal) on every page, About section rewritten to match the CV and LinkedIn. The Dataset Manager fix `6a9f1c6` also went live with this merge.
- **job-search** is committed and pushed (`3af5207`, `81adb57`). Uncommitted at handoff: TODO.md and the plan status line (edited after the last commit), plus this file.
- **Interview fix plan, day 1:** only the fact card was read. NOT done: playbook review, `abax` impact session, drill 2, the FluidVoice transcript test. All carried to Fri 2026-11-20, which already has its own load (see the plan calendar).
- **Clips for the other cases:** not started. TODO item "Interaction clips for every case".
- Mobile layout of the new case section and About section: never checked.

## Decisions made (with reasons)

- **Remuner before/after dropped** from the visual piece (Manel): the before looked very poor, so the after proves little.
- **Clips are HTML rebuilds at 1:1 from Figma values**, rendered frame by frame with headless Chrome and ffmpeg (`scripts/video/record.js`). No Remotion: deterministic frames, no extra dependency.
- **Claims:** table density is shared work (the head of design defined the spacing; Manel built and published the tokens and adapted the cell and table components; shipped). Select additions are shared work (Manel did the states and spec; shipped). Table selection: designed and prototyped, shipped status unknown. All in [evidence/experience-facts.md](evidence/experience-facts.md).
- **No "rebuilt" sentence on the case page** (Manel deleted it). In interviews, say the clips were rebuilt from his Figma specs.
- **Pipeline:** Stripe DS kept open (posting check 2026-12-03). Bunge requisition closed 2026-11-03. Haddock: no reply; mark stale 2026-11-26.
- **Business fluency:** the $849 masterclass is out of budget; free path in [interviews/reference/business-learning.md](interviews/reference/business-learning.md), after 2026-12-02. Business stays one line per answer (Designer, not PM).
- **Favicon option A** (M on teal): clearest at 16 px, brand hue.
- **Video rules** are canonical in [context/brand.md](context/brand.md), section "Interaction clips for cases".

## Tried and rejected

- A selection box that snaps cell by cell, then one that glides between cells: Manel wanted it to follow the pointer. The final version follows continuously and settles at release.
- Wide frames with lots of white space, and titles inside the videos: replaced with tight frames and captions on the page.
- Notes in the Select clip that disappeared after about 1.4 s: now held 3.5 s, one note per row.
- Unequal density holds (4.4, 2.8, 3.4 s): now 3.5 s each.
- Maven link for Ryan Scott's free lessons: 404. Replaced with his podcast episode and dscout guide.
- Exporting Figma vectors as SVG through the bridge timed out; reading `vectorPaths` worked.

## Files touched

- Portfolio: `portfolio/public/cases/design-systems.html`, `portfolio/public/index.html`, all `portfolio/public/cases/*.html` (favicon tags), `portfolio/public/css/case.css`, `portfolio/public/assets/videos/abax-*`, `portfolio/public/favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`.
- Renderer and sources: `scripts/video/` (`record.js`, `cursor.js`, `abax-select.html`, `abax-table-density.html`, `abax-table-selection.html`, `abax-table-selection-driver.js`).
- Records: [TODO.md](TODO.md), [analysis/2026-11-18/interview-fix-plan.md](analysis/2026-11-18/interview-fix-plan.md), [evidence/experience-facts.md](evidence/experience-facts.md), [context/brand.md](context/brand.md), [interviews/reference/business-learning.md](interviews/reference/business-learning.md), Stripe DS, Bunge and Haddock records in `applications/records/`, [applications/active.md](applications/active.md).
- Not changed on purpose: [interviews/perk/perk-table-selection-rebuild.html](interviews/perk/perk-table-selection-rebuild.html) (approved Perk page; the video uses a copy).

## Next steps

1. Commit and push this file plus the TODO and plan status edits.
2. Fri 2026-11-20: run the carried day-1 items (playbook review, `abax` impact session with one recall question at a time, drill 2, FluidVoice test), then Friday's own items. Fixed dates: Wizeline check-in with David Ho, Fever test check, Neotalent nudge. Expect the plan to need re-balancing; propose it, don't assume it.
3. Interaction clips for the next case: ask Manel which component per case (candidates in TODO), confirm his part and shipped status, record it in the register, then build following [context/brand.md](context/brand.md).
4. Check the Abacum DS case and About section on a phone width.
5. Write the per-pair visual decisions for the visual piece (hierarchy, spacing, type, colour) if Manel still wants them alongside the clips.

## Open questions

- Should the visual decisions text (workstream E) still be written now that the clips are live, or do captions cover it?
- Which component per remaining case (Dataset Manager, Modeling Syntax, AI agent, Remuner DS)?
- Did Manel do the playbook review today? Only the fact card is confirmed.
- Pre-existing en dash in the Abacum case tag ("2022–2024", `design-systems.html` line 55) is still there; fix or leave?

## How to verify

- Live clips: `curl -s https://www.manel-leiva.com/cases/design-systems | grep -c abax-` (expect 9 or more).
- Favicon: `curl -s -o /dev/null -w '%{http_code}' https://www.manel-leiva.com/favicon.ico` (expect 200).
- Links: `python3 scripts/check-links.py`.
- Re-render a clip (needs playwright-core somewhere; it is not a repo dependency): `NODE_PATH=<dir>/node_modules node scripts/video/record.js scripts/video/abax-table-density.html portfolio/public/assets/videos/abax-table-density`. The selection clip also needs `--driver scripts/video/abax-table-selection-driver.js --viewport 780x488`.
- Repo state: `git status` in job-search and `git -C portfolio status -sb`.
