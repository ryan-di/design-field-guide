# Context pack

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 26 · Write the brief agents build from
Live: https://ryan-di.github.io/design-field-guide/#eff-context-pack
Kind: workflow
Cite as: Design Field Guide v35, #eff-context-pack

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A context pack is what a new teammate would need on their first day: design tokens, components to reuse, copy rules, examples of good screens, repo conventions and the design frames. An agent that doesn’t get these makes up its own, and the result may work but doesn’t look or read like the rest of the product.

Where the [problem brief](https://ryan-di.github.io/design-field-guide/#eff-brief) says what to solve, the context pack says how things are done here. Include the accessibility rules too: focus order, labels, and which color tokens pass contrast. An agent may skip rules that aren’t in the pack, and the gap only shows up in review.

## Rules

Four rules keep a context pack useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Point to the design system by path

https://ryan-di.github.io/design-field-guide/#eff-context-pack-rule-1

An agent doesn’t know your design system unless you show it where it lives, so it writes a new button with its own color, shape and focus style. Each one is small, but they add up to a product that looks patched together. Give the path to the token file and the components to reuse, and name the ones it must not rebuild.

### 2. Pick what this task touches

https://ryan-di.github.io/design-field-guide/#eff-context-pack-rule-2

Pasting the whole repo or every design page seems thorough, but the agent then has to guess which parts matter, and it may copy an old screen instead of the current one. The brief itself can get lost in the pile. Pick what this task touches: one or two similar screens, the frames for this flow, the rules that apply.

### 3. Show the look, don’t only describe it

https://ryan-di.github.io/design-field-guide/#eff-context-pack-rule-3

Words leave room for guessing: “a small image on the left” can mean many sizes and positions, and the agent picks one. Link the design frame instead, or attach a screenshot of a similar screen. Claude Code can read Figma frames through the Figma MCP connector (MCP is a standard way to plug tools into an agent).

### 4. Keep the stable parts in one file

https://ryan-di.github.io/design-field-guide/#eff-context-pack-rule-4

Tokens, copy rules and conventions rarely change between tasks. Pasting them into every request takes time, and sooner or later one part gets left out, so that task breaks a rule the others followed. Keep the stable parts in a file the agent reads every session, such as CLAUDE.md, the project notes file Claude Code loads on its own. Add only the task-specific parts to each brief.

## In real products

- Figma: Dev Mode shows a frame with its spacing, the variables and the components it uses. Whoever builds it gets the rules behind the pixels, not just a picture. `eff-context-pack-example-01`
- Storybook: every component has stories for its states and a docs page with its props. A newcomer, or an agent, can see what already exists before building something new. `eff-context-pack-example-02`
- Airbnb: hosts write check-in steps, Wi‑Fi details, house rules and a house manual once, and every guest who books gets them, like the stable part of a context pack. `eff-context-pack-example-03`

## Related entries

[eff-brief](eff-brief.md)
