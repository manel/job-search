# Factorial Practice Challenge C — Performance Reviews

Worked example. Structure mirrors the four Figma pages from the round 3 hour-1 playbook: Problem framing, Core flow, Design, What I didn't build. This is the murkiest of the three verticals. There is no obvious "core loop" the way clock-in or leave-approval has one, so the framing work carries almost all the weight. If you nail the problem definition here, the screen is easy. If you skip it, you will design a beautiful form nobody fills in honestly.

> **Flag legend**
> 🚩 **MOVE** — a rehearsable tactical action. Transferable to any brief. Internalise these, not the specific design.
> ⭐ **SINGLE DECISION** — the spine. One decision the whole solution hangs on, defensible three ways (user pain, business risk, what it teaches).

---

## The brief (as handed to you)

> The spinoff wants to help companies run performance reviews. Design the core experience. 60 minutes.

This is the vaguest brief of the set, on purpose. "Performance reviews" is a culture problem disguised as a software problem. The candidate who starts drawing a review form has already lost. The whole game is in deciding what "performance reviews" even means for v1 before you touch a component.

---

## 0–8 min — Clarifying questions (ask before opening Figma)

> 🚩 **MOVE** — Questions before Figma. Even when the brief says "start working." With a brief this vague, questions are not optional politeness; they are the only way to make the problem designable.

Pick 3 to 4. Each must collapse the ambiguity in a different direction.

1. "Performance reviews can mean a once-a-year appraisal, continuous feedback, or goal tracking. Which problem are we solving for v1? They imply very different products." Forces the scope decision onto them, and shows you know these are not the same thing.
2. "Who is v1 for: the employee being reviewed, the manager writing reviews, or the HR admin running the cycle?" Three users, three products again.
3. "Is the painful job writing the review, or running the cycle so reviews actually get done on time and fairly?" Separates the document problem from the operations problem.
4. "Are we optimising for review quality, for completion rate, or for reducing bias? I can design for one cleanly."

> 🚩 **MOVE** — Name the hidden branch out loud. Performance is loaded with delegation, calibration, visibility, and fairness branches. Surfacing one shows you see the political reality, not just the form.

Hidden branch to name out loud:
"Before I design anything I would clarify who can see a review. Self, manager, manager's manager, HR. Visibility rules are not a setting bolted on later; they shape what people are willing to write, so they are part of the core design."

Assume for this worked example: **v1 is the manager writing a review during a company-wide cycle, the painful job is completing fair reviews on time, optimise for completion rate and review quality together, default visibility is employee plus management chain plus HR.**

---

## 8–18 min — Problem framing (Figma page 1, leave it visible)

**Who is the primary user?**
The manager, mid-cycle, with six reviews due Friday and a full week of actual work. Not the HR admin who configures the cycle, not the employee who reads the result. The manager is where reviews succeed or fail, because an unwritten or rushed review is the failure mode that makes the whole product worthless.

**The one job that creates the most friction or cost?**
Writing a review that is specific and fair, when the manager cannot remember what happened in February. The friction is not the form. It is the blank page plus bad memory plus time pressure, which together produce vague, recency-biased reviews that help nobody and that employees resent.

**Success vs failure.**
Success: the manager writes a specific, evidence-grounded review in one focused sitting and submits on time. Failure: the manager stares at a blank rating scale, writes "great team player, keep it up" from memory of last week only, and the review actively erodes trust.

**Business objective (one line).**
Raise review completion rate and review quality at the same time. Measure: on-time completion %, the share of sections backed by linked evidence, and employee trust in the process. The user's win is a review they would read aloud without wincing; the business's win is real signal on its people instead of boilerplate.

**The core loop.**
> 🚩 **MOVE** — When the loop is not obvious, say so and define it. Murky domains reward the candidate who imposes a loop rather than pretending one was given.

There is no daily loop here; this is a periodic cycle, not a habit. The loop is per-review: open a review, recall the evidence, assess against a few dimensions, write specifics, submit. The design problem is making that one sitting produce a good review despite imperfect memory.

**MVP boundary.**
In: the manager's review-writing surface, with evidence surfaced to fight the blank page and recency bias. Out for v1: self-reviews, peer/360 feedback, calibration, goal setting, the cycle-configuration admin, analytics.

**The real problem vs the brief's problem.**
> 🚩 **MOVE** — Separate the real problem from the brief's surface problem. In this vertical it is the entire challenge. The directors read this paragraph hardest because the brief gave them almost nothing.

The brief says "help companies run performance reviews," which sounds like a forms-and-workflow engine: rating scales, routing, deadlines. The real problem is that reviews are low quality because managers write them from memory under time pressure, and a workflow engine does nothing about that. It just routes bad reviews faster. The actual leverage is reducing the recall burden at the moment of writing, so the review is grounded in what happened rather than what the manager remembers from last week. Solve recall and quality follows. Build the workflow and you have automated the production of resentment.

---

## 18–30 min — Structure before screens (Figma page 2, boxes and arrows)

**Entry point:** manager gets a cycle notification, "6 reviews due by 12 July," and lands on a list of their direct reports to review. They arrive under deadline pressure.

**The 3 to 5 steps per review:**
1. Open one person's review.
2. Recall: the screen surfaces evidence from the period (goals hit, past 1:1 notes, prior feedback, peer mentions if available) so the manager is not starting blank.
3. Assess against a small set of dimensions, kept few on purpose.
4. Write specifics, with the evidence sitting right there to reference.
5. Submit, with a light check that flags an empty or suspiciously thin section before it goes.

**States to design for:**
- Cycle overview: who is done, who is pending, deadline.
- Blank review (the enemy state): must never feel like a blank page.
- In-progress, saved: managers write reviews across several sittings, so draft state is core, not a nicety.
- Thin-review warning: a gentle nudge when a section is empty or one line.
- Submitted, locked.

**Output the manager has at the end:**
Specific, evidence-grounded reviews submitted on time, that they would be comfortable reading aloud to the employee.

Decision to record on this page: **evidence-alongside-writing, not a blank form with a deadline.** A blank form plus a due date is the spreadsheet-and-Word-doc status quo with a progress bar added. The structural bet is that the review is written next to the evidence, not from memory.

---

## 30–50 min — Design the core flow (Figma page 3)

> 🚩 **MOVE** — One real screen open by minute 35. This is the vertical where you are most at risk of over-framing, because the problem work is so rich. Set a hard stop and open the screen even if the framing feels unfinished.

Build one screen properly: **the manager's single-review writing surface, evidence on one side, writing on the other.**

Layout, two-panel:
- Left panel, evidence (the differentiator): the employee's goals for the period and their status, dated highlights pulled from 1:1 notes, prior feedback given during the cycle, peer mentions if in scope. Scannable, timestamped, so the manager sees February as well as last week.
- Right panel, the review: a small number of dimensions, not a long rubric. Each is a short prompt plus a text field, not a bare 1 to 5 star rating. The prompts ask for specifics: "What did they deliver this period? Point to something concrete."
- Each evidence item can be referenced into the review with one action, so writing is grounded by default.
- Footer: Save draft (always visible, drafts are expected), and Submit with the thin-review check.

Annotations on the screen:
- "Evidence panel is the core bet. It fights the blank page and recency bias, which are the real causes of bad reviews."
- "Dimensions kept few on purpose. More dimensions lower completion and quality, they do not raise them."
- "Prompts ask for specifics over scores. Scores without evidence are where bias hides."
- "Ratings model shown lightly. Whether the company uses a numeric scale at all is a cycle-config decision, out of scope here."
- "Visibility is employee plus management chain plus HR. Configurable visibility is named, not designed."

> ⭐ **SINGLE DECISION** — **Evidence alongside the writing, not a blank form with a deadline.** The manager writes each section next to dated evidence from the whole period, so the review is grounded by construction instead of pulled from last week's memory. Defend it three ways: user pain (the blank page under deadline is the thing managers dread and do badly), business risk (vague recency-biased reviews erode trust and make the whole product worthless), learning (validates whether grounding the write moment raises review quality, which is the metric every other performance feature depends on).

---

## 50–60 min — What I didn't build (Figma page 4)

1. **Self-reviews and 360/peer feedback.** Real and arguably essential to fairness, but each is a separate input surface. v1 proves the manager-writing problem first; the others plug into the same evidence model later.
2. **Calibration.** The cross-manager fairness conversation. A genuinely hard problem and a different user setting. Deferred deliberately, not forgotten.
3. **Goal setting.** Goals appear here as evidence, read-only. Authoring them is a separate continuous surface, not part of the review moment.
4. **Cycle configuration.** The HR-admin product: dimensions, timelines, visibility rules, reminders. Different user, separate session.
5. **Analytics and reporting.** What HR does with completed reviews. Downstream, out of scope for proving the core write experience.

> 🚩 **MOVE** — "If I had two more hours." Names the next real problem and admits the current limit. The Staff signal most candidates skip.

"If I had two more hours, I would design the evidence-capture path that runs through the year, the lightweight 1:1 note and feedback logging that feeds this panel. Right now I am assuming that evidence exists; the honest risk is that without a year-round capture habit the panel is empty, and then v1 is back to a blank form. That dependency is the thing I would validate first."

Hold one or two of these for Q&A. Do not pre-empt everything.

---

## Hour 2 — narration order (do not present the output)

1. **"Here's how I read the problem."** For Jonathan: bad reviews are written from memory under deadline, they help nobody and quietly damage trust between manager and employee, and a company that runs reviews badly is worse off than one that does not run them at all. Frame the cost.
2. **"Here's what I chose to solve."** "Performance reviews" could mean five products. I scoped it to the manager writing reviews during a cycle, and the real problem under that is recall, not workflow. I deprioritised self-reviews, calibration, and the admin product on purpose.
3. **"Here's the structure before UI."** Evidence-alongside-writing over a blank form with a deadline, and why: a workflow engine just routes bad reviews faster.
4. **"Here's what I designed and why."** The evidence panel is the bet. Tradeoff: I kept dimensions deliberately few, trading rubric completeness for completion and honesty.
5. **"Here's what's missing."** Frame the bet as a hypothesis: my core bet is that evidence-alongside-writing raises review quality, and the riskiest assumption is that the evidence exists at all. I would validate by checking whether the panel would actually be populated for real employees today. The signal I am wrong: it is empty, and v1 is back to a blank form. That is the first test I would run.

**Likely panel questions and the line to hit:**
- Marta, "Why this as the MVP?" Three axes: user pain (the dreaded blank page under deadline), business risk (vague reviews erode trust and waste the entire cycle), learning potential (validates whether grounding the write moment lifts quality, which every other performance feature depends on). Not "it felt like the right scope."
- Alberto, "How does this scale as complexity grows?" The review is composed of dimension components fed by an evidence model. Self-reviews, peer feedback, and goals are additional inputs to the same model, not new screens. Visibility is a property on each section, so adding configurable visibility or calibration extends the structure rather than breaking it. This is where keeping dimensions few and the model clean compounds.
- Jonathan, "How does this improve business outcomes?" Reviews actually get completed on time and they are specific enough to be useful, so the company gets real signal on its people instead of "great team player" boilerplate, and employees trust the process instead of resenting it. That is retention and manager credibility, not paperwork.
- Compensation, if raised: "That depends on where this sits in your framework. Senior or Staff?" Then €80K or €93K. Do not volunteer first.
