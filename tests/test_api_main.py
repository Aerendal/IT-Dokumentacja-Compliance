"""
Tests for scripts/api/main.py — FastAPI REST endpoints.

Coverage: GET /health, GET /templates, GET /coverage/{code},
          GET /mappings/{path}, GET /violations, POST /review, auth checks.
"""

import sqlite3
from contextlib import contextmanager

import pytest
from fastapi.testclient import TestClient

from scripts.api.main import API_TOKEN, app, get_db


# ---------------------------------------------------------------------------
# DB fixture helpers
# ---------------------------------------------------------------------------

def _seed_db(path: str) -> None:
    """Create and seed test DB at path."""
    conn = sqlite3.connect(path)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS doc_standard_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT NOT NULL,
            standard_code TEXT NOT NULL,
            confidence REAL,
            match_reason TEXT,
            evidence TEXT
        );
        CREATE TABLE IF NOT EXISTS template_violations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT NOT NULL,
            violation_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            details TEXT
        );
        INSERT INTO doc_standard_mapping (doc_path, standard_code, confidence, match_reason, evidence)
        VALUES
            ('docs/security_policy.md', 'ISO/IEC 27001', 0.9, 'keyword_match', 'security keyword'),
            ('docs/security_policy.md', 'ISO/IEC 27002', 0.6, 'keyword_match', 'security policy'),
            ('docs/test_plan.md',       'ISO/IEC 29119', 0.8, 'keyword_match', 'test plan'),
            ('docs/test_plan.md',       'IEEE 829',      0.4, 'keyword_match', 'test doc'),
            ('docs/api_spec.md',        'ISO/IEC 27001', 0.3, 'keyword_match', 'api security');
        INSERT INTO template_violations (path, violation_type, severity, details)
        VALUES
            ('docs/orphan.md', 'missing_section', 'ERROR', 'No ## Purpose section'),
            ('docs/short.md',  'too_short',       'WARNING', 'Only 2 lines');
    """)
    conn.commit()
    conn.close()


@pytest.fixture()
def db_path(tmp_path):
    path = str(tmp_path / "test.db")
    _seed_db(path)
    return path


@pytest.fixture()
def test_db(db_path):
    """Read-back connection for asserting DB state after requests."""
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


@pytest.fixture()
def client(db_path):
    """TestClient with DB dependency overridden to use test DB file."""

    def override_get_db():
        conn = sqlite3.connect(db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


AUTH = {"Authorization": f"Bearer {API_TOKEN}"}
WRONG_AUTH = {"Authorization": "Bearer wrong-token"}


# ---------------------------------------------------------------------------
# GET /health
# ---------------------------------------------------------------------------

class TestHealth:
    def test_returns_ok(self, client):
        r = client.get("/health")
        assert r.status_code == 200
        assert r.json()["status"] == "ok"

    def test_returns_total_mappings(self, client):
        r = client.get("/health")
        assert r.json()["total_mappings"] == 5

    def test_returns_null_confidence_count(self, client):
        r = client.get("/health")
        assert r.json()["null_confidence"] == 0


# ---------------------------------------------------------------------------
# GET /templates
# ---------------------------------------------------------------------------

class TestListTemplates:
    def test_returns_list(self, client):
        r = client.get("/templates")
        assert r.status_code == 200
        assert isinstance(r.json(), list)

    def test_default_limit_respected(self, client):
        r = client.get("/templates")
        assert len(r.json()) <= 50

    def test_filter_by_standard(self, client):
        r = client.get("/templates?standard=ISO%2FIEC+27001")
        data = r.json()
        assert len(data) == 2
        for item in data:
            assert item["standard_code"] == "ISO/IEC 27001"

    def test_filter_by_min_confidence(self, client):
        r = client.get("/templates?min_confidence=0.7")
        data = r.json()
        for item in data:
            assert item["confidence"] >= 0.7

    def test_pagination_limit(self, client):
        r = client.get("/templates?limit=2")
        assert len(r.json()) == 2

    def test_pagination_offset(self, client):
        r1 = client.get("/templates?limit=2&offset=0")
        r2 = client.get("/templates?limit=2&offset=2")
        all_paths = {i["doc_path"] for i in r1.json()} | {i["doc_path"] for i in r2.json()}
        assert len(all_paths) >= 2  # different pages

    def test_empty_result_for_unknown_standard(self, client):
        r = client.get("/templates?standard=NONEXISTENT")
        assert r.status_code == 200
        assert r.json() == []

    def test_limit_out_of_range_returns_422(self, client):
        r = client.get("/templates?limit=0")
        assert r.status_code == 422

    def test_confidence_out_of_range_returns_422(self, client):
        r = client.get("/templates?min_confidence=2.0")
        assert r.status_code == 422


# ---------------------------------------------------------------------------
# GET /coverage/{standard_code}
# ---------------------------------------------------------------------------

class TestGetCoverage:
    def test_known_standard_returns_200(self, client):
        r = client.get("/coverage/ISO%2FIEC%2027001")
        assert r.status_code == 200

    def test_coverage_fields_present(self, client):
        r = client.get("/coverage/ISO%2FIEC%2027001")
        body = r.json()
        for field in ("standard_code", "total_mappings", "high_conf_50", "coverage_pct_50"):
            assert field in body

    def test_correct_total_mappings(self, client):
        r = client.get("/coverage/ISO%2FIEC%2027001")
        assert r.json()["total_mappings"] == 2

    def test_coverage_pct_50_value(self, client):
        # 1 of 2 mappings has confidence >= 0.5 (0.9). Second is 0.3 < 0.5
        # But security_policy 0.6 IS >=0.5. So high_conf_50 = 2 (0.9 + 0.6 ... wait 0.3 is api_spec)
        # Rows: (security_policy, 27001, 0.9), (api_spec, 27001, 0.3)
        r = client.get("/coverage/ISO%2FIEC%2027001")
        assert r.json()["coverage_pct_50"] == 50.0  # 1 of 2

    def test_unknown_standard_returns_404(self, client):
        r = client.get("/coverage/UNKNOWN_STANDARD")
        assert r.status_code == 404

    def test_standard_with_slash_in_path(self, client):
        r = client.get("/coverage/ISO%2FIEC%2029119")
        assert r.status_code == 200
        assert r.json()["total_mappings"] == 1


# ---------------------------------------------------------------------------
# GET /mappings/{doc_path}
# ---------------------------------------------------------------------------

class TestGetMappingsForDoc:
    def test_known_doc_returns_200(self, client):
        r = client.get("/mappings/docs/security_policy.md")
        assert r.status_code == 200

    def test_returns_all_mappings_for_doc(self, client):
        r = client.get("/mappings/docs/security_policy.md")
        assert len(r.json()) == 2

    def test_ordered_by_confidence_desc(self, client):
        r = client.get("/mappings/docs/security_policy.md")
        confs = [item["confidence"] for item in r.json()]
        assert confs == sorted(confs, reverse=True)

    def test_unknown_doc_returns_404(self, client):
        r = client.get("/mappings/docs/nonexistent.md")
        assert r.status_code == 404


# ---------------------------------------------------------------------------
# GET /violations
# ---------------------------------------------------------------------------

class TestListViolations:
    def test_returns_list(self, client):
        r = client.get("/violations")
        assert r.status_code == 200
        assert isinstance(r.json(), list)
        assert len(r.json()) == 2

    def test_filter_by_severity_error(self, client):
        r = client.get("/violations?severity=ERROR")
        data = r.json()
        assert all(v["severity"] == "ERROR" for v in data)
        assert len(data) == 1

    def test_filter_by_severity_warning(self, client):
        r = client.get("/violations?severity=WARNING")
        data = r.json()
        assert all(v["severity"] == "WARNING" for v in data)
        assert len(data) == 1

    def test_violation_fields_present(self, client):
        r = client.get("/violations")
        for v in r.json():
            for field in ("path", "violation_type", "severity"):
                assert field in v

    def test_empty_table_returns_empty_list(self, db_path):
        conn = sqlite3.connect(db_path)
        conn.execute("DELETE FROM template_violations")
        conn.commit()
        conn.close()

        def override_get_db():
            c = sqlite3.connect(db_path, check_same_thread=False)
            c.row_factory = sqlite3.Row
            try:
                yield c
            finally:
                c.close()

        app.dependency_overrides[get_db] = override_get_db
        with TestClient(app) as c:
            r = c.get("/violations")
        app.dependency_overrides.clear()
        assert r.status_code == 200
        assert r.json() == []


# ---------------------------------------------------------------------------
# POST /review — authentication
# ---------------------------------------------------------------------------

class TestReviewAuth:
    def test_missing_token_returns_401(self, client):
        r = client.post("/review", json={"mapping_id": 1, "approved": True})
        assert r.status_code == 401

    def test_wrong_token_returns_401(self, client):
        r = client.post(
            "/review",
            json={"mapping_id": 1, "approved": True},
            headers=WRONG_AUTH,
        )
        assert r.status_code == 401

    def test_correct_token_allows_access(self, client):
        r = client.post(
            "/review",
            json={"mapping_id": 1, "approved": True},
            headers=AUTH,
        )
        assert r.status_code == 200


# ---------------------------------------------------------------------------
# POST /review — approve
# ---------------------------------------------------------------------------

class TestReviewApprove:
    def test_approve_returns_approved_action(self, client):
        r = client.post(
            "/review",
            json={"mapping_id": 1, "approved": True},
            headers=AUTH,
        )
        assert r.json()["action"] == "approved"

    def test_approve_sets_match_reason_expert_reviewed(self, client, db_path):
        client.post("/review", json={"mapping_id": 1, "approved": True}, headers=AUTH)
        conn = sqlite3.connect(db_path)
        row = conn.execute(
            "SELECT match_reason FROM doc_standard_mapping WHERE id=1"
        ).fetchone()
        conn.close()
        assert row[0] == "expert_reviewed"

    def test_approve_confidence_override(self, client, db_path):
        client.post(
            "/review",
            json={"mapping_id": 2, "approved": True, "confidence_override": 0.99},
            headers=AUTH,
        )
        conn = sqlite3.connect(db_path)
        row = conn.execute(
            "SELECT confidence FROM doc_standard_mapping WHERE id=2"
        ).fetchone()
        conn.close()
        assert abs(row[0] - 0.99) < 0.001

    def test_approve_boosts_low_confidence_to_08(self, client, db_path):
        # mapping id=4 has confidence=0.4 — below 0.8
        client.post("/review", json={"mapping_id": 4, "approved": True}, headers=AUTH)
        conn = sqlite3.connect(db_path)
        row = conn.execute(
            "SELECT confidence FROM doc_standard_mapping WHERE id=4"
        ).fetchone()
        conn.close()
        assert row[0] >= 0.8

    def test_approve_nonexistent_mapping_returns_404(self, client):
        r = client.post(
            "/review", json={"mapping_id": 9999, "approved": True}, headers=AUTH
        )
        assert r.status_code == 404

    def test_approve_returns_new_confidence_field(self, client):
        r = client.post(
            "/review",
            json={"mapping_id": 1, "approved": True},
            headers=AUTH,
        )
        assert "new_confidence" in r.json()
        assert r.json()["new_confidence"] is not None


# ---------------------------------------------------------------------------
# POST /review — reject
# ---------------------------------------------------------------------------

class TestReviewReject:
    def test_reject_returns_rejected_action(self, client):
        r = client.post(
            "/review",
            json={"mapping_id": 3, "approved": False},
            headers=AUTH,
        )
        assert r.json()["action"] == "rejected"

    def test_reject_deletes_mapping_from_db(self, client, db_path):
        client.post("/review", json={"mapping_id": 3, "approved": False}, headers=AUTH)
        conn = sqlite3.connect(db_path)
        row = conn.execute(
            "SELECT id FROM doc_standard_mapping WHERE id=3"
        ).fetchone()
        conn.close()
        assert row is None

    def test_reject_returns_null_confidence(self, client):
        r = client.post(
            "/review",
            json={"mapping_id": 5, "approved": False},
            headers=AUTH,
        )
        assert r.json()["new_confidence"] is None
        assert r.json()["new_match_reason"] is None

    def test_reject_nonexistent_mapping_returns_404(self, client):
        r = client.post(
            "/review", json={"mapping_id": 9999, "approved": False}, headers=AUTH
        )
        assert r.status_code == 404
