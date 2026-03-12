import json


def log_event(conn, event_type: str, node_id: str = None, payload: dict = None):
    conn.execute(
        "INSERT INTO events (node_id, event_type, payload) VALUES (?, ?, ?)",
        (node_id, event_type, json.dumps(payload or {})),
    )
    conn.commit()


def get_node_history(conn, node_id: str) -> list:
    return conn.execute(
        "SELECT * FROM events WHERE node_id = ? ORDER BY created_at", (node_id,)
    ).fetchall()


def get_recent_events(conn, limit: int = 50) -> list:
    return conn.execute(
        "SELECT * FROM events ORDER BY created_at DESC LIMIT ?", (limit,)
    ).fetchall()
