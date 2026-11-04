# Motion

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 5 · Sweat the states and the edges
Live: https://ryan-di.github.io/design-field-guide/#good-motion
Kind: principle
Cite as: Design Field Guide v35, #good-motion

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Motion should explain a change, like where a panel came from or where a deleted item went, and then get out of the way fast. Motion that explains nothing only makes people wait.

Two settings shape every animation: how long it takes, and its easing, which is how its speed changes along the way. The demo below lets you change both on the same panel.

## Rules

Four rules keep motion useful.

### 1. Keep it short

https://ryan-di.github.io/design-field-guide/#good-motion-rule-1

An animation that takes 600 ms looks smooth the first time, but by the tenth time people are waiting for it, and if it blocks clicks while it plays, the app feels broken. Keep most interface motion around 150–300 ms: small moves get less, big ones a little more, and nothing should block the next click.

### 2. Animate to explain, not to decorate

https://ryan-di.github.io/design-field-guide/#good-motion-rule-2

When everything bounces, fades and slides, motion stops meaning anything, because people can’t tell which movement is about the thing they just did. Use motion to show a change, such as where something came from, where it went or what was added, and cut any animation that explains nothing.

### 3. Respect reduced motion

https://ryan-di.github.io/design-field-guide/#good-motion-rule-3

Large movement on screen can make some people dizzy or sick, so they turn on the reduce motion setting on their device, and an app that ignores it keeps sliding and zooming anyway. Check `prefers-reduced-motion` and test with the setting on. Swap slides and zooms for an instant change or a short fade: the change still happens, only the movement goes.

### 4. Match the easing to the direction

https://ryan-di.github.io/design-field-guide/#good-motion-rule-4

Linear motion looks mechanical. Ease-in starts slow, so something that arrives with it feels late, and something that leaves with ease-out seems to linger. Ease out for things that enter, so they arrive fast and settle, and ease in for things that leave. Keep overshoot for rare, playful moments.

## In real products

- iOS: an app opens by growing out of its icon and shrinks back into it when you leave, so you see where it lives. With Reduce Motion on, it fades instead. `good-motion-example-01`
- macOS: a minimized window shrinks down into the Dock. The motion shows where the window went, so you know where to click to get it back. `good-motion-example-02`
- Gmail: swipe an email and it slides off the side, then the rows below move up to close the gap. You see that it left and what took its place, and a bar offers Undo. `good-motion-example-03`
- Instagram: double-tap a photo and a big heart pops up on it, then fades, while the small heart below fills in. A little bounce suits this one quick, light action. `good-motion-example-04`
