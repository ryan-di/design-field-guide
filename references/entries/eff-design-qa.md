# Design QA

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 30 · Check it with evidence
Live: https://ryan-di.github.io/design-field-guide/#eff-design-qa
Kind: workflow
Cite as: Design Field Guide v35, #eff-design-qa

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Design QA means checking a change everywhere people will see it before it ships: in light and dark, on narrow and wide screens, and in every state it can be in. An agent can render all of those and list what looks wrong much faster than you can. You still read the list, open the important findings yourself and decide what to fix.

The agent does the looking, which is slow and easy to skip, and you keep the judgment that tools lack: what matters to people, and what is a false alarm.

## Rules

Four rules keep design QA useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Check every theme and width

https://ryan-di.github.io/design-field-guide/#eff-design-qa-rule-1

You build in your own theme on your own screen, so that’s where the change looks right. Other people use dark mode and phones, and that’s where text goes faint and buttons get cut off. Have the agent take screenshots in light and dark, at 360px and at a desktop width, every time. It takes the agent seconds.

### 2. Render every state

https://ryan-di.github.io/design-field-guide/#eff-design-qa-rule-2

The state you designed is usually the one that works. Problems hide in the others: while it loads, when it fails, when a name is long. List every state the change can be in, and have the agent render each one with [real, messy data](https://ryan-di.github.io/design-field-guide/#good-edge-cases), because it is longer than the sample.

### 3. Open the findings yourself

https://ryan-di.github.io/design-field-guide/#eff-design-qa-rule-3

An agent can misread a screenshot, or flag something that is meant to look that way. If you apply every finding without looking, you can break what was right. Open at least two findings yourself and check them against the brief. Dismiss the wrong ones and say why.

### 4. Test with the keyboard yourself

https://ryan-di.github.io/design-field-guide/#eff-design-qa-rule-4

An automated scan checks things like contrast and missing labels, but it can’t tell whether the focus moves in a sensible order, or whether a screen reader reads the page in a useful way. Tab through the change once and try a screen reader once. Only then call it accessible.

## In real products

Notice that the tool renders every state, theme or size and points at what changed or failed, but a person makes the call.

- Chromatic: every Storybook story is captured on each change, in the browsers and widths you choose, and changed snapshots wait for a person to accept or deny them. `eff-design-qa-example-01`
- Xcode: SwiftUI previews have a variants mode that shows one screen in each color scheme, orientation or text size, side by side. A label that only breaks at the largest text size is in view while you work. `eff-design-qa-example-02`
- Lighthouse: besides what a tool can measure, the accessibility audit lists items to check by hand, like a sensible tab order, because a scan can’t judge them. `eff-design-qa-example-03`
- Chrome DevTools: device mode resizes the page to a phone width, and the Rendering panel can switch it to dark mode or reduced motion. You can confirm a finding yourself in seconds, without a phone or a change to system settings. `eff-design-qa-example-04`

## Related entries

[good-edge-cases](good-edge-cases.md)
