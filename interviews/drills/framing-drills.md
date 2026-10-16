# Framing drills

Created 2026-10-16 after the Alan live case, where the synthesis came from the vision paragraph instead of the task and its data point. Rule in `memory.md` (2026-10-16).

All briefs below are **made up for practice**. Each one is written in the shape of Alan's brief: a vision, instructions, research and data, tips. Each hides **one data point that defines the problem** among distractors: a mission paragraph, industry-wide statistics, a stakeholder's favourite solution, a vivid anecdote, or a big number that doesn't matter.

Answer keys are in `framing-drills-keys.md`. Don't open them before you've done the drill.

## How to run a drill (10 minutes, understanding only)

1. Set a timer for 10 minutes. Read the brief once, start to finish, before writing anything.
2. Write these six lines, and nothing else:
   1. **Task:** what they asked for, in one line, in your words.
   2. **Signal:** the one number or break point that defines the problem. Quote it.
   3. **Noise:** what you're setting aside, and why each item doesn't define the problem.
   4. **Problem statement:** for [user] in [situation], the problem is [X], shown by [the signal].
   5. **Metric:** baseline → target, measuring the signal. Add one guardrail.
   6. **Three questions** you'd ask first, ranked.
3. Run the check: does line 4 quote line 2? Would line 5 move if the problem got solved?
4. Paste your six lines into a session with Claude and ask for scoring against the key.

Scoring, 0–2 per line (12 max). The pass mark is 10, with lines 2 and 4 both at 2. If you pick the wrong signal, the drill fails whatever the other lines score.

To practise the full case afterwards, take the same brief into the 20/70 format with Claude playing the interviewer.

---

## Drill 1: Rentwise, "Get your deposit back"

**Our vision**
Housing is broken. Rents in Europe's major cities rose 30% in five years, and young people spend up to 45% of their income on housing. Rentwise wants to make renting fair and transparent for everyone.

**Instructions**
- We're designing a feature in the Rentwise tenant app.
- Rentwise manages tenancies between private landlords and tenants, including the security deposit, which Rentwise holds.
- The objective is to **design the experience of getting the deposit back after moving out**.
- First version in 3 weeks, with 2 engineers. Landlords use a separate web portal.

**Initial research and data**
- Median time to return a deposit is 34 days. The legal maximum in our main market is 30.
- 41% of tenant support tickets in the month after move-out are "where is my deposit?".
- In 60% of returns, the delay sits between move-out and the landlord submitting the check-out inspection report.
- Our CEO believes an AI chatbot answering deposit questions would cut tickets significantly.
- In interviews, one tenant told us she had to borrow money from her parents to pay the next deposit while waiting for the old one.

**Useful tips**
Focus on the user journey, not the UI. Make assumptions where needed.

### Lines
1. **Task:** Design the experience to get deposit after moving out
2. **Signal:** Median time to return a deposit is 34 days when it should be 30
3. **Noise:** Rents rose 30% in 5 years, 45% of their income spent in housing, ceo ai chatbot
4. **Problem statement:** Tenants after moving-out need to get the deposit within 30 days, shown by median time to return a deposit
5. **Metric:** Median time to return a deposit
6. **Three questions:** Why do landlords take that amount of time to submit the check-out report?  What happens between the check-out and the deposit return? Why do we need to fix this now?

---

## Drill 2: Fleetly, "Report it before it breaks"

**Our vision**
Last-mile delivery produces 25% of urban transport emissions. Fleetly helps delivery companies move to electric fleets and run them well. By 2030, we want every van we manage to be electric.

**Instructions**
- We're designing a feature in the Fleetly driver app (Android, mounted in the van).
- Fleetly manages maintenance for delivery companies with fleets of 50 to 500 vans.
- The objective is to **design how drivers report vehicle issues**.
- First version in 4 weeks, with 3 engineers.

**Initial research and data**
- Drivers make around 120 stops a day and are paid partly per delivery.
- Today, drivers report issues by calling the dispatcher. Average call: 6 minutes.
- In our breakdown reviews, 70% of breakdowns followed a warning sign the driver had noticed in the previous week but didn't report.
- 38% of drivers say they worry about EV range on long routes.
- Last month a van broke down on a motorway with a full load and the driver waited 4 hours for recovery. The story went round the whole company.

**Useful tips**
Focus on the user journey, not the UI. The team has deep knowledge of drivers and fleet operations.

### Lines
1. **Task:** Design reporting vehicle issues for drivers in the app
2. **Signal:** 70% of breakdowns followed a warning sign the driver had noticed in the previous week but didn't report
3. **Noise:** 25% of urban transport emissions -> irrelevant, drivers make around 120 stops -> irrelevant, 38% of drivers say they worry -> that’s an opinion; last month… -> a story
4. **Problem statement:** For drivers reporting issues, the problem is they didn’t report the warning sign, shown by the 70% breakdown
5. **Metric:**
6. **Three questions:**

---

## Drill 3: Learnloop, "A first week that sticks"

**Our vision**
1.5 billion people are learning English, and language is the biggest barrier to career mobility. Learnloop wants every employee in the world to be able to work in any language.

**Instructions**
- Learnloop is a language-learning app that companies buy for their employees.
- The objective is to **improve retention in the learner's first week**.
- First version in 3 weeks, with 2 engineers and 1 content designer.

**Initial research and data**
- 46% of new learners are inactive by day 7.
- 55% of learners who drop out in week 1 never finish the placement test. The test takes about 18 minutes.
- Learners who finish the placement test have 74% week-1 retention.
- HR admins at our customers keep asking for better completion reports to share with leadership.
- Our competitor launched streaks and leaderboards last quarter and got a lot of press.

**Useful tips**
Remember who buys and who uses. Focus on the journey.

---

## Drill 4: Medlink, "Renew my prescription"

**Our vision**
Chronic disease accounts for 80% of healthcare spending in Europe, and there aren't enough GPs. Medlink wants to give people with long-term conditions a care experience that fits around their lives.

**Instructions**
- Medlink is an app that connects patients with their GP practice.
- The objective is to **design the repeat-prescription request flow**.
- First version in 2–3 weeks, with 2 engineers. Only the GP can approve a prescription.

**Initial research and data**
- Patients with chronic conditions request a repeat prescription on average every 6 weeks.
- 1 in 3 requests is rejected by the GP because the patient picked the wrong medication or dosage. Today patients type the medication name in a free-text field.
- A rejected request takes 6 days on average to resolve, and some patients run out of medication meanwhile.
- GPs say they spend too much time on admin and would love AI to help them.
- NPS for the app is 21. The top complaint in comments is "the app is slow".

**Useful tips**
You don't need to redesign the GP side. Make assumptions where needed.

---

## Drill 5: Basketly, "When something's out of stock"

**Our vision**
A third of all food produced is wasted. Basketly delivers groceries in 30 minutes and wants to build the most sustainable grocery supply chain in Europe.

**Instructions**
- Basketly is a quick-commerce grocery app in Spain and Portugal.
- The objective is to **design what happens when an ordered item is out of stock**.
- First version in 3 weeks, with 2 engineers. Pickers in the warehouse use a separate handheld app.

**Initial research and data**
- 18% of orders contain at least one item that's out of stock when picked.
- Today, the picker either picks a substitute or skips the item, without asking the customer.
- 40% of customers with a substituted item contact support, and 1 in 4 of them asks for a refund on the substitute.
- Our head of sustainability wants a "zero waste" badge on products close to their expiry date.
- Average order value is EUR 34 and has grown 12% this year.

**Useful tips**
Consider both the customer and the picker. Focus on the journey.

---

## Results log

| Date | Drill | Score | Signal right? | Note |
| --- | --- | --- | --- | --- |
| 2026-10-16 | 1 Rentwise | 8/12, below pass | Partly | Took the outcome (34 vs 30 days) as the signal. Saw the landlord inspection step (60% of delay) but only used it in a question. The problem statement restated the goal. |
