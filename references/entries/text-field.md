# Text field

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 20 · Inputs
Live: https://ryan-di.github.io/design-field-guide/#text-field
Kind: component
Cite as: Design Field Guide v35, #text-field

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A text field is a box where people type their own words: a name, an address, a message, a search. A label above it says what goes in, and hints and errors appear below it.

That is what separates it from a [picker](https://ryan-di.github.io/design-field-guide/#picker), which offers only valid values, like the days on a calendar. A text field accepts anything people type, so it has to say what it expects and help when the text doesn’t fit.

## Forms

Text fields come in four common forms, set by what people type. A single line holds a short value, like a name or an email. A multi-line box holds longer text, like a message. Search and password fields are single lines with a control of their own.

- **Single line.** Use it for a short value, like a name or an email.
- **Multi-line.** Use it for text that runs past a sentence, like a message.
- **Search.** Use it to find things in a list or a whole app.
- **Password.** Use it for a secret that shouldn’t show on screen, like a password or a PIN.

## Rules

Four rules keep text fields useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Say back what you understood

https://ryan-di.github.io/design-field-guide/#text-field-rule-1

Some values can be written in more than one way: “12/11” is 11 December in the US and 12 November in most other places. If the field guesses without saying so, people find out at the hotel desk. Use a picker for values like this, or read the typed text back in words and ask when it could mean two things.

### 2. Keep the label visible

https://ryan-di.github.io/design-field-guide/#text-field-rule-2

A placeholder disappears as soon as there’s text in the field, and after that nothing on screen says what the field is for. People can’t check a filled form without clearing it, so a value in the wrong field gets through. Put the label above the field, where it stays while people type.

### 3. Show long text in full

https://ryan-di.github.io/design-field-guide/#text-field-rule-3

In a small fixed box, people only see a slice of what they wrote, so they can’t reread it before they post. If typing also stops at a hidden limit, the end of their text is lost. Use a box that grows as they write, and show a count when there is a limit.

### 4. Say how to fix it

https://ryan-di.github.io/design-field-guide/#text-field-rule-4

“Invalid username” has the same problem as [a bare “Invalid date”](https://ryan-di.github.io/design-field-guide/#inline-message): people can’t tell whether it’s the dot, the length or a name someone else has, so they change things at random. Say what’s wrong in plain words and offer a value that works, one click away.

## In real products

Notice how each field fits the text it holds: a label that stays, a box that grows, a count near the limit, and the value shown back the way it will be saved.

- Google sign-in: the field’s label sits inside the box, then moves up into the border once you type. Unlike a placeholder, it never disappears. `text-field-example-01`
- Slack: the message box grows line by line as you write, up to a set height, then scrolls. Short messages stay compact and long ones stay readable. `text-field-example-02`
- YouTube Studio: the title and description fields show a running count against their limits, like 31/100. People see the limit before they hit it. `text-field-example-03`
- GitHub: if a new repository name has spaces or other characters it can’t use, the form shows the name it will create instead, like portrait-tools. People see the fix, not just an error. `text-field-example-04`

## Related entries

[inline-message](inline-message.md), [picker](picker.md)
