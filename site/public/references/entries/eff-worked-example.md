# Worked example

Design Field Guide v35 (2026-11) · Part 4 · Effective design · Chapter 31 · One problem, start to finish
Live: https://ryan-di.github.io/design-field-guide/#eff-worked-example
Kind: workflow
Cite as: Design Field Guide v35, #eff-worked-example

> Evidence boundary: this is a learning guide. Its demos and product examples are illustrations written for the book, not verified product documentation, so check a product’s own docs before citing how it behaves. Tools named in it are 2026 examples, not endorsements.

This entry follows one problem from brief to release: people lose unsaved work when they close a workflow tab. Each stage ends with one small thing someone else can read: a brief, a context pack, directions, a decision, a plan, checks and a note on what you learned. The stages follow [the loop](https://ryan-di.github.io/design-field-guide/#eff-loop), with Problem folded into the brief and the context pack as a step of its own.

With those artifacts, anyone can pick up the problem at any stage and see why it went the way it did, including you a month later. The rule demos below use smaller problems of their own.

### Stage 1 · Brief

Sample brief · Linear ticket

People lose unsaved work when they close a workflow tab.

- **Who**: People with several workflows open, tidying their tabs.
- **Trying to**: Close what they don’t need without thinking about it.
- **In the way**: A tab with changes can close before they meant to keep them.
- **Evidence**: Three support threads this month, and you lost work the same way in your own runs. To check: how often it happens.
- **Done when**: Closing a tab never throws away changes without a choice the person made.

- **You**: Name the person, the moment and what stops them. Write “done when”.
- **Agents**: Draft the brief from threads you paste in. You cut it down.

### Stage 2 · Context pack

Sample context pack · one page, linked from the ticket

- How the tab bar closes a tab *repo · subagent*
- How saving and the unsaved marker work *repo · subagent*
- Related tickets and threads *Linear · you*
- Tab, dialog and toast frames, plus tokens *Figma connector*
- Patterns: [dialog](https://ryan-di.github.io/design-field-guide/#dialog), [undo](https://ryan-di.github.io/design-field-guide/#pat-undo), [autosave](https://ryan-di.github.io/design-field-guide/#pat-autosave) *this book*

**Out of scope:** closing the whole app. Note it, don’t solve it here.

- **You**: Say what’s in scope and what isn’t.
- **Agents**: Read the repo, tickets and Figma in parallel, and summarize each in a few lines.

### Stage 3 · Three directions

- **A · Ask on close**: A dialog before the tab closes.

- **B · Close, then Undo**: Close right away, offer Undo for a while.

- **C · Keep a draft**: Close right away, offer the changes back on reopen.

Three subagents each prototyped one direction. All three went on one shared page.

- **You**: Ask for directions that differ, not three versions of one idea.
- **Agents**: Each subagent prototypes one direction. One page shows all three.

### Stage 4 · Decision

Sample scores · 1 to 5, criteria from the brief

| Criterion | A · Ask | B · Undo | C · Draft |
|---|---|---|---|
| Never loses work | 3 of 5 | 1 of 5 | 5 of 5 |
| No extra step | 1 of 5 | 5 of 5 | 5 of 5 |
| Pattern people know | 5 of 5 | 5 of 5 | 3 of 5 |
| Small to build | 5 of 5 | 5 of 5 | 1 of 5 |

Totals: A · Ask 14, B · Undo 16, C · Draft 14. Counting “never loses work” twice: A · Ask 17, B · Undo 17, C · Draft 19.

Counted once: B wins on points, but its work is gone once the toast fades. The brief says never lose work, so that criterion should count more. Counted twice: C wins: nothing is lost, even after the toast is gone. Keep B’s Undo for the moment right after closing. Record why in the ticket.

- **You**: Pick the criteria from the brief, score the directions yourself, then decide.
- **Agents**: Score them separately. You look again wherever the two disagree.

### Stage 5 · Build plan and checks

Build plan · agreed in plan mode

1. Work in its own git worktree, so main stays clean.
1. Save a draft when a tab with changes closes. Restore it on reopen. Clear it on save.
1. Show “Tab closed · Undo” right after closing.
1. Write the checks first: they should fail before the change.

Sample PR description

Keep unsaved changes when a workflow tab closes

What changes for people

- Closing a tab with changes closes it right away and offers Undo.
- Reopening that workflow offers to restore the changes.
- Tabs without changes close as before.

Checks

- Vitest: draft saved on close, restored on reopen, cleared on save.
- Playwright: close with edits, Undo, edits are back. Close, reopen, Restore.

- **You**: Approve the plan and the PR’s behavior list.
- **Agents**: Build in a worktree, write the tests, open the PR.

### Stage 6 · Evaluation plan

Sample evaluation plan · in the PR, under the behaviors

We’ll know it worked when…

- **No silent loss.** Closing a tab with changes never discards them without a choice. *Playwright spec on every PR*
- **Found without help.** People get closed work back on their own. *Watch five people close and reopen tabs*
- **Fewer reports.** No new threads about work lost on close. *Read support threads a month after release*

- **You**: Say what you’ll watch for, and when you’ll look.
- **Agents**: Run the checks on every change.

### Stage 7 · What was learned

Sample session tally · written in the ticket when it closes

- 3 directions explored
- 1 kept, plus B’s Undo
- 4 subagent runs
- 1 worktree
- 5 checks added
- 2 review rounds

**Learned:** drafts need a limit, or old ones pile up. **Next time:** ask in the brief what happens when the whole app closes.

- **You**: Write one lesson for next time.
- **Agents**: Count what happened in the session.

## Rules

Four rules keep the stages useful.

### 1. Explore directions before you build

https://ryan-di.github.io/design-field-guide/#eff-worked-example-rule-1

An agent builds fast, so it’s tempting to go from the brief straight to code. Then the first idea is the only idea, and a better one turns up in review, after the work is done. Spend that speed on [directions](https://ryan-di.github.io/design-field-guide/#eff-explore-wide) instead: ask for three different ones, and pick one before anything is built for real.

### 2. Leave one artifact per stage

https://ryan-di.github.io/design-field-guide/#eff-worked-example-rule-2

If each stage lives in your head or in a long chat, nobody else can follow it: when someone asks why you chose this design, the answer is somewhere in hundreds of messages. Leave one small artifact per stage: the brief in the ticket, the directions on a page, the decision and checks in the pull request.

### 3. Scale the stages to the problem

https://ryan-di.github.io/design-field-guide/#eff-worked-example-rule-3

Agents make every stage cheap, so it’s tempting to run all of them at full size. For a typo, three directions and a scoring table waste a day and bury a one-word change. Ask what each stage is for, and if its artifact wouldn’t change a decision, keep it to a line.

### 4. Check the result after release

https://ryan-di.github.io/design-field-guide/#eff-worked-example-rule-4

[Merged isn’t done](https://ryan-di.github.io/design-field-guide/#eff-loop): the evaluation plan only helps if someone reads it after release. Go back to it once people have used the change, check each line, and write down one thing you learned.

## In real products

Notice that each story moves through clear stages, and each stage leaves something others can read or try.

- Gmail: Undo send began as an opt-in Labs experiment for people who hit Send too soon. People could try it for years before it became a standard setting, where you choose how long to wait before the message goes. `eff-worked-example-example-01`
- Basecamp: in Shape Up, each stage leaves something others can read: the written pitch, the bet leaders place on it, and the hill chart the team updates while it builds. `eff-worked-example-example-02`
- Amazon: in “working backwards”, the press release and FAQ are the first thing the team reads and revises together, before anything is built. `eff-worked-example-example-03`
- GV: each day of the design sprint leaves something the team can see: a map and a target on Monday, sketches on Tuesday, a storyboard on Wednesday, a prototype on Thursday and interview notes on Friday. `eff-worked-example-example-04`

## Related entries

[dialog](dialog.md), [eff-explore-wide](eff-explore-wide.md), [eff-loop](eff-loop.md), [pat-autosave](pat-autosave.md), [pat-undo](pat-undo.md)
