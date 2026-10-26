# Enginy: Senior Product Designer

Record: `applications/records/enginy-product-designer.md`. CV source: `cv/roles/enginy-product-designer.md`. Cover letter: `cover-letters/roles/enginy-product-designer.md` (what they were told: Remuner sole designer, AI agent, Codex token pipeline via reviewed PRs, CMS front ends, Dataset Manager).

## Round 1: Recruiter screen

- **When:** Mon 26 Oct 2026, 11:30-12:00 Madrid. Google Meet meet.google.com/njk-uojp-rkf.
- **Interviewer:** Saul Villa, Manager, Talent Acquisition at Enginy (since Feb 2026; about four years recruiting at N26 before that).
- **Purpose of this round:** filter. Saul checks the must-haves a recruiter can tick: level, maker bar, English, on-site, money, availability. Short answers, one proof each, then stop. He asked for full-hour slots but booked 30 minutes, so expect a fast pace.

### What Enginy most likely cares about

1. **Maker bar, taken literally.** Diogo Rendeiro's post ("push PRs, not pixels", "Shipped a PR last week? DM me") and Damián Rodrígues's deck (about 90% of his designs go to production through his own PRs in Cursor or Claude Code; components built first in Storybook). Saul reposted Diogo, so he will screen for it.
2. **End-to-end ownership with a metric.** Damián's process starts from a Linear issue, sets a target metric before designing and measures it in Datadog. "Moved means done."
3. **Practical fit:** on-site Barcelona ("Onsite in sunny Barcelona"; 48 WFH days a year), Senior level, salary.

### Scripted answers

Drafted 2026-10-26 before the screen. Spoken versions; say them, don't read them. Backup if he asks about dense data workflows: Dataset Manager (`prep.md` Story A).

#### Q1. Walk me through your background

*about 60 seconds, then stop*

> I'm a senior product designer in Barcelona. Most of my career is complex B2B products.
>
> I co-founded a UX studio, Kings of Mambo, and ran it for eleven years. I designed there, and I also wrote the front end myself: HTML, CSS, JavaScript and PHP, on commerce sites like Kymco, whose checkout took real orders. I pushed my own code and deployed it.
>
> Then I joined Abacum, a finance planning platform. I started as the designer on data integrations, led Dataset Manager, which let finance teams set up their data without support, and ended up co-leading the design system across five product squads.
>
> Most recently I was the only designer at Remuner, a sales-compensation platform. I covered plans, approvals, the rep and manager views, and a conversational AI agent we shipped to every customer. I built the design system from scratch and opened PRs against the front end replacing hardcoded styles with tokens, which the front-end team reviewed and merged.
>
> So I'm used to designing for sales teams, working with AI features, and shipping my own changes. That's what drew me to Enginy.

Don't mention React/TypeScript here; the "Do you code" answer covers it if asked.

#### Q2. Why did you leave Remuner?

*`prep.md` "Priority zero", adjusted for Enginy; say it and stop*

> We parted ways in March. Product direction at Remuner came from the top, and design input didn't always carry weight in those calls. That model works for some startups, but it's not where I do my best work, and by early 2026 both sides could see the fit wasn't there. On the work itself: the design system shipped to production, and the CTO said, unprompted, that the product had gone from looking like a 2010 app to a 2020 app. I'm proud of what got built.

If he asks directly whether you left or were let go (answer honestly; don't call it mutual or your decision):

> It was their call. I'd already felt the fit wasn't right.

Then stop. Don't mention the timing or that you expected a conversation first; it reads as a grievance.

If he probes ("were there signs it wasn't working?"):

> Decisions moved faster than the research could inform them. I pushed back where I could, but when the call sits with founders, there's a limit to how much that changes.

Enginy change: "founder-driven" dropped, because Enginy's designers work directly with the founders. The problem named is design input having no weight, not founders being involved. Never: "fired", research being overridden, any executive by role or behaviour.

#### Q3. Why Enginy?

*`prep.md` Q11 framework: product problem, background match, why this role*

> On the product side, Enginy puts AI between a sales rep and the person they're writing to: the research, the reply drafts, the intent tags. The rep sends that under their own name, so the design problem is knowing when to trust it and when to check it. I worked on the same question at Remuner, where reps asked our AI agent about their own commissions.
>
> I also know the users. At Remuner I designed the rep and manager views for sales teams, so I know how they work and what they skip.
>
> On the designers work side. I saw Damián's post: designers take a feature from the Linear issue to their own PR, then check the metric. That's how I worked by the end at Remuner, and I want to do it on a team that expects it, instead of being the only one.

Manel confirmed on 2026-10-26 that he wants this role, on-site, in outbound-sales software.

#### Q4. Do you code? Have you shipped PRs?

*about 45 seconds*

> Yes. At the studio I wrote the front end myself for eleven years: HTML, CSS, JavaScript, PHP, WordPress. I made the commits and deployed my own work and test.
>
> At Remuner I worked in the repos with AI. I owned the tokens repository, and I used Codex to add CI, drift checks and smoke tests to the token pipeline. I also fixed hardcoded styles in the front-end app with Claude and sent them as PRs. The engineers reviewed and merged both.
>
> I'm not a front-end engineer. In React and TypeScript, AI writes most of the code and I direct it. From what I've seen, that's close to how your designers work in Cursor and Claude Code.

If he pushes on React: "I can build components with AI help; I wouldn't claim production React on my own." Don't say React for Remuner (its front end was Vue/Vuetify). Don't name a CI tool or deploy tool for the studio.

#### Q5. How do you use AI in your work?

*about 40 seconds; three concrete uses, no tool tour*

> Three ways. For prototypes: at Remuner I built working prototypes with AI that users could click through in tests, instead of static Figma flows.
>
> For design system work: I connected Figma to Codex, then Claude, through the Figma MCP. I used it to even out the colour palette and bring it to AA standard, generate component variants with the same props as the code, and produce the Storybook views and documentation.
>
> And in the code, as I said: the token pipeline and the front-end PRs. Day to day I work in Claude Code with MCP connections, much like your team does.

Prototypes were not connected to production and their tools aren't recorded: don't name a tool or call them shipped. If asked about designing AI products (not using AI), go to the Remuner agent: role-based context, refusing off-scope questions, structured answers.

#### Q6. Tell me about the impact of something you shipped

*about 60 seconds; problem, change, how you checked it, then the honest limit and one real number*

> At Remuner, reps told us their commission dashboard wasn't intuitive. That's too vague to design from, so I went back to the people who said it and interviewed them. Three different problems came out: some didn't understand how their plan was calculated, some couldn't see which metrics drove it, and some read the commission on screen as what they'd be paid this period, when payouts were quarterly.
>
> We added an explanation of the calculation with a link to the full plan, and a period selector that showed when the payout would land. We tested it with users and checked it resolved those three problems.
>
> Before, the metrics sat in a slideshow, so reps clicked through to find the one they needed. After the change, our analytics showed they got there in fewer clicks, and they opened the full plan view less, because the dashboard now answered the question they'd gone there for.

Evidence limits: the analytics changes are directional, seen in Remuner's internal dashboard; no percentages, time periods or tool name. If asked for numbers: "I saw the direction, not a figure I'd quote." Abax 47% is a reconstructed count: state it alone, never "against an 80% target" (it's in no answer now; use it only if asked for a number). Remuner AI agent has no adoption or accuracy data; if asked about its impact, say it shipped to every customer and stop there. Never claim you pushed code to move a metric.

#### Q7. Tell me about your design system experience

*about 50 seconds; Abax then Remuner, two or three sentences each*

> I've built two. At Abacum I co-led the design system, Abax, with the head of design. We made the business case to the product team, built it on top of MUI instead of from scratch so squads could move over gradually, and worked on tokens, components and governance across five squads. When I left, two squads had finished migrating their form elements and a third was partway through.
>
> At Remuner I built one from scratch as the only designer. I kept the token set small on purpose, because at Abacum I'd seen complexity turn into debt. I brought the token pipeline over, the engineers adapted it to their stack, and I owned the tokens repository from there.
>
> In both cases the point was to ship faster with fewer one-off fixes, which matches how your posting describes the system.

Don't repeat the AI pipeline and PR details if Q4 or Q5 already covered them; point back ("the PRs I mentioned"). Limits: co-led, never sole owner of Abax; the all-hands presentation sought buy-in, don't say it won it; no tool chain (Token Studio, Style Dictionary, ESLint) unless asked, and ESLint enforcement is recorded for Remuner, not Abax. `prep.md` Story B's "presented formally to engineering leadership" is not in the evidence register; don't use it.

#### Q8. Are you OK working on-site?

*about 15 seconds, then turn it into your question*

> Yes. I live in Barcelona, and I worked on-site five days a week for eleven years at the studio. Abacum and Remuner were hybrid. What does a normal week look like for the design team? The posting mentions 48 remote days a year.

On-site accepted 2026-10-19. Log his answer on cadence in the record. Don't negotiate remote days in this round.

#### Q9. How is your English?

> C1. I'm comfortable working in English day to day.

Spanish and Catalan native if asked.

#### Q10. When could you start?

> Straight away. I'm not in a role right now, so there's no notice period.

Same answer as Perk and RemoFirst. Don't add why or how soon you need it.

#### Q11. Are you in other processes?

> Yes, a few, some at interview stage. Enginy is one I'd prioritise.

Don't name companies or stages. If he asks about timelines: "Nothing is forcing a decision this week, but I'd rather keep this moving." Only say the second line if it's true on the day.

#### Q12. What are your salary expectations?

*ask the band first; never move off 62 by yourself*

> I put 62 on the form. What's the band for this role?

Then, depending on the band:

- **62 sits inside it:** "Good, that works. Is there equity or variable on top?" Stop.
- **Band tops out below 62:** "That can work depending on the full package. What else is in it: equity, benefits?" Don't name a lower figure; let them make the offer.
- **Band starts above 62:** "62 was a guess before I knew the scope. Where in the band would depend on the level, so I'd rather you place me." Don't confirm 62.
- **He won't share the band and asks you to confirm:** "62 is still my number, with some flexibility for the right package."
- **Previous salary:** "I'm not sharing previous compensation, but I'm targeting 62 for this role based on scope and the market."

Already stated: EUR 62,000 gross annual on the application form (2026-09-15); Enginy's range unknown. Saul came from N26, so expect a structured band. Never: previous salary, the private floor, any figure below 62, that you need income soon. Log the band, whether he asked, what you said and any feedback in the record (`context/salary.md` rule 5).

### [NEEDS YOUR STORY] gaps this round could hit

- **Disagreement with your manager (`prep.md` Q10):** no story in the library. Unlikely in a recruiter screen; if it comes up, use the "no SQL" call (Story A, `prep.md` Q3) instead of inventing one.
- **Story E (Kings of Mambo incidents):** not fleshed out. The missed-deadline story (`prep.md` Q2) is the only ready one.

### Questions to ask Saul

1. **Office:** "The posting says in-person with 48 remote days a year. What does a normal week look like for the design team?" (Skip if you already asked it in Q8.)
2. **Level and process:** "The posting title changed from Product Designer to Senior. How is the role levelled, and what are the next rounds? Who runs them?"
3. **Team:** "Who would I work with day to day? Is it a pod with a product engineer, and who leads the design team?" (Diogo is likely the hiring manager; inference, don't name him unless Saul does.)

#### More options (pick two or three)

Saul can answer these. Save questions about design craft for the hiring manager.

**The role**

4. "Why is the role open: is it a new seat or a replacement?"
5. "What would the first project be? Is there a product area already waiting for this person?"
6. "What separates someone who does well in this role after six months from someone who doesn't?"
7. "The posting mentions helping a junior designer grow. How much of the job is that?"

**The team**

8. "How big is the design team now, and how many designers are you hiring this year?"
9. "How are designers and product managers split? Does a designer lead a pod, or does a PM?"
10. "How much of the designers' work goes to production through their own PRs, versus handed to engineering?"

**The process**

11. "What does the build or design exercise look like, and how much time does it take?"
12. "What's the timeline to a decision? When would you expect to make an offer?"
13. "Is there anything in my profile you'd want me to address in the next round?"

**The company**

14. "How has the company grown this year, in people or customers?"
15. "Is Enginy hiring ahead of a funding round, or after one?"
16. "What's changed in the product since the AI features went in? Is that where most of the roadmap goes now?"

**The conditions**

17. "Is the contract permanent, and is there a probation period?"
18. "Is there equity for this role?"
19. "What's the policy on the 48 remote days: block them, or spread across the year?"

Q13 is the most useful single question for a recruiter screen: it surfaces his doubts while you can still answer them.

### After the call

Run `/debrief-interview enginy screen`. Log the range, what you stated, office cadence, level and the next rounds in the record.
