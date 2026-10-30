# Abacum design-system case: drafted changes (2026-10-30)

Target file: `portfolio/public/cases/design-systems.html` (submodule: edit there, commit there, then update the pointer here; ask Manel before pushing, a push may deploy the live site).
Status: APPLIED 2026-10-30 (portfolio commit f3d4c47, pushed). C placed after the issue-reporting paragraph; detach follow-up confirmed by Manel 2026-10-30. Facts from Manel's answers on 2026-10-30, recorded in `evidence/experience-facts.md` (Abax design system, Abax measurement). Run no-ai-slop and humanizer again after any edit.

Limits from the register: no Figma figures, trends or detach counts (not recoverable); say "a script", not REST API or plugin; "likely detaches", since they were matched by name; never "80% of new UI" or "47% of new UI".

---

## A. Replace in "Deciding how the work would run"

Current: "Vision 1.0 set two targets before the sprint started. New UI would need to reach 80% built from Abax components, and legacy MUI components would be fully deprecated everywhere an Abax equivalent existed."

New: "Vision 1.0 set two targets before the sprint started. Abax would reach 80% of the component uses in the codebase, growing every time a squad reworked a screen, iterated on it, or built a new feature. Legacy MUI components would be fully deprecated everywhere an Abax equivalent existed."

## B. Replace the first outcome paragraph

Current: "At departure, Abax accounted for approximately 47% of tracked Abax and MUI component uses across the codebase. The separate target was for 80% of new UI to use Abax."

New: "At departure, Abax accounted for approximately 47% of tracked Abax and MUI component uses across the codebase, against the 80% target."

## C. New paragraph, append to "Making adoption stick" (after the ESLint paragraph)

We tracked adoption on both sides. In code, the front-end engineers ran a monthly script that counted every Abax and MUI component use. In Figma, I ran a script every week on the frames marked ready for dev. It measured how many layers were Abax instances, and it flagged layers named like an Abax component that weren't instances, which usually meant someone had detached one. Those flags fed the issue reports, where the "detached instances" category told us why.

## Open

- Paragraph C's last sentence links the script to the issue category. Confirm with Manel that detaches flagged by the script were followed up through the issue process before publishing it.
