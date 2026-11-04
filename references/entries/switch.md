# Switch

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 20 · Inputs
Live: https://ryan-di.github.io/design-field-guide/#switch
Kind: component
Cite as: Design Field Guide v35, #switch

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A switch turns one setting on or off. The change takes effect the moment it’s flipped, with nothing to save, so people expect to see the result at once.

That is what separates it from a checkbox, which marks a choice in a form and does nothing until people press Save or Submit.

## Forms

Switches come in four common forms. Most sit in a settings list, one per row, and some add a line that explains the setting. One switch can also turn a whole group of settings on or off, and in a toolbar a switch changes how the page is shown.

- **In a list.** Use it for a list of settings, one per row.
- **With a description.** Use it when the name alone doesn’t say what will change.
- **For a group.** Use it to turn a whole group of settings on or off at once.
- **In a toolbar.** Use it for a view option people change often, like showing only unread mail.

## Rules

Four rules keep switches useful.

### 1. Don’t use it in a form with Save

https://ryan-di.github.io/design-field-guide/#switch-rule-1

A switch slides to On at once, so the setting looks done. In a form that still needs Save, people leave without pressing it, and the change is lost. Use a [checkbox](https://ryan-di.github.io/design-field-guide/#checkbox) there, because it reads as a choice that waits for Save.

### 2. Name the setting and show its state

https://ryan-di.github.io/design-field-guide/#switch-rule-2

A label like “Turn off emails” reads as a command, and with the switch off it becomes a double negative. A vague label like “Notifications” doesn’t say which kind. Either way, people have to puzzle out what’s on, and many get it wrong. Name one setting per row, and write “On” or “Off” next to the switch, so the answer doesn’t depend on color.

### 3. Show what really happened

https://ryan-di.github.io/design-field-guide/#switch-rule-3

Some changes take time or can fail, like turning on backup while the phone is offline. If the switch says On at once, people trust it and find out when a photo is lost. Show a small busy state while the change runs, and if it fails, flip the switch back and say why.

### 4. Use it only for on and off

https://ryan-di.github.io/design-field-guide/#switch-rule-4

A switch has two positions. When a setting has three choices, “Off” could mean either of the others, and one of them can’t be reached at all, which people only find out by flipping it. Use a [segmented control](https://ryan-di.github.io/design-field-guide/#segmented) or a [radio group](https://ryan-di.github.io/design-field-guide/#radio), so every choice is in view with its name.

## In real products

- iOS Settings: Airplane Mode is a switch right in the list, while rows that open their own page, like Bluetooth, show their state in words. `switch-example-01`
- YouTube: the autoplay switch sits in the player’s controls. It decides whether the next video starts on its own, and its tooltip says which way it’s set. `switch-example-02`
- Gmail: the full settings page has a Save Changes button at the bottom, so it uses radio buttons and checkboxes instead of switches. `switch-example-03`

## Related entries

[checkbox](checkbox.md), [radio](radio.md), [segmented](segmented.md)
