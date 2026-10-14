# Spendesk hiring manager interview questions

**Interview:** 17 September 2026, 11:30 CEST, with Cyrièle Piancastelli, Head of Product Design  
**Role:** Confirmed Product Designer  
**Format:** The role page describes a portfolio presentation and discussion. The meeting is 45 minutes; the exact agenda is unknown.

Use this as a prompt sheet, not a script. Ask two or three questions that the conversation has not already answered. For your own answers, lead with the decision and its reason. Then explain the alternative, your part in the work, and the result.

The [current Abax deck](https://www.figma.com/slides/ae1SMrxEXfMMdUygkGTMcH/Abacum-DS) has 10 main slides. Slides 3-4 cover the business case and staffing choice, slide 5 shows the Button proof, slide 6 covers roadmap priorities, slide 8 covers migration, slide 9 covers outcomes, and slide 10 is hypothetical LLM work. The deck does not include customer research; keep Dataset Manager ready as a short supporting case.

## Questions to ask Cyrièle

### Ask first if time is short

1. **Which product area would this designer join, and what is the hardest workflow the team is trying to improve?**
   This tests the actual product scope behind the broad job description.
2. **Why is the design system a priority now? Where are teams running into problems with it today?**
   Listen for a component gap, weak documentation, adoption problems, or unclear ownership. They call out all four in the role description, but the current state is unknown.
3. **How would you expect this person to divide their time between squad work and design-system work? Who decides when those priorities compete?**
   The role combines both. The answer will show whether the system work has real capacity and decision rights.
4. **What would you want this person to have changed after six months? How would you know it was working?**
   Ask for a concrete outcome, not a generic description of success.

### Use if the conversation leaves room

5. **What decisions would a designer at the Confirmed level own independently? How does that differ from Lead here?**
   This gives you a better read on scope than the title alone.
6. **How do designers get access to finance users and to product data when they need to test a decision?**
   The role promises research and iteration. Check what is practical in the team.
7. **For AI or automation work, where do you want the user to stay in control?**
   This opens a useful discussion about transparency and error handling without assuming Spendesk's current solutions.

## Questions Cyrièle may ask

These are predictions based on the role description and the Abax deck, not questions Spendesk has confirmed. The first group is the one to rehearse aloud.

### The likely why questions about Abax

| Question | What your answer needs to cover |
| --- | --- |
| **Why build a design system when squads already had MUI?** | Repeated local implementations made shared changes expensive. Abax added product patterns on top of MUI. Do not claim that the product was unusable. |
| **Why spend engineering time on this instead of a customer feature?** | Show the buttons, cells, and menus that differed. Explain the maintenance cost you argued for. The trust concern was a risk in the business case, not a measured customer outcome. |
| **Why seek a Maker Days week?** | Normal squad work left little dedicated time. A focused week gave Design and Engineering room to test one path to production. You and the Head of Design co-led the case. Do not imply you alone secured the capacity. |
| **Why choose a larger team for one week over a smaller team for two weeks?** | Slide 4 shows the actual options: 2 frontend engineers and 1 designer alongside sprints for two weeks, or at least 4 frontend engineers and 2 designers for one dedicated week. The team used Maker Days for a bounded production test. The tradeoff was more concentrated capacity away from squad work. Do not claim the team calculated ROI or that the smaller plan would have failed. |
| **Why start with tokens, and when did you stop refining them?** | Tokens connected design decisions to code. Once that path worked, missing components and variants became the more immediate barrier to adoption. This is the prioritisation decision on slide 6. |
| **Why was Button the first component?** | The deck supports that Button was the first end-to-end production proof. Your exact selection criteria are not recorded in the source notes. Explain them only if you remember them clearly. |
| **Why keep MUI underneath Abax?** | Replacing a framework already used by five squads meant a broad rewrite. Extending it let the team improve consistency without stopping product delivery. |
| **Why use two token layers?** | Primitive values held the raw values; semantic names described where they belonged. Give one concrete example if asked. Keep your ownership separate from the Head of Design's final colour and font-token work. |
| **Why release form elements behind flags and leave migration to squads?** | Teams could switch in stages and find edge cases before wider use. Squads owned their product backlogs, so migration had to fit their capacity. |
| **Why separate Exploration and Implementation in Figma?** | Designers needed room to test ideas without making unfinished components appear production-ready. The Implementation library was the published source. |
| **Why keep deprecated components visible?** | Existing files still used them. Marking them clearly let designers find the replacement while teams moved off the old component. The old version was unpublished later. |
| **Why set an 80% target, and what did 47% tell you?** | The goal was for Abax to account for 80% of tracked Abax and MUI component uses across the codebase. Frontend engineers counted those uses monthly with custom scripts. The roughly 47% figure at departure is reconstructed, with no raw export available. Two squads had completed form migration and a third was partway through. The record does not establish why the team chose exactly 80%. |
| **Why was migration unfinished? What would you change now?** | Adoption depended on squad backlogs. You would preserve tracking evidence more carefully and settle token-naming rules earlier. Do not invent a missed deadline or a quantified cost. |

### Ownership and judgment

| Question | What your answer needs to cover |
| --- | --- |
| **What did you personally own?** | Co-led the business case with the Head of Design; worked on token architecture, Figma structure, governance, and design decisions. An engineer built the original token pipeline. |
| **What did Engineering push back on, and how did you respond?** | Their recorded concerns were a side project, competition with squad priorities, and lack of a platform-wide view. Slides 3-4 show the bounded test and the capacity options. Explain the choice without claiming a quantified financial case. |
| **What would you cut if you had half the time?** | Name the smallest production proof and the adoption problem it would test. This is a judgment question; do not pretend the team actually ran a half-length version. |
| **How did you know the system helped?** | Slides 9-10 show codebase counts, the designer's screen-building feedback, named tokens in code, and the migration state. Separate those operational signals from measured time savings or customer outcomes, which you do not have. |
| **What was a decision you got wrong or changed?** | The shift from token infrastructure to usable components and variants is a grounded example. Explain what signalled that shift. Avoid presenting a normal priority change as a dramatic failure. |
| **How would you use LLMs on Abax now?** | Slide 10 is hypothetical. Describe Figma context, reviewed token and component changes, documentation, and a code PR with engineering review. Your later Codex work on Remuner's token repository is real supporting experience, with engineers reviewing and merging it. |

### Questions beyond the deck

| Question | Best story to prepare |
| --- | --- |
| **Tell me about a complex workflow you owned from problem to delivery.** | Dataset Manager. The Abax deck does not answer this on its own. Explain the users, finance concepts, constraints, validation, and what shipped in about two minutes. |
| **Tell me about a research finding that changed your design.** | Dataset Manager's finance-language and configuration decisions. Be precise about what users said and what changed. |
| **How do you balance user needs, business goals, and engineering limits?** | Choose one concrete decision from Dataset Manager or Abax. State the rejected alternative. |
| **How do you design AI features users can trust?** | Remuner AI agent: capability boundaries, answer formats, refusals, and feedback. Do not claim the agent calculated commissions or that you measured adoption or accuracy. |
| **Why Spendesk?** | Connect your interest in financial workflows, systems work, and responsible automation to a specific problem you heard from Cyrièle. Do not recite the job description. |
| **Why this Confirmed role, given your experience?** | Explain that you care about the actual problem and ownership. Ask about the scope. Avoid saying title does not matter if the role would in fact be too narrow for you. |

## Follow-up pattern to practise

For any major decision in the deck, expect a second question:

1. What problem made you act?
2. What else did you consider?
3. Why did you choose this option then?
4. What was your part in the decision and delivery?
5. What evidence did you have afterward, and what remains unknown?

The most exposed answers are **why Button first**, **why 80%**, **what 47% meant**, and **why a dedicated week justified taking more people away from squad work**. The records establish the staffing options, the first shipped component, and the adoption target. They do not establish the exact rationale for choosing Button or the 80% threshold. Recover your own reasoning before the interview. Do not fill gaps with a plausible story.

## Sources

- [Spendesk role description](https://career.spendesk.com/jobs/8209958-confirmed-product-designer), checked 16 September 2026. It describes the portfolio stage and the role's product, design-system, research, and AI scope.
- `interviews/spendesk/spendesk-hiring-manager.md` and `applications/records/spendesk-confirmed-product-designer.md` for confirmed interview details and preparation boundaries.
- `evidence/experience-facts.md` and the Abax notes in `context/design-systems-notes.md` for ownership and outcome limits.
