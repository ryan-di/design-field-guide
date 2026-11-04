# Keyboard shortcuts

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 14 · Newcomers & experts
Live: https://ryan-di.github.io/design-field-guide/#pat-shortcuts
Kind: pattern
Cite as: Design Field Guide v35, #pat-shortcuts

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A keyboard shortcut runs a command from the keyboard, without the mouse. People who repeat the same commands all day save a second or two each time, and that adds up. Shortcuts are for people who already know the command, while new people find it in a button or a menu and learn the key from there.

Where a [command palette](https://ryan-di.github.io/design-field-guide/#pat-command-palette) lets people search for a command by name, a shortcut runs one they already know with a single key press.

## Ways to do it

Shortcuts come in four shapes. A single key is the fastest, but it only works where people aren’t typing. A key with Ctrl or ⌘ works anywhere. A sequence of two keys gives room for more commands. A command palette lets people type the name of any command and shows its key on the way.

- **Single key.** Use it for commands people repeat many times in one area, like moving through a list. It only works while focus is in that area, never in a text field.
- **With Ctrl or ⌘.** Use it for commands that should work anywhere, even while people type, like sending. Click in the reply and press
- **Sequence.** Use it when there are more commands than free keys. Gmail uses G then I to go to the inbox. The first key waits for the second, so show that it’s waiting.
- **Command palette.** Use it when there are many commands. People type part of a name and pick from the list. The list shows each command’s key, so people learn it on the way.

## Rules

Four rules keep shortcuts useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Show the keys where people look

https://ryan-di.github.io/design-field-guide/#pat-shortcuts-rule-1

A shortcut nobody knows about saves nobody any time, and people don’t read help pages, so they never learn the key and keep clicking. Show each key next to its command, in buttons, menus and [tooltips](https://ryan-di.github.io/design-field-guide/#tooltip), and keep the full list behind “?”.

### 2. Don’t take keys the browser already uses

https://ryan-di.github.io/design-field-guide/#pat-shortcuts-rule-2

People rely on keys like copy, paste, undo, find and close tab in every app. If your app uses one of them, either the browser wins and your command never runs, or your app wins and people lose a key they rely on. Pick keys that are free, and let people see and change all of them in one place.

### 3. Ignore single keys while people type

https://ryan-di.github.io/design-field-guide/#pat-shortcuts-rule-3

A single-letter shortcut is fast in a list, but in a text field the same letter is part of a word. As with [a palette that opens on “/”](https://ryan-di.github.io/design-field-guide/#pat-command-palette), a shortcut that still fires there runs commands people didn’t ask for. Turn single keys off while focus is in a text field, and give each shortcut a clear area where it works.

### 4. Keep a visible way to do it

https://ryan-di.github.io/design-field-guide/#pat-shortcuts-rule-4

Some people never use the keyboard: they use a mouse, a touch screen or voice. Others haven’t learned the key yet, and if a command only has a shortcut, none of them can use it. Give every command a button or a menu item, and treat the shortcut as the faster path to it.

## In real products

Notice how each product teaches its shortcuts on the slow path, and keeps single keys out of the way while people type.

- macOS: every menu shows each command’s shortcut on the right. Using the menu once teaches the faster key. `pat-shortcuts-example-01`
- VS Code: the command palette shows each command’s key binding beside it, and the Keyboard Shortcuts editor lets you search and remap any of them. `pat-shortcuts-example-02`
- Gmail: single-key shortcuts like j, k and e are off until you turn them on in Settings. Once they’re on, ? opens the full list. `pat-shortcuts-example-03`
- YouTube: k pauses, j and l jump back and ahead 10 seconds, and ? lists the rest. None of them fire while you type a search or a comment. `pat-shortcuts-example-04`

## Related entries

[pat-command-palette](pat-command-palette.md), [tooltip](tooltip.md)
