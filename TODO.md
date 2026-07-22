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
- [ ] Make the shipped AI work visible: sharpen the line in `cv/cv-base.md`, `context/linkedin.md` + live profile, `context/positioning.md`. Shipped AI product work is the strongest screening signal in the 2026 market and it's currently invisible. **Elevated 2026-07-13** after the Qonto AI Lab screen rejection: the application claimed a shipped GA agent and the portfolio showed no AI evidence to a screener who clicked through. **Updated 2026-07-14: the "minimal version first, not a new case" call was superseded by Manel; full case drafted.** Intake in `context/ai-agent-notes.md` (6 questions answered), draft at `portfolio/public/cases/ai-agent.html` (uncommitted, not linked from any page). Remaining before it can ship:
  - [ ] Manel reviews the draft copy for factual accuracy (especially the refusal wording, the answer anatomy, and the behavioral-proxy description)
  - [ ] Artifacts: reach and loop diagrams generated as SVG 2026-07-16, reviewed by Manel. Reach diagram corrected 2026-07-20: the "Integrations agent" node duplicated "Items agent" (both read ERP/line items); replaced with a Simulator agent (what-if payout scenarios, using the sliders/inputs reps already had), which Manel confirmed existed pre-departure and was answerable through chat. Scope section prose and the build comment in ai-agent.html updated to match; correction logged in ai-agent-notes.md. Remaining: the annotated answer-anatomy hero and the formats image, Manel builds both from the Remu Figma components (brief in the HTML comments). Invented realistic data only; remuner.com/remu is inspiration, never asset source. Optional: recolor design-systems-pipeline.svg from steel blue #4A7C9E to brand teal (it predates brand.md's no-blue rule)
  - [ ] Add the case to the home page and the other cases' sidebars, commit in the submodule, update the pointer. Hold until the hero and formats images exist; the draft references both by filename and would ship with broken images otherwise
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
- [ ] Manel: confirm resolutions for the read-only-state debate, the naming disputes, and which of the 3 deprecated-component fixes actually shipped
- [ ] Rewrite/extend both DS cases with a conflict-resolution story, an elaborated contribution-model paragraph, a roadmap/prioritization section, outcome-bucket framing, and a closing meta-lesson
- [ ] Re-run `/review-case` on both after the rewrite
- [x] **CV/CL side done 2026-07-22.** Contribution-model and roadmap-judgment material (Abacum's naming-proposals issue tracker, feature-flag self-managed migrations, explicit 80%/100% adoption targets tracked in-codebase; Remuner's audit fix-now-vs-defer process, monthly FE meeting cadence) added to `cv/cv-base.md`'s Additional material swap bank for both entries, then pulled into the OLX/Otodom package (cv/roles/ and cover-letters/roles/ olx-otodom-senior-product-designer-design-system.md) as new bullets. Conflict-resolution stories still can't be used anywhere (CV or case) until Manel confirms outcomes above. Reuse the swap-bank material for 3Commas, Bunge, and any other DS-adjacent role in this batch.

## Interview prep (yours to write)

- [ ] **Priority zero: "Why did you leave Remuner?"** — framing guidance at the top of `interviews/prep.md`. Rehearse out loud before any screen.
- [ ] The 8 `[NEEDS YOUR STORY]` gaps in `interviews/prep.md`: missed deadline, public failure, disagreed with manager, hardest feedback to receive, bad day, skills gap, feedback that changed you, getting better at weaknesses. Plus 2–3 usable Kings of Mambo incidents (Story E).

## Records hygiene

- [ ] cv/roles/ and cover-letters/roles/ are empty but six applications went out as PDFs. Decide: backfill plain-text sources from the sent PDFs, or accept the PDFs as the only record. From now on, sources before export (rule in CLAUDE.md). Progress 2026-07-15: Factorial IT spinoff backfilled (cover-letters/roles/factorial-senior-product-designer-it-spinoff-BACKFILL.md) from the sent PDF plus form answers Manel recovered from a claude.ai chat. Recovery method for the rest: PDFs in cv-pdf-to-send/ + search claude.ai chat history around each send date.
- [ ] Start using Linear actively — unblocks the deferred Linear application.

## Parked (decided, no action now)

- Rep Letters case: stays hidden. Revisit condition (DS images done) met 2026-07-08 — decide when there's slack, not urgent.
- Salary benchmarks for Staff/Lead scope: add only if a live process advances to comp conversations.
- index-OLD.html: still deployed and publicly reachable. Delete or keep — your call.
