# Design Field Guide

An interactive book about design: how to tell good design, the patterns and components it is built from, and how to work with agents on it.

Live: https://ryan-di.github.io/design-field-guide/ (GitHub Pages, built from `main` `/`). `live.html` only redirects there.

## Source of truth

`index.html` in this repo is the book. It is one self-contained file (CSS and JS inline). Edit it here; nothing outside the repo is needed to rebuild it.

Larger edits are written as scripts in `tools/migrations/`, one per commit, and applied once to the previous `index.html`. Each script asserts what it expects to find, so it fails instead of half-applying. Keep them as the record of what changed and why.

## Exports for agents

`llms.txt` and everything in `references/` are generated from `index.html` by `tools/export.py`, so never edit them by hand. After changing the book, run:

```sh
python3 tools/export.py           # rewrites llms.txt and references/
python3 tools/find_reference.py --query "undo recovery" --limit 3
```

- `references/entries/<id>.md`: one file per entry, with a link to every section and rule
- `references/chapters/<id>.md`: chapter intros, checklists and cheat sheets
- `references/index.json`: parts, chapters, entries, rules, tables, related entries, search tags
- `references/rubrics.json`: every reference table marked `data-rubric`, with its word lists

`CHANGELOG.md` is written by hand, one line per push. The version and date come from `<meta name="dfg-version">` and `<meta name="dfg-date">` in `index.html`. Cite as “Design Field Guide v35, #<anchor>” with the live link.

## Checking a change

Needs Node with Playwright (set `PW_PATH` if `@playwright/test` isn't resolvable) and Python 3 with Pillow.

```sh
node tools/check.cjs --shots /tmp/shots/after       # 1280 and 390 px, light and dark
git stash && node tools/check.cjs --shots /tmp/shots/before && git stash pop
python3 tools/shotdiff.py /tmp/shots/before /tmp/shots/after /tmp/shots/diff
```

`check.cjs` fails on console errors, broken contents links or in-page anchors, missing ids from `tools/ids-baseline.txt`, duplicate ids, empty demos, rule switches that don't work, horizontal overflow, and exports that are stale or link to a missing anchor. After pushing, `sh tools/verify-live.sh` waits for Pages, checks the live page, and confirms it serves the same exports. Ids in the baseline are cited from outside the book, so never remove or rename one; add an alias instead.
