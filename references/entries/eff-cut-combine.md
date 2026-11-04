# Cut and combine

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 28 · Decide with judgment, not by polish
Live: https://ryan-di.github.io/design-field-guide/#eff-cut-combine
Kind: workflow
Cite as: Design Field Guide v35, #eff-cut-combine

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

When you have several design directions, the best answer is often none of them whole: it takes the strongest part of each and cuts the rest. Then you check that the parts you kept still work together as one design.

Agents make it cheap to get many directions, so the work that’s left is choosing which parts solve the problem and which only add to it. In the demo, each direction has three parts: the trigger (what starts it), the surface (what people see) and the recovery (how they get their work back).

## Rules

Four rules keep this choice useful. Each comes with a demo. Switch between “Common mistake” and “Do this instead” to see the difference.

### 1. Take directions apart

https://ryan-di.github.io/design-field-guide/#eff-cut-combine-rule-1

Each direction is usually strong in one place and weak in others, so if you pick one whole, you keep its weak parts too. Split every direction into the same parts, such as trigger, surface and recovery, and pick the best version of each part.

### 2. Cut what the problem doesn’t need

https://ryan-di.github.io/design-field-guide/#eff-cut-combine-rule-2

Good ideas pile up fast, and each one sounds worth keeping, but every part is something to build, test and explain, and people have to work out what each control does. Write the problem down and keep only the parts that solve it. The rest can wait until people ask for it.

### 3. Read the result as one story

https://ryan-di.github.io/design-field-guide/#eff-cut-combine-rule-3

Parts from different directions can contradict each other. A design can keep both a confirm dialog and an Undo toast: each makes sense alone, but together they ask people to decide twice. Describe the combined design in one sentence, from trigger to surface to recovery. If the sentence needs an “or”, cut one side.

### 4. Write down why parts were cut

https://ryan-di.github.io/design-field-guide/#eff-cut-combine-rule-4

A few weeks later, nobody remembers why a part was cut, so someone suggests it again and the team repeats the discussion or adds it back. Write one line per cut part in the ticket or the pull request, so it comes back only with new evidence.

## In real products

- GV’s design sprint: people put dot stickers on the parts they like in each sketch, not on whole sketches. The team then draws one storyboard from the best parts, which shows whether they still fit together. `eff-cut-combine-example-01`
- Basecamp’s Shape Up: a pitch ends with “No-gos”, the parts left out on purpose, so they don’t creep back in during the build. `eff-cut-combine-example-02`
- VS Code: for each merge conflict you can keep one side, the other, or both. Keeping both still needs a read, because two good changes can contradict each other, like a save prompt and an Undo on the same close. `eff-cut-combine-example-03`
- Google Pixel: Best Take works from a few group shots taken seconds apart. You pick each person’s best face, and because the shots are so close, the result still looks like one moment. `eff-cut-combine-example-04`
