"""metagraph/core/report.py — Generowanie raportów projektu."""
import json
from datetime import datetime


def _risk_icon(p, i):
    score = p * i
    if score >= 9: return "🔴"
    if score >= 4: return "🟡"
    return "🟢"


def generate_project_report(conn) -> dict:
    """Zbiera dane z grafu i zwraca strukturę raportu."""
    r = {}

    # Meta
    r["generated_at"] = datetime.utcnow().isoformat() + "Z"

    # Goals
    r["goals"] = [dict(row) for row in conn.execute("""
        SELECT n.title, n.body, g.target_date, g.okr
        FROM nodes n JOIN pm_goals g ON n.id=g.node_id
    """).fetchall()]

    # Epics
    r["epics"] = [dict(row) for row in conn.execute("""
        SELECT n.title, e.start_date, e.end_date
        FROM nodes n JOIN pm_epics e ON n.id=e.node_id
        ORDER BY e.start_date
    """).fetchall()]

    # Sprints
    r["sprints"] = []
    for sprint in conn.execute("""
        SELECT n.id, n.title, s.sprint_number, s.start_date, s.end_date, s.velocity
        FROM nodes n JOIN scrum_sprints s ON n.id=s.node_id
        ORDER BY s.sprint_number
    """).fetchall():
        stories = conn.execute("""
            SELECT n2.title, ss.story_points, n3.title as module
            FROM scrum_stories ss
            JOIN nodes n2 ON ss.node_id=n2.id
            LEFT JOIN edges e ON e.from_node=n2.id AND e.type_id='implements'
            LEFT JOIN nodes n3 ON e.to_node=n3.id AND n3.type_id='docs:module'
            WHERE ss.sprint_id=?
            ORDER BY ss.story_points DESC
        """, (sprint['id'],)).fetchall()
        r["sprints"].append({
            "number": sprint["sprint_number"],
            "title": sprint["title"],
            "start": sprint["start_date"],
            "end": sprint["end_date"],
            "velocity": sprint["velocity"],
            "stories": [dict(s) for s in stories],
            "total_sp": sum(s["story_points"] or 0 for s in stories),
        })

    # Totals
    r["total_sp"] = sum(s["total_sp"] for s in r["sprints"])
    r["total_stories"] = sum(len(s["stories"]) for s in r["sprints"])

    # Requirements summary
    req_counts = {row[0]: row[1] for row in conn.execute("""
        SELECT json_extract(metadata, '$.req_type') as rt, count(*)
        FROM nodes WHERE type_id='docs:requirement' AND status!='archived'
        GROUP BY rt
    """).fetchall()}
    r["requirements"] = {
        "total": sum(req_counts.values()),
        "by_type": req_counts,
    }

    # Risks
    r["risks"] = [dict(row) for row in conn.execute("""
        SELECT n.title, r.probability, r.impact, r.mitigation
        FROM nodes n JOIN pm_risks r ON n.id=r.node_id
        ORDER BY (r.probability * r.impact) DESC
    """).fetchall()]

    # Module breakdown
    r["modules"] = []
    for mod in conn.execute("""
        SELECT n.id, n.title FROM nodes n WHERE n.type_id='docs:module' ORDER BY n.title
    """).fetchall():
        reqs = conn.execute("""
            SELECT count(*) FROM edges e
            JOIN nodes n ON e.to_node=n.id
            WHERE e.from_node=? AND e.type_id='implements' AND n.type_id='docs:requirement'
        """, (mod['id'],)).fetchone()[0]
        eps = conn.execute("""
            SELECT count(*) FROM edges WHERE from_node=? AND type_id='exposes'
        """, (mod['id'],)).fetchone()[0]
        sps = conn.execute("""
            SELECT sum(ss.story_points) FROM scrum_stories ss
            JOIN edges e ON ss.node_id=e.from_node
            WHERE e.to_node=? AND e.type_id='implements'
        """, (mod['id'],)).fetchone()[0] or 0
        r["modules"].append({
            "name": mod["title"],
            "requirements": reqs,
            "endpoints": eps,
            "story_points": sps,
        })

    return r


def render_markdown(report: dict) -> str:
    lines = []
    a = lines.append

    a(f"# Raport Projektu — AI Documentation Workshop")
    a(f"\n> Wygenerowano: {report['generated_at']}\n")

    # Cele
    if report["goals"]:
        a("## 🎯 Cel Projektu\n")
        for g in report["goals"]:
            a(f"**{g['title']}**")
            if g.get("okr"): a(f"\n_{g['okr']}_")
            if g.get("target_date"): a(f"\nTermin: `{g['target_date']}`")
            a("")

    # Podsumowanie
    a("## 📊 Podsumowanie\n")
    a(f"| Metryka | Wartość |")
    a(f"|---|---|")
    a(f"| Total Story Points | **{report['total_sp']} SP** |")
    a(f"| User Stories | {report['total_stories']} |")
    a(f"| Sprints | {len(report['sprints'])} × 2–4 tyg. |")
    a(f"| Zakres | {report['sprints'][0]['start']} → {report['sprints'][-1]['end']} |")
    a(f"| Wymagania łącznie | {report['requirements']['total']} |")
    for rt, cnt in sorted(report['requirements']['by_type'].items(), key=lambda x: -x[1]):
        if rt:
            a(f"| &nbsp;&nbsp;— {rt} | {cnt} |")
    a("")

    # Moduły
    a("## 🧩 Podział per moduł\n")
    a("| Moduł | Wymagania | Endpointy | Story Points |")
    a("|---|---|---|---|")
    for m in sorted(report["modules"], key=lambda x: -x["story_points"]):
        a(f"| {m['name']} | {m['requirements']} | {m['endpoints']} | **{m['story_points']} SP** |")
    a("")

    # Sprints
    a("## 🏃 Plan Sprintów\n")
    for s in report["sprints"]:
        a(f"### Sprint {s['number']} — {s['title']}")
        a(f"📅 `{s['start']}` → `{s['end']}` | **{s['total_sp']} SP**\n")
        a("| Story | Moduł | SP |")
        a("|---|---|---|")
        for st in s["stories"]:
            a(f"| {st['title'][:55]} | {st.get('module','—') or '—'} | {st['story_points']} |")
        a("")

    # Ryzyka
    if report["risks"]:
        a("## ⚠️ Rejestr Ryzyk\n")
        a("| Ryzyko | P | I | Ocena | Mitygacja |")
        a("|---|---|---|---|---|")
        for rk in report["risks"]:
            p, i = rk['probability'], rk['impact']
            icon = _risk_icon(p, i)
            a(f"| {rk['title'][:50]} | {p} | {i} | {icon} {p*i} | {(rk.get('mitigation') or '—')[:40]} |")
        a("")

    return "\n".join(lines)
