# Starlight pilot

The book on [Starlight](https://starlight.astro.build/), one page per chapter. Everything under `src/content/docs/`
(except `index.mdx`), `src/fragments/`, `src/styles/book.css`, `src/sidebar.json` and `public/anchors.json` is generated
from `../index.html`; edit the book and regenerate.

```sh
python3 ../tools/starlight/convert.py      # regenerate from index.html
npm install && npx astro dev               # http://localhost:4321
node ../tools/starlight/check-pilot.cjs    # compare with the book: ids, demos, switches, errors, old anchors
```
