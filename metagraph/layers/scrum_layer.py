"""Scrum layer: sprints, stories, tasks."""
from metagraph.core.graph import create_node, create_edge


def create_sprint(conn, title: str, sprint_number: int, start_date: str = None,
                  end_date: str = None, goal: str = None) -> str:
    node_id = create_node(conn, "scrum:sprint", title, body=goal or "")
    conn.execute(
        "INSERT OR IGNORE INTO scrum_sprints (node_id, sprint_number, start_date, end_date, goal) "
        "VALUES (?, ?, ?, ?, ?)",
        (node_id, sprint_number, start_date, end_date, goal),
    )
    conn.commit()
    return node_id


def create_story(conn, title: str, body: str = "", epic_id: str = None,
                 sprint_id: str = None, story_points: int = 0,
                 acceptance_criteria: str = None) -> str:
    node_id = create_node(conn, "scrum:story", title, body=body)
    conn.execute(
        "INSERT OR IGNORE INTO scrum_stories "
        "(node_id, epic_id, sprint_id, story_points, acceptance_criteria) VALUES (?, ?, ?, ?, ?)",
        (node_id, epic_id, sprint_id, story_points, acceptance_criteria),
    )
    if epic_id:
        create_edge(conn, node_id, epic_id, "part_of")
    if sprint_id:
        create_edge(conn, node_id, sprint_id, "part_of")
    conn.commit()
    return node_id


def create_task(conn, title: str, story_id: str = None, assignee: str = None,
                estimate_h: float = 0, task_type: str = "feature") -> str:
    node_id = create_node(conn, "scrum:task", title)
    conn.execute(
        "INSERT OR IGNORE INTO scrum_tasks (node_id, story_id, assignee, estimate_h, task_type) "
        "VALUES (?, ?, ?, ?, ?)",
        (node_id, story_id, assignee, estimate_h, task_type),
    )
    if story_id:
        create_edge(conn, node_id, story_id, "part_of")
    conn.commit()
    return node_id


def get_sprint_velocity(conn, sprint_id: str) -> dict:
    stories = conn.execute(
        "SELECT SUM(story_points) as total, "
        "SUM(CASE WHEN n.status='done' THEN story_points ELSE 0 END) as done "
        "FROM scrum_stories s JOIN nodes n ON s.node_id = n.id WHERE s.sprint_id = ?",
        (sprint_id,),
    ).fetchone()
    return {"total": stories["total"] or 0, "done": stories["done"] or 0}
