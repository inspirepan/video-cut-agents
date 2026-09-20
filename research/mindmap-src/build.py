# /// script
# requires-python = ">=3.10"
# ///
"""Assemble branch JSON files into the mindmap HTML."""
import json, os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = '/Users/panjx/code/video-agent/'
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'preview.html')

# id -> (side, num, color)
PLAN = [
    ('ingest',         'right', '①',  '#4C7DD9'),
    ('understand',     'right', '②',  '#2E9BB5'),
    ('brief-script',   'right', '③',  '#E08A2C'),
    ('recall',         'right', '④',  '#B8961E'),
    ('refine',         'right', '⑤',  '#D9534F'),
    ('arrange',        'right', '⑥',  '#8E5BD0'),
    ('music',          'right', '⑦',  '#D65A9E'),
    ('packaging',      'right', '⑧',  '#3FA96B'),
    ('product',        'left',  '',   '#5D6B7A'),
    ('mg',             'left',  '',   '#C2338F'),
    ('timeline-ir',    'left',  '⑨',  '#2F80ED'),
    ('render',         'left',  '⑩',  '#E0651B'),
    ('qa',             'left',  '⑪',  '#B23A48'),
    ('gui',            'left',  '⑫',  '#1FA37A'),
    ('atomic-catalog', 'left',  '',   '#7B61C8'),
    ('pitfalls',       'left',  '',   '#C2410C'),
    ('repo-map',       'left',  '',   '#6B7C93'),
]

branches = {}
for f in sorted(os.listdir(os.path.join(HERE, 'branches'))):
    if not f.endswith('.json'):
        continue
    d = json.load(open(os.path.join(HERE, 'branches', f), encoding='utf-8'))
    for b in d['branches']:
        if b['id'] in branches:
            print(f'!! duplicate branch {b["id"]} in {f}', file=sys.stderr)
        branches[b['id']] = b
        b['_file'] = f

ids = set()
missing_paths = []
warnings = []
stats = {'nodes': 0, 'atomic': 0, 'pitfalls': 0, 'refs': 0, 'l1': 0, 'l2': 0, 'l3': 0}

SRC_RE = re.compile(r'^([A-Za-z0-9_.\-/]+?)(?::(\d+))?$')

def walk(n, depth, branch_id):
    stats['nodes'] += 1
    stats[f'l{min(depth,3)}'] += 1
    if n['id'] in ids:
        warnings.append(f'duplicate id {n["id"]} (branch {branch_id})')
        n['id'] = f'{n["id"]}-{stats["nodes"]}'
    ids.add(n['id'])
    if len(n.get('title', '')) > 16:
        warnings.append(f'long title ({len(n["title"])}): {n["title"]}')
    for k in ('inputs', 'outputs', 'points'):
        if k in n and not isinstance(n[k], list):
            n[k] = [str(n[k])]
    n['atomic'] = [a for a in n.get('atomic', []) if a.get('name')]
    n['pitfalls'] = [p for p in n.get('pitfalls', []) if p.get('title')]
    refs = []
    for r in n.get('refs', []):
        p = r.get('path', '')
        if not p:
            continue
        if not os.path.exists(os.path.join(BASE, p)):
            missing_paths.append((n['id'], p))
            continue
        refs.append(r)
    n['refs'] = refs
    for p in n['pitfalls']:
        s = (p.get('source') or '').strip()
        m = SRC_RE.match(s)
        if m and '/' in m.group(1) and not os.path.exists(os.path.join(BASE, m.group(1))):
            warnings.append(f'pitfall source missing: {s} ({n["id"]})')
    stats['atomic'] += len(n['atomic'])
    stats['pitfalls'] += len(n['pitfalls'])
    stats['refs'] += len(n['refs'])
    for c in n.get('children', []):
        walk(c, depth + 1, branch_id)

ordered = []
for bid, side, num, color in PLAN:
    b = branches.get(bid)
    if not b:
        warnings.append(f'branch missing: {bid}')
        continue
    b['side'] = side
    b['num'] = num
    b['color'] = color
    b.pop('_file', None)
    stats['l1'] += 0
    walk(b, 1, bid)
    ordered.append(b)
for bid, b in branches.items():
    if bid not in [p[0] for p in PLAN]:
        warnings.append(f'unplanned branch {bid} from {b.get("_file")} -> appended left')
        b['side'] = 'left'; b['num'] = ''; b['color'] = '#888'
        b.pop('_file', None)
        walk(b, 1, bid)
        ordered.append(b)

data = {
    'root': {
        'title': '长视频集锦 Agent',
        'subtitle': '<b>原视频理解</b> → <b>LLM 按意图写脚本</b> → <b>选片 + 本地 BGM</b> → <b>合成视频</b>',
        'note': '长访谈 · 体育赛事 · MG 动效 · 35 个本地实现仓库 + 2 个云端 Skill 包 · 2026-09-06',
    },
    'branches': ordered,
    'meta': {'base': BASE, 'generatedAt': datetime.date.today().isoformat(), 'stats': stats},
}

tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
html = tpl.replace('__DATA_JSON__', payload)
open(OUT, 'w', encoding='utf-8').write(html)

print(f'wrote {OUT} ({len(html)/1024:.0f} KB)')
print('stats', json.dumps(stats, ensure_ascii=False))
if missing_paths:
    print(f'-- dropped {len(missing_paths)} refs with missing paths:')
    for nid, p in missing_paths:
        print(f'   {nid}: {p}')
if warnings:
    print(f'-- {len(warnings)} warnings:')
    for w in warnings:
        print('   ' + w)
