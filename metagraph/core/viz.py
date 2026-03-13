"""metagraph/core/viz.py — Generowanie diagramów Mermaid."""


def generate_module_diagram(conn) -> str:
    """Diagram modułów z zależnościami, endpointami i tabelami."""
    lines = ["graph TD"]

    modules = {r['id']: r['title'] for r in conn.execute(
        "SELECT id, title FROM nodes WHERE type_id='docs:module'"
    ).fetchall()}

    # Węzły modułów
    lines.append("  subgraph modules[Moduły]")
    for mid, mtitle in modules.items():
        safe_id = mid.replace("-", "_")
        sp = conn.execute("""
            SELECT coalesce(sum(ss.story_points),0) FROM scrum_stories ss
            JOIN edges e ON ss.node_id=e.from_node
            WHERE e.to_node=? AND e.type_id='implements'
        """, (mid,)).fetchone()[0]
        ep_count = conn.execute(
            "SELECT count(*) FROM edges WHERE from_node=? AND type_id='exposes'", (mid,)
        ).fetchone()[0]
        lines.append(f'    {safe_id}["{mtitle}<br/>{sp}SP · {ep_count} API"]')
    lines.append("  end")
    lines.append("")

    # Zależności między modułami
    for edge in conn.execute("""
        SELECT e.from_node, e.to_node FROM edges e
        WHERE e.type_id='depends_on'
          AND e.from_node IN (SELECT id FROM nodes WHERE type_id='docs:module')
          AND e.to_node   IN (SELECT id FROM nodes WHERE type_id='docs:module')
    """).fetchall():
        f = edge['from_node'].replace("-", "_")
        t = edge['to_node'].replace("-", "_")
        lines.append(f"  {f} -->|depends on| {t}")

    # Spec docs
    lines.append("")
    lines.append("  subgraph specs[Spec Docs]")
    for r in conn.execute("""
        SELECT n.id, n.title, d.doc_number FROM nodes n
        JOIN doc_specs d ON n.id=d.node_id
        WHERE n.type_id='docs:spec' ORDER BY d.doc_number
    """).fetchall():
        safe_id = r['id'].replace("-", "_")
        lines.append(f'    {safe_id}["spec{r["doc_number"]:02d}: {r["title"][:30]}"]')
    lines.append("  end")

    # implements: module → spec (via wymagania)
    seen = set()
    for edge in conn.execute("""
        SELECT DISTINCT e1.from_node as mod_id, n2.source_file
        FROM edges e1
        JOIN nodes n1 ON e1.from_node=n1.id
        JOIN nodes n2 ON e1.to_node=n2.id
        WHERE e1.type_id='implements' AND n1.type_id='docs:module'
          AND n2.type_id='docs:requirement' AND n2.source_file IS NOT NULL
    """).fetchall():
        spec = conn.execute(
            "SELECT id FROM nodes WHERE source_file=? AND type_id='docs:spec' LIMIT 1",
            (edge['source_file'],)
        ).fetchone()
        if spec:
            key = (edge['mod_id'], spec['id'])
            if key not in seen:
                seen.add(key)
                f = edge['mod_id'].replace("-", "_")
                t = spec['id'].replace("-", "_")
                lines.append(f"  {f} -.->|implements| {t}")

    return "\n".join(lines)


def generate_sprint_diagram(conn) -> str:
    """Timeline diagram sprintów."""
    lines = ["gantt", "  title Plan Sprintów — AI Documentation Workshop", "  dateFormat YYYY-MM-DD"]

    for sprint in conn.execute("""
        SELECT n.title, s.start_date, s.end_date, s.sprint_number
        FROM nodes n JOIN scrum_sprints s ON n.id=s.node_id
        ORDER BY s.sprint_number
    """).fetchall():
        lines.append(f"  section Sprint {sprint['sprint_number']}")
        stories = conn.execute("""
            SELECT n2.title, ss.story_points FROM scrum_stories ss
            JOIN nodes n2 ON ss.node_id=n2.id WHERE ss.sprint_id=(
                SELECT n.id FROM nodes n JOIN scrum_sprints sp ON n.id=sp.node_id
                WHERE sp.sprint_number=?)
            ORDER BY ss.story_points DESC
        """, (sprint['sprint_number'],)).fetchall()
        for i, st in enumerate(stories):
            title_safe = st['title'][:40].replace(":", "").replace(",", "")
            if i == 0:
                lines.append(f"  {title_safe} [{st['story_points']}SP] :active, {sprint['start_date']}, {sprint['end_date']}")
            else:
                lines.append(f"  {title_safe} [{st['story_points']}SP] : {sprint['start_date']}, {sprint['end_date']}")

    return "\n".join(lines)
