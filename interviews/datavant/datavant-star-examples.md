# Datavant: STAR example bank

Use alongside the [hiring-manager practice script](datavant-hiring-manager.md).

The employer asks for 5 to 10 specific examples. These nine cards cover different projects and decisions. Several come from Abacum, so choose the one that best answers the question. Each card covers the situation, your responsibility, your actions, and the result.

**Evidence labels:** Confirmed means supported by the current evidence register or recorded user confirmations. Recollection is an attributed account without recoverable measurement. Historical notes provide supporting detail and may need your confirmation before a precise spoken claim. Unknown details stay open.

## How to use each story

- **Situation:** Give only enough context to understand the problem.
- **Task:** State the specific goal or decision you were responsible for.
- **Action:** Spend most of the answer here. Use “I” for your research, recommendation, design, or recovery work. Use “we” when Product, Engineering, or leadership genuinely made or delivered the decision together.
- **Result:** State what shipped, changed, or was learned. Distinguish measured outcomes from feedback, team recollection, and your interpretation.

Choose one specific episode. A mixed result is still useful when you own your part and explain what you changed. Keep the first answer short and leave room for follow-up questions.

## Quick selection

| Prompt family | Card | Evidence status |
| --- | --- | --- |
| Research changed the design and complex self-service | 1. Dataset Manager | Ready. Attribute the outcome to team recollection. |
| Product judgment and technical collaboration | 2. Modeling language | Ready. The syntax example is confirmed. |
| Influence, Engineering pushback, and investment | 3. Abax Maker Days | Ready. Ownership was shared. |
| Adoption, gradual delivery, and system stewardship | 4. Abax migration | Supported. Adoption was incomplete. |
| AI trust, unclear scope, and learning after launch | 5. Remuner AI agent | Supported. There is no measured impact or guaranteed correctness. |
| Mistake, accountability, and a process change | 6. Remuner token incident | Ready. The recovery and safeguard are confirmed. |
| Prioritisation with limited capacity | 7. Remuner audit | General pattern. It needs one specific episode. |
| User friction and practical tradeoffs | 8. Deprecated components | Ready. The decision was specific and the fix shipped. |
| Connecting separate tools into one flow | 9. Dataset Manager and Dimensions | Ready. The flow shipped and feedback was qualitative. |

## Mapping the linked STAR prompts to your examples

| Prompt from the linked guide | Best available example |
| --- | --- |
| Persuasion, presentation, initiative, or taking the lead | Abax Maker Days: co-led the business case and proposed a bounded production test. |
| Good judgment, fact-finding, or solving the wrong initial problem | Dataset Manager: testing showed that the users understood the data logic, while SQL was the blocker. |
| Setting and pursuing a goal | Dataset Manager: increase autonomy for standard configurations and reduce implementation dependence. |
| Too many priorities | Abax roadmap: prioritise missing production components and variants over further token refinement. |
| Conflict, an unpopular direction, or supporting a decision you challenged | Remuner manager view: challenged the full redesign. Then kept the main research findings in it and analysed the mixed feedback. |
| Stress, failure, or a missed dependency | Remuner token incident: restore production, add the required-file check, and change the removal process. |
| An important written document | Abacum Script: document syntax rules so new functions follow a consistent structure. |
| Anticipating problems or creating preventive measures | Abax governance and contribution rules. Use only as a general operating example unless a specific incident is requested. |

## 1. Dataset Manager: research changed the direction

**Use for:** “Tell me about research that changed your design”; a complex workflow; reducing dependence on specialists.

- **Situation:** Finance users depended on the implementation team and JSON to configure datasets. A simpler interface did not solve the gap between the product's language and the way users understood their data.
- **Responsibility:** You led design and customer testing. Your earlier rehearsal account describes taking the research finding to the PM and lead engineer.
- **Action and rationale:** You showed that the product language was the problem. The team chose guided configuration and familiar modeling functions instead of exposing SQL to users.
- **Result:** The guided product shipped. Customers reached a working configuration in their first session. The implementation team believed standard configuration took roughly half the previous time. This was not measured through analytics.

**Ownership/evidence:** Your design and testing work is confirmed. The decision and delivery were shared with Product and Engineering. The outcome comes from team recollection.

**For follow-up:** Explain that users could express the transformation in Excel but not in SQL. Do not quote participants or give a test count.

**Follow-up:** What did the team choose not to build, and what did that choice make harder?

## 2. Modeling language: make the language consistent

**Use for:** Product judgment, technical collaboration, research beyond a single screen, cross-squad work.

- **Situation:** Abacum's modeling layer used several formula patterns. Users had to learn a different structure for each function.
- **Responsibility:** You led research and design, using customer-call evidence and competitor benchmarking. You worked with the Head of Design and partnered with Engineering on syntax decisions.
- **Action and rationale:** You proposed extending and standardising the existing language. You used customer evidence to explain the problem and worked with Engineering on the syntax.
- **Result:** The consistent language later supported suggestions in the formula editor. Faster writing and fewer support questions are qualitative feedback, not measured results.

**Ownership/evidence:** Your research and design work is confirmed. Syntax decisions were shared with Engineering. The outcomes are qualitative.

**For follow-up:** `SUM(amount) FROM Transactional WHERE accounts_level_2 IS "Workforce"` became `SUM(Transactional.amount, accounts_level_2 = "Workforce")`. The parameters moved inside the function and the dataset became an explicit input.

**Follow-up:** What was the cost of retaining the existing language?

## 3. Abax Maker Days: win time for a small test

**Use for:** Engineering pushback, influence without authority, making an investment case, capacity tradeoffs.

- **Situation:** Engineering was concerned that the design system would compete with squad priorities and never reach production.
- **Responsibility:** You co-led the business case with the Head of Design and owned parts of the token/library work. Engineering built the original pipeline.
- **Action and rationale:** You showed examples of product inconsistencies and compared two staffing options. The team chose one focused Maker Days week, with more people stepping away from squad work for less time.
- **Result:** The token setup and first Button reached production during the week. This proved the path from design to code. It did not prove a return on investment or measured time savings.

**Ownership/evidence:** You co-led the business case with the Head of Design. Engineering built the original pipeline. Archived notes confirm the staffing options and shipped work.

**For follow-up:** Explain your own contribution and how the team chose the focused week. Avoid quoting headcounts unless needed.

**Follow-up:** Why was taking more people away from delivery worth it at that point?

## 4. Abax migration: adoption across squad backlogs

**Use for:** Gradual delivery, adoption, governance, balancing consistency and local ownership.

- **Situation:** Five squads already used MUI. Replacing it would have required broad product work. Shared components still had to fit into each squad's delivery plan.
- **Responsibility:** You worked on shared patterns and governance, including the library review and migration approach. Squads retained ownership of their backlogs; Engineering owned implementation.
- **Action and rationale:** The team kept MUI underneath Abax, released new form elements behind flags, and let squads schedule the migration. Weekly reviews exposed missing states and variants.
- **Result:** When you left, two squads had completed the form migration and a third was in progress. A reconstructed codebase count put Abax at about 47% of tracked Abax and MUI component uses. Adoption was incomplete.

**Ownership/evidence:** Archived notes support the governance details. The migration state is your recollection. The 47% figure was reconstructed, and the raw exports are unavailable. It is not a percentage of screens, users, or squads.

**For follow-up:** Be ready to explain one missing variant or edge case. Do not invent an escalation when a squad delayed migration.

**Follow-up:** What did you gain and lose by leaving migration in squad backlogs?

## 5. Remuner AI agent: useful answers with clear limits

**Use for:** AI product judgment, trust, shared scoping, iteration after launch.

- **Situation:** Sales reps and managers needed answers about commissions and plans. Correct interpretation mattered because the information concerned their pay.
- **Responsibility:** As sole designer, you owned the interface, conversation design, answer formats, and trust patterns. Scope decisions were shared with the founders and Engineering. There was no PM on the project.
- **Action and rationale:** You defined supported questions and refusals. You designed direct answers with context, using tables or lists when useful. After launch, you improved the tone, terminology, and presentation.
- **Result:** The agent launched to all customers before March 2026. Feedback was mixed, and the team kept improving it. There are no reliable adoption, accuracy, or business metrics.

**Ownership/evidence:** Your design ownership is confirmed. Product scope was agreed with the founders and Engineering. Engineering owned the technical implementation.

**For follow-up:** The agent could return wrong numbers when customer-specific calculation code was outside its view. The recorded fix is unclear. Data freshness appeared elsewhere in the app, not in the chat. Do not claim these issues were solved. Engineering owned the multi-agent architecture.

**Follow-up:** How did you distinguish a useful response from a correct response? No complaint or follow-up was only a weak operational signal, not ground truth.

## 6. Remuner token file: own a production mistake

**Use for:** Failure, accountability, recovery, learning that changed working practice.

- **Situation:** You thought a token file was duplicated and deleted it. The app still depended on it, and the next deployment caused a short outage.
- **Responsibility:** Own the mistaken assumption and deletion. Do not shift blame to the deployment or the engineer.
- **Action and rationale:** You restored the file and pushed a fix. For several days, you checked every required file before deployment. The team then added a required-file check until the frontend dependency could be removed. Automation is not confirmed.
- **Result:** The outage was fixed and the process changed. The exact duration, impact, and recurrence were not measured.

**Ownership/evidence:** You confirmed the mistake, recovery, and safeguard sequence on 2026-09-30.

**For follow-up:** The check verified that required files were present. Do not claim more implementation detail or connect separate hardening work to this incident.

**Follow-up:** What would you check before making the same kind of change now?

## 7. Remuner audit: decide what to fix and what to defer

**Use for:** Limited capacity, ongoing maintenance, prioritisation alongside product work.

- **Situation:** Patterns differed between the designs and the product while feature work continued. The inconsistency was a shared problem.
- **Responsibility:** As sole designer, you ran an ongoing screen/pattern audit and built the component library alongside product work.
- **Action and rationale:** You gathered examples, defined the variants and behaviours, created tickets, and discussed them with frontend engineers. You fixed urgent problems and delayed work that an upcoming feature would change.
- **Result:** The library and product improved together. The CTO noticed the change across the product, but there is no measured time saving or result from one specific delay decision.

**Ownership/evidence:** Library ownership is confirmed. Audit and meeting details are recorded user recollection in the design-system notes.

**Gap:** This is a working pattern, not one complete incident. Use it for a general prioritisation question, not for “Tell me about a time.”

**Follow-up:** When was leaving an inconsistency temporarily the better product decision?

## 8. Abax deprecated components: a smaller workable fix

**Use for:** Responding to user friction, practical design-system decisions, comparing options.

- **Situation:** Deprecated components still appeared in Figma search, so designers could select the wrong version during migration.
- **Responsibility:** You diagnosed the problem and proposed three approaches with tradeoffs.
- **Action and rationale:** You marked the old component as deprecated and published the replacement under the clean name. You kept the old version during the transition and later unpublished it. This avoided a heavier remove and republish process.
- **Result:** The fix shipped and the old component was later unpublished. The team did not measure incorrect selection or saved time.

**Ownership/evidence:** Archived design system notes confirm your diagnosis, proposal, and the final decision.

**For follow-up:** Explain the chosen option and the heavier alternative. The records do not preserve the third option, so leave it out.

**Follow-up:** Why did you keep the obsolete component available during the transition?

## 9. Dataset Manager and Dimensions: integrate around the user's task

**Use for:** Connecting separate tools, workflow design, customer feedback, reducing context switching.

- **Situation:** Users could assign dimensions to dataset columns. If a dimension did not exist, they had to leave the dataset, create it elsewhere, return, and resume. Customers said this added time, errors, and confusion.
- **Responsibility:** You identified the workflow problem and owned the proposed solution.
- **Action and rationale:** You proposed basic dimension creation and editing inside the open dataset. Product and Engineering agreed to build it.
- **Result:** The flow shipped. Customers reported faster configuration, fewer errors, and less confusion. Advanced management stayed in the separate area and was expanded in a later project. Dimensions then supported aggregation and data work in modeling.

**Ownership/evidence:** You identified the problem and proposed the solution. Product and Engineering agreed on it and shared delivery. The outcome comes from customer feedback, not measured data.

**Follow-up:** Why did the first version stop at basic creation and editing?

## Known gaps

1. A concrete Remuner fix-versus-defer episode for card 7.
2. A real disagreement with a PM, if asked specifically. Engineering capacity pushback does not establish a PM conflict. The Remuner AI project had no PM.
3. Any details Aideen shared about the team, current problems, and expectations.

Do not add anecdotes, quotes, or metrics simply to reach ten cards.

## Evidence sources

- Current authority: [experience facts](../../evidence/experience-facts.md), [Datavant record](../../applications/records/datavant-senior-ux-designer-provider-experience.md), [Spendesk preparation](../spendesk/spendesk-hiring-manager.md), and [supporting questions](../spendesk/spendesk-hiring-manager-questions.md). The current register supersedes older conflicting phrasing.
- Read-only historical detail reviewed 2026-09-25: `context/portfolio.md` (Dataset Manager, Modeling Syntax, AI Agent); `context/design-systems-notes.md` (Maker Days, governance, deprecation, Remuner audit); `context/ai-agent-notes.md` (ownership, format selection, trust limits and corrections).
- Earlier Dataset Manager rehearsal, 2026-09-23 to 2026-09-25: Manel's recorded account of the initial UI hypothesis, research finding, PM/lead-engineer discussion, and familiar modeling functions. This adds personal recall, not independent measurement.
- Employer interview guide supplied 2026-09-25 establishes the request for 5-10 examples and behavioral/situational preparation; it does not prescribe these particular stories.
