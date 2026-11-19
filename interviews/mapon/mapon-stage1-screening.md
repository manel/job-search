# Mapon, stage 1: Testlify introductory task

Record: [applications/records/mapon-senior-product-designer.md](../../applications/records/mapon-senior-product-designer.md). Invite from Elizabete Millere, 2026-11-17: three written questions and one video question on experience, motivation and approach to the role. About 20 minutes, no pause once started (block 25). Window: 4 days, so submit by 2026-11-20.

## How to use this file

- The real questions are shown only when the task starts. The ones below are guesses based on the invite wording and the JD.
- Mapon asked for answers "in their own words". Testlify can flag pasted text and tab switches. Read these drafts before the task, then write the answers yourself from memory during it. Do not paste.
- If a question doesn't match a draft, take the facts from the closest draft and answer the question they actually asked.
- Written answers: one short paragraph each, first person, open on the matching experience ([memory, form answers](../../memory.md)).

## Facts to keep consistent

- Location: based in Barcelona, the location on the posting. Occasional on-site weeks in Riga are fine. No relocation and no regular Riga office days. This matches the cover letter.
- Salary: not asked. If a question asks for it, read [context/salary.md](../../context/salary.md) first. The published range is EUR 3,000 to 5,000 gross a month.
- AI agent: released to all customers before March 2026, mixed feedback, no adoption or accuracy metrics. Engineering owned the architecture. Limits in [stories.md, ai-agent](../stories.md#ai-agent).
- IC dashboard: analytics results are directional only. Say "fewer clicks" and "opened the full plan view less", with no figures and no tool name. Limits in [stories.md, ic-dashboard](../stories.md#ic-dashboard).
- Abax: co-led with the head of design; about 47% of tracked component uses at departure, against an 80% goal.

## Written: why Mapon, why this role

I'd like to join because this role asks for shipping AI assistants, recommendations and automations for fleet operators. The assistant side is similar to what I designed and shipped at Remuner, an AI agent that answered sales reps' and managers' questions about their commissions and plans. Managers could ask about their team, and reps only about themselves, which is close to how Tachogram separates managers and drivers. The agent could also give wrong numbers for clients with custom calculation code, so I understand why you want AI that's easy to correct when it's wrong.

Case: manel-leiva.com/cases/ai-agent

Prep note: the Remuner agent answered questions only. Do not claim recommendations or automations from it. Tachogram's manager and driver access comes from tachogram.com/en/for-businesses, read 2026-11-18.

## Written: tell us about relevant experience or a project

A recent example is the AI agent I designed at Remuner, a sales-compensation platform. Reps and managers asked about their pay, and each role was allowed to see different data. I owned the conversation design, the answer formats and the trust patterns. I also set up the role-based context: managers could ask about their team's plans, and reps could only see their own. Engineering told us what data the agent could use, and I agreed the scope with the founders and the engineers. Then I designed which questions it would answer and how it would refuse the others, and laid out answers as tables or lists when that made them easier to read. It went live for all customers. Feedback was mixed, so after launch we kept changing the tone, the terminology and how answers were laid out.

## Written: how you approach a design problem, or how you use research and analytics

I use interviews to find out what a vague complaint means, and product analytics to check whether the change worked. At Remuner, when reps told us their dashboard wasn't intuitive, I found the people who had said it and interviewed them. They meant different things. Some couldn't follow how their commission was calculated, some didn't know which metrics affected their plan, and some read the commission on screen as what they'd get paid that month, though payouts were quarterly. I added a calculation summary with access to the full detail, and showed the period and the payment dates. Then I tested the changes with users. After the release, product analytics showed reps reaching the metric they wanted in fewer clicks. They also opened the full plan view less, because the dashboard now showed what they used to look for there.

## Written: design systems, if asked

At Abacum I co-led the Abax design system with the head of design, across five product squads. I worked on the token architecture, components and governance. Squads planned their own migration tickets, and we released new form components behind feature flags. When I left, about 47% of the component uses we tracked in the code were Abax, against a goal of 80%. At Remuner, as the only designer, I built the component library from scratch and owned the token repo. I also opened pull requests that replaced hardcoded styles with tokens, and the front-end team reviewed and merged them.

## Written: how you use AI, if asked

Use the approved wording in [perk/perk.md](../perk/perk.md#how-do-you-use-ai-in-your-work-approved-by-manel-2026-11-16), shortened to its first three paragraphs. Change the closing paragraph for Mapon: the JD lists Claude as a plus and asks for AI-native ways of working.

## Video: introduce yourself

About 60 to 75 seconds. Based on the approved [opening intro](../answers.md#opening-intro). Say it from memory and use the lines below only as reminders.

Hi, I'm Manel, a Senior Product Designer based in Barcelona.

I co-founded a UX studio, Kings of Mambo, and ran it for eleven years.

There I worked across research, interaction design, prototyping and delivery, for clients in several industries.

Then I joined Abacum, a finance platform.

I worked on data integrations and financial modeling, and I co-led the design system with the head of design.

Most recently I was the only designer at Remuner, a sales-compensation platform.

I designed its AI agent, the one that answers questions about commissions, and I built the design system.

Your role asks for AI assistants and automated workflows in an operational product, and for design system work.

I did both at Remuner, and design systems at Abacum too.

I'm in Barcelona, and I'm happy to come to Riga for on-site weeks now and then.

Thanks for watching. I hope we can talk soon.

## Before you start

- Read each written draft once, then close this file.
- Say the video answer aloud once. Rewrite any line you trip over.
- Check the camera, the microphone and the light. Close Slack and email.
- Start only when you have 25 free minutes, and not right before or after the Fever Mettl test.

## Debrief (completed 2026-11-18)

Source: Manel's account after the task. The prepared drafts covered the AI and experience angles, but the questions recalled below went elsewhere. Exact wording was not kept, and which questions were written is not recorded beyond the video.

| Question | What Manel said | Check against the evidence |
|---|---|---|
| Figma proficiency and design systems | Very proficient in Figma and in developing design systems. A lot of experience working in Figma, creating components and using "Atomic Design System". | No figure or system count given. Atomic Design confirmed by Manel 2026-11-18 as the method in all his systems (small components up to larger ones); the files do not use atom or molecule names. |
| Biggest achievement in an iOS and Android app | Not much experience in native iOS and Android apps, but a lot with web views, mobile and responsive web. Biggest achievement: the checkout process of the Kymco store. | Consistent. Kymco checkout launched and took real orders; lead designer and front-end owner, with Eric Cardona also designing. No conversion figures. Best webview proof: Remuner iOS and Android wrapper apps, summer 2024. |
| Video: project most proud of | The Abacum design system. No system on arrival, inconsistencies, developers rebuilding the same components. Presented the case with the head of design and got the go-ahead. Used a Maker Days week as a first test: created and deployed tokens and built 5 components, which then improved time for designers building screens and for developers. | Three details differ, listed below. |
| One more question | Not remembered. | Unknown. |

Corrections for later stages (do not contact Mapon about these):

- Tokens were in production from late 2022. The Abax components came in the October 2023 Maker Days week.
- That week merged seven components, the Button first. Engineers wrote the code. Manel said 5.
- No time saving was measured. The measured figure is about 47% of tracked component uses at departure, against an 80% goal.
- The work was selected for Maker Days and leadership then agreed to continue it. Do not say the all-hands presentation won approval.

Next step, from the JD: practical task, then a video interview with the Hiring Manager and HR of up to 60 minutes. No timing given.
