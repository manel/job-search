# Perk: Senior Design Systems Designer (Suitcase), November 2026

Record: `applications/records/perk-senior-design-systems-designer.md`. Applied 2026-10-21, referred by Tanna 2026-10-26, template rejection the same day, reversed by Clare's interview invite 2026-11-02. The July Staff Product Designer, Events process is a different, closed process; its unused brief is in `perk-events.md`.

---

## Suitcase: what is public (researched 2026-11-05)

External research. Little is public: there's no public Figma file, documentation site or token export.

- **What it is:** "our Design System, a collection of reusable components, guidelines, and standards. At Perk, we call ours Suitcase", "the shared language between designers and engineers", covering buttons, colour, typography and spacing rules. Source: Bea Silvia, "Working with designers, AI, or both?", builders.perk.com, 13 May 2026.
- **How designers work with it:** in mature product areas where "the design system is stable", some designers work directly in code; others start from AI prototypes. Design delivery can be a Figma file, a working prototype or code. AI is used to document guidelines ("Suitcase remains the source of truth, but AI helps us document and communicate it better"). One of the post's ideas for the future is "Figma-to-Suitcase pipelines". Same source.
- **2025 rebrand:** Wolff Olins did the brand, which went live on all digital platforms on 31 March 2025. A small team built "a new token-based design system" for it, covering typography, colour, spacing, corner radii and interaction states, with components rebuilt in Figma alongside developers. Source: Gary Brown (Senior UI & Design Systems Designer), gary-brown.com case page, undated, read 2026-11-05. The page doesn't use the name Suitcase. Perk's own rebrand post (builders.perk.com, "Rebranding TravelPerk") returned 403. Per the search summary only: they took the deadline as a chance to improve the Suitcase component library rather than just reskin it, and tokens define colour, spacing and typography so new themes (dark mode, high contrast) can come later by swapping tokens.
- **Web architecture:** an older Builders post on microfrontends reportedly says the migration would have been impossible without Suitcase. Source: search summary only; the page returned 403.
- **Mobile:** the Android design system was moved into Compose Multiplatform (CMP) and made "the source of truth for shared features"; colour, spacing and alignment mismatches between the apps "all gone". In hindsight they would "invest earlier in a CMP design system". Source: Luis G. Valle, "Compose Multiplatform at Perk", builders.perk.com, 2 Dec 2025. It doesn't say whether this is part of Suitcase or a separate mobile system.
- **The JD's ambition** (posting 2026-10-15, read via the Ashby API 2026-11-05): "a complete, consumer-grade, accessible and distributable system, so Perk feels like one consistent product on every surface... including AI agents and assistants". It sits alongside 25+ designers, an experimental and a core layer, content tokens, and component specs readable by AI prototyping tools.
- **Two postings, same text:** London `78dafbf1` (the one applied to) and a separate Barcelona req `3ec33996` (published 2026-10-21, hybrid), with identical text. Both open 2026-11-05.
- **Not Perk:** "Suitcase design system — from theory to practice" (Willy Fontenelle, Medium) is about Hurb's Suitcase. Ignore it.

**Use in the call:** folded into Round 1 below (the "Why Perk / why this role?" answer and the questions to ask). Use one public detail at most (the rebrand rebuild or the CMP move) as proof of interest; don't quote the blog posts at Clare as though they've been studied in depth. Ask which req this is (London or Barcelona) only if the location comes up as unclear.

---

## Round 1: TA Preliminary (brief written 2026-11-03)

**Date:** Thu 2026-11-05, 15:30-15:55 Madrid, Google Meet (https://meet.google.com/oue-gzhv-jni). 25 minutes, not the 15 in the first email.
**Interviewer:** Clare Watts, Senior Talent Acquisition Partner. Her stated agenda: background, motivation for the role, team and culture.
**Before the call:** confirmed. Reply sent and invite accepted 2026-11-02. In English.

### What Perk most likely cares about (this round)
- **A credible "why Suitcase" from someone they already rejected once.** The invite most likely came from the referral rule (Tanna, 2026-11-05: every referral gets at least a first interview), not from a strong CV read. Clare has to justify passing Manel on; give her a clear, checkable reason: Suitcase is past its foundations stage and into the stage Manel has done (production adoption tracking, migration across squads, contribution model). Full answer in the question map below.
- **Logistics knock-outs:** three days a week in the Barcelona office, English working level, availability (immediate), salary fit against the EUR 65,000 already on the form.
- **Seniority read without a DS title:** two production systems, one co-led across five squads, one built alone. TA will check that "Senior Product Designer" on the CV still means system ownership.

### Lead story
Design-systems mapping in `context/positioning.md`: **Story B (Abax) as lead, Story C (Remuner DS) as support.** Abax first because it carries the JD's rarest asks (adoption measured monthly, about 47% at departure; consolidation off MUI; contribution review). Remuner second for building alone and the AI/Figma MCP work. Keep both to headline level; a TA screen won't go into token tiers.

### Likely questions

Answers written to be said out loud, checked against `evidence/experience-facts.md`. Read them, then say them in your own words; only the Remuner answer is meant word for word.

#### Background

*Under two minutes. Source: opening intro in `prep.md`, weighted to design systems.*

> I'm a Senior Product Designer based in Barcelona. I co-founded a UX studio, Kings of Mambo, and ran it for eleven years. I did research, interaction and visual design there, and I wrote a lot of the front-end code for client sites myself.
>
> Then I joined Abacum, a financial planning platform. I started on data integrations and ended up co-leading our design system, Abax, with the head of design. It covered five product squads, and we were moving the product off MUI onto our own components.
>
> Most recently I was the only designer at Remuner, a sales compensation platform. I built the design system there from scratch, including the token pipeline, and I designed the product's AI agent.
>
> So most of my last few years has been design system work in production, and that's why this role caught my eye.

#### Why Perk, and why this role?

*The answer that matters most today. Q11 framework: structural hook, stage, alignment.*

> Mainly because Suitcase is run like infrastructure. The job description talks about a core layer and an experimental layer, about measuring adoption and Figma-to-code parity, and about content tokens. Most design system roles I see don't go that far.
>
> Also, from what I've read, there was a rebrand last year and they rebuilt the foundations on tokens. What this role describes is the next part: measuring, governance, keeping web, mobile and AI surfaces consistent. That's the part I've done. At Abacum we tracked adoption every month. When I left, Abax was about 47% of all the component uses we tracked, and the goal was 80%. We hadn't reached it yet; we were migrating squad by squad off MUI and reviewing contributions as they came in.
>
> There are smaller overlaps too. A post on your engineering blog mentions Figma-to-Suitcase pipelines as something you'd like to build. I built that kind of pipeline at Abacum, from Figma Variables through Token Studio to Style Dictionary. And at Remuner I put the translation keys inside the components, which is close to what you call content tokens.

#### Why did you leave Remuner?

*Priority zero in `prep.md`. Memorised version, word for word. Then stop.*

> We parted ways in March. The product direction came from the top, and design input didn't always have real weight in those calls. That's a legitimate model for a certain kind of startup, but it's not where I do my best work, and by early 2026 both sides could see the fit wasn't there. What I'd say about the work: the design system shipped to production, and the CTO described the product's before-and-after as going from a 2010 app to a 2020 app. That was unprompted. I'm proud of what got built.

If asked whether you left or were let go:

> It was their call. I'd already felt the fit wasn't right.

#### What have you been doing since March?

*Confirmed 2026-11-03. Freelance clients and scope aren't recorded; if she asks "what kind?", answer from memory in one line.*

> Two things. I've gone deeper into using Claude with the Figma MCP for design system work: keeping tokens in sync between code and Figma, catching drift, running accessibility checks. Your job description mentions MCP tooling, so that's been useful. And I've done some freelance work along the way.

#### How do you use AI day to day?

*Now a recruiter-screen question (`memory.md` 2026-10-26). Three uses.*

> Three ways, mostly. When I want to test an idea, I build an AI prototype that behaves like the real thing. A lot of my design system work goes through the Figma MCP: managing tokens, generating a Storybook view and documentation for each component, checking colour contrast. And I open my own pull requests for small front-end fixes, mostly styles and tokens, which the front-end team reviews before they merge.

#### What kind of team do you work best in?

*Q12 in `prep.md`.*

> One where engineers are involved from the start of a design, and where the PM understands the constraints and doesn't over-specify. I also need enough room to spot problems early, instead of only working through tickets. With a design system that matters even more, because the people I'm designing for are the designers and engineers sitting next to me.

#### You applied to the Events role in July

*Not in `prep.md`. Don't raise the 26 Oct rejection unless Clare does.*

> Yes, that was a Staff product role on Events, a different kind of job. This one is design system work, which is what I've been doing for the last few years, so it's a much more direct fit.

If she mentions the rejection:

> Thanks for taking a second look.

#### Do you have experience with Code Connect, accessibility or mobile?

*JD gaps, not story gaps. Say what's true, then stop.*

Code Connect (named in the JD: "Experience prototyping with AI tools and with Storybook, Code Connect and MCP tooling"):

> I haven't used Code Connect itself, though I know what it does: it maps Figma components to their code. The closest thing I've done is through the Figma MCP. I generated a Storybook view for each component, with a grid of the Figma props, so you could see every state and variant.

Accessibility (WCAG 2.2 AA with keyboard and screen readers in the JD):

> At Remuner I brought the colours we actually used up to WCAG AA contrast, and I designed focus and error states that don't rely on colour alone. In some cases I checked how screen readers read them. I haven't done full keyboard and screen-reader conformance work, and I'd want to do that properly here.

Mobile:

> My mobile work is the Remuner app: the web product adapted for mobile and shipped to both app stores as a webview app. I haven't designed with native iOS or Android components.

#### What are your salary expectations?

*Full rules in the salary reminder below.*

> I put 65,000 on the form. Is there a range for the Barcelona role?

If she presses:

> 65,000 base is where I am.

#### Are you in other processes?

*Checked 2026-11-05: Enginy, Wizeline and Haddock at interview stage, none at offer.*

> Yes, I'm interviewing with a few other companies. Nothing is at offer stage.

### [NEEDS YOUR STORY] gaps this round could hit
- **Q17 bad day** is marked [NEEDS YOUR HONEST ANSWER]. Low odds in a TA screen; "team and culture" makes it possible.
- **Story E (KOM)** is unfleshed. Only matters if Clare probes the eleven studio years.
- JD gaps (Code Connect, keyboard and screen-reader conformance, native mobile): answers are under "Do you have experience with Code Connect, accessibility or mobile?" above.

### Questions to ask Clare (pick 2-3)
- What are the next steps, and where does the process stand: how many candidates are further along? (Kabilio rule, `memory.md` 2026-10-16.)
- Who owns Suitcase day to day right now, and who does this role report to? (Tanna said she had been covering it; this is "what happened to the last person in this role" phrased for TA.)
- Is mobile on the same Suitcase foundations, or is the Compose Multiplatform system separate today? (Shows homework. Clare may not know; if not, note it as a hiring-manager question.)
- What is the salary range for the Barcelona hire? (Only if she hasn't raised compensation. Salary rule 2: ask before restating a number.)

### Salary reminder
- Stated on the form: **EUR 65,000 gross annual base**. No range published. Floor (40K employed) is never stated.
- If asked: give Clare a chance to name the band first ("Is there a range for the Barcelona role?"). If she presses, keep 65K; don't drop it to look flexible. Never share Abacum or Remuner pay (rule 8 wording in `context/salary.md`).
- After the call, record in the record: range given (if any), whether asked, what was said, any compensation feedback.

*After the call: run `/debrief-interview perk "TA Preliminary"` while it's fresh.*

## Round 1 debrief: TA Preliminary (Thu 2026-11-05)

Source: call transcript pasted by Manel. Clare joined about five minutes late; the call ran about 18 minutes.

### Logistics confirmed
- Based in Barcelona; three days a week in the office is fine; available immediately; no visa sponsorship needed. Remuner end date (March) on the CV confirmed as current.

### Questions asked, and what Manel answered
- **Background:** close to the prepared answer. Added two things not in the prep: "I started there working on design systems for clients" (Kings of Mambo).
- **Why did you leave Remuner?** A paraphrase, not the memorised version: product came from the top, design didn't have the input needed, "not the way I like to work. So we parted." The CTO "2010 app to a 2020 app" line was left out. Clare summed it up as wanting "more ownership of your own decision making... set the strategy yourself"; Manel agreed.
- **Why Perk?** Clare noted the referral first (Tanna named). Manel gave the structural hook (core and experimental layers, adoption measurement, Figma-to-code parity) and said that's what he has been doing. The stage part (47% and 80%, MUI migration) and the alignment part (pipeline, content keys) weren't used.
- **Design team scale vs. past teams (not in prep):** Manel said six designers at Abacum, and that at Kings of Mambo he had clients with "around 15, 16 designers".
- **Did you train and coach those 15? (not in prep):** "Yes, totally": worked on adoption, explained how to build and use the system, took feedback to iterate on components and variants.
- **How much do you use AI?** The three-use answer: live prototypes tested with users instead of static Figma ones; design system work through the Figma MCP (tokens, Storybook, documentation, colour contrast); "push code to production where I can", with guardrails. Said he started "at the beginning of the year, or at the end of the past year".
- **Happy working alongside engineers, or want to keep code ownership? (not in prep):** "I was a front-end engineer in the past, but not now"; comfortable working with engineers because he understands their language.
- **Salary:** Manel said 65K was on the form and asked for the range. Clare checked and said "probably closer to seventy actually", plus benefits and stock options: "we're in the right spot".
- **Other processes:** interviewing elsewhere, nothing at offer stage.

### Claims to check against the evidence register
Not in `evidence/experience-facts.md`; confirm before the hiring-manager session, because Tim may ask for detail:
- Design system work for Kings of Mambo clients.
- A client with around 15-16 designers, and coaching them on adoption.
- "Push code to production": the register supports PRs for styles and tokens, reviewed and merged by the front-end team. Keep that wording.
- "I was a front-end engineer": the register supports studio front-end production code, but says not to present Manel as a front-end engineer. He qualified it ("not now").

### What we learned about the role and team
- **Design team:** about 40 people including researchers and content designers, about 30 of them product designers, split across London and Barcelona and weighted a little to Barcelona. Designers report as a craft and are aligned to product pillars, working daily with their squads.
- **Suitcase today:** Clare called design systems "a bit of a bolt-on" at Perk so far. One person is dedicated to it now (inference: likely Tanna, who said she had been covering it), with a project team of designers from different squads. Not greenfield; this role will set the vision and strategy and own execution, workshops, coaching and stakeholder explanation.
- **Squad:** a dedicated front-end engineer, based in Barcelona. A dedicated PM is unlikely; probably several PMs across pillars. Clare will check; Tim can explain.
- **Reporting line:** hiring manager Tim, in London; his manager (a director) is in Barcelona. Inference, not confirmed: Tim is Tim Archer, Senior Content Design Manager, who posted the role on LinkedIn on 2026-10-20 and whose post Manel commented on (content tokens and the SimpleLocalize keys).
- **Mobile:** Clare thinks Suitcase covers all platforms and product pillars, including acquired businesses now integrated. Her belief, not confirmed; ask Tim.

### Process
1. **Hiring manager session, on site in Barcelona:** Tim dials in from London, with a local designer or the director in the room. Exploratory; they want to see the portfolio. Target next week; Tim is off Tue 10 and Wed 11 Nov.
2. **Online case study:** one of Manel's own portfolio cases, no new deck. Dig into the problem, challenges, success metrics and how adoption went. Plus a couple of scenario questions about challenges at Perk, run as a team exercise.
3. **Leadership wrap-up:** the CPO or another design leader.

Two to three weeks in total; Clare can speed it up if another process moves faster.

### Next step
Clare will send two emails: a process confirmation with prep links, and an availability link for the on-site session. Submit slots for next week (Mon 9, Thu 12 or Fri 13 Nov, given Tim's leave), then run `/prep-interview perk hiring-manager`.

## Process email from Clare (Thu 2026-11-05, 20:12)

Pass confirmed. Scheduling arrived in a second email the same evening: an Ashby availability link (https://you.ashbyhq.com/meeting/3363cb0c-aa0c-4e70-bc49-2520a7764fe4/), 9:00-18:00 GMT/CET, round not named. The email describes "the Perk Product interview process":

1. **Depth of Expertise (60 min, video), with a Lead Product Manager.** One recent project end to end: core challenges, steps from start to finish, final impact. Also the collaboration side: who else was involved and how the team dynamics were handled. No presentation required; assets or documentation welcome.
2. **Design Critique Exercise (60 min, ideally in person; screen share if remote).** Walk through a Perk flow together; how feedback to peers is structured, the thinking behind suggestions, and next steps to move the design forward. Collaborative, no prep.
3. **Final interview with a Leadership Team member.** Career goals, Perk values, ways of working. Bring thoughtful questions.

At least one session in person at the office applied to (Barcelona).

**Prep list from the email:** Perk website and core values; Platform Overview; what Perk does, the space, target customers and competitors; a product-insights blog post and the engineering blog; the Entry Ready launch presented by the CPO (Nikita); the Audi Revolut F1 Team travel story; what excites Manel about the role.

**Conflict with the TA call.** Clare said round 1 is a hiring-manager session with Tim, on site, and round 2 an online case study on Manel's own case. The email says round 1 is a video call with a Lead PM and round 2 an in-person critique of a Perk flow. Resolved 2026-11-06 (Manel's call): the written email is later and explicit, so round 1 is the Depth of Expertise video call. Prep the project deep dive; the critique is the likely in-person round. The invite will name the interviewer (Lead PM or Tim).

## Round 2: Depth of Expertise (brief written 2026-11-06)

**Date:** not booked. Slots submitted Wed 11 to Tue 17 Nov. 60 min, video.
**Interviewer:** unknown until the invite. The email says "one of our Lead Product Managers"; on the call Clare said Tim. Re-read this brief once the name is known: a PM probes delivery and prioritisation, Tim (content design) probes content tokens and coaching.
**Format:** one recent project end to end (core challenges, steps, final impact) plus collaboration: who else was involved and how the team dynamics were handled. No deck required; assets welcome. Time for questions.

### What Perk most likely cares about
1. **Adoption across a team that doesn't report to you.** Suitcase is "a bit of a bolt-on" with one dedicated person and a project team from the squads; about 30 designers. They need someone who gets squads to use and contribute to a system they didn't ask for.
2. **System work competing with the product roadmap.** A Lead PM will ask how infrastructure got prioritised against features, and what the system did for delivery. No dedicated PM on the role, so the designer makes that case.
3. **Honest impact.** "Final impact of the solution" is in the brief. They'll test whether numbers are real and whether you know what didn't work.

### Lead project: Abax (Abacum), with Remuner as the follow-on
Positioning mapping for DS roles: Remuner and Abacum systems. Choose Abax as the deep dive because this round is about collaboration and team dynamics, and Abax is the one with a team: head of design, engineering leadership, five squads, a contribution process and a tracked adoption number. Remuner was sole-designer work, so it's thin on team dynamics; use it as "what I did next with what I learned" (smaller token set, ESLint enforcement, Codex CI checks).

Arc to know cold (beats, not script), all from `evidence/experience-facts.md` ("Abax design system"):
- **Problem:** ad hoc components and MUI across five squads, no mandate.
- **Case for it:** co-led the business case with the head of design; presented to engineering leadership and at an all-hands.
- **Capacity objection:** engineering feared the system would compete with squad work → Maker Days, one focused week → tokens and the first Button in production (battle card C).
- **Rollout:** new components behind feature flags; squads added their own migration tickets; weekly design-library sync and review before anything entered the canonical library.
- **Tokens:** two-tier architecture, Token Studio to Style Dictionary.
- **Impact:** a monthly codebase count put Abax at about 47% of tracked Abax and MUI uses at departure, against an 80% goal; two squads finished the form-element migration, a third was mid-way. Qualitative: a designer built a screen fast from the variants; customers said the product felt more polished. Say the 80% wasn't reached, and why, before they ask.
- **Example to use:** Select and Autocomplete. Designers weren't sure which to use, and detached the menu to add or remove items because hiding items broke the auto layout and the menu didn't resize. Detachment data pointed at it (Figma health measure: you defined it, an engineer built the script). Fix: split into Select, Menu and Menu item, with a slot (placeholder component plus instance swap) so designers build their own items locally; guidance in the docs page and the component description; a weekly-meeting session walking designers through it and taking feedback. Result: detachments on it almost stopped; the remaining issues went into later iterations.
- **Adoption work:** no real resistance; the problem was designers forgetting what existed. Every release on Slack, coaching in the weekly DS meetings, ad hoc sessions for those who needed it; adoption and detachment metrics showed where to ask why, then fix in the next iteration. This is the part that maps straight onto Suitcase.
- **Your part vs the team's:** "I" for the business case, token and library work, the sync and contribution process; "we" for the decision and the migration. Engineering built the original pipeline.

**Assets to have open:** the live DS case (manel-leiva.com/cases/design-systems). Screen-share only if it helps a specific point.

### Likely questions, mapped
| Question | Use |
|---|---|
| Walk me through a recent project end to end | Abax arc above |
| Who else was involved; how did you handle the dynamics? | Head of design (co-lead), engineering leadership, squad designers in the sync. Battle card C |
| How did system work get prioritised against features? | Maker Days as a bounded bet; squads owning migration tickets |
| What was the impact? How did you measure it? | 47% vs 80%, the count method, squads migrated; no velocity number, don't invent one |
| What would you do differently? | What Remuner changed: smaller token set first, ESLint enforcement earlier |
| A squad or designer who didn't want to adopt | No real resistance; the friction was remembering components and variants exist. Slack release notes, coaching in the weekly DS meetings, ad hoc sessions; adoption and detachment metrics → ask the designer why → fix next iteration |
| How did you coach designers on the system? | Abax coaching (above). Earlier and larger: vLex, a Kings of Mambo client, about 15 designers |
| A disagreement with a stakeholder | Battle card D (Manager view, Remuner) |
| A mistake | Battle card E (token file outage) |
| How do you use AI in system work? | Figma MCP: tokens and drift, accessibility checks, docs. Ties to the JD's AI-readable specs |
| How would you approach Suitcase in the first months? | Listen first: who consumes it, what's measured, where squads bypass it. Don't present a plan for a system you haven't seen |

### Gaps this round could hit (don't invent)
- **A single coaching episode with a result.** The practice is now recorded (2026-11-06: Slack releases, weekly DS-meeting coaching, ad hoc sessions), but no one designer's before-and-after. If asked, describe the practice; don't invent an individual.
- **vLex detail.** Confirmed 2026-11-06 as the client behind "about 15-16 designers". Dates, your exact scope on the system and any outcome aren't recorded; if Tim or the PM digs in, give what you remember and stop there.
- **Q10 disagreement with your manager** (`prep.md` [NEEDS YOUR STORY]); battle card D is the closest real episode.
- **Figma-side measurement detail.** Recorded 2026-11-06: you defined the measures (library instances vs custom frames, unlinked layers, a health score in Notion), an engineer built the Figma REST API script. Bi-weekly; health score = library instances / all UI nodes (library + detached + one-off frames); a detachment ranking set the fix order; per-component thresholds under 5% OK, 5-15% warning, over 15-20% broken. All approximate recollection; no history survives, so don't quote a score. Keep it separate from the codebase count behind the 47%: two measures, two denominators. One concrete example would make the adoption loop much stronger; have it ready if you can recall it.
- **Native mobile and multi-platform scale:** Remuner webview only. Say so if asked.

### Questions to ask (pick 2-3)
- How is Suitcase adoption measured today, if at all, and who looks at the number?
- When a squad needs something Suitcase doesn't have, what happens now: build it locally, wait, or contribute it back?
- (PM interviewer) How does system work get onto a pillar's roadmap today, with no dedicated PM on it?
- (Tim) Where are content tokens today, after the comment on your post?

### Salary
Not expected in this round. Stated EUR 65,000 on the form; Clare said the level is "probably closer to seventy" plus benefits and stock options. If raised, say it was covered with Clare and refer to her. Don't open a new number with the interviewer.

### Prep checklist before the call
- Say the Abax arc out loud once, timed to about 10 minutes, then the impact part alone in 90 seconds.
- Clare's prep list: Platform Overview, Entry Ready launch (CPO), one product blog post. Enough to answer "what excites you" with one specific detail.
- Recall one component fixed after the detachment loop, and the tool behind the detachment count.

*After the interview: run `/debrief-interview perk "Depth of Expertise"`.*
