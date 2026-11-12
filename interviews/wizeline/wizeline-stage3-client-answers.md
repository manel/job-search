# Wizeline client interview (Dow Jones): answers to read

Fri 13 Nov 2026, 18:30-19:30 Madrid (moved from 10 Nov). Panel: Forest Evashevski (Director, Experience Design, WSJ), Esteban Gabriel Abete (EMEA Delivery Director, Wizeline), Wizeline staffing and David Ho. Brief: [wizeline-stage3-client.md](wizeline-stage3-client.md).

Headline first, 60 to 90 seconds, then stop.

## Tell us about yourself

Variant of [answers.md](../answers.md#opening-intro) for a design-systems seat: it adds vLex and the design-system thread.

> I'm a Senior Product Designer based in Barcelona, with about 15 years in the field.
>
> I co-founded a UX studio, Kings of Mambo, and ran it for eleven years. I did research, interaction and visual design for clients in very different industries, and I wrote a lot of the front-end code myself. Part of that client work was design systems. For vLex, for example, I helped build their system and coached about 15 of their designers on using it.
>
> Then I joined Abacum, a financial planning platform. I started on data integrations and ended up co-leading the design system, Abax, with the head of design. It served five product squads, and we moved the product off MUI onto our own components.
>
> Most recently I was the only designer at Remuner, a sales compensation platform. I built the design system there from scratch and designed the product's AI agent.
>
> So I've spent most of my career on design systems and on the product work around them, in client work and in-house. That's why this role interests me.

## Why WSJ, why Dow Jones?

> What interests me is a system that has to serve several brands and a lot of different surfaces, the app, the web, articles, and still feel like one product to the reader. I've built similar systems but I'd like to work on it at that scale.

Then expect "have you done multi-brand?" (below).

## Have you worked on multi-brand or theming?

> Not as a shipped multi-brand system. Both Remuner products were the same brand. But the structure was ready for it: one core of primitives, then a semantic layer for the app and another for the marketing site, with typography modes for desktop and mobile. A new brand would be one more semantic layer on that core. I'd like to hear how you've solved that.

## Why should we hire you? / What would you bring?

> Three things. First, I've built design systems for several clients, so I know how to work inside someone else's team and process. Second, I've worked inside one system shared by many teams: at Abacum it served five squads, with a weekly library sync. Third, I work close to the code. At Remuner I owned the tokens repo and opened PRs the engineers reviewed.
>
> In the first months I'd learn your design system and how people contribute to it, check what my area uses against it, and bring the gaps back as proposals.

## Senior Visual Designer. How strong is your visual design?

> Visual design is where I started. At the studio I did the visual design for client sites and products for eleven years. In the systems work it shows in the foundations. At Remuner I built the colour ramps from the brand colours and chose contrast over harmony when they clashed. I also set the type scale after an audit found text anywhere from 9 to 25 pixels. And I designed the marketing site's library and the LinkedIn templates the marketing team used.

## How do you contribute to a design system you don't own?

> I keep looking at the system and at what people ask of it. When I find a gap, I bring it back as a proposal instead of building my own version. At Abacum, squads reported problems through a Notion page and a Slack channel, sorted into broken components, naming proposals, improvements and detached instances. We went through them in the weekly library sync and tracked adoption every month.
>
> The requests also tell you where the system needs to go. So I'd help shape that direction with the people who own it, and then work towards it: making the system faster to use, more widely adopted and easier for designers and engineers, without lowering the quality customers see.

## Accessibility

> At Remuner I brought the text and icon colours up to WCAG double A contrast. Where double A and visual harmony clashed, double A won. Error states carry a message, not just a red border, and I checked some components with screen readers. I haven't done full keyboard and screen-reader conformance work. In an accessibility-first system I'd follow its rules and check contrast and states in every component I touch.

## How did you measure success?

> At Remuner I tracked adoption screen by screen on an audit board: when I left in March, 10 of the 18 core screens ran on system components. The CTO described the change, unprompted, as going from a 2010 app to a 2025 app. I didn't measure product impact, and I'd do that differently now. On a product like yours I'd track how long a new surface takes to ship on the system components.

## A demanding senior stakeholder / a time you disagreed

Story [`manager-view`](../stories.md#manager-view): opener, then context, the decision you accepted, what you kept in, the mixed result.

If they push back during the interview: acknowledge it, give your reason once, ask what they'd weigh.

## Have you worked on consumer or news products?

> Not news. At the studio I designed content sites and CMS workflows for clients, including modular content blocks that the client's team edited per product page. That's consumer web and content tooling. News is new to me.

## Working with remote or US-based teams

> Yes, in several companies.
>
> To work well like that, a lot of the work has to happen in writing: specs, tickets, documentation. Then someone in another time zone can pick it up without waiting for a meeting.

## A mistake you made

Story [`token-file`](../stories.md#token-file). It's already in the deck (Figma 17), so keep it to the opener and what changed afterwards.

## Why did you leave Remuner?

[answers.md](../answers.md#why-did-you-leave-remuner), the standard version, unchanged. Say it and stop.

## What have you been doing since March?

[answers.md](../answers.md#what-have-you-been-doing-since-march). Lead with the Claude and Figma MCP work on design systems (token sync between code and Figma, drift, contrast checks), then occasional freelance.

## Situational questions

Hypotheticals: answer with "I'd", then give one real example where one exists. Never present the proposed steps as something you did. If they ask "has that happened to you?" and no example is listed, say so.

### A team on a deadline wants to build a custom component because the system one doesn't cover their case

> First I'd ask why. Is it a one-off, or will other teams hit the same case? Then I'd check whether an existing component covers it, and if not, whether a new variant would. If it really blocks the release, I'd let them ship the custom version and put the replacement on the system roadmap, so it gets replaced once the system covers it.

### Two teams use their own detached versions of a core component

> I'd find out why they left the core one first. It could be a real user need, or they couldn't find it, or the docs didn't explain it. Then I'd compare how far each version drifted and plan one component that covers both needs. I'd release it behind a flag and track adoption per team before deprecating the old versions.
>
> That's how we rolled out the new form components at Abacum. They shipped behind feature flags, and each squad added its own migration tickets to its sprint, so the central team didn't gatekeep the rollout.

### A brand or editorial team wants something the system doesn't allow

> I'd ask what they're trying to do for the reader. Often the need is fair, and then the system should give them a supported way to do it, like a brand layer of tokens or a component made for that kind of expression. What I'd hold firm on is the base: contrast, spacing, and how interactive components behave.

### An accessibility problem shows up just before release

> I'd reproduce it with QA and engineering, then check who it affects and whether it blocks a core task. The options are usually a focused fix, cutting that part from the release, or delaying it. I'd give whoever owns the release a clear recommendation. A deadline isn't a good enough reason to ship something some readers can't use. Before closing it, I'd check the fix against the WCAG criterion it failed.

### Several teams need you at once and priorities keep changing

> I'd make the queue visible: each request with its deadline, who it affects and what depends on it. Then I'd agree the order with the leads instead of saying yes to each one separately. When something new becomes urgent, we say out loud what moves down.

### A stakeholder changes an approved decision late

> I'd find out what changed: new evidence, a business constraint, or a preference. Then I'd lay out the options and what each one costs for users, for delivery and in rework. We agree who decides, I update the spec, and everyone affected hears about it. If the new reason holds, we change course, and the team sees the cost before we do.

## Questions to ask

For Forest. Ask the first one early, right after the deck; then pick one more:
1. "The profile says Senior Visual Designer. How much of the role is visual design, and how much is product and system work?"
2. "Which WSJ surfaces would I work on first, and how do product designers work with the design system team?"
3. "How does a new pattern get into the design system? Who decides what goes into the core and what stays in a product library?"
4. "What would make the first three months a success for you?"

For Esteban, if there's time:
- "How is the Wizeline team on the account set up, and who would I work with day to day?"

## Salary

Agreed with Wizeline. If anyone asks: "I've agreed the terms with Wizeline and they work for me." Never mention a floor or prior pay.
