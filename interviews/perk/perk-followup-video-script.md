# Perk: follow-up video script (record 2026-11-18)

For Tim and Mateo, sent through Clare with the follow-up email. Answers Tim's "a component you elevated visually or with motion" from the [Hiring Manager Interview](perk.md#round-2-debrief-hiring-manager-interview-tue-2026-11-17). About 2 minutes. The docs-from-one-source answer goes in the email text, not the video.

Material:
- Table rebuild: [perk-table-selection-rebuild.html](perk-table-selection-rebuild.html), recorded at real size (Cmd+Shift+5, "Record Selected Portion" around the table and label).
- 2023 spec board: Figma "Abacum | Abax Components | Exploration", page "✅ 2306 -> Table cells", board "Table - Cell".
- Remuner pairs: Figma "Remuner | Dashboard (IC)", page "Before-after for Perk (2026-11-17)".

Claim limits: [evidence/experience-facts.md](../../evidence/experience-facts.md), table selection entry and its AG Grid line. Designed and prototyped, never "shipped". What exactly was poor in AG Grid's default is not recorded, so the script doesn't say.

Open before recording: confirm that "Dashboard (before)" is the production dashboard you inherited in May 2024. If it isn't, cut the "I inherited" sentence.

## Opening (about 15 seconds)

Hi Tim, hi Mateo.

Thanks for Tuesday's conversation, I really enjoyed it.

I was reflecting on it afterwards, and there's one answer I'd like to complete.

Tim, you asked me for a component I'd improved visually or with motion.

I didn't have one ready to show, so I've recorded two.

## Table selection, Abacum (about 60 seconds)

▶ Show the 2023 "Table - Cell" board.

The first one is from Abacum, in June 2023.

Our data tables ran on AG Grid.

AG Grid comes with a default range selection, and I wanted to improve on it.

These are my spec boards from then.

The original prototype is lost, so I rebuilt it in code from these specs.

▶ Switch to the rebuild. Hover across a few cells.

The highlight follows the mouse.

The row and column indicators follow it too, so you can see where you are in a big table.

▶ Click a cell, then drag the bottom-right handle down and across.

A click selects the cell, and you drag the handle to expand the range.

▶ Move to the top edge of a column, then onto the indicator. Click.

Each column header has three hover zones: the cell, the column and the indicator.

A click on the indicator selects the whole column.

Rows work the same way, from the left edge.

▶ Switch to "Drag & drop". Drag a column, then a row.

With drag and drop on, the indicator becomes a handle.

You drag a column or a row, and a blue line shows where it'll land.

▶ [If asked about the drag] The handles and their states are from my 2023 specs. The drag itself followed Notion's table pattern.

## Remuner before and after (about 40 seconds)

▶ Show the "Dashboard (before)" frame, then the "after" frame.

The second one is from Remuner, where I built the design system on my own.

This is the dashboard I inherited in May 2024.

And this is the same dashboard after the work on the system.

▶ Show the personal target card pair, then commissions card to earnings widget.

▶ [Fill in before recording: one sentence per pair on what you changed and why. Use only what you can point at on screen.]

I also rebuilt the colour ramps and brought the colours we use in the app up to WCAG AA contrast.

Our CTO said it went from a 2010 app to a 2025 app.

## Close (about 10 seconds)

I've also written a short answer on documentation from one source, Tim. It's in the email.

Thanks again, and I'm happy to walk you through any of it in Figma.
