# Explore wide

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 27 · Explore wide before you narrow
Live: https://ryan-di.github.io/design-field-guide/#eff-explore-wide
Kind: workflow
Cite as: Design Field Guide v35, #eff-explore-wide

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Before you build one answer, ask for several different ones. Give each direction its own short brief and its own subagent (a helper agent that works alongside the others), then lay the results side by side and choose. With agents a rough direction costs minutes, so the first idea doesn’t have to be the one you build.

How the directions should differ, so that each one teaches you something, is the subject of [Vary along named axes](https://ryan-di.github.io/design-field-guide/#eff-axes).

## Rules

Four rules keep exploring wide useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Ask for several at once

https://ryan-di.github.io/design-field-guide/#eff-explore-wide-rule-1

If you ask one agent for one answer, you get the obvious idea, and every round of polish after that makes the same idea neater, not better. Ask for several directions at the same time instead: one subagent per direction, or one git worktree (a separate working copy of the code) each when a direction needs real code.

### 2. Give each one its own bet

https://ryan-di.github.io/design-field-guide/#eff-explore-wide-rule-2

Agents given the same prompt tend to land on the same answer, so you get three versions of one idea, differing only in wording or layout, and think you’ve explored. Write each brief around a different bet about what people need, such as “never interrupt” or “make it fixable in one step”. If two results still differ only in layout, rewrite one brief with a different bet.

### 3. Keep them equally rough

https://ryan-di.github.io/design-field-guide/#eff-explore-wide-rule-3

When one direction looks finished and the others are sketches, the finished one wins, and you end up choosing the polish, not the idea. Ask for every direction at the same level of detail, so the only difference left is the idea.

### 4. Set the number first

https://ryan-di.github.io/design-field-guide/#eff-explore-wide-rule-4

Asking for “a few more” has no natural end. The pile grows, each new card adds less, and nothing gets chosen. Decide before you start how many directions to ask for, say three to six, then keep two or three and drop the rest.

## In real products

- Google Ventures: in the design sprint’s Crazy 8s step, each person folds a sheet into eight panels and sketches eight ideas in eight minutes. The time limit keeps every idea rough, so people compare ideas, not drawing skill. `eff-explore-wide-example-01`
- Lightroom Classic: a virtual copy is a second edit of the same photo, without duplicating the file. Survey view shows the copies side by side, so you remove the weak ones and keep the best. `eff-explore-wide-example-02`
- Midjourney: each prompt returns a grid of four different images at once. You pick the ones worth taking further and ask for variations or a larger version of just those. `eff-explore-wide-example-03`
- Google Maps: directions show a few different routes at once, each with its time on the map. You see the trade-offs side by side and tap the one you want, instead of taking the first answer. `eff-explore-wide-example-04`

## Related entries

[eff-axes](eff-axes.md)
