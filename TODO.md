# TODO

Single list of open items. Snapshot dated 2026-07-02, rebuilt from the full search diagnosis run that day. Pipeline follow-up dates live only in `context/applications.md` (a SessionStart hook surfaces overdue ones automatically); do not duplicate them here. The hook also surfaces the "This week" section below at every session start. Remove items when done.

Diagnosis summary behind this plan (2026-07-02): 7 applications in 6 weeks, 1 screen (Factorial, cold apply, Barcelona-local, reached round 3). Fast rejections were global-remote DS-titled roles, the hardest segment, hit while the Remuner DS case was live with broken images. First-order problems in order: volume collapsed after June 4; portfolio DS evidence missing/broken; segment weighting wrong; AI differentiator invisible.

---

## This week

- [ ] **1. Portfolio: export the 4 Figma images for the Remuner DS case.** Audit board first (one pattern study: every autocomplete/input state across the product with defined variants beside them — it's the proof behind the CTO quote). Then: token architecture (variables panel, primitive + semantic collections), pipeline evidence (passing CI run or HTML preview sandbox), hero + home thumbnail. Specs are in TODO comments inside `portfolio/public/cases/design-system-remuner.html`. Crop: another company's product internals.
- [x] **2. Portfolio: removed "without a dedicated team"** (done 2026-07-06, on dev, uncommitted) from the Abacum DS description on the home page (`portfolio/public/index.html`, work-item desc). Violates the memory.md 2026-06-08 rule: reads as excuse-framing. Claude can do this one.
- [ ] **3. Portfolio: finish dev, merge to main, deploy, update the pointer here.** Corrected 2026-07-06: the live site (main branch) is the old version with no broken images; the Remuner DS case exists only on dev (3 unmerged commits plus uncommitted image/copy changes). Sequence: finish items 1 and 2 on dev, commit, merge dev into main, push (deploys to manel-leiva.com), then update the submodule pointer in this repo. Until merged, the Remuner DS case is invisible to recruiters: no new DS-titled application goes out before this is done.
- [ ] **4. Send BVNK LinkedIn outreach** (due 2026-07-03, stale 2026-07-10). Find hiring manager or senior DS designer via company People tab (method in `context/outreach.md`). Draft:
  > Hi [name], I applied for the Lead Design Systems role on June 1 and I'm still interested. I've built two production design systems end to end, most recently at Remuner, where I also owned the token pipeline from Token Studio through Style Dictionary to a published npm package with CI validation. Happy to share more if useful: manel-leiva.com. Best, Manel
- [ ] **5. Send Finom LinkedIn outreach** (due 2026-07-03, stale 2026-07-10). Find a design lead via company People tab. Draft:
  > Hi [name], I applied for the Senior Product Designer role on June 2 and I'm still interested. My recent work is on data-heavy B2B products; at Abacum I designed the dataset management layer and the modeling syntax behind its FP&A platform. Happy to share more if useful: manel-leiva.com. Best, Manel
- [ ] **6. Spendesk package by 2026-07-04.** Already unblocked: set salary position (`context/salary.md` framework), then `/new-application Spendesk "Senior Product Designer" product`. Use the canonical AI agent description; manager claim confirmed safe 2026-07-06. Barcelona hybrid — exactly the segment that converts.
- [ ] **7. Monday 2026-07-06: sourcing session, Barcelona-weighted.** LinkedIn filtered Barcelona + hybrid, Manfred, direct careers pages of Barcelona B2B SaaS. Weight local/hybrid and Senior product roles over global-remote DS-titled ones (that segment reopens when the Remuner case evidence is live). Target 3–5 assessed. Run `/source-roles` with everything found.

## Standing strategy (from the diagnosis, until revisited)

- Volume: 3–5 roles assessed per week, sustained. Zero new applications June 4–July 2 is the failure to not repeat. Never let one live process stop sourcing.
- Segment: prefer Barcelona-local/hybrid and Senior product roles (breadth + Abacum data-layer lead). Global-remote DS-titled Staff/Lead roles are the lowest-conversion segment; enter them only with the DS evidence complete.
- Warm paths: still check before every cold apply (good hygiene), but the 2026-07-02 correction stands: the one conversion so far was a cold apply. Don't over-invest in outreach at the expense of volume.
- Interviews with live challenges: vision first, then disciplined scoping as a choice within it. Validation-first framing reads as junior (Factorial rejection feedback, memory.md 2026-07-01/02 entries).

## AI differentiator (highest-value positioning work after this week)

- [x] Confirm whether managers were real users of the Remuner AI agent. Resolved 2026-07-06: yes, most had their own comp plan and could query team info (memory.md). "And managers" is safe in all copy.
- [ ] Make the shipped AI work visible: sharpen the line in `cv/cv-base.md`, `context/linkedin.md` + live profile, `context/positioning.md`. Then decide: short case or a section inside an existing case. Shipped AI product work is the strongest screening signal in the 2026 market and it's currently invisible.

## Interview prep (yours to write)

- [ ] **Priority zero: "Why did you leave Remuner?"** — framing guidance at the top of `interviews/prep.md`. Rehearse out loud before any screen.
- [ ] The 8 `[NEEDS YOUR STORY]` gaps in `interviews/prep.md`: missed deadline, public failure, disagreed with manager, hardest feedback to receive, bad day, skills gap, feedback that changed you, getting better at weaknesses. Plus 2–3 usable Kings of Mambo incidents (Story E).

## Records hygiene

- [ ] cv/roles/ and cover-letters/roles/ are empty but six applications went out as PDFs. Decide: backfill plain-text sources from the sent PDFs, or accept the PDFs as the only record. From now on, sources before export (rule in CLAUDE.md).
- [ ] Start using Linear actively — unblocks the deferred Linear application.

## Parked (decided, no action now)

- Rep Letters case: stays hidden. Revisit after DS images are done.
- Salary benchmarks for Staff/Lead scope: add only if a live process advances to comp conversations.
- index-OLD.html: still deployed and publicly reachable. Delete or keep — your call.
