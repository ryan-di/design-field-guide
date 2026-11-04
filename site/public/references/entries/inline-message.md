# Inline message

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 16 · Feedback & status
Live: https://ryan-di.github.io/design-field-guide/#inline-message
Kind: component
Cite as: Design Field Guide v35, #inline-message

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

An inline message is a short line of text right next to the thing it’s about. Most often it sits under a form field and says what’s wrong and how to fix it. It can also give a hint before people type, or point out a value that looks like a mistake.

Where a banner is about the whole page or app, an inline message is about one field or one item, and it sits right beside it.

## Forms

Inline messages come in four kinds: a hint, an error, a warning and a success note. A hint is there before people type. The other three respond to what they typed, and only an error stops them from going on.

- **Hint.** Use it to say what a field needs before people type.
- **Error.** Use it when a value can’t be accepted and people must change it to go on.
- **Warning.** Use it when a value is allowed but may be a mistake.
- **Success.** Use it only when people wait to learn whether a value works, like a free username.

## Rules

Four rules keep inline messages useful.

### 1. Bring the problem to where people look

https://ryan-di.github.io/design-field-guide/#inline-message-rule-1

After a failed submit, the message often sits next to a field that has scrolled out of view, so people see nothing change near the button and press again or give up. Add a short summary at the top of the form that lists each problem, links to its field and gets focus when the form is sent.

### 2. Give each field one next step

https://ryan-di.github.io/design-field-guide/#inline-message-rule-2

When every check adds its own red line, the form turns into a wall of errors: people can’t tell what to fix first, and several lines say the same thing. Show only the most useful message for each field. If something is still wrong after they fix it, the next message appears then.

### 3. Wait until people leave the field

https://ryan-di.github.io/design-field-guide/#inline-message-rule-3

An error that appears on the first key press tells people they’re wrong before they’ve finished, when they’re only not done yet. Check the value when they leave the field or send the form, and if a message is already showing, clear it as soon as the value is right.

### 4. Say what to do instead

https://ryan-di.github.io/design-field-guide/#inline-message-rule-4

“Invalid date” says that something is wrong, but not which date or why, so people guess and often change the wrong field. A good message names the field and the rule in plain words, and offers the fix as a button when it’s obvious.

## In real products

- VS Code: a squiggle marks the exact spot, and hovering it shows the message. A count in the status bar opens the full Problems list, so the markers stay small and one list holds them all. `inline-message-example-01`
- Google: when a new account’s username is taken, the message appears right under the field and says what to do next. What you typed stays, so the fix is one edit. `inline-message-example-02`
- Stripe Checkout: the card number is checked when you leave the field, and the message under it says what’s wrong, like “incomplete”. You fix it before you press Pay, not after. `inline-message-example-03`
