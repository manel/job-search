# Wizeline stage 2: case (UX interview)

Index: [wizeline.md](wizeline.md). Deck talk track: [wizeline-case-deck.md](wizeline-case-deck.md).

- **When:** Fri 30 Oct 2026, 17:00-18:00 Madrid (10:00 Mexico City). Google Meet via the Greenhouse invite.
- **Interviewers:** Max Gutiérrez Liceaga, probably Associate Tech Director - Design (Mexico City; 2nd degree via Thiago Soares). Jesús Alonso Gutiérrez Ruiz, probably Lead Product Designer. Neither LinkedIn match shows the employer; confirm both work at Wizeline before the call.
- **Format (from David's email):** 15-minute case on one design-systems project (situation, task, actions, outcomes; your role and how you worked with the team; high-fidelity assets fine; no long paragraphs, no small or blurry assets). Then a 25-minute whiteboard challenge on a canvas you prepare and share. That's 40 of 60 minutes; expect about 20 minutes of questions.
- **What this round decides:** David said the Wizeline technical interview confirms Level 4 and leads to the offer. A down-level would cut the EUR 49K, so the bar here is a clear Senior, not Staff.

## What they most likely care about

1. **Depth on design-system decisions.** Two designers will push on why, not what: token structure, component props, what you deferred, how the system reached code.
2. **Working inside someone else's system.** The client runs a "core design system" with many designers on it. Can you contribute through governance you don't own: audits, deprecation, working with engineers, documentation?
3. **The JD must-haves they know you're thin on.** WCAG and multi-brand theming. The Index posting's client is news media and publishing, with multi-brand as a plus. Expect at least one of these to come up in the whiteboard or the questions.

## Case choice: Remuner (`remuner-ds`)

Use Remuner. The mapping in [playbooks/case-presentation.md](../playbooks/case-presentation.md#story-selection) ("Story selection") puts DS-first roles on Remuner, and it suits this brief better than Abacum for three reasons:
- **"Your role":** you were the sole designer and owned the tokens repo, so there's no co-ownership to hedge. Abacum needs "co-led with the head of design" and "worked on, not built" the pipeline, which costs time in a 15-minute slot.
- **WCAG:** the palette AA work lives here, and it matches written answer Q3. They've read it.
- **Recoverable numbers:** 10 of 18 core screens on system components, 630 token variables, 161 component sets, 14 reviewed PRs to the token repo, CTO quote. All from [case-deck-design-systems-remuner.md](../../decks/case-deck-design-systems-remuner.md) Q&A notes.

Keep Abacum (`abax`) ready for "how would this work at scale?" or "multiple teams": five squads, business case, migration off MUI, weekly library sync. Do not compare 47% against the 80% target (register conflict, unresolved).

**Deck cut, 15 minutes.** The existing deck runs 15-20 minutes before Q&A and ends on a Factorial slide. Seven slides, about two minutes each:
1. Context and your role (cover + slide 2): sole designer, engineers 2 → 5, no components or tokens on day one.
2. The constraint (slide 3): product work couldn't stop, so the system grew alongside it.
3. Three decisions (slide 4): small scope with dark mode and motion deferred, Sass + utility-class export chosen with engineers, the pipeline.
4. **New: palette to WCAG AA.** Inherited base colours, your shade ramps, HSL normalisation, contrast checks, AA over visual consistency where they clashed, rolled out section by section. Source: [context/remuner-case-additions-2026-10-20.md](../../context/remuner-case-additions-2026-10-20.md) A. Needs a visual: before/after ramps or contrast results from Figma.
5. Incident and hardening (slides 7-8): the deleted token file, then CI, drift checks, smoke tests, engineer-reviewed. Say Codex/Claude plainly.
6. Governance and audit (slides 9-10): monthly FE meetings, mark-before-delete (ranking tokens, Select), audit board as adoption tracker.
7. Outcome + what you'd do differently (slide 11). Close on the trade-off, not the artifact list.

Use big Figma screenshots, not text. Drop slide 12 (Factorial).

## Likely questions mapped to material

| Question | Use |
|---|---|
| Why that token structure / why so few tokens? | Deck slide 4 and 4-OLD: Abacum lesson, build what the product uses. |
| How did engineers actually consume it? | Tokens repo as submodule of the app; Sass + utility classes from the FE meetings; your PRs replacing hardcoded styles (register, 2026-10-20). |
| How did you handle accessibility? | Palette to AA. Stop there: no keyboard, screen-reader or full WCAG 2.2 conformance claim. If pressed beyond colour, answer from principle and say so. |
| How would you support multiple brands? | **Gap.** No shipped multi-brand system. Answer from principle: brand as a layer above semantic tokens (Figma variable modes per brand, components bound only to semantic tokens). Remuner's separate branding collection (two brand colours) is the seed of that idea; don't stretch it into theming you shipped. |
| A team wants to go custom / two teams forked a component | Your written answers Q1 and Q2. Stay consistent with what you wrote; Remuner Select deprecation is the real example. |
| Tell us about a mistake | `token-file`. Already in the deck, so keep it short in Q&A. |
| Who did what? | Remuner: you owned brief, tokens repo, Figma library, audit; engineers adapted the pipeline and reviewed your PRs. Never sole pipeline authorship. |
| How did you measure it? | Audit board: 10/18 screens. Never npm releases or an ESLint violation trend. |
| How do you use AI in DS work? | Figma MCP with Codex then Claude: variants with props matching code, Storybook views, docs, palette normalisation. One umbrella line, then examples if they ask. |
| What did Abacum add? | `abax`: scale, business case, five squads. Co-led. |

**Consistency check from the screen:** you told David you were "owner or lead" at both companies and can "push code to production to move a metric". With designers in the room, say co-led at Abacum, and describe code work as engineer-reviewed PRs fixing styles and tokens.

## Whiteboard: prepare the canvas, not the answer

Prompt unknown. Likely candidates (inference): a component or pattern for a multi-brand publishing product, an extension of the written scenarios (custom vs variant, forked data table), or a general product problem.

Build a FigJam board before Friday, with empty labelled frames in this order:
1. **Brief:** paste it verbatim.
2. **Framing (first 3-4 min):** task · signal (the number or break point they give) · problem statement citing it · metric baseline → target + one guardrail. Rule from Alan ([memory.md](../../memory.md) 2026-10-16 and 10-22): the panel should never have to supply this.
3. **Who and what breaks:** consumers (product designers, engineers, end readers), and the 2-3 challenges that could break it, named before drawing.
4. **Direction:** where this should end up (vision first, per Factorial), then what you'll cover in this session.
5. **Solution:** for a DS prompt, anatomy → variants and states → tokens → accessibility → props/API → rollout and deprecation. For a product prompt, flow first, then screens.
6. **Not doing, and how we'd know it worked.**

Timebox for 25 minutes: framing to ~4, direction to ~8, solution to ~19, rollout/a11y to ~23, metric and close to 25. Say the step aloud when stuck. Expect one deliberate pushback. Test screen-share of the FigJam board in Meet before Friday.

## [NEEDS YOUR STORY] gaps this round may hit

- **One feature that shipped faster because a component existed** (Remuner deck slide 11, NEEDS INPUT). The most likely "outcome" probe. Find it before Friday or say you don't have it.
- **Accessibility gap found after shipping** ([question-bank.md](../question-bank.md#gaps-no-direct-material-do-not-invent), enterprise gaps). No story. Principle only.
- **Disagreeing with your manager** ([question-bank.md](../question-bank.md#10-a-time-you-disagreed-with-your-manager-and-what-you-did) Q10). No story; `manager-view` is the closest.
- **Kings of Mambo incidents** ([stories.md](../stories.md#gaps)). A consultancy panel may ask about client work. Not fleshed out; don't improvise one.

## Questions to ask them

Pick two:
1. "On the client's core design system, who owns decisions: the client's own DS team or Wizeline's designers?" Tells you whether this is contribution or ownership.
2. "How far along is the multi-brand side of the system, and what's the biggest gap in it right now?"
3. "What separates a Wizeline designer who does well on an account like this at 12 months from one who's just good?"

Don't ask about the client hiring freeze here; that's for David.

## Salary

Already settled at the screen: Level 4 entry EUR 49K, which you called aligned. If it comes up: "David shared the Level 4 range and it works for me." Don't reopen it, and never mention a floor or prior pay.

## After the call

Run `/debrief-interview wizeline ux-interview` the same evening.

## Debrief (2026-10-30)

Source: Manel's account after the call.

**Format as run**
- Case presentation given (Remuner deck). No whiteboard challenge: the panel used that time to look at how Manel's files were structured. Manel showed examples of implementation files.

**Feedback given in the call**
- The presentation was good.
- They wanted to see how the components were built following atomic design. Manel answered by opening the files and walking through them.
- Missing from the presentation: what Manel would bring to the table. The next round is a meeting with the client, and the panel said that part matters because clients want proof of why they should hire a designer.

**Prep vs. what came up**
- Not covered by the prep: a live walkthrough of the Figma file and component construction (atomic design), and a client-facing value pitch.
- The whiteboard canvas prepared for this round went unused.

**Process**
- Decision expected within two days at most (by Mon 2 Nov).
- Next round, if passed: client meeting. No news on when; the client's hiring freeze (reported 23 Oct) was not addressed.
