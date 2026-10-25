# Enginy: Senior Product Designer

Record: `applications/records/enginy-product-designer.md`. CV source: `cv/roles/enginy-product-designer.md`. Cover letter: `cover-letters/roles/enginy-product-designer.md` (what they were told: Remuner sole designer, AI agent, Codex token pipeline via reviewed PRs, CMS front ends, Dataset Manager).

## Round 1: Recruiter screen

- **When:** Mon 26 Oct 2026, 11:30-12:00 Madrid. Google Meet meet.google.com/njk-uojp-rkf.
- **Interviewer:** Saul Villa, Manager, Talent Acquisition at Enginy (since Feb 2026; about four years recruiting at N26 before that).
- **Purpose of this round:** filter. Saul checks the must-haves a recruiter can tick: level, maker bar, English, on-site, money, availability. Short answers, one proof each, then stop. He asked for full-hour slots but booked 30 minutes, so expect a fast pace.

### What Enginy most likely cares about

1. **Maker bar, taken literally.** Diogo Rendeiro's post ("push PRs, not pixels", "Shipped a PR last week? DM me") and Damián Rodrígues's deck (about 90% of his designs go to production through his own PRs in Cursor or Claude Code; components built first in Storybook). Saul reposted Diogo, so he will screen for it.
2. **End-to-end ownership with a metric.** Damián's process starts from a Linear issue, sets a target metric before designing and measures it in Datadog. "Moved means done."
3. **Practical fit:** on-site Barcelona ("Onsite in sunny Barcelona"; 48 WFH days a year), Senior level, salary.

### Lead story

Positioning mapping (`context/positioning.md`), AI product lane, because Enginy is AI-enabled sales software: **Remuner AI agent** first. It is the domain match: sales compensation, a production agent shipped to all customers, sole designer working with founders and engineers, no PM. Follow it with the **maker proof** (Story C plus Kings of Mambo), since that is the bar Saul is screening for. Dataset Manager (Story A) is a backup if he asks about dense data workflows.

### Likely questions mapped to stories

| Question | Use |
|---|---|
| Walk me through your background | `prep.md` "Opening intro: Work and history". Add one line: years of production front-end code at Kings of Mambo, own code, self-deployed. That answers the maker question before he asks it. |
| Why are you looking / why did you leave Remuner? | `prep.md` "Priority zero". Say it and stop. |
| Why Enginy? | `prep.md` Q11 framework. Honest anchors: sales software you already know from Remuner; AI behaviour design; designers shipping their own work. **Decide before the call whether you actually want primarily on-site, outbound-sales software**; the record has this unconfirmed. |
| Do you code / have you shipped PRs? | Remuner: PRs to the front-end app replacing hardcoded styles with tokens, written with Claude, reviewed by the front-end team; token pipeline extended with Codex (CI, drift checks, smoke tests), reviewed and merged. Kings of Mambo: HTML/CSS/JS, jQuery, PHP, WordPress, October CMS; own code, self-deployed; Kymco checkout took real orders. **Limit:** React/TypeScript only with substantial AI help. If asked directly, say so; it matches how their team works (Cursor plus Claude Code). |
| How do you use AI in your work? | Figma MCP with Claude for tokens, parity checks, accessibility audits, documentation; AI-built prototypes users tested at Remuner (not connected to production); this Claude Code and MCP setup in daily use. |
| Tell me about the impact of something you shipped | AI agent: shipped to all customers; **no adoption or accuracy metrics on record.** Name the qualitative signal and say there was no instrumentation. Don't claim you "pushed code to move a metric" (you said this at Wizeline; the register doesn't support it). |
| Your design system experience | Story C (Remuner, from scratch), Story B (Abax, co-led with the head of design). Two sentences each. |
| On-site, five days? | You accept on-site (2026-10-19). Ask what the normal week is. |
| English | C1. |
| Availability | Available immediately (same answer as Perk and RemoFirst). |
| Other processes? | Yes, a few at interview stage. Don't name companies or stages unless it helps. |
| Salary | See below. |

### [NEEDS YOUR STORY] gaps this round could hit

- **Q10, disagreement with your manager:** no story in the library. Unlikely in a recruiter screen; if it comes up, use the "no SQL" call (Story A, Q3) instead of inventing one.
- **Story E (Kings of Mambo incidents):** not fleshed out. The missed-deadline story (Q2) is the only ready one.
- **Metric-first framing:** not a library gap but the weak spot from Damián's deck. Have one sentence ready that names the metric a project was meant to move, even where the evidence was qualitative (for example the Remuner IC dashboard: reps confusing displayed commission with the amount payable).

### Questions to ask Saul

Ask the range first if salary comes up (below). Then:

1. **Office:** "The posting says in-person with 48 remote days a year. What does a normal week look like for the design team?"
2. **Level and process:** "The posting title changed from Product Designer to Senior. How is the role levelled, and what are the next rounds? Who runs them, and is there a hands-on or build exercise?"
3. **Team:** "Who would I work with day to day? Is it a pod with a product engineer, and who leads the design team?" (Diogo is likely the hiring manager; inference, don't name him unless Saul does.)

### Salary position

- **Already stated:** EUR 62,000 gross annual (application form, 2026-09-15). Range: unknown.
- Ask the range before repeating a number: "I put 62 on the form. What's the band for this role?"
- If the band is lower, stay open without naming a figure ("that can work depending on the full package"). Saul came from N26; expect a structured band.
- Never: previous salary, the private floor, any mention of needing income soon.

### After the call

Run `/debrief-interview enginy screen`. Log the range, what you stated, office cadence, level and the next rounds in the record.
