"""Unit tests for the FastAPI compliance REST API."""
import os
import sqlite3
import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.unit


@pytest.fixture
def client(tmp_path):
    """Create test client with in-memory SQLite DB (legacy-runtime schema + API tables)."""
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    conn.executescript("""
        -- legacy-runtime required tables
        CREATE TABLE _schema_version (version TEXT, applied_at TEXT);
        INSERT INTO _schema_version VALUES ('1.0.0', '2026-01-01');
        CREATE TABLE docs (doc_uid TEXT PRIMARY KEY, title TEXT, title_norm TEXT, path TEXT, origin TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        CREATE TABLE sections (section_uid TEXT PRIMARY KEY, doc_uid TEXT, heading_text TEXT, heading_norm TEXT, heading_level INTEGER, heading_path TEXT, anchor TEXT, ordinal INTEGER, status TEXT, text_fingerprint_sha256 TEXT, start_line INTEGER, end_line INTEGER);
        CREATE TABLE standards (standard_id INTEGER PRIMARY KEY, standard_code TEXT, standard_name TEXT, standard_name_en TEXT, description TEXT, version TEXT, url TEXT, applicable_industries TEXT);
        CREATE TABLE compliance_regulations (id INTEGER PRIMARY KEY, regulation_code TEXT, regulation_name TEXT, jurisdiction TEXT, industry TEXT, key_requirements TEXT, penalty_info TEXT, data_engineering_impact TEXT);
        CREATE TABLE content_links (id INTEGER PRIMARY KEY, from_doc TEXT, to_doc TEXT, link_type TEXT);
        INSERT INTO content_links VALUES (1, 'core/a.md', 'core/b.md', 'requires');
        CREATE TABLE content_links_resolved (id INTEGER PRIMARY KEY, content_link_id INTEGER, from_kind TEXT, from_uid TEXT, to_kind TEXT, to_uid TEXT, link_type TEXT, direction TEXT, rationale TEXT, strength TEXT, resolution_method TEXT, resolution_confidence REAL, notes TEXT);
        INSERT INTO content_links_resolved VALUES (1, 1, 'doc', 'UID001', 'doc', 'UID002', 'requires', 'forward', '', 'required', 'explicit', 1.0, '');
        CREATE TABLE rhythm_edges (edge_id INTEGER PRIMARY KEY, from_node TEXT, to_node TEXT, rhythm_type TEXT, weight REAL, conditions TEXT, version_range TEXT, notes TEXT);
        INSERT INTO rhythm_edges VALUES (1, 'UID001', 'UID002', 'triggers', 0.9, '', '', '');
        CREATE TABLE contracts (contract_id INTEGER PRIMARY KEY, scope_kind TEXT, scope_uid TEXT, version TEXT, inputs_json TEXT, outputs_json TEXT, gates_json TEXT, impact_json TEXT, owner TEXT, notes TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        INSERT INTO contracts VALUES (1, 'doc', 'UID001', '1.0', '[]', '[]', '[]', '{}', 'owner', '', '2026-01-01', '2026-01-01');
        CREATE TABLE flags (id INTEGER PRIMARY KEY, doc_uid TEXT, version TEXT, branch_id INTEGER, access_mask INTEGER);
        INSERT INTO flags VALUES (1, 'UID001', '1.0.0', 1, 0);

        -- API-specific tables
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY, doc_path TEXT, standard_code TEXT,
            confidence REAL, match_reason TEXT, evidence TEXT
        );
        CREATE TABLE template_violations (
            id INTEGER PRIMARY KEY, path TEXT, violation_type TEXT,
            severity TEXT, details TEXT
        );
        INSERT INTO doc_standard_mapping VALUES (1,'core/a.md','ISO/IEC 27001',0.8,'expert_reviewed','test');
        INSERT INTO doc_standard_mapping VALUES (2,'core/b.md','ISO/IEC 27001',0.3,'keyword_match_scored','tokens');
        INSERT INTO doc_standard_mapping VALUES (3,'core/c.md','NIST CSF',0.6,'candidate_match','test');
        INSERT INTO template_violations VALUES (1,'core/bad.md','SECTION_MISSING','ERROR','missing section');
        INSERT INTO template_violations VALUES (2,'core/warn.md','SHORT_SECTION','WARNING','too short');
    """)
    conn.commit()
    conn.close()

    os.environ['IT_DOC_API_TOKEN'] = 'test-token'

    import scripts.api.main as api_main
    api_main.DB_PATH = db_path
    api_main.API_TOKEN = 'test-token'

    from scripts.api.main import app
    return TestClient(app)


def test_health_returns_ok(client):
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"
    assert data["total_mappings"] == 3


def test_list_templates_default(client):
    r = client.get("/templates")
    assert r.status_code == 200
    assert len(r.json()) == 3


def test_list_templates_filter_standard(client):
    r = client.get("/templates?standard=ISO/IEC 27001")
    assert r.status_code == 200
    assert len(r.json()) == 2
    for item in r.json():
        assert item["standard_code"] == "ISO/IEC 27001"


def test_list_templates_min_confidence(client):
    r = client.get("/templates?min_confidence=0.5")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 2
    for item in items:
        assert item["confidence"] >= 0.5


def test_list_templates_limit(client):
    r = client.get("/templates?limit=1")
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_get_coverage_iso(client):
    r = client.get("/coverage/ISO/IEC%2027001")
    assert r.status_code == 200
    data = r.json()
    assert data["standard_code"] == "ISO/IEC 27001"
    assert data["total_mappings"] == 2
    assert data["high_conf_50"] == 1  # only 0.8 >= 0.5 (0.3 is below)


def test_get_coverage_not_found(client):
    r = client.get("/coverage/FAKE_STANDARD")
    assert r.status_code == 404


def test_get_mappings_for_doc(client):
    r = client.get("/mappings/core/a.md")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 1
    assert items[0]["doc_path"] == "core/a.md"


def test_get_mappings_not_found(client):
    r = client.get("/mappings/nonexistent.md")
    assert r.status_code == 404


def test_list_violations(client):
    r = client.get("/violations")
    assert r.status_code == 200
    assert len(r.json()) == 2


def test_list_violations_filter_error(client):
    r = client.get("/violations?severity=ERROR")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 1
    assert items[0]["severity"] == "ERROR"


def test_review_approve_requires_token(client):
    r = client.post("/review", json={"mapping_id": 1, "approved": True})
    assert r.status_code == 401


def test_review_approve_with_valid_token(client):
    r = client.post(
        "/review",
        json={"mapping_id": 1, "approved": True, "notes": "looks good"},
        headers={"Authorization": "Bearer test-token"},
    )
    assert r.status_code == 200
    data = r.json()
    assert data["action"] == "approved"
    assert data["mapping_id"] == 1
    assert data["new_confidence"] == 0.8
    assert data["new_match_reason"] == "expert_reviewed"


def test_review_reject_with_valid_token(client):
    r = client.post(
        "/review",
        json={"mapping_id": 2, "approved": False},
        headers={"Authorization": "Bearer test-token"},
    )
    assert r.status_code == 200
    data = r.json()
    assert data["action"] == "rejected"
    assert data["mapping_id"] == 2
    assert data["new_confidence"] is None


def test_review_not_found(client):
    """Covers line 139: mapping_id not found → 404."""
    r = client.post(
        "/review",
        json={"mapping_id": 9999, "approved": True},
        headers={"Authorization": "Bearer test-token"},
    )
    assert r.status_code == 404
    assert "9999" in r.json()["detail"]


def test_violations_missing_table(tmp_path):
    """Covers lines 122-123: OperationalError when template_violations table is missing → returns []."""
    import sqlite3
    import os
    db_path = tmp_path / "empty.db"
    conn = sqlite3.connect(db_path)
    # Create legacy-runtime required tables but NOT template_violations
    conn.executescript("""
        CREATE TABLE _schema_version (version TEXT, applied_at TEXT);
        INSERT INTO _schema_version VALUES ('1.0.0', '2026-01-01');
        CREATE TABLE docs (doc_uid TEXT PRIMARY KEY, title TEXT, title_norm TEXT, path TEXT, origin TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        CREATE TABLE sections (section_uid TEXT PRIMARY KEY, doc_uid TEXT, heading_text TEXT, heading_norm TEXT, heading_level INTEGER, heading_path TEXT, anchor TEXT, ordinal INTEGER, status TEXT, text_fingerprint_sha256 TEXT, start_line INTEGER, end_line INTEGER);
        CREATE TABLE standards (standard_id INTEGER PRIMARY KEY, standard_code TEXT, standard_name TEXT, standard_name_en TEXT, description TEXT, version TEXT, url TEXT, applicable_industries TEXT);
        CREATE TABLE compliance_regulations (id INTEGER PRIMARY KEY, regulation_code TEXT, regulation_name TEXT, jurisdiction TEXT, industry TEXT, key_requirements TEXT, penalty_info TEXT, data_engineering_impact TEXT);
        CREATE TABLE content_links (id INTEGER PRIMARY KEY, from_doc TEXT, to_doc TEXT, link_type TEXT);
        INSERT INTO content_links VALUES (1, 'core/a.md', 'core/b.md', 'requires');
        CREATE TABLE content_links_resolved (id INTEGER PRIMARY KEY, content_link_id INTEGER, from_kind TEXT, from_uid TEXT, to_kind TEXT, to_uid TEXT, link_type TEXT, direction TEXT, rationale TEXT, strength TEXT, resolution_method TEXT, resolution_confidence REAL, notes TEXT);
        INSERT INTO content_links_resolved VALUES (1, 1, 'doc', 'UID001', 'doc', 'UID002', 'requires', 'forward', '', 'required', 'explicit', 1.0, '');
        CREATE TABLE rhythm_edges (edge_id INTEGER PRIMARY KEY, from_node TEXT, to_node TEXT, rhythm_type TEXT, weight REAL, conditions TEXT, version_range TEXT, notes TEXT);
        INSERT INTO rhythm_edges VALUES (1, 'UID001', 'UID002', 'triggers', 0.9, '', '', '');
        CREATE TABLE contracts (contract_id INTEGER PRIMARY KEY, scope_kind TEXT, scope_uid TEXT, version TEXT, inputs_json TEXT, outputs_json TEXT, gates_json TEXT, impact_json TEXT, owner TEXT, notes TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        INSERT INTO contracts VALUES (1, 'doc', 'UID001', '1.0', '[]', '[]', '[]', '{}', 'owner', '', '2026-01-01', '2026-01-01');
        CREATE TABLE flags (id INTEGER PRIMARY KEY, doc_uid TEXT, version TEXT, branch_id INTEGER, access_mask INTEGER);
        INSERT INTO flags VALUES (1, 'UID001', '1.0.0', 1, 0);
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY, doc_path TEXT, standard_code TEXT,
            confidence REAL, match_reason TEXT, evidence TEXT
        );
    """)
    conn.close()

    os.environ['IT_DOC_API_TOKEN'] = 'test-token'

    import scripts.api.main as api_main
    api_main.DB_PATH = db_path
    api_main.API_TOKEN = 'test-token'

    from scripts.api.main import app
    from fastapi.testclient import TestClient
    c = TestClient(app)
    r = c.get("/violations")
    assert r.status_code == 200
    assert r.json() == []
