# Problem framing

Design Field Guide v35 (2026-11) · Part 1 · Good design · Chapter 1 · Get the problem right first
Live: https://ryan-di.github.io/design-field-guide/#good-problem-framing
Kind: principle
Cite as: Design Field Guide v35, #good-problem-framing

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Framing the problem means writing down who has it, what they’re trying to do and what stops them, before anyone draws a screen. It also says how you’ll know the problem got smaller, which [success criteria](https://ryan-di.github.io/design-field-guide/#good-success-criteria) then spell out.

When a request arrives as a solution, the frame turns it back into the problem behind it, so the team can compare more than one answer. Name the person closely enough to include how they work, for example with a keyboard only or on a small phone.

## Rules

Five rules keep a problem frame useful.

### 1. Restate the request as a problem

https://ryan-di.github.io/design-field-guide/#good-problem-framing-rule-1

A ticket often names its own answer, like “add an Export to PDF button”, and if the work starts there, the only question left is where the button goes. The request is a hint about what hurts, not a spec, so write down the problem behind it first, then look for answers.

### 2. Name the person, the moment and the obstacle

https://ryan-di.github.io/design-field-guide/#good-problem-framing-rule-2

A frame like “make settings easier to use” fits almost any design: two people can read it, picture different screens, and both feel right. Say who it is, when it happens and what gets in their way. If two readers still picture different things, narrow it again. A who that’s only a group, like “users” or “everyone”, is always too broad. The [brief check](https://ryan-di.github.io/design-field-guide/#eff-brief-check) lists the words to watch for.

### 3. Show where you saw it

https://ryan-di.github.io/design-field-guide/#good-problem-framing-rule-3

A problem nobody has seen is a guess: the team can’t tell how often it happens or how much it hurts, so the talk turns into opinions. Point to where it came from: a support message, a session you watched, a count. One real example is worth more than a paragraph of reasons.

### 4. Keep the answer out of the frame

https://ryan-di.github.io/design-field-guide/#good-problem-framing-rule-4

“People can’t find the Sort button” already holds its answer: only one design fits it, so the frame just repeats the request. Any control name in the problem, like a button, a dialog or a toggle, is the sign to look for. Describe what people are trying to get done, without naming a control. Then sketch at least two different answers.

### 5. Leave what you don’t know empty

https://ryan-di.github.io/design-field-guide/#good-problem-framing-rule-5

A frame filled with guesses reads like fact, so nobody checks it, and the team builds for a problem that may not exist. Say where each part came from: something people told you, something you read or saw, or your own guess. Look before you guess, in the support threads, tickets and notes that already exist. When nobody knows yet, leave the part empty and add it to a list of things to check. Label any guess with how you’ll check it, and when two sources disagree, show both.

## In real products

Notice how narrow each problem is: who, what they want, and what stops them. The frames are this book’s summary, not the companies’ own notes.

- Gmail: Undo send holds each email for a few seconds and offers Undo in the corner. It solves the moment of regret without an “Are you sure?” before every send. `good-problem-framing-example-01`
- Slack: threads move the replies to one message into a side panel. The channel stays readable, and the side conversation still has a home. `good-problem-framing-example-02`
- Uber: shows the car moving on the map, the minutes until pickup, and the car and its plate. Waiting becomes something riders can plan around. `good-problem-framing-example-03`
- Spotify: Discover Weekly is a fresh playlist picked for each listener every week. It removes the search step instead of making search better. `good-problem-framing-example-04`

## Related entries

[good-success-criteria](good-success-criteria.md)
