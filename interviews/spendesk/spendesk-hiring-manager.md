# Spendesk - Hiring Manager interview

**Role:** Confirmed Product Designer  
**Date:** 2026-09-17, 11:30-12:15 CEST  
**Interviewer:** Cyrièle Piancastelli, Head of Product Design  
**Format:** The email says background, experience, and fit. The role page calls this stage a portfolio presentation and Hiring Manager discussion. The meeting is 45 minutes. Aim for an 11-13 minute case and leave room for discussion. Spendesk has not confirmed a presentation time limit.

**Deck:** [Abacum DS](https://www.figma.com/slides/ae1SMrxEXfMMdUygkGTMcH/Abacum-DS). Eleven slides are in the main presentation, including the final hypothetical LLM slide. Two detailed slides remain skipped as backup.

## What Spendesk is most likely testing

1. Can Manel own a complex product problem from definition through delivery and iteration?
2. Has he built a design system as operating infrastructure: patterns, documentation, contribution, governance, and adoption, not only components?
3. Can he make evidence-based decisions with Product and Engineering in financial, data-heavy, and increasingly automated workflows?

## Common opening questions

Use these as speaking notes. Keep the opening answer under 90 seconds, then let Cyrièle choose where to go deeper. The first-person wording is a draft in Manel's voice, not a script to memorise.

### Tell me about yourself. Who is Manel?

"I'm a product designer based in Barcelona. I spent 11 years co-running a UX studio, then moved into B2B product teams. At Abacum I worked on finance configuration and modeling, and helped build a design system used by five squads. More recently, I was the sole designer at Remuner. I worked across the product, including an AI agent for questions about sales compensation. I like work where the hard part is understanding how a product works and making it usable. The mix of financial workflows and design-system work here caught my attention."

### Walk me through your background

Start with the studio, then spend most of the answer on the last four years.

- **Kings of Mambo, 2010-2021:** Co-founded a UX studio. Worked from research and information architecture through delivery, often with front-end implementation. The studio exposed Manel to several industries and gave him direct responsibility for clients and projects.
- **Abacum, 2022-2024:** Senior Product Designer, first in integrations and then in the engine squad. Led design and customer testing for Dataset Manager, worked on modeling syntax, and co-led the Abax business case with the Head of Design.
- **Remuner, 2024-2026:** Senior Product Designer and sole designer. Worked across the product, built the design system, and designed a production AI agent for sales-compensation questions.

Close with the common thread: complex B2B products, decisions that cross screens and teams, and close work with Engineering. Do not spend equal time on all 15 years.

### Why did you move from running a studio into product teams?

The career change is confirmed. The personal reason is not recorded as a confirmed fact. Give your real reason. A possible framing, **only if it is true**, is: "The studio gave me breadth and ownership. I wanted to stay with one product longer, see what happened after launch, and work through the deeper problems that appear as a product grows."

### Why Spendesk?

"The product problems are close to the work I enjoy. Finance teams have to manage complicated information and rules, while other employees need a simple way to act. I've worked on financial configuration at Abacum and compensation workflows at Remuner. This role also includes design-system adoption across a larger product, which is work I've done at both companies. I'd like to understand which product area needs the most help now."

Spendesk's role description also mentions AI-powered workflows. If Cyrièle takes the conversation there, connect it to the Remuner agent's answer boundaries and trust decisions. Do not lead with the hypothetical LLM slide.

### Why this role rather than a design-system-only role?

"I want to stay close to product problems. At Abacum, the design-system work mattered because squads were building related workflows in different ways. At Remuner, I owned product design and the system at the same time. I enjoy doing both, as long as there is a clear product area to own and enough time to keep the shared work healthy."

### Why are you looking now? Why did you leave Remuner?

**Needs Manel's wording.** The records confirm the role ended in March 2026 but do not establish the departure reason. Answer that part plainly and truthfully in one sentence. Then explain what you want next: a hands-on product role with complex workflows, a design team to work with, and scope to improve shared patterns. Do not substitute this preference for the actual reason you left.

### What are you looking for in your next role?

"I'd like to own a product problem from understanding it through to release and iteration. I work well with Engineering and Product when the workflow has real complexity. I also want design-system work to have a clear purpose and a way for teams to adopt it. I prefer the senior individual-contributor path to people management."

### Why apply for a Confirmed role with your experience?

"The work described here interested me before the level did. It combines a product area, complex financial workflows, and design-system work. I want to understand how much ownership the person in this role has and how you distinguish Confirmed from Lead. If the scope fits, I'm open to discussing the level with you."

Do not say the title does not matter if the role would actually be too narrow. Ask Cyrièle about autonomy, expected impact, and how the two levels differ.

## Common product and collaboration questions

### How do you approach a new problem?

Use Dataset Manager. Manel first had to understand how finance teams configured datasets and where JSON-based setup blocked them. Customer testing exposed a mismatch between the product's data-type language and the terms finance users used. The design introduced a guided UI layer and used the existing modeling language where it helped. Explain the decision that changed after testing, then what shipped. Avoid a generic list of design-process stages.

### Tell me about user research that changed your design

Use the language mismatch in Dataset Manager. Say what users struggled to understand, why that mattered for configuration, and how the interface changed. The available record confirms customer testing and the decision to extend modeling syntax rather than introduce SQL. Do not invent a quote, a sample size, or a measured conversion result.

### Tell me about a complex project you owned end to end

Use Dataset Manager as the product case. Cover the original JSON-based configuration, finance users' mental model, the guided UI decision, testing, delivery, and the implementation team's later read of the outcome. That team believed standard configuration took roughly half as long. This is a recollection, not instrumented timing data, so attribute it to them.

### How do you work with Product and Engineering?

Give one decision rather than a general claim. At Abacum, the MUI decision kept an existing framework in place while Abax added shared patterns. Engineering built the original token pipeline. At Remuner there was no PM, so Manel shared AI-agent capability decisions with the founders and Engineering. Be clear which setting the example comes from.

### Tell me about pushback or a disagreement

Two grounded options: Engineering's concern that Abax would compete with squad work, or the debate about a read-only component state. For the first, explain the two staffing plans and the bounded Maker Days test. For the second, designers and engineers compared mental models and reused an existing framework state rather than adding a new one. State the other side's concern fairly.

### How do you choose between speed and system quality?

Abax kept MUI as its base because replacing working components across five squads would have delayed product work. New form elements went out behind flags, and squads scheduled migration in their own backlogs. The decision was to improve consistency in steps without demanding a full rewrite. Mention the cost of this choice too: migration remained incomplete when Manel left.

### How do you know whether design-system work is helping?

For Abax, the team aimed for Abax to account for 80% of tracked Abax and MUI component uses across the codebase. Frontend engineers ran custom scripts monthly to count those uses. Weekly reviews exposed missing variants. At departure, the reconstructed Abax share was about 47%, with no recoverable raw export. The team was still improving the metric. Designer feedback and named tokens in code were useful signals. Time saved and customer impact were not measured.

### Tell me about AI work you have shipped

At Remuner, Manel designed and shipped a production agent that answered sales-compensation questions for sales reps and managers. He owned the UX, conversation design, answer formats, and trust patterns. Capability decisions were shared with the founders and Engineering. The agent read platform calculations; it did not calculate commissions itself. There are no claimable adoption or accuracy metrics.

### What would you do differently on Abax?

"I'd keep a more durable record of adoption and decision evidence. We did set goals and count component use, but I no longer have the raw exports behind the departure figure. I would also make the criteria for moving from token work to production components easier to see, so the next team could understand why priorities changed."

Do not imply there was no roadmap or no measurement. The gap is preserving evidence and making the decision logic legible later.

### What are your strengths, and where are you still improving?

For a strength, use a concrete pattern: spotting work repeated across teams, then helping people agree on a shared approach that reaches production. Abax is the example. For improvement, use evidence discipline: keep decision and adoption records in a form that survives a job change. Avoid a rehearsed weakness that sounds like a disguised strength.

### Why should we hire you?

"This role needs someone who can design a product workflow and help teams use shared patterns in the product. I've done both in a financial B2B setting. At Abacum I worked on configuration for finance users and on Abax across five squads. At Remuner I owned product design as the sole designer and shipped an AI agent. I can bring that experience while staying close to the actual work in a squad."

### What motivates you in design work?

Keep this personal. A grounded answer is the point where a complex product starts making sense to its users and the team can maintain that clarity as it grows. Dataset Manager shows the first part; Abax shows the second. Add a real moment that matters to you rather than repeating the job description.

### Tell me about a mistake or failure

The Remuner token incident is a direct answer. Manel deleted a token file he thought was a duplicate. The app depended on it, and the next deployment caused a short production outage. He recovered the file and pushed a fix. Afterward, he introduced a check before token-repository deployments. The team then moved the dependency so the file could be removed safely. Own the outage plainly. The learning was that a token repository feeding production needs the same care as other production code.

### How do you handle competing priorities?

Use the shift after the first Abax Button shipped. More token refinement had diminishing value while teams still lacked components and variants they could use. The team put production components first, then used weekly reviews and codebase counts to check the gaps. Give the specific tradeoff, who agreed to it, and what was deferred. Do not claim a formal scoring framework that the records do not show.

### How do you respond to feedback?

One Abacum designer reported that she could build a screen quickly with the available variants. She also pointed out gaps in other components. Manel captured those gaps and worked on them through the library review. The useful point is the feedback loop, not a claim that the whole team became faster.

### What would you do in your first months here?

"I'd first understand the product area, its users, and the work already underway. I'd also look at how the design system reaches squads today: where components are missing, where contribution is unclear, and what Engineering has to maintain. Then I'd agree with the PM and engineers on a small number of problems to tackle first. I would not prescribe a design-system roadmap before seeing the actual constraints."

### Do you want to manage people?

"I prefer the senior individual-contributor path. I like being hands-on with product problems, mentoring through the work, and helping teams make decisions together. I'm open to broad influence without direct reports."

### What salary are you looking for?

No Spendesk-specific figure from the recruiter screen is recorded here. Do not invent a number from this document. Use the figure you actually discussed with Talent Acquisition, if any, and keep it consistent. If none was discussed, clarify the role's range before committing to a precise figure.

## Lead case

**Abacum design system (Abax).** This is the strongest match to a mandatory requirement in the role. It demonstrates cross-squad influence, an engineering-facing business case, deliberate reuse of MUI, token and code infrastructure, governance, contribution, and tracked but incomplete adoption across five squads.

Present it through the decisions:

- The product and engineering cost of fragmented patterns across five squads.
- How Manel and the Head of Design built the case and won sanctioned Maker Days investment.
- The staffing choice: two frontend engineers and one designer over two weeks alongside sprints, or at least four frontend engineers and two designers for one dedicated Maker Days week. The team used the latter. This was a concentrated use of capacity, with a bounded production test.
- The scope decision to keep MUI and build a two-tier token and contribution model around it.
- The roadmap decision to move from token infrastructure to usable production components and form variants once the Button proved the path.
- How governance and migration worked across squads.
- Honest outcome: Abax accounted for about 47% of tracked Abax and MUI component uses across the codebase at departure; two squads completed form migration and a third was mid-migration. The percentage is reconstructed, not a live analytics export.
- The final LLM slide is a hypothetical approach today. The later Remuner token-repository work is the real example of AI-assisted code work with engineering review.

## Slide order and rehearsal timing

The current notes contain about 887 words. Reading them alone would take roughly 6-7 minutes. Use the actual artifacts and one concrete decision example to reach an 11-13 minute discussion. Do not slow down or add unsupported impact claims to fill time.

| Slides | Point to make | Rehearsal budget |
| --- | --- | --- |
| 1-2 | Five squads had repeated interface problems. | 1:15 |
| 3-4 | The business case and the two staffing options. Explain the capacity tradeoff. | 3:00 |
| 5 | The Button proved the Figma-to-code path. | 1:15 |
| 6-7 | How the team set priorities and why it kept MUI. Use the Notion artifact. | 2:15 |
| 8 | Squad-owned migration and the weekly review. | 1:45 |
| 9 | The result, the 80% goal, and the limits of the 47% figure. | 1:15 |
| 10 | What Manel would do with LLMs today. Keep the hypothetical boundary clear. | 0:45 |

This budget totals about 11:30. Run one full rehearsal aloud. If it exceeds 13 minutes, shorten the architecture explanation on slide 7 before cutting the investment or adoption decisions.

## Where Cyrièle may press

- **Investment:** The screenshots showed repeated defects, but the deck does not quantify their cost. Explain the competing capacity options and the reason for a bounded test. Do not claim a calculated ROI.
- **Ownership:** Manel co-led the business case with the Head of Design and worked on design-side architecture and governance. An engineer built the original pipeline. State who made each decision if asked.
- **Prioritisation:** The decisive change was putting missing components and form variants ahead of further token refinement. Use one specific example from the weekly reviews, such as the read-only state debate or a missing form variant.
- **Measurement:** The 80% figure was a documented goal. The surviving notes do not explain why the team chose that exact threshold. Frontend scripts counted Abax and MUI component uses across the codebase monthly. The roughly 47% departure figure is reconstructed and its raw exports are unavailable. Do not invent a trend.
- **Product-design breadth:** The Abax case does not show customer research or a user-facing financial workflow. Spendesk asks for both. Have a two-minute Dataset Manager account ready: the user problem, evidence, design decision, test, and shipped result.
- **LLMs:** Slide 10 describes a present-day approach, not work done on Abax. Anchor it to the later Remuner token-repository work only if Cyrièle asks for proof of code contribution.

**Supporting stories if Cyrièle redirects:**

- Complex product and research: Dataset Manager.
- AI, trust, and capability boundaries: Remuner AI agent.
- Judgment without a mandate: Modeling Syntax.
- Smaller-company design-system execution and failure learning: Remuner design system and token-pipeline incident.

## Likely questions mapped to evidence

| Question | Best evidence |
|---|---|
| Tell me about a complex problem you owned end to end. | Dataset Manager |
| How did you get teams to adopt a design system? | Abax governance, feature flags, squad migration work, weekly library sync |
| What did you personally own versus Engineering or design leadership? | Abax: co-led business case; engineer built original pipeline. Remuner: Manel chose the foundation and later hardened it with AI assistance; engineers adapted, reviewed, and merged |
| How do you balance system quality and delivery speed? | Kept MUI; incremental migration; fix-now versus defer decisions |
| Tell me about a decision that changed after research. | Dataset Manager language mismatch and rejection of SQL |
| How do you design trustworthy AI workflows? | Remuner agent capability limits, structured answer formats, refusals, and customer-specific terminology |
| Tell me about a failure. | Remuner token-file deletion caused a short production outage; recovery and structural safeguards followed |
| Why Spendesk? | Direct overlap: complex financial workflows, system infrastructure, product-engineering partnership, and responsible automation |
| Why a Confirmed role given your experience? | Scope matters more than title, but clarify how Spendesk distinguishes Confirmed from Lead and whether ownership is genuinely senior enough |

## Claims to handle carefully

- The AI agent had one global chat surface. The submitted CV says "contextual in-app answers"; if asked, clarify that answers were contextual and structured inside that chat, not separate embedded AI surfaces.
- No PM was assigned to the AI-agent project. Capability scope was shared among Manel, the founders, and Engineering.
- The agent did not calculate commissions itself; it read platform calculations.
- There are no claimable adoption, accuracy, satisfaction, or revenue metrics for the agent.
- Do not present Abax adoption figures as instrumented analytics.
- Manel built two design systems, but did not solely implement the original token pipeline at either company.

## Questions to ask Cyrièle

1. "The role puts unusual emphasis on contribution, governance, and adoption. Where is the design system today, and what is preventing it from scaling the way you want?"
2. "Which product area would this designer likely own, and what is the hardest unresolved workflow in that area?"
3. "How do you distinguish the Confirmed and Lead levels in ownership, autonomy, and expected impact?"

If there is time: "What would make someone in this role exceptional rather than simply good after twelve months?"

## Open gaps before the interview

- **[NEEDS YOUR INPUT]** What is your real reason for leaving Remuner? The record confirms when the role ended, not why.
- **[NEEDS YOUR INPUT]** What made you move from studio work into an in-house product role? The suggested framing above needs your confirmation.
- **[NEEDS YOUR INPUT]** What compensation figure, if any, was stated in the recruiter screen? No Spendesk-specific salary position is recorded.
- **[NEEDS YOUR INPUT]** Did Clement share a squad, product area, hiring reason, team structure, or concern from the recruiter round?
- **[NEEDS YOUR INPUT]** Why did the team choose the exact 80% adoption target? The source notes record the target, not its rationale.
- **[NEEDS YOUR INPUT]** How did the frontend scripts count a component use: imports, rendered instances, or another unit? Manel confirmed that 47% used the whole-codebase Abax-versus-MUI count, but the raw exports are unavailable.

## Final preparation

- Rehearse the 11-slide Abax walk-through aloud. Aim for 11-13 minutes and stop by 13 unless Cyrièle asks to go deeper.
- Rehearse ownership boundaries and reconstructed outcomes exactly.
- Keep Dataset Manager and AI agent ready as two-minute supporting stories.
- Ask Clement for the missing candidate guide only if the format or required preparation remains unclear; the public process already confirms a portfolio presentation.
- After the interview, capture what Cyrièle emphasized, objections, questions, and next steps in the application record.
