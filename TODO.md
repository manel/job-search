# TODO

Single list of open items. Snapshot dated 2026-07-02, rebuilt from the full search diagnosis run that day. Pipeline follow-up dates live only in `context/applications.md` (a SessionStart hook surfaces overdue ones automatically); do not duplicate them here. The hook also surfaces the "This week" section below at every session start. Remove items when done.

Diagnosis summary behind this plan (2026-07-02): 7 applications in 6 weeks, 1 screen (Factorial, cold apply, Barcelona-local, reached round 3). Fast rejections were global-remote DS-titled roles, the hardest segment, hit while the Remuner DS case was live with broken images. First-order problems in order: volume collapsed after June 4; portfolio DS evidence missing/broken; segment weighting wrong; AI differentiator invisible.

---

## This week

- [x] **1 + 3. Portfolio: DONE 2026-07-08.** The 3 remaining Remuner images were exported and the case is live on manel-leiva.com with all 5 images (verified same day: main deployed, dev in sync, submodule pointer current). The DS-titled segment is now open.
- [x] **4. BVNK outreach: SENT 2026-07-09.** Connect-note to Anton Yee (Principal PD). Full draft goes out on acceptance; fallback to Nishta Daya 2026-07-16 (tracked in applications.md). Full draft kept here for the acceptance follow-up:
  > Hi Anton, thanks for connecting. I applied for the Lead Design Systems role on June 1 and I'm still interested. I've built two production design systems end to end, most recently at Remuner, where I also owned the token pipeline from Token Studio through Style Dictionary to a published npm package with CI validation. Happy to share more if useful: manel-leiva.com. Best, Manel
- [x] **5. Finom: CLOSED 2026-07-09.** June req delisted unanswered; the replacement Core Product req excludes Spain (application dropdown: Berlin, Italy, Amsterdam, Warsaw, Cyprus). No eligible role, no outreach. Removed from active work.
- [x] **7. Sourcing session: CLOSED 2026-07-10.** The 2026-07-08 sweep's only proceed (Seqera) closed 2026-07-10 on the dev requirement (not claimable honestly; watch seqera.io for designer-titled reqs). The 2026-07-10 manual batch ran 11 assessments: 1 proceed (Datavant HealthSource, gated on genuine-interest call due 2026-07-13) and 10 skips (Preply, JetBrains AIR (location-only; watch for remote/BCN repost), HRS, SocialHub, Vista, Dow Jones (their Senior B2B req worth assessing separately), AirHelp, SlashMobility, Bizneo, Faham, INFINNI). Signal captured in memory.md: 4 JDs in one week name Claude/Cursor as designer qualifications. LinkedIn recommended feed was the weakest channel of the batch.

## Standing strategy (from the diagnosis, until revisited)

- Volume: 3–5 roles assessed per week, sustained. Zero new applications June 4–July 2 is the failure to not repeat. Never let one live process stop sourcing.
- Segment: prefer Barcelona-local/hybrid and Senior product roles (breadth + Abacum data-layer lead). Global-remote DS-titled Staff/Lead roles are the lowest-conversion segment; enter them only with the DS evidence complete.
- Warm paths: still check before every cold apply (good hygiene), but the 2026-07-02 correction stands: the one conversion so far was a cold apply. Don't over-invest in outreach at the expense of volume.
- Interviews with live challenges: vision first, then disciplined scoping as a choice within it. Validation-first framing reads as junior (Factorial rejection feedback, memory.md 2026-07-01/02 entries).

## AI differentiator (highest-value positioning work after this week)

- [x] Confirm whether managers were real users of the Remuner AI agent. Resolved 2026-07-06: yes, most had their own comp plan and could query team info (memory.md). "And managers" is safe in all copy.
- [x] Make the shipped AI work visible. **Done 2026-07-23** (verified): case live at `portfolio/public/cases/ai-agent.html` on both `dev` and `main` (main tip `52b9ffb`), wired into the home page and all four other cases' sidebars (`0caa143`), hero image + thumbnail fix shipped (`c10545c`), homepage hero copy updated (`52b9ffb`). All four artifacts (`ai-agent-hero.png`, `ai-agent-formats.png`, `ai-agent-loop.png`, `ai-agent-reach.png`) present and committed. job-search submodule pointer matches (`52b9ffbe`). CV/LinkedIn line was already live (see below).
  - [x] Propagate two corrections to `context/portfolio.md` and memory.md. Done 2026-07-20: portfolio.md's Remuner agent entry rewritten as a numbered case (5. AI Agent) with both facts fixed; memory.md got a new 2026-07-16 dated entry alongside the existing PM correction; cv-base.md's CV bullet (line 34) also carried the two-surface error and is now fixed
  - [x] CV/LinkedIn line. Already live in `cv/cv-base.md` and `context/linkedin.md`'s Remuner entry ("designed and shipped an AI agent for sales reps and managers"); the CV bullet's wording just got the two-surface fix above. Nothing further needed here

## DS case studies: day-to-day operating signal gap (raised 2026-07-21)

Both DS cases (`portfolio/public/cases/design-systems.html` Abax, `design-system-remuner.html` Remuner) are strong on architecture and adoption mechanics but thin on the signals that prove you *run* a system, not just build one — exactly what Staff-titled DS roles probe for (surfaced while assessing OLX/Otodom, but applies to any future DS/Staff DS role). Checked live copy against `context/design-systems-notes.md`: the raw material for most of this already exists and was cut during the original distillation.

Gaps, mapped to what's missing:
- **Conflict resolution under tension** — no case shows a standard-setting decision actually being resolved. Candidates already in the notes: the read-only state debate (engineers vs. designers, different mental models), component naming disputes, the deprecated-components-in-search bug (3 tradeoff solutions proposed). None of these have a recorded resolution — **need Manel to fill in how each was actually resolved (or confirm it wasn't) before any of this can be written.**
- **Contribution model, elaborated** — Abax case has one throwaway phrase ("contribution guidelines") never explained. Raw material exists: the issue-reporting system's "naming proposals" category, and the feature-flag migration where squads self-managed their own backlog instead of a central team gatekeeping.
- **Roadmap / prioritization judgment** — Vision 1.0's explicit 80%/100% success criteria, the two sprint-format options evaluated (small team/2 weeks vs. large team/1 week), and the audit's fix-now-vs-defer-into-feature logic are real prioritization decisions that never get framed as "how I decided what's next."
- **Closing meta-lesson** — both cases end cold on an outcome bullet list. `portfolio.md`'s own Staff-level signals checklist (item 7) already calls for this; neither case has it.
- **Outcome buckets** — outcomes are flat lists, not framed around the four categories `portfolio.md` already recommends (product velocity, engineering consistency, team scalability, organizational behavior).

Next steps:
- [x] Manel: confirm resolutions for the read-only-state debate, the naming disputes, and which of the 3 deprecated-component fixes actually shipped. **Done 2026-07-23**, recorded in `context/design-systems-notes.md`: naming disputes settled by a documented convention (not case-by-case); read-only state resolved by reusing/adapting an existing MUI/Vuetify state rather than building new, reflecting a general "extend the framework unless design genuinely requires new" principle (same logic as the MUI decision); deprecated components fixed by an "⛔ - DEPRECATED" rename + clean-name replacement, unpublished after a transition period.
- [x] Rewrite/extend both DS cases with a conflict-resolution story, an elaborated contribution-model paragraph, a roadmap/prioritization section, outcome-bucket framing, and a closing meta-lesson. **Done 2026-07-24.** Abacum case gained a sprint-planning/success-criteria section, a resolved-disputes section (naming, read-only state, deprecated-component bug), and the Exploration/Implementation contribution model. Both cases got outcome bullets reframed into velocity/consistency/scalability/behavior and a closing "Lesson" section. Fact-checked against `context/design-systems-notes.md` (5 issues caught and fixed: an invented resolution, an unsupported attribution, invented specific positions in the read-only debate, a fabricated consequence, and an internal contradiction in an outcomes bullet). Sprint-format decision corrected to "engineering leadership" (Manel confirmed 2026-07-24 it was a C-level call, not his). Three sentences using generic-principle/aphorism phrasing rewritten as direct first-person decisions per Manel's steer, one in the Remuner lesson, two in the Abacum case, plus the pre-existing Remuner outcomes lead. Committed across 5 commits on the portfolio's `dev` branch, pushed to origin. **Not merged to `main` — live site untouched, pending Manel's review.**
- [x] Re-run `/review-case` on both after the rewrite. **Done 2026-07-24.** Both score strong on 4 of 5 criteria. Abacum's one open item (sprint-format ownership) resolved above. Remuner has no interpersonal-conflict story to match Abacum's three disputes; Manel confirmed there wasn't a relevant one, so the case stands on its sequencing/bandwidth tradeoffs instead.
- [ ] Manel reviews the `dev` branch content, then merge `dev` → `main`, push, and update the submodule pointer in job-search's `context/portfolio.md`/git submodule reference so the live site matches.
- [x] **CV/CL side done 2026-07-22.** Contribution-model and roadmap-judgment material (Abacum's naming-proposals issue tracker, feature-flag self-managed migrations, explicit 80%/100% adoption targets tracked in-codebase; Remuner's audit fix-now-vs-defer process, monthly FE meeting cadence) added to `cv/cv-base.md`'s Additional material swap bank for both entries, then pulled into the OLX/Otodom package (cv/roles/ and cover-letters/roles/ olx-otodom-senior-product-designer-design-system.md) as new bullets. Conflict-resolution stories still can't be used anywhere (CV or case) until Manel confirms outcomes above. Reuse the swap-bank material for 3Commas, Bunge, and any other DS-adjacent role in this batch.

## Interview prep (yours to write)

- [ ] **Priority zero: "Why did you leave Remuner?"** — framing guidance at the top of `interviews/prep.md`. Rehearse out loud before any screen.
- [ ] The 8 `[NEEDS YOUR STORY]` gaps in `interviews/prep.md`: missed deadline, public failure, disagreed with manager, hardest feedback to receive, bad day, skills gap, feedback that changed you, getting better at weaknesses. Plus 2–3 usable Kings of Mambo incidents (Story E).
- [ ] **AI agent case deck** (`interviews/decks/case-deck-ai-agent.md`): speaker notes and slide structure are fully written, but the visual artifacts for each slide (flow diagram, annotated conversation screenshot, reach diagram, cycle diagram, outcome cards) still need to be built or copied over from the live portfolio AI agent case. Raised 2026-07-24 during Biorce prep; explicitly parked until after the Biorce recruiter screen (2026-07-28), since that round doesn't need it. Revisit if Biorce (or any other process) advances to a case-presentation round, or whenever Manel has slack. Once picked back up: figure out output form first (Figma slides via figma-console MCP, a standalone HTML artifact, or just refined visual descriptions for Manel to build himself), and reuse whatever's already live on the portfolio's AI agent case page where it overlaps.

## Records hygiene

- [ ] cv/roles/ and cover-letters/roles/ are empty but six applications went out as PDFs. Decide: backfill plain-text sources from the sent PDFs, or accept the PDFs as the only record. From now on, sources before export (rule in CLAUDE.md). Progress 2026-07-15: Factorial IT spinoff backfilled (cover-letters/roles/factorial-senior-product-designer-it-spinoff-BACKFILL.md) from the sent PDF plus form answers Manel recovered from a claude.ai chat. Recovery method for the rest: PDFs in cv-pdf-to-send/ + search claude.ai chat history around each send date.
- [ ] Start using Linear actively — unblocks the deferred Linear application.

## Parked (decided, no action now)

- Rep Letters case: stays hidden. Revisit condition (DS images done) met 2026-07-08 — decide when there's slack, not urgent.
- Salary benchmarks for Staff/Lead scope: add only if a live process advances to comp conversations.
- index-OLD.html: still deployed and publicly reachable. Delete or keep — your call.
