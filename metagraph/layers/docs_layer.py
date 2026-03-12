"""Docs layer: spec documents, modules, endpoints, tables, findings."""
from metagraph.core.graph import create_node, create_edge


def create_spec_doc(conn, title: str, doc_number: int, file_path: str = None,
                    version: str = "1.0", body: str = "") -> str:
    node_id = create_node(conn, "docs:spec", title, body=body, source_file=file_path)
    conn.execute(
        "INSERT OR IGNORE INTO doc_specs (node_id, doc_number, file_path, version) VALUES (?, ?, ?, ?)",
        (node_id, doc_number, file_path, version),
    )
    conn.commit()
    return node_id


def create_module(conn, title: str, module_type: str = "service",
                  spec_doc_id: str = None, body: str = "") -> str:
    node_id = create_node(conn, "docs:module", title, body=body)
    conn.execute(
        "INSERT OR IGNORE INTO doc_modules (node_id, module_type, spec_doc_id) VALUES (?, ?, ?)",
        (node_id, module_type, spec_doc_id),
    )
    if spec_doc_id:
        create_edge(conn, node_id, spec_doc_id, "part_of")
    conn.commit()
    return node_id


def create_finding(conn, title: str, finding_id: str, round_num: int,
                   severity: str = "minor", body: str = "") -> str:
    node_id = create_node(conn, "docs:finding", title, body=body)
    conn.execute(
        "INSERT OR IGNORE INTO doc_findings (node_id, round, finding_id, severity) VALUES (?, ?, ?, ?)",
        (node_id, round_num, finding_id, severity),
    )
    conn.commit()
    return node_id


def get_findings_summary(conn) -> list:
    return conn.execute(
        "SELECT f.round, f.severity, COUNT(*) as count, "
        "SUM(f.resolved) as resolved "
        "FROM doc_findings f GROUP BY f.round, f.severity ORDER BY f.round, f.severity"
    ).fetchall()


def ingest_spec_doc_sections(conn, spec_node_id: str, sections: list[dict]) -> list[str]:
    """Tworzy węzły sekcji dla dokumentu spec. sections = [{'title':..., 'body':...}]"""
    ids = []
    for sec in sections:
        sec_id = create_node(
            conn, "docs:section",
            sec["title"],
            body=sec.get("body", ""),
            source_section=sec.get("section_id"),
        )
        create_edge(conn, sec_id, spec_node_id, "part_of")
        ids.append(sec_id)
    return ids
