import json
import hashlib
import sqlite3
from typing import Optional


def _make_id(layer: str, type_short: str, title: str) -> str:
    """Generuje deterministyczny ID węzła."""
    slug = title.lower()[:30].replace(" ", "-").replace("/", "-")
    slug = "".join(c for c in slug if c.isalnum() or c == "-")
    h = hashlib.md5(title.encode()).hexdigest()[:6]
    return f"{layer}-{type_short}-{slug}-{h}"


def create_node(
    conn,
    type_id: str,
    title: str,
    body: str = "",
    status: str = "active",
    priority: int = 3,
    metadata: dict = None,
    source_file: str = None,
    source_section: str = None,
) -> str:
    layer = type_id.split(":")[0]
    type_short = type_id.split(":")[1][:4]
    node_id = _make_id(layer, type_short, title)

    conn.execute(
        """
        INSERT OR IGNORE INTO nodes
            (id, type_id, title, body, status, priority,
             metadata, layer, source_file, source_section)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            node_id, type_id, title, body, status, priority,
            json.dumps(metadata or {}), layer, source_file, source_section,
        ),
    )
    conn.execute(
        "INSERT INTO events (node_id, event_type, payload) VALUES (?, 'create', ?)",
        (node_id, json.dumps({"title": title, "type": type_id})),
    )
    conn.commit()
    return node_id


def create_edge(
    conn,
    from_node: str,
    to_node: str,
    type_id: str,
    weight: float = 1.0,
    label: str = None,
) -> str:
    edge_id = (
        "edge-"
        + hashlib.md5(f"{from_node}-{to_node}-{type_id}".encode()).hexdigest()[:8]
    )
    conn.execute(
        """
        INSERT OR IGNORE INTO edges (id, from_node, to_node, type_id, weight, label)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (edge_id, from_node, to_node, type_id, weight, label),
    )
    conn.execute(
        "INSERT INTO events (node_id, event_type, payload) VALUES (?, 'link', ?)",
        (from_node, json.dumps({"to": to_node, "type": type_id})),
    )
    conn.commit()
    return edge_id


def get_node(conn, node_id: str) -> Optional[sqlite3.Row]:
    return conn.execute("SELECT * FROM nodes WHERE id = ?", (node_id,)).fetchone()


def list_nodes(
    conn,
    layer: str = None,
    type_id: str = None,
    status: str = None,
    limit: int = 50,
) -> list:
    q = "SELECT * FROM nodes WHERE 1=1"
    params = []
    if layer:
        q += " AND layer = ?"
        params.append(layer)
    if type_id:
        q += " AND type_id = ?"
        params.append(type_id)
    if status:
        q += " AND status = ?"
        params.append(status)
    q += " ORDER BY created_at DESC LIMIT ?"
    params.append(limit)
    return conn.execute(q, params).fetchall()


def get_neighbors(conn, node_id: str, depth: int = 1, direction: str = "both") -> list:
    """BFS po grafie do podanej głębokości."""
    visited = {node_id}
    queue = [(node_id, 0)]
    result = []

    while queue:
        current, d = queue.pop(0)
        if d >= depth:
            continue
        if direction in ("out", "both"):
            rows = conn.execute(
                "SELECT n.*, e.type_id as edge_type FROM nodes n "
                "JOIN edges e ON e.to_node = n.id WHERE e.from_node = ?",
                (current,),
            ).fetchall()
            for r in rows:
                if r["id"] not in visited:
                    visited.add(r["id"])
                    result.append(r)
                    queue.append((r["id"], d + 1))
        if direction in ("in", "both"):
            rows = conn.execute(
                "SELECT n.*, e.type_id as edge_type FROM nodes n "
                "JOIN edges e ON e.from_node = n.id WHERE e.to_node = ?",
                (current,),
            ).fetchall()
            for r in rows:
                if r["id"] not in visited:
                    visited.add(r["id"])
                    result.append(r)
                    queue.append((r["id"], d + 1))
    return result


def search_nodes(conn, query: str, limit: int = 20) -> list:
    """Pełnotekstowe wyszukiwanie (FTS5)."""
    try:
        return conn.execute(
            "SELECT n.* FROM nodes_fts f JOIN nodes n ON f.id = n.id "
            "WHERE nodes_fts MATCH ? LIMIT ?",
            (query, limit),
        ).fetchall()
    except Exception:
        return conn.execute(
            "SELECT * FROM nodes WHERE title LIKE ? OR body LIKE ? LIMIT ?",
            (f"%{query}%", f"%{query}%", limit),
        ).fetchall()


def graph_stats(conn) -> dict:
    nodes = conn.execute(
        "SELECT COUNT(*) FROM nodes WHERE status != 'archived'"
    ).fetchone()[0]
    edges = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    by_layer = conn.execute(
        "SELECT layer, COUNT(*) FROM nodes WHERE status != 'archived' GROUP BY layer"
    ).fetchall()
    return {"nodes": nodes, "edges": edges, "by_layer": {r[0]: r[1] for r in by_layer}}
