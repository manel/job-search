# Remuner design-system case: drafted additions (2026-10-20)

Target file: `portfolio/public/cases/design-system-remuner.html` (submodule: edit there, commit there, then update the pointer here; ask Manel before pushing, a push may deploy the live site).
Status: DRAFT, awaiting Manel's approval. Facts from Manel's answers on 2026-10-20, recorded in `evidence/experience-facts.md` (Design system and token pipeline: Figma MCP examples). Run no-ai-slop and humanizer again after any edit.

Limits from the register: say WCAG AA (never AAA), no named failing colours, no PR counts, no claim that engineers adopted the Storybook views.

---

## A. New section, after "Adapting the output to the team's existing conventions"

## Making the palette consistent and accessible

I built the colour palette by hand, setting each shade by eye, so I couldn't be sure the steps between shades were consistent across hues. I used the Figma MCP to convert the palette to HSL, compare the steps colour by colour, and normalise them so every hue followed the same progression.

Then I ran contrast checks on the result. Some pairings failed, and I adjusted the ones the product used until they met WCAG AA. The changes went through the tokens repository, which the front end consumes as a submodule, so the corrected values reached the app as soon as engineers pulled the update.

## B. Append to "The ongoing product audit"

Some fixes I made myself. Where the audit found hardcoded styles or missing tokens in the front-end code, I fixed part of them with Claude in small changes and opened PRs to the app repository for the engineers to review.

## C. Append to "The token pipeline and its evolution"

I also used the Figma MCP, first with Codex and then with Claude, to keep Figma and code aligned. I generated component variants with props named to match the engineering components, and a Storybook view per component with a props grid covering every state and variant, which I used to find and fix inconsistencies. The component documentation came out of the same workflow.

## Stack row

Add: Storybook, Codex, Claude, Figma MCP.

## Open

- Optional visual for A: before and after of the palette ramps in HSL, or the contrast results. Ask Manel whether Figma has anything usable.
