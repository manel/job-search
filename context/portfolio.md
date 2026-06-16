# Portfolio Context

Portfolio live at: manel-leiva.com
Stack: Next.js, Vercel (Hobby tier). Fully public, no password (confirmed 2026-06-12).
Portfolio repo is linked as a git submodule at `../portfolio/` relative to this file.

To update case study copy: edit files in the `portfolio/` submodule, commit there first, then update the submodule pointer in this repo.

**Names rule (decided 2026-06-12):** Live case copy never names colleagues, research participants, or customers. Roles only: "the head of design", "the CTO", "a designer on the team". Specificity comes from the detail of what happened, not attribution. Names in this file are internal reference for Manel only.

---

## Candidate

Manel Leiva — Senior Product Designer
- Kings of Mambo (UX studio, co-founder, 2010–2021)
- Abacum (Senior Product Designer, Jan 2022–Apr 2024, integrations and engine squads)
- Remuner (Senior Product Designer, May 2024–Mar 2026, sole designer and DS lead)
- Postgraduate teaching: UX and digital design. Framed in portfolio as skills developed (explaining complex systems, depth of craft, mentoring). Not a standalone work entry.

Education: Higher National Diploma in Computing Design and Multimedia from ESI (2002). Vocational qualification (Spanish CFGS equivalent). Not a university degree.

---

## Case studies

### 1. Modeling Syntax (Abacum)
URL: /cases/modeling-syntax
Status: Complete and live

Summary: Standardised formula syntax across Abacum's modeling layer. The problem was identified with Julian (head of design). Ran competitor benchmark, synthesised GONG call evidence from the Swirldlabs call. Cross-squad ownership. Collaborated with Manuel C. (engineer) on syntax decisions. Unlocked the follow-on editor suggestions project.

Key decisions:
- Identified the problem as systemic, not a surface UI issue
- Chose to extend and standardise existing syntax rather than design a new one
- Worked across squad boundaries without formal mandate

Signals:
- Faster formula writing (qualitative, from user feedback)
- Quieter support channel (qualitative)
- Unlocked follow-on project (operational)

No hard metrics. Own this directly. The live case's "days rather than weeks" and "support requests dropped" characterizations are real recollections confirmed by Manel 2026-06-12, no recoverable numbers. Keep them as recollections, never as measured data. Customer name (Swirldlabs) removed from live copy 2026-06-12; keep it internal only.

Internal reference (names never appear in live copy): Julian (head of design), Manuel C. (engineer collaborator).

---

### 2. Dataset Manager (Abacum)
URL: /cases/dataset-manager
Status: Complete and live

Summary: Introduced a UI abstraction layer over JSON-based dataset configuration, enabling finance teams to manage data autonomously.

Key decisions:
- First dedicated designer on the squad — had to establish the problem space before designing anything
- Ran 3 user tests: Maria, Eduardo, Guillermo, Oriol. Weighted Oriol most heavily (most experienced user)
- Identified language mismatch between product language (data types) and user language (dimensions)
- Decided not to introduce SQL. Extended Modeling Syntax instead (prerequisite work that closed the gap)
- Work was incremental due to technical constraints — this was the right call, not a compromise

Signals:
- Implementation team had less work (operational signal from CS and implementation teams)
- Customer autonomy increased (qualitative, from implementation team feedback)
- Oriol's session: specific moments where the abstraction landed

No hard metrics. Own this directly. The live case's characterizations (implementation team spending roughly half the time on standard configuration, CS requests dropping in the following quarters, first-session onboarding) are real recollections confirmed by Manel 2026-06-12, with no recoverable numbers behind them. Keep them framed as team reads and recollections, never as measured data.

Internal reference (names never appear in live copy): Maria, Eduardo, Guillermo, Oriol (research participants). In live copy: "the most experienced user", "a research participant".

---

### 3. Design Systems (Abacum + Remuner)
URL: /cases/design-systems
Status: Complete and live
Title: From scattered components to a production design system

Summary: Promoted, built buy-in for, and implemented production-ready design systems at two companies alongside regular product work.

#### Abacum (Abax)

The business case, not the components, is the Staff-level story. Engineering was skeptical going in: documented FE concerns were "side project, co-prioritization, squads not having a platform picture". The presentation had to answer that skepticism with evidence of cost: screenshots of bugs and inconsistencies across buttons, cells, and menus, framed as "inconsistencies create a perception of immaturity, resulting in lack of trust". Getting the DS selected as a Maker Days initiative was the actual win. It converted a side project into a company-sanctioned quarterly initiative, competing against other initiatives for dedicated time.

Build and infrastructure:
- Two-tier token architecture
- Token Studio → Style Dictionary → GitHub → npm pipeline (an engineer built the original pipeline)
- ESLint rules for adoption enforcement
- Storybook deployed in Chromatic
- Kept MUI as base — deliberate decision: replacing it meant rewriting components across five squads with no immediate product benefit
- Covered five squads
- The Button was the first component shipped end to end through the pipeline, in one Maker Days week — first proof the pipeline worked

Measurement: success criteria were defined up front (80% of new UI from Abax components, 100% deprecation of legacy MUI where equivalents existed) with a planned metrics framework (MUI vs Abax component counts, disabled ESLint rules, token usage). Adoption was tracked, but the data is not recoverable. Own this directly in copy: the measurement happened, the numbers are gone. Do not fabricate figures.

Governance (8+ months of active operation, the part most DS cases skip):
- Structured issue reporting (categories, Slack channel, Notion)
- New components released under feature flags; squads added migration tasks to their own backlogs — avoided inconsistency during transition
- Weekly design library sync with a standing discoverability agenda
- Two-library Figma structure: Exploration file ([Experiment] prefix) vs canonical Implementation file. Manel proposed and drove this.

Real tensions worth surfacing in copy or interviews: when to stop building token infrastructure and start shipping components; contested component naming; the read-only state debate (engineers and designers had different mental models); the deprecated-components-in-search bug Manel diagnosed with three trade-off solutions.

#### Remuner

Starting condition: the product's visual design was reasonable, but implementation was fragmented. Zero Figma components; each engineer had built their own component set, with MUI defaults filling gaps. The problem was implementation fragmentation, not bad design. Team grew from 2 to 5 FEs during tenure.

- Built the component library from scratch. Sole designer. Buy-in was easy; the constraint was bandwidth (couldn't slow product work), which shaped the start-small approach
- Started with a small token set deliberately — lesson applied from Abacum (bigger token set created drift and maintenance overhead)
- Pipeline ownership, stated precisely: the foundation came from Abacum. Manel made the call to bring it in; engineers adapted it to Remuner's stack (Vuetify, Sass variables). In February 2026 Manel hardened the repo himself with AI assistance (Codex): CI pipeline, safety gates, build drift checks, W3C token format, HTML preview sandbox, smoke tests, JSON output for JS consumers. Engineers reviewed and merged. Do not overstate beyond this.
- Tokens exported as both Sass variables and utility classes, matching Vuetify conventions FEs already thought in. This decision came out of the monthly FE meetings, not top-down — "speaking the same language"
- Monthly FE meetings were the governance mechanism: everyone presented progress, problems discussed, goals set
- Ongoing product audit throughout tenure: systematically capture all instances of a pattern, define variants and states, ticket it, decide fix-now vs defer-into-upcoming-feature. The deferral judgment matters: not every inconsistency was worth fixing immediately
- Separate icons file and icons repo. Figma variables throughout

Key signals:
- The CTO: "from a 2010 app to a 2020 app" (unprompted, during a review session, after the audit had been running for a while — it reflects product-wide change, not a Figma library existing)
- Engineers called tokens by name (`color-text-primary` instead of `#2D2D2D`); hardcoded hex in review became a caught violation instead of a shipping inconsistency
- A designer built a screen fast because the components had what she needed, and flagged adjustments that Manel captured and acted on — the feedback loop is the signal, not just the speed
- Designers stopped double-checking whether components were connected to the system: if it was in the library, it was correct
- Storybook screen recording: placed as last item in the case, evidence the system works in production

Stack: Figma variables, Token Studio, Style Dictionary, GitHub submodule, Storybook, ESLint, npm packages, Chromatic

Internal reference (names never appear in live copy): Julian (head of design, Abacum, co-led DS business case). Raw intake material lives in `context/design-systems-notes.md`.

---

### 4. Rep Letters / Agreement lifecycle (Remuner)
URL: /cases/reps-letter
Status: LIVE but hidden from all navigation (commented out in sidebar and home). Manel considers it his weakest case (stated 2026-06-12). Unfinished: four image placeholders, thin outcomes.

Corrected facts (2026-06-12, from Manel):
- This project has NO AI component. Earlier versions of this file, cv-base.md, and the live case conflated it with the separate AI agent project below. The live case's "AI-generated block" claim has been corrected to "generated automatically from the plan's structured rules" — confirm with Manel that this is how the generated block actually worked.
- What shipped: the full agreement lifecycle. Template creation, letter generation, delivery, signature, record keeping.
- Decision: keep hidden for now. Remuner DS images are the higher-leverage portfolio work. Revisit whether to finish or retire this case after that.

---

### Remuner work that is NOT yet a case (recorded 2026-06-12)

**AI agent for sales reps and managers.** Shipped. Feedback existed but is no longer accessible; no recoverable data. The exact function of the agent is NOT yet recorded in this project — ask Manel and write it down before using any detail in copy. CVs sent before 2026-06-12 described it as "generates compensation letters", which is the conflation error; if an interviewer asks about it from an old CV, Manel should describe the agent accurately and move on.

**Sales rep plan creation experience for admins.** Designed in Manel's final months (late 2025 / early 2026). In development when he left in March 2026; some of it was built and ready for internal testing. If ever used as case material, the only honest framing is: designed end to end, partially built at departure, outcomes unknown. Never imply it shipped.

---

## Portfolio evaluation standard

Cases must show:
- Problem complexity and ambiguity
- Candidate's specific role and decisions (not "we" without context)
- Cross-functional influence
- Measurable or operational impact
- What made it hard

## Case study storytelling principle

A good case study is not "here is everything I did." It is "here is how I think when the problem is messy."

Interviewers cannot see the judgment behind the screen. That is what they are evaluating. Before writing or reviewing a case study, check whether the invisible layer is present: what were the competing directions, what made one wrong, what friction existed, what did you decide and own. If that layer is missing, the case study is a process record, not a judgment record.

Structure: lead with the result or decision, then the constraint or insight that made it hard, then what you did. Process-first reads as "I did stuff." Judgment-first reads as seniority.

This applies equally to live portfolio presentations during interviews: the framing should be "here is a decision I made when the problem was unclear," not "here is my process."

## HTML section structure

Every section follows this pattern:

```html
<section>
  <h2>Section headline</h2>
  <p class="lead">Lead paragraph. One or two sentences. Sets the frame.</p>
  <p>Body paragraph.</p>
  <h3>Subsection if needed</h3>
  <p>Body paragraph.</p>
</section>
```

No section-label spans unless specifically requested. No decorative motion. Screen recordings as evidence of a system working are appropriate and encouraged.

## Outcomes section rules

- Use named qualitative signals. Name the person or team where it adds credibility.
- Own the absence of hard metrics directly. Do not hedge with "we believe" or "we think."
- Anchor outcomes in: named people's reactions, operational changes, follow-on work unlocked.
- Avoid: "the project was well received," "users found it easier to use," any vague positive claim.
