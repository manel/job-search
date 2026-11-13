# TODO

Open items that aren't tracked elsewhere. Rebuilt 2026-10-14 during the career-os merge; the July version (full search diagnosis and DS-case work log) is at commit `83bef9f`.

Where else work is tracked:
- **Pipeline and follow-ups:** [applications/active.md](applications/active.md) and the `next_action_on` field of each record in `applications/records/`. A SessionStart hook surfaces overdue dates; don't duplicate them here.
- **CV template, portfolio and interview-deck improvements:** [context/application-assets-rework.md](context/application-assets-rework.md).

The hook also surfaces open items in "This week" at every session start. Keep it to current priorities and remove items when done.

---

## This week

- [ ] **Mon 16 Nov: answer Capitole (Araceli Massieu) on EUR 40K.** Call held 13 Nov; client revealed at the next interview. Record: [applications/records/capitole-senior-ai-product-designer-insurance.md](applications/records/capitole-senior-ai-product-designer-insurance.md).
- [x] **Wizeline UX interview held 30 Oct.** Debrief in [interviews/wizeline/wizeline-stage2-case.md](interviews/wizeline/wizeline-stage2-case.md). No whiteboard; the canvas sub-tasks are moot.
- [x] **Wizeline UX interview passed 2 Nov** at Level 4 (David Ho email).
- [ ] **Wizeline client interview: on hold.** The Fri 13 Nov slot was cancelled on 12 Nov (the 10 Nov one was too): the client is clarifying the role, and David Ho expects news the week of 16 Nov. Check in with him Fri 20 Nov if silent. Brief done 6 Nov, refreshed 12 Nov ([interviews/wizeline/wizeline-stage3-client.md](interviews/wizeline/wizeline-stage3-client.md); panel includes Forest Evashevski, Director, Experience Design, WSJ). The sub-tasks below wait until a new date is set:
  - Check the speaker notes on Remuner deck slides 1 and 13b (flagged for a re-paste) and look up Cristian Rodriguez, the new Wizeline guest.
  - [x] "What I bring" (Figma 20) and "Thank you" (Figma 21) slides built 2026-11-07 after Handover; talk track and notes in [interviews/wizeline/wizeline-case-deck.md](interviews/wizeline/wizeline-case-deck.md). Speaker notes pasted 2026-11-08, including slide 13b (Select anatomy, kept as the vector drawing, dissolve transition).
  - Rehearse "why WSJ" from the brief's anchors: "work on" or "contribute to" Index, not "manage"; one sentence on readers or surfaces; multi-brand follow-up ready.
  - Rehearse the outcome answer before Forest asks (10 of 18 screens, CTO quote, no product metric, what you'd measure now).
  - [x] Organizer identified 2026-11-10: Esteban Gabriel Abete, EMEA Delivery Director, Wizeline.
  - Highlights file ("Manel Leiva Portfolio Highlights"): script updated 2026-11-09 ([interviews/wizeline/wizeline-stage3-client-portfolio.md](interviews/wizeline/wizeline-stage3-client-portfolio.md): FP&A specialists then customers; 15 of 37 functions, the four-competitor benchmark, one engineer; parameter preview). Read it through once. Checked 2026-11-09: frame text clean; Dataset Manager AFTER image replaced (it showed a real customer's name) with column settings and auto-map, "Abacum | Dataset manager - Implementation" `2813:116108`, matching the script. Modeling Syntax AFTER image is the 2023 chips step; the script now says so. Prototype flow "Highlights" added 2026-11-10 (AI Agent → Dataset Manager → Modeling Syntax, click or right arrow, 0.3s dissolve), so Present opens fullscreen.

- [x] **Remuner DS case additions: applied and pushed 2026-10-30 (portfolio 8c6ffdb).** Drafts in [context/remuner-case-additions-2026-10-20.md](context/remuner-case-additions-2026-10-20.md) (palette HSL normalisation and WCAG AA, own front-end PRs, Figma MCP with Storybook views, stack row). Manel to approve the wording and say whether a palette visual exists; then edit the case in `portfolio/`, commit there, update the pointer, and ask before pushing.
- [x] **LinkedIn Abacum entry.** Abax outcome and MUI-to-Abax PR lines live 2026-11-07; Kings of Mambo title corrected to Co-founder. [context/linkedin.md](context/linkedin.md) updated.

- [x] **Abacum front-end PRs in the Abax case.** Live 2026-11-07 (portfolio `0ec2eaf`): PR and Abax import-lint sentences in the migration paragraph; hex outcome bullet now says "fewer".

- [x] **Push `portfolio/` and commit the pointer.** Pushed 2026-11-07 (portfolio `221911e`); pointer committed.
- [ ] **Abacum deck v2 (Figma "Abacum DS", top row), before the Perk Hiring Manager Interview (Tim Archer, Tue 17 Nov, 10:00).** Built 2026-11-06; source [decks/case-deck-design-systems-abacum.md](decks/case-deck-design-systems-abacum.md).
  - Play it once in presentation mode: the Smart Animate builds (slides 2, 3, 8, 9, 10, 12) are untested.
  - [x] Slide 6 Roadmap screenshot cropped 2026-11-08 (clip frame "Roadmap crop"): starts at "How to get there", Owner column removed. The paragraph text is cut at the right edge.
  - [x] Speaker notes for all 34 Figma slides pasted 2026-11-08. Re-paste slides 1, 9, 23, 29 and 32 after the humanizer pass (also Remuner slides 1 and 13b).
  - Screenshots to `decks/assets/abacum/`: inconsistent buttons, cells and menus before Abax (slide 2); Abax Select, Menu and Menu item (slide 10, now a recreation). Then swap them in.
  - Delete the two old skipped rows once v2 is approved.

- [ ] **Dataset Manager deck v2 (Figma "Dataset manager", top row).** Built 2026-11-09; source `decks/case-deck-dataset-manager.md`.
  - Paste the 14 speaker notes from the source ("Speaker notes to paste into Figma").
  - Play the slide 5 build in presentation mode; check the slide 4 scope crop and the teal strip on slide 9.
  - Delete the skipped v1 row once v2 is approved.
  - Re-paste speaker notes Figma 5 to 8, 11 and 13: the source changed 2026-11-09 (first test round was our FP&A specialists, then customers; autonomy-metric "Next time"). On-slide text already updated.

- [ ] **Tomorrow, 10 Nov: finish the Notion-driven deck updates** (backlog and status in [evidence/notion/deck-and-case-updates.md](evidence/notion/deck-and-case-updates.md); index in [evidence/notion/README.md](evidence/notion/README.md)).
  - **Modeling Syntax deck (Figma "Modeling syntax", built 2026-11-09, 10 slides + skipped B1):** paste the speaker notes from [decks/case-deck-modeling-syntax.md](decks/case-deck-modeling-syntax.md) (slides 1 and 3 changed 2026-11-12: Manel wrote Improve Syntax Usability, "nobody had ticketed this problem" restored); play it once; decide whether slide 5 gets the planned build (benchmark, then quote).
  - **Abacum DS deck:** re-paste speaker notes Figma 11, 12, 16, 24 and 30 (nine weeks, tokens already in production, sync since July 2022 for almost two years; 24: "I ran the Figma one every two weeks"). Backup B3 built 2026-11-12 (skipped, after B2); check it once in presentation view.
  - **Live cases (portfolio submodule):** check /cases/dataset-manager for "three customers" or customer-only testing; /cases/modeling-syntax for "nobody had ticketed" or "no ticket"; /cases/design-systems for "quarterly", "eight months" and "one week". Add the benchmark table and customer-call fragments to the syntax case, and the groundwork timeline to the DS case, if they fit.
  - **Open question:** Dataset Manager slide 2 says the squad's engineers configured each dataset; Notion (August 2022) says our FP&A team created customers' connections and datasets in the back office. Confirm who did what before changing the slide.
  - **Commit** the Notion index, register, deck sources and notes changes from 2026-11-09 (nothing committed yet).

- [ ] **Decide Stripe DS and Bunge.** Stripe Product Designer Design Systems: 36 days silent, posting open, past the 5-week stale line. Bunge: `applied` 104 days, posting status unknown; likely stale.
- [ ] **Haddock review (due 3 Nov).** Posting still open on 3 Nov, process on hold since 9 Oct; the 12 Oct reply to Ingrid is unconfirmed as sent. Decide on a short follow-up.
- [x] **Assess the 15 role leads from the 3 Nov scan** (done 2026-11-07, together with the 4 Nov manual leads: 6 proceed, 2 defer, 12 skip, 2 closed; see [applications/active.md](applications/active.md)). New queue: 011h and the Spendesk message to Cyrièle by 9 Nov, Exoticca 10 Nov, Canonical DS 11 Nov, Fever and The Knot (base CV) 12 Nov.

- [ ] **Overdue follow-ups** (`/follow-up`). 12 Nov: Haddock nudged, Spendesk moved to 18 Nov, Qonto closed, Senovo skipped. Babel email to Mauro dropped: Babel rejected 2026-10-22.

- [ ] **Portfolio PDF text.** The Flodesk portfolio PDF has no extractable email (underlined links, see memory.md 2026-10-20). The planned portfolio PDF (Portfolio section below) must carry contact details as real text: no underlined text, then run the PDF check.

## Portfolio

- [ ] **Portfolio PDF (5-8 pages)** for upload-only portfolio fields (Flodesk's Greenhouse form accepted only a file, 2026-10-19). Key visuals from the design-systems, Remuner system, Dataset Manager and AI agent cases, each with a clickable link; add Kymco modular blocks or other studio web work if presentable (web-craft roles). Reusable across applications. For Flodesk, a one-page case-card PDF was used as a stopgap.

- [ ] Add Figma MCP use to the Remuner design-system case: one umbrella line (Manel does not want the full list), covering token sync with code, accessibility and parity checks, and documentation, mostly at Remuner. Examples recorded in [evidence/experience-facts.md](evidence/experience-facts.md) on 2026-10-20 (palette HSL normalisation and AA contrast, shipped via the tokens repo; component parity; Storybook views and docs; hardcoded-colour PRs). Full list in [evidence/experience-facts.md](evidence/experience-facts.md) (2026-10-19).

- [ ] **Case visual rework, modelled on spidleweb.net (raised 2026-10-26).** Reference and analysis in [context/portfolio.md](context/portfolio.md) ("Reference portfolios"). Goal: each case gets a proof layer of 8 or so large figures, mostly looping recordings, each with a readable one-sentence caption (behaviour plus reason, realistic domain data). Keep the judgment narrative; the media supplements it. Pilot on one case before touching the rest.
  - [ ] Pilot case: Dataset Manager. Run the Abacum front end locally with seeded fake finance data (Manel has the Figma files and FE/BE code); list the 8 flows worth recording.
  - [ ] Record the clips (muted loop, poster frame). No real customer data in any frame; screens only, never code.
  - [ ] Write the captions; run `no-ai-slop` and `anthropic-skills:humanizer`. Add a user-terms subtitle ("Finance teams can…") and a one-line note that the data is illustrative.
  - [ ] Layout in [portfolio/public/css/case.css](portfolio/public/css/case.css): captions from 12px at 55% opacity to body size; media column uninterrupted by long prose; check against [context/brand.md](context/brand.md) first.
  - [ ] Review the pilot with `/review-case dataset-manager`, then decide on Modeling Syntax, AI agent and the two DS cases (the Storybook recording already covers part of the DS proof).

- [x] **Case edits of 2026-11-09, pushed (portfolio `9a83428`).** Dataset Manager: SQL-like chronology, scope section (three jobs, "self-service means activation", mapping first), dependencies section, link to Modeling Syntax, support line attributed to Manel's own check. Abacum DS: about six designers, adoption-as-teaching paragraph. Modeling Syntax: three contrast sentences rewritten, "implementation support", suggestions dated and linked to Dataset Manager. Remuner DS: SimpleLocalize line.
- [ ] **Deck and live-case updates from the Figma audit (raised 2026-11-09).** Ranked backlog with node links and boundaries in [evidence/figma/deck-and-case-updates.md](evidence/figma/deck-and-case-updates.md). Do item 1 (token audit in the Abacum DS deck) before the Perk Depth of Expertise call.
- [ ] **Analyze the Abacum Notion export (raised 2026-11-09).** `/Users/manel/Desktop/Abacum (Notion)`: 4.6 GB, 7,751 files (5,134 HTML pages, 330 CSV databases, about 2,000 images, 58 videos). Start a new session. Scripted inventory first (titles, dates, authors, folders, databases), then read pages on Dataset Manager, the modeling language, dimensions and mappings, Abax, research and team process. Cross-check against [evidence/experience-facts.md](evidence/experience-facts.md), [context/design-systems-notes.md](context/design-systems-notes.md) and [evidence/figma/README.md](evidence/figma/README.md). Report new claimable facts, contradictions and gaps (look for the Modeling Syntax benchmark table and customer-call evidence, missing from Figma). Write to `evidence/notion/`. Skip videos.
- [ ] **Dataset Manager case images (raised 2026-11-09).** PNGs for most of these frames are already exported in `evidence/figma/images/` (see [evidence/figma/images/README.md](evidence/figma/images/README.md)). The new Scope and Guardrails sections have no figures. Export from the frames in [evidence/abacum-figma-index.md](evidence/abacum-figma-index.md) ("Best images for the story"): HMW notes, architecture board, 2022 SQL-like transform field, column settings, "used in" dialog, impact warning, formula box with library. Check every frame for real customer data and colleague names first (the scope-list crop shows one). Save to `portfolio/public/assets/images/`.
- [ ] **Remuner IC dashboard as a case (raised 2026-11-09).** Candidate to replace the hidden Reps Letter case. Evidence in [evidence/experience-facts.md](evidence/experience-facts.md) ("IC dashboard: clarifying vague feedback"): vague "not intuitive" feedback, interviews with the users who gave it, plan-calculation dialog, period selector and payout timing, fewer clicks and fewer plan-view visits seen in the internal analytics dashboard. Figma file "Remuner | Dashboard (IC)". New evidence from the 2026-11-09 audit: the June 2025 dashboard adoption research and the late-2025 "My plans" rep interviews (item 7 in [evidence/figma/deck-and-case-updates.md](evidence/figma/deck-and-case-updates.md)). Run the fit against [context/portfolio.md](context/portfolio.md) signals and `/review-case` before building.
- [ ] **Outcome up front in every case (raised 2026-11-05, from a hiring-manager LinkedIn post on Senior and Staff portfolios).** Outcomes now sit at the end or mid-case with no heading: in `ai-agent.html` the reach line is the last lead paragraph; in `design-systems.html` the ~47% figure sits inside "Building the case". Add a short fact line under each case title (role, scope, outcome) using only figures already in [context/portfolio.md](context/portfolio.md) and [evidence/experience-facts.md](evidence/experience-facts.md); no rewrite of the narrative. Cases: the five linked ones (Reps Letter stays hidden).

- [ ] **Reflection close in every case (raised 2026-11-05, same source).** No case has a reflection or lesson heading, against Staff checklist point 7 in [context/portfolio.md](context/portfolio.md) (closing meta-lesson naming the trade-off). First check whether each case's closing paragraph already carries one; add a short closing section only where it doesn't. Run `no-ai-slop` and `anthropic-skills:humanizer` on any new copy. Related: the two DS cases run about 1,950 and 2,000 words; consider trimming in the same pass.

## Design-systems lane review

Raised 2026-10-26 after the Perk DS rejection at CV review (zero interviews from DS-titled roles at product companies; see memory.md 2026-10-26). The gaps below are inference, not employer feedback. Do this before the next DS-titled application, or once Stripe DS resolves. OLX Otodom (Oct) resolved 2026-10-29: rejected at CV review again. Perk reversed its rejection on 2026-11-02 with a TA call invite after Tanna's referral, so the Perk data point now argues for referrals, not against the DS CV.

- [ ] **DS reads as secondary on the CV.** Both titles are Senior Product Designer and the Abacum entry opens on Integrations and Engine. Reorder bullets in the DS CV so system work leads; keep the scope paragraphs.
- [ ] **Accessibility nearly absent.** Add the Remuner palette line (HSL normalisation, in-use colours to WCAG AA) once the case-additions draft is approved. Keyboard and screen-reader work stays unclaimed.
- [ ] **No visual foundations evidence.** The CV is all architecture and tooling. Check what else is claimable (type scale, iconography, motion) in [evidence/experience-facts.md](evidence/experience-facts.md); ask Manel, don't invent.
- [ ] **Scale and native mobile.** Largest system served five squads; mobile is the Remuner webview. Not fixable by writing: decide whether to keep applying to large multi-platform DS teams (Perk, OLX, Bitpanda, Hostaway shape) or retarget to web-first B2B SaaS where one senior PD builds and runs the system. Record the decision in [context/target-roles.md](context/target-roles.md).
- [ ] **Smaller factors to check:** the visible gap since March 2026; React expectations in DS JDs (production React not claimable).
- [ ] **Real signal:** Perk reopened 2026-11-02 (TA call invite) and Manel passed the TA screen 2026-11-05. Ask Clare or Tanna what moved the CV after the template rejection ([applications/records/perk-senior-design-systems-designer.md](applications/records/perk-senior-design-systems-designer.md)).

## Interview prep (yours to write)

- [ ] The `[NEEDS YOUR STORY]` gaps, listed in [interviews/stories.md](interviews/stories.md#gaps) and marked in [interviews/question-bank.md](interviews/question-bank.md) (Q10, Q17, enterprise gaps). Battle cards merged into stories.md on 2026-11-12.
- [ ] **Recall sessions** (raised 2026-11-12: targeted questions brought back the Claims-to-Issues rename and the planes fix). 30 to 45 minutes each, one era or project per session, one question at a time, answers logged to [evidence/experience-facts.md](evidence/experience-facts.md) as they come. Order: (1) before Perk Tue 17 Nov, short: one mentoring episode with a result, and vLex scope; (2) after Perk: Kings of Mambo, starting with a year-by-year client and project inventory, then two or three incidents from it (fills the [stories.md gaps](interviews/stories.md#gaps)); (3) Remuner fix-versus-defer and the Q10 manager disagreement. Bring artifacts if you can: old portfolio, archived studio site, Figma or Drive folders, client emails.
- [ ] **Check three claims carried over from the old prep.md** (2026-11-12): "Storybook in Chromatic" (ways-of-working playbook), the Kings of Mambo deadline and lo-fi feedback stories (not in the register), and Q20's "got cross-squad buy-in". Confirm or correct, then update [evidence/experience-facts.md](evidence/experience-facts.md).
- [ ] **AI agent case deck** ([decks/case-deck-ai-agent.md](decks/case-deck-ai-agent.md)): speaker notes and slide structure are written, but the visuals per slide (flow diagram, annotated conversation screenshot, reach diagram, cycle diagram, outcome cards) still need building or copying from the live portfolio case. Parked 2026-07-24; pick up when a process reaches a case-presentation round. Decide the output form first.

## Records hygiene

- [ ] **General Figma index for Abacum and Remuner (raised 2026-11-09, not urgent).** Grow [evidence/abacum-figma-index.md](evidence/abacum-figma-index.md) into one index covering every Abacum and Remuner Figma file (DS, Engine/modeling, AI agent, Remuner product and archive), with page links and a "best images per story" table per case. Seed data: the three `evidence/figma-*-scope-2026-10-06.json` files. Add files as Manel connects them through the Desktop Bridge.

- [ ] Applications sent before July 2026 have PDFs in `cv-pdf-to-send/` but no plain-text sources in `cv/roles/` or `cover-letters/roles/`. Decide: backfill from the PDFs (plus chat history around each send date), or accept the PDFs as the only record. Factorial IT spinoff was backfilled 2026-07-15.
- [ ] Keep `application_channel`, `role_lane` and the first-contact date (in History) on every new record; the response-time analysis depends on them. Invite dates are missing for Spendesk and Secfix; applied dates for Secfix, Valeria, Tabby, Murphy, Deel Staff and Pilar. New conversations also need an entry in `FIRST_RESPONSE` and, when lost, `LOST_AT` in [scripts/analyze-response-times.py](scripts/analyze-response-times.py).
- [ ] Start using Linear actively; it unblocks the deferred Linear application (see [applications/archive-2026-07.md](applications/archive-2026-07.md)).

## Parked (decided, no action now)

- Rep Letters case: stays hidden. Decide when there's slack.
- Salary benchmarks for Staff/Lead scope: add only if a live process reaches compensation talks.
