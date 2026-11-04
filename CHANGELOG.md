# Changelog

One line per push. Cite the book as “Design Field Guide v35, #<anchor>”; anchors listed in `tools/ids-baseline.txt` stay valid in later versions.

## v35 (2026-11)

- v35-4a: a preface, “How to read this book” (`#ch-preface`), before Start here. Parts 3 and 4 get “How each entry reads”. The demo sentence in every rule intro is now said once, in the preface.
- v35-3: `llms.txt` and `references/` for agents (one markdown file per entry and chapter, `index.json`, `rubrics.json`), generated from the page by `tools/export.py`. Page metadata for version and description.
- v35-2: four new rules: leave what you don’t know empty (`#good-problem-framing-rule-5`), hear their read first (`#good-critique-rule-4`), say what a mock can’t show (`#good-heuristic-review-rule-4`, with the fidelity table), frame a hunch as a question (`#eff-loop-rule-5`).
- v35-1: the rubrics the demos used are now tables in the text: vague words, brief check, critique kinds, loop stages, ownership split, severity 0–4, the ten heuristics, the accessibility pass. One 1–5 score scale, and the worked example uses the loop’s stage names.
- v35-0: standards-mode page shell; an anchor on every rule (`#<entry>-rule-N`) and section (`#<entry>-rules`, `-products`, `-forms`, `-ways`, `-kinds`); `live.html` redirects to the book; check tools.

## v34 (2026-11-03)

- Published as one continuous book instead of slides, with a collapsible contents rail and stable deep links.
