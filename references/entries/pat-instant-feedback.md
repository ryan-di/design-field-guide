# Instant feedback

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 10 · Did it work?
Live: https://ryan-di.github.io/design-field-guide/#pat-instant-feedback
Kind: pattern
Cite as: Design Field Guide v35, #pat-instant-feedback

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Instant feedback means the screen answers an action right away: a pressed button changes, a ticked box shows a tick, a save says “Saving…”. People know their action registered, so they don’t click again or give up.

The work itself may take seconds, but the sign that it started should take less than a tenth of a second. Put the new state in text as well, so screen readers announce it too.

## Ways to do it

Feedback comes in four common strengths. The bigger or slower the action, the stronger the answer.

- **Pressed state.** Use it for most clicks. The control itself changes the moment it’s pressed, and nothing else is needed.
- **Status line.** Use it for work that runs in the background while people keep going, such as saving. A short status near the title says “Saving…”, then settles on “Saved” until the next change.
- **Change in place.** Use it when the action changes the thing on screen. The item shows its new state at once: the button reads “Following” and the count goes up.
- **Toast.** Use it when the result leaves the screen or matters more, such as archiving an email. The email is gone from view, so a short toast says where it went and offers Undo.

## Rules

Four rules keep feedback useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Leave the confirmation up long enough

https://ryan-di.github.io/design-field-guide/#pat-instant-feedback-rule-1

A confirmation that flashes by is gone before people look at it, so they’re left unsure and do the action again. Keep a short confirmation on screen for one to two seconds, or better, switch to a state that lasts, like “Saved just now”, until the next change.

### 2. Show it where the action happened

https://ryan-di.github.io/design-field-guide/#pat-instant-feedback-rule-2

People look at the thing they just clicked, so a change in a far corner of the screen goes unseen and they click again. Show the answer on the button, row or card that was used. A counter elsewhere can update too, as a second sign.

### 3. Match the strength to the action

https://ryan-di.github.io/design-field-guide/#pat-instant-feedback-rule-3

When every small action gets a toast, the toasts pile up and people stop reading them, so they miss the one that matters too. A changed control is enough for most clicks. Keep toasts and other strong signals for actions that matter or take a while.

### 4. Ignore repeat clicks while it works

https://ryan-di.github.io/design-field-guide/#pat-instant-feedback-rule-4

When a button gives no sign during a slow action, people click again, and each click can run the action again: two comments, two orders. While it works, say so on the button and ignore further clicks. Use aria-disabled instead of disabled, so keyboard focus stays on the button.

## In real products

- GitHub: the copy button on a code block turns into a check mark for a moment. The answer appears on the button that was just pressed. `pat-instant-feedback-example-01`
- Google Docs: next to the title, the status says it’s saving while you type, then settles on a saved state that stays until the next change. `pat-instant-feedback-example-02`
- Duolingo: pressing Check turns the bottom panel green or red right away, with a sound, and the same button becomes Continue. `pat-instant-feedback-example-03`
