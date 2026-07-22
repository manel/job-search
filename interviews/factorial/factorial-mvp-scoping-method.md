# Factorial — How to decide what is MVP (when you don't know the domain)

Read this at 9:55 tomorrow. The point: scoping is a reasoning move, not a domain-recall move. The panel is hiring a product designer, not an HR consultant. They know you are not an HR expert. They are testing whether you can carve scope under ambiguity. That is a method, and it runs on a domain you have never seen.

---

## The core-loop test (this is the whole thing)

1. **Find the single core loop.** The one thing the primary user does, repeatedly, that the product exists to make better. One user, one job, one loop.
2. **For everything else, ask one question:** does the core loop still produce value without this in v1?
   - If yes, it is not MVP. Defer it.
   - If no, it is in.
3. **Assume away the hard inputs.** If something deep is needed but is not the loop itself, treat it as a given input. The leave balance can be a number you assume exists; you do not have to build the engine that calculates it.

You do not need to know what "accrual" is to know the manager can still approve a request whether or not the system calculates the balance. The loop survives without it. That is the test, every time.

---

## The seven axes (this is where the "what I didn't build" list comes from)

Scope expands along the same seven directions in any workflow product. Once you have named your core loop, walk these out loud and ask "what is the version of this for the thing in front of me." This is how you produce a credible deferral list without knowing the domain.

1. **Configuration / admin** — someone sets up the rules. Almost always a different user. Defer.
2. **Upstream** — what feeds the data in.
3. **Downstream** — what consumes the output: reporting, analytics, integrations, exports.
4. **Permissions / delegation** — who can see or do what, multi-level approval, delegated authority.
5. **Compliance / rules engines** — calculations and legal logic. Deep, country-specific. Defer.
6. **Adjacent inputs** — other people's contributions to the same artifact.
7. **Platform variants** — mobile, offline, multi-region, biometric / identity, kiosk vs personal device.

Every item in all three worked-challenge deferral lists came from these axes, not from HR knowledge. Geofencing and biometric: axis 7. Overtime rules: axis 5. Scheduling: axis 2. Memorise the seven. Reciting them sounds like domain fluency; it is actually just a checklist.

---

## Two safety rules

- **Your clarifying questions buy the domain knowledge you lack.** The panel is the domain expert in the room. "Is balance calculation in scope, or do I treat it as an input?" both signals seniority and extracts the fact you do not have. You are not supposed to walk in knowing the domain. You are supposed to know how to interrogate it.
- **You can defer something even if you are not sure it is a real feature.** "I would also defer anything around delegated approval authority" is a strong line whether or not Factorial has built that. No penalty for deferring something that turns out not to exist. Big penalty for trying to build everything.

---

## Two-line domain primer for the eight verticals

Enough vocabulary so the words are not alien. Derivable live, not required. For each: the likely core loop, and the obvious deferrals by axis. Do not memorise the deferrals; derive them tomorrow by walking the seven axes. This is here so you recognise the terms if the panel uses them.

**Time & attendance**
Core loop: worker records start/end of shift, gets confirmation. Defer: scheduling (upstream), payroll export (downstream), overtime rules (compliance), geofencing/biometric (platform).

**Leave management**
Core loop: manager decides on a request with balance and coverage context. Defer: accrual engine (compliance), policy config (admin), approval chains (permissions), calendar/payroll integration (downstream).

**Payroll**
Core loop: payroll admin reviews and runs a pay cycle, catches errors before sending. Defer: tax/deduction rules engine (compliance), time/leave feeds (upstream), payslip distribution and accounting export (downstream), corrections workflow (adjacent). Note: payroll is the most rules-heavy vertical. If you get it, scope hard to the review-and-approve moment; do not try to design the calculation.

**Recruitment / ATS**
Core loop: recruiter or hiring manager moves a candidate through pipeline stages and decides next step. Defer: job-posting/advertising (upstream), offer and onboarding handoff (downstream), interview scheduling (adjacent), permissions across hiring team (permissions), careers-page config (admin).

**Onboarding**
Core loop: new hire (or the manager) completes a sequence of tasks and documents before/at start. Defer: task/template config (admin), document e-signature engine (compliance), provisioning integrations (downstream), role-specific branching (permissions).

**Performance**
Core loop: manager writes a specific, evidence-grounded review during a cycle. Defer: self/peer/360 input (adjacent), calibration (different user), goal authoring (upstream), cycle config (admin), analytics (downstream).

**Expenses**
Core loop: employee submits an expense; approver decides with enough context to say yes. Defer: receipt OCR/extraction (compliance-adjacent), policy/limit config (admin), accounting/reimbursement export (downstream), card-feed import (upstream), multi-level approval (permissions). The real friction is usually approver context (is this within policy?), mirroring the leave pattern.

**Org structure / company hierarchy**
Core loop: HR admin views and edits the reporting structure, sees the effect. Defer: permissions derived from hierarchy (permissions), import from HRIS/payroll (upstream), headcount/cost rollups (downstream), historical versioning (compliance-adjacent). Watch the trap: this one is tempting to over-build as a fancy org chart. The job is editing structure with confidence, not rendering a pretty tree.

---

## The one line to keep in your head

Find the loop. Keep only what the loop needs. Defer everything on the seven axes. Ask the panel for the domain facts you are missing. That is senior scoping, and none of it requires you to know HR.
