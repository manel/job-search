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

Starting condition: the product didn't look broken, but it wasn't designed with system thinking. Built by a graphic designer: decisions made screen by screen, no typographic scale, no spatial rhythm, no component logic. Visually passable; no structure underneath. Implementation side matched: zero Figma components, each engineer had built their own component set with Vuetify defaults filling gaps. The gap was in both layers. Team grew from 2 to 5 FEs during tenure.

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

#### Figma file audit — Remuner | ⚛️ Core (June 2026)

Source: live Figma file read via Desktop Bridge. This is the actual token file, not documentation.

**Architecture — 4 collections, 630 variables:**
- `branding` (2 variables, 1 mode) — the two brand colors: blue and green
- `_core` (417 variables, 1 mode) — full primitive scales: grey, blue, green, red, orange, yellow, pink, purple, cyan, brown; brand blue/green; gold/silver/bronze; chart palettes (9 colors); chip palettes (9 colors); dimensions; border-radius; raw font values
- `product` (189 variables, 1 mode) — semantic tokens: color/text/*, color/icon/*, color/bg/*, color/border/*, space/*, formElements, stateLayer, and all domain-specific tokens
- `typography` (22 variables, 2 modes: desktop + mobile) — responsive type scale: 9 semantic font sizes, 3 weights, 6 line heights, 3 letter spacings, 1 font family

By type: 535 COLOR · 88 FLOAT · 7 STRING. **No Figma styles — 100% variables.**

**Domain-specific tokens (signals the system served real product surfaces, not generic UI):**
- `ranking/` — 1st/2nd/3rd/other × text, bg, icon, border, hover, highlight states. Backed by full gold/silver/bronze primitive scales.
- `tiers/` — current and past tier states (text, icon, border)
- `progress/` — progress indicator text and bg states
- `space/tableCell/compact` + `space/tableCell/comfortable` — table density tokens
- `color/chart/*` — 9 semantic chart colors × light/default/dark variants each
- `color/chip/*` — 8 semantic chip colors × bg/text/icon

**Explicit scope boundaries (what was not built):**
- Dark mode — `product` collection has a single "Value" mode, no light/dark theming
- Elevation/shadow tokens — not present
- Motion/animation tokens — not present
- Grid, layout, breakpoint tokens — not present

**Governance evidence in the file:**
- `color/chart/⛔ rankingFirst (TO DELETE)`, `rankingSecond (TO DELETE)`, `rankingThird (TO DELETE)` — old flat ranking tokens, deprecated and replaced by the structured `ranking/` namespace. Still present in the file, explicitly marked. Staged deprecation: nothing removed quietly.

#### Figma file audit — Remuner | 💠 Components (June 2026)

Source: live Figma file read via Desktop Bridge. 63 pages total, 54 with components.

**Generic UI components (what any DS would cover):**
Avatar, Avatar Group, Icon, Banner, Alert, Snackbar, Button (130 variants), IconButton, BulkActions, SplitButton, FAB, Chip (60 variants + FrequencyChip + RankingChip), Divider, Dialog (12 variants + Compositions), Popover, BottomSheet, Tooltip, Tabs, Menu, ActionsMenu, Pagination, Step, Slider, Checkbox, Radio, RadioGroup, Select (131 variants), Segmented Control, Switch, Textarea, TextField, Autocomplete, Date Input, Date Picker, File Input, Color Picker, Appbar, Navigation, Subheader, ListItem, ListPanel

**Domain-specific components (unique to Remuner's product):**
- `Chart` — 21 component sets: bar grouped, bar stacked, waterfall, area chart, pie, ranking chart variants
- `Cards` — 24 sets with named product-persona variants: Individual/Metric, Individual/Payout, Individual/Ranking, Individual/Average, Individual/Operations, Manager/Ranking, Manager/UsersDetails, Designer/Payout, Simulator/Card
- `Progress Bar` — 8 sets including ranking-specific (1st/2nd/3rd/default), pace indicators, metric progress bars, widget progress bars
- `Widgets` — 16 sets: IC (individual contributor) and Manager content views covering metrics, earnings, payments, personal targets, rankings, pending payments
- `Tiers` — tier blocks and indicators (links to tiers/ token domain)
- `Remu` — 6 sets: the AI assistant widget (saved chats, header, footer, content states)
- `Email` — full email template system: header, footer, icons, content slots, templates

**Mobile coverage:** Cards, Table, Appbar, Subheader, BottomSheet, Chips, Widgets, Pagers all have explicit mobile variants.

**Governance evidence in components:**
- `DEPRECATED → Select` — entire page retained for the old Select component, explicitly named deprecated. Same mark-before-delete discipline as the ⛔ token pattern. Consistent across both layers.

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

**AI agent for sales reps and managers.** Shipped, GA to all customers before March 2026. Canonical description (from Manel, 2026-06-12, recorded in memory.md and transferred here 2026-07-06): a chat panel plus embedded answers inside the app that let sales reps consult their own data: ERP line items, aggregations by period, where to focus, understanding their sales plan and decisions based on it. Manel owned the full UX/UI, conversation design (tone, answer formats), capability scoping with PM and engineering, and trust/accuracy patterns. Post-release feedback was mixed; he iterated on tone, response format, and per-customer terminology (the same object was a "deal", "contract", or "item" depending on the customer).

Managers confirmed as real users (Manel, 2026-07-06): most managers had a compensation plan of their own, and they could also query team info through the agent. "And managers" is safe in all copy.

Evidence position: no claimable metrics or named signal. Pre-release user interviews showed strong interest ("a genuine tool to improve their work"). Own the absence of metrics; the post-GA iteration loop is the interview story, not a public claim.

CVs sent before 2026-06-12 described the agent as "generates compensation letters" (conflation with the separate rep letters project); if an interviewer asks about it from an old CV, describe the agent accurately and move on.

**Sales rep plan creation experience for admins.** Designed in Manel's final months (late 2025 / early 2026). In development when he left in March 2026; some of it was built and ready for internal testing. If ever used as case material, the only honest framing is: designed end to end, partially built at departure, outcomes unknown. Never imply it shipped.

---

## Portfolio evaluation standard

Cases must show:
- Problem complexity and ambiguity
- Candidate's specific role and decisions (not "we" without context)
- Cross-functional influence
- Measurable or operational impact
- What made it hard

## Staff-level signals for written cases

The master checklist lives in `interviews/prep.md` (Case presentation round → Staff-level signals checklist). That version is written for in-person deck presentation. Below is how each point adapts to written, async portfolio cases — where there are no speaker notes and no conversation to recover from.

**1. Opening frame**
The first paragraph of the case must signal ambiguity + leverage + strategic allocation — not domain or craft. A reader who skims only the opener should understand: this is about deciding where design investment creates the most leverage, not about shipping a deliverable. If the opener describes what was built, rewrite it to describe the decision context.

**2. Constraint as a named section**
"I was the sole designer" is one sentence. A Staff-level constraint section does three things: names the allocation problem explicitly ("every infrastructure week competed with a product delivery week"), shows the structure of the tension (e.g. product velocity vs. system quality vs. team scalability — impossible to maximise all three), and makes clear that this tension was managed deliberately, not absorbed passively.

**3. Prioritisation as a section with a concrete table**
Include a named section — "How I decided what to build" or equivalent — with a visible decision framework and a table of at least 3–4 real choices: what was prioritised, what was deferred, and why. Written cases that omit this read as build logs. Cases with this section read as strategic records.

**4. Restraint as a visible subsection**
"What I chose not to build" should appear as a callout or dedicated heading, not be implied by absence. Name the deferred items. Name the reasoning. Staff credibility comes from visible tradeoff discipline, and readers can't see deferred decisions unless you show them.

**5. PM-like behaviours in the body**
Ticket creation, sprint prioritisation participation, system debt treated as first-class roadmap items — these must appear in the body of the case, not in speaker notes that don't exist. If you shaped the backlog, name it. If you created the ticket that unlocked the work, say so. Make the influence chain traceable: observation → framing → ticket → sprint → shipped.

**6. Outcome buckets, not artifact lists**
The outcomes section should be structured around impact categories, not things shipped. Four categories that work: product velocity (what repeated work was eliminated), engineering consistency (what previously implicit decisions became enforceable), team scalability (what got faster or cheaper to onboard), organisational behaviour (what changed in how the team plans). The last category is the hardest to write and the strongest signal.

**7. Closing meta-lesson**
The final section of the case must name the underlying tradeoff — not the artifact, not the process step. "The biggest lesson wasn't about component architecture. It was learning to continuously balance short-term delivery against long-term leverage." If the case ends on an artifact or a quote, it's ending at the wrong level.

**8. Own missing metrics in the body**
Don't wait for a follow-up question. A sentence in the outcomes section that names the proxies and acknowledges the absence directly is stronger than a silent gap. "No instrumentation was in place to measure X. The signals I can point to are: [Y], [Z], and the CTO's observation that [quote]." Confidence, not apology.

**9. Portfolio breadth check**
If the only case is DS/infrastructure, a hiring manager may read the portfolio and pigeonhole. Before any application, check whether the portfolio as a whole shows: at least one product discovery story, at least one user research story, at least one decision-under-ambiguity story that is not primarily about systems. If not, the case selection needs to change or the written framing needs to carry the breadth.

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
