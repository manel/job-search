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
