# Factorial Practice Challenge B — Time & Attendance

Worked example. Structure mirrors the four Figma pages from the round 3 hour-1 playbook: Problem framing, Core flow, Design, What I didn't build. Use it to see the reasoning bar, not as a script. This brief has a scope trap planted in the wording; the worked solution shows how to name the seam instead of designing both halves.

> **Flag legend**
> 🚩 **MOVE** — a rehearsable tactical action. Transferable to any brief. Internalise these, not the specific design.
> ⭐ **SINGLE DECISION** — the spine. One decision the whole solution hangs on, defensible three ways (user pain, business risk, what it teaches).

---

## The brief (as handed to you)

> The spinoff needs clock in / clock out for hourly and shift workers. Design v1 of how an employee tracks their time and how that time gets to payroll. 60 minutes.

> 🚩 **MOVE** — Spot the scope trap in the wording. "And how that time gets to payroll" quietly doubles the scope into two surfaces with two different users. Designing both is the Senior move. Name the seam and pick one.

The trap is "and how that time gets to payroll." That quietly doubles the scope into two surfaces with two different users. Designing both is the Senior move. Name the seam and pick one.

---

## 0–8 min — Clarifying questions (ask before opening Figma)

> 🚩 **MOVE** — Questions before Figma. Even when the brief says "start working." Senior candidates solve the prompt; Staff candidates reshape it first.

1. "Platform: are these workers on personal mobile, a shared kiosk or tablet at a site, or desktop? A warehouse kiosk and a remote phone are different designs." Highest-leverage question. Get this wrong and the whole flow is wrong.
2. "The brief mentions getting time to payroll. I read that as a separate surface with a different user, the payroll admin. For v1 should I focus on the employee tracking experience and define the handoff, or is the payroll side the priority?" This is you naming the seam, on the record.
3. "Optimising for speed, for compliance, or for correcting errors? A worker clocks in hundreds of times a month, so friction compounds; but the legal record has to hold up."
4. "Can an employee edit their own timesheet, or does a manager approve corrections?" The delegated-authority branch, in attendance clothing.

> 🚩 **MOVE** — Name the hidden branch out loud. Surfacing the worst real-world failure unprompted signals you see past the happy path.

Hidden branch to name out loud:
"The single highest-friction real event in this domain is the forgotten clock-out. I will design for it explicitly rather than treat it as an edge case, because it is the one that generates payroll disputes."

Assume for this worked example: **shared tablet kiosk at the work site, focus on the employee tracking experience with a defined payroll handoff, optimise for speed plus error correction, manager approves corrections.**

---

## 8–18 min — Problem framing (Figma page 1, leave it visible)

**Who is the primary user?**
The hourly shift worker at a shared kiosk. Low patience, gloves or wet hands possible, often a queue behind them at shift change. Not a knowledge worker at a laptop.

**The one job that creates the most friction or cost?**
Recording an accurate start and end of shift in under a few seconds, and recovering cleanly when they forget. Accuracy here is money: every wrong entry is a payroll correction or a dispute later.

**Success vs failure.**
Success: worker clocks in or out in one tap, sees instant unambiguous confirmation, and the forgotten clock-out has a fast self-serve fix. Failure: ambiguous state, the worker is not sure if it registered, double-clocks or skips, and payroll inherits a mess weeks later.

**Business objective (one line).**
Cut the volume of payroll corrections and the disputes they cause. Measure: corrections per pay period, time-entry accuracy, and admin reconciliation hours. The user's win is a fast certain punch; the business's win is a clean record that needs no human cleanup.

**The core loop (daily):**
Arrive, identify self, clock in, get confirmation. Reverse at end of shift. Breaks if in scope. That is it, hundreds of times a month. Every gram of friction multiplies.

**MVP boundary.**
In: the kiosk clock-in / clock-out experience, instant confirmation, and the forgotten-clock-out correction. Out for v1: payroll calculation, scheduling and shift assignment, overtime rules, geofencing, biometric identity.

**The real problem vs the brief's problem.**
> 🚩 **MOVE** — Separate the real problem from the brief's surface problem. The highest-value paragraph on the page. The directors read it.

The brief frames a data-capture pipeline: track time, send to payroll. The real problem is trust and speed at the moment of capture. A worker who is not certain the tap registered is the root cause of every downstream payroll dispute. Solve certainty-in-one-tap and the payroll data is clean by construction. The payroll handoff is then a boring, reliable export, not a design problem.

---

## 18–30 min — Structure before screens (Figma page 2, boxes and arrows)

**Entry point:** worker walks up to the kiosk. The screen is already showing the clock, idle, ready. No login wall as the first barrier.

**The 3 to 5 decisions / steps:**
1. Identify (PIN or badge tap, fast, not a password).
2. System shows current state: you are clocked OUT, ready to clock IN. Or the reverse.
3. One primary action, sized for the current state.
4. Instant confirmation: large, unambiguous, "Clocked in at 08:02, Maria."
5. Exception path: "Forgot to clock out yesterday?" surfaced when the system detects an open shift.

**States to design for:**
- Idle / ready (default).
- Identified, clocked out, offering Clock in.
- Identified, clocked in, offering Clock out.
- Confirmation (the most important state, must be impossible to misread).
- Open-shift detected: forgotten clock-out recovery.
- Offline: kiosk loses connection. Queue the punch locally, confirm, sync later. Name this even if not fully drawn, because a kiosk that fails silently when the wifi drops is a payroll disaster.

**Output the user has at the end:**
A recorded, confirmed punch they trust, and a clean record that flows to payroll without human cleanup.

Decision to record: **state-first, single primary action.** The kiosk always shows your current state and offers exactly one obvious next action, never both clock-in and clock-out as equal buttons. Tradeoff named: one identify step costs a tap, but it lets the system show the right single action and removes the most common error, clocking the wrong direction.

---

## 30–50 min — Design the core flow (Figma page 3)

Build one screen properly: **the kiosk confirmation moment, with the identified clocked-in state and the forgotten-clock-out recovery as a second frame.**

Kiosk, identified, clocked-in state:
- Large greeting and current status: "Maria, you are clocked in since 08:02."
- One large primary button: Clock out. Sized for a thumb, reachable, high contrast.
- Today's hours so far, small, for reassurance.
- After tap: full-screen confirmation, "Clocked out at 16:31. 8h 29m today." Auto-returns to idle after a few seconds so the next worker has a clean screen.

Forgotten-clock-out recovery frame:
- On identify, if an open shift from a previous day is detected: "You did not clock out yesterday. When did your shift end?" with quick presets (scheduled end time, or enter manually).
- The correction is flagged for manager approval, not silently accepted. Annotation: "Self-serve fix, manager-approved. Balances speed against an auditable record."

Annotations on the screen:
- "Kiosk, shared device. Identity is PIN or badge, not password. Biometric out of scope for v1."
- "Confirmation is the core bet: the worker must never wonder if it registered."
- "Offline punches queue locally and sync. Logic noted, full design deferred."
- "Payroll handoff: this data exports to the payroll surface. That surface and its user are out of scope, named not designed."

**Hard constraint met: one real screen open by minute 35.** If you are still drawing flows, open the confirmation screen rough and refine.

> ⭐ **SINGLE DECISION** — **State-first single action over a symmetric clock-in/clock-out pair.** It costs one identify tap and removes the most expensive everyday error, punching the wrong direction at shift change when there is a queue and no patience. Defend it three ways: user pain (speed and certainty under queue pressure), business risk (every ambiguous punch is a future payroll dispute), learning (validates whether one-tap certainty cuts correction volume).

---

## 50–60 min — What I didn't build (Figma page 4)

1. **Payroll calculation and the admin surface.** The seam I named at minute 5. Different user, different problem. v1 produces clean data and exports it; designing the payroll engine in 60 minutes would be shallow.
2. **Scheduling and shift assignment.** Who works when is upstream of tracking. Real, separate, deferred.
3. **Overtime and break rules.** Compliance logic that varies by country and contract. A rules layer, not a v1 screen.
4. **Geofencing and biometric identity.** Adoption and anti-fraud features. They matter once the core capture loop is trusted, not before.
5. **Manager approval dashboard.** Corrections route to a manager, but their review surface is a separate screen I would design after validating the worker side.

> 🚩 **MOVE** — "If I had two more hours." Names the next real problem and admits the current limit. The Staff signal most candidates skip.

"If I had two more hours, I would design the offline-and-sync model properly. A kiosk that drops connection mid-shift and loses punches silently is the failure that destroys trust in the whole system, and right now I have only noted it, not solved it."

Hold one or two for Q&A. Do not pre-empt everything.

---

## Hour 2 — narration order (do not present the output)

1. **"Here's how I read the problem."** For Jonathan: the worker punches hundreds of times a month, every ambiguous tap becomes a payroll dispute weeks later, and disputes cost admin time and worker trust. Frame the cost the business pays now.
2. **"Here's what I chose to solve."** The brief said track-time-and-send-to-payroll. I split that seam and chose the capture moment, because clean capture makes the payroll handoff trivial and dirty capture makes it impossible. I deprioritised the payroll surface on purpose.
3. **"Here's the structure before UI."** State-first single action over a symmetric pair, and why: removes the wrong-direction punch, the most common shift-change error.
4. **"Here's what I designed and why."** Confirmation is the bet. The forgotten-clock-out recovery is designed in, not treated as an edge case, because it is the top dispute generator.
5. **"Here's what's missing."** Frame the bet as a hypothesis: my core bet is that one-tap certainty cuts errors, and the riskiest assumption is the offline case, whether punches survive a connection drop. I would validate by piloting one site and comparing correction volume to baseline. The signal I am wrong: disputes do not drop. That is the test I would run before shipping.

**Likely panel questions and the line to hit:**
- Marta, "Why this as the MVP?" Three axes: user pain (speed and certainty at the kiosk under queue pressure), business risk (every ambiguous punch is a future payroll dispute and an admin cost), learning potential (validates whether one-tap certainty reduces correction volume, which is the metric the whole product lives or dies on).
- Alberto, "How does this scale as complexity grows?" The kiosk renders from a single attendance-state model: clocked-in, clocked-out, open-shift, offline-queued. Breaks, overtime flags, and multi-location all extend that state model rather than adding screens. The confirmation and state-first pattern is reusable across any punch surface, mobile or kiosk.
- Jonathan, "How does this improve business outcomes?" Fewer payroll disputes, less admin time spent reconciling timesheets, and workers who trust their hours are recorded right. It turns a recurring monthly cleanup cost into a non-event.
- Compensation, if raised: "That depends on where this sits in your framework. Senior or Staff?" Then €80K or €93K. Do not volunteer first.
