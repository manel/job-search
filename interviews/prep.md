# Interview Prep

This file covers the full interview surface: behavioral, culture fit, growth, case presentation, and ways-of-working rounds. Built from actual CV and positioning context. Gaps marked [NEEDS YOUR STORY] where I don't have the real detail.

---

## How to use this

The goal is not to memorize answers. It is to know which story fits which question well enough that you can reach for it without hesitation. The stories repeat. The angle changes.

Before any interview, re-read the role JD and note which of the four stories below is most relevant to that company's context. Lead with that one.

---

## Core story library

These are the 4-5 stories that cover most behavioral and culture fit ground. Know them cold. Everything else maps to one of these.

### Story A: Dataset Manager (Abacum, Integrations)

The setup: joined as first designer on integrations squad. Finance teams couldn't configure their own data without engineering support. Initial assumption was that the product needed a better UI.

The turn: ran structured user research across multiple sessions. Found a fundamental language mismatch. Finance people didn't think in product terms; they thought in dataset terms. The problem wasn't UI; it was conceptual vocabulary.

The decision: made the call not to introduce SQL, which was the obvious power-user solution. Extended the modeling syntax instead. Lower ceiling, but much lower learning curve for the actual users.

The outcome: enabled autonomous configuration without engineering support. Unlocked a follow-on editor suggestions project.

Use for: changed approach mid-project, decision with no clear answer, delivered bad news (the "no SQL" call), systems-level thinking, research-driven direction change.

---

### Story B: Abax DS (Abacum, cross-squad)

The setup: no design system mandate. Product was running on ad-hoc components across five squads. Inconsistency was accumulating but nobody had been asked to fix it.

The move: co-led the business case with head of design. Didn't wait for a ticket. Built the ROI argument, presented formally to engineering leadership. Got buy-in.

The build: two-tier token architecture. Token Studio to Style Dictionary to GitHub to npm. ESLint for adoption enforcement. Kept MUI as base to reduce scope and accelerate adoption rather than build from scratch.

Use for: influence without authority, going above and beyond, cross-functional alignment, owning a problem without a mandate.

---

### Story C: Remuner DS + CTO relationship

The setup: sole designer at a startup. No infrastructure, no prior system. Had to build everything from context at Abacum but with a smaller budget and no engineering team to rely on.

The approach: deliberately small token set. Lessons from Abacum applied: complexity is a debt you pay later. Used AI assistance for the pipeline implementation, had engineer sign-off on each step.

The outcome: CTO described the before-and-after as going from a 2010 app to a 2020 app. That quote exists because the change was visible to someone technical who previously had no strong opinion about design.

Use for: earning trust quickly, above and beyond, working without authority, making decisions with no playbook, startup context.

---

### Story D: Modeling Syntax (Abacum, Engine squad)

The setup: moved to engine squad. Identified, with the head of design, that formula syntax across Abacum's modeling layer was inconsistent. Not a ticket that came from product. An observation.

The work: competitor benchmarking. Synthesized evidence from customer call recordings. Collaborated directly with one engineer on syntax decisions rather than going through PM.

The outcome: standardized the syntax. Unlocked a follow-on editor suggestions project. The work itself created demand for the next thing.

Use for: decision with no clear answer, influence without authority (working directly with engineering), identifying problems above your assigned scope.

---

### Story E: Kings of Mambo / client work [NEEDS YOUR STORY TO FLESH OUT]

11 years of client work. Teaching UX at postgrad level. This is where your "stayed motivated on projects you didn't choose" answers live, your "dealing with stakeholders who don't listen" answers, and probably your most honest "project that failed" and "missed a deadline" answers.

Pick 2-3 real incidents from KOM that are usable in a senior IC interview. Flag the ones you're comfortable telling publicly. The KOM period is underused in these prep materials.

---

## Priority zero: "Why did you leave Remuner?"

This question will come up in every process. The departure was company-initiated (March 2026). [NEEDS YOUR ANSWER — before any screen, this outranks every other gap in this file.]

What a workable answer requires:
- Honest without volunteering the word "fired". "The company ended the role" / "we parted ways" framing, said evenly, is accurate and normal at startups.
- One factual, neutral sentence about context (restructuring, runway, fit — whatever is true), with zero bitterness and zero defensiveness. Interviewers read tone more than content here.
- Pivot immediately to evidence the work was valued: sole designer for nearly two years, the system shipped to production, the CTO's unprompted before/after assessment. Then stop talking. Over-explaining reads as guilt.
- Never criticize Remuner, the CTO, or the decision. One bitter word costs more than the firing itself.

Rehearse this out loud until it's boring. The goal is that it sounds like a fact, not a wound.

---

## Behavioral questions

### 1. Tell me about a project that didn't go as planned.

Use: Story A (Dataset Manager)

The research didn't confirm the original hypothesis. I went in expecting a UI problem. The sessions showed a vocabulary problem. The plan had to change before any screens were designed.

What went wrong: the initial scoping assumed users would adapt to product language. They wouldn't. The product needed to adapt to their mental model.

What changed: scrapped the SQL direction that was already half-specced. Extended the existing modeling syntax instead. The scope shifted, the timeline shifted, the output was different from what was originally expected.

Do not: make this sound like a heroic pivot. Frame it as: a research process working correctly to surface a real constraint before it became a shipped mistake.

---

### 2. Tell me about a time you missed a deadline. What happened?

[NEEDS YOUR STORY]

A real one from KOM or Abacum. What I'd look for in a good answer: the reason was a constraint that wasn't visible at scoping (not negligence), you communicated early rather than late, you made a call about what to ship and what to defer, the stakeholder relationship survived.

Avoid a story where the miss was your error and there was no learning. Avoid a story that's too small to be interesting at senior level.

---

### 3. Describe a time you had to deliver bad news to a stakeholder.

Use: Story A (Dataset Manager, the "no SQL" call)

The stakeholder framing: a PM or stakeholder wanted the more powerful feature. SQL would have given power users more control. You had to deliver: "we're not building that."

The argument: the data didn't support it for the actual user base. The right solution for a small segment would have made the product harder for the majority. Made the case with research evidence, not opinion.

The reception: not every stakeholder agreed immediately. The work was to show the reasoning, not just the conclusion.

---

### 4. Tell me about a time you had to make a decision with no clear answer.

Use: Story D (Modeling Syntax) or Story A (Dataset Manager, SQL decision)

Modeling Syntax is the better one here. There was no established pattern for how to standardize formula syntax in a product like Abacum. No competitor had solved this cleanly. The answer came from benchmarking, customer recordings, and direct collaboration with an engineer. The decision was a judgment call at the end, not a derivable answer.

State that explicitly: "there was no right answer in the literature. I had to build enough evidence to make a defensible call and move."

---

### 5. Describe a situation where you had to influence without authority.

Use: Story B (Abax DS)

No ticket. No mandate. The business case was built by me and the head of design, presented to engineering leadership. Engineering had no obligation to prioritize this. The argument had to be good enough that they chose to.

The angle: influence without authority is not persuasion tricks. It is building evidence that makes the right decision obvious to the person with authority.

---

### 6. Tell me about a time you failed publicly. How did you recover?

[NEEDS YOUR STORY]

This one matters. A story that's actually a stealth success won't work here. The interviewer is testing for self-awareness and resilience, not whether you've had failures.

Requirements for a good answer: something visible to others (not an internal misstep you quietly fixed), a real consequence, a clear account of what you learned, evidence that you changed something as a result.

---

### 7. When have you had to change your approach mid-project?

Use: Story A (Dataset Manager)

Straightforward mapping. Set up: what the original approach was. Trigger: what the research showed. Change: what you did differently and why. Outcome: what shipped.

Keep it concrete. Don't editorialize. Let the logic of the change speak for itself.

---

### 8. Tell me about a time you went above and beyond and why.

Use: Story C (Remuner token pipeline) or Story B (Abax DS)

Remuner pipeline angle: CI validation, drift checks, smoke tests, W3C migration, HTML sandbox preview. These weren't in any spec. They were added because pipeline autonomy without engineering dependency was the actual goal, not just "a component library."

The "why": at a startup as the sole designer, if the system breaks and I'm the only person who can fix it, that's a product risk. The extra infrastructure was self-preservation as much as craft.

Avoid framing this as martyrdom or extra hours. The "above and beyond" was in scope definition, not in effort volume.

---

### 9. Describe a moment where you had to earn someone's trust quickly.

Use: Story C (Remuner, earning CTO trust)

Context: sole designer at a startup means your first 60-90 days either establish or undermine credibility. No team to absorb a bad start.

How trust was built: ship something visible and correct early. The DS work was visible to the CTO because it changed the look of the product in a way he could point to. The "before/after" quote came from that.

What trust looks like at technical companies: it's not warmth. It's engineers and PMs who stop checking your work because they've seen your reasoning be right enough times.

---

### 10. Tell me about a time you disagreed with your manager and what you did.

[NEEDS YOUR STORY - most likely from Abacum or KOM]

Frame: you had a different read on what the product needed. You made the case. Either: (a) you were overruled and executed anyway because the decision wasn't yours, or (b) you persuaded and changed the direction. Both are valid. Be honest about which happened.

What not to do: imply you always win these. That's a red flag. What matters is that you made your case clearly and then acted professionally regardless of the outcome.

---

## Culture fit questions

### 11. Why do you want to work here specifically?

This answer changes per company. The framework stays the same:
- One specific thing about the product that you find structurally interesting (not "I love your design" — something about the problem space)
- One alignment with your background (DS work, complex workflows, fintech, etc.)
- One honest statement about why this role at this stage

Never: "I've always admired your brand." That's empty. Go one layer deeper on the product or the company's approach to design.

Before any interview, answer this question for real. If you can't answer it honestly, that's a signal worth taking seriously.

---

### 12. What kind of team brings out your best work?

Direct answer: cross-functional teams where engineering is treated as a design partner, not a delivery function. Where there's a PM who understands constraints and doesn't over-specify. Where there's enough autonomy to identify problems upstream rather than just executing tickets.

What you don't work well in: teams where design is the last step in a pre-decided flow. Where the job is to make something look good rather than figure out what to build.

Be honest about this. It's also a filter question. If the team they describe doesn't match this, you want to know before you accept.

---

### 13. What does a good design culture look like to you?

Not about process (sprints, crits, retros). About signal:
- Design has input at the problem definition stage, not after the spec is written
- Decisions are made with evidence, not seniority
- Critique is honest and specific. People say "that doesn't work because..." not "interesting direction"
- Engineers and PMs see design as a thinking partner, not a production service

One concrete marker: whether design leadership can push back on a product decision and be heard.

---

### 14. How do you know when a company is the right fit before you join?

Specific signals, not gut feel:
- How do they talk about design in public (blog posts, talks)? Are designers explaining their reasoning or just showing outputs?
- Who made the decision to hire for this role? Is it a design leader, a product leader, or HR?
- What happened to the last person in this role?
- What does the current product look like? What does that tell you about the working conditions that produced it?
- Do engineers and PMs reference design decisions in public writing?

You've built a version of this filter. The roles you've skipped (PandaDoc, Proton, Hostinger) reflect it.

---

### 15. What would your last team say about working with you?

Draw from the Remuner CTO quote (the "before/after" framing). That's a real signal.

Beyond that: someone who identifies problems outside their assigned scope (Modeling Syntax was not a brief). Someone who brings engineering into the design process rather than presenting finished work. Someone who makes decisions and documents the reasoning.

What they wouldn't say: easy to work with in the sense of agreeable. You push back. That's part of what makes the collaboration useful.

---

### 16. What kind of feedback do you find hardest to receive?

[NEEDS YOUR HONEST ANSWER]

Don't say "none, I love all feedback." Don't say something so broad it's meaningless.

A credible answer is specific: a type of feedback that arrives in a way that makes it hard to hear (late, in public, with no evidence), or feedback on a dimension where you have a real blind spot. Name it and say what you've done about it.

---

### 17. What does a bad day at work look like and how do you handle it?

[NEEDS YOUR HONEST ANSWER]

Good angle: a day where the problem you're solving isn't the real problem. Where you're being asked to design a solution to a symptom. Where the upstream decision that created the constraint can't be touched.

How you handle it: depends on whether the upstream decision is genuinely fixed or just feels fixed. Distinguish between constraints and assumptions. Push on assumptions. Accept constraints.

---

### 18. How do you stay motivated on projects you didn't choose?

Draw from KOM client work: 11 years of projects you didn't originate. The work had to be interesting on its own terms.

The honest answer: you find the structural problem inside any assignment. A brief that looks boring usually has a real constraint underneath it. Engaging with the constraint is what makes the work interesting, not the surface domain.

What you've learned: you can't manufacture enthusiasm for a problem that has no structural interest. So you developed a practice of finding where the real problem is before committing to an approach.

---

### 19. What's something most people get wrong about working with designers?

Strong positioning answer:

Most people assume design happens after the problem is defined. That a designer's job is to make a solution look good and work smoothly. The actual leverage is upstream: what is the problem, why does it have the shape it has, what would change if you solved it differently.

Second thing: designers who say "I need more research" before committing to a direction and designers who commit too early. The good ones can hold a hypothesis and update it without either paralysis or stubbornness.

Third angle (optional): design systems work is not polish. A production token pipeline with CI validation and adoption enforcement is infrastructure, not art direction.

---

## Growth and learning questions

### 20. What's the biggest gap in your skills right now?

[NEEDS YOUR HONEST READ]

Candidates. Honest options that could work:
- Quantitative research at scale (your track record is qualitative and inference-based)
- Stakeholder management in large organizations (most of your context is startup/small team)
- Product strategy above the design layer (identifying which markets or bets to make, not just how to design for a chosen one)
- Specific technical areas (depends on your actual gaps)

Don't pick a "weakness that's actually a strength." Pick a real one and pair it with what you're doing about it.

---

### 21. How do you keep up with how design is changing?

Be specific. Not "I read industry blogs."

Current real signal: AI tooling is changing what's possible in prototyping (Figma Make, Claude-powered workflows). You're already using it in production. You've adapted the token pipeline using AI assistance. That's not passive consumption.

Other specifics: who do you actually follow? What's the last thing you read that changed how you think? If you don't have a good answer to this, that's the gap.

---

### 22. What's the last thing you learned that changed how you work?

Use: AI-assisted implementation of the token pipeline at Remuner.

The honest version: using Claude to implement Style Dictionary configuration step by step, with engineer sign-off at each stage, changed what "pipeline autonomy" means. It was no longer blocked on having the engineering knowledge yourself. The brief was precise enough that the implementation could be delegated and validated.

What changed: the way you scope "what a designer can own" expanded. Technical infrastructure that used to require a frontend engineer is now within reach if the problem is well-defined.

---

### 23. How do you get better at something you're not naturally good at?

[NEEDS YOUR HONEST ANSWER]

The structural answer works here: find someone who's already good at it, watch how they approach the problem (not just what they produce), borrow the mental model, apply it with your own constraints.

The teaching background is relevant: explaining something forces precision about what you actually know vs. what you can fake. Teaching UX made you more rigorous about design principles because you couldn't hide behind craft.

---

### 24. Tell me about a piece of feedback that genuinely changed you.

[NEEDS YOUR REAL STORY]

Not a critique of your visual work. Something about your process, your communication, or how you work with others. The best version: feedback that was uncomfortable to receive because it was true, and you can point to a specific change you made because of it.

---

### 25. Who do you learn from and how?

Be specific. Not "the design community." Names, roles, media.

Real signals to draw from: engineers you've worked with closely (the engineer on Modeling Syntax syntax decisions, the engineer sign-off at Remuner). People who are one layer more technical than you and willing to explain the constraints.

Teaching is also learning: you'll have learned from students asking the questions you didn't have good answers to.

---

### 26. Where do you want to be as a designer in 3 years?

Direct answer: deeper craft and broader scope on the IC track. Staff or Principal level. Not management.

The specific version: working on structural problems at the product and system level. Owning a design system that's treated as infrastructure. Having enough influence over product direction that design considerations shape what gets built, not just how it looks.

What you're not interested in: a management track. Growing a team is a different skill set with different rewards. The work you want to be doing in 3 years is the same kind of work, on harder problems.

---

### 27. What does growth look like to you beyond a title change?

The real version: the quality of problems you get access to. Whether people bring you in before the solution is decided or after. Whether your previous work is used as evidence by others when making decisions.

Concrete markers: an engineer citing your DS documentation to resolve a debate. A PM saying "let me check with Manel before we commit to this direction." Problems where the answer isn't obvious arriving on your desk rather than only the problems where the answer is clear but the execution is needed.

---

## Case presentation round

This section assumes a 30-45 minute format: walk us through a project, then Q&A.

### Story selection

Lead with the case that matches the company's context. Use the same mapping from `context/positioning.md`:
- DS-first roles: Remuner DS (CTO quote is the credibility anchor)
- Product roles with DS: Abacum Dataset Manager
- Fintech: Modeling Syntax
- Founding designer: breadth narrative across both companies

Don't try to cover everything. One case, deep, is more effective than three cases shallow.

### Structure that works

1. Context (60 seconds): company, team, my role, the surface problem
2. The real problem (90 seconds): what research or investigation showed the real constraint was
3. The decision (2 minutes): what you chose to do and why. What you chose NOT to do and why. The "why not" is often more interesting than the "why."
4. The work (3-4 minutes): what was actually designed. Show the process, not just the output. Failure states, iterations, constraints.
5. Outcome (90 seconds): what shipped, what changed, what you'd do differently. Own absence of metrics directly.

### Q&A what to expect

- "How did you handle disagreement in the team?"
- "What would you do differently?"
- "How did you validate the direction?"
- "Who else was involved and what was your specific contribution?"
- "How did this connect to business outcomes?"

The last one is the hardest if you don't have hard metrics. Answer: here is the qualitative signal, here is why it mattered, here is why I don't have a number, here is the proxy I would use.

---

## Ways-of-working round

These questions test how you actually function in a team day-to-day. Interviewers are checking for: process maturity, collaboration patterns, communication, how you handle ambiguity and disagreement.

### Common themes

**Handling ambiguity**
What do you do when a brief is underspecified? Answer: distinguish between ambiguity in the problem (explore it) and ambiguity in the scope (clarify it before starting). Don't ship a solution to a problem you haven't confirmed.

**Cross-functional collaboration**
Describe your relationship with engineering. Specific answer from experience: the Modeling Syntax work happened in direct collaboration with one engineer, not through a PM intermediary. The Remuner pipeline had engineer sign-off at each implementation step. The relationship is a partnership, not a handoff.

**Prioritization**
How do you decide what to work on? At a startup: survival first. Does the product work well enough to retain users? At a scale-up: what's the highest-leverage design change given the engineering cost? The framing shifts by company stage.

**Documentation and handoff**
How do you make sure your work doesn't die when you leave? Design system documentation was a solved problem at both Abacum and Remuner. Storybook in Chromatic is the artifact. ESLint adoption rules are the enforcement. The system should work without you explaining it every time.

**Receiving feedback and iterating**
You get a critique that's partly right and partly wrong. How do you handle it? Separate the diagnosis from the prescription. The interviewer's diagnosis of what's wrong may be accurate even if their proposed fix is wrong. Engage with the diagnosis.

---

## Questions to ask them

These signal seniority. Choose 2-3 per interview based on what you already know.

**On the problem space**
- What's the most important design problem that's currently unsolved in this product?
- Where does design have the most influence over product direction right now?

**On the team**
- How do design and engineering collaborate? Who drives the prioritization conversation?
- What happened to the last person in this role?

**On design systems specifically (DS roles)**
- Who owns the relationship between the design system and product teams?
- What's the biggest gap in the current system?

**On culture**
- What's a recent example of a design decision that pushed back on a product direction?
- How does the team handle design quality vs. shipping speed when they conflict?

**On growth**
- What would make someone in this role exceptional versus good at 12 months?

---

## Pre-interview checklist

Before each interview:
1. Read the JD again. Note the 2-3 things they care most about.
2. Pick the story that maps to those 2-3 things.
3. Answer "why this company specifically" honestly. If you can't, that's a signal.
4. Check `context/salary.md` so you're not caught off guard on compensation.
5. Prepare 2-3 questions based on what you actually want to know about them.
