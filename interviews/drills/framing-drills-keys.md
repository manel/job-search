# Framing drills: answer keys

Don't read before doing the drill. Briefs are in `framing-drills.md`. Each key is one reasonable answer, not the only one. A different signal can still score if it's argued from the brief's own data and the direction would move the metric.

---

## Drill 1: Rentwise

- **Task:** the tenant's journey from move-out to deposit received.
- **Signal:** in 60% of returns, the delay sits between move-out and the landlord's check-out inspection report. The 41% "where is my deposit?" tickets are the symptom.
- **Noise:**
  - rent inflation and income share: market context that no deposit flow can change
  - the CEO's chatbot: a solution, and it answers the symptom (tickets), not the cause (the inspection step)
  - the borrowing anecdote: explains the emotional stakes (put it in the user's state), but doesn't define the problem
- **Trap:** the task says "tenant app", but the cause sits with the landlord. A strong answer notices this and designs what the tenant can do or see at that step: inspection status visible, a joint or tenant-led check-out with photos at move-out, an automatic reminder to the landlord. It also asks whether Rentwise can enforce the deadline.
- **Problem statement:** for tenants who have moved out, the problem is that they can't see or speed up the landlord's inspection step, which causes the delay in 60% of returns and drives the 41% ticket share.
- **Metric:** median days to deposit return, 34 → under 30 (the legal limit). Guardrail: disputed deductions don't rise.
- **Top questions:** Can Rentwise enforce an inspection deadline on landlords? What does the tenant see today after move-out? Why do landlords delay the report?

## Drill 2: Fleetly

- **Task:** how drivers report vehicle issues.
- **Signal:** 70% of breakdowns followed a warning sign the driver noticed but didn't report. Reporting means a 6-minute call, for drivers paid per delivery at 120 stops a day.
- **Noise:**
  - emissions and the EV mission
  - the 38% range anxiety figure: a real driver concern, but not about reporting
  - the motorway anecdote: shows the cost of a breakdown, but pulls you towards recovery, not reporting
- **Trap:** designing for the breakdown moment (recovery, roadside help) when the problem is the moment a week earlier when the driver noticed something and said nothing.
- **Problem statement:** for drivers mid-shift who notice a warning sign, the problem is that reporting costs them 6 minutes of paid time, so most signs go unreported, and 70% of breakdowns had one.
- **Metric:** share of breakdowns with a prior unreported warning, 70% → 40%; or reports per 1,000 driving hours, up from baseline. Guardrail: no rise in false reports clogging maintenance.
- **Top questions:** What happens after a report today, and does the driver hear back? Can a report wait until the end of the shift or a stop? Who decides whether the van keeps driving?

## Drill 3: Learnloop

- **Task:** week-1 retention for learners.
- **Signal:** 55% of week-1 dropouts never finish the 18-minute placement test; those who finish retain at 74%.
- **Noise:**
  - 1.5 billion learners and the career-mobility mission
  - HR completion reports: the buyer's need, valid, but not week-1 retention for learners
  - the competitor's streaks: a solution looking for a problem
- **Trap:** jumping to engagement mechanics (streaks, reminders, gamification) when the drop happens before learning even starts.
- **Problem statement:** for new learners, the problem is that an 18-minute placement test stands between signing up and the first lesson, and 55% of week-1 dropouts never finish it.
- **Metric:** day-7 active learners, 54% → 65%; placement completion rate, up from baseline. Guardrail: placement accuracy (learners moved between levels in week 2) doesn't get worse.
- **Top questions:** Where in the test do people quit? Does the test need to be complete before the first lesson? Is the 74% correlation or cause (are finishers just more motivated)?

## Drill 4: Medlink

- **Task:** the patient's repeat-prescription request.
- **Signal:** 1 in 3 requests is rejected because the patient picked the wrong medication or dosage in a free-text field; each rejection costs 6 days.
- **Noise:**
  - chronic-disease spending and the GP shortage
  - GPs wanting AI: a GP-side wish, and the brief says don't redesign the GP side
  - NPS 21 and "the app is slow": real, but not this flow's problem
- **Trap:** proposing AI (for the GP or for symptom input) when the fix is structured input: show the patient's current medication list from their record and let them select it.
- **Problem statement:** for patients with chronic conditions renewing medication, the problem is that free-text entry leads to wrong medication or dosage, causing 1 in 3 requests to be rejected and 6 days of delay.
- **Metric:** rejection rate for wrong medication or dosage, 33% → under 10%. Guardrail: time to approval doesn't rise; no patient runs out because of the new flow.
- **Top questions:** Can we read the patient's current prescriptions from the GP system? What does a patient see after a rejection today? Which requests must the GP see in full, and which could be pre-filled?

## Drill 5: Basketly

- **Task:** the out-of-stock moment for the customer (and the picker).
- **Signal:** substitutes are chosen without asking the customer, and 40% of customers who get one contact support, 1 in 4 of them for a refund.
- **Noise:**
  - food waste and the sustainability mission
  - the zero-waste badge: a stakeholder's pet feature, unrelated to out-of-stock
  - order value growth: a business-health number that doesn't define this problem
- **Trap:** treating the 18% out-of-stock rate as the problem. Stock levels are operations. The design problem is that the customer has no say.
- **Problem statement:** for customers whose ordered item is out of stock, the problem is that the picker substitutes without asking, which leads 40% of them to contact support.
- **Metric:** support contacts per substituted order, 40% → 15%. Guardrail: delivery time stays within 30 minutes (asking the customer mustn't hold up the picker).
- **Top questions:** How long can a picker wait for a customer's answer? Do we know at order time what's likely to be out of stock? Can customers set substitution preferences before checkout?
