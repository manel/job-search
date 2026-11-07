# TODO

Open items that aren't tracked elsewhere. Rebuilt 2026-10-14 during the career-os merge; the July version (full search diagnosis and DS-case work log) is at commit `83bef9f`.

Where else work is tracked:
- **Pipeline and follow-ups:** `applications/active.md` and the `next_action_on` field of each record in `applications/records/`. A SessionStart hook surfaces overdue dates; don't duplicate them here.
- **CV template, portfolio and interview-deck improvements:** `context/application-assets-rework.md`.

The hook also surfaces open items in "This week" at every session start. Keep it to current priorities and remove items when done.

---

## This week

- [x] **Wizeline UX interview held 30 Oct.** Debrief in `interviews/wizeline/wizeline.md`. No whiteboard; the canvas sub-tasks are moot.
- [x] **Wizeline UX interview passed 2 Nov** at Level 4 (David Ho email).
- [ ] **Wizeline client interview Tue 10 Nov, 17:30-18:30.** Brief done 6 Nov (Round 3 in `interviews/wizeline/wizeline.md`; panel includes Forest Evashevski, Director, Experience Design, WSJ). Still to do before Tuesday:
  - Build the closing "what I bring" slide in the Remuner deck (Figma "Remuner DS"), after slide 10 (Handover). Three anchors from the brief: vLex client DS work and coaching about 15 designers; working inside a shared system across teams (Abacum five squads, Remuner governance loop); closing the gap to code (tokens repo, reviewed PRs, studio front-end). Plus one plan line for the first months. Update `interviews/wizeline/ux-interview-deck.md` with the slide's talk track.
  - Rehearse "why WSJ" from the brief's anchors: "work on" or "contribute to" Index, not "manage"; one sentence on readers or surfaces; multi-brand follow-up ready.
  - Rehearse the outcome answer before Forest asks (10 of 18 screens, CTO quote, no product metric, what you'd measure now).
  - Optional: identify the opisnet.com organizer.

- [x] **Remuner DS case additions: applied and pushed 2026-10-30 (portfolio 8c6ffdb).** Drafts in `context/remuner-case-additions-2026-10-20.md` (palette HSL normalisation and WCAG AA, own front-end PRs, Figma MCP with Storybook views, stack row). Manel to approve the wording and say whether a palette visual exists; then edit the case in `portfolio/`, commit there, update the pointer, and ask before pushing.
- [ ] **LinkedIn Abacum entry (deferred 2026-10-30).** Add the Abax outcome (about 47% of component uses at departure, against an 80% goal) and apply the co-led wording from `context/linkedin.md`; Manel pastes it live, then update that file.

- [ ] **Abacum front-end PRs: details for the Abax case.** Recorded as a plain fact 2026-10-20. Ask Manel: part of the MUI-to-Abax migration or general cleanup; roughly how many; reviewed and merged by engineers; any AI tools. Then decide whether it goes into "Making adoption stick" in `portfolio/public/cases/design-systems.html`.

- [x] **Push `portfolio/` and commit the pointer.** Pushed 2026-11-07 (portfolio `221911e`); pointer committed.
- [ ] **Abacum deck v2 (Figma "Abacum DS", top row), before the Perk Depth of Expertise call.** Built 2026-11-06; source `interviews/decks/case-deck-design-systems-abacum.md`.
  - Play it once in presentation mode: the Smart Animate builds (slides 2, 3, 8, 9, 10, 12) are untested.
  - Slide 6 Roadmap screenshot shows the Vision 1.0 line "80% of new UI" and colleagues' full names in the owner column. Crop it to "How to get there" or replace it.
  - Screenshots to `interviews/decks/assets/abacum/`: inconsistent buttons, cells and menus before Abax (slide 2); Abax Select, Menu and Menu item (slide 10, now a recreation). Then swap them in.
  - Delete the two old skipped rows once v2 is approved.

- [ ] **Decide Stripe DS and Bunge.** Stripe Product Designer Design Systems: 36 days silent, posting open, past the 5-week stale line. Bunge: `applied` 104 days, posting status unknown; likely stale.
- [ ] **Haddock review (due 3 Nov).** Posting still open on 3 Nov, process on hold since 9 Oct; the 12 Oct reply to Ingrid is unconfirmed as sent. Decide on a short follow-up.
- [ ] **Assess the 15 role leads from the 3 Nov scan** marked `initial_fit: not assessed` in `sourcing/role-leads.csv` (the other 9 are already skipped). Overdue follow-ups outrank them.

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

- [ ] **Outcome up front in every case (raised 2026-11-05, from a hiring-manager LinkedIn post on Senior and Staff portfolios).** Outcomes now sit at the end or mid-case with no heading: in `ai-agent.html` the reach line is the last lead paragraph; in `design-systems.html` the ~47% figure sits inside "Building the case". Add a short fact line under each case title (role, scope, outcome) using only figures already in `context/portfolio.md` and `evidence/experience-facts.md`; no rewrite of the narrative. Cases: the five linked ones (Reps Letter stays hidden).

- [ ] **Reflection close in every case (raised 2026-11-05, same source).** No case has a reflection or lesson heading, against Staff checklist point 7 in `context/portfolio.md` (closing meta-lesson naming the trade-off). First check whether each case's closing paragraph already carries one; add a short closing section only where it doesn't. Run `no-ai-slop` and `anthropic-skills:humanizer` on any new copy. Related: the two DS cases run about 1,950 and 2,000 words; consider trimming in the same pass.

## Design-systems lane review

Raised 2026-10-26 after the Perk DS rejection at CV review (zero interviews from DS-titled roles at product companies; see memory.md 2026-10-26). The gaps below are inference, not employer feedback. Do this before the next DS-titled application, or once Stripe DS resolves. OLX Otodom (Oct) resolved 2026-10-29: rejected at CV review again. Perk reversed its rejection on 2026-11-02 with a TA call invite after Tanna's referral, so the Perk data point now argues for referrals, not against the DS CV.

- [ ] **DS reads as secondary on the CV.** Both titles are Senior Product Designer and the Abacum entry opens on Integrations and Engine. Reorder bullets in the DS CV so system work leads; keep the scope paragraphs.
- [ ] **Accessibility nearly absent.** Add the Remuner palette line (HSL normalisation, in-use colours to WCAG AA) once the case-additions draft is approved. Keyboard and screen-reader work stays unclaimed.
- [ ] **No visual foundations evidence.** The CV is all architecture and tooling. Check what else is claimable (type scale, iconography, motion) in `evidence/experience-facts.md`; ask Manel, don't invent.
- [ ] **Scale and native mobile.** Largest system served five squads; mobile is the Remuner webview. Not fixable by writing: decide whether to keep applying to large multi-platform DS teams (Perk, OLX, Bitpanda, Hostaway shape) or retarget to web-first B2B SaaS where one senior PD builds and runs the system. Record the decision in `context/target-roles.md`.
- [ ] **Smaller factors to check:** the visible gap since March 2026; React expectations in DS JDs (production React not claimable).
- [ ] **Real signal:** Perk reopened 2026-11-02 (TA call invite) and Manel passed the TA screen 2026-11-05. Ask Clare or Tanna what moved the CV after the template rejection (`applications/records/perk-senior-design-systems-designer.md`).

## Interview prep (yours to write)

- [ ] The 5 remaining `[NEEDS YOUR STORY]` gaps in `interviews/prep.md`. Check `interviews/behavioral-battle-cards.md` first; some may already be covered there.
- [ ] **AI agent case deck** (`interviews/decks/case-deck-ai-agent.md`): speaker notes and slide structure are written, but the visuals per slide (flow diagram, annotated conversation screenshot, reach diagram, cycle diagram, outcome cards) still need building or copying from the live portfolio case. Parked 2026-07-24; pick up when a process reaches a case-presentation round. Decide the output form first.

## Records hygiene

- [ ] Applications sent before July 2026 have PDFs in `cv-pdf-to-send/` but no plain-text sources in `cv/roles/` or `cover-letters/roles/`. Decide: backfill from the PDFs (plus chat history around each send date), or accept the PDFs as the only record. Factorial IT spinoff was backfilled 2026-07-15.
- [ ] Keep `application_channel`, `role_lane` and the first-contact date (in History) on every new record; the response-time analysis depends on them. Invite dates are missing for Spendesk and Secfix; applied dates for Secfix, Valeria, Tabby, Murphy, Deel Staff and Pilar. New conversations also need an entry in `FIRST_RESPONSE` and, when lost, `LOST_AT` in `scripts/analyze-response-times.py`.
- [ ] Start using Linear actively; it unblocks the deferred Linear application (see `applications/archive-2026-07.md`).

## Parked (decided, no action now)

- Rep Letters case: stays hidden. Decide when there's slack.
- Salary benchmarks for Staff/Lead scope: add only if a live process reaches compensation talks.
