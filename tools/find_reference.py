#!/usr/bin/env python3
"""Search the book's exported references without loading the whole page.

python3 tools/find_reference.py --query "undo recovery" --limit 3
python3 tools/find_reference.py --id eff-brief
python3 tools/find_reference.py --kind workflow --query prototype
"""
import argparse
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def search(entries, query, kind=None):
    tokens = set(re.findall(r'[\w-]+', query.lower()))
    ranked = []
    for item in entries:
        if kind and item['kind'] != kind:
            continue
        title = (item['id'] + ' ' + item['title']).lower()
        tags = item.get('tags', '').lower()
        body = item['search_text'].lower()
        score = sum(10 * (t in title) + 6 * (t in tags) + min(body.count(t), 2) for t in tokens)
        if score:
            ranked.append((score, item))
    return [item for _, item in sorted(ranked, key=lambda p: (-p[0], p[1]['id']))]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    target = p.add_mutually_exclusive_group(required=True)
    target.add_argument('--query')
    target.add_argument('--id')
    p.add_argument('--kind', choices=['pattern', 'component', 'principle', 'workflow'])
    p.add_argument('--limit', type=int, default=5)
    args = p.parse_args()
    if not 1 <= args.limit <= 20:
        p.error('--limit must be 1 to 20')
    index = json.load(open(os.path.join(ROOT, 'references', 'index.json'), encoding='utf-8'))
    entries = index['entries']
    if args.id:
        result = [e for e in entries if e['id'] == args.id]
        if not result:
            p.error('unknown id: ' + args.id)
    else:
        result = search(entries, args.query, args.kind)[:args.limit]
    print(json.dumps({
        'version': index['version'],
        'matches': [{k: e[k] for k in ('id', 'title', 'kind', 'chapter', 'url', 'summary', 'related', 'example_ids')}
                    | {'reference': os.path.join(ROOT, e['path']), 'rules': [r['id'] for r in e['rules']]} for e in result],
        'cite': index['cite'],
        'note': 'Read the reference files you pick. No match does not mean the book never covers it.',
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
