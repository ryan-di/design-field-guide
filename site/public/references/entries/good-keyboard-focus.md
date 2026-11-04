# Keyboard and focus

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 5 · Sweat the states and the edges
Live: https://ryan-di.github.io/design-field-guide/#good-keyboard-focus
Kind: principle
Cite as: Design Field Guide v35, #good-keyboard-focus

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Every control should work from the keyboard alone, focus should move in the order people read, and a visible ring should always show where it is. People who can’t use a mouse depend on this, and so do screen reader users and people who type fast.

Focus is the keyboard’s pointer. Tab moves it, and Enter or Space act on what it points at. If people can’t see focus, or it jumps around, they can’t tell what the next key will do.

## Ways to move with the keyboard

There are four main ways to move with the keyboard. Most apps need Tab and arrow keys, a skip link helps on long pages, and shortcuts help in apps people use all day.

- **Tab.** Tab moves to the next field, button or link in reading order, and Shift+Tab goes back. click Name, then press Tab.
- **Arrow keys.** A group of options, such as tabs, a radio set or a menu, is one Tab stop, and arrow keys move inside it. People don’t have to tab through every option to get past the group. click Week, press the arrow keys, then press Tab.
- **Skip link.** The first Tab on the page shows a “Skip to main content” link. Enter jumps past the header, so people don’t tab through the same eight links on every page. press Load the page, then press Tab and Enter.
- **Shortcuts.** Single keys run frequent actions. They add to Tab and never replace it, and a ? key lists them so people can learn them. click the inbox, then press j, k and e.

## Rules

Four rules keep the keyboard path usable.

### 1. Keep the focus ring visible

https://ryan-di.github.io/design-field-guide/#good-keyboard-focus-rule-1

Focus rings are often removed because they look out of place, so keyboard users press Tab, see nothing change, and can’t tell which button Enter will press until it’s too late. Restyle the ring to fit the design instead of removing it. `:focus-visible` shows it for keyboard use and hides it on most mouse clicks.

### 2. Make focus order match reading order

https://ryan-di.github.io/design-field-guide/#good-keyboard-focus-rule-2

People expect Tab to follow the layout: left to right, top to bottom. When CSS moves things around, or a positive `tabindex` sets its own order, focus jumps to a field they haven’t reached yet, so they type into the wrong field or skip one. Put elements in the DOM in reading order, and use only `tabindex="0"` and `tabindex="-1"`.

### 3. Use real buttons and links

https://ryan-di.github.io/design-field-guide/#good-keyboard-focus-rule-3

A `div` or `span` with a click handler works with a mouse and nothing else: Tab skips it, Enter does nothing, and a screen reader doesn’t call it a button. Use a `button` for actions and a link for going somewhere, because they get focus, the keys and a role for free. See [Link vs button](https://ryan-di.github.io/design-field-guide/#link-vs-button).

### 4. Move focus with what opens and closes

https://ryan-di.github.io/design-field-guide/#good-keyboard-focus-rule-4

When a [dialog](https://ryan-di.github.io/design-field-guide/#dialog) opens and focus stays behind it, keyboard users keep tabbing through a page they can’t see. When it closes and focus goes back to the top, they have to find their place again. Move focus into the dialog when it opens, and when it closes, put focus back on the control that opened it.

## In real products

Notice where focus lands in each one, and how it’s marked.

- VS Code: the Command Palette opens with focus already in its search box, arrows move the highlight, and Esc puts focus back where you were typing. `good-keyboard-focus-example-01`
- GitHub: the first Tab press shows a “Skip to content” link at the top. Keyboard users jump past the long header in one key instead of tabbing through every link. `good-keyboard-focus-example-02`
- Gmail: with keyboard shortcuts turned on in settings, j and k move through the inbox and a marker shows the current conversation, so you always know what Enter will open. `good-keyboard-focus-example-03`
- YouTube: on a video, k pauses, j and l jump 10 seconds, m mutes and f goes full screen. The player flashes an icon when you pause or mute, so you can tell the key worked. `good-keyboard-focus-example-04`

## Related entries

[dialog](dialog.md), [link-vs-button](link-vs-button.md)
