# Labels

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 4 · Treat the words as the interface
Live: https://ryan-di.github.io/design-field-guide/#good-labels
Kind: principle
Cite as: Design Field Guide v35, #good-labels

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A button label should say what happens when people press it: a verb, and the thing it acts on. “Save draft” and “Delete 3 photos” do that, and “OK” and “Yes” don’t.

Labels are the smallest case of [plain language](https://ryan-di.github.io/design-field-guide/#good-plain-language), and they matter more on a button, because pressing it changes something.

## Rules

Four rules keep labels clear. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Name the action, not the answer

https://ryan-di.github.io/design-field-guide/#good-labels-rule-1

“OK”, “Submit” and “Yes” only make sense next to the question above them. People who skim read the buttons first, and so do screen-reader users who jump between buttons, so they have to go back to the text to learn what a button does, or guess. Use a verb and an object, like “Delete draft”, so the button makes sense on its own.

### 2. Use people’s words

https://ryan-di.github.io/design-field-guide/#good-labels-rule-2

Words like “Execute query” describe what the code does, not what people want to do, so people stop to translate them and some give up. Use the words people use for their own tasks, like “Search” and “Add contact”. [Labels in people’s words](https://ryan-di.github.io/design-field-guide/#pat-information-scent) covers how to find those words.

### 3. Pick one capital style

https://ryan-di.github.io/design-field-guide/#good-labels-rule-3

When “Add To Cart” sits next to “Save for later”, the page looks like it was put together from different apps, and people notice the mismatch before they read the words. Pick one style and use it on every button, menu item and title. Sentence case is a common choice: only the first word and names get a capital.

### 4. Keep one verb per action

https://ryan-di.github.io/design-field-guide/#good-labels-rule-4

If the menu says “Remove” and the dialog it opens says “Delete”, people can’t tell whether it’s the same action, and often it isn’t: removing a photo from an album keeps it, deleting it doesn’t. Give each action [one name everywhere](https://ryan-di.github.io/design-field-guide/#good-consistency), so the confirm button repeats the verb from the menu item that opened it.

## In real products

Read only the buttons in each sketch: they still tell you what will happen.

- macOS: closing an unsaved document asks with Don’t Save, Cancel and Save, not Yes, No and Cancel. `good-labels-example-01`
- GitHub: the merge button names the method you picked, like “Squash and merge”, and the confirm step repeats it. `good-labels-example-02`
- WhatsApp: deleting a message offers “Delete for me” and “Delete for everyone”, so each button says who loses the message. `good-labels-example-03`
- Spotify: a song’s menu is a list of verbs with their objects, like Add to playlist, Add to queue and Go to album. `good-labels-example-04`

## Related entries

[good-consistency](good-consistency.md), [good-plain-language](good-plain-language.md), [pat-information-scent](pat-information-scent.md)
