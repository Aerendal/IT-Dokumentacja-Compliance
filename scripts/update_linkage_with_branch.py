import json, re, unicodedata
from pathlib import Path

def slugify(s: str) -> str:
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s

BASE = Path(__file__).resolve().parent.parent
linkage_path = BASE / 'generated_templates' / 'linkage_index.jsonl'
branch_index_path = BASE / 'reports' / 'branch_isic_index.jsonl'
doc_branch_map_path = BASE / 'reports' / 'doc_branch_map.jsonl'

branch_index = {r['branch_id']: r for r in (json.loads(l) for l in branch_index_path.read_text().splitlines())}
branch_slug_index = {r['slug']: r for r in branch_index.values() if 'slug' in r}

doc_map = []
if doc_branch_map_path.exists():
    doc_map = [json.loads(l) for l in doc_branch_map_path.read_text().splitlines() if l.strip()]
manual_title_map = {}
manual_slug_map = {}
for m in doc_map:
    bid = m['branch_id']
    if 'title' in m:
        manual_title_map[m['title']] = bid
    if 'slug' in m:
        manual_slug_map[m['slug']] = bid

updated = []
added = 0
for line in linkage_path.read_text().splitlines():
    row = json.loads(line)
    bid = None
    # frontmatter-based branch_id if present
    if 'branch_id' in row:
        bid = row['branch_id']
    # manual title map
    if bid is None and row.get('title') in manual_title_map:
        bid = manual_title_map[row['title']]
    # manual slug map
    if bid is None:
        sl = slugify(row.get('title',''))
        if sl in manual_slug_map:
            bid = manual_slug_map[sl]
    if bid is None:
        updated.append(row)
        continue
    branch = branch_index.get(bid)
    if not branch:
        updated.append(row)
        continue
    row['branch_id'] = bid
    row['isic_code'] = branch['isic_code']
    added += 1
    updated.append(row)

linkage_path.write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in updated))
print(f'updated records: {added}/{len(updated)}')
