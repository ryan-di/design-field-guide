# The loop

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 25 · Work in a loop: frame, explore, decide, build, check
Live: https://ryan-di.github.io/design-field-guide/#eff-loop
Kind: workflow
Cite as: Design Field Guide v35, #eff-loop

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Every change goes through the same loop. Problem and Brief frame the work, then come Explore, Decide, Build and Check, and what Learn finds starts the next round. Each stage takes something in and hands something on, so a skipped stage leaves the next one guessing.

Agents make Build fast, so the stages around it matter more: framing the problem before, and checking the result after.

Each stage at a glance. [What you own, what agents do](https://ryan-di.github.io/design-field-guide/#eff-ownership) shows how the split moves with the kind of work.

Table: https://ryan-di.github.io/design-field-guide/#eff-loop-stages

| Stage | Takes in | Hands on | Who owns it |
|---|---|---|---|
| Problem | A signal: a support thread, a ticket, something you hit yourself. | One sentence: who has the problem, and what stops them. | You |
| Brief | The problem statement and what you know about it. | A short brief: the goal, limits, what’s out of scope and how you’ll know it worked. | You (agents can draft) |
| Explore | The brief. | Several real options, each with its trade-offs. | Agents, you steer |
| Decide | The options, checked against the brief. | One direction, and why, written down. | You |
| Build | The decision and the brief. | A pull request with tests. | Agents, you review |
| Check | The PR and the brief’s “how you’ll know”. | Pass or fail against the brief, plus the gaps. | Both |
| Learn | What the check found, and feedback after release. | A note, and the next problem or a sharper brief. | You |

## Rules

Five rules keep the loop useful.

### 1. Frame the problem before you build

https://ryan-di.github.io/design-field-guide/#eff-loop-rule-1

A ticket that names a fix sends the agent straight to Build, and it builds that fix quickly and well. If the fix doesn’t solve the real problem, people still have it and the fast build was wasted. [Frame the problem](https://ryan-di.github.io/design-field-guide/#good-problem-framing) and write a short brief first, so the agent explores answers to the right question.

### 2. Close the loop

https://ryan-di.github.io/design-field-guide/#eff-loop-rule-2

A merged pull request means the change shipped, not that it worked. When shipping is the last step, nobody checks, and the problems it didn’t solve come back weeks later as support requests. Check the change against the brief and write down what you learned, because that note becomes the problem for the next round.

### 3. Choose yourself, and write down why

https://ryan-di.github.io/design-field-guide/#eff-loop-rule-3

Agents are quick to build the first idea that fits. If you merge it because it’s already built, the agent made the choice, and later nobody can say why it was done this way. Ask for several options, pick one yourself, and write the reason in the ticket or the PR.

### 4. Try it in the real app

https://ryan-di.github.io/design-field-guide/#eff-loop-rule-4

Tests an agent wrote check what the agent thought of, so they can all pass while the change fails people in a case nobody listed. Open the change in the real app and walk through the brief yourself. A problem found before the merge costs minutes, not a bug report.

### 5. Frame a hunch as a question

https://ryan-di.github.io/design-field-guide/#eff-loop-rule-5

Some work starts from a hunch, with no evidence yet and a goal that’s still moving. Written as a spec, the hunch gets built as if it were known, and a whole round passes before anyone learns it was wrong. Write the brief as a question instead: what you want to find out, what you believe now and what would change your mind. Keep the rounds short, and let each Learn rewrite the brief.

## In real products

Notice how long a round runs in each: a week, eight weeks, or as long as one test takes.

- Google Ventures: the design sprint fits the loop into one week. Map the problem, sketch, decide, build a prototype, then test it with five customers on Friday. What the tests show decides the next step. `eff-loop-example-01`
- Basecamp: in Shape Up, ideas are shaped into pitches, a betting table picks which to build, and a team builds for six weeks. A two-week cool-down follows, and the next bets are placed then, so every round has a clear end and a fresh start. `eff-loop-example-02`
- Duolingo: many changes ship first as A/B tests. Some learners get the new version and the rest keep the current one. The result decides what ships, and it suggests what to test next. `eff-loop-example-03`

## Related entries

[eff-ownership](eff-ownership.md), [good-problem-framing](good-problem-framing.md)
