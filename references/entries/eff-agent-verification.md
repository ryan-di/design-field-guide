# Agent checks

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 29 · Build in small, reviewable steps
Live: https://ryan-di.github.io/design-field-guide/#eff-agent-verification
Kind: workflow
Cite as: Design Field Guide v35, #eff-agent-verification

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

When an agent says it’s done, ask it to show the proof: which unit tests ran, the end-to-end specs for the screens it changed, screenshots before and after, and a clean type check. Then you can see what was checked and what wasn’t.

Proof isn’t the same as trying the change. Checks cover only what someone thought to test, so the proof tells you where the agent looked. Trying the change yourself, as in [Check output that looks finished](https://ryan-di.github.io/design-field-guide/#eff-spot-plausible), covers the rest.

## Rules

Four rules keep this proof useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Ask what ran, and see the output

https://ryan-di.github.io/design-field-guide/#eff-agent-verification-rule-1

“All tests pass” is also true when no tests ran. A new test file can be empty, or the agent can run a folder that doesn’t touch the change. Ask which tests ran and have the agent paste the output. Also read the test diff: an agent can make a failing test pass by changing what the test expects.

### 2. Run the end-to-end specs for visible changes

https://ryan-di.github.io/design-field-guide/#eff-agent-verification-rule-2

Unit tests check logic, not screens, so a change can pass every unit test and still move a button people rely on, or break a flow another screen depends on. For anything people see, run the end-to-end specs that touch the changed screens, and compare screenshots from before and after.

### 3. Get screenshots for each theme, width and state

https://ryan-di.github.io/design-field-guide/#eff-agent-verification-rule-3

A screenshot in one theme at one width shows only the case that was easiest to check. Ask for light and dark, wide and narrow, and the states that matter, such as empty, error and long names. Each one catches different problems, as [Let an agent run design QA](https://ryan-di.github.io/design-field-guide/#eff-design-qa) shows.

### 4. Try it yourself anyway

https://ryan-di.github.io/design-field-guide/#eff-agent-verification-rule-4

Green checks only mean that nothing tested broke, so a case nobody thought of still gets through. Before you approve, [try it in the real app](https://ryan-di.github.io/design-field-guide/#eff-loop) for a few minutes, the way people will.

## In real products

Notice that “done” comes with proof anyone can open: a list of checks, a link, a picture.

- GitHub: each pull request lists its checks, like tests and a type check, with a pass or fail and a link to the output, so anyone can see what ran. `eff-agent-verification-example-01`
- Vercel: the preview link on each pull request lets anyone open the real change, instead of reading that it works. `eff-agent-verification-example-02`
- Chromatic: each change comes with snapshots of every Storybook story and any differences side by side, so a visual change can’t pass as “no change”. `eff-agent-verification-example-03`
- Amazon: a “Delivered” status can come with a photo of the package where it was left. You don’t have to take the status on trust, and you know where to look. `eff-agent-verification-example-04`

## Related entries

[eff-design-qa](eff-design-qa.md), [eff-loop](eff-loop.md), [eff-spot-plausible](eff-spot-plausible.md)
