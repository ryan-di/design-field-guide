# Starlight pilot

The book on [Starlight](https://starlight.astro.build/), one page per chapter. Everything under `src/content/docs/`
(except `index.mdx`), `src/fragments/`, `src/styles/book.css`, `src/sidebar.json` and `public/anchors.json` is generated
from `../index.html`; edit the book and regenerate.

```sh
python3 ../tools/starlight/convert.py      # regenerate from index.html
npm install && npx astro dev               # http://localhost:4321
node ../tools/starlight/check-pilot.cjs    # compare with the book: ids, demos, switches, errors, old anchors
node ../tools/starlight/check-notes.cjs    # check the comparison notes against the built pages
```

`annotations/` is written by hand, one JSON file per chapter. A comparison with notes there is shown as one canvas:
both demos live, each beside numbered notes whose rings and numbers sit on the element they explain. Comparisons
without notes keep the book's switch. The format is described at the top of `../tools/starlight/convert.py`.
