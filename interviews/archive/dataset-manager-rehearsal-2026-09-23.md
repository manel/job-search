# Historical interview rehearsal, 23–25 September 2026

Recovered 2026-10-13 from worktree thread `01a0ce90-e645-7702-8aaa-d213686d968b`. This is a historical transcript, not the current interview script.

Two English practice answers were submitted and received assistant feedback. Their existence establishes that practice occurred; live spoken delivery, timing and improvement were not independently verified.

The final historical token-file card overstates the later dependency cleanup. Manel clarified on 2026-09-30 that he checked required files manually for several days, followed by a required-file presence check while dependency cleanup remained pending. Use `evidence/experience-facts.md` and the current battle cards for that story. Dataset Manager chronology also retains the documented SQL conflict; do not use this transcript to resolve it.

## 2026-09-23T14:00:03.098Z — assistant

I’ll check the Career OS guidance, then we’ll start with your first practice answer.

## 2026-09-23T14:00:13.883Z — assistant

Welcome, Manel. We’ll take one question at a time.

**Tell me about a time you made a complex product easier for users to understand. What was your role, what did you change, and what happened?**

Choose one specific episode. Answer naturally in English, by voice or typing, aiming for roughly 60–90 seconds. It doesn’t need to be polished—we’ll work through it after your first attempt.

## 2026-09-23T14:07:56.540Z — user

So I'm going to explain a feature called Dataset Manager that was done in a vacuum, where I was the first designer in the integrations squad, and this task was meant to change the way users add data to the platform. So they could add datasets and work with them, transform data, aggregate, and so on. My target was to increase autonomy and to improve the experience working with the datasets, as users couldn't work on them, since it was really difficult for them to work, as they were JSON. It was a JSON file, so they couldn't work on it. So the first thing I did was— sorry. So the first thing we did was no. So for this, the first hypothesis was to just improve the experience, making a UI for the JSON, so users could edit the JSON, but in a simpler way. But after doing some research and giving users some tasks, I saw that that was not the part of the— that was not the problem for them. They stuck at the same point, so they couldn't finish the task. And I discovered that the problem was, apart from working in a JSON file, was also the language we used in the platform was not matching the language they were expecting. So I brought that to the trio, to the lead engineer and the PM, and I shared the results with them. And then I had to convince them to go to another direction, because only changing the UX was not going to improve the experience. Yeah, this is really difficult.

## 2026-09-23T14:08:11.054Z — assistant

You gave me a concrete episode to work with. The clearest part was your discovery: **making the JSON easier to edit wasn’t enough—the product’s language also confused users.**

What I understood:

- You were the first designer in the integrations squad, helping users manage datasets more independently.
- The initial hypothesis was that a visual interface for editing JSON would help.
- You tested that hypothesis with users. They still got stuck, and you identified a mismatch between the platform’s terminology and their understanding.
- You brought those findings to the PM and lead engineer to argue for a different direction.

Where I lost the thread: the opening repeated why datasets were difficult, but didn’t give me one concrete task users were trying to complete. Later, “only changing the UX” was confusing because changing terminology is also UX work. “Adding an interface over the JSON” is more precise.

**You partly answered the question.** I heard your role and discovery, but the story stopped before what actually changed and what happened afterward. Convincing the team is currently an unfinished part of the story.

Try the same episode again. Shorten the opening, keep the research discovery, and leave room for the change and outcome. Use “I” for your contribution and “we” for shared work. If the outcome wasn’t measured, say what you actually observed.

**What did you change to make Dataset Manager easier to understand, and what happened?**

## 2026-09-23T14:09:48.634Z — user

I think I better memorise the answer, it's difficult to answer while thinking in the whole story.

## 2026-09-23T14:09:58.544Z — assistant

Yes—preparing the answer first could help. Recalling the story, structuring it, and speaking English at the same time is a lot to manage.

I’d memorise **the sequence and a few key phrases**, rather than every word. A word-for-word script can make it harder to recover if you forget a sentence or the interviewer asks a different question.

You already have three useful anchors:

- **Problem:** users struggled to work with datasets through JSON.
- **Discovery:** a visual interface wasn’t enough; the terminology also confused them.
- **Decision:** you brought the findings to the PM and lead engineer to propose a different direction.

We still need the ending before preparing an answer you can practise. Let’s build it one piece at a time—short fragments are fine.

**After you shared the findings, what did the team actually change in the product?**

## 2026-09-23T14:13:23.153Z — user

So after sharing the findings, we decided to explore other options to create a better experience and to match customers' language. We went through different approaches, and we ended up doing a step by step, or no, not a step by step, but an order list of actions that users could perform in a dataset. While doing that, we realized that the best or the most useful way, or technical way to do it, was using SQL, which was the language we used to translate the JSON file. But I also discovered that users don't think in SQL. They are used to Excel formulas. So I also proposed to go with something similar to Excel. We already had some functions and specific language for modeling. So the solution was matching some of those functions and expanding them in the Dataset Manager. I also shared with the PM and the lead engineer that meant the project was going to get more complex and longer in time, but in the end we decided that that was the best decision for the user. So we took this approach, and we made it in several iterations. This way we could release stuff without blocking the users.

## 2026-09-23T14:13:33.801Z — assistant

This gives us the missing decision and tradeoff. I understood that:

- You replaced direct JSON editing with an ordered list of actions users could perform on a dataset.
- SQL made sense technically, but users were more familiar with Excel formulas.
- You proposed reusing and extending functions from the platform’s existing modeling language.
- The team accepted the additional complexity and delivered the solution in several iterations.

Your individual contribution is clearer here: **you identified the language mismatch and proposed building on familiar functions.** Exploring options and choosing the approach were shared work.

I became unsure about how JSON, SQL, and formulas related to each other. For a recruiter answer, that technical explanation probably needs only one point: users needed familiar language to work with their data. Keep the distinction between an ordered list of actions and a wizard; you don’t need to recount your search for the right phrase.

We now have the change, but not yet the user outcome. Releasing in iterations tells me how you delivered it. “Without blocking users” needs a concrete explanation.

**What evidence did you have, from testing or after release, that users could understand or complete the work more easily?** Qualitative observations are fine; we don’t need a metric if you don’t have one.

## 2026-09-25T07:32:07.052Z — user

Can you write the three short story cards?

## 2026-09-25T07:32:26.883Z — assistant

Here are three short cards for the **Dataset Manager story**. Use the bold phrases as memory cues.

:::writing{variant="standard" id="85319"}
### 1. Problem → initial idea
I was the first designer in the integrations squad. We wanted users to manage their datasets more independently, but editing JSON made that difficult. Our first idea was to add a visual interface so users could edit the data more easily.

### 2. Research → change of direction
When I tested that approach with users, they still got stuck. I found that the problem also involved our terminology: it didn’t match how they thought about their work. I shared those findings with the PM and lead engineer, and we explored a different approach.

### 3. Familiar language → shared decision
We designed an ordered list of actions users could apply to a dataset. SQL made sense technically, but users were familiar with Excel formulas. I proposed reusing and extending functions from our existing modeling language. We knew this would make the project longer and more complex, but agreed to take that direction and deliver it in several iterations.
:::

The ending still needs **what you observed in testing or after release**. These cards explain your contribution and the team’s decision; they don’t yet establish that users found the result easier.

## 2026-09-25T07:34:27.816Z — user

No, in the datavant-recruiter-screen.md file there's a section called "prepare 3 short story cards" with tdifferent prompt families. CAn you prepare those 3 stories?

## 2026-09-25T07:34:30.635Z — assistant

I’ll read that section and the supporting evidence, then prepare the three stories it calls for.

## 2026-09-25T07:35:24.185Z — assistant

I misunderstood: you meant three different examples. I’ve now read the [Datavant preparation file](/Users/manel/Dev/career-os/interviews/datavant-recruiter-screen.md) and its supporting notes. They also contain the Dataset Manager outcome I should have checked earlier.

Each card follows the requested four cues, with wording you can practise aloud.

:::writing{variant="standard" id="72641"}
### 1. Complex problem / research changed my design
**Dataset Manager — JSON → testing → familiar language**

- **Situation:** At Abacum, finance users struggled to configure datasets because they had to work with JSON. We wanted them to do more independently.
- **My responsibility:** I led the design and customer testing as the first designer in the integrations squad.
- **Action and rationale:** Our first idea was to make the JSON easier to edit through a visual interface. But in testing, users still got stuck. I found that our language didn’t match how they thought about their work. I brought this to the PM and lead engineer. We changed direction toward an ordered list of actions, and I proposed extending our existing formula language because users were familiar with Excel.
- **Result:** We delivered it in iterations. The implementation team’s recollection was that standard configuration took roughly half the previous time, and customers could reach a working configuration in their first session. That was qualitative feedback, not instrumented measurement.
:::

:::writing{variant="standard" id="72642"}
### 2. Disagreement / influencing others / a tradeoff
**Abax — capacity concern → bounded test → production component**

- **Situation:** At Abacum, we had repeated interface problems across five squads. Engineering was concerned that investing in a design system would take capacity away from product work.
- **My responsibility:** I co-led the business case with the Head of Design. We needed an approach that accounted for that capacity concern.
- **Action and rationale:** We compared two options: a smaller team working alongside sprints over two weeks, or a larger team working for one dedicated Maker Days week. We chose the dedicated week as a bounded production test. It concentrated the staffing cost, but gave us a concrete way to test whether the system could work in the product.
- **Result:** The first Button component reached production and proved the path from design to code. We then shifted attention toward usable components and missing variants. The outcome I can point to is what shipped; we didn’t measure a financial return.
:::

:::writing{variant="standard" id="72643"}
### 3. Mistake / learning from failure
**Remuner — wrong assumption → outage → recovery and safeguards**

- **Situation:** At Remuner, I deleted a design-token file because I thought it was a duplicate. The app still depended on it, and the next deployment caused a short production outage.
- **My responsibility:** I made the mistaken assumption and deleted the file. That was my mistake.
- **Action and rationale:** I recovered the file and pushed a fix. Afterward, I introduced a check before token-repository deployments. The team also moved the dependency so the file could be removed safely.
- **Result and learning:** We recovered from the outage and changed both the deployment check and the dependency. I learned that a design-token repository feeding a live product needs the same care as other production code. A file looking redundant isn’t enough evidence that it is safe to delete.
:::

The Abax and Remuner cards follow the [recorded incident notes](/Users/manel/Dev/career-os/interviews/spendesk-hiring-manager.md:80). **Check that their details match your recollection before using them**, especially the staffing decision and recovery sequence.

