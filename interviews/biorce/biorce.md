# Biorce: Interview Notes

Senior Product Designer. Applied 2026-07-24 via Estefania Galvan's referral (former Abacum colleague, Growth Marketing Manager at Biorce). Screen call email received same day.

---

## Round 1: Recruiter / Talent screen
**Date:** Tuesday, July 28, 2026, 12:25 PM to 12:50 PM (GMT+2 / Europe Madrid), confirmed via calendar invite
**Interviewer:** Akeel Hussain, Talent/recruiting (email signed "Best, Akeel Hussain", contact akeel.hussain@biorce.com). Confirmed as a recruiter screen, not the hiring manager, per the email's tone and the note that "our interviewer" will confirm availability separately, suggesting Akeel is coordinating rather than the one evaluating design work.
**Format:** 25 minutes, video, Google Meet. Confirmation email with details to follow once the interviewer accepts.

### What Biorce most likely cares about (this round)
- Genuine motivation for an AI-native healthtech company when the domain (drug development, clinical research) is new territory. The cover letter named this honestly; expect it to get probed directly at a screen stage, not deferred to later rounds.
- AI/Claude fluency as lived practice, not a checkbox. The JD asks for "proficiency with Claude or willingness to quickly learn" and lists Claude Design/Figma Make as nice-to-haves. This is the strongest match in the application; be ready to go deeper than the letter did.
- Logistics: salary, availability, remote/hybrid expectations. First screens usually cover this explicitly.

### Lead story for this round
Story C (Remuner AI agent + CTO relationship) for the AI/Claude match, same lead as the written package. If pushed on domain-specific product reasoning, bring in Story A (Dataset Manager) as the complex-data-domain parallel: a non-technical user needing to act on rule-governed data without engineering support generalizes cleanly to clinical data.

### Likely questions → story map
- "Walk me through your background" → prep.md "Work and history" intro (client work at KOM, then Abacum, then Remuner as sole designer, left in March)
- "Why Biorce, why this domain?" → Q11 framework: one structurally interesting thing about AI-native drug development (not "I love your mission"), one alignment with your background (complex, data-heavy B2B systems work), one honest note that clinical research itself is new territory, same as the cover letter
- "Why did you leave Remuner?" → Priority zero answer, memorized version, do not deviate
- "Tell me about your experience with AI tools" → Growth Q21/Q22: Claude-assisted Style Dictionary implementation with engineer sign-off at each step, Figma Make in daily practice. This is the one place to go further than the cover letter did, since it's the JD's clearest ask
- "What are your salary expectations?" → already stated 78,000 EUR on the application form; hold at that number, no range

### [NEEDS YOUR STORY] gaps this round could hit
- Accessibility/WCAG: the JD names it three times (champion accessibility throughout, WCAG understanding, inclusive design as a core principle). No documented incident exists in cv-base.md or prep.md's enterprise gap list. If asked directly, do not claim specific WCAG work; answer from general craft principles and be straightforward that it isn't a documented strength.
- Q17 (what does a bad day look like) has no finalized honest answer in prep.md; low risk for a first screen but worth having a real answer ready before any round that goes deeper on culture fit.

### Questions to ask them
At 25 minutes with a recruiter, there's likely time for one, not three. Lead with:
- What does the process look like after this call, and who would the next round be with?

Save these for a hiring-manager or design round instead, they need someone who actually works in the product to answer well:
- The JD mentions working closely with an existing user research and design system team. How does this role's scope split from theirs day to day?
- How much does the clinical/regulatory context constrain the interface work in practice?

### Salary reminder
€78K (salary.md, conservative-anchoring floor). Already stated as 78,000 EUR on the application's salary expectations field. Hold at that number if asked again; the JD's stated bar (4-6 years experience) reads softer than a clean Senior floor, so don't volunteer anything higher.

*After this round happens: run `/debrief-interview Biorce "Round 1"` while it's fresh.*

---

## Round 2: Speculative, not yet confirmed

Nothing about this round is scheduled. No interviewer, format, or date exists yet, this only exists because Manel asked to prep ahead "just in case." Treat every assumption below as provisional; re-check against whatever Biorce actually sends once Round 1 concludes.

Manel's own read on the process (2026-07-24): passing a recruiter screen is the norm, not the exception, at this stage. If it doesn't convert, the likelier cause is something like a salary or logistics mismatch rather than the interview itself going badly. Worth remembering if Round 1 doesn't advance: check for a mismatch signal (recruiter pushing on the 78,000 EUR number, availability, or location/hybrid expectations) before assuming the conversation itself was the problem.

### Best guess at format
Biorce's JD already asked for a portfolio link as part of the application ("Portfolio demonstrating thoughtful problem-solving and design process, please share a link") and names presenting to leadership as a core responsibility. Manel's expectation, and the more likely shape: Round 2 is a case presentation with the hiring manager or head of design, and a live design challenge, if one exists in this process at all, would come later as a Round 3, not here. Nothing in the JD signals an on-the-spot brief (no "whiteboard," no timed exercise language), so treat a live challenge as a distinct, separate, and less certain later stage rather than folding it into this round's prep.

### What Biorce most likely cares about (this round)
- Depth on the same two things from Round 1, now with room to go further: the AI agent's trust and scoping decisions, and genuine motivation for the domain.
- Design process and judgment, not just outcome. The JD explicitly wants someone who can "defend design decisions," so expect follow-up pressure on the harder calls, not just a narrated walkthrough.
- Whether you're a self-starter who operates with minimal direction, comfortable with ambiguity. Listen for questions probing how you'd behave without a fully-specified brief.

### Lead story for this round
Story C (Remuner AI agent), now at full depth using `interviews/decks/case-deck-ai-agent.md`. The deck's "restraint hero" framing (scoping the agent narrow under competitive pressure, defending that boundary, the custom-code blind spot as the real failure) is built for exactly this kind of walkthrough. Screen-share the live portfolio case page (manel-leiva.com/cases/ai-agent.html) rather than the deck file itself. It already has the real images (hero, formats, loop, reach diagrams) committed and deployed; the deck's own visual assets are still unfinished and aren't needed to use this story well in a conversational walkthrough.

Keep Story A (Dataset Manager) ready as the second, non-AI case per prep.md's own advice: if the conversation wants a second example, or wants to test product judgment outside the AI framing, this is the one that shows research-driven direction change and a defensible "no" to a stakeholder.

### Likely questions → story map
- "Walk me through a project, start to finish" → Story C via the live portfolio case; use the deck's slide order as your internal structure (context, role, scoping decision, architecture boundary, trust/answer anatomy, where it broke, feedback loop, outcomes) even without showing slides
- "What would you do differently?" → deck Q&A prep: answer-level data freshness in the first release, and pushing earlier to map the custom-code blind spot
- "How do you know the scoping decision was right?" → deck Q&A prep: no A/B test on the boundary, the signal was structural, not proof
- "Who else was involved, what was specifically yours?" → deck Q&A prep: no PM, CEO/CTO plus engineering plus Manel on scope; the multi-agent orchestrator was engineering's build, describe it, don't claim it
- "Isn't 'no metrics' weak?" → deck Q&A prep: reframe, an honest absence beats a decorated number, name what's actually checkable
- "Why did you leave Remuner?" → priority zero answer, same as Round 1, don't improvise a variant
- "Tell me about a decision with no clear answer" or "influence without authority" → Story A or Story D as backup if the AI case doesn't cover it directly

### [NEEDS YOUR STORY] gaps this round could hit
- Same accessibility/WCAG gap as Round 1: no documented evidence, don't claim it if a case walkthrough turns toward inclusive design specifics.
- If this becomes a live challenge after all: read `interviews/prep.md`'s "Live design challenge" section before going in. Vision before scoping, the Factorial lesson. Don't default to validation-first framing.
- Q10 (disagreed with your manager) and Q17 (bad day at work) are still unfinished in prep.md; low risk for a portfolio walkthrough but worth having real answers before any round that goes deeper on culture fit.

### Questions to ask them
- What's the most important design problem that's currently unsolved in the product? (held over from Round 1's "save for later" list)
- The JD mentions working closely with an existing user research and design system team. How does this role's scope split from theirs day to day?
- How much does the clinical/regulatory context constrain the interface work in practice?

### Salary reminder
Same as Round 1: €78K, already stated on the application form. Hold at that number if it comes up again.

*Once Round 1 happens and any actual Round 2 details arrive, come back and correct everything above rather than trusting this speculative version.*

---

## Round 3: Even more speculative, live challenge if it exists

No signal yet that this round exists at all. Flagged only because Manel expects a possible later live-challenge stage after the case presentation, not folded into Round 2's prep above.

If it happens: read `interviews/prep.md`'s "Live design challenge" section in full before going in, not just skimmed. The core lesson, learned the hard way at the Factorial rejection (2026-07-02): vision before scoping. State what the product needs to be to win, in writing, before opening any design tool. Validation-first, scope-down-first framing reads as junior even when it's the operationally correct answer. Do the pre-challenge checklist in that section (write the vision answer first, make it visible on a labeled page, lead the presentation with it) rather than defaulting to the disciplined-scoping instinct that cost the round there.

*Not worth further detail until there's an actual signal this round exists.*
