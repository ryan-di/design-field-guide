# Interaction states

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 24 · States
Live: https://ryan-di.github.io/design-field-guide/#interaction-states
Kind: component
Cite as: Design Field Guide v35, #interaction-states

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Interaction states are the different looks one control takes as people use it: hover, focus, pressed, selected, disabled, loading, and the result after. Each state tells people something they need in that moment: that the control reacts, that it heard the click, that it’s working, or that it’s done.

A state lives on the control itself, so people see it exactly where they acted. A message, like a [toast](https://ryan-di.github.io/design-field-guide/#toast) or an [inline message](https://ryan-di.github.io/design-field-guide/#inline-message), is for anything that needs more words than a control can hold.

## Forms

States fall into four kinds, by what they report. Hover and pressed follow the pointer, focus shows where the keyboard is, selected shows what’s chosen, and disabled and loading say what the control can do right now.

- **Hover and press.** Use them on anything people can click: hover says it reacts, and pressed says the click landed.
- **Focus.** Use it to show which control the keyboard is on. It moves with Tab.
- **Selected.** Use it to show what’s chosen or switched on, like photos picked for sharing.
- **Disabled.** Use it when a control can’t work yet, like Continue before there’s an amount.
- **Loading.** Use it when an action takes more than a moment, like exporting a file.

## Rules

Four rules keep interaction states useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Design every state, not just the default

https://ryan-di.github.io/design-field-guide/#interaction-states-rule-1

A button that looks the same while it sends, after it fails and when there’s nothing to send gives people no answer, so they press again or give up. Give each state its own look and words, such as “Sending…”, “Sent” and “Retry”. Before building, list every state (default, hover, focus, pressed, disabled, loading, error, success) and check each one in the browser.

### 2. Say why it’s off

https://ryan-di.github.io/design-field-guide/#interaction-states-rule-2

A disabled control shows that people can’t act, but not why, so they check every field and guess. Put the reason right next to it, or keep it enabled and explain when it’s pressed, the same fix as for [a disabled button](https://ryan-di.github.io/design-field-guide/#buttons).

### 3. Keep the focus ring

https://ryan-di.github.io/design-field-guide/#interaction-states-rule-3

Without a focus ring, keyboard users can’t see which button they’re on, so they press Enter and hope. As in [Keyboard and focus](https://ryan-di.github.io/design-field-guide/#good-keyboard-focus), restyle the ring to fit the design instead of removing it. `:focus-visible` shows it only when people use the keyboard, so it never shows on mouse clicks.

### 4. Block the second click

https://ryan-di.github.io/design-field-guide/#interaction-states-rule-4

If a button still works while it’s loading, a nervous double-click places two orders. Once it’s pressed, ignore repeat clicks and show that it’s working. Keep its width fixed too, because a button that grows to fit “Placing your order…” moves the buttons next to it, like [content that loads late](https://ryan-di.github.io/design-field-guide/#good-edge-cases).

## In real products

- Figma: hovering a layer draws a thin outline; selecting it adds handles and its size. “I’m pointing at it” and “I’ve picked it” never look the same. `interaction-states-example-01`
- YouTube: Subscribe is a strong filled button; once pressed it becomes a quieter Subscribed button. The color and the label both say which state you’re in. `interaction-states-example-02`
- Spotify: hovering a track swaps its number for a play icon, and the playing track is highlighted with small moving bars. The main button shows pause while music plays. `interaction-states-example-03`
- Slack: the send button stays dimmed while the message box is empty and turns on as soon as you type. The reason it’s off is right there: there’s nothing to send. `interaction-states-example-04`

## Related entries

[buttons](buttons.md), [good-edge-cases](good-edge-cases.md), [good-keyboard-focus](good-keyboard-focus.md), [inline-message](inline-message.md), [toast](toast.md)
