# Chapter 29 · Build in small, reviewable steps

Design Field Guide v35 (2026-11) · Part 4 · Effective design
Live: https://ryan-di.github.io/design-field-guide/#ch-build
Cite as: Design Field Guide v35, #ch-build

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Plan before any code, then build in small steps that each end with a check. Agents can run most of the checks, but the calls on what people will see stay yours.

## Entries

- [Small steps](../entries/eff-small-steps.md): Before an agent writes code, agree on a plan with it, for example in Claude Code’s plan mode.
- [Agent checks](../entries/eff-agent-verification.md): When an agent says it’s done, ask it to show the proof: which unit tests ran, the end-to-end specs for the screens it changed, screenshots before and after, and a clean type check.
- [UX calls](../entries/eff-ux-calls.md): Every change people will see is a design decision: the wording, the spacing, which kind of dialog appears.
