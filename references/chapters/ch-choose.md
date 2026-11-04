# Before you pick one, ask three questions

Design Field Guide v35 (2026-11) · Part 3 · Components
Live: https://ryan-di.github.io/design-field-guide/#ch-choose
Cite as: Design Field Guide v35, #ch-choose

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

- **How urgent is it?**: Sets how much it may interrupt: its step on the [interruption ladder](https://ryan-di.github.io/design-field-guide/#ch-start).
- **How long must it stay?**: Sets whether it fades, stays while true, or waits for an answer.
- **What must people do?**: Sets whether it holds words, buttons, or a whole form.

## Quick reference

Start from what the person needs, then read across. Each component links to its entry.

| If people need to… | Use | Avoid |
|---|---|---|
| Know an action worked | [Toast](https://ryan-di.github.io/design-field-guide/#toast), with Undo if reversible | A dialog |
| Fix a problem with one field or item | [Inline message](https://ryan-di.github.io/design-field-guide/#inline-message) | A toast |
| Know about a state that lasts | [Banner](https://ryan-di.github.io/design-field-guide/#banner) | A toast |
| Notice a count without interruption | [Badge](https://ryan-di.github.io/design-field-guide/#badge) | A banner |
| Wait a few seconds | [Spinner](https://ryan-di.github.io/design-field-guide/#spinner), delayed 400 ms | A full-screen loader |
| Wait for long work | [Progress bar](https://ryan-di.github.io/design-field-guide/#progress-bar), in the background | A spinner |
| Wait for a known layout | [Skeleton](https://ryan-di.github.io/design-field-guide/#skeleton) | A blank screen |
| Learn what an icon does | [Tooltip](https://ryan-di.github.io/design-field-guide/#tooltip), or a visible label | Must-know info in a tooltip |
| Adjust a few settings in place | [Popover](https://ryan-di.github.io/design-field-guide/#popover) | A dialog |
| Run a command on one item | [Menu](https://ryan-di.github.io/design-field-guide/#menu) | A row of many buttons |
| Decide before going on | [Dialog](https://ryan-di.github.io/design-field-guide/#dialog) | A banner |
| Do a side task while seeing the main view | [Side panel](https://ryan-di.github.io/design-field-guide/#side-panel) | A modal dialog |
| Turn something on right now | [Switch](https://ryan-di.github.io/design-field-guide/#switch) | A checkbox |
| Choose any of several, applied later | [Checkbox](https://ryan-di.github.io/design-field-guide/#checkbox) | A switch |
| Choose one of a few | [Radio group](https://ryan-di.github.io/design-field-guide/#radio) or [segmented control](https://ryan-di.github.io/design-field-guide/#segmented) | A select |
| Choose one of many | [Select or combobox](https://ryan-di.github.io/design-field-guide/#combobox) | A long radio group |
| Set a value in a range | [Slider + number field](https://ryan-di.github.io/design-field-guide/#slider) | A slider alone |
| Enter free text | [Text field](https://ryan-di.github.io/design-field-guide/#text-field) | A placeholder as the label |
| Enter a known format | [Structured picker](https://ryan-di.github.io/design-field-guide/#picker) + typed input | Free text |
| Do the main thing on a screen | [Primary button](https://ryan-di.github.io/design-field-guide/#buttons) | Two primaries |
| Act in a tight space | [Icon button](https://ryan-di.github.io/design-field-guide/#icon-button), if the icon is universal | Unlabeled custom icons |
| Go somewhere | [Link](https://ryan-di.github.io/design-field-guide/#link-vs-button) | A button |
| See one part of something at a time | [Tabs](https://ryan-di.github.io/design-field-guide/#tabs) | Tabs for things people compare |
| Hide rarely needed detail | [Accordion](https://ryan-di.github.io/design-field-guide/#accordion) | Tabs |
| Scan items, then open one | [Cards](https://ryan-di.github.io/design-field-guide/#card) | Cards full of buttons |
| Move between areas | [Side navigation](https://ryan-di.github.io/design-field-guide/#side-nav) | Navigation for actions |
| Get back up a hierarchy | [Breadcrumbs](https://ryan-di.github.io/design-field-guide/#breadcrumbs) | The Back button only |
| Follow a fixed sequence | [Stepper](https://ryan-di.github.io/design-field-guide/#stepper) | Tabs |
| See that a control heard them | [Interaction states](https://ryan-di.github.io/design-field-guide/#interaction-states) on the control | One look for every state |
| Start when there’s nothing yet | [Empty state](https://ryan-di.github.io/design-field-guide/#empty-state), with one way to start | “No items” |
| Recover when something fails | [Error state](https://ryan-di.github.io/design-field-guide/#error-state), with a next step | “Something went wrong” |
