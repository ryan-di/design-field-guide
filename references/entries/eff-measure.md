# Measure

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 30 · Check it with evidence
Live: https://ryan-di.github.io/design-field-guide/#eff-measure
Kind: workflow
Cite as: Design Field Guide v35, #eff-measure

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Measuring against the brief means choosing, before you build, the numbers that will show whether the brief’s goal was met. Each success criterion gets one number that moves only if people got what they needed. You add one number that must not get worse, and read both next to what people say.

Without this, teams count what is easy to count, and a banner can be seen a million times and still help nobody.

## Rules

Four rules keep these numbers useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Count the outcome, not the activity

https://ryan-di.github.io/design-field-guide/#eff-measure-rule-1

Views and clicks are easy to count, so they end up on the dashboard, but they rise with traffic whether or not anyone got what they came for. Count the outcome instead, as a share of the people who could have reached it, such as finished reorders out of everyone who opened a past order. Then more visitors alone can’t move the number.

### 2. Add a number that must not get worse

https://ryan-di.github.io/design-field-guide/#eff-measure-rule-2

A change can raise one number by hurting something else, so if you only watch the number you want to raise, you’ll pick the version that does the most harm. Add a guardrail: one number that must not get worse, with a limit you set before looking. In an A/B test, where each group of people gets a different version, a version that crosses the limit is out, however good the main number looks.

### 3. Pick the numbers before you build

https://ryan-di.github.io/design-field-guide/#eff-measure-rule-3

If you choose the number after release, the event you need is often missing, so you can only look at what happens to be logged, and that rarely answers the brief. Write the numbers in the brief and add their events in the same pull request. An event only needs to record that something happened, such as a suggestion being picked, so never log what people typed or made.

### 4. Read the number with what people say

https://ryan-di.github.io/design-field-guide/#eff-measure-rule-4

A number tells you that something changed, not why. A drop can mean people stopped wanting a feature, or that they can’t find it anymore. Read it next to support threads and a few [watched sessions](https://ryan-di.github.io/design-field-guide/#eff-quick-sessions), which usually explain the change.

## In real products

Notice that each team counts a number that moves only when people get what they came for, and some add one that must not get worse.

- YouTube: recommendations count watch time, not just clicks. A misleading thumbnail wins the click, but people leave early, so watch time shows whether they found what they wanted. `eff-measure-example-01`
- Google: the HEART framework starts from a goal, then names the signal that shows it, then the metric. It has a slot each for happiness, engagement, adoption, retention and task success, and teams fill only the ones that fit the goal. `eff-measure-example-02`
- Microsoft: experiments are judged on one main measure agreed before the test, plus guardrails like page load time. A win on the main number isn’t enough if a guardrail slips. `eff-measure-example-03`
- PageSpeed Insights: speed is measured the way people feel it: when the main content appears, how fast a tap gets a response, and whether the layout jumps. A page can fire its load event early and still look blank. `eff-measure-example-04`

## Related entries

[eff-quick-sessions](eff-quick-sessions.md)
