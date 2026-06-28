# Factorial — Round 2: Design Director

**Interviewer:** Marta Serrano, Product Design Director (at Factorial since Jan 2025)
**Format:** ~1 hour video call
**Date:** Mon 2026-06-29 (requested) or Wed 2026-07-01

---

## Factorial's design competency framework

From their public career path doc. Marta will be evaluating against these — mirror the framing:

- **Research & Analysis:** "detect opportunities, anticipate needs, bring forward new knowledge that guides product decisions." Not just executing research — shaping what gets investigated.
- **Ideation & Planning:** "scalability, feasibility, and alignment with business goals." They want to see you thinking about what's buildable and what the business gets from it, not just what's desirable.
- **Design & Craft:** "leverage design systems to ensure consistency and scalability... set standards, contribute to raising the quality of design across the company." DS work is explicitly framed as a quality and scale lever, not a side project.
- **Communication & Collaboration:** "facilitate decision-making... build bridges with engineers, product managers, and business partners." The bridge-builder framing is their explicit expectation at senior level.
- **Learning & Sharing:** "mentor others, document their work, contribute to scaling practices." Mentoring and documentation are evaluated, not optional.

Their evaluation philosophy: "outcomes rather than outputs." Use that phrase back to them — it's their frame, and it's accurate to how you work.

---

## Who is Marta

Background: Head of Product & Design at Bravo Studio (no-code app builder), Head of Product Design & Product Owner at Codeless Labs. She's held PM and PO titles alongside design titles. She thinks in both design and product outcome terms simultaneously, and she'll probe for both. She also mentors designers on ADPList — she's seen a lot of candidates.

Her lens: judgment and influence, not craft. She knows what tokens are. Explaining tokens to her is the wrong level.

---

## What Marta most likely cares about

1. **How you think, not what you shipped.** Her PM background means she's evaluating whether your design decisions connected to product outcomes. "We built a token system" is not interesting. "We built a token system because [decision] and it unblocked [outcome]" is interesting.

2. **How you collaborate at senior level.** This is a Senior/Staff role on a new spinoff. She wants to know you can work with engineers and PMs as a peer, not as a service. She'll probe for specific collaboration patterns.

3. **Your read on Factorial and the spinoff.** She'll want to see genuine curiosity about what they're building, not a rehearsed "I love your brand" answer. The spinoff is still largely unknown — make asking about it feel natural, not like you're filling a gap.

---

## If she asks for a portfolio walkthrough

Marta's round is 1 hour — long enough for a case walkthrough if she wants one. If asked:

- Lead with Dataset Manager (Story A) — shows product judgment and research-driven direction change. Remuner DS is support, not the opener.
- Before presenting any case, run the **Staff-level signals checklist** in `interviews/prep.md` (Case presentation round section). The checklist covers: opening frame, constraint framing, prioritisation as a section, showing restraint, PM-like behaviours, outcome buckets, closing meta-lesson, and metrics ownership.
- The Remuner DS deck has been updated with Staff signals. If she asks to see it, it's ready. If she asks about Dataset Manager, that deck has not been reviewed against the checklist yet — treat it as a verbal walkthrough only until reviewed.
- Have the non-DS story ready for Q&A. Marta may probe product discovery or ambiguity navigation to check for range beyond DS. Story A (Dataset Manager) is that story.

---

## Lead story for this round

**Story A (Dataset Manager) — lead with this.**

Remuner DS already landed in Round 1. Don't repeat it as the opening. The Dataset Manager story shows something different and more relevant to a Design Director: identifying that the real problem is upstream of the brief, changing direction mid-project based on evidence, making a decision with a real tradeoff (no SQL — lower ceiling, right user base). This is what Marta is listening for.

Use Remuner DS as support — particularly when the conversation moves to systems thinking or AI tooling.

Opening intro (if asked to walk through background or tell me about yourself): use the two-part format in `prep.md` → "Opening intro" section. Who I am first, then work history. Keep each under 45 seconds.

---

## Likely questions → story map

**"Walk me through a project where you had to make a hard design decision."**
→ Story A. The "no SQL" call is the decision. Frame the tradeoff: SQL was the obvious power-user answer, but the actual users didn't think in SQL. The right solution was harder to implement and had a lower ceiling — but it was the right call for the user base. Show the reasoning, not just the outcome.

**"How do you work with engineering?"**
→ Modeling Syntax (Story D): direct collaboration with one engineer, bypassing the PM intermediary. Remuner pipeline: engineer sign-off at each step, not a finished-work handoff. The relationship is a partnership where you're bringing the design constraint and they're bringing the technical constraint, and the solution lives in between.

**"Tell me about a time you influenced a direction without having the authority to decide."**
→ Story B (Abax DS). No ticket, no mandate, built the ROI case with head of design and presented to engineering leadership. Influence without authority is not persuasion — it's building evidence that makes the right decision obvious to the person who has to make the call.

**"What does good design look like at the system level?"**
→ Your framing: design systems are infrastructure, not art direction. A system that works is one that doesn't require you to explain it every time. Adoption enforcement (ESLint rules), CI validation, drift checks — these are engineering-quality signals applied to design output.

**"Tell me about a project that didn't go as planned."**
→ Story A again, or the production outage story (Story F from behavioral section): deleted a token file that was a production dependency. App went down. Own it plainly, describe the structural fix.

**"Why Factorial / why the spinoff?"**
Honest version: Barcelona-headquartered tech company building something greenfield, which means real design influence over what gets built rather than executing a decided roadmap. The HR domain has genuinely complex workflow problems (multi-market payroll, compliance, cross-jurisdictional edge cases) — this is not a simple CRUD product. And the spinoff specifically is interesting because it's early enough that design can shape the architecture, not just the interface. Then ask what the spinoff is solving, if it hasn't come up yet.

**"How are you using AI in your work?"**
This is the question Lucia already raised and Marta will go deeper. Don't describe tools — describe what changed. The real answer: AI assistance changed what "designer-owned" means. Implemented the token pipeline (Style Dictionary config, CI checks) step-by-step with AI assistance and engineer sign-off — infrastructure that previously required a frontend engineer is now within reach when the problem is well-defined. Also using AI to build and test prototypes faster than Figma-only workflows allow. Have a clear opinion on where AI helps (speed, implementation, synthesis) and where it doesn't (defining the right problem, making tradeoffs).

**"What are you looking for in your next role?"**
Senior IC scope with real influence upstream of the spec. Design that shapes what gets built, not just how it looks. Complex B2B product with structural workflow problems. Not a management track.

**"What's your salary expectation?"** *(unlikely at this round, but possible)*
→ See salary section below. Do not give a number to Marta — redirect to framework first.

---

## Case study Q&A — Dataset Manager

Prepared answers for deep-dive case questions. These are the arguments, not scripts.

### 1. Why did you choose this project?

I chose it because it represents the kind of work I'm strongest at: ambiguous, systems-heavy product problems where the visible UI issue is only a symptom.

The core challenge wasn't interface design. It was identifying that the product abstraction itself was wrong and then helping redefine both the product model and the delivery strategy.

That combination — diagnosis, architecture thinking, cross-functional alignment — is where I create the most value.

### 2. Why only three research sessions?

The goal wasn't statistical confidence. It was diagnostic confidence.

I needed to answer one question: was the friction caused by unfamiliarity with the interface, or by a deeper mismatch in mental models?

The decisive signal came when the most experienced user struggled with the same conceptual blockers as newer users. At that point, more sessions would have increased confidence in frequency — not changed the diagnosis.

That told me the ceiling of improvement from UI changes alone was limited.

### 3. What exactly changed after research?

Before research, the scope was a UX improvement initiative. After research, it became a product architecture initiative.

Initially: how do we make this interface easier to use? After: how do we expose the underlying system using concepts finance teams already understand?

That scope change affected roadmap, technical dependencies, and implementation complexity.

### 4. Why reject SQL?

SQL was a reasonable proposal — it would have solved flexibility quickly.

The problem was user fit. It served the technically sophisticated minority, not the core ICP, which was finance teams operating in business concepts rather than query language.

Supporting SQL would also have introduced long-term product complexity: two paradigms to maintain, a technical path and a non-technical path.

The PM's hypothesis wasn't wrong. It was solving a different problem for a different segment.

The tradeoff was deliberate: power users stayed underserved longer so the majority could become autonomous.

### 5. What was your specific contribution?

Four parts:

First, I ran the research that changed our diagnosis.

Second, I reframed the problem from interface usability to abstraction design.

Third, I worked with the PM and lead engineer to define the rollout strategy and capability sequencing.

Fourth, I designed the abstraction layer and interaction model that translated backend complexity into finance-native workflows.

I wasn't just designing screens. I was helping shape product direction and delivery strategy.

### 6. How did you influence PM and engineering?

I try not to influence through opinion or design authority.

I influence by creating shared clarity around tradeoffs.

In this case, alignment came from making the tradeoff explicit: we could optimize for implementation speed, or for long-term self-serve scalability.

Once the team aligned on the target user and business goal, the design decisions became much easier to discuss.

A big part of senior IC influence is reducing ambiguity for the team.

### 7. Why phase delivery instead of shipping the full solution?

Because a big-bang replacement carried too much risk.

Three risks: migration risk, implementation risk, and adoption risk.

The phased rollout preserved flexibility for advanced users while letting us validate whether the abstraction actually worked for common workflows.

I generally prefer progressive capability release for complex workflow systems.

### 8. What was the hardest tradeoff?

Balancing simplicity against flexibility.

Complex B2B systems become dangerous when you oversimplify them. The challenge was reducing cognitive load without removing necessary capability — deciding which complexity should disappear and which should remain visible when needed.

That's a product judgment problem more than a visual design problem.

### 9. What would you do differently?

I would instrument the workflow earlier.

We had strong qualitative evidence and operational feedback, but weak quantitative baselines.

I would define success metrics upfront: completion rate, failure points, time-to-configuration, support dependency. That would improve both prioritization and impact measurement.

---

## Staff / leadership Q&A

### 10. What does Staff-level design mean to you?

Staff design is less about design output and more about organizational leverage.

A staff designer improves the quality of decisions across the system. That usually means operating in ambiguity, influencing strategy, aligning stakeholders, and helping teams make better tradeoffs earlier.

The leverage comes from improving decision quality, not just producing better screens.

### 11. How do you handle disagreement?

I try to identify whether we actually disagree on solutions or whether we disagree on goals, assumptions, or constraints.

Most conflicts are upstream. Once the underlying assumptions are explicit, disagreements become much easier to resolve.

I focus on making tradeoffs visible rather than arguing for preferred solutions.

### 12. How do you work with product managers?

I work best with PMs as thinking partners, not as handoff partners.

I contribute heavily in problem framing, prioritization discussions, and tradeoff analysis.

I care a lot about understanding business constraints because design decisions become much better when those constraints are explicit.

### 13. How do you prioritize?

I evaluate opportunities across four dimensions: user pain severity, business impact, strategic leverage, and implementation complexity.

I pay special attention to leverage. I prefer solving foundational problems that unlock multiple downstream improvements.

### 14. What environments do you thrive in?

I do my best work in complex product environments with meaningful constraints — especially B2B workflow products, data-heavy systems, or products where architecture and interaction design are tightly connected.

I'm strongest when the problem requires deep product reasoning rather than surface-level UI iteration.

### 15. Why Factorial?

Factorial is interesting because HR software contains a combination I enjoy: operational complexity, cross-functional workflows, and high business impact. There's significant product complexity underneath what often looks like simple UI.

That kind of environment rewards systems thinking and strong product reasoning, which aligns with how I work.

### 16. What are your weaknesses?

One area I've actively worked on is adapting communication to different audiences.

Because I naturally think in systems and abstractions, I can sometimes over-index on complexity too early. I've become much more deliberate about simplifying communication and adjusting detail depending on the audience and decision context.

---

## Gaps still to resolve before the call

- **"Tell me about a time you missed a deadline."** — Covered. KOM WordPress e-commerce: scope too large, called the client proactively, shipped the site without purchase functionality + email capture form. See prep.md Q2.
- **"Tell me about feedback that changed you."** — Covered. KOM: client stopped a hi-fi review and told him to go low-fi first. Structural change: validate direction before investing in polish. See prep.md Q24.
- **"What's your biggest skill gap right now?"** — Covered. Stakeholder navigation in politically complex organizations. Short decision chains (founders, clients) have been the norm; large-org alignment across multiple stakeholders with partial veto is the gap. See prep.md Q20.

---

## Questions to ask (pick 2–3)

**Ask these — still genuinely unanswered:**

- "What is the IT spinoff solving and what stage is it at?" — If Lucia didn't cover it in detail, this is still the most important unknown. Ask it early.
- "What does the design team look like on the spinoff? Is it a solo role to start, or joining an existing team?"
- "Where does design sit relative to product direction? Is design shaping what gets built, or primarily executing a decided roadmap?"

**If the above are covered:**

- "What differentiates strong senior designers from staff-level designers at Factorial?"
- "Where do you currently see the biggest design bottlenecks in the organization?"
- "What would make someone in this role exceptional versus good at 12 months?"

---

## Salary — UNRESOLVED, READ BEFORE THE CALL

Factorial's published internal bands (obtained 2026-06-25):
- Senior: €68K–€80K (+ 25% ESOPs)
- Staff: €93K–€107K (+ 50% ESOPs)

€82K sits above the Senior ceiling and below the Staff floor. Lucia said it was "within range" — which is either flexibility on their end or a signal they're thinking Staff.

**Do not confirm a number with Marta.** If compensation comes up, say: "That depends on where this role sits in your framework — can you tell me whether you're thinking Senior or Staff?" Then anchor from there. If Staff: open at €93K. If Senior: their ceiling is €80K and the gap is their problem to solve, not yours to close by dropping. Do not share previous compensation. Do not give a range.

---

*After the call: run `/debrief-interview Factorial design-director` while it's fresh.*
