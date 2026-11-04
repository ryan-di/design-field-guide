# Contextual hints

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 12 · Blank screen
Live: https://ryan-di.github.io/design-field-guide/#pat-contextual-hints
Kind: pattern
Cite as: Design Field Guide v35, #pat-contextual-hints

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A contextual hint teaches one thing at the moment people need it, next to the thing it explains. It appears after a related action, such as a first click on an empty whiteboard, and stays away once people know the thing, so people who already know it never see it.

A product tour works the other way round: it explains everything up front, before people have a reason to care. Most people skip it, and the rest forget it by the time they get stuck.

## Ways to do it

Hints range from quiet to loud. Placeholder text sits inside an empty field. A help icon waits until people ask. A callout points at one control, once. A nudge appears after people do something the long way and offers the short way. Pick the quietest one that still reaches people at the right moment.

- **Placeholder.** Use it for a short example of what goes in an empty field.
- **Help icon.** Use it for detail only some people want.
- **Callout.** Use it once, to point at a new or easy-to-miss control.
- **Nudge.** Use it after people do something the long way, to offer the short way.

## Rules

Four rules keep contextual hints useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Show one hint at a time

https://ryan-di.github.io/design-field-guide/#pat-contextual-hints-rule-1

When every feature gets its own hint, they all show up at once. People can’t tell which one matters, the bubbles sit on top of the things they wanted to use, and they close them all without reading. Show one hint, right after people do the related thing, and skip hints for things they already use.

### 2. Remember when people close a hint

https://ryan-di.github.io/design-field-guide/#pat-contextual-hints-rule-2

A closed hint that comes back tells people their choice didn’t count, and after the second time they close hints without reading them, new ones included. Remember every closed hint, ideally with the account so it holds on every device, and give people one place to see the tips again.

### 3. Keep the target in view

https://ryan-di.github.io/design-field-guide/#pat-contextual-hints-rule-3

A hint is about one control. If it sits on top of that control, people have to close the hint before they can try what it explains, and by then they have half forgotten it. Place the hint beside the control and point at it. Keep the control usable, and don’t move keyboard focus into the hint.

### 4. Keep key help somewhere else too

https://ryan-di.github.io/design-field-guide/#pat-contextual-hints-rule-4

Once a hint is closed, it’s gone, so if it was the only place that explained something, people who need it later have nowhere to look. Write the same help in the help pages or a help panel, and link there from the hint so people know where to find it again.

## In real products

- Google Maps: on a map inside a web page, a one-finger swipe scrolls the page, and the map shows “Use two fingers to move the map” only when you try. If you already use two fingers, you never see it. `pat-contextual-hints-example-01`
- Notion: an empty line shows a faint hint to type “/” for commands, but only the line your cursor is on, and it’s gone the moment you type. `pat-contextual-hints-example-02`
- Slack: once you start typing, a small note in the corner of the message box says how to add a new line, right where people would otherwise send by mistake. `pat-contextual-hints-example-03`
- Photoshop: holding the pointer over a tool shows its name, one line on what it does and a short looping video of it in use, right when you’re wondering what the icon means. `pat-contextual-hints-example-04`
