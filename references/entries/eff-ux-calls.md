# UX calls

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 29 · Build in small, reviewable steps
Live: https://ryan-di.github.io/design-field-guide/#eff-ux-calls
Kind: workflow
Cite as: Design Field Guide v35, #eff-ux-calls

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Every change people will see is a design decision: the wording, the spacing, which kind of dialog appears. An agent makes these choices for you if you let it, so treat each one as a proposal: decide on it, then name it in the pull request.

This keeps the decisions with the people who own them. When the pull request describes each visible change, reviewers can judge it, but a change it doesn’t mention gets approved without anyone deciding on it.

## Rules

Four rules keep these calls visible. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Decide on each visible choice

https://ryan-di.github.io/design-field-guide/#eff-ux-calls-rule-1

An agent fills every gap with a default: generic wording, the nearest dialog, a button that says OK. Each default looks reasonable on its own, so it ships without anyone choosing it. List the choices people will see and decide on each one: keep it, change it or drop it.

### 2. Keep side changes out

https://ryan-di.github.io/design-field-guide/#eff-ux-calls-rule-2

Agents often change things on the way: a font size, a color, a label in another screen. Buried in a bigger pull request, these changes ship without review, because the description doesn’t mention them. Drop them, or move them into their own pull request with their own note.

### 3. Lead with what people will notice

https://ryan-di.github.io/design-field-guide/#eff-ux-calls-rule-3

Reviewers and teammates read the first lines of a description. If those lines list files and functions, they have to work out from the code what changes for people. Start with what people will notice, in their words, and put the code notes under it.

### 4. Check before saying “no visible change”

https://ryan-di.github.io/design-field-guide/#eff-ux-calls-rule-4

Refactors and shared components often change how things look by a few pixels or a color, and saying “no visible change” without checking hides that from reviewers. Compare screenshots from before and after, and skim the diff for new strings, styles and components. If anything differs, describe it as a visible change.

## In real products

Notice that each change people will see is shown on its own, in plain words, where someone can decide on it.

- Google Docs: in Suggesting mode, each edit shows up marked in the text with its own accept and reject. Nothing changes for good until someone decides, one edit at a time. `eff-ux-calls-example-01`
- GitHub: a repo can add a pull request template, so every description starts from the same sections. Teams use it to put what people will see, with before and after screenshots, above the code notes. `eff-ux-calls-example-02`
- App Store: every app update comes with a “What’s New” note. The good ones name each change people will notice, in plain words, instead of “bug fixes and improvements”. `eff-ux-calls-example-03`
