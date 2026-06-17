# Business Terms and Ways of Working

A reference for refreshing the vocabulary interviewers expect a senior product designer to speak fluently. Organized by category. Use it to speak specifically, not to perform fluency.

---

## Business health metrics

**ARR / MRR (Annual / Monthly Recurring Revenue)**
The total revenue a company expects from subscriptions per year or month. ARR is the B2B SaaS standard. When a company says "we're at $10M ARR," that's the scale you're designing for. Relevant to you when you're explaining design ROI: faster onboarding → more activations → more paid conversions → ARR goes up.

**Churn rate**
The percentage of customers who cancel in a given period. High churn signals a product that doesn't deliver ongoing value. Design is directly implicated: confusing workflows, poor onboarding, and feature debt all drive churn. If you're working on a product with high churn, your design work should trace to retention, not just acquisition.

**Retention rate**
Inverse of churn. What percentage of customers stay. For B2B, retention is often broken into logo retention (did the account renew) and revenue retention (did the account expand or shrink). Net Revenue Retention (NRR) above 100% means expansion outpaces churn — a strong sign of product-market fit.

**LTV (Lifetime Value)**
How much revenue a customer generates over their full relationship with the product. High LTV justifies more investment in onboarding and activation — it means getting a user to their first value moment is worth spending engineering time on.

**CAC (Customer Acquisition Cost)**
What it costs to acquire one new customer. Design affects CAC indirectly: a product that sells itself through demos or viral loops has lower CAC than one that needs heavy sales support. For B2B, a clear product value demo reduces sales cycle length.

**Gross margin**
Revenue minus direct costs of delivering the product. Software companies typically have high gross margins (~70-80%). Relevant when discussing build vs buy decisions on the design side: a 3rd-party component library with a seat license reduces gross margin slightly but accelerates development.

---

## Product and activation metrics

**Activation**
The moment a new user first experiences the core value of the product. Not sign-up, not first login — the moment they see why they signed up. Activation is a critical design metric because it's where onboarding either works or fails. Common proxy: "user has completed [key workflow] within 7 days of sign-up."

**DAU / MAU (Daily / Monthly Active Users)**
How many users are active daily vs monthly. The ratio (DAU/MAU) is a stickiness signal. A DAU/MAU of 0.2 means users come back about 6 days out of 30. For B2B products used by finance or ops teams, DAU/MAU expectations differ from consumer apps: weekly is often the right cadence, not daily.

**Feature adoption rate**
The percentage of users or accounts using a specific feature. A low adoption rate on a feature you designed doesn't always mean bad design — it may mean discoverability, onboarding, or positioning failed. Worth distinguishing in a case presentation.

**Time to value (TTV)**
How long it takes a new user or account to reach their first meaningful outcome. Shorter TTV correlates with higher activation and retention. Onboarding design directly affects this.

**Task completion rate**
In usability research: what percentage of participants complete a defined task successfully. A standard quantitative usability metric. Pairs with time-on-task (how long it takes).

**Error rate**
How often users make errors in a workflow. Useful for evaluating form design, complex configuration UIs, or any system where mistakes are costly. High error rates in B2B workflows often show up in support volume rather than user-reported feedback.

---

## Customer satisfaction metrics

**NPS (Net Promoter Score)**
Asks: "How likely are you to recommend this product to a colleague?" on a 0-10 scale. Promoters (9-10) minus detractors (0-6) gives a score from -100 to +100. A blunt instrument — it tells you sentiment direction, not cause. In B2B, NPS surveys often go to account owners rather than end users, which distorts the signal.

**CSAT (Customer Satisfaction Score)**
A rating collected at a specific touchpoint: "How satisfied were you with this?" Usually 1-5 or 1-7. More granular than NPS for a particular workflow or support interaction. Useful for A/B comparison after a redesign.

**CES (Customer Effort Score)**
Measures how easy something was to do: "How much effort did you have to put in to accomplish this?" Lower is better. This is the metric most directly connected to design quality — complexity and friction show up here before they show up in NPS.

---

## Design system and platform metrics

**Component adoption rate**
What percentage of new UI uses design system components versus custom implementations. Used to track DS ROI. At Abacum, the target was 80% of new UI from Abax components.

**Token usage**
Whether engineers are referencing design tokens (semantic variables like `color-text-primary`) rather than hardcoded values (hex codes). A behavioral proxy for system health.

**Time-to-ship for UI**
How long it takes to build a screen or feature when a mature DS is in place versus without. Typically cited as a velocity multiplier, though hard numbers are difficult to isolate.

---

## Ways of working

**Dual-track agile**
A development model where discovery (research, problem definition, concept validation) runs in parallel with delivery (engineering, QA, shipping). The intent: by the time a feature is built, the problem is already well-understood. Contrasts with models where design happens immediately before or during a sprint.

**OKRs (Objectives and Key Results)**
A goal-setting framework: an Objective states what you want to achieve, Key Results are the measurable signals that tell you if you got there. Common in B2B SaaS. Designers are often asked how their work connects to a team or company OKR. Useful answer: "the key result for Q2 was reducing time-to-first-value — my focus was the onboarding flow."

**Design sprint (GV method)**
A 5-day structured process for answering a product question through design and testing before committing to build. Most useful for high-stakes decisions with significant uncertainty. Less useful for incremental feature work.

**Shape Up (Basecamp)**
An alternative to Scrum used at some product companies. Teams work in 6-week cycles with clear "bets" scoped upfront. No backlogs. Pitches are written documents describing a problem and a rough solution. Designers often write the pitch. The concept of "appetite" (how much time is this worth) rather than estimates.

**RICE prioritization**
A scoring framework: Reach × Impact × Confidence ÷ Effort. Helps compare features across different scales. Designers are sometimes asked to contribute to RICE scoring; your input is on Reach (does this affect the right users) and Impact (how meaningfully does it change their experience).

**Impact/effort matrix**
A simpler 2×2 for prioritization: high impact / low effort are quick wins; high impact / high effort are strategic bets; low impact / high effort are things to cut. Used in planning sessions and cross-functional alignment discussions.

**Jobs to be Done (JTBD)**
A framework for defining what a user is trying to accomplish — the "job" they hire the product to do — independent of the product's current feature set. Useful for reframing problems: instead of "users need a better import UI," the job might be "I need my data in the system before the team meeting." The job definition changes what counts as a good solution.

**North Star metric**
A single metric that best captures the value a product delivers to users. Chosen because it correlates with long-term business health. Everything else is either an input metric (things that drive the North Star) or a guardrail metric (things you can't let fall while pursuing the North Star). Knowing a product's North Star helps designers prioritize: does this feature move the number that matters?

---

## Connecting design to business outcomes

Interviewers at senior level will ask how your work tied to business results. Most design work doesn't have clean A/B tests. Here is how to speak about it without fabricating data or hedging into uselessness.

**Proxies and operational signals**
If hard metrics aren't available, name what changed operationally: CS requests dropped, implementation teams spent less time on configuration, engineers stopped asking questions in Slack about component naming. These are real signals even without a dashboard.

**Qualify what you know**
"The implementation team read the change as roughly half the time on standard setup — that was their read, not a measured figure." This is more credible than false precision and more useful than silence.

**Follow-on work as signal**
When your project creates demand for the next project, that's an operational outcome. The Modeling Syntax work unlocked the editor suggestions project. That's a business signal: the product became good enough in that area that the team could invest in making it better, rather than firefighting.

**Frame the counterfactual**
"Without this work, five squads would be building conflicting implementations indefinitely. The DS wasn't just about the current components — it was about the cost of not having it compound over time."

**What to avoid**
Don't claim metrics you didn't actually track. Interviewers can probe on measurement methodology and will notice immediately when a number doesn't hold up. Own the absence directly: "We tracked adoption, but that data is no longer with me. What I can speak to is what changed in how the team worked."

---

## B2B SaaS-specific vocabulary

**ARR per seat / per user**
B2B pricing often ties to number of seats (individual licenses) or usage tiers. Relevant when discussing feature scope: a power feature that works for 10% of seats may still justify engineering investment if those seats are enterprise accounts.

**Expansion revenue**
Revenue from existing customers upgrading their plan or buying more seats. For product designers, expansion is often connected to feature discovery: do users know what's available at higher tiers?

**ICP (Ideal Customer Profile)**
The specific type of company or user the product is built for. Relevant when you're discussing who you designed for and why. A feature useful to an ICP account gets prioritized over one useful to an edge-case segment.

**Enterprise vs SMB**
Enterprise accounts (large companies) often have different needs from small/medium businesses. Enterprise typically needs admin controls, role-based access, audit logs, and SSO. SMB needs simpler onboarding and self-serve. B2B products that serve both often have genuinely split design problems.

**PLG (Product-Led Growth)**
A growth strategy where the product itself drives acquisition, activation, and expansion — rather than sales. Freemium models and self-serve trials are typical PLG patterns. Relevant to you: PLG products put higher design weight on first-run experience, because there's no sales rep helping the user.

**SLG (Sales-Led Growth)**
The traditional B2B model: a sales team closes deals, then hands the account to customer success. Design is less visible in acquisition but critical in retention and expansion. The product needs to perform without the sales rep in the room.

**Time to close**
How long it takes to convert a prospect into a paying customer. Complex products with confusing demos have longer sales cycles. A product design that makes the core value obvious in a demo reduces time to close — this is how design affects revenue even before a user signs up.
