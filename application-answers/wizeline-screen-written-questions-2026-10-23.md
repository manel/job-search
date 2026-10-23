# Wizeline: written questions after the recruiter screen (sent 2026-10-23)

Context: David Ho (recruiter) pasted three questions in the Meet chat at the end of the phone screen on 23 Oct 2026 and asked for answers by email in 15-30 minutes, written without AI. Manel wrote the answers himself; Claude gave feedback on structure, evidence and grammar only and did not draft text. Sent by email to David Ho on 2026-10-23, after the call. Verbatim as sent:

---

Hello David,

Thanks for the interview. Here are the answers for the questions you left. Let me know if you need something else.

Q1: "A product team is on a strict deadline and insists on building a custom UI solution because the current Design System component doesn't meet their specific edge case. How do you evaluate whether to enforce system consistency, build a new variant, or let them build custom—and how do you handle the resulting technical debt?"
A: I would first understand why this custom UI solution is needed, if this will be a recurring case or one-off and if it affects other teams. That would give me an understanding of the urgency which i'd use to decide priority. Then I'd check if there is a component that could cover that case. If so, I'd push for it. If not, I'd check if a new variant could cover this custom UI and help the team build it. If not and it's really blocking the release or a user need, then I would let them ship it and after that, add the task to the design system roadmap and prioritise it so the team can replace it when ready.

Q2: "You discover two different product teams are using wildly different, detached versions of a core data-table component. Walk me through your exact process for untangling this. How do you align the teams, deprecate the rogue versions, and roll out a unified component without breaking their workflows"?
A: I'd understand why neither team uses the core component. It could be a user need, could be a documentation problem or a discoverability problem. After that, I'd make clear what each team needs and how to support them. I'd need to check how much they drifted from the core component to understand what needs to be built. From there, I'd share a plan to unify and improve the current component and, depending on the complexity, a release plan to cover all the needs and replace all those components. As this component can be critical, I'd start releasing it under a flag so we can control and test how it behaves. Then I'd also track both teams' adoption rate for that component to check if it's working for them and see if I can deprecate the old versions.

Q3: "Translating visual design into scalable tokens and components is complex. Tell us about a time you had to balance high aesthetic craft with strict WCAG accessibility constraints and rigid front-end APIs. Where did you draw the line between visual perfection and technical reality?"
A: At Remuner I inherited a color palette and some shades that didn't meet the AA standard. For example, some texts or icons were barely visible on a white background. When I joined, one of the projects was making this pass the standard, so I adjusted the palette to match luminance and saturation, rebuilt the shades, ran contrast checks. It went from looking like a bunch of randomly chosen colors to having a harmonious palette. Some shades still didn't pass AA so I had to fix them although they looked a bit off. I planned to include these changes in each app release because we couldn't afford to fix them all at once. So I had to accept there would be inconsistencies until we covered all of them. I was the owner of the design tokens repo and one of the constraints that I found was having to export them as Sass variables and utility classes matching Vuetify conventions so they can use them the same way they were using the other classes.

Have a good weekend.

Thanks,
Manel Leiva

---

## Claims to keep consistent in later rounds

- Q3 is the Remuner palette story (`evidence/experience-facts.md`, palette consistency and contrast example). In a live round, the same facts: base colours inherited, shades rebuilt by eye then normalised (luminance and saturation), AA for in-use colours, some fixed shades looked off, fixes shipped section by section with feature releases, tokens exported as Sass variables and Vuetify-style utility classes.
- Q1 and Q2 are hypothetical process answers. If asked for an example: Remuner audit loop (fix now vs. defer to an upcoming feature change); Abax feature flags, squad-owned migration tickets, monthly Abax vs. MUI usage scripts.
