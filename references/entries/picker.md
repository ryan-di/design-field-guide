# Structured picker

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 20 · Inputs
Live: https://ryan-di.github.io/design-field-guide/#picker
Kind: component
Cite as: Design Field Guide v35, #picker

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A structured picker lets people enter a value with a set format by pointing at it: a day on a calendar, a time from a list, a color from a row of swatches. Every value it offers is valid, so people can’t enter a date that doesn’t exist or a color the app can’t use.

Where a [text field](https://ryan-di.github.io/design-field-guide/#text-field) takes any text and checks it afterwards, a picker shows the possible values up front, so people choose one instead of remembering the format.

## Forms

Pickers take the shape of the value they hold. A calendar picks one date, and a range calendar picks a start and an end. Times often come as a set of slots. Colors from a short list come as swatches.

- **Calendar.** Use it for one date in the near future, like a delivery day.
- **Date range.** Use it when the value has a start and an end, like a hotel stay.
- **Time.** Use it when only some times work, like table bookings every 30 minutes.
- **Swatches.** Use them when only a few colors are allowed, like label colors in a mail app.

## Rules

Three rules keep pickers useful. Each comes with a demo. Switch between “When it breaks” and “Do this instead” to see the difference.

### 1. Let people type too

https://ryan-di.github.io/design-field-guide/#picker-rule-1

A calendar is quick for a date next week, but slow for a date people know by heart, like a birthday: March 1988 is hundreds of clicks back. Put a text field next to the picker and accept the common ways of writing the value. The picker follows what people type, so they can still check it or click instead.

### 2. Show every allowed value

https://ryan-di.github.io/design-field-guide/#picker-rule-2

Sometimes only a few values are allowed, like the 8 colors a calendar keeps for events. A free color strip suggests that any color will do, so people pick one, save, and get a different one with no reason given. Show the allowed values as swatches, chips or radio buttons, so what people pick is what they get.

### 3. Put the context in the picker

https://ryan-di.github.io/design-field-guide/#picker-rule-3

A bare calendar doesn’t say which day is today, so to pick “a week from now”, people have to work out today’s date and count squares. Mark today in the calendar, offer presets for the usual choices, like “In 7 days”, and spell out the result in words, so people can check it before they move on.

## In real products

Notice how each picker gives a fast path for the common case and a way to be exact: presets, context inside the calendar, or plain typing.

- Gmail: Schedule send offers a few presets like tomorrow morning, each with its exact date and time, and a full picker for anything else. Most picks take one click. `picker-example-01`
- Google Flights: the date picker shows a price under each day, with the cheaper days in a different color. People pick dates with the cost in view. `picker-example-02`
- Figma: the color picker pairs a color area with a hex field and an eyedropper. People can point, type the exact code, or take a color from the canvas. `picker-example-03`
- Todoist: typing a date in plain words, like “tomorrow 3pm”, highlights it and sets the due date. People who know the date never open a calendar. `picker-example-04`

## Related entries

[text-field](text-field.md)
