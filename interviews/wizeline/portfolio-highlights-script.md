# Portfolio highlights script (Wizeline client interview, 10 Nov)

Figma file "Manel Leiva Portfolio Highlights", three frames, about a minute each.

## Opening, when they ask for the portfolio

I'll show three projects quickly, about a minute each, so you can see the product work I do outside design systems. Stop me on anything you want to go deeper on.

## Frame 1: AI Agent

This is Remu, a conversational agent I designed at Remuner, a sales compensation platform. I was the only designer and there was no PM, so I agreed the scope with the founders and Engineering.

Sales reps open it from anywhere in the app and ask about their own commissions, targets and plans. Managers can also ask about their team. I set up that split by role, so a rep only sees their own data.

Most of my time went into what you see on the right. The answer changes shape with the question. A progress question gets a short structured summary, and a question about periods gets a table. If someone asks something outside the scope, the agent says it can't answer that.

It launched to all customers. Feedback was mixed, so I kept working on tone, answer formats and terminology, because each customer called the same thing a deal, a contract or an item. I don't have adoption metrics for it.

## Frame 2: Dataset Manager

At Abacum, a financial planning platform, finance teams had to configure their data before they could model with it. On the left is what that configuration was: JSON, handled by our engineers. Customers depended on them for every setup.

I led the design and the testing for Dataset Manager, an interface on top of that configuration. On the right, a user picks a column, marks it as a dimension and turns on auto-mapping, without writing any code.

Testing changed one decision. I tested first with our FP&A specialists, who set up datasets for customers every day, then with customers. They could explain their transformations with Excel functions, but they couldn't write them in SQL. After an interim step with SQL-like formulas, transformations moved to Abacum's own formula language, which stays close to Excel.

The result is qualitative. The engineers who handled customer setups reported less configuration work. We didn't measure it.

## Frame 3: Modeling Syntax

Same company, different problem. Abacum's formulas had grown across teams, so they mixed Excel conventions, SQL-style clauses and custom syntax. On top you see the plain-text version.

With the head of design's support, I audited the functions: 15 of 37 broke the pattern. I went through customer calls and benchmarked Excel, Google Sheets, Pigment and Causal, and all four put parameters inside parentheses. At the bottom is the first step, from 2023: datasets and dimensions became coloured chips, so you can read a formula at a glance. You can still see the FROM and WHERE clauses outside the function. In 2024 I worked out the rules with one of our engineers to move every parameter inside the parentheses.

That stable structure later supported suggestions and a parameter preview in the formula editor.

## Close

Happy to open the Figma files behind any of these. Which one would be most useful?

*(Pause and let them choose.)*
