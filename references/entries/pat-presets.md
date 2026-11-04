# Presets

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 8 · Too much at once
Live: https://ryan-di.github.io/design-field-guide/#pat-presets
Kind: pattern
Cite as: Design Field Guide v35, #pat-presets

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

A preset sets several linked values at once, under a name that says what you get, like “Fast” or “Best quality”. People pick the outcome they want instead of tuning each value, and the values stay in view, so people can still adjust one.

Unlike a [smart default](https://ryan-di.github.io/design-field-guide/#pat-smart-defaults), which fills in one field, a preset fills in a group of fields that only make sense together. Build the picker as a radio group, so arrow keys move between presets.

## Ways to do it

Presets come in four common forms. They differ in how people choose one, and in whether it stays linked after it’s picked.

- **Picker.** Use it when there are three to five outcomes people can name. The values each one sets stay in view.
- **Gallery.** Use it when the result is easier to see than to describe. Each preset shows a small preview of what it will do to this photo.
- **Starting point.** Use it when people pick once and then make it their own. The preset fills in the fields, and later edits don’t need to match it.
- **Linked style.** Use it when the same look appears in many places. Changing the style once updates every heading that uses it.

## Rules

Four rules keep presets useful. Each comes with a demo. Switch between “When it backfires” and “Do this instead” to see the difference.

### 1. Show what each preset sets

https://ryan-di.github.io/design-field-guide/#pat-presets-rule-1

A preset name alone doesn’t say what will change, so people pick one and find out what it did only when the result arrives, and careful people avoid presets. Show the values each preset sets next to the picker, and let people edit them.

### 2. Switch to “Custom” after an edit

https://ryan-di.github.io/design-field-guide/#pat-presets-rule-2

Once someone changes a value, the settings no longer match the preset, so a label that still shows the preset’s name is wrong, and people trust it. Switch the label to “Custom” as soon as a value changes, and mark what was edited. Picking the preset again brings its values back.

### 3. Offer a few, named by outcome

https://ryan-di.github.io/design-field-guide/#pat-presets-rule-3

A long list of presets is a new decision on top of the old one, and internal names make it worse, because people can’t tell what “JPG-80-2048” is for. Keep three to five presets, and name each one by what people want to do, like “Email” or “Print”.

### 4. Let people save their own

https://ryan-di.github.io/design-field-guide/#pat-presets-rule-4

Some people need the same mix of settings every time, and no built-in preset matches it, so without a way to save it they set each value again on every visit. Let them save their mix as a preset with their own name, next to the built-in ones.

## In real products

- Photoshop: a new document starts from presets grouped by use, like Print or Web. Picking one fills in the size, resolution and color mode, which stay editable, and a custom setup can be saved as a new preset. `pat-presets-example-01`
- YouTube: on phones, video quality offers choices named by outcome, like higher quality or data saver. Exact resolutions are still there under Advanced. `pat-presets-example-02`
- Instagram: one tap on a filter changes several adjustments at once. Tapping it again shows a strength slider, so the look can be softened without starting over. `pat-presets-example-03`
- Google Docs: styles like Heading 1 set size, weight and spacing together. After restyling one heading by hand, “Update Heading 1 to match” gives every Heading 1 that look. `pat-presets-example-04`

## Related entries

[pat-smart-defaults](pat-smart-defaults.md)
