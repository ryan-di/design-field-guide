# Slider + number

Design Field Guide v35 (2026-11) · Part 3 · Components · Chapter 20 · Inputs
Live: https://ryan-di.github.io/design-field-guide/#slider
Kind: component
Cite as: Design Field Guide v35, #slider

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A slider sets a value by dragging a handle along a track. The track shows the whole range, so people see where the value sits between the lowest and the highest. Dragging is quick, but it’s hard to land on one exact number.

A number field is the opposite: exact, but it doesn’t show the range, and people can’t try values by feel. Many settings show both, side by side.

## Forms

Sliders differ in what they let people set. A plain slider moves smoothly. Adding a number field makes it exact. A range slider has two handles for a minimum and a maximum. A stepped slider snaps to a few fixed values.

- **Plain.** Use it when people judge the result by eye or by ear, like brightness or volume. Show the effect live while they drag, because the number itself matters less.
- **With a number.** Use it when people sometimes need an exact value, like a quality setting. Typing a number moves the slider, and dragging updates the number.
- **Range.** Use it to set a minimum and a maximum, like a price filter. Show both values, and how many results are left, while people drag.
- **Steps.** Use it when only a few values make sense, like text size. The handle snaps to each step, and tick marks show where the steps are.

## Rules

Four rules keep sliders useful.

### 1. Let people type the exact value

https://ryan-di.github.io/design-field-guide/#slider-rule-1

When the range has more values than the track has pixels, one pixel covers several values, so landing on exactly 37 takes many tries, and with a finger it’s worse. Put a number field next to the slider, so people can drag to get close and type the exact value.

### 2. Spread out a huge range

https://ryan-di.github.io/design-field-guide/#slider-rule-2

On a straight track from $1 to $10,000, all the small amounts share the first few pixels, so setting $50 by dragging is nearly impossible. Use a number field, or a slider where $1 to $10, $10 to $100 and so on each get the same room, with a field beside it for any exact amount.

### 3. Make the handle easy to grab

https://ryan-di.github.io/design-field-guide/#slider-rule-3

A tiny handle is hard to hit with a mouse, and a finger covers it completely. If clicking the track does nothing and the keyboard can’t reach it, some people can’t set the value at all. Make the handle and its hit area bigger, let a click on the track move it there, and let arrow keys move it too, with Shift for bigger steps.

### 4. Show what the value does

https://ryan-di.github.io/design-field-guide/#slider-rule-4

When only a number changes, people can’t tell if higher is stricter or looser, so they guess or leave it alone. Label both ends with what they mean, and show the effect while people drag, like which emails would go to Spam.

## In real products

Notice how each product pairs dragging with something exact or something you can see: a typed number, a live result, or a preview of where you’ll land.

- Figma: number fields double as sliders. Drag sideways on a field’s label to scrub the value, or click into it and type the exact number. `slider-example-01`
- Lightroom: every edit slider shows its value, and the value can be typed. The photo changes while you drag, so people judge by the result, not the number. `slider-example-02`
- YouTube: hovering or dragging along the seek bar shows a small frame and the time at that point. People see where they’ll land before they let go. `slider-example-03`
- Airbnb: the price filter shows a bar chart of prices above a two-handle slider, with minimum and maximum fields below. Drag for a rough range, or type an exact one. `slider-example-04`
