"""PM layer: goals, epics, risks."""
import json
from metagraph.core.graph import create_node, create_edge


def create_goal(conn, title: str, body: str = "", target_date: str = None,
                okr: str = None, priority: int = 3) -> str:
    node_id = create_node(conn, "pm:goal", title, body=body, priority=priority)
    conn.execute(
        "INSERT OR IGNORE INTO pm_goals (node_id, target_date, okr) VALUES (?, ?, ?)",
        (node_id, target_date, okr),
    )
    conn.commit()
    return node_id


def create_epic(conn, title: str, goal_id: str = None, body: str = "",
                start_date: str = None, end_date: str = None) -> str:
    node_id = create_node(conn, "pm:epic", title, body=body)
    conn.execute(
        "INSERT OR IGNORE INTO pm_epics (node_id, goal_id, start_date, end_date) VALUES (?, ?, ?, ?)",
        (node_id, goal_id, start_date, end_date),
    )
    if goal_id:
        create_edge(conn, node_id, goal_id, "part_of")
    conn.commit()
    return node_id


def create_risk(conn, title: str, body: str = "", probability: int = 3,
                impact: int = 3, mitigation: str = None) -> str:
    node_id = create_node(conn, "pm:risk", title, body=body)
    conn.execute(
        "INSERT OR IGNORE INTO pm_risks (node_id, probability, impact, mitigation) VALUES (?, ?, ?, ?)",
        (node_id, probability, impact, mitigation),
    )
    conn.commit()
    return node_id


def get_risk_matrix(conn) -> list:
    return conn.execute(
        "SELECT n.title, r.probability, r.impact, r.score, r.status "
        "FROM pm_risks r JOIN nodes n ON r.node_id = n.id "
        "ORDER BY r.score DESC"
    ).fetchall()
