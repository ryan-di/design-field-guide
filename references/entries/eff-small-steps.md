# Small steps

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 29 · Build in small, reviewable steps
Live: https://ryan-di.github.io/design-field-guide/#eff-small-steps
Kind: workflow
Cite as: Design Field Guide v35, #eff-small-steps

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Before an agent writes code, agree on a plan with it, for example in Claude Code’s plan mode. Then build one small change at a time, and check each change before the next one starts.

Small steps keep mistakes cheap: when a step fails review, only that step goes back. In one big change, a problem in one part sends the whole change back, and it’s harder to find.

## Rules

Four rules keep small steps useful.

### 1. Plan before code

https://ryan-di.github.io/design-field-guide/#eff-small-steps-rule-1

If you ask an agent to build a whole feature from one prompt, it makes every decision on its own, and you find the wrong ones in review, after the code is written. Ask for a plan first and read it, because changing a step in the plan takes a sentence, and changing it in code can take a day.

### 2. Slice so each step works

https://ryan-di.github.io/design-field-guide/#eff-small-steps-rule-2

Steps sliced by layer, such as database, then server, then screen, leave nothing to try until the last step lands. Problems then show up all at once, and nobody knows which step caused them. Slice so each step leaves the app working and gives you something to try. If a step can’t stand on its own, merge it behind a feature flag, a switch that keeps new code turned off for people, until the step that completes it lands.

### 3. Give every step a check

https://ryan-di.github.io/design-field-guide/#eff-small-steps-rule-3

Without a check, a step is “done” when the agent stops typing, so a broken step looks the same as a working one, and the next step builds on it. Write the check into the plan next to each step: a unit test, an end-to-end spec, a screenshot or you trying it. A step is done when its check passes.

### 4. Finish one step before the next

https://ryan-di.github.io/design-field-guide/#eff-small-steps-rule-4

Open questions about a step don’t go away when the next step starts. Later steps build on the answer, so a late answer can undo several steps of work. Finish the review of one step, open questions included, before the next one starts.

## In real products

Notice that each step is small, leaves things working, and gets checked before the next one builds on it.

- Basecamp’s Shape Up: a project is split into scopes, each a slice that works end to end. A hill chart shows each scope moving from “figuring things out” to “making it happen”, so a stuck one is easy to spot. `eff-small-steps-example-01`
- Google’s code review guide: each change should be small and do one self-contained thing. Small changes get reviewed faster and more carefully, and a bad one is easy to roll back. `eff-small-steps-example-02`
- LaunchDarkly: each step can merge behind a feature flag that’s off for most people, so the app keeps working in between. When the last step lands, you can turn it on for your team first, then a few percent of people, then everyone. `eff-small-steps-example-03`
- Duolingo: a course is a path of short lessons. Each takes a few minutes and opens the next one when you finish, so you always know where you are and never face a whole unit at once. `eff-small-steps-example-04`
