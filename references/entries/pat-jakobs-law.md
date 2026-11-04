# Jakob’s law

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 15 · Lean on how people already behave
Live: https://ryan-di.github.io/design-field-guide/#pat-jakobs-law
Kind: pattern
Cite as: Design Field Guide v35, #pat-jakobs-law

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Jakob’s law says that people spend most of their time in other products, so they expect yours to work the same way. A search box has a magnifying glass, a link is underlined, and the cart sits in the top right corner. People use these without thinking and bring those habits to every new product they open.

The law isn’t a ban on new ideas, but it tells you what one costs: every break from a convention is something people have to stop and learn. Sometimes that cost is worth paying, but it should be a choice.

## Rules

Three rules help you work with people’s habits. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Use the control people already know

https://ryan-di.github.io/design-field-guide/#pat-jakobs-law-rule-1

A new kind of control can look fresh in a design review, but in use people try what works everywhere else, and it doesn’t work here. Some never find out how it works. Use the familiar control, which assistive tech understands too, and change it only when testing shows a clear win for a real task.

### 2. Adapt a convention to the task

https://ryan-di.github.io/design-field-guide/#pat-jakobs-law-rule-2

A convention that is right in one kind of product can be wrong in another. In a document, Enter starts a new line, but in a table people expect Enter to save the cell and move down. Find out how people do this work in the tools they already use, and test the result with them.

### 3. Teach a break where it happens

https://ryan-di.github.io/design-field-guide/#pat-jakobs-law-rule-3

Sometimes a product has a good reason to break a convention. If nothing explains the change, people try the usual way, nothing happens, and they don’t know why. Show a short hint at the moment they try the usual way, and keep the familiar path working where you can.

## In real products

Notice what each product kept familiar.

- Google Docs: menus, toolbar and shortcuts like Ctrl+B and Ctrl+Z (⌘B and ⌘Z on Mac) work like a desktop word processor. `pat-jakobs-law-example-01`
- Blender: selects with the left mouse button by default, like most software, and offers an Industry Compatible keymap for people coming from other 3D tools. `pat-jakobs-law-example-02`
- Instagram: stories work like stories in other apps. Tap right for next, tap left to go back, hold to pause. `pat-jakobs-law-example-03`
