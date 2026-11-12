# Question bank

Common interview questions mapped to a story in [stories.md](stories.md), plus the questions that have their own answer (culture, growth). The numbers Q1 to Q27 match the old prep.md, so "Q11" in an old brief still means the same question.

For a behavioral question, the story is in [stories.md](stories.md); this file only gives the angle for that question. Set-piece answers (intro, departure, since March) are in [answers.md](answers.md).

---

## Behavioral questions

### 1. A project that didn't go as planned.

Use: `dataset-manager`.

The research didn't confirm the original hypothesis, so the plan changed before screens were designed. Frame it as a research process working correctly to surface a real constraint before it became a shipped mistake, not as a heroic pivot.

### 2. A time you missed a deadline. What happened?

Use: `kom-deadline`.

### 3. A time you had to deliver bad news to a stakeholder.

Use: `dataset-manager`, the "no SQL" call.

SQL would have given power users more control, and the research showed it was wrong for most users. Make the case with the evidence, not opinion. Not every stakeholder agreed at once; the work was showing the reasoning, not just the conclusion. The decision was shared with Product and Engineering, so say "we" for the call.

### 4. A time you had to make a decision with no clear answer.

Use: `modeling-language` (better), or `dataset-manager`.

State it explicitly: "there was no right answer in the literature. I had to build enough evidence to make a defensible call and move."

### 5. A situation where you had to influence without authority.

Use: `maker-days`.

Engineering had no obligation to prioritise the system, so the case had to be good enough that they chose to. Influence here means building evidence that makes the decision easy for the person with authority.

### 6. A time you failed publicly. How did you recover?

Use: `token-file`.

### 7. When have you had to change your approach mid-project?

Use: `dataset-manager`.

Original approach, what the research showed, what you did differently and why, what shipped. Keep it concrete and don't editorialise.

### 8. A time you went above and beyond and why.

Use: `remuner-ds` (the February 2026 pipeline additions) or `abax`.

The goal was a pipeline that kept working without engineering help. As sole designer, a system only you can fix is a product risk, so the extra infrastructure was self-preservation as much as craft. The "above and beyond" was in scope definition, not in hours; avoid martyrdom framing.

### 9. A moment where you had to earn someone's trust quickly.

Use: `remuner-ds`, earning the CTO's trust.

As sole designer, the first 60 to 90 days establish or undermine credibility. At technical companies trust isn't warmth: it's engineers and PMs who stop checking your work because your reasoning has been right enough times.

### 10. A time you disagreed with your manager and what you did.

[NEEDS YOUR STORY], most likely from Abacum or Kings of Mambo. Closest real episode: `manager-view` (a disagreement with the CEO and CTO, not a direct manager).

Either you were overruled and executed anyway, or you persuaded and changed the direction. Both are valid; be honest about which happened. Don't imply you always win these.

---

## Culture fit questions

### 11. Why do you want to work here specifically?

This answer changes per company. The framework stays the same:
- One specific thing about the product that you find structurally interesting (not "I love your design" — something about the problem space)
- One alignment with your background (DS work, complex workflows, fintech, etc.)
- One honest statement about why this role at this stage

Never: "I've always admired your brand." That's empty. Go one layer deeper on the product or the company's approach to design.

Before any interview, answer this question for real. If you can't answer it honestly, that's a signal worth taking seriously.

### 12. What kind of team brings out your best work?

Direct answer: cross-functional teams where engineering is treated as a design partner, not a delivery function. Where there's a PM who understands constraints and doesn't over-specify. Where there's enough autonomy to identify problems upstream rather than just executing tickets.

What you don't work well in: teams where design is the last step in a pre-decided flow. Where the job is to make something look good rather than figure out what to build.

Be honest about this. It's also a filter question. If the team they describe doesn't match this, you want to know before you accept.

### 13. What does a good design culture look like to you?

Not about process (sprints, crits, retros). About signal:
- Design has input at the problem definition stage, not after the spec is written
- Decisions are made with evidence, not seniority
- Critique is honest and specific. People say "that doesn't work because..." not "interesting direction"
- Engineers and PMs see design as a thinking partner, not a production service

One concrete marker: whether design leadership can push back on a product decision and be heard.

### 14. How do you know when a company is the right fit before you join?

Specific signals, not gut feel:
- How do they talk about design in public (blog posts, talks)? Are designers explaining their reasoning or just showing outputs?
- Who made the decision to hire for this role? Is it a design leader, a product leader, or HR?
- What happened to the last person in this role?
- What does the current product look like? What does that tell you about the working conditions that produced it?
- Do engineers and PMs reference design decisions in public writing?

You've built a version of this filter. The roles you've skipped (PandaDoc, Proton, Hostinger) reflect it.

### 15. What would your last team say about working with you?

Draw from the Remuner CTO quote (the "before/after" framing). That's a real signal.

Beyond that: someone who identifies problems outside their assigned scope (Modeling Syntax was not a brief). Someone who brings engineering into the design process rather than presenting finished work. Someone who makes decisions and documents the reasoning.

What they wouldn't say: easy to work with in the sense of agreeable. You push back. That's part of what makes the collaboration useful.

### 16. What kind of feedback do you find hardest to receive?

Feedback that tells me something needs to be redone because of information that was wrong, missing, or misleading upstream. Not redoing because I learned something or requirements changed — that's normal, I can do that without friction. What's genuinely hard is when the redo was avoidable: the brief was vague, a constraint wasn't shared, someone misspoke about what was needed. The work wasn't wrong given what I knew. It's just that the inputs were bad.

Learning and redoing is fine. Redoing because of an information failure is the one that costs me more than it probably should.

What I've done about it: I front-load constraint extraction now. Before committing to a direction I push harder to surface the things that aren't in the brief — stakeholder assumptions, technical limits, things that have already been decided upstream. Not because I distrust people, but because I know that discovering them mid-build is the thing I find hardest to absorb.

### 17. What does a bad day at work look like and how do you handle it?

[NEEDS YOUR HONEST ANSWER]

Good angle: a day where the problem you're solving isn't the real problem. Where you're being asked to design a solution to a symptom. Where the upstream decision that created the constraint can't be touched.

How you handle it: depends on whether the upstream decision is genuinely fixed or just feels fixed. Distinguish between constraints and assumptions. Push on assumptions. Accept constraints.

### 18. How do you stay motivated on projects you didn't choose?

Draw from KOM client work: 11 years of projects you didn't originate. The work had to be interesting on its own terms.

The honest answer: you find the structural problem inside any assignment. A brief that looks boring usually has a real constraint underneath it. Engaging with the constraint is what makes the work interesting, not the surface domain.

What you've learned: you can't manufacture enthusiasm for a problem that has no structural interest. So you developed a practice of finding where the real problem is before committing to an approach.

### 19. What's something most people get wrong about working with designers?

Strong positioning answer:

Most people assume design happens after the problem is defined. That a designer's job is to make a solution look good and work smoothly. The actual leverage is upstream: what is the problem, why does it have the shape it has, what would change if you solved it differently.

Second thing: designers who say "I need more research" before committing to a direction and designers who commit too early. The good ones can hold a hypothesis and update it without either paralysis or stubbornness.

Third angle (optional): design systems work is not polish. A production token pipeline with CI validation and adoption enforcement is infrastructure, not art direction.

---

## Growth and learning questions

### 20. What's the biggest gap in your skills right now?

Use: stakeholder navigation in politically complex organizations.

Most of your experience is founder-driven or client-driven — short decision chains where one person says yes and it happens. At Abacum you got closer: built the DS business case with the head of design, presented to engineering leadership, got cross-squad buy-in. But still a startup with a relatively flat structure.

What you haven't done: aligned 4–5 stakeholders across different departments who each have partial veto and competing priorities, in an environment where the right decision alone isn't enough to move things. That's what larger orgs require and where you have least reps.

What you're doing about it: the job search itself is a version of this — navigating processes with multiple stakeholders, no direct line to the decision-maker, building a case through each layer. Not the same, but the muscle is related.

What to avoid: don't say "I avoid confrontation" or frame this as a personality trait. It's an organizational context gap, not a character flaw. You've done alignment work — just not at the scale or complexity of large enterprises.

Evidence check: "got cross-squad buy-in" overstates the register. The all-hands presentation sought buy-in; say that, and use `maker-days` for what Engineering agreed to.

### 21. How do you keep up with how design is changing?

Be specific. Not "I read industry blogs."

Current real signal: AI tooling is changing what's possible in prototyping (Figma Make, Claude-powered workflows). You're already using it in production. You've adapted the token pipeline using AI assistance. That's not passive consumption.

Other specifics: who do you actually follow? What's the last thing you read that changed how you think? If you don't have a good answer to this, that's the gap.

### 22. What's the last thing you learned that changed how you work?

Use: AI-assisted implementation of the token pipeline at Remuner.

The honest version: using Claude to implement Style Dictionary configuration step by step, with engineer sign-off at each stage, changed what "pipeline autonomy" means. It was no longer blocked on having the engineering knowledge yourself. The brief was precise enough that the implementation could be delegated and validated.

What changed: the way you scope "what a designer can own" expanded. Technical infrastructure that used to require a frontend engineer is now within reach if the problem is well-defined.

Evidence check: the register records Codex first, then Claude, for the February 2026 pipeline work, and engineers adapting the original pipeline. Say "Codex, then Claude" and keep the engineers' part.

### 23. How do you get better at something you're not naturally good at?

Practice, primarily. Reading and videos give you vocabulary and a mental model, but I don't actually know something until I've used it under real conditions. The discomfort of doing it badly at first is part of how I learn — I keep going until it feels boring, which is when I know it's actually in.

Real example: getting comfortable with AI tooling. I read and watched, but what actually moved the needle was setting up Claude projects from scratch, building skills, configuring MCPs, iterating on prompts until they worked the way I needed. Passive consumption told me what was possible. Practice told me what was actually hard and why.

The pattern: I consume enough to understand the shape of the thing, then I stop reading and start doing. I go back to references when I hit a specific wall, not before.

The honest flip side: I really don't like doing things more than once. The cost of having to redo something feels disproportionate to me, so I front-load the practice to avoid it. That probably explains why I gravitate toward getting foundations right early — in design systems work especially, the decisions you make at the token level are expensive to reverse, so I'd rather spend more time there than retrofit it later.

### 24. Tell me about a piece of feedback that genuinely changed you.

Use: `kom-lofi-feedback`.

### 25. Who do you learn from and how?

Be specific. Not "the design community." Names, roles, media.

Real signals to draw from: engineers you've worked with closely (the engineer on Modeling Syntax syntax decisions, the engineer sign-off at Remuner). People who are one layer more technical than you and willing to explain the constraints.

Teaching is also learning: you'll have learned from students asking the questions you didn't have good answers to. Teaching is confirmed in the register (UX, components, WordPress themes; a Sketch course at LABASAD around 2018); course level and institutions beyond that are not.

### 26. Where do you want to be as a designer in 3 years?

Direct answer: deeper craft and broader scope on the IC track. Staff or Principal level. Not management.

The specific version: working on structural problems at the product and system level. Owning a design system that's treated as infrastructure. Having enough influence over product direction that design considerations shape what gets built, not just how it looks.

What you're not interested in: a management track. Growing a team is a different skill set with different rewards. The work you want to be doing in 3 years is the same kind of work, on harder problems.

### 27. What does growth look like to you beyond a title change?

The real version: the quality of problems you get access to. Whether people bring you in before the solution is decided or after. Whether your previous work is used as evidence by others when making decisions.

Concrete markers: an engineer citing your DS documentation to resolve a debate. A PM saying "let me check with Manel before we commit to this direction." Problems where the answer isn't obvious arriving on your desk rather than only the problems where the answer is clear but the execution is needed.

---

## Questions that keep coming up

Patterns logged in [memory.md](../memory.md) ("Interview question patterns"); the dated entry there has the context.

- **"How do you use AI day to day?"** Recruiter-screen question at AI-native companies. See [answers.md](answers.md#how-do-you-use-ai-day-to-day).
- **"How many designers did your system serve?"** DS screens. See the count gap in [stories.md](stories.md#gaps).
- **"How do bugs that reach designers get handled?"** Early-stage teams without full PM coverage. Have a concrete Remuner example ready ([NEEDS YOUR STORY]).
- **"What would you do if you were the CEO?"** A vision probe: an opinionated answer about product direction, not design craft.
- **"How would you build it with full resources?"** A ranked argument about what matters most, not "everything".
- **"How would we know it worked?"** Expect the measurement question directly in live cases. See [playbooks/live-challenge.md](playbooks/live-challenge.md).

---

## Enterprise / legacy-product question bank

Collected externally (not tied to an active process, no IBM entry in the pipeline as of 2026-07-23). Kept here because the domain, long-lived enterprise software, legacy modernization, regulated and global stakeholders, recurs across the kind of roles being targeted. Grouped by theme. Where an existing story already answers the question, that is noted instead of writing new material. Where there is a real gap, it is flagged rather than invented.

### Theme: modernize or extend a legacy product without breaking it

Covers: "designing for a product that's been in market 15+ years without breaking habits," "a design system with 8 years of legacy patterns, modernize without a full rebuild," "a client on an older version wants new features," "a redesign breaks backward compatibility for enterprise contracts," "90% of users on outdated browsers or restricted corporate environments."

Use: `abax-migration`. Keeping MUI underneath Abax to reduce scope and speed up adoption, instead of building from scratch, is a direct answer to "modernize without a full rebuild." Frame the general principle: legacy constraints are not obstacles to route around, they are scope information. The redesign that respects them is usually the one that ships.

### Theme: inherited, inconsistent component library across product lines

"You inherit a component library used inconsistently across five product lines. Where do you start?"

This is the `abax` setup almost exactly (five squads, components used inconsistently). Use it as is. Start: audit for the highest-cost inconsistency, not the most visible one. Business case before build, as in `maker-days`.

### Theme: defend a simpler solution against "more options = more powerful"

"How do you defend a simplification of a complex enterprise workflow to a client who equates more options with more power?"

Use: `dataset-manager`, the "no SQL" call. Same shape: a more powerful option existed, the evidence showed it was wrong for the actual user base, the case was made on data not opinion. Q3 above covers the same story.

### Theme: sole designer, multiple product lines, competing release cycles

"You're the sole designer supporting three enterprise product lines with different release cycles. How do you prioritize?"

Merge the ways-of-working "Prioritization" answer ([playbooks/ways-of-working.md](playbooks/ways-of-working.md)) with the `remuner-ds` audit loop (fix now versus defer into an upcoming feature) for credibility. No new story needed.

### Theme: long-time power users resist change, even improvements

"A long-time enterprise client's power users resist any UI change, even improvements. How do you introduce redesign without losing their trust?"

Use: `remuner-ds` (earning trust quickly) for the trust mechanism, plus `dataset-manager` for the change-management angle (the change was justified by research, not imposed). The honest addition: with entrenched power users, the fix is usually sequencing, not persuasion, ship the change where the cost of being wrong is lowest first, let the evidence build trust before touching the workflow they rely on most.

### Gaps, no direct material, do not invent

- **Global stakeholder conflict.** "Stakeholders in the US, India, and Germany all review the same design and give conflicting feedback. How do you reconcile it?" No direct experience at this scale, reinforces the stakeholder-navigation gap already logged in Growth Q20. If asked, answer from principle (separate signal from noise, find the shared success metric each region actually cares about, escalate the tradeoff rather than picking a side unilaterally) and be honest that the org-scale version of this is the least-reps area, per Q20.
- **AI feature judgment in a legacy tool.** "Your PM wants to add an AI feature to a legacy enterprise tool. How do you decide where AI adds value vs. noise?" The shipped Remuner agent (`ai-agent`) is real user-facing AI material: scope agreed with the founders and Engineering, supported questions and refusals. It wasn't a legacy tool, so answer the legacy part from principle: value is where the tool currently forces the user to do translation or lookup work themselves; noise is AI bolted onto a flow that already works.
- **Researching specialized users you are not** (network admins, data engineers). No documented case. If asked, answer from the general research approach (the `dataset-manager` sessions), but do not claim domain-specialist research experience that is not there.
- **Regulated-industry compliance restricting UX patterns** (banking, healthcare). Abacum and Modeling Syntax are financial-data-adjacent but not documented as compliance-driven pattern restrictions. Flag as [NEEDS YOUR STORY] if there is a real KOM or Abacum incident here; otherwise do not claim it.
- **Accessibility gap found during a client audit, post-shipment.** No documented incident. [NEEDS YOUR STORY]. If none exists, do not manufacture one, answer from principle only if pressed (triage by user impact, patch the highest-severity gap first, retrospective on why it shipped). Closest real material: the Remuner contrast work in `remuner-ds` (in-use colours brought to WCAG AA).
