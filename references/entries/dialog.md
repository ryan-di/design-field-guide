# Dialog

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 19 · Dialogs & panels
Live: https://ryan-di.github.io/design-field-guide/#dialog
Kind: component
Cite as: Design Field Guide v35, #dialog

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A dialog is a box that opens over the page and asks the person something. The page behind it is dimmed and can’t be used until they answer. Use it for a decision they have to make before they go on, such as deleting something for good.

A [popover](https://ryan-di.github.io/design-field-guide/#popover) also opens over the page, but a click anywhere else closes it.

## Forms

Dialogs come in four common forms, set by what they ask for: a confirmation, a choice about unsaved work, a short form and a notice. They differ in how many buttons they have and which button gets focus first.

- **Confirm.** Use it before an action that can’t be undone.
- **Unsaved work.** Use it when people close something with changes they haven’t saved.
- **Short form.** Use it to ask for one or two things that belong to one action, like a new name.
- **Notice.** Use it only when people can’t go on without knowing, like after they’ve been signed out.

## Rules

Five rules keep dialogs useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Don’t use it for news

https://ryan-di.github.io/design-field-guide/#dialog-rule-1

People open an app to do something, like read their mail, so a box with news or a tip stands in their way, and most close it without reading. Put the news where people can open it when they want, such as a “What’s new” entry or a short note they can close. They can read it now, later or never, and the mail works right away.

### 2. Offer Undo instead of asking

https://ryan-di.github.io/design-field-guide/#dialog-rule-2

If every action asks “Are you sure?”, people learn to press OK without reading, so the one time it matters, the dialog doesn’t protect them. Let actions that can be undone happen at once, and offer Undo. Keep the dialog for the rare action that can’t be undone, and say what will be lost.

### 3. Give long tasks a page or a panel

https://ryan-di.github.io/design-field-guide/#dialog-rule-3

A dialog is a small box that covers the page, so a long form inside it hides what people need to look at, like the chart behind it. To check a number they have to close the dialog, and they lose what they typed. A page or a side panel gives them room to scroll and look things up, and keeps what they entered.

### 4. Name the action on each button

https://ryan-di.github.io/design-field-guide/#dialog-rule-4

“OK” and “Cancel” don’t say what will happen. When someone leaves a photo they were cropping, “Cancel” could mean cancel the crop or cancel leaving, so people have to read the whole question, and many guess wrong. When each button names its action, the buttons alone answer the question, and the one that throws work away stands out.

### 5. Don’t open it on load

https://ryan-di.github.io/design-field-guide/#dialog-rule-5

A dialog that opens with the app stands between people and what they came for. They haven’t done anything yet, so they close it unread. Ask at the moment it matters, like after they press Download, when the question is about what they just asked for and they read it.

## In real products

Notice which actions get a dialog at all, and that the buttons say what will happen.

- macOS: when an app asks before closing a document with unsaved changes, the buttons say Save, Don’t Save and Cancel, so people can answer without reading the message. `dialog-example-01`
- GitHub: deleting a repository can’t be undone, so the dialog spells out what will be lost and asks people to type the repository’s name before the delete button works. `dialog-example-02`
- WhatsApp: deleting a message you sent asks who it should disappear for. Each button names its outcome, so the choice is clear without any extra text. `dialog-example-03`
- Gmail: archiving or deleting an email doesn’t ask first. It happens at once, and a toast in the corner offers Undo for a few seconds. `dialog-example-04`

## Related entries

[popover](popover.md)
