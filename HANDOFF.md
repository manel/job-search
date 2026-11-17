# Handoff: Perk follow-up to Tim and Mateo (session 2026-11-17, continue 2026-11-18 morning)

Replaces the 2026-11-14 handoff (TODO walk-through, steps 1 to 8). That one is in git history; its open items (Stripe DS stale decision, Haddock TODO, Portfolio PDF item, portfolio `dev` to `main` merge) are still open and also live in [TODO.md](TODO.md).

Manel wants short STE-style replies, one step at a time. Before any text Tim or Mateo will read or hear: run `no-ai-slop` before drafting and `anthropic-skills:humanizer` after; for spoken text, follow "Writing for speech" in [interviews/playbooks/case-presentation.md](interviews/playbooks/case-presentation.md#writing-for-speech).

## Goal

Send Tim Archer (content design manager, owns design systems and technical writing) and Mateo (product designer, Suitcase expert) a follow-up after the Perk Hiring Manager Interview of Tue 2026-11-17. Send through Clare Watts (TA), by the morning of **2026-11-19**. Manel first said "tomorrow" (2026-11-18), so aim for 2026-11-18 if the video is ready.

The follow-up completes two weak answers from the call (debrief in [interviews/perk/perk.md](interviews/perk/perk.md#round-2-debrief-hiring-manager-interview-tue-2026-11-17)):

1. Tim: "A component you elevated visually, or with motion?" Manel had nothing to show ("I only have one animation I could record"). Tim said visual craft is half the role: Suitcase must reach "consumer grade", with a B2C retail feel. He also named poor accessibility across the component set.
2. Tim: "How would you organise documentation across platforms into one source?" Manel said "I don't really know" plus a general layering list. Tim runs technical writing and listed "documentation from a single source that AI and other platforms can read" as a 6 to 12 month success measure.

Format agreed: an email to Clare asking her to forward a short note to Tim and Mateo. The note carries an unlisted video link (answer 1) and a short written answer (answer 2).

## Current status

- **Table selection rebuild: done, approved by Manel.** [interviews/perk/perk-table-selection-rebuild.html](interviews/perk/perk-table-selection-rebuild.html). Self-contained HTML, Inter from Google Fonts (needs internet), `noindex`. Real size, 1:1 with the 2023 boards (702x408). Manel: "yes, that's it".
  - No drag and drop variant: cell hover follows the mouse; row and column indicators follow it; click selects a cell with two handles; drag the bottom-right handle to expand a range; header has three hover zones (header cell, top edge strip, indicator); click zone 1 selects the header cell only, zone 2 or 3 the whole column; rows the same from the left edge (click on the first cell selects the row with an empty indicator, as on the board); Esc or a click outside clears.
  - Drag and drop variant (toggle top right, or `#dnd` in the URL): grip handles 24x16 (top) and 16x24 (left), radius 4, dots `#bdc4c7`; hover blue outline; selected solid blue. Drag follows Notion's pattern: faded copy follows the pointer on one axis, 2px blue drop line, 200 ms FLIP slide on drop. Switching variants resets the order.
  - Row and column selected states use blue (`#0078b2` stroke, `#ebf8ff` fill). The 2023 boards used an older green style (`287:47` / `1457:4`); Manel said it should be blue.
  - Tested only in headless Chromium (scripts in [scripts/table-rebuild-check/](scripts/table-rebuild-check/)). **Not tested in Manel's real browser with a mouse or trackpad.**
- **Video script: drafted, partly open.** [interviews/perk/perk-followup-video-script.md](interviews/perk/perk-followup-video-script.md). Opening (with Manel's "I was reflecting on it afterwards, and there's one answer I'd like to complete"), table section (about 60 s), Remuner section (about 40 s), close pointing to the email. **The Remuner section is now rejected by Manel and must be replaced** (see Decisions).
- **Email: drafted.** [outreach/perk-tim-mateo-followup-2026-11-18.md](outreach/perk-tim-mateo-followup-2026-11-18.md). Email to Clare plus the note for Tim and Mateo, with `[video link]` placeholder. The note says the video shows "table selection at Abacum ... and the Remuner dashboard before and after": **this sentence must change once the second example is chosen.** About 95 words against the 80-word cap in [principles.md](principles.md); accepted because it carries two answers.
- **Second visual example: open. This is where Manel continues tomorrow.** He will check his Figma libraries in the morning for components he redesigned. The generic list he liked (button states, form field, select/combobox/menu, toast, modal/drawer, tabs indicator, skeleton loading, empty states, cards, charts, status chips, date picker, toggle/checkbox, theming) is in the chat only; reproduced in "Open questions" below so it is not lost.
- **Figma click-through: built, then rejected.** Page "Selection prototype (rebuilt 2026-11-17)" (`40000013:429295`) in "Abacum | 💠 Abax Components | Exploration" (`H7KF9JPK3wwFGd8333TaHT`). 15 frames, three flows. Manel: not responsive like the original. It is still in the file; ask whether to delete it. Original boards on page "✅ 2306 -> Table cells" (`2947:66597`) were never edited.
- **Evidence register updated.** Table selection entry in [evidence/experience-facts.md](evidence/experience-facts.md) ("Abax design system" section) now has: the Rebuilt line (Figma page, colour change, click ring, then the HTML page as the one to use); the drag and drop note (handles from boards, drag pattern from Notion, Manel's recollection); the AG Grid context line.

## Decisions made (with reasons)

- **HTML rebuild over Figma.** Figma frame flows can't reproduce "cell highlight follows mouse" or a handle drag; Manel's original used interactive components and felt live. Code took about an hour and behaves like the original.
- **Copy only what the boards show.** No Shift-click range, no tweens on state changes, no "Selected (non-expandable)" state, no expandable rows or columns. Reason: it is labelled "Rebuilt from my 2023 specs"; extra behaviour would misrepresent the spec.
- **Blue, not green, for row and column selection.** Manel's call. Recorded in the register as a change from the boards.
- **Real size, not scaled.** Manel: the 1.7x and fit-to-window versions were far bigger than the original. Record with Cmd+Shift+5, "Record Selected Portion" around the table and the label.
- **AG Grid framing.** Manel's aim in 2023 was to improve AG Grid's default selection, which he judged poor. Verified in `~/Dev/webapp`: June 2023 `package.json` had AG Grid 27.3.0 with `@ag-grid-enterprise/range-selection`. Safe line: "redesigned the selection states on top of AG Grid's default range selection". What was poor, and how much shipped, are not recorded; don't say either.
- **Drag pattern = Notion's.** Manel's recollection. In the script only as an "If asked" line.
- **Fit framing.** Table selection is interaction and state design more than visual elevation. Present it as motion and feedback in a dense data table. A second example must carry the visual-craft half.
- **Remuner dashboard before/after rejected as the second example.** Manel: the old version was very bad, so the improvement was easy and proves little. Same objection rules out the Remuner type scale (9 to 25px audit).
- **Abax Select and Autocomplete ruled out.** Tim already saw it (deck slide 10).
- **Opening line.** Manel wanted to keep his "I was reflecting on our conversation" idea. It is in the video only. The email opens with "Thanks again for Tuesday." Manel asked to cut it from the email so it is not said twice.
- **Original opener edits kept:** "Tuesday's conversation" (not "yesterday", since sending may slip to 2026-11-19); "one answer I'd like to complete" in place of "some answers that weren't ideal from my side" (names one answer, not a general weakness).
- **"here's the answer I should have given"** in the email's docs paragraph: kept. Alternative offered to Manel if he wants it neutral: "On documentation from one source, here's how I'd set it up."
- **Docs answer content** (from the fixes in [interviews/perk/perk.md](interviews/perk/perk.md#assessment-and-fixes-for-the-next-stage-2026-11-17)): one source next to the components (names, usage guidance, content rules), published to Figma, Storybook and the AI tools; nobody edits the same guidance in three places; ask how his team publishes product docs today.

## Tried and rejected

- **Figma Smart Animate flows** (1440x900 frames, after-delay 0.9 s plus on-click, layer names matched): plays a fixed path only, no real hover. Rejected by Manel.
- **Click ring frames** (blue ring at the cursor before each Selected frame): added to the Figma flows, rejected with them.
- **Scaled table** (1.7x in Figma, then fit-to-window up to 1.9x in HTML): too big. Now 1:1.
- **Ghost at 60% opacity, then 90%:** underlying text showed through and looked messy. Now opaque white with blue outline and fill, content at 60%.
- **`figma_take_screenshot`:** REST token invalid. Use `figma_capture_screenshot` (plugin export) after `figma_navigate` with `lock: true`.
- **Python Playwright:** not installed. Node `playwright-core@1.56.1` plus the cached headless shell works (see How to verify).

## Files touched (all uncommitted)

This session:
- [interviews/perk/perk-table-selection-rebuild.html](interviews/perk/perk-table-selection-rebuild.html) (new)
- [interviews/perk/perk-followup-video-script.md](interviews/perk/perk-followup-video-script.md) (new)
- [outreach/perk-tim-mateo-followup-2026-11-18.md](outreach/perk-tim-mateo-followup-2026-11-18.md) (new)
- [scripts/table-rebuild-check/](scripts/table-rebuild-check/) `shot.js` and `dnd.js` (new; headless checks, write PNGs to `shots/` in the current directory)
- [evidence/experience-facts.md](evidence/experience-facts.md): table selection entry (Rebuilt, drag and drop, AG Grid lines)
- [TODO.md](TODO.md): Perk follow-up item points to the email, script and HTML; still says "Remuner before and after" as item (2), which is now rejected
- Figma `H7KF9JPK3wwFGd8333TaHT`: new page `40000013:429295` (rejected click-through)

Not from this session, don't commit without asking Manel: `applications/active.md`, `applications/records/mapon-senior-product-designer.md`, `interviews/mapon/` (untracked). Some `TODO.md` and `evidence/experience-facts.md` changes may also be Mapon work from another session; check `git diff` before committing.

## Next steps

1. **Ask Manel what he found in the libraries.** For each candidate: which company, which Figma file and page, what the before looked like, what he changed (spacing, type, colour token, states, motion timing), whether it entered the system (tokens, variants, docs). One question at a time.
2. **Check each candidate against [evidence/experience-facts.md](evidence/experience-facts.md)** before it goes into the video. New claims go into the register with class and date. Ownership matters: Abacum had other designers (check the "two Manels" trap in memory before crediting Notion or Figma work).
3. **Screen the frames** for real customer names, colleague names and real data before recording. Use copies on a separate page, never edit originals.
4. **Rewrite the Remuner section** of the video script for the chosen example: one sentence per line, one idea per sentence, about 40 s. Then run humanizer and the speech check.
5. **Update the email note's video sentence** to name the chosen example. Keep the docs paragraph as is unless Manel asks.
6. **Update TODO.md** Perk item (2) and the evidence register to match.
7. Manel records: real browser, one practice drag first, Cmd+Shift+5 selected portion. Table part follows the ▶ lines in the script. Time the first take (target about 2 minutes total).
8. Manel uploads unlisted, checks the link in a private window, replaces `[video link]`, sends to Clare in the "Perk | Video Interview for Manel" thread by 2026-11-19 morning.
9. After sending: update [interviews/perk/perk.md](interviews/perk/perk.md) (what was sent and when), the Perk record in `applications/records/`, and the dashboard. Note the claims made in the video so later stages stay consistent.
10. Ask whether to delete the rejected Figma page `40000013:429295`.
11. Commit this session's files once Manel approves (separate from Mapon work).

## Open questions

- **Second visual example.** Candidates already discussed, from the register:
  - Remu, the Remuner AI agent chat panel (visual and conversation design, structured tables and lists, launched to all customers before March 2026; frames in "Remuner | Dashboard (IC)", page `0925 -> Remu refinement`). No bad "before". Already the portfolio AI case.
  - Kymco e-bikes (Kings of Mambo): consumer retail commerce, full design and front end, checkout took real orders. Closest to Tim's "B2C retail feel"; older, a website, not a DS component. Sketch files imported into Figma (see memory "KoM archive").
  - Remuner component states for accessibility: focus, error and context states that don't rely on colour alone, some readable by screen readers. Matches Tim's accessibility gap. No frames recorded yet.
  - Menu animations and mobile screen transitions: Manel told Tim about them on the call. Unconfirmed: project, file, owner unknown. Question asked, not answered: which product, and does a file, prototype or recording exist?
  - Generic types Manel liked, to check against his libraries: button state set (hover, pressed, focus ring, loading keeps width); form field (label, focus, error with icon and text, validation on blur); select/combobox/menu (open motion, keyboard highlight, groups, search); toast (enter/exit, stacking, undo, auto-dismiss); modal/drawer/sheet; tabs with sliding indicator; skeleton loading; empty states; cards (hierarchy, image ratio, hover lift); charts (accessible palette, tooltips, update motion); status chips (colour plus icon or text); date/range picker; toggle/checkbox micro-interactions; one component in light and dark via tokens.
  - What makes one convincing for Tim: an acceptable "before" (so the gain is judgement), named decisions, accessibility built in, how it entered the system, a reference point (Tim plans to compare Suitcase with high-quality retail platforms).
- Does the video keep two examples, or table selection plus a static image for the second? Manel hasn't said.
- Where is the video hosted (YouTube unlisted, Loom, or a `noindex` page on manel-leiva.com as an earlier TODO plan said)? Not decided.
- Delete the Figma click-through page or keep it?

## How to verify

- Open the rebuild: `open interviews/perk/perk-table-selection-rebuild.html` (drag and drop: add `#dnd` in the browser URL, or use the toggle).
- Headless check (the scratchpad copy of node_modules will be gone):
  - `mkdir -p /tmp/pwcheck && cd /tmp/pwcheck && npm init -y && npm i playwright-core@1.56.1`
  - `cp ~/Dev/job-search/scripts/table-rebuild-check/*.js . && mkdir -p shots && node shot.js && node dnd.js`
  - `dnd.js` prints `errors: []` when the page has no console errors. PNGs land in `/tmp/pwcheck/shots/`. Chromium path is hardcoded to `~/Library/Caches/ms-playwright/chromium_headless_shell-1248/`.
- `python3 scripts/check-links.py` after editing Markdown (last run: 0 broken).
- `grep -n "—\|–" interviews/perk/perk-followup-video-script.md outreach/perk-tim-mateo-followup-2026-11-18.md` should print nothing.
- Figma: `figma_list_open_files`, then `figma_navigate` with `lock: true` on `H7KF9JPK3wwFGd8333TaHT` before any capture. Keep one to three files open.
