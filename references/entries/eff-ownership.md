# Ownership

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 25 · Work in a loop: frame, explore, decide, build, check
Live: https://ryan-di.github.io/design-field-guide/#eff-ownership
Kind: workflow
Cite as: Design Field Guide v35, #eff-ownership

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

Agents are good at wide, repeatable work: searching a codebase, writing test scaffolds, making many variations. You keep the judgment: framing the problem, choosing between options and checking the result. Between agent steps, put a checkpoint where you read what came back before the next step starts.

Where [the loop](https://ryan-di.github.io/design-field-guide/#eff-loop) names the stages of a change, this entry says who owns each one. Agent output often sounds sure, but confident wording isn’t evidence, so ask for the file, the test or the screenshot behind each claim before you build on it.

An agent can draft any part of a brief, and any option or check, as long as it says where each part came from, such as a support thread, a ticket or a file. Confirming who has the problem, the evidence and the problem itself stays with you, and so do the choice between options and every judgment call. The table shows the split from the demo for each kind of work.

Table: https://ryan-di.github.io/design-field-guide/#eff-ownership-split

| Stage | Small fix | New feature | Open exploration |
|---|---|---|---|
| Problem | Reproduce it yourself. Is it really one line? | You confirm people really lose work, and when. | A hunch to test, not a spec. |
| Brief | Expected and actual, in one sentence. | An agent can draft from the ticket; you cut and sharpen. | What question should the prototypes answer? |
| Explore | An agent finds the cause. Usually one obvious option. | Subagents sketch three options in parallel. | Many quick prototypes as artifacts. |
| Decide | You approve the fix, or notice it isn’t small after all. | You pick one and write why. | You choose what to learn more about, or stop. |
| Build | The agent writes the fix and a test that failed before. | Claude Code builds in a worktree, plan first. | Throwaway build; speed over code quality. |
| Check | Tests run; you check the real app once. | Agents run tests; you close real tabs. | You watch people try it. That part is yours. |
| Learn | Is it a pattern? Note it, or close it. | You decide what becomes the next problem. | Write down what you now believe. |

## Rules

Four rules keep the split between you and agents useful.

### 1. Ask for trade-offs, not a verdict

https://ryan-di.github.io/design-field-guide/#eff-ownership-rule-1

When you ask an agent to pick the best design, it picks one and sounds sure about it, so you get a choice with nothing to check and can’t explain it later. Ask for the options and what each one is good at and costs, then make the choice yourself. If you already lean one way, write it down first, so the agent’s confident answer doesn’t become yours, as [Hear their read first](https://ryan-di.github.io/design-field-guide/#good-critique-rule-4) explains.

### 2. Hand over the wide, repetitive work

https://ryan-di.github.io/design-field-guide/#eff-ownership-rule-2

Some tasks are long only because there is a lot of the same thing: every use of a color token, every form to update, ten variations of a layout. Doing them by hand takes hours that framing and checking needed. Agents can do that work, several at once, and you spend the time you get back reading what they found.

### 3. Stop after each agent step

https://ryan-di.github.io/design-field-guide/#eff-ownership-rule-3

If exploring flows straight into planning and building, an early misreading carries all the way through, and you find out at the end, when many files have changed. Stop after each step and read what came back. Claude Code’s plan mode, where the agent proposes a plan and changes no files until you approve it, is one built-in checkpoint.

### 4. Review the plan before the build

https://ryan-di.github.io/design-field-guide/#eff-ownership-rule-4

A wrong approach takes a minute to fix in a short plan, but in a finished diff (the changed lines of code) it runs through many files, and fixing it means building again. Read the plan before the agent builds, as [Plan, then take small steps](https://ryan-di.github.io/design-field-guide/#eff-small-steps) explains.

## In real products

Notice where each tool stops and hands over to a person: before the merge, at the sliders, before Send.

- GitHub: Dependabot opens pull requests that update dependencies, with release notes inside, and the repo’s checks run on each one. It does the dull, repeated part in every repo; a person still reads and merges. `eff-ownership-example-01`
- Lightroom: Auto sets the basic tone sliders in one click. The sliders stay in view and editable, so the photographer starts from a good guess and keeps the final call. `eff-ownership-example-02`
- Gmail: Smart Reply suggests a few short answers under a message. Picking one only drafts the reply; you can edit it, and nothing goes out until you press Send. `eff-ownership-example-03`

## Related entries

[eff-loop](eff-loop.md), [eff-small-steps](eff-small-steps.md)
