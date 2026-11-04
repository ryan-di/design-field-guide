# Smart defaults

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 8 · Too much at once
Live: https://ryan-di.github.io/design-field-guide/#pat-smart-defaults
Kind: pattern
Cite as: Design Field Guide v35, #pat-smart-defaults

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A smart default is a value filled in for people because it fits most of them, so they can accept it and move on, or change it. Each good default removes one decision, and on a long form that adds up.

A default is a real value that will be used, shown in a field people can change. That separates it from a placeholder, which disappears when people type and is never used, and from a [preset](https://ryan-di.github.io/design-field-guide/#pat-presets), which sets several linked values at once.

## Ways to do it

Defaults differ in where the value comes from.

- **Most common.** Use it when one answer fits most people. Base it on what people actually pick, not on what you hope they pick.
- **Last used.** Use it when people repeat their own choice. Each person gets their own default, so it fits more people than one value can.
- **From context.** Use it when the place, time or device already gives the answer. Say where the value came from, so a wrong guess is easy to spot and change.
- **From another field.** Use it when one value follows from another, like an end time from a start time. Once people set it by hand, stop changing it for them.

## Rules

Four rules keep smart defaults useful.

### 1. Base defaults on what people pick

https://ryan-di.github.io/design-field-guide/#pat-smart-defaults-rule-1

A default that’s wrong for many people is worse than none, because they have to notice it and change it on every visit. Look at what people actually choose and start there, then remember what each person used last, so someone with a different habit stops fixing it too.

### 2. Keep defaults in view

https://ryan-di.github.io/design-field-guide/#pat-smart-defaults-rule-2

Some defaults are applied where people can’t see them, so the result surprises people and they have no idea which setting caused it. Show every default in the form, in a field people can change. Mark values that differ from the default in words, not only with color, so people see what will happen before they press the button.

### 3. Start risky options off

https://ryan-di.github.io/design-field-guide/#pat-smart-defaults-rule-3

A default can quietly serve the business instead of the person, like a pre-ticked “public” box, and because most people never change defaults, they end up sharing what they meant to keep. Pick the safe, reversible option: anything that publishes, deletes, costs money or overwrites files should start off.

### 4. Use real values, not placeholders

https://ryan-di.github.io/design-field-guide/#pat-smart-defaults-rule-4

Gray text in an empty field looks like an answer, so people skip the field, and the form fails because it was empty all along. The gray text also vanishes as soon as they type. Put a real value in the field, or write the hint as a label or help text.

## In real products

Notice where each default comes from: the spot you clicked, the most common choice, where you are, or what you already wrote.

- Google Calendar: clicking a time slot starts an event right there, with the default length already set. Most events only need a title. `pat-smart-defaults-example-01`
- Figma: adding an export starts at PNG at 1x, the choice most people want. Both values sit right there to change. `pat-smart-defaults-example-02`
- Uber: pickup is already set to where you are, so the first question is only where to. `pat-smart-defaults-example-03`
- Google Docs: a document you never named takes its first line as its name. Files get a useful name without a question. `pat-smart-defaults-example-04`

## Related entries

[pat-presets](pat-presets.md)
