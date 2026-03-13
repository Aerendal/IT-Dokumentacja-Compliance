"""metagraph/core/check.py — Integrity checks dla metagraph.db."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str = ""
    items: List[str] = field(default_factory=list)


def run_all_checks(conn) -> List[CheckResult]:
    results = []

    # 1. Węzły izolowane
    orphans = conn.execute("""
        SELECT id, title, type_id FROM nodes
        WHERE status NOT IN ('archived','deleted')
          AND id NOT IN (SELECT from_node FROM edges)
          AND id NOT IN (SELECT to_node FROM edges)
    """).fetchall()
    results.append(CheckResult(
        name="Węzły bez krawędzi (orphans)",
        ok=len(orphans) == 0,
        detail=f"{len(orphans)} węzłów",
        items=[f"{r['id']} [{r['type_id']}] {r['title'][:50]}" for r in orphans[:10]],
    ))

    # 2. Dangling edges (krawędź → nieistniejący węzeł)
    dangling = conn.execute("""
        SELECT e.id, e.from_node, e.to_node FROM edges e
        WHERE e.from_node NOT IN (SELECT id FROM nodes)
           OR e.to_node   NOT IN (SELECT id FROM nodes)
    """).fetchall()
    results.append(CheckResult(
        name="Krawędzie do nieistniejących węzłów (dangling)",
        ok=len(dangling) == 0,
        detail=f"{len(dangling)} krawędzi",
        items=[f"{r['id']}: {r['from_node']} → {r['to_node']}" for r in dangling[:10]],
    ))

    # 3. Stories bez przypisanego modułu
    orphan_stories = conn.execute("""
        SELECT n.id, n.title FROM nodes n JOIN scrum_stories ss ON n.id=ss.node_id
        WHERE n.id NOT IN (
            SELECT from_node FROM edges WHERE type_id='implements'
            AND to_node IN (SELECT id FROM nodes WHERE type_id='docs:module'))
    """).fetchall()
    results.append(CheckResult(
        name="User stories bez modułu",
        ok=len(orphan_stories) == 0,
        detail=f"{len(orphan_stories)} stories",
        items=[f"{r['title'][:60]}" for r in orphan_stories],
    ))

    # 4. Endpoints bez exposes edge
    orphan_eps = conn.execute("""
        SELECT n.id, n.title FROM nodes n
        WHERE n.type_id='docs:endpoint'
          AND n.id NOT IN (SELECT to_node FROM edges WHERE type_id='exposes')
    """).fetchall()
    results.append(CheckResult(
        name="Endpoints bez exposes edge",
        ok=len(orphan_eps) == 0,
        detail=f"{len(orphan_eps)} endpoints",
        items=[f"{r['title'][:60]}" for r in orphan_eps[:10]],
    ))

    # 5. FTS działa
    fts_count = 0
    try:
        fts_count = conn.execute(
            "SELECT count(*) FROM nodes_fts WHERE nodes_fts MATCH 'llm'"
        ).fetchone()[0]
    except Exception:
        pass
    results.append(CheckResult(
        name="FTS5 wyszukiwanie działa",
        ok=fts_count > 0,
        detail=f"{fts_count} wyników dla 'llm' (oczekiwane >0)",
    ))

    # 6. pm:goal połączony z epics
    goal_rows = conn.execute("SELECT id FROM nodes WHERE type_id='pm:goal'").fetchall()
    disconnected_goals = []
    for g in goal_rows:
        cnt = conn.execute(
            "SELECT count(*) FROM edges WHERE to_node=? AND type_id='part_of'", (g['id'],)
        ).fetchone()[0]
        if cnt == 0:
            disconnected_goals.append(g['id'])
    results.append(CheckResult(
        name="pm:goal połączony z pm:epic",
        ok=len(disconnected_goals) == 0,
        detail=f"{len(disconnected_goals)} celów bez epics",
        items=disconnected_goals,
    ))

    # 7. Duplikaty edges (ten sam from/to/type)
    dups = conn.execute("""
        SELECT from_node, to_node, type_id, count(*) as cnt
        FROM edges GROUP BY from_node, to_node, type_id HAVING cnt > 1
    """).fetchall()
    results.append(CheckResult(
        name="Zduplikowane krawędzie",
        ok=len(dups) == 0,
        detail=f"{len(dups)} grup duplikatów",
        items=[f"{r['from_node']} -[{r['type_id']}]→ {r['to_node']} ×{r['cnt']}" for r in dups[:10]],
    ))

    # 8. Schema: kolumna tags istnieje
    cols = [r[1] for r in conn.execute("PRAGMA table_info(nodes)").fetchall()]
    results.append(CheckResult(
        name="Schema: kolumna nodes.tags istnieje",
        ok="tags" in cols,
        detail="Sprawdza czy ALTER TABLE tags był wykonany",
    ))

    # 9. Wymagania z brakującym req_type
    missing_req_type = conn.execute("""
        SELECT count(*) FROM nodes
        WHERE type_id='docs:requirement'
          AND status NOT IN ('archived', 'deleted')
          AND (metadata='{}' OR json_extract(metadata,'$.req_type') IS NULL)
    """).fetchone()[0]
    results.append(CheckResult(
        name="Wymagania z req_type w metadata",
        ok=missing_req_type == 0,
        detail=f"{missing_req_type} wymagań bez req_type",
    ))

    return results
