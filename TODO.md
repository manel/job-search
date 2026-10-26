# TODO

Open items that aren't tracked elsewhere. Rebuilt 2026-10-14 during the career-os merge; the July version (full search diagnosis and DS-case work log) is at commit `83bef9f`.

Where else work is tracked:
- **Pipeline and follow-ups:** `applications/active.md` and the `next_action_on` field of each record in `applications/records/`. A SessionStart hook surfaces overdue dates; don't duplicate them here.
- **CV template, portfolio and interview-deck improvements:** `context/application-assets-rework.md`.

The hook also surfaces open items in "This week" at every session start. Keep it to current priorities and remove items when done.

---

## This week

- [ ] **Wizeline UX interview, Fri 30 Oct 17:00: build the deck and canvas by Tue 27 Oct.** Brief done: `interviews/wizeline/wizeline.md`, Round 2. To do: cut `interviews/decks/case-deck-design-systems-remuner.md` to seven slides, adding the WCAG AA palette slide. Manel to supply: one feature that shipped faster because a component existed; a palette before/after or contrast visual from Figma; confirmation on LinkedIn that both interviewers work at Wizeline. The palette visual also unblocks the Remuner case additions below.
  - [ ] Reply-all to David Ho's 23 Oct email: confirm the slot and say the whiteboard will be in a Figma file (decided 2026-10-24 over FigJam: DS panel, likely component or token prompt, shows tool fluency and covers multi-brand live). If they name another tool, rework the canvas plan.
  - [ ] Build the whiteboard Figma Design file: empty framing sections (problem, constraints, users and consumers, options, decision, open questions).
  - [ ] Add a sticky-note component and a connector style to it, so rough capture is as fast as FigJam.
  - [ ] Add a starter kit: primitive and semantic token collection with two brand modes, plus two or three base components (button, input).
  - [ ] Run one mock DS prompt in the file against a 25-minute timer; tighten the setup if FigJam habits slow you down.
  - [ ] Test screen-sharing the Figma file in Google Meet.
  - [ ] Update the Round 2 canvas plan in `interviews/wizeline/wizeline.md` and the record's `next_action` from FigJam to Figma.

- [ ] **Remuner DS case additions: approve and apply.** Drafts in `context/remuner-case-additions-2026-10-20.md` (palette HSL normalisation and WCAG AA, own front-end PRs, Figma MCP with Storybook views, stack row). Manel to approve the wording and say whether a palette visual exists; then edit the case in `portfolio/`, commit there, update the pointer, and ask before pushing.

- [ ] **Abacum front-end PRs: details for the Abax case.** Recorded as a plain fact 2026-10-20. Ask Manel: part of the MUI-to-Abax migration or general cleanup; roughly how many; reviewed and merged by engineers; any AI tools. Then decide whether it goes into "Making adoption stick" in `portfolio/public/cases/design-systems.html`.

- [ ] **Senovo questions to Menna** and the overdue follow-ups (`/follow-up`). Babel email to Mauro dropped: Babel rejected 2026-10-22.

- [ ] **Portfolio PDF text.** The Flodesk portfolio PDF has no extractable email (underlined links, see memory.md 2026-10-20). The planned portfolio PDF (Portfolio section below) must carry contact details as real text: no underlined text, then run the PDF check.

## Portfolio

- [ ] **Portfolio PDF (5-8 pages)** for upload-only portfolio fields (Flodesk's Greenhouse form accepted only a file, 2026-10-19). Key visuals from the design-systems, Remuner system, Dataset Manager and AI agent cases, each with a clickable link; add Kymco modular blocks or other studio web work if presentable (web-craft roles). Reusable across applications. For Flodesk, a one-page case-card PDF was used as a stopgap.

- [ ] Add Figma MCP use to the Remuner design-system case: one umbrella line (Manel does not want the full list), covering token sync with code, accessibility and parity checks, and documentation, mostly at Remuner. Examples recorded in `evidence/experience-facts.md` on 2026-10-20 (palette HSL normalisation and AA contrast, shipped via the tokens repo; component parity; Storybook views and docs; hardcoded-colour PRs). Full list in `evidence/experience-facts.md` (2026-10-19).

- [ ] **Case visual rework, modelled on spidleweb.net (raised 2026-10-26).** Reference and analysis in `context/portfolio.md` ("Reference portfolios"). Goal: each case gets a proof layer of 8 or so large figures, mostly looping recordings, each with a readable one-sentence caption (behaviour plus reason, realistic domain data). Keep the judgment narrative; the media supplements it. Pilot on one case before touching the rest.
  - [ ] Pilot case: Dataset Manager. Run the Abacum front end locally with seeded fake finance data (Manel has the Figma files and FE/BE code); list the 8 flows worth recording.
  - [ ] Record the clips (muted loop, poster frame). No real customer data in any frame; screens only, never code.
  - [ ] Write the captions; run `no-ai-slop` and `anthropic-skills:humanizer`. Add a user-terms subtitle ("Finance teams can…") and a one-line note that the data is illustrative.
  - [ ] Layout in `portfolio/public/css/case.css`: captions from 12px at 55% opacity to body size; media column uninterrupted by long prose; check against `context/brand.md` first.
  - [ ] Review the pilot with `/review-case dataset-manager`, then decide on Modeling Syntax, AI agent and the two DS cases (the Storybook recording already covers part of the DS proof).

## Interview prep (yours to write)

- [ ] The 5 remaining `[NEEDS YOUR STORY]` gaps in `interviews/prep.md`. Check `interviews/behavioral-battle-cards.md` first; some may already be covered there.
- [ ] **AI agent case deck** (`interviews/decks/case-deck-ai-agent.md`): speaker notes and slide structure are written, but the visuals per slide (flow diagram, annotated conversation screenshot, reach diagram, cycle diagram, outcome cards) still need building or copying from the live portfolio case. Parked 2026-07-24; pick up when a process reaches a case-presentation round. Decide the output form first.

## Records hygiene

- [ ] Applications sent before July 2026 have PDFs in `cv-pdf-to-send/` but no plain-text sources in `cv/roles/` or `cover-letters/roles/`. Decide: backfill from the PDFs (plus chat history around each send date), or accept the PDFs as the only record. Factorial IT spinoff was backfilled 2026-07-15.
- [ ] Start using Linear actively; it unblocks the deferred Linear application (see `applications/archive-2026-07.md`).

## Parked (decided, no action now)

- Rep Letters case: stays hidden. Decide when there's slack.
- Salary benchmarks for Staff/Lead scope: add only if a live process reaches compensation talks.
