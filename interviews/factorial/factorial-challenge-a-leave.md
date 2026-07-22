# Factorial Practice Challenge A — Leave Management

Worked example. Structure mirrors the four Figma pages from the round 3 hour-1 playbook: Problem framing, Core flow, Design, What I didn't build. Read it as a reference for what Staff-level reasoning looks like end to end, not a script to memorise. The real brief will differ; the order of moves should not.

> **Flag legend**
> 🚩 **MOVE** — a rehearsable tactical action. Transferable to any brief. Internalise these, not the specific design.
> ⭐ **SINGLE DECISION** — the spine. One decision the whole solution hangs on, defensible three ways (user pain, business risk, what it teaches).

---

## The brief (as handed to you)

> Factorial's spinoff is building leave management from scratch. Design the core experience for requesting and approving time off. You have 60 minutes. Start working.

The sparseness is the test. Do not start working.

---

## 0–8 min — Clarifying questions (ask before opening Figma)

> 🚩 **MOVE** — Questions before Figma. Even when the brief says "start working." Senior candidates solve the prompt; Staff candidates reshape it first.

Pick 3 to 4. Each one should reshape the design depending on the answer, otherwise it is filler.

1. "Who is the primary user for v1: the employee requesting, the manager approving, or the HR admin who owns the policy?" Forces them to commit, and tells them you know these are three different products.
2. "Is approval authority centralised with HR, or delegated to team managers?" This is the highest-leverage branch. Centralised is one queue and one approver. Delegated means routing, escalation, and coverage logic.
3. "Are we optimising for request speed, for policy compliance, or for balance trust? I can design for one cleanly, not all three."
4. "Greenfield spinoff, so I assume no existing accrual engine. Is balance calculation in scope, or do I treat balance as a given input?"

> 🚩 **MOVE** — Name the hidden branch out loud. HR and finance flows expand into permissions, delegation, exceptions, audit. Surfacing one unprompted signals you see the problem the brief is hiding.

Hidden branch to name out loud even if they wave you on:
"Before I lock anything I would clarify what happens when two people on the same team request the same week. Coverage conflict is where the real friction lives, and whether it is in scope changes the manager flow significantly."

Assume for this worked example: **primary user is the team manager, authority is delegated, optimise for approval speed and balance trust, accrual is an input not in scope.**

---

## 8–18 min — Problem framing (Figma page 1, leave it visible)

**Who is the primary user?**
Team manager. Not the employee. The employee requests once a quarter; the manager processes requests every week and is the bottleneck. Designing for the high-frequency user is the higher-leverage choice.

**The one job that creates the most friction or cost?**
Deciding on a leave request with enough context to say yes or no without a side conversation. Today, in spreadsheet-and-email companies, the manager has to leave the request to go check: does this person have the balance, who else is off that week, is this a busy period. The decision is cheap; gathering context is expensive.

**Success vs failure.**
Success: manager approves or declines in one screen, in seconds, with full confidence. Failure: manager rubber-stamps without seeing a coverage clash, then has to walk it back, which costs trust with two employees.

**Business objective (one line).**
Cut approval cycle time and eliminate the approvals that get reversed or escalated after a missed clash. Measure: time-to-decision, and the rate of reversed or escalated approvals. The user's win is a fast confident decision; the business's win is fewer reversals and reclaimed manager time.

**The core loop (weekly, not edge cases):**
Manager opens a queue of pending requests, sees each request with balance and team coverage inline, decides, moves on. That is the loop. Everything else is support around it.

**MVP boundary.**
In: the manager decision surface, with balance and coverage context inline. The employee request form, minimal. Out for v1: accrual rules, policy configuration, multi-level approval chains, calendar integrations, reporting.

**The real problem vs the brief's problem.**
> 🚩 **MOVE** — Separate the real problem from the brief's surface problem. This is the single highest-value paragraph on the page. The directors read it.

The brief says "requesting and approving time off," which sounds like a two-sided form-and-button flow. The real problem is decision context. Approval is not a workflow step that needs a button; it is a judgment that needs information co-located. Solve context and the button is trivial. Build the button without context and you have shipped the spreadsheet with nicer styling.

---

## 18–30 min — Structure before screens (Figma page 2, boxes and arrows)

**Entry point:** manager gets a notification, or opens a "Pending approvals" item in their nav. They arrive with intent: clear the queue.

**The 3 to 5 decisions the manager makes per request:**
1. Does this person actually have the balance? (yes / no / borderline)
2. Is the team covered that week? (clash / clear)
3. Is this a protected or busy period? (blackout / fine)
4. Approve, decline, or ask a question.

**States to design for:**
- Empty: no pending requests. The good state. Reassure, do not leave blank.
- Queue with items: the working state.
- Single request expanded: the decision moment.
- Conflict surfaced: two people, same week.
- Post-decision: confirmation, undo window, employee notified.

**Output the user has at the end they did not have at the start:**
A cleared queue and a defensible decision, made without leaving the screen to gather context.

Decision to record on this page: queue-with-inline-context, not a one-request-at-a-time wizard. A wizard is cleaner per request but hides the cross-request signal (two people, same week), which is exactly the information that prevents the costly mistake. Tradeoff named: I trade a slightly busier screen for cross-request visibility, because the expensive failure is a missed clash, not a slow single decision.

---

## 30–50 min — Design the core flow (Figma page 3)

Build one screen properly: **the manager approval queue with an expanded request.**

Layout, top to bottom:
- Header: "Pending approvals (4)". Count anchors the job: clear this.
- List of request rows. Each row, collapsed, carries the decision-critical facts inline so the manager can often decide without expanding:
  - Employee name and team
  - Dates and total days
  - Balance after this request (e.g. "9 days left after this"), colour-weighted if it goes negative or near zero
  - Coverage signal: a small indicator that says "2 others off this week" or "team clear", clickable
- Expanded row: adds a mini team-calendar strip for the requested week showing who else is off, the reason if provided, and three actions: Approve, Decline, Ask.
- Decline requires a one-line reason. Approve is one click with a short undo window.

Annotations placed directly on the screen:
- "Balance shown is read from the accrual engine, treated as input. Accrual logic out of scope for v1."
- "Coverage strip is the core bet. It is the difference between this and an email approval."
- "Happy path shown. Decline-with-reason and the ask-a-question thread are stubbed, not designed."
- "Employee request form is a secondary surface. Designed minimally, linked, not the focus."

**Hard constraint met: one real screen open by minute 35.** If you are still in flow diagrams here, stop and open this screen rough.

> ⭐ **SINGLE DECISION** — **Coverage context inline, not a separate calendar view.** A manager who has to open a separate calendar to check coverage will stop checking. Co-locating the clash with the decision is the whole product. Defend it three ways: user pain (the weekly context detour), business risk (rubber-stamped clashes cost trust), learning (validates whether inline context changes manager behaviour).

---

## 50–60 min — What I didn't build (Figma page 4)

Five things scoped out, one line each:

1. **Accrual and balance calculation.** Treated as input. It is a deep rules engine and a different problem; designing it in 60 minutes would be shallow on both.
2. **Policy configuration.** The HR-admin surface for defining leave types and entitlements. Real, separate user, separate session.
3. **Multi-level approval chains.** Assumed single delegated approver for v1. Chains are a routing problem I would design once the single-approver decision surface is validated.
4. **Calendar and payroll integrations.** Important for adoption, not for proving the core decision loop works.
5. **Mobile.** Managers do approve from their phone. I would design the queue mobile-first in v2 once the information model is settled, because the coverage strip is the hard responsive problem.

> 🚩 **MOVE** — "If I had two more hours." Names the next real problem and admits the current limit. This is the Staff signal most candidates skip.

"If I had two more hours, I would design the conflict-resolution flow: what the manager does when there is a clash, since approve-anyway, decline, or propose-alternative-dates is the actual hard decision and right now I have only surfaced the clash, not helped resolve it."

Keep one or two of these for Q&A rather than pre-empting everything. Over-annotating reads as defensive.

---

## Hour 2 — narration order (do not present the output)

1. **"Here's how I read the problem."** For Jonathan: the manager is the bottleneck, every leave decision today costs a context-gathering detour, and a missed coverage clash costs trust with two employees. Frame the cost the business pays now.
2. **"Here's what I chose to solve."** The real problem is decision context, not the approval button. Name that I deprioritised the employee request form and the accrual engine on purpose.
3. **"Here's the structure before UI."** Queue-with-inline-context over a wizard, and why: cross-request visibility prevents the expensive mistake.
4. **"Here's what I designed and why."** The coverage strip is the bet. State the tradeoff: busier screen for clash visibility.
5. **"Here's what's missing."** Conflict resolution is the next thing and the riskiest gap. Frame the bet as a hypothesis: my core bet is that inline coverage changes the decision, and the riskiest assumption under it is that managers actually look at it and trust it. I would validate by watching a handful of managers clear a queue with a planted clash. The signal I am wrong: they approve straight through it anyway. That is the test I would run before building further.

**Likely panel questions and the line to hit:**
- Marta, "Why this as the MVP?" Three axes: user pain (the weekly context detour), business risk (rubber-stamped clashes cost trust and rework), learning potential (validates whether inline context changes manager behaviour, which informs every other approval surface in the product).
- Alberto, "How does this scale as complexity grows?" The row is a state-bearing component: balance state, coverage state, decision state. Approval chains, blackout periods, and leave types extend the same model without a new screen. The coverage strip is a reusable pattern any approval surface in the HRIS can adopt.
- Jonathan, "How does this improve business outcomes?" It removes the back-and-forth between manager and employee that delays approvals, and it catches coverage clashes before they become two unhappy people and a reschedule. Faster approvals, fewer reversals.
- Compensation, if raised: "That depends on where this sits in your framework. Senior or Staff?" Then €80K or €93K. Do not volunteer first.
