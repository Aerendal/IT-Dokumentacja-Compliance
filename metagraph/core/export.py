"""metagraph/core/export.py — Eksport węzłów grafu do Markdown."""
from collections import defaultdict
import json


def export_requirements(conn, req_type: str = None, module: str = None) -> str:
    """Eksportuj wymagania do Markdown — opcjonalnie filtruj po typie lub module."""
    q = """
        SELECT n.id, n.title, n.body, n.source_file, n.priority,
               json_extract(n.metadata,'$.req_type') as rt,
               m.title as module_name
        FROM nodes n
        LEFT JOIN edges e ON e.to_node=n.id AND e.type_id='implements'
        LEFT JOIN nodes m ON e.from_node=m.id AND m.type_id='docs:module'
        WHERE n.type_id='docs:requirement' AND n.status='active'
    """
    params = []
    if req_type:
        q += " AND json_extract(n.metadata,'$.req_type')=?"
        params.append(req_type)
    if module:
        q += " AND m.title LIKE ?"
        params.append(f"%{module}%")
    q += " ORDER BY json_extract(n.metadata,'$.req_type'), n.source_file, n.priority DESC"

    rows = conn.execute(q, params).fetchall()

    lines = [f"# Rejestr Wymagań"]
    if req_type:
        lines[0] += f" — {req_type}"
    if module:
        lines[0] += f" / {module}"
    lines.append(f"\n> Łącznie: {len(rows)} wymagań\n")

    by_type = defaultdict(list)
    for r in rows:
        by_type[r['rt'] or '?'].append(r)

    type_labels = {
        'FR': '⚙️ Wymagania Funkcjonalne (FR)',
        'NFR': '🚀 Wymagania Niefunkcjonalne (NFR)',
        'CR': '🔒 Ograniczenia (CR)',
        'IR': '🔗 Wymagania Integracyjne (IR)',
        'DR': '📦 Zależności (DR)',
        'SR': '🏗️ Wymagania Systemowe (SR)',
        'TR': '🧪 Wymagania Testowe (TR)',
        '?': '❓ Niesklasyfikowane',
    }

    for rt in ['FR', 'NFR', 'CR', 'IR', 'DR', 'SR', 'TR', '?']:
        if rt not in by_type:
            continue
        items = by_type[rt]
        lines.append(f"\n## {type_labels.get(rt, rt)} ({len(items)})\n")
        lines.append("| # | Wymaganie | Moduł | Prioryt |")
        lines.append("|---|---|---|---|")
        for i, r in enumerate(items, 1):
            mod = r['module_name'] or '—'
            prio_map = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                        'low': 2, 'medium': 3, 'high': 4, 'critical': 5}
            prio_val = prio_map.get(str(r['priority'] or 3), 3)
            prio = '⭐' * prio_val
            title = r['title'].replace('|', '\\|')[:80]
            lines.append(f"| {i} | {title} | {mod} | {prio} |")

    return "\n".join(lines)


def export_module_spec(conn, module_name: str) -> str:
    """Eksportuj pełną specyfikację modułu jako Markdown."""
    mod = conn.execute(
        "SELECT * FROM nodes WHERE type_id='docs:module' AND title LIKE ?",
        (f"%{module_name}%",)
    ).fetchone()
    if not mod:
        return f"# Błąd: moduł '{module_name}' nie znaleziony"

    lines = [f"# Specyfikacja: {mod['title']}", ""]
    if mod['body']:
        lines.extend([mod['body'], ""])

    # Wymagania
    reqs = conn.execute("""
        SELECT n.title, json_extract(n.metadata,'$.req_type') as rt, n.priority
        FROM edges e JOIN nodes n ON e.to_node=n.id
        WHERE e.from_node=? AND e.type_id='implements' AND n.type_id='docs:requirement'
          AND n.status='active'
        ORDER BY rt, n.priority DESC
    """, (mod['id'],)).fetchall()
    if reqs:
        lines.append(f"## Wymagania ({len(reqs)})\n")
        by_type = defaultdict(list)
        for r in reqs: by_type[r['rt'] or '?'].append(r)
        for rt, items in sorted(by_type.items()):
            lines.append(f"### {rt}\n")
            for r in items:
                lines.append(f"- [{r['priority'] or 3}★] {r['title']}")
            lines.append("")

    # Endpointy
    eps = conn.execute("""
        SELECT n.title, n.body FROM edges e JOIN nodes n ON e.to_node=n.id
        WHERE e.from_node=? AND e.type_id='exposes'
        ORDER BY n.title
    """, (mod['id'],)).fetchall()
    if eps:
        lines.append(f"## API Endpoints ({len(eps)})\n")
        for ep in eps:
            lines.append(f"- `{ep['title']}`")
            if ep['body']:
                lines.append(f"  > {ep['body'][:100]}")
        lines.append("")

    # Zależności od innych modułów
    deps = conn.execute("""
        SELECT n.title FROM edges e JOIN nodes n ON e.to_node=n.id
        WHERE e.from_node=? AND e.type_id='depends_on' AND n.type_id='docs:module'
    """, (mod['id'],)).fetchall()
    if deps:
        lines.append(f"## Zależności\n")
        for d in deps:
            lines.append(f"- → {d['title']}")
        lines.append("")

    # Stories
    stories = conn.execute("""
        SELECT n.title, ss.story_points FROM edges e
        JOIN nodes n ON e.from_node=n.id
        JOIN scrum_stories ss ON n.id=ss.node_id
        WHERE e.to_node=? AND e.type_id='implements'
        ORDER BY ss.story_points DESC
    """, (mod['id'],)).fetchall()
    if stories:
        total_sp = sum(s['story_points'] or 0 for s in stories)
        lines.append(f"## Backlog ({len(stories)} stories, {total_sp} SP)\n")
        for s in stories:
            lines.append(f"- [{s['story_points']} SP] {s['title']}")
        lines.append("")

    return "\n".join(lines)


def export_sprint_plan(conn) -> str:
    """Eksportuj plan sprintów jako Markdown."""
    lines = ["# Plan Sprintów — AI Documentation Workshop\n"]

    for sprint in conn.execute("""
        SELECT n.id, n.title, s.sprint_number, s.start_date, s.end_date, s.velocity, s.goal
        FROM nodes n JOIN scrum_sprints s ON n.id=s.node_id
        ORDER BY s.sprint_number
    """).fetchall():
        stories = conn.execute("""
            SELECT n2.title, ss.story_points, m.title as module,
                   ss.acceptance_criteria
            FROM scrum_stories ss
            JOIN nodes n2 ON ss.node_id=n2.id
            LEFT JOIN edges e ON e.from_node=n2.id AND e.type_id='implements'
            LEFT JOIN nodes m ON e.to_node=m.id AND m.type_id='docs:module'
            WHERE ss.sprint_id=?
            ORDER BY ss.story_points DESC
        """, (sprint['id'],)).fetchall()
        total_sp = sum(s['story_points'] or 0 for s in stories)

        lines.append(f"## Sprint {sprint['sprint_number']}: {sprint['title']}")
        lines.append(f"📅 `{sprint['start_date']}` → `{sprint['end_date']}` | "
                     f"**{total_sp} SP** | Velocity: {sprint['velocity'] or '—'}\n")
        if sprint['goal']:
            lines.append(f"> {sprint['goal']}\n")
        lines.append("| Story | Moduł | SP | Kryteria akceptacji |")
        lines.append("|---|---|---|---|")
        for s in stories:
            ac = (s['acceptance_criteria'] or '—')[:60].replace('|', '\\|')
            lines.append(f"| {s['title'][:55]} | {s['module'] or '—'} | {s['story_points']} | {ac} |")
        lines.append("")

    return "\n".join(lines)
