"""python3 tools/shotdiff.py BEFORE_DIR AFTER_DIR [OUT_DIR]
Compares screenshots with the same relative path. Prints the share of changed pixels per shot and, with OUT_DIR,
writes before | after | diff strips for every shot that changed, so a person can look at them."""
import os
import sys
from PIL import Image, ImageChops

before, after = sys.argv[1], sys.argv[2]
out = sys.argv[3] if len(sys.argv) > 3 else None
rows = []
for dirpath, _, files in os.walk(before):
    for f in sorted(files):
        if not f.endswith('.png'):
            continue
        rel = os.path.relpath(os.path.join(dirpath, f), before)
        b = os.path.join(before, rel)
        a = os.path.join(after, rel)
        if not os.path.exists(a):
            rows.append((rel, None))
            continue
        ib, ia = Image.open(b).convert('RGB'), Image.open(a).convert('RGB')
        if ib.size != ia.size:
            ia = ia.resize(ib.size)
        d = ImageChops.difference(ib, ia).convert('L').point(lambda v: 255 if v > 24 else 0)
        share = sum(d.histogram()[255:]) / (d.size[0] * d.size[1])
        rows.append((rel, share))
        if out and share > 0.001:
            w, h = ib.size
            strip = Image.new('RGB', (w * 3, h), 'white')
            strip.paste(ib, (0, 0)); strip.paste(ia, (w, 0)); strip.paste(Image.merge('RGB', (d, d.point(lambda v: 0), d.point(lambda v: 0))), (w * 2, 0))
            dest = os.path.join(out, rel.replace(os.sep, '__'))
            os.makedirs(out, exist_ok=True)
            strip.save(dest)
for rel, share in rows:
    print(f"{'missing' if share is None else f'{share * 100:6.2f}%'}  {rel}")
