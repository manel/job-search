# Perk (TravelPerk): Interview Notes

Staff Product Designer - Events. Applied 2026-07-10 via Xavi Francisco's referral link.

---

## Round 1: Recruiter / Talent screen
**Date:** Not yet scheduled
**Interviewer:** Unconfirmed. Xavi (referral) is a Senior SWE, not the hiring path himself; ask who the recruiter or hiring manager is once contacted.

### Clarify first
- Confirm Xavi's referral actually registered in their system (he was asked to confirm this 2026-07-10; check whether he replied before assuming the referral is live).
- Confirm the Events product line's team structure: who Manel would report to, and whether there's an existing design lead already on Events or this role creates that function.
- Confirm the 3-day office expectation (Barcelona hybrid) is fixed or negotiable, since this affects nothing about fit but is worth knowing going in.

### What Perk most likely cares about (this round)
- AI as a working default: the JD explicitly names Claude, Cursor, Bolt, Figma, and Git as expected daily tools, not optional extras. This is a screen-stage differentiator, lead with it early rather than waiting to be asked.
- Multi-sided platform design: Events is a marketplace with planners, suppliers, participants, and staff as distinct personas, integrating with the broader travel and spend platform. This is a workflow-complexity problem, not a UI-polish one.
- Staff-level scope: genuine IC ownership of a full product line, not a support role on someone else's roadmap.

### Lead story for this round
Story A (Dataset Manager) for multi-persona workflow complexity and product-architecture reasoning. Bring the shipped AI agent (Remuner) forward explicitly and early, since the JD's AI-as-default requirement is a named qualification, not an inference. Positioning.md doesn't have an exact bucket for "Staff product role, multi-sided platform, no DS-title." Dataset Manager plus the AI agent story together cover the two things this JD actually asks for.

### Likely questions → story map
- "Tell me about designing for a platform with multiple distinct user types" → Story A (Dataset Manager): finance teams as the primary persona, but the underlying reasoning (mental-model mismatch, staged delivery) generalizes to multi-sided design.
- "How do you use AI tools in your daily practice?" → Growth Q21/Q23: AI-assisted token pipeline implementation, Claude Code/Cursor project setup. Be ready to go deeper here than at other companies; this is a named requirement, not small talk.
- "What's your experience owning a full product line at Staff level?" → Story B (Abax DS) for the closest evidence of full-scope ownership without a mandate; be honest that this is DS scope, not a product-line P&L, and reframe toward the judgment pattern (identifying the real problem, building the case, owning delivery) rather than overclaiming line ownership.

### [NEEDS YOUR STORY] gaps this round could hit
- No story currently documents owning a full product line end to end in the way "Staff Product Designer - Events" implies. Story B and Story D (Modeling Syntax) are the closest analogues (squad-level ownership); be ready to name that distinction honestly if probed on scope.

### Questions to ask them
- How does design collaborate with engineering and product on the Events line specifically, day to day?
- What would make someone in this role exceptional versus good at 12 months?

### Salary reminder
€95K opening (set 2026-07-10): Staff scope above the €93K Senior benchmark. Not volunteered; state only if the form or a screen asks. If they publish or volunteer a band, open at its top per the standing rule.

*After this round happens: run `/debrief-interview Perk "Round 1"` while it's fresh.*

---

# Senior Design Systems Designer (Suitcase), November 2026

Record: `applications/records/perk-senior-design-systems-designer.md`. Applied 2026-10-21, referred by Tanna 2026-10-26, template rejection the same day, reversed by Clare's interview invite 2026-11-02. The Events round above is a different, closed process.

## Round 1: TA Preliminary (brief written 2026-11-03)

**Date:** Thu 2026-11-05, 15:30-15:55 Madrid, Google Meet (https://meet.google.com/oue-gzhv-jni). 25 minutes, not the 15 in the first email.
**Interviewer:** Clare Watts, Senior Talent Acquisition Partner. Her stated agenda: background, motivation for the role, team and culture.
**Before the call:** confirmed. Reply sent and invite accepted 2026-11-02. In English.

### What Perk most likely cares about (this round)
- **A credible "why Suitcase" from someone they already rejected once.** Clare has to justify the reversal internally; give her a clear, checkable reason to pass Manel to the hiring manager: production adoption tracking, migration across squads, contribution model.
- **Logistics knock-outs:** three days a week in the Barcelona office, English working level, availability (immediate), salary fit against the EUR 65,000 already on the form.
- **Seniority read without a DS title:** two production systems, one co-led across five squads, one built alone. TA will check that "Senior Product Designer" on the CV still means system ownership.

### Lead story
Design-systems mapping in `context/positioning.md`: **Story B (Abax) as lead, Story C (Remuner DS) as support.** Abax first because it carries the JD's rarest asks (adoption measured monthly, about 47% at departure; consolidation off MUI; contribution review). Remuner second for building alone and the AI/Figma MCP work. Keep both to headline level; a TA screen won't go into token tiers.

### Likely questions → story map
- "Walk me through your background" → Opening intro (`prep.md`), DS-weighted: KOM component libraries, Abax co-lead, Remuner built from scratch. Under two minutes.
- "Why Perk / why this role?" → Q11 framework. Structural hook: Suitcase is named infrastructure with core and experimental layers, adoption and parity measures, and content tokens. Alignment: the Abax rollout and the SimpleLocalize keys built into Remuner components. Stage: Q26 (a system treated as infrastructure). Answer it for real before the call.
- "Why did you leave Remuner?" → Priority zero, memorised version. Then stop.
- "What have you been doing since March?" → two anchors, confirmed by Manel 2026-11-03: deepening Claude and Figma MCP work (ties straight to the JD's MCP line) and occasional freelance work. Clients and scope of the freelance work aren't recorded; if Clare asks "what kind?", answer from memory and keep it to one line.
- "How do you use AI day to day?" → Q22/Q23 plus the three-use answer from `memory.md` 2026-10-26 (AI prototypes, DS work through the Figma MCP, own PRs within limits). Recruiter-screen question now; have it ready.
- "What kind of team do you work best in?" → Q12.
- "You applied to the Events role in July" → not in prep. Facts only: different role shape (product, Staff); this one matches the system work directly. Don't raise the 26 Oct rejection unless Clare does; if she does, thank her for the second look and move on.
- "Salary expectations?" → see reminder below.
- "Other processes?" → true and short: interviewing elsewhere, nothing at offer stage (check the pipeline on the day before saying it).

### [NEEDS YOUR STORY] gaps this round could hit
- **Q17 bad day** is marked [NEEDS YOUR HONEST ANSWER]. Low odds in a TA screen; "team and culture" makes it possible.
- **Story E (KOM)** is unfleshed. Only matters if Clare probes the eleven studio years.
- JD gaps that are not story gaps but could come up as "experience with X?": Code Connect (named in the JD, 2026-11-03 check: "Experience prototyping with AI tools and with Storybook, Code Connect and MCP tooling". Not used; say so, then bridge to the Figma MCP work and Storybook views generated from Figma props. Understanding how it maps Figma components to code is fair to claim; use is not), WCAG keyboard and screen-reader work (not evidenced; WCAG AA contrast only), native mobile (Remuner webview only). Say so plainly.

### Questions to ask Clare (pick 2-3)
- What are the next steps, and where does the process stand: how many candidates are further along? (Kabilio rule, `memory.md` 2026-10-16.)
- Who owns Suitcase day to day right now, and who does this role report to? (Tanna said she had been covering it; this is "what happened to the last person in this role" phrased for TA.)
- What is the salary range for the Barcelona hire? (Only if she hasn't raised compensation. Salary rule 2: ask before restating a number.)

### Salary reminder
- Stated on the form: **EUR 65,000 gross annual base**. No range published. Floor (40K employed) is never stated.
- If asked: give Clare a chance to name the band first ("Is there a range for the Barcelona role?"). If she presses, keep 65K; don't drop it to look flexible. Never share Abacum or Remuner pay (rule 8 wording in `context/salary.md`).
- After the call, record in the record: range given (if any), whether asked, what was said, any compensation feedback.

*After the call: run `/debrief-interview perk "TA Preliminary"` while it's fresh.*
