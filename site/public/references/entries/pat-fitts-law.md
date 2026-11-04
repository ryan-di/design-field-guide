# Fitts’s law

Design Field Guide v35 (2026-11) · Part 2 · Patterns · Chapter 15 · Lean on how people already behave
Live: https://ryan-di.github.io/design-field-guide/#pat-fitts-law
Kind: pattern
Cite as: Design Field Guide v35, #pat-fitts-law

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Fitts’s law says that the time it takes to hit a target depends on its size and its distance. A big target close to the pointer or the thumb is fast to hit. A small target far away is slow, and people miss it more often.

It applies to every click and tap: buttons, links, menu items, close icons. The screen edges help too, because the pointer stops there and can’t overshoot. People with a tremor, on a touch screen or using zoom feel the difference most.

## Rules

Three rules put Fitts’s law to work.

### 1. Make the hit area bigger than the icon

https://ryan-di.github.io/design-field-guide/#pat-fitts-law-rule-1

Small icons look tidy, but a 12-pixel target is hard to hit, especially with a finger or a shaky hand, so people miss, try again, and sometimes hit the thing next to it. The icon can stay small if the clickable area around it is large, at least 24 by 24 pixels. See [Icon button](https://ryan-di.github.io/design-field-guide/#icon-button).

### 2. Put the action near what it acts on

https://ryan-di.github.io/design-field-guide/#pat-fitts-law-rule-2

When the button sits far from where people are working, every use costs a long move across the screen. On a wide screen that adds up, and on a phone it can mean a stretch of the thumb. Put the action next to the field, at the end of the form, or in a menu that opens at the pointer.

### 3. Keep risky actions away from common ones

https://ryan-di.github.io/design-field-guide/#pat-fitts-law-rule-3

If Delete sits right next to Reply and both are the same size, a fast move lands on either one, and a small slip deletes something. Make the common action the big, easy target, move the risky one away or into a menu, and [let people undo it](https://ryan-di.github.io/design-field-guide/#pat-undo).

## In real products

Notice how each one makes the target bigger, or puts it where the pointer or thumb already is.

- macOS: the menu bar sits on the top edge of the screen. The pointer can’t overshoot it, so a quick flick up always lands on it. `pat-fitts-law-example-01`
- Blender: pie menus open around the pointer. Every option is the same short move away, and you pick by direction, so each target is a whole slice. `pat-fitts-law-example-02`
- YouTube: on phones, double-tap the left or right side of the video to jump back or ahead 10 seconds. Half the screen is the target. `pat-fitts-law-example-03`
- Gmail: on phones, Compose is a large button in the bottom corner, where the thumb already rests, not a small icon at the top. `pat-fitts-law-example-04`

## Related entries

[icon-button](icon-button.md), [pat-undo](pat-undo.md)
