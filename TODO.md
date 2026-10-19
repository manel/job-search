# TODO

Open items that aren't tracked elsewhere. Rebuilt 2026-10-14 during the career-os merge; the July version (full search diagnosis and DS-case work log) is at commit `83bef9f`.

Where else work is tracked:
- **Pipeline and follow-ups:** `applications/active.md` and the `next_action_on` field of each record in `applications/records/`. A SessionStart hook surfaces overdue dates; don't duplicate them here.
- **CV template, portfolio and interview-deck improvements:** `context/application-assets-rework.md`.

The hook also surfaces open items in "This week" at every session start. Keep it to current priorities and remove items when done.

---

## This week

- [ ] **Tue 2026-10-20: fix the Figma CV and letter template** before the next PDF export. Text from exports since 2026-10-13 extracts split ("wit h", "t he", "mont hly", "librar y"): the Flodesk, Learnwise and OLX Otodom DS CVs and letters, and the OLX PD letter. Older template (Deel CV) extracted its headings as single letters (`S U M M A R Y`); check the current template's headings too. Likely cause, not confirmed: ligatures, letter spacing or kerning. Change one setting, re-export a test page, run `python3 scripts/check-pdf-text.py <pdf>` until it passes. From then on, run the check on every PDF before sending. Never regenerate PDFs that were already sent.

- [ ] **Tue 2026-10-20: reconcile the Perk (DS) CV before sending.** The PDF in `cv-pdf-to-send/Perk (DS)/` extracts clean but differs from `cv/roles/perk-senior-design-systems-designer.md`: the PDF has no case-study link line in the summary (breaks the one-case-link rule), says "Barcelona, hybrid" where the source says "Barcelona (Remote)", and words the summary and audit bullet differently. Decide which is correct, fix the other, then re-run `python3 scripts/check-pdf-text.py "cv-pdf-to-send/Perk (DS)/Manel Leiva CV 2026.pdf" --source cv/roles/perk-senior-design-systems-designer.md`.

- [ ] **Tue 2026-10-20: portfolio PDF text.** The Flodesk portfolio PDF has no extractable email. Make sure the planned portfolio PDF (Portfolio section below) carries contact details as real text.

- [ ] **Tue 2026-10-20:** prepare one concrete example each for Figma MCP work: accessibility audit (which components or colours, what failed, what changed), design-code parity check (which component, which options differed), and two-way token sync (what drifted, how it was caught). Needed before any design-systems interview (Perk, Flodesk, OLX Otodom) and for the Remuner case update. Record them in `evidence/experience-facts.md`.

## Portfolio

- [ ] **Portfolio PDF (5-8 pages)** for upload-only portfolio fields (Flodesk's Greenhouse form accepted only a file, 2026-10-19). Key visuals from the design-systems, Remuner system, Dataset Manager and AI agent cases, each with a clickable link; add Kymco modular blocks or other studio web work if presentable (web-craft roles). Reusable across applications. For Flodesk, a one-page case-card PDF was used as a stopgap.

- [ ] Add Figma MCP use to the Remuner design-system case: one umbrella line (Manel does not want the full list), covering token sync with code, accessibility and parity checks, and documentation, mostly at Remuner. Needs one concrete example from Manel before writing case copy. Full list in `evidence/experience-facts.md` (2026-10-19).

## Interview prep (yours to write)

- [ ] The 5 remaining `[NEEDS YOUR STORY]` gaps in `interviews/prep.md`. Check `interviews/behavioral-battle-cards.md` first; some may already be covered there.
- [ ] **AI agent case deck** (`interviews/decks/case-deck-ai-agent.md`): speaker notes and slide structure are written, but the visuals per slide (flow diagram, annotated conversation screenshot, reach diagram, cycle diagram, outcome cards) still need building or copying from the live portfolio case. Parked 2026-07-24; pick up when a process reaches a case-presentation round. Decide the output form first.

## Records hygiene

- [ ] Applications sent before July 2026 have PDFs in `cv-pdf-to-send/` but no plain-text sources in `cv/roles/` or `cover-letters/roles/`. Decide: backfill from the PDFs (plus chat history around each send date), or accept the PDFs as the only record. Factorial IT spinoff was backfilled 2026-07-15.
- [ ] Start using Linear actively; it unblocks the deferred Linear application (see `applications/archive-2026-07.md`).

## Parked (decided, no action now)

- Rep Letters case: stays hidden. Decide when there's slack.
- Salary benchmarks for Staff/Lead scope: add only if a live process reaches compensation talks.
