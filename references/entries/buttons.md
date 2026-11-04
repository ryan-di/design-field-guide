# Button hierarchy

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 21 · Actions
Live: https://ryan-di.github.io/design-field-guide/#buttons
Kind: component
Cite as: Design Field Guide v35, #buttons

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A button starts an action: save, send, pay, delete. Its style shows how important that action is, so people can find the main step without reading every label.

That is what separates it from a [link](https://ryan-di.github.io/design-field-guide/#link-vs-button), which takes people to another page or place. A button does something where they are.

## Forms

Buttons come in three styles, set by how important the action is: primary, secondary and tertiary. A fourth, destructive style marks actions that delete or lose something.

- **Primary.** Use it for the one main action on a screen or in a dialog, like Pay.
- **Secondary.** Use it for other likely actions next to the main one, like Save for later beside Add to bag.
- **Tertiary.** Use it for rare or low-stakes actions, like Not now or Show more.
- **Destructive.** Use it for actions that delete or lose something, like Delete photos.

## Rules

Four rules keep buttons useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Keep one primary button

https://ryan-di.github.io/design-field-guide/#buttons-rule-1

When two buttons are filled, neither one stands out, and people have to read both labels before they know which one takes them forward. Give each screen or dialog one filled button for the main step, and make the others secondary or tertiary, so they’re still there but quieter.

### 2. Say what the button does

https://ryan-di.github.io/design-field-guide/#buttons-rule-2

As with [dialog buttons](https://ryan-di.github.io/design-field-guide/#dialog), OK, Yes and Cancel only make sense next to the question: during an upload, “Cancel” could mean stop the upload or close the question. Use a verb and an object, like “Stop upload”, so each button makes sense on its own.

### 3. Set the risky action apart

https://ryan-di.github.io/design-field-guide/#buttons-rule-3

People press familiar buttons by habit, often by where they sit, so if Delete looks like Save and sits where Save usually goes, one quick click removes a folder and all its files. Make the destructive button red and move it away from the main button’s spot. Where you can, let people undo it instead of asking them to be careful.

### 4. Explain why it won’t work

https://ryan-di.github.io/design-field-guide/#buttons-rule-4

A grayed-out button shows that something is missing, but not what, and when every field looks filled in, people recheck the whole form or give up. Keep the button enabled, and when it’s pressed, say what’s missing and move the cursor there. Or show the reason next to the button before it’s pressed.

## In real products

Notice how each screen has one strong action, and how the risky one is set apart and named for what it does.

- Gmail: in the compose window, Send is the only filled button. Formatting tools are small icons, and discarding the draft is a trash icon at the far end, away from Send. `buttons-example-01`
- Airbnb: the booking card has one wide, filled Reserve button, and a short note under it says nothing is charged yet. `buttons-example-02`
- GitHub: deleting a repository sits in a red-bordered Danger Zone at the bottom of settings. The final button names the action and only works after you type the repository’s name. `buttons-example-03`
- iOS Photos: deleting a photo opens a sheet with a red Delete Photo button, and Cancel sits apart in its own block. `buttons-example-04`

## Related entries

[dialog](dialog.md), [link-vs-button](link-vs-button.md)
