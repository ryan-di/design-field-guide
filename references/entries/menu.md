# Menu

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 18 · Overlays
Live: https://ryan-di.github.io/design-field-guide/#menu
Kind: component
Cite as: Design Field Guide v35, #menu

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A menu is a short list of commands that opens from a button. It holds actions people need now and then, like Rename, Duplicate or Delete, so they don’t crowd the screen. Picking an item runs it and closes the menu.

Where a select fills in a value, like a size or a country, and the field keeps showing that value, a menu runs a command, and then it’s gone.

## Forms

Most menus open from a button: a “More” button with three dots, or a button with a name like Sort, which may let people pick one setting. A context menu opens when people right-click or long-press an item, and a menu bar along the top of a window holds all of an app’s commands.

- **More button.** Use it for the actions people need now and then on one item.
- **Pick one.** Use it for one setting with a few short choices, like sort order.
- **Context menu.** Use it for shortcuts on items people can right-click or long-press.
- **Menu bar.** Use it in a large app with many commands, like a document editor.

## Rules

Four rules keep menus useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Keep it short

https://ryan-di.github.io/design-field-guide/#menu-rule-1

In a menu of more than about a dozen items, people have to read every item to find the one they want, and if it’s out of view at the bottom, they scroll past it or give up. Split the list into small groups with the common actions on top. Move rare actions out, or let people type a few letters to find them. Very large sets need a [command palette](https://ryan-di.github.io/design-field-guide/#pat-command-palette).

### 2. Keep the main action in view

https://ryan-di.github.io/design-field-guide/#menu-rule-2

Every trip into a menu costs a click and a search. That is fine for rare actions, but for the action people take most, like Reply in email, they pay it every time. Give the one or two most used actions their own buttons, and keep the menu for the rest.

### 3. Put options to compare on the page

https://ryan-di.github.io/design-field-guide/#menu-rule-3

A menu shows names only, and only while it’s open, so to compare prices or dates, people open it again and again and keep the numbers in their head. When options differ in price, time or size, lay them out on the page with those details, for example as radio buttons or cards, so people can compare them in one look.

### 4. Don’t nest submenus

https://ryan-di.github.io/design-field-guide/#menu-rule-4

Each submenu opens on hover and switches when the pointer slips onto a neighbor, so people retrace their steps or pick the wrong item without noticing. Keep a menu to one level, two at most. When a choice needs more steps, open a dialog that shows every option at once and has room to explain them.

## In real products

Notice that the most common actions stay in view, the rest wait in a short grouped list, and very large sets get a search.

- Slack: pointing at a message shows a few buttons for what people do most, like reacting or replying in a thread. Everything else waits in a More menu. `menu-example-01`
- VS Code: the editor’s right-click menu groups commands with dividers and shows each shortcut on the right, so the menu also teaches the faster way. The full set of commands lives in the Command Palette. `menu-example-02`
- macOS: the Help menu has a search field that finds commands across every menu. Pointing at a result opens its menu and points to the command, so people learn where it lives. `menu-example-03`
- iOS Photos: pressing and holding a photo lifts a preview with a menu of actions under it. Delete comes last, in red. `menu-example-04`

## Related entries

[pat-command-palette](pat-command-palette.md)
