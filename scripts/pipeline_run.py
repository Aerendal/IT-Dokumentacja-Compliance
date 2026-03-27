#!/usr/bin/env python3
"""One-shot pipeline: build metadata, manifest v2, validate, snapshot-if-changed, prune.
Outputs go to reports/runs/<run_id>/ and reports/latest/.
Assumes CURRENT is already built (documents_current up to date, alignment_log.csv present).
"""
import csv
import hashlib
import json
import os
import shutil
import sqlite3
import sys
from collections import OrderedDict
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

# Ensure repo root is on sys.path so itdoc package is importable when
# this script is run as a subprocess (editable install may point to old path)
_SCRIPTS_DIR = Path(__file__).resolve().parent
_REPO_ROOT_PATH = _SCRIPTS_DIR.parent
for _p in (str(_REPO_ROOT_PATH), str(_SCRIPTS_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import check_no_emoji

# Config
TEMPLATES_ROOT = Path('generated_templates')
ALIGNMENT_LOG = Path('reports/alignment_log.csv')
DB_PATH = Path('reports/it_doc_matrix_clean.db')
RUNS_ROOT = Path('reports/runs')
LATEST_ROOT = Path('reports/latest')
ALLOWLIST_PATH = Path('reports/policy/dup_hash_allowlist_v2.txt')
EXEMPTIONS_PATH = Path('reports/policy/dup_content_exemptions.txt')
TAG_RULES_PATH = Path('reports/tag_rules/doc_tag_rules.csv')
HASHING_RULE_VERSION = 2
HASHING_RULE = "sha256(bytes with CRLF->LF and CR->LF normalization)"
RETENTION_WEEKLY = 12
RETENTION_MONTHLY = 12
BASELINE_ID = 1

# Thresholds (simple defaults; adjust if needed)
TH_COLLISIONS_WARN = 20   # +20 over baseline 94
TH_COLLISIONS_FAIL = 200
TH_ANOM_WARN = 200        # +200 over baseline 995
TH_ANOM_FAIL = 2000
TH_DUPHASH_WARN = 10
TH_DUPHASH_FAIL = 200

@dataclass
class Coverage:
    files_count: int
    log_count: int
    db_documents_current: int
    distinct_title_norm: int
    aligned_not_ok: int
    empty_path: int
    dup_path: int
    csv_vs_fs_missing: int
    csv_vs_fs_extra: int
    snapshot_count: int

@dataclass
class SnapshotAction:
    action: str  # CREATED or NOOP
    snapshot_id: int | None

@dataclass
class PruneReport:
    kept: list[int]
    deleted: list[int]

@dataclass
class ValidateReport:
    status: str  # PASS/WARN/FAIL
    reasons: list[str]
    metrics: dict

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H-%M-%SZ')

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def hash_v2_bytes(b: bytes) -> str:
    b = b.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return sha256_bytes(b)

# Allowlist for duplicate hashes (hash_sha256_v2)
def load_allowlist_hashes(path: Path) -> set[str]:
    if not path.exists():
        return set()
    out = set()
    for line in path.read_text(encoding='utf-8').splitlines():
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        out.add(s)
    return out

# Exemptions (path-based glob)
from pathlib import PurePosixPath

def load_exemption_patterns(path: Path) -> list[str]:
    if not path.exists():
        return []
    patterns = []
    for ln in path.read_text(encoding='utf-8').splitlines():
        s = ln.strip()
        if not s or s.startswith('#'):
            continue
        patterns.append(s)
    return patterns

def is_exempt_path(rel_path: str, patterns: list[str]) -> bool:
    # szybka ścieżka: wszystko pod imported/ traktujemy jako potencjalnie niekrytyczne duplikaty
    if rel_path.startswith('imported/'):
        return True
    p = PurePosixPath(rel_path)
    return any(p.match(g) for g in patterns)

def normalize_path_for_reports(p: str) -> str:
    p = (p or '').strip().replace('\\', '/').replace('\n', '').replace('\r', '')
    if p.startswith('./'):
        p = p[2:]
    marker = 'generated_templates/'
    ix = p.find(marker)
    if ix != -1:
        p = p[ix + len(marker):]
    return p

# Tagging support
def load_tag_rules(path: Path):
    import csv
    if not path.exists():
        return [], "missing"
    rules = []
    with path.open('r', encoding='utf-8', newline='') as f:
        rdr = csv.DictReader(f)
        required = {"rule_id","match_type","match_value","tag_type","tag_value","priority"}
        if not rdr.fieldnames or not required.issubset(set(rdr.fieldnames)):
            return [], "invalid_header"
        for row in rdr:
            rid = (row['rule_id'] or '').strip()
            # pomiń puste lub komentowane wiersze
            if not rid or rid.startswith('#'):
                continue
            try:
                rules.append({
                    'rule_id': rid,
                    'match_type': (row['match_type'] or '').strip(),
                    'match_value': (row['match_value'] or '').strip(),
                    'tag_type': (row['tag_type'] or '').strip(),
                    'tag_value': (row['tag_value'] or '').strip(),
                    'priority': int((row['priority'] or '0').strip()),
                })
            except Exception:
                continue
    return rules, "ok"

def match_rule(rule, rel_path: str) -> bool:
    mt = rule['match_type']
    mv = rule['match_value']
    if mt == 'prefix':
        return rel_path.startswith(mv)
    if mt == 'glob':
        return PurePosixPath(rel_path).match(mv)
    return False

def apply_tag_rules(cur: sqlite3.Cursor, rules_path: Path, run_dir: Path) -> dict:
    rules, status = load_tag_rules(rules_path)
    if status != 'ok':
        rep = {'status': 'FAIL', 'reason': status, 'rules_total': len(rules)}
        (run_dir/'tagging_report.json').write_text(json.dumps(rep, indent=2), encoding='utf-8')
        return rep

    cur.execute("SELECT id, path FROM documents_current")
    docs = cur.fetchall()

    matches_per_rule = {r['rule_id']: 0 for r in rules}
    inserts = []
    conflict_docs = 0

    for doc_id, path in docs:
        rel = normalize_path_for_reports(path)
        bucket = {}
        for r in rules:
            if not match_rule(r, rel):
                continue
            matches_per_rule[r['rule_id']] += 1
            tt = r['tag_type']; tv = r['tag_value']
            bucket.setdefault(tt, set()).add(tv)
        for tt, vals in bucket.items():
            if len(vals) > 1:
                conflict_docs += 1
            for tv in vals:
                inserts.append((doc_id, tt, tv))

    cur.execute("DELETE FROM document_tags_current")
    cur.executemany("INSERT OR IGNORE INTO document_tags_current(document_id, tag_type, tag_value) VALUES(?,?,?)", inserts)

    dead_rules = [rid for rid, cnt in matches_per_rule.items() if cnt == 0]
    rep = {
        'status': 'OK',
        'rules_total': len(rules),
        'dead_rules': len(dead_rules),
        'dead_rules_ids': dead_rules[:50],
        'conflicts_docs': conflict_docs,
        'inserted_rows': len(inserts),
        'rules_path': str(rules_path),
    }
    (run_dir/'tagging_report.json').write_text(json.dumps(rep, indent=2), encoding='utf-8')
    return rep

# Transitions (snapshot N-1 -> N)
def previous_snapshot_id(cur: sqlite3.Cursor, snapshot_id: int) -> int | None:
    cur.execute('SELECT snapshot_id FROM snapshots WHERE snapshot_id < ? ORDER BY snapshot_id DESC LIMIT 1', (snapshot_id,))
    row = cur.fetchone()
    return row[0] if row else None

def _load_snapshot_index(cur: sqlite3.Cursor, snapshot_id: int) -> dict[str, dict]:
    idx: dict[str, dict] = {}
    cur.execute('SELECT path, hash_sha256_v2, template_id FROM documents_snapshot WHERE snapshot_id=?', (snapshot_id,))
    for path, h, tid in cur.fetchall():
        key = (tid or '').strip()
        kind = 'template_id'
        if not key:
            key = h
            kind = 'hash_sha256_v2'
        if not key:
            continue
        bucket = idx.setdefault(key, {'kind': kind, 'paths': []})
        bucket['paths'].append(path)
    return idx

def compute_transitions(cur: sqlite3.Cursor, from_snapshot_id: int, to_snapshot_id: int, run_dir: Path) -> dict:
    idx_from = _load_snapshot_index(cur, from_snapshot_id)
    idx_to = _load_snapshot_index(cur, to_snapshot_id)

    common_keys = sorted(set(idx_from.keys()) & set(idx_to.keys()))

    moves = []
    ambiguous_changed = 0
    changed_clusters = 0
    unchanged_clusters = 0
    examples_ambiguous = []

    for key in common_keys:
        prev_paths = idx_from[key]['paths']
        curr_paths = idx_to[key]['paths']
        prev_set = set(prev_paths)
        curr_set = set(curr_paths)

        if prev_set == curr_set:
            unchanged_clusters += 1
            continue

        changed_clusters += 1
        removed = sorted(list(prev_set - curr_set))
        added = sorted(list(curr_set - prev_set))

        if len(removed) == 1 and len(added) == 1:
            kind = 'template_id' if (idx_from[key]['kind'] == 'template_id' or idx_to[key]['kind'] == 'template_id') else 'hash_sha256_v2'
            moves.append({
                'identity_kind': kind,
                'identity_key': key,
                'old_path': removed[0],
                'new_path': added[0],
            })
        else:
            ambiguous_changed += 1
            if len(examples_ambiguous) < 10:
                examples_ambiguous.append({
                    'identity_key': key,
                    'removed': removed,
                    'added': added,
                })

    # persist to DB (idempotent per pair)
    cur.execute('DELETE FROM path_transitions WHERE from_snapshot_id=? AND to_snapshot_id=?', (from_snapshot_id, to_snapshot_id))
    now = utc_now_iso()
    rows = [(from_snapshot_id, to_snapshot_id, m['identity_key'], m['old_path'], m['new_path'], now, m['identity_kind'], '') for m in moves]
    if rows:
        cur.executemany('''
            INSERT INTO path_transitions(
              from_snapshot_id, to_snapshot_id, identity_key, old_path, new_path, detected_at_utc, identity_kind, note
            ) VALUES (?,?,?,?,?,?,?,?)
        ''', rows)

    # write CSV + report
    csv_path = run_dir / 'transitions.csv'
    with csv_path.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['identity_kind','identity_key','old_path','new_path'])
        for m in moves:
            w.writerow([m['identity_kind'], m['identity_key'], m['old_path'], m['new_path']])

    rep = {
        'status': 'OK',
        'from_snapshot_id': from_snapshot_id,
        'to_snapshot_id': to_snapshot_id,
        'common_keys': len(common_keys),
        'unchanged_clusters': unchanged_clusters,
        'changed_clusters': changed_clusters,
        'moves_detected': len(moves),
        'ambiguous_changed_clusters': ambiguous_changed,
        'csv': csv_path.name,
        'ambiguous_examples': examples_ambiguous,
    }
    (run_dir/'transitions_report.json').write_text(json.dumps(rep, indent=2), encoding='utf-8')
    return rep

# Diff snapshot → snapshot (added/removed/changed)
def _load_snapshot_map(cur: sqlite3.Cursor, snapshot_id: int) -> dict[str, str]:
    """Return {path: hash_sha256_v2} for a snapshot."""
    cur.execute('SELECT path, hash_sha256_v2 FROM documents_snapshot WHERE snapshot_id=?', (snapshot_id,))
    return {path: h for path, h in cur.fetchall()}

def compute_snapshot_diff(cur: sqlite3.Cursor, from_snapshot_id: int, to_snapshot_id: int, run_dir: Path) -> dict:
    old_map = _load_snapshot_map(cur, from_snapshot_id)
    new_map = _load_snapshot_map(cur, to_snapshot_id)

    old_paths = set(old_map.keys())
    new_paths = set(new_map.keys())

    added = sorted(list(new_paths - old_paths))
    removed = sorted(list(old_paths - new_paths))

    changed = []
    unchanged = 0
    for p in sorted(old_paths & new_paths):
        if old_map[p] != new_map[p]:
            changed.append(p)
        else:
            unchanged += 1

    csv_path = run_dir / 'snapshot_diff.csv'
    with csv_path.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['kind','path'])
        for p in added:
            w.writerow(['added', p])
        for p in removed:
            w.writerow(['removed', p])
        for p in changed:
            w.writerow(['changed', p])

    rep = {
        'status': 'OK',
        'from_snapshot_id': from_snapshot_id,
        'to_snapshot_id': to_snapshot_id,
        'added': len(added),
        'removed': len(removed),
        'changed': len(changed),
        'unchanged': unchanged,
        'csv': csv_path.name,
        'examples': {
            'added': added[:10],
            'removed': removed[:10],
            'changed': changed[:10],
        }
    }
    (run_dir/'snapshot_diff_report.json').write_text(json.dumps(rep, indent=2), encoding='utf-8')
    return rep

# Runs log (insert/refresh metrics)
def record_run_metrics(db_path: Path, run_id: str, started_at_utc: str, finished_at_utc: str, pipeline_result: dict, pipeline_result_sha: str):
    # sanity: artifacts_dir must exist and pipeline_result.json must match SHA
    artifacts_dir = Path(pipeline_result.get('run_dir'))
    pr_path = artifacts_dir / 'pipeline_result.json'
    if not artifacts_dir.exists():
        raise ValueError(f"artifacts_dir does not exist: {artifacts_dir}")
    if not pr_path.exists():
        raise ValueError(f"pipeline_result.json missing in artifacts_dir: {pr_path}")
    pr_disk_sha = sha256_bytes(pr_path.read_bytes())
    if pr_disk_sha != pipeline_result_sha:
        raise ValueError(f"pipeline_result sha mismatch (computed {pipeline_result_sha} vs disk {pr_disk_sha})")

    artifacts_dir_str = str(artifacts_dir)
    status = pipeline_result.get('status')
    manifest_hash = pipeline_result.get('manifest_hash_v2')
    alignment_hash = pipeline_result.get('alignment_log_hash')
    hashing_rule_version = pipeline_result.get('dup_content_policy', {}).get('hashing_rule_version', HASHING_RULE_VERSION)
    policy_version_dup = pipeline_result.get('dup_content_policy', {}).get('policy_version')
    dup_exemptions_path = pipeline_result.get('dup_content_policy', {}).get('exemptions_path')

    docs_count = pipeline_result.get('coverage_db', {}).get('files_count')
    anomalies_total = pipeline_result.get('validate', {}).get('metrics', {}).get('anomalies_total')

    dup_clusters_total = pipeline_result.get('dup_content_policy', {}).get('dup_hash_clusters_total')
    dup_clusters_exempt_only = pipeline_result.get('dup_content_policy', {}).get('dup_hash_clusters_exempt_only')
    dup_clusters_unexpected = pipeline_result.get('dup_content_policy', {}).get('dup_hash_clusters_unexpected')

    tags_inserted_rows = pipeline_result.get('tagging', {}).get('inserted_rows')
    tags_dead_rules = pipeline_result.get('tagging', {}).get('dead_rules')
    tags_conflicts_docs = pipeline_result.get('tagging', {}).get('conflicts_docs')

    snapshot_status = pipeline_result.get('snapshot', {}).get('action') or pipeline_result.get('snapshot', {}).get('status')
    snapshot_id = pipeline_result.get('snapshot', {}).get('snapshot_id')

    diff = pipeline_result.get('snapshot_diff', {}) or {}
    diff_added = diff.get('added')
    diff_removed = diff.get('removed')
    diff_changed = diff.get('changed')
    diff_unchanged = diff.get('unchanged')

    transitions = pipeline_result.get('transitions', {}) or {}
    moves_detected = transitions.get('moves_detected')
    ambiguous_changed_clusters = transitions.get('ambiguous_changed_clusters')
    unchanged_clusters = transitions.get('unchanged_clusters')
    changed_clusters = transitions.get('changed_clusters')

    manual_meta = pipeline_result.get('manual_meta_sla') or {}
    manual_meta_total = manual_meta.get('total')
    manual_meta_resolved = manual_meta.get('resolved')
    manual_meta_pass = None
    if manual_meta.get('pass') is not None:
        manual_meta_pass = 1 if manual_meta.get('pass') else 0

    conn = sqlite3.connect(str(db_path))
    conn.execute('PRAGMA foreign_keys=ON;')
    cur = conn.cursor()

    # ensure columns for manual/meta SLA
    cur.execute("PRAGMA table_info(runs)")
    cols = {r[1] for r in cur.fetchall()}
    for col in ("manual_meta_total", "manual_meta_resolved", "manual_meta_pass"):
        if col not in cols:
            cur.execute(f"ALTER TABLE runs ADD COLUMN {col} INTEGER")

    cur.execute('''
        INSERT INTO runs(
          run_id, started_at_utc, finished_at_utc, status,
          artifacts_dir,
          templates_manifest_hash_v2, alignment_log_hash_sha256, hashing_rule_version,
          policy_version_dup, dup_exemptions_path,
          docs_count, anomalies_total,
          dup_clusters_total, dup_clusters_exempt_only, dup_clusters_unexpected,
          tags_inserted_rows, tags_dead_rules, tags_conflicts_docs,
          snapshot_status, snapshot_id,
          diff_added, diff_removed, diff_changed, diff_unchanged,
          moves_detected, ambiguous_changed_clusters, unchanged_clusters, changed_clusters,
          manual_meta_total, manual_meta_resolved, manual_meta_pass,
          pipeline_result_sha256
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(run_id) DO UPDATE SET
          finished_at_utc=excluded.finished_at_utc,
          status=excluded.status,
          artifacts_dir=excluded.artifacts_dir,
          templates_manifest_hash_v2=excluded.templates_manifest_hash_v2,
          alignment_log_hash_sha256=excluded.alignment_log_hash_sha256,
          hashing_rule_version=excluded.hashing_rule_version,
          policy_version_dup=excluded.policy_version_dup,
          dup_exemptions_path=excluded.dup_exemptions_path,
          docs_count=excluded.docs_count,
          anomalies_total=excluded.anomalies_total,
          dup_clusters_total=excluded.dup_clusters_total,
          dup_clusters_exempt_only=excluded.dup_clusters_exempt_only,
          dup_clusters_unexpected=excluded.dup_clusters_unexpected,
          tags_inserted_rows=excluded.tags_inserted_rows,
          tags_dead_rules=excluded.tags_dead_rules,
          tags_conflicts_docs=excluded.tags_conflicts_docs,
          snapshot_status=excluded.snapshot_status,
          snapshot_id=excluded.snapshot_id,
          diff_added=excluded.diff_added,
          diff_removed=excluded.diff_removed,
          diff_changed=excluded.diff_changed,
          diff_unchanged=excluded.diff_unchanged,
          moves_detected=excluded.moves_detected,
          ambiguous_changed_clusters=excluded.ambiguous_changed_clusters,
          unchanged_clusters=excluded.unchanged_clusters,
          changed_clusters=excluded.changed_clusters,
          manual_meta_total=excluded.manual_meta_total,
          manual_meta_resolved=excluded.manual_meta_resolved,
          manual_meta_pass=excluded.manual_meta_pass,
          pipeline_result_sha256=excluded.pipeline_result_sha256
    ''', (
        run_id, started_at_utc, finished_at_utc, status,
        artifacts_dir_str,
        manifest_hash, alignment_hash, hashing_rule_version,
        policy_version_dup, dup_exemptions_path,
        docs_count, anomalies_total,
        dup_clusters_total, dup_clusters_exempt_only, dup_clusters_unexpected,
        tags_inserted_rows, tags_dead_rules, tags_conflicts_docs,
        snapshot_status, snapshot_id,
        diff_added, diff_removed, diff_changed, diff_unchanged,
        moves_detected, ambiguous_changed_clusters, unchanged_clusters, changed_clusters,
        manual_meta_total, manual_meta_resolved, manual_meta_pass,
        pipeline_result_sha
    ))
    conn.commit()
    conn.close()

def ensure_dirs(run_dir: Path):
    run_dir.mkdir(parents=True, exist_ok=True)
    LATEST_ROOT.mkdir(parents=True, exist_ok=True)
    ALLOWLIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXEMPTIONS_PATH.parent.mkdir(parents=True, exist_ok=True)

# Emoji guard
def emoji_check(root: Path, run_dir: Path) -> dict:
    problems = []
    total_files = 0
    total_hits = 0
    for path in check_no_emoji.iter_text_files(root):
        total_files += 1
        hits = check_no_emoji.scan_file(path)
        if hits:
            total_hits += len(hits)
            # keep only first few lines to avoid huge logs
            problems.append({
                'path': str(path),
                'lines': [{'lineno': ln, 'text': line} for ln, line in hits[:5]],
                'hit_count': len(hits),
            })
    status = 'PASS' if not problems else 'FAIL'
    rep = {
        'status': status,
        'files_scanned': total_files,
        'emoji_lines': total_hits,
        'problem_files': problems[:50],  # cap to keep report small
    }
    (run_dir / 'emoji_report.json').write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding='utf-8')
    return rep

# DB helpers
def table_has_column(cur, table: str, col: str) -> bool:
    cur.execute(f"PRAGMA table_info({table})")
    return any(r[1] == col for r in cur.fetchall())

def ensure_schema(conn: sqlite3.Connection):
    cur = conn.cursor()
    # runs log (additive)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS runs (
          run_id TEXT PRIMARY KEY,
          started_at_utc TEXT NOT NULL,
          finished_at_utc TEXT NOT NULL,
          status TEXT NOT NULL,
          artifacts_dir TEXT NOT NULL,
          templates_manifest_hash_v2 TEXT,
          alignment_log_hash_sha256 TEXT,
          hashing_rule_version INTEGER,
          policy_version_dup INTEGER,
          dup_exemptions_path TEXT,
          docs_count INTEGER,
          anomalies_total INTEGER,
          dup_clusters_total INTEGER,
          dup_clusters_exempt_only INTEGER,
          dup_clusters_unexpected INTEGER,
          tags_inserted_rows INTEGER,
          tags_dead_rules INTEGER,
          tags_conflicts_docs INTEGER,
          snapshot_status TEXT,
          snapshot_id INTEGER,
          diff_added INTEGER,
          diff_removed INTEGER,
          diff_changed INTEGER,
          diff_unchanged INTEGER,
          moves_detected INTEGER,
          ambiguous_changed_clusters INTEGER,
          unchanged_clusters INTEGER,
          changed_clusters INTEGER,
          pipeline_result_sha256 TEXT NOT NULL
        )
    ''')
    cur.execute('CREATE INDEX IF NOT EXISTS idx_runs_finished_at ON runs(finished_at_utc)')
    cur.execute('CREATE INDEX IF NOT EXISTS idx_runs_status ON runs(status)')
    cur.execute('CREATE INDEX IF NOT EXISTS idx_runs_manifest ON runs(templates_manifest_hash_v2)')
    cur.execute('CREATE INDEX IF NOT EXISTS idx_runs_snapshot_id ON runs(snapshot_id)')
    # path_transitions base table (additive, safe if exists)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS path_transitions (
          id INTEGER PRIMARY KEY,
          from_snapshot_id INTEGER NOT NULL REFERENCES snapshots(snapshot_id) ON DELETE CASCADE,
          to_snapshot_id   INTEGER NOT NULL REFERENCES snapshots(snapshot_id) ON DELETE CASCADE,
          identity_key TEXT NOT NULL,
          old_path TEXT NOT NULL,
          new_path TEXT NOT NULL,
          detected_at_utc TEXT NOT NULL,
          identity_kind TEXT,
          note TEXT
        )
    ''')
    # documents tables
    if not table_has_column(cur, 'documents_current', 'hash_sha256_v2'):
        cur.execute('ALTER TABLE documents_current ADD COLUMN hash_sha256_v2 TEXT')
        cur.execute('CREATE INDEX IF NOT EXISTS idx_doc_current_hash_v2 ON documents_current(hash_sha256_v2)')
    if not table_has_column(cur, 'documents_current', 'template_id'):
        cur.execute('ALTER TABLE documents_current ADD COLUMN template_id TEXT')
        cur.execute('CREATE INDEX IF NOT EXISTS idx_doc_current_template_id ON documents_current(template_id)')
    if not table_has_column(cur, 'documents_snapshot', 'hash_sha256_v2'):
        cur.execute('ALTER TABLE documents_snapshot ADD COLUMN hash_sha256_v2 TEXT')
        cur.execute('CREATE INDEX IF NOT EXISTS idx_doc_snap_hash_v2 ON documents_snapshot(snapshot_id, hash_sha256_v2)')
    if not table_has_column(cur, 'documents_snapshot', 'template_id'):
        cur.execute('ALTER TABLE documents_snapshot ADD COLUMN template_id TEXT')
        cur.execute('CREATE INDEX IF NOT EXISTS idx_doc_snap_template_id ON documents_snapshot(snapshot_id, template_id)')
    # snapshot meta
    meta_cols = [
        ('templates_manifest_hash_v2','TEXT'),
        ('alignment_log_hash_sha256','TEXT'),
        ('hashing_rule_version','INTEGER'),
        ('hashing_rule','TEXT'),
        ('templates_count','INTEGER'),
        ('anomalies_total','INTEGER'),
        ('collisions_title_norm','INTEGER'),
    ]
    for c,t in meta_cols:
        if not table_has_column(cur, 'snapshots', c):
            cur.execute(f'ALTER TABLE snapshots ADD COLUMN {c} {t}')
    cur.execute('CREATE INDEX IF NOT EXISTS idx_snap_manifest_hash_v2 ON snapshots(templates_manifest_hash_v2)')
    # path_transitions note/identity_kind if absent
    cur.execute('PRAGMA table_info(path_transitions)')
    cols = [r[1] for r in cur.fetchall()]
    if 'identity_kind' not in cols:
        cur.execute('ALTER TABLE path_transitions ADD COLUMN identity_kind TEXT')
        cur.execute('CREATE INDEX IF NOT EXISTS idx_transitions_identity_kind ON path_transitions(identity_kind)')
    if 'note' not in cols:
        cur.execute('ALTER TABLE path_transitions ADD COLUMN note TEXT')
    conn.commit()


# CSV coverage (FS vs alignment_log paths) – BOM/ delimiter / alt path columns safe
def _detect_delimiter(sample: str) -> str:
    semi = sample.count(';')
    comma = sample.count(',')
    tab = sample.count('\\t')
    if tab > semi and tab > comma:
        return '\\t'
    return ';' if semi > comma else ','

def _sanitize_csv_bom_copy(src: Path, dst: Path) -> dict:
    raw = src.read_bytes()
    bom = b"\\xef\\xbb\\xbf"
    had_bom = raw.startswith(bom)
    dst.write_bytes(raw[len(bom):] if had_bom else raw)
    return {"had_bom": had_bom, "sanitized_path": str(dst)}

def _open_dictreader(csv_path: Path):
    f = open(csv_path, "r", encoding="utf-8-sig", newline="")
    pos = f.tell(); sample = f.read(8192); f.seek(pos)
    delim = _detect_delimiter(sample)
    rdr = csv.DictReader(f, delimiter=delim)
    raw_fn = rdr.fieldnames[:] if rdr.fieldnames else None
    if rdr.fieldnames:
        rdr.fieldnames = [fn.replace("\\ufeff", "").strip() for fn in rdr.fieldnames]
    norm_fn = rdr.fieldnames[:] if rdr.fieldnames else None
    header_diag = {"raw": raw_fn, "normalized": norm_fn}
    return rdr, f, delim, header_diag

def _detect_path_column(fieldnames):
    if not fieldnames:
        return None
    candidates = ["path", "Path", "relative_path", "template_path", "file_path", "rel_path"]
    fset = set(fieldnames)
    for c in candidates:
        if c in fset:
            return c
    for fn in fieldnames:
        if fn.strip().lower() == "path":
            return fn
    return None

def _normalize_rel_path(p: str) -> str:
    p = (p or "").strip().lstrip("\\ufeff").replace("\\\\", "/")
    if p.startswith("./"):
        p = p[2:]
    marker = "generated_templates/"
    if marker in p:
        p = p[p.find(marker) + len(marker):]
    return p

def coverage_report(run_dir: Path) -> dict:
    fs_paths = sorted([p.relative_to(TEMPLATES_ROOT).as_posix() for p in TEMPLATES_ROOT.rglob('*.md') if p.is_file()])
    fs_set = set(fs_paths)

    sanitized = _sanitize_csv_bom_copy(ALIGNMENT_LOG, run_dir / "alignment_log_sanitized.csv")
    rdr, f, delim, header_diag = _open_dictreader(Path(sanitized["sanitized_path"]))
    first_rows_diag = []
    try:
        path_col = _detect_path_column(rdr.fieldnames)
        if not path_col:
            rep = {
                "status": "FAIL",
                "reason": "missing path column",
                "fieldnames": rdr.fieldnames,
                "delimiter_detected": delim,
                "had_bom": sanitized["had_bom"],
                "sanitized_csv": sanitized["sanitized_path"],
                "header_diag": header_diag,
            }
            (run_dir/'csv_coverage_report.json').write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding='utf-8')
            return rep

        seen_raw = []
        for i, row in enumerate(rdr):
            if i < 3:
                first_rows_diag.append(row)
            v = row.get(path_col)
            if v:
                seen_raw.append(_normalize_rel_path(v))
    finally:
        f.close()

    dup = 0; seen_set = set()
    for p in seen_raw:
        if p in seen_set: dup += 1
        seen_set.add(p)
    csv_set = set(seen_set)
    files_without_log = sorted(list(fs_set - csv_set))
    log_without_files = sorted(list(csv_set - fs_set))
    status = 'PASS' if (dup==0 and not files_without_log and not log_without_files) else 'FAIL'
    rep = {
        'status': status,
        'repo_paths': len(fs_set),
        'log_paths': len(csv_set),
        'duplicate_log_paths': dup,
        'files_without_log_row': len(files_without_log),
        'log_rows_without_file': len(log_without_files),
        'examples': {
            'files_without_log_row': files_without_log[:20],
            'log_rows_without_file': log_without_files[:20],
        },
        'delimiter_detected': delim,
        'path_column_used': path_col,
        'had_bom': sanitized['had_bom'],
        'sanitized_csv': sanitized['sanitized_path'],
        'header_diag': header_diag,
        'first_rows_diag': first_rows_diag,
    }
    (run_dir/'csv_coverage_report.json').write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding='utf-8')
    return rep


# Diagnostics: collisions and duplicate hashes
def diagnostics_report(db_path: Path, run_dir: Path) -> dict:
    conn = sqlite3.connect(str(db_path)); cur = conn.cursor()
    col_csv = run_dir/'collision_title_norm.csv'
    cur.execute("""
      SELECT title_norm, COUNT(*) AS cnt
      FROM documents_current
      GROUP BY title_norm
      HAVING cnt > 1
      ORDER BY cnt DESC, title_norm
    """)
    norms = cur.fetchall()
    with col_csv.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['title_norm','count','title','path','source'])
        for tn,cnt in norms:
            cur.execute("SELECT title, path, source FROM documents_current WHERE title_norm=? ORDER BY path", (tn,))
            for title,path,source in cur.fetchall():
                w.writerow([tn,cnt,title,path,source])

    dup_csv = run_dir/'dup_content_hashes.csv'
    cur.execute("""
      SELECT hash_sha256_v2, COUNT(*) AS cnt
      FROM documents_current
      WHERE hash_sha256_v2 IS NOT NULL
      GROUP BY hash_sha256_v2
      HAVING cnt > 1
      ORDER BY cnt DESC, hash_sha256_v2
    """)
    dups = cur.fetchall()
    allow = load_allowlist_hashes(ALLOWLIST_PATH)
    patterns = load_exemption_patterns(EXEMPTIONS_PATH)

    # classify per hash: exempt-only vs unexpected (path-based)
    dup_allowed = sum(1 for h,_cnt in dups if h in allow)

    def cluster_is_exempt_only(hash_val: str) -> bool:
        cur.execute("SELECT path FROM documents_current WHERE hash_sha256_v2=?", (hash_val,))
        paths = [normalize_path_for_reports(p) for (p,) in cur.fetchall()]
        return all(is_exempt_path(p, patterns) for p in paths)

    dup_exempt_only = 0
    for h,_cnt in dups:
        if cluster_is_exempt_only(h):
            dup_exempt_only += 1
    dup_unexpected_clusters = len(dups) - dup_exempt_only

    with dup_csv.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['hash_sha256_v2','count','path'])
        for h,cnt in dups:
            cur.execute("SELECT path FROM documents_current WHERE hash_sha256_v2=? ORDER BY path", (h,))
            for (path,) in cur.fetchall():
                w.writerow([h,cnt,normalize_path_for_reports(path)])

    rep = {
        'collisions_title_norm': len(norms),
        'dup_content_hashes': len(dups),
        'dup_content_hashes_allowed': dup_allowed,
        'dup_content_hashes_exempt_only': dup_exempt_only,
        'dup_content_hashes_unexpected_clusters': dup_unexpected_clusters,
        'dup_hash_allowlist_path': str(ALLOWLIST_PATH),
        'dup_hash_exemptions_path': str(EXEMPTIONS_PATH),
        'collision_title_norm_csv': col_csv.name,
        'dup_content_hashes_csv': dup_csv.name
    }
    (run_dir/'diagnostics_report.json').write_text(json.dumps(rep, indent=2), encoding='utf-8')
    conn.close(); return rep


# CSV coverage (FS vs alignment_log paths)
def _detect_delimiter(sample: str) -> str:
    semi = sample.count(';')
    comma = sample.count(',')
    tab = sample.count('\\t')
    if tab > semi and tab > comma:
        return '\\t'
    return ';' if semi > comma else ','

def _sanitize_csv_bom_copy(src: Path, dst: Path) -> dict:
    raw = src.read_bytes()
    bom = b"\\xef\\xbb\\xbf"
    had_bom = raw.startswith(bom)
    dst.write_bytes(raw[len(bom):] if had_bom else raw)
    return {"had_bom": had_bom, "sanitized_path": str(dst)}

def _open_dictreader(csv_path: Path):
    f = open(csv_path, "r", encoding="utf-8-sig", newline="")
    pos = f.tell(); sample = f.read(8192); f.seek(pos)
    delim = _detect_delimiter(sample)
    rdr = csv.DictReader(f, delimiter=delim)
    raw_fn = rdr.fieldnames[:] if rdr.fieldnames else None
    if rdr.fieldnames:
        rdr.fieldnames = [fn.replace("\\ufeff", "").strip() for fn in rdr.fieldnames]
    norm_fn = rdr.fieldnames[:] if rdr.fieldnames else None
    header_diag = {"raw": raw_fn, "normalized": norm_fn}
    return rdr, f, delim, header_diag

def _detect_path_column(fieldnames):
    if not fieldnames:
        return None
    candidates = ["path", "Path", "relative_path", "template_path", "file_path", "rel_path"]
    fset = set(fieldnames)
    for c in candidates:
        if c in fset:
            return c
    for fn in fieldnames:
        if fn.strip().lower() == "path":
            return fn
    return None

def _normalize_rel_path(p: str) -> str:
    p = (p or "").strip().lstrip("\\ufeff").replace("\\\\", "/")
    if p.startswith("./"):
        p = p[2:]
    marker = "generated_templates/"
    if marker in p:
        p = p[p.find(marker) + len(marker):]
    return p

def coverage_report(run_dir: Path) -> dict:
    fs_paths = sorted([p.relative_to(TEMPLATES_ROOT).as_posix() for p in TEMPLATES_ROOT.rglob('*.md') if p.is_file()])
    fs_set = set(fs_paths)

    sanitized = _sanitize_csv_bom_copy(ALIGNMENT_LOG, run_dir / "alignment_log_sanitized.csv")
    rdr, f, delim, header_diag = _open_dictreader(Path(sanitized["sanitized_path"]))
    first_rows_diag = []
    try:
        path_col = _detect_path_column(rdr.fieldnames)
        if not path_col:
            rep = {
                "status": "FAIL",
                "reason": "missing path column",
                "fieldnames": rdr.fieldnames,
                "delimiter_detected": delim,
                "had_bom": sanitized["had_bom"],
                "sanitized_csv": sanitized["sanitized_path"],
                "header_diag": header_diag,
            }
            (run_dir/'csv_coverage_report.json').write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding='utf-8')
            return rep

        seen_raw = []
        for i, row in enumerate(rdr):
            if i < 3:
                first_rows_diag.append(row)
            v = row.get(path_col)
            if v:
                seen_raw.append(_normalize_rel_path(v))
    finally:
        f.close()

    dup = 0; seen_set = set()
    for p in seen_raw:
        if p in seen_set: dup += 1
        seen_set.add(p)
    csv_set = set(seen_set)
    files_without_log = sorted(list(fs_set - csv_set))
    log_without_files = sorted(list(csv_set - fs_set))
    status = 'PASS' if (dup==0 and not files_without_log and not log_without_files) else 'FAIL'
    rep = {
        'status': status,
        'repo_paths': len(fs_set),
        'log_paths': len(csv_set),
        'duplicate_log_paths': dup,
        'files_without_log_row': len(files_without_log),
        'log_rows_without_file': len(log_without_files),
        'examples': {
            'files_without_log_row': files_without_log[:20],
            'log_rows_without_file': log_without_files[:20],
        },
        'delimiter_detected': delim,
        'path_column_used': path_col,
        'had_bom': sanitized['had_bom'],
        'sanitized_csv': sanitized['sanitized_path'],
        'header_diag': header_diag,
        'first_rows_diag': first_rows_diag,
    }
    (run_dir/'csv_coverage_report.json').write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding='utf-8')
    return rep


# Diagnostics: collisions and duplicate hashes
def diagnostics_report(db_path: Path, run_dir: Path) -> dict:
    conn = sqlite3.connect(str(db_path)); cur = conn.cursor()
    # collisions
    col_csv = run_dir/'collision_title_norm.csv'
    cur.execute("""
      SELECT title_norm, COUNT(*) AS cnt
      FROM documents_current
      GROUP BY title_norm
      HAVING cnt > 1
      ORDER BY cnt DESC, title_norm
    """)
    norms = cur.fetchall()
    with col_csv.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['title_norm','count','title','path','source'])
        for tn,cnt in norms:
            cur.execute("SELECT title, path, source FROM documents_current WHERE title_norm=? ORDER BY path", (tn,))
            for title,path,source in cur.fetchall():
                w.writerow([tn,cnt,title,path,source])

    # duplicate hashes (v2) - classify by path-based exemptions
    dup_csv = run_dir/'dup_content_hashes.csv'
    cur.execute("""
      SELECT hash_sha256_v2, COUNT(*) AS cnt
      FROM documents_current
      WHERE hash_sha256_v2 IS NOT NULL
      GROUP BY hash_sha256_v2
      HAVING cnt > 1
      ORDER BY cnt DESC, hash_sha256_v2
    """)
    dups = cur.fetchall()

    patterns = load_exemption_patterns(EXEMPTIONS_PATH)
    allow = load_allowlist_hashes(ALLOWLIST_PATH)

    def cluster_is_exempt_only(hash_val: str) -> bool:
        cur.execute("SELECT path FROM documents_current WHERE hash_sha256_v2=?", (hash_val,))
        paths = [normalize_path_for_reports(p) for (p,) in cur.fetchall()]
        return all(is_exempt_path(p, patterns) for p in paths)

    dup_exempt_only = 0
    for h,_cnt in dups:
        if cluster_is_exempt_only(h):
            dup_exempt_only += 1

    dup_allowed = sum(1 for h,_cnt in dups if h in allow)
    dup_unexpected_clusters = len(dups) - dup_exempt_only

    with dup_csv.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['hash_sha256_v2','count','path'])
        for h,cnt in dups:
            cur.execute("SELECT path FROM documents_current WHERE hash_sha256_v2=? ORDER BY path", (h,))
            for (path,) in cur.fetchall():
                w.writerow([h,cnt,normalize_path_for_reports(path)])

    rep = {
        'collisions_title_norm': len(norms),
        'dup_content_hashes': len(dups),
        'dup_content_hashes_exempt_only': dup_exempt_only,
        'dup_content_hashes_unexpected_clusters': dup_unexpected_clusters,
        'dup_content_hashes_allowed_hashes': dup_allowed,
        'dup_hash_allowlist_path': str(ALLOWLIST_PATH),
        'dup_hash_exemptions_path': str(EXEMPTIONS_PATH),
        'collision_title_norm_csv': col_csv.name,
        'dup_content_hashes_csv': dup_csv.name
    }
    (run_dir/'diagnostics_report.json').write_text(json.dumps(rep, indent=2), encoding='utf-8')
    conn.close(); return rep

# Manifest and hashes
def build_manifest_v2(run_dir: Path) -> tuple[str, Path]:
    out = run_dir / 'templates_manifest_v2.csv'
    rows = []
    for p in sorted(TEMPLATES_ROOT.rglob('*.md')):
        rel = p.relative_to(TEMPLATES_ROOT).as_posix()
        h = hash_v2_bytes(p.read_bytes())
        rows.append((rel, h))
    with out.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['path','hash_sha256_v2']); w.writerows(rows)
    return sha256_bytes(out.read_bytes()), out

def load_counts(cur):
    cur.execute('SELECT COUNT(*) FROM documents_current'); files_count = cur.fetchone()[0]
    cur.execute('SELECT COUNT(*) FROM anomalies_current'); anomalies_total = cur.fetchone()[0]
    cur.execute('SELECT COUNT(*) FROM (SELECT title_norm FROM documents_current GROUP BY title_norm HAVING COUNT(*)>1)'); collisions = cur.fetchone()[0]
    cur.execute('SELECT COUNT(*) FROM documents_current WHERE hash_sha256_v2 IS NULL'); null_v2 = cur.fetchone()[0]
    return files_count, anomalies_total, collisions, null_v2

# Coverage report
def build_coverage(cur) -> Coverage:
    files_count = cur.execute('SELECT COUNT(*) FROM documents_current').fetchone()[0]
    log_count = sum(1 for _ in ALIGNMENT_LOG.open()) - 1
    distinct_title_norm = cur.execute('SELECT COUNT(DISTINCT title_norm) FROM documents_current').fetchone()[0]
    aligned_not_ok = cur.execute('SELECT COUNT(*) FROM documents_current WHERE aligned<>1').fetchone()[0]
    empty_path = cur.execute("SELECT COUNT(*) FROM documents_current WHERE path IS NULL OR TRIM(path)='';").fetchone()[0]
    dup_path = 0
    csv_vs_fs_missing = 0
    csv_vs_fs_extra = 0
    snapshot_count = cur.execute('SELECT COUNT(*) FROM snapshots').fetchone()[0]
    return Coverage(files_count, log_count, files_count, distinct_title_norm, aligned_not_ok, empty_path, dup_path, csv_vs_fs_missing, csv_vs_fs_extra, snapshot_count)

# Validate thresholds
def validate(cur, base_anom: int, base_coll: int, base_duphash: int) -> ValidateReport:
    reasons = []
    status = 'PASS'
    cur.execute('SELECT COUNT(*) FROM (SELECT hash_sha256_v2, COUNT(*) c FROM documents_current WHERE hash_sha256_v2 IS NOT NULL GROUP BY hash_sha256_v2 HAVING c>1)')
    duphash = cur.fetchone()[0]
    cur.execute('SELECT COUNT(*) FROM anomalies_current')
    anom = cur.fetchone()[0]
    cur.execute('SELECT COUNT(*) FROM (SELECT title_norm FROM documents_current GROUP BY title_norm HAVING COUNT(*)>1)')
    coll = cur.fetchone()[0]
    # helpers
    def bump(level, msg):
        nonlocal status
        if level == 'FAIL':
            status = 'FAIL'
        elif level == 'WARN' and status == 'PASS':
            status = 'WARN'
        reasons.append(f"{level}: {msg}")
    # collisions
    if coll > base_coll + TH_COLLISIONS_FAIL:
        bump('FAIL', f'collisions_title_norm {coll}')
    elif coll > base_coll + TH_COLLISIONS_WARN:
        bump('WARN', f'collisions_title_norm {coll}')
    # anomalies total
    if anom > base_anom + TH_ANOM_FAIL:
        bump('FAIL', f'anomalies_total {anom}')
    elif anom > base_anom + TH_ANOM_WARN:
        bump('WARN', f'anomalies_total {anom}')
    # dup hash
    if duphash > base_duphash + TH_DUPHASH_FAIL:
        bump('FAIL', f'dup_content_hashes {duphash}')
    elif duphash > base_duphash + TH_DUPHASH_WARN:
        bump('WARN', f'dup_content_hashes {duphash}')

    metrics = {
        'collisions_title_norm': coll,
        'anomalies_total': anom,
        'dup_content_hashes': duphash,
    }
    return ValidateReport(status, reasons, metrics)

# Snapshot creation
def create_snapshot_if_changed(cur, manifest_hash_v2: str, log_hash: str, files_count: int, anomalies_total: int, collisions: int) -> SnapshotAction:
    cur.execute('''
        SELECT snapshot_id, templates_manifest_hash_v2
        FROM snapshots
        WHERE templates_manifest_hash_v2 IS NOT NULL
        ORDER BY snapshot_id DESC
        LIMIT 1
    ''')
    row = cur.fetchone()
    last_hash = row[1] if row else None
    if last_hash == manifest_hash_v2:
        return SnapshotAction('NOOP', None)
    cur.execute('''
        INSERT INTO snapshots(
          created_at_utc, git_commit, note,
          templates_manifest_hash_v2, alignment_log_hash_sha256,
          hashing_rule_version, hashing_rule,
          templates_count, anomalies_total, collisions_title_norm
        ) VALUES (?,?,?,?,?,?,?,?,?,?)
    ''', (utc_now_iso(), None, 'auto snapshot if changed', manifest_hash_v2, log_hash,
          HASHING_RULE_VERSION, HASHING_RULE, files_count, anomalies_total, collisions))
    snap_id = cur.lastrowid
    cur.execute('''
        INSERT INTO documents_snapshot (
          snapshot_id, path, title, title_norm, source, status, aligned, aligned_at_utc, aligned_by,
          hash_sha256, hash_sha256_v2, template_id
        )
        SELECT ?, path, title, title_norm, source, status, aligned, aligned_at_utc, aligned_by,
               hash_sha256, hash_sha256_v2, template_id
        FROM documents_current
    ''', (snap_id,))
    return SnapshotAction('CREATED', snap_id)

# Pruning
def prune_snapshots(cur) -> PruneReport:
    cur.execute('SELECT snapshot_id, created_at_utc FROM snapshots ORDER BY snapshot_id ASC')
    all_snaps = cur.fetchall()
    keep_ids = set()
    cur.execute('SELECT snapshot_id FROM snapshots ORDER BY snapshot_id DESC LIMIT ?', (RETENTION_WEEKLY,))
    keep_ids.update(r[0] for r in cur.fetchall())
    monthly = OrderedDict()
    for sid, ts in all_snaps:
        ym = ts[:7]
        if ym not in monthly:
            monthly[ym] = sid
    months = list(monthly.keys())
    for ym in months[-RETENTION_MONTHLY:]:
        keep_ids.add(monthly[ym])
    keep_ids.add(BASELINE_ID)
    cur.execute('SELECT snapshot_id FROM snapshots')
    all_ids = [r[0] for r in cur.fetchall()]
    to_delete = [sid for sid in all_ids if sid not in keep_ids]
    for sid in to_delete:
        cur.execute('DELETE FROM snapshots WHERE snapshot_id=?', (sid,))
    return PruneReport(sorted(list(keep_ids)), to_delete)

# Copy latest

def sync_latest(run_dir: Path):
    if LATEST_ROOT.exists():
        shutil.rmtree(LATEST_ROOT)
    shutil.copytree(run_dir, LATEST_ROOT)

# Main

def main():
    started_at_utc = utc_now_iso()
    run_id = utc_now_iso() + '__run'
    run_dir = RUNS_ROOT / run_id
    ensure_dirs(run_dir)

    # preflight: verify required artefacts and DB profile before doing any work
    preflight_errors = []
    if not TEMPLATES_ROOT.exists():
        preflight_errors.append(f"TEMPLATES_ROOT missing: {TEMPLATES_ROOT}")
    if not ALIGNMENT_LOG.exists():
        preflight_errors.append(f"ALIGNMENT_LOG missing: {ALIGNMENT_LOG}")
    if not DB_PATH.exists():
        preflight_errors.append(f"DB_PATH missing: {DB_PATH}")
    else:
        _conn = sqlite3.connect(str(DB_PATH))
        try:
            from itdoc.schema_profile import detect_schema_profile
            _check = detect_schema_profile(_conn)
            if _check.profile != "current-snapshot":
                preflight_errors.append(
                    f"DB profile mismatch: expected=current-snapshot, "
                    f"got={_check.profile}, missing={sorted(_check.missing_required)}"
                )
        finally:
            _conn.close()
    if preflight_errors:
        for err in preflight_errors:
            print(f"PREFLIGHT FAIL: {err}", file=sys.stderr)
        sys.exit(1)

    # hard gate: no emoji allowed in templates (not the whole repo)
    emoji_report = emoji_check(TEMPLATES_ROOT, run_dir)
    if emoji_report['status'] != 'PASS':
        print('FAIL: emoji check failed')
        sys.exit(1)

    # compute manifest v2
    manifest_hash_v2, manifest_path = build_manifest_v2(run_dir)
    log_hash = sha256_bytes(ALIGNMENT_LOG.read_bytes())

    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA journal_mode=DELETE;')
    conn.execute('PRAGMA foreign_keys=ON;')
    conn.execute('PRAGMA busy_timeout=5000;')
    cur = conn.cursor()

    ensure_schema(conn)

    # update hash_v2 in current using manifest_v2.csv (path relative to templates_root)
    rows_update = []
    with manifest_path.open('r', encoding='utf-8', newline='') as mf:
        import csv
        reader = csv.DictReader(mf)
        for row in reader:
            rel = row['path']
            h = row['hash_sha256_v2']
            rows_update.append((h, f'generated_templates/{rel}'))

    cur.executemany('UPDATE documents_current SET hash_sha256_v2=? WHERE path=?', rows_update)

    # coverage checks
    cov_db = build_coverage(cur)
    cov_fs_csv = coverage_report(run_dir)
    if cov_db.aligned_not_ok or cov_db.empty_path:
        print('FAIL: coverage preconditions not met'); sys.exit(1)
    if cov_fs_csv.get('status') != 'PASS':
        print('FAIL: csv coverage fail'); sys.exit(1)

    # counts and validate
    files_count, anomalies_total, collisions, null_v2 = load_counts(cur)
    if null_v2 != 0:
        print('FAIL: hash_v2 NULL in documents_current'); sys.exit(1)
    cur.execute('SELECT hash_sha256_v2, COUNT(*) c FROM documents_current WHERE hash_sha256_v2 IS NOT NULL GROUP BY hash_sha256_v2 HAVING c>1')
    duphash = len(cur.fetchall())
    conn.commit()  # zwolnij locka przed otwarciem nowego polaczenia w diagnostics_report
    diag = diagnostics_report(DB_PATH, run_dir)
    # tagging (Tor 2) - używamy istniejącego połączenia/locka
    tagging = apply_tag_rules(cur, TAG_RULES_PATH, run_dir)

    # simple validation: WARN tylko, jeśli są nieoczekiwane duplikaty, FAIL jeśli tagging=FAIL
    val_status = 'PASS'
    val_reasons = []
    unexpected_clusters = diag.get('dup_content_hashes_unexpected_clusters', 0)
    if unexpected_clusters > 0:
        val_status = 'WARN'
        val_reasons.append(f'unexpected_dup_content_hash_clusters={unexpected_clusters}')
    if tagging.get('status') == 'FAIL':
        val_status = 'FAIL'
        val_reasons.append('tagging_fail')
    validate_report = {
        'status': val_status,
        'reasons': val_reasons,
        'metrics': {
            'collisions_title_norm': diag['collisions_title_norm'],
            'dup_content_hashes': diag['dup_content_hashes'],
            'dup_content_hashes_exempt_only': diag.get('dup_content_hashes_exempt_only', 0),
            'dup_content_hashes_unexpected_clusters': unexpected_clusters,
            'tagging_rules_total': tagging.get('rules_total'),
            'tagging_dead_rules': tagging.get('dead_rules'),
            'tagging_conflicts_docs': tagging.get('conflicts_docs'),
            'anomalies_total': anomalies_total,
            'files_count': files_count
        }
    }

    # snapshot if changed
    action = create_snapshot_if_changed(cur, manifest_hash_v2, log_hash, files_count, anomalies_total, collisions)
    # transitions N-1 -> N (idempotent)
    transitions = {'status': 'SKIP', 'reason': 'snapshot_noop'}
    diff_report = {'status': 'SKIP', 'reason': 'snapshot_noop'}
    if action.action == 'CREATED':
        prev_id = previous_snapshot_id(cur, action.snapshot_id)
        if prev_id:
            transitions = compute_transitions(cur, prev_id, action.snapshot_id, run_dir)
            diff_report = compute_snapshot_diff(cur, prev_id, action.snapshot_id, run_dir)
        else:
            transitions = {'status': 'SKIP', 'reason': 'no_previous_snapshot', 'to_snapshot_id': action.snapshot_id}
            (run_dir/'transitions_report.json').write_text(json.dumps(transitions, indent=2), encoding='utf-8')
            diff_report = {'status': 'SKIP', 'reason': 'no_previous_snapshot', 'to_snapshot_id': action.snapshot_id}
            (run_dir/'snapshot_diff_report.json').write_text(json.dumps(diff_report, indent=2), encoding='utf-8')
    else:
        (run_dir/'transitions_report.json').write_text(json.dumps(transitions, indent=2), encoding='utf-8')
        (run_dir/'snapshot_diff_report.json').write_text(json.dumps(diff_report, indent=2), encoding='utf-8')

    # pruning
    prune = prune_snapshots(cur)

    conn.commit()
    conn.close()

    # write reports
    with (run_dir/'build_report.json').open('w') as f:
        json.dump({'run_id': run_id, 'coverage': asdict(cov_db), 'manifest_hash_v2': manifest_hash_v2,
                   'alignment_log_hash': log_hash, 'anomalies': anomalies_total,
                   'collisions_title_norm': collisions, 'dup_content_hashes': duphash,
                   'validate': validate_report['status']}, f, indent=2)
    with (run_dir/'validate_report.json').open('w') as f:
        json.dump(validate_report, f, indent=2)
    with (run_dir/'snapshot_action.json').open('w') as f:
        json.dump(asdict(action), f, indent=2)
    with (run_dir/'prune_report.json').open('w') as f:
        json.dump(asdict(prune), f, indent=2)

    manual_meta_sla = {}
    sla_path = LATEST_ROOT / 'manual_meta_sla.json'
    if sla_path.exists():
        try:
            manual_meta_sla = json.loads(sla_path.read_text(encoding='utf-8'))
        except Exception:
            manual_meta_sla = {"status": "unreadable"}

    # aggregate pipeline result
    pipeline_result = {
        'run_id': run_id,
        'status': validate_report['status'],
        'manifest_hash_v2': manifest_hash_v2,
        'alignment_log_hash': log_hash,
        'coverage_db': asdict(cov_db),
        'coverage_csv': cov_fs_csv,
        'diagnostics': diag,
        'emoji_check': emoji_report,
        'validate': validate_report,
        'dup_content_policy': {
            'policy_version': 1,
            'hashing_rule_version': HASHING_RULE_VERSION,
            'exemptions_path': str(EXEMPTIONS_PATH),
            'dup_hash_clusters_total': diag.get('dup_content_hashes', 0),
            'dup_hash_clusters_exempt_only': diag.get('dup_content_hashes_exempt_only', 0),
            'dup_hash_clusters_unexpected': diag.get('dup_content_hashes_unexpected_clusters', 0),
            # przykłady są generowane tylko gdy unexpected > 0; tu zostawiamy puste dla PASS
            'unexpected_examples': []
        },
        'tagging': tagging,
        'tagging_policy': {
            'rules_path': str(TAG_RULES_PATH),
            'conflict_policy': 'allow_multi'
        },
        'snapshot': asdict(action),
        'transitions': transitions,
        'snapshot_diff': diff_report,
        'prune': asdict(prune),
        'manual_meta_sla': manual_meta_sla,
        'run_dir': str(run_dir),
        'latest_dir': str(LATEST_ROOT),
    }
    pipeline_result_json = json.dumps(pipeline_result, ensure_ascii=False, indent=2)
    pipeline_result_sha = sha256_bytes(pipeline_result_json.encode('utf-8'))
    finished_at_utc = utc_now_iso()
    with (run_dir/'pipeline_result.json').open('w', encoding='utf-8') as f:
        f.write(pipeline_result_json)

    # runs log (DB)
    record_run_metrics(DB_PATH, run_id, started_at_utc, finished_at_utc, pipeline_result, pipeline_result_sha)

    sync_latest(run_dir)
    print({'status': validate_report['status'], 'run_id': run_id, 'snapshot': action.action, 'pruned': prune.deleted})

if __name__ == '__main__':
    main()
