# Case Deck: Design Systems at Remuner

**Figma:** "Remuner DS" (Slides). The current version is the Wizeline one, with its own talk track and pasted notes: [interviews/wizeline/ux-interview-deck.md](../wizeline/ux-interview-deck.md). This file is the general version; its slide numbers haven't been matched to Figma positions.
**Best for:** Founding and sole-designer roles, early-stage companies that need foundations built from scratch, DS roles where one senior designer builds and runs the system.
**Duration:** walk-through 10 to 12 minutes; leave the rest for questions. If time runs short, cut slides 2 (Starting point) and 7 (Governance) to one sentence each before touching the proof slides (4, 5, 8, 9).
**Lead framing:** as the only designer, I built the system inside feature work, and the production incident is the learning arc.
**Effects:** builds follow [context/brand.md](../../context/brand.md) ("Build sequences"): duplicate slides with identical layer names, Smart Animate 0.3s ease-out.

Every claim is checked against [evidence/experience-facts.md](../../evidence/experience-facts.md) (Remuner, "Design system and token pipeline"). Speaker notes are beats, not a script.

---

## 1. Cover

**Headline:** Building Remuner's design system inside feature work
**Sub:** Remuner, 2024 to 2026 · B2B sales compensation platform

**Notes:** Result first: I was Remuner's only designer. I built its design system alongside product work, and when I left in March 2026, 10 of 18 core screens ran on it.

---

## 2. Starting point

**Label:** Context
**Headline:** Each engineer had built their own components
**Visual:** product UI (looks fine) next to the implementation layer: per-engineer components, Vuetify defaults, zero Figma components.

**Notes:** Screens were designed one at a time by someone from a graphic design background. Every screen was built from scratch by whoever picked it up.

---

## 3. Constraint

**Label:** Constraint
**Headline:** One designer, and product work couldn't stop
**Visual:** timeline: 2 front-end engineers at hire, 5 at departure; one designer throughout.

**Notes:** Buy-in was easy; bandwidth was the constraint. Each new engineer copied the existing patterns, so the cost grew with every hire.

---

## 4. Scope, format, pipeline

**Label:** Decisions
**Headline:** Build what the product uses, in the format engineers already used
**Visual:** three columns: Scope (built vs deferred: dark mode, motion tokens) · Format (Sass variables and utility classes for Vuetify) · Pipeline (Token Studio → Style Dictionary → GitHub → Vuetify and Storybook).

**Notes:** Tighter scope than at Abacum. Foundations first, then the most-used form fields (TextField, Textarea, Select, then Autocomplete). The format came out of the monthly front-end meetings. Pipeline foundation from Abacum, adapted by the engineers.

---

## 5. Production incident

**Label:** Incident
**Headline:** I deleted a token file and took the app down
**Visual:** timeline: file deleted → next deploy → app down → file recovered → structural change.

**Notes:** Several minutes of downtime, visible to users and engineering. I had treated a production dependency like a design file.

---

## 6. Hardening

**Label:** Hardening
**Headline:** CI checks, drift detection and a preview sandbox
**Visual:** pipeline before and after: CI checks, drift detection, smoke tests, HTML preview, W3C token format, JSON output.

**Notes:** February 2026, built with Codex; an engineer reviewed and merged each stage.

---

## 7. Governance

**Label:** Governance
**Headline:** Monthly front-end meetings ran the system
**Visual:** meeting format: progress, open problems, goals for next month.

**Notes:** Staged deprecation: ranking tokens and the old Select marked before removal. Notion page for issues between meetings. No issue count recorded.

---

## 8. Audit

**Label:** Audit
**Headline:** An audit board tracked every core screen
**Visual:** audit board: pattern, instances, variants, ticket, fix now or defer.

**Notes:** Lint rule for token use, loosened to block only new violations, and a weekly component-count script fed the board. The team built both; I ran the script and set each screen's status.

---

## 9. Outcome (build: quote, then three outcomes)

**Label:** Outcome
**Headline:** 10 of 18 core screens on the system when I left
**Quote:** "From a 2010 app to a 2025 app" (the CTO, unprompted)
**Columns:** Coverage: 161 component sets, about 1,600 variants, 630 token variables, 157 icons · Consistency: tokens enforced in CI and lint; engineers named tokens in code reviews · New joiners: a designer and a PM worked from the library from the start
**Next time:** harden the pipeline before something breaks.

**Notes:** Coverage is not speed. If asked "how much faster?", say it wasn't measured.

---

## 10. For this role

**Label:** For [company]
**Headline:** What I'd bring to [company]'s product
**Visual:** two columns: principles from Remuner, and where each applies in the role's domain (from the JD).

**Notes:** Tailor per role before each use. The last tailored version (Factorial spinoff, July 2026) is in git history.

---

## 11. Close

**Headline:** What would be most useful to go deeper on?

**Notes:** Stop talking.

---

## Speaker notes

Keyed by slide number; match them to Figma positions before pasting. Actions sit on their own line, starting with ▶ and in [brackets]. Don't read those lines aloud.

**Slide 1 (Cover)**
I was Remuner's only designer. I built its design system alongside product work, and when I left in March 2026, 10 of the 18 core screens ran on it.
This case is about how one designer did that without stopping delivery, while the front-end team grew from two engineers to five.

**Slide 2 (Starting point)**
The product didn't look broken. The person who designed it came from graphic design, and decisions were made screen by screen, so there was no structure underneath.
The code matched. Each engineer had built their own components, with Vuetify defaults filling the gaps, and there were no Figma components. Every screen was built from scratch by whoever picked it up.
▶ [Short on time: one sentence.]

**Slide 3 (Constraint)**
Buy-in was easy, because the team could see the problem. The constraint was bandwidth.
Front-end headcount was going from two to five, and each new engineer would pick up the existing patterns and extend them. The cost of having no system grew with every hire. If I spent three months on infrastructure, three months of product work wouldn't happen, so the system had to grow alongside the features.

**Slide 4 (Scope, format, pipeline)**
Three decisions shaped it.
Scope: tighter than at Abacum. Build what the product uses now and extend when it needs more. Dark mode and motion tokens were deferred on purpose. Foundations came first, palette, spacing, radius and type, then the components the product used most: TextField, Textarea and Select. There was no standard Select, and auditing every select turned up autocompletes too, so Autocomplete came next. I wrote the tickets with the spec and the screens to update, and the new Select replaced the old ones as feature work reached each screen.
Format: the engineers worked in Vuetify, which uses Sass variables, so I exported tokens as Sass variables and utility classes. That came out of the monthly front-end meetings.
Pipeline: Token Studio, Style Dictionary and GitHub. The foundation came from my Abacum work, and the engineers adapted it to Remuner's stack.

**Slide 5 (Production incident)**
The token files fed straight into the front-end app. I deleted one I thought was a duplicate without checking whether anything referenced it. Something did, and the next deploy took the app down for several minutes, in front of users and engineering.
Recovering the file was quick. The bigger change was how I treated the repo: it was production infrastructure, and I'd been tidying it like a working folder.

**Slide 6 (Hardening)**
In February 2026 I hardened the repo with Codex, working through it step by step, with an engineer reviewing and merging each stage. It got CI checks that catch breaking changes before a deploy, drift detection, the W3C token format, an HTML preview, smoke tests and JSON output for JavaScript.
I defined what it needed and checked every output. The incident pushed forward work I should have done earlier.

**Slide 7 (Governance)**
Every month, each front-end engineer showed what they'd built, raised problems and set goals for the next month. It caught drift early, and the engineers ran the system with me instead of reading a doc I maintained.
We marked things before removing them. The flat ranking tokens were replaced by a structured ranking namespace, and the old ones stayed in the file marked for deletion. The old Select stayed on a page labelled "DEPRECATED → Select" so anyone still using it could find the replacement.
Between meetings, engineers and the product team logged component problems on a Notion page I set up.
▶ [No count of logged issues. Don't give one.]
▶ [Short on time: one sentence.]

**Slide 8 (Audit)**
I ran a continuous audit of the product: find every instance of a pattern, define the variants and states it needs, write the tickets, and decide whether to fix it now or fold it into an upcoming feature. Most of the judgment was in that last call.
The board also tracked adoption. Two checks in the code fed it: a lint rule that flagged styles bypassing the tokens, and a script that counted the components in each template. I ran the script weekly and set each screen's status from the counts and my own review. The lint rule started strict, and engineers ended up fixing old code just to get changes through, so we loosened it to block only new violations.
▶ [The team built the rule and the script. Weekly results aren't recoverable: describe the mechanism, never a trend.]

**Slide 9 (Outcome)**
When I left, 10 of the 18 core screens ran fully on the system. A few months into the audit, the CTO said, unprompted, that it had gone "from a 2010 app to a 2025 app".
▶ [Click, if built.]
The library had 161 component sets, about 1,600 variants, 630 token variables and 157 icons in their own repository. Tokens were enforced in CI and by the lint rule, and engineers started naming tokens in code reviews instead of hex values. A designer and a PM joined in my last months and both worked from the library from the start.
If I did it again, I'd harden the pipeline before something broke.
▶ [Coverage isn't speed. If asked how much faster: it wasn't measured.]
▶ [NEEDS YOUR STORY: one feature that shipped faster because a component existed.]

**Slide 10 (For this role)**
▶ [Write per role from the JD: two or three Remuner principles and where each applies in their product. Use their terms.]

**Slide 11 (Close)**
What would be most useful to go deeper on?
▶ [Stop talking.]

---

## Backup

The slides marked [SKIP] in the July version (full text in git history before 2026-11-09):
- **Applied lesson (old 4):** the deferred items. No dark mode (one value mode) and no motion tokens; the icon system lived in its own repository.
- **Same language (old 5):** a Figma token exported as `$color-text-primary` and `.text-primary`.
- **Pipeline (old 6):** three token tiers: branding (2 variables), core (417 primitives), product (189 semantic). Variables held colour and spacing; text and elevation styles sat alongside them.
- **Old outcome (old 11):** the domain layer: 21 chart sets, persona cards (Individual/Metric, Individual/Payout, Manager/UsersDetails), tiers, the AI assistant widget, the email template system.

---

## Q&A preparation

**"What would you do differently?"** Harden the pipeline earlier. I treated the token repo as a design asset too long, and it took an outage to change that.

**"How did you balance system work with product delivery?"** I built the smallest token set and governance that worked, then extended them as features exposed gaps. The monthly meeting, the ratchet lint rule and the weekly component count kept the board current without anyone stopping feature work.

**"How did this connect to business outcomes?"** With a growing engineering team and no system, each new feature was a one-off and each new engineer added inconsistency. The checkable signals are the 10 of 18 screens and the CTO's comment. Speed wasn't measured.

**"How was adoption measured?"** The audit board in Notion, fed by the lint rule and the weekly component count; I set each screen's status from the counts and my review. The weekly data isn't recoverable. Scale: 161 component sets, about 1,600 variants, 630 token variables (417 primitive, 189 semantic), 157 icons, 84 commits and 14 reviewed PRs to the token repo over 21 months.

**"What's different from Abacum?"** Abacum: co-led the business case, an engineer built the pipeline, five squads. Remuner: sole designer, adapted and owned the pipeline, smaller token scope on purpose. Same principles, smaller team, plus the lesson about treating the repo as infrastructure.

**"Did the system serve more than the product?"** The marketing website used the same core tokens plus its own semantic layer. I built its Figma library, designed pages and handed them to the agency that built the WordPress site, and kept it in sync by hand. Same brand on both. I also built a template kit so marketing could publish LinkedIn posts without me.

**"How did you handle accessibility?"** I normalised the palette in HSL with the Figma MCP, ran contrast checks and brought the colours the product used to WCAG AA. Errors carry a message as well as the red border. Limit: field focus was a border-colour change; buttons had a separate focus ring.

**Don't claim:** npm releases (say token updates or commits); a lint violation trend; a measured speed gain; full WCAG, keyboard or screen-reader conformance; contrast ratios for the muted and action text colours; multi-brand or white-label theming.
