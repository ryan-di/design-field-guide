# Side panel

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 19 · Dialogs & panels
Live: https://ryan-di.github.io/design-field-guide/#side-panel
Kind: component
Cite as: Design Field Guide v35, #side-panel

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A side panel opens along the left or right edge of the screen. It holds a second task next to the main view, such as comments on a doc, the details of a photo or search filters. In most forms, people can keep using the main view while it’s open.

Unlike a [dialog](https://ryan-di.github.io/design-field-guide/#dialog), it shares the screen, so people can look at both and move between them.

## Forms

Side panels come in three forms, which differ in what happens to the page: a docked panel makes it narrower, an overlay panel covers its edge, and a modal panel dims it and blocks it.

- **Docked.** Use it for a panel people keep open for a while, like the play queue in a music app.
- **Overlay.** Use it for details people open and close often, like a place on a map.
- **Modal.** Use it when people should finish one task before going back, like checking their cart.

## Rules

Four rules keep side panels useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Give the main task the full width

https://ryan-di.github.io/design-field-guide/#side-panel-rule-1

A panel is narrow, which is fine for a side task. When the task in it becomes the main job, like writing a long reply, lines wrap every few words and the draft is hard to read back. Give that task a full page or a mode of its own, with a clear way back.

### 2. Use the whole screen on phones

https://ryan-di.github.io/design-field-guide/#side-panel-rule-2

On a phone, a side panel takes half the screen, so the page next to it shrinks to a sliver and neither half is big enough to use. Let the panel cover the whole screen while people choose, with a clear Close or Back. When they’re done, the page comes back at full size.

### 3. Keep one panel per side

https://ryan-di.github.io/design-field-guide/#side-panel-rule-3

Each panel takes another slice of the screen, so with three open, the document people are editing becomes a thin strip. Allow one panel on each side, and use tabs inside it for the rest. Switching tabs changes what’s in the panel, and the document keeps its room.

### 4. Don’t dim a page people still use

https://ryan-di.github.io/design-field-guide/#side-panel-rule-4

A dimmed page tells people it’s off-limits, so they don’t think to click the photos behind the panel, and if they do, the click only closes it. If the page is meant to stay usable, keep it bright and clickable, so picking another photo updates the panel in place.

## In real products

Notice that the main view stays visible and usable while the panel is open, and what changes when space runs out.

- Slack: opening a thread puts it in a panel on the right. The channel stays readable beside it, and people can reply in either place without losing their spot. `side-panel-example-01`
- Figma: the panel on the right always shows the selected layer’s properties. Select another layer and it updates in place, while the canvas stays fully usable. `side-panel-example-02`
- VS Code: the icons on the far left swap which view fills the one side bar, such as files or search, instead of opening a new panel for each. `side-panel-example-03`
- Google Maps: on a computer, a place’s details open in a panel beside the map, which you can still pan. On a phone, the same details come up as a sheet you drag up from the bottom. `side-panel-example-04`

## Related entries

[dialog](dialog.md)
