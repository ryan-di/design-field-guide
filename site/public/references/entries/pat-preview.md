# Preview

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 9 · Scared to click
Live: https://ryan-di.github.io/design-field-guide/#pat-preview
Kind: pattern
Cite as: Design Field Guide v35, #pat-preview

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A preview shows what a change will do before it’s applied. People try a setting on their own content, see the result, and then apply it or go back, and nothing changes until they say so.

It suits changes that are slow, costly or hard to reverse. For quick changes that are easy to take back, [undo](https://ryan-di.github.io/design-field-guide/#pat-undo) is lighter: the change happens at once, and people step back if they don’t like it.

## Ways to do it

Previews come in three common forms, which differ in where the result shows.

- **In place.** Use it when trying an option is quick, such as styles or fonts. The real content changes while the pointer or focus rests on an option, goes back when it leaves, and only a click applies it.
- **Preview view.** Use it when the result looks different from what people edit, such as formatted text. A separate view shows the result before anyone else sees it.
- **Summary.** Use it when the result is something people can’t see yet, such as a price or what happens to their files. Say in words what will change before people confirm.

## Rules

Four rules keep previews useful.

### 1. Make the preview match the result

https://ryan-di.github.io/design-field-guide/#pat-preview-rule-1

A preview is only useful if people can trust it. When it’s drawn differently from the real result, small differences slip in, like text that fits in the preview and is cut off in the result, and people stop trusting it. Draw the preview with the same code as the final output, and if it can’t match, label it “Approximate preview”.

### 2. Keep the preview fast

https://ryan-di.github.io/design-field-guide/#pat-preview-rule-2

People adjust a setting by watching the result, so if the preview trails behind the control, they overshoot, wait and adjust again, and the control feels sticky. Show a quick rough version right away and finish it when the full one is ready, and hold back slow work while a slider is still moving.

### 3. Show that it’s a preview

https://ryan-di.github.io/design-field-guide/#pat-preview-rule-3

People forget they’re in a preview, leave, and believe the change was applied, then find out later that it never happened. Mark the preview with a label and an outline, and keep Apply and Cancel in view the whole time. Put the label in text so screen readers announce it too, and ask before people leave with changes that aren’t applied.

### 4. Skip it for small changes

https://ryan-di.github.io/design-field-guide/#pat-preview-rule-4

A preview step on every setting turns each change into two clicks, so people get slower and stop reading the previews. Apply cheap, reversible changes at once and offer [undo](https://ryan-di.github.io/design-field-guide/#pat-undo), and keep preview-then-apply for changes that are slow, costly or hard to reverse.

## In real products

- Photoshop: filter dialogs show the effect on the image as values change, with a Preview checkbox to compare before and after. Nothing is applied until OK. `pat-preview-example-01`
- GitHub: comment boxes have Write and Preview tabs, so the formatting can be checked before anyone else sees it. `pat-preview-example-02`
- Word: resting the pointer on a style or font shows it on your text. Moving away puts it back, and only a click applies it. `pat-preview-example-03`
- Uber: before you confirm, each ride option shows its price and how soon it arrives. `pat-preview-example-04`

## Related entries

[pat-undo](pat-undo.md)
