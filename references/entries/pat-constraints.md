# Constraints

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 13 · Prevent, explain, recover
Live: https://ryan-di.github.io/design-field-guide/#pat-constraints
Kind: pattern
Cite as: Design Field Guide v35, #pat-constraints

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A constraint makes a wrong value impossible to enter. Instead of a free text field and an error afterwards, people pick from options that all work, or set a number that stops at its limits. There is nothing to refuse, because every choice is valid.

Validation works the other way round: it lets people type anything, then checks it and explains the mistake. Use a constraint when the valid values are few or follow a clear rule, and keep validation for values too varied to offer as choices.

## Ways to do it

Constraints come in a few shapes. A list offers only the values that work. A number with limits stops at its smallest and largest value. Options that don’t apply right now stay visible but turned off. Split fields take one part of a value at a time, so its shape can’t go wrong.

- **List.** Use it when the valid values are few and known.
- **Limits.** Use it for a count or an amount within a range.
- **Turned off.** Use it when some options exist but can’t be chosen right now.
- **Split fields.** Use it for a value with a fixed shape, like a 6-digit code.

## Rules

Four rules keep constraints useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Leave a way out for odd cases

https://ryan-di.github.io/design-field-guide/#pat-constraints-rule-1

A short list covers most people, but not everyone. Someone with an odd-sized window has no way to enter the width they really need, so they give up or pick something wrong. Add a “Custom…” choice for those cases, check what people type there, and [say so when you round it](https://ryan-di.github.io/design-field-guide/#pat-forgiving-input).

### 2. Say why an option is off

https://ryan-di.github.io/design-field-guide/#pat-constraints-rule-2

A grayed-out option with no reason looks broken: people click it, nothing happens, and they don’t know whether to upgrade, free up space or give up. Put the reason next to the option, in plain text: what it needs and how to get it. Leave out options that can never apply to this person.

### 3. Show the rule before people need it

https://ryan-di.github.io/design-field-guide/#pat-constraints-rule-3

Some values follow a rule that can’t be built into the control, like which characters a username may use. If people only learn the rule from an error, they have to guess again. Write the rule in the label or the help text under the field, so people get it right on the first try.

### 4. Keep the rule in one place

https://ryan-di.github.io/design-field-guide/#pat-constraints-rule-4

The list, the help text and the final check often get written at different times. When they disagree, people pick a value the list allows and get refused at the end. Write the rule once and build the list, the help text and the check from it, so they can’t drift apart.

## In real products

Notice that choices that can’t work are either never offered or visibly off.

- Google Calendar: the end-time list only runs forward from the start time and shows each length, like “(1 hr)”, so an event can’t end before it begins. `pat-constraints-example-01`
- Airbnb: dates that are already booked are grayed out and can’t be picked. `pat-constraints-example-02`
- Duolingo: many exercises have you build the answer from word tiles, so every try is a sentence that can be checked, and you can switch to typing when you want it harder. `pat-constraints-example-03`
- VS Code: the Settings editor builds each control from the setting’s definition, so a setting with fixed options gets a dropdown and an on/off one gets a checkbox. `pat-constraints-example-04`

## Related entries

[pat-forgiving-input](pat-forgiving-input.md)
