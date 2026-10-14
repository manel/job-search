# Datavant: Hiring Manager practice script

This is a 30-minute conversation about design experience, product judgment, partnership style, and fit. No portfolio presentation has been requested for this stage. [Background and evidence notes](datavant-hiring-manager-reference.md).

## Tell me about yourself

I'm a product designer based in Barcelona with more than fifteen years of experience. I'm analytical and I enjoy working on complex problems.

I work closely with Product and Engineering, from defining the problem through delivery. I'm comfortable questioning an assumption if the evidence points in a different direction. I try to make the tradeoffs clear and help the team decide what to do next.

I'm now looking for a hands-on senior role where I can own a complex product area and make the product easier to understand and use.

## Walk me through your background

I co-founded a UX studio called Kings of Mambo and spent eleven years working with clients in different industries. My work covered research, information architecture, design, delivery, and also front-end implementation.

In 2022, I joined Abacum, a financial planning and analysis platform, as a Senior Product Designer. I started in the integrations squad and later moved to the engine squad. I led the design and customer testing for Dataset Manager, which gave finance teams a guided way to configure their data. I also worked on the modeling language and co-led the design system business case with the Head of Design.

Most recently, I was the sole designer at Remuner, a sales compensation platform. I worked across the product, built its component system, and designed an AI agent that answered questions about sales compensation.

I'm now looking for a hands-on senior product design role where I can own a complex product area and work closely with Product and Engineering.

## Why Datavant?

Aideen described a challenge that was very interesting to me: bringing several complex tools together and helping providers do more without contacting support. I enjoy understanding how the different parts work and making the experience consistent as users move between them.

It connects well with my experience at Abacum. I helped finance teams configure their own data, made the language more consistent across datasets and modeling, and developed shared patterns across squads.

Healthcare would be new to me, but the underlying product problems are familiar. I could bring experience with complex workflows while learning the needs of providers.

## You do not have healthcare experience. How would you close that gap?

I would first learn the terminology, regulations, operational constraints, and main user groups. I wouldn't assume that finance and healthcare work in the same way.

How I learn a complex domain is transferable from past experiences. At Abacum, I combined customer research with input from implementation, Product, and Engineering.
- Internal teams helped me find repeated support problems and system constraints.
- Customer testing showed me how users understood the work.

I would take the same approach at Datavant: learn from internal experts, test assumptions with providers when possible, and be clear about what we still don't know.

## How would you approach making several complex tools feel like one product?

I would start by mapping the full user task, learning the concepts shared across the tools, and the handoffs between them. I would focus on what interrupts the user's work.

At Abacum, finance teams used Dataset Manager to configure imported data. They used dimensions to organise that data for financial modeling. A dimension could be a department, region, or account. Dataset configuration and dimension management were separate parts of the product.

Users could assign an existing dimension to a dataset column. But, if the dimension did not exist, they had to leave the dataset, create it elsewhere, return, and resume. Customer feedback showed that this added time spent , errors and confusion.

I identified the problem and proposed basic dimension creation and editing inside the open dataset and we built it. After launch, customers said configuration was faster, clearer, and less prone to errors.

We placed the actions where users needed them. I would use the same approach at Datavant. I would understand the full workflow, find what causes friction, and connect the tools around the user's task.

## Why did you leave Remuner?

Remuner was very founder-led, and I felt that sometimes there was limited room for design to influence product direction. Over time, I realised the fit wasn't right. I do my best work when I can help shape the problem and discuss options early with Product and Engineering.

I'm proud of projects I did there like the design system and the AI agent we shipped. I want to build on that kind of work in my next role.

## A time you disagreed with leadership

At Remuner, we were rethinking the manager view. Research showed three main problems:
- Managers couldn't compare sales representatives by metric without opening them one by one.
- Reaching information took too many clicks, as there where cards opening more cards.
- It was hard to compare the current period with previous ones.

I recommended fixing those workflow and information architecture problems before doing a broader redesign. The CEO and CTO wanted to continue with the full redesign. I explained my concerns and the research behind them. Once they made the decision, I committed to making it work as well as I could.

I kept the main research findings in the redesign. I introduced tabs organised by metric, with a custom order, so managers could compare representatives more easily. I also reduced the number of navigation steps, although I felt that part needed more work.

The redesign shipped. Feedback on those changes was positive, but feedback on the overall experience was mixed. Some users were adjusting to a new interface. Others still had trouble finding information they needed. I reviewed the feedback and separated task blockers from less urgent friction so we could prioritise future changes.

It taught me to make my case clearly, support the final decision, and stay honest about what still isn't working after launch.

## A time research changed your design

At Abacum, I was working on the Dataset Manager. The goal was to let finance teams configure their own data without depending on the implementation team and a JSON editor.

Our first direction was simplifying the interface and combine it with SQL for data transformations. During testing, users could describe the transformation with Excel functions but couldn't reproduce the same logic in SQL. We were asking them to use the wrong language.

I took that finding to the PM and lead engineer. We dropped the SQL direction and went for extending Abacum's modeling language instead. It was a custom language designed to feel familiar to Excel users. The guided interface handled the rest of the configuration flow.

After shipping it, the implementation team reported spending roughly half the previous time, and customers reached a working configuration in their first session. We didn't measure that through analytics. The important lesson was that research changed the product language, not just the interface.

## Approaching a complex workflow?

I start with the user's goal, the current workflow and the constraints. I map what users need to do, what information they need, and what might block them.

Then I identify the riskiest assumptions and explore them at a basic level. That might be a flow, a wireframe, or an interactive Figma prototype when the sequence matters. I involve Product and Engineering early, while the options are still easy to change.

I test the parts that need evidence and add detail as the direction becomes clearer.

During delivery, I stay involved in edge cases, implementation, and design QA. I also agree with the team on how we will judge and measure the result.

## How do you work with Product and Engineering?

I keep Product and Engineering involved throughout the design process, from research to delivery. At the start, we agree on the problem, the goal, the evidence we have, and the main constraints.

I share work early and involve them in research and debriefs when possible. This means we see the same evidence and can discuss the options together.

At Abacum, testing Dataset Manager showed that users understood the logic in Excel but couldn't use SQL. I discussed the finding with the PM and lead engineer. Because we were looking at the same evidence, we changed the direction together and extended Abacum's Excel-like modeling language.

As the work moves into development, I stay involved to answer questions, resolve edge cases, and review the implementation. The goal is to keep the team working with the same context and avoid surprises during delivery.

## A time Engineering pushed back

At Abacum, the Head of Design and I were making the case for a shared design system. Engineering had a reasonable concern. The system could become a side project that competed with squad priorities and never reached production.

We showed examples of repeated product inconsistencies and compared two staffing options. A smaller group could work alongside normal sprints for two weeks, or a larger group could run a focused one-week Maker Days test. The team chose the focused week.

During that week, the token setup and first Button component reached production. That showed that the system could move from design into code. It also gave the team something real to evaluate.

## How do you prioritise when you cannot fix everything?

I look at how much a problem blocks the user, what is missing, the cost of fixing it, and the team's capacity. I also consider whether planned work will change that area.

For example, at Abacum we first proved that our design tokens could reach a production component by building the Button. We could have kept refining the tokens, but teams still lacked components and variants they needed for product work. Closing those gaps had more immediate value.

We prioritised production components and missing form variants, and delayed some foundation work. We used weekly reviews and codebase counts to find the biggest gaps and adjust the order. The team made those decisions together.

I make the tradeoff clear. I explain what we are fixing, what we are delaying, and when we should reconsider it. The goal is to use the team's capacity on the problems that matter most at that moment.

## Tell me about a mistake you made

At Remuner, I made a production mistake while cleaning up our design token files. I thought one file was a duplicate and deleted it, but the frontend application still depended on it. The next deployment caused a short outage.

I quickly restored the file, pushed the fix, and took responsibility for the mistake. For the next few days, I checked every required file before deploying changes from the token repository. We then added a required-file check until we could remove the duplicate dependency from the frontend application.

## How do you measure whether a design was successful?

I like to define success around the user's task. For Dataset Manager, the main goal was autonomy. Finance teams should be able to handle most standard configurations without the implementation team. We also wanted to reduce configuration time and support work.

After launch, customers reached a working configuration in their first session. The implementation team believed that standard configurations took roughly half the previous time. That was a team estimate, not analytics data.

With better measurement, I would track completion without help, time spent, where users leave the flow, and how often the implementation team steps in. That would show whether the product gives customers more autonomy or simply moves the same complexity into a new interface.

## What would you focus on when joining Datavant?

I would first learn who the main users are, which flows they follow, and what they do most often. I would also learn the platform and its terminology so I could understand past decisions and current discussions.

Then I would study the main user problems and the evidence behind them. I would review research, product data, support themes, and previous design decisions. I would also speak with the people closest to the users. The long-term vision matters too, because it tells us whether a problem needs a local fix or a broader change across the tools.

From there, I would work with Product and Engineering to choose a useful first problem. It should matter to users, fit the longer-term direction, and be focused enough to deliver and learn from.

## A provider workflow generates many support requests. Where would you start?

I would first identify the users, task, and types of support request involved. I would review support evidence and product data, speak with the teams handling those requests, and observe the workflow with providers when possible.

Then I would separate the likely causes. Users might be missing information, misunderstanding a term, facing a permissions issue, hitting a product limit, or dealing with a process outside the product. Each cause needs a different response.

With Product and Engineering, I would choose the most serious problem we could test safely and agree on how to measure the change. Depending on the workflow, I would look at completion without help, time, errors, abandonment, and support contacts. The goal would be to remove the reason users need help.

## How would you approach notifications across several tools?

I would start with the decision or action the user needs to take. For each event, I would ask who needs to know, how urgent it is, what happens if they miss it, and what they can do next.

Then I would define shared rules across the tools for priority, language, channels, status, ownership, and duplicate alerts. In healthcare, I would also learn the privacy, audit, and escalation requirements before designing the interaction.

I would prototype the riskiest cases, such as repeated alerts or unclear ownership, and test them with providers and internal teams. I would measure time to action, completion after an alert, ignored alerts, duplicates, and related support contacts. I have not owned a dedicated notification system, so this is how I would approach it, not a past example.

## What is an area you are working to improve?

I'm working on becoming more fluent when I give formal presentations in English. I work in English, but presentations require more time to structure my ideas and find the right words than they do in Spanish or Catalan. That can affect the flow.

I prepare a few clear points for each section and rehearse them aloud. That helps me focus on the argument without memorising every sentence. I also practise likely follow-up questions, because answering without a prepared structure is harder. I can explain the work clearly today, and I want to do it with more ease and consistency.

## What is one of your main strengths?

One of my main strengths is systems thinking and organisation. When patterns are inconsistent, I look across the product and find the shared structure. I turn that into components, states, behaviours, and rules that Design and Engineering can use.

At Remuner, I built the component system while continuing to work on product features. I reviewed the product, grouped repeated patterns, defined their variants and behaviours, and discussed technical constraints with frontend engineers. This let us improve the product in stages while building the system.

I use the same skill outside component libraries. It helps me organise complex workflows, show dependencies, and create structures the team can extend without answering the same questions again.

## What project are you most proud of?

The project I'm most proud of is the modeling language work at Abacum. The product mixed Excel conventions, SQL clauses, and custom syntax. Users understood the financial logic, but each function followed a different structure. That caused problems during onboarding and daily use.

The Head of Design and I identified the inconsistency. I reviewed customer calls, compared the language with familiar tools, and documented the different patterns. Then I worked with engineers on one function-based structure that stayed close to Excel and still supported datasets, dimensions, and joins.

I'm proud of it because the result went beyond the immediate usability problem. The predictable structure made the language easier to document and supported an inline formula helper that suggested the right parameters. It also gave the team clear rules for adding new functions.

## Questions for Mary

1. Which provider workflow would I most likely own first, and where do users need the most help?

2. When someone finds a product opportunity, what helps move it from evidence into the roadmap?

3. Who would I report to, and how would I work with you? If you would be my manager, what do you expect a designer to own independently?

4. What does growth look like for a senior individual contributor at Datavant? How do you assess progress and wider scope?
