# Link vs button

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 21 · Actions
Live: https://ryan-di.github.io/design-field-guide/#link-vs-button
Kind: component
Cite as: Design Field Guide v35, #link-vs-button

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Links and buttons are both things people click, but they do different jobs. A link takes people to another page or place. A button does something where they are: it saves, sends, adds or deletes.

The difference matters because browsers treat them differently: a link has an address, so people can open it in a new tab, bookmark it and come back with Back, and a button has none of that. So choose by what happens on click, not by how it should look.

## Forms

Each comes in a few forms. A link can sit inside a sentence or stand on its own, and a button can be a full button or a lighter text button. A link can also look like a button when it’s the main next step: the look follows how important it is, but whether it’s a link or a button still follows what it does.

- **Inline link.** Use it to point to another page from inside a sentence.
- **Standalone link.** Use it for a way to another page that sits on its own, such as “See all orders”.
- **Button.** Use it when pressing it changes something here: add, save, send, delete.
- **Button-style link.** Use it when the main next step is another page, such as “Go to checkout”.
- **Text button.** Use it for a small action that shouldn’t compete with the main one, such as “Remove”.

## Rules

Three rules keep links and buttons clear.

### 1. Use a button when something changes

https://ryan-di.github.io/design-field-guide/#link-vs-button-rule-1

People open links in a new tab just to look, so if a link deletes or sends something, opening it is enough to do it, with no warning and no way back. A button tells people that pressing it does something, so they press it on purpose. Put Undo next to the result to cover a slip.

### 2. Use a link to go somewhere

https://ryan-di.github.io/design-field-guide/#link-vs-button-rule-2

People open pages in a new tab to keep their place, and use Back to return. A button that only swaps the view breaks both: the address doesn’t change, so there’s nothing to bookmark or share, and Back can’t return to the page they came from. A link keeps all of this working, the same as on every other site.

### 3. Underline links in text

https://ryan-di.github.io/design-field-guide/#link-vs-button-rule-3

A link that differs from the words around it only by color is easy to miss, because people with color blindness or low vision, or anyone on a dim screen, see plain text. An underline marks it without relying on color, so it still shows in grayscale. Links that stand on their own, like “See all orders”, can do without it, because their place already says what they are.

## In real products

Notice that in each product a link and a button sit side by side.

- Google Docs: links in the text are underlined. In the card that opens on one, the address is a link, while copy, edit and remove are buttons. `link-vs-button-example-01`
- GitHub: in a comment, issue numbers like #42 and @mentions are links to other pages. Comment and Close issue change things here, so they are buttons. `link-vs-button-example-02`
- YouTube: under a video, the channel name is a link to the channel’s page. Subscribe is a button: it changes something without leaving the video. `link-vs-button-example-03`
- Amazon: in search results, each product title is a link, so it can open in a new tab for comparing. Add to cart is a button that acts right where you are. `link-vs-button-example-04`
