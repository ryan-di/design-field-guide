# Design Field Guide

An interactive book about design: how to tell good design, the patterns and components it is built from, and how to work with agents on it.

Live: https://ryan-di.github.io/design-field-guide/ (GitHub Pages, built from `main` `/`). `live.html` only redirects there.

## Source of truth

`index.html` in this repo is the book. It is one self-contained file (CSS and JS inline). Edit it here; nothing outside the repo is needed to rebuild it.

Larger edits are written as scripts in `tools/migrations/`, one per commit, and applied once to the previous `index.html`. Each script asserts what it expects to find, so it fails instead of half-applying. Keep them as the record of what changed and why.

## Checking a change

Needs Node with Playwright (set `PW_PATH` if `@playwright/test` isn't resolvable) and Python 3 with Pillow.

```sh
node tools/check.cjs --shots /tmp/shots/after       # 1280 and 390 px, light and dark
git stash && node tools/check.cjs --shots /tmp/shots/before && git stash pop
python3 tools/shotdiff.py /tmp/shots/before /tmp/shots/after /tmp/shots/diff
```

`check.cjs` fails on console errors, broken contents links or in-page anchors, missing ids from `tools/ids-baseline.txt`, duplicate ids, empty demos, rule switches that don't work, and horizontal overflow. Ids in the baseline are cited from outside the book, so never remove or rename one; add an alias instead.
