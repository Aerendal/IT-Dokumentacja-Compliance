"""tests/test_check_standards_online.py

Testy dla scripts/check_standards_online.py.

Pokrywa:
- validate_format() — czysta funkcja, bez IO
- check_url() — z mock HTTP (unittest.mock.patch)
- check_mapping_quality() — z prawdziwym SQLite
- main() --offline — bez połączeń HTTP
"""

import sqlite3
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import check_standards_online as cso


# ---------------------------------------------------------------------------
# validate_format()
# ---------------------------------------------------------------------------


class TestValidateFormat:
    """Weryfikuje poprawność formatu kodów standardów bez IO."""

    # --- Poprawne formaty ---
    @pytest.mark.parametrize("code", [
        "ISO/IEC 27001",
        "ISO/IEC 27001-2",
        "ISO/IEC 42001",
        "ISO 9001",
        "ISO 22301",
        "IEEE 829",
        "IEEE 42010",
        "NIST CSF",
        "NIST SP 800-53",
        "OWASP ASVS",
        "OWASP SAMM",
        "ITIL",
        "ITIL v4",
        "COBIT",
        "TOGAF",
        "PMBOK",
        "PRINCE2",
        "SAFe",
        "SCRUM Guide",
        "PCI DSS",
        "SOC 2",
        "NIS2",
        "DORA",
        "GDPR",
    ])
    def test_valid_codes_return_true(self, code):
        valid, msg = cso.validate_format(code)
        assert valid is True, f"Oczekiwano True dla {code!r}, dostałem: {msg}"

    # --- Niepoprawne formaty ---
    @pytest.mark.parametrize("code", [
        "27001",           # brak prefiksu
        "ISO27001",        # brak spacji
        "",                # pusty
        "random text",     # nieznany format
        "ISO IEC 27001",   # brak ukośnika
    ])
    def test_invalid_codes_return_false(self, code):
        valid, msg = cso.validate_format(code)
        assert valid is False, f"Oczekiwano False dla {code!r}"
        assert "Nieznany format" in msg

    def test_returns_tuple_of_two(self):
        result = cso.validate_format("ISO/IEC 27001")
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_valid_returns_ok_message(self):
        valid, msg = cso.validate_format("ISO/IEC 27001")
        assert valid is True
        assert "OK" in msg

    def test_invalid_code_message_contains_repr(self):
        _, msg = cso.validate_format("UNKNOWN-CODE")
        assert "UNKNOWN-CODE" in msg


# ---------------------------------------------------------------------------
# check_url() — mock HTTP
# ---------------------------------------------------------------------------


class TestCheckUrl:
    def test_returns_200_for_successful_request(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        with patch("check_standards_online.requests.get", return_value=mock_response):
            status, info = cso.check_url("https://example.com")
        assert status == 200
        assert "200" in info

    def test_returns_404_for_not_found(self):
        mock_response = MagicMock()
        mock_response.status_code = 404
        with patch("check_standards_online.requests.get", return_value=mock_response):
            status, info = cso.check_url("https://example.com/missing")
        assert status == 404

    def test_connection_error_returns_0(self):
        import requests as _req
        with patch("check_standards_online.requests.get",
                   side_effect=_req.exceptions.ConnectionError("no network")):
            status, info = cso.check_url("https://unreachable.example.com")
        assert status == 0
        assert "ConnectionError" in info

    def test_timeout_returns_0(self):
        import requests as _req
        with patch("check_standards_online.requests.get",
                   side_effect=_req.exceptions.Timeout("timed out")):
            status, info = cso.check_url("https://slow.example.com", timeout=1)
        assert status == 0
        assert "Timeout" in info

    def test_returns_minus1_when_requests_not_available(self, monkeypatch):
        monkeypatch.setattr(cso, "_HAS_REQUESTS", False)
        status, info = cso.check_url("https://example.com")
        assert status == -1
        assert "niedostepny" in info

    def test_returns_tuple_of_two(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        with patch("check_standards_online.requests.get", return_value=mock_response):
            result = cso.check_url("https://example.com")
        assert isinstance(result, tuple)
        assert len(result) == 2


# ---------------------------------------------------------------------------
# check_mapping_quality() — real SQLite
# ---------------------------------------------------------------------------


def _make_quality_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT,
            standard_code TEXT,
            confidence REAL,
            match_reason TEXT
        )
    """)
    conn.executemany(
        "INSERT INTO doc_standard_mapping (doc_path, standard_code, confidence, match_reason) VALUES (?,?,?,?)",
        [
            ("core/security/policy.md", "ISO/IEC 27001", 0.9, "keyword_match"),
            ("core/security/procedure.md", "ISO/IEC 27001", 0.8, "keyword_match"),
            ("core/hr/onboarding.md", "ITIL", 0.5, "explicit_audit"),  # NOT keyword_match
        ],
    )
    conn.commit()
    return conn


class TestCheckMappingQuality:
    def test_returns_list(self):
        conn = _make_quality_db()
        result = cso.check_mapping_quality(conn)
        assert isinstance(result, list)

    def test_only_keyword_match_rows_included(self):
        conn = _make_quality_db()
        result = cso.check_mapping_quality(conn)
        # only keyword_match rows → max 2
        assert len(result) <= 2

    def test_result_has_required_keys(self):
        conn = _make_quality_db()
        result = cso.check_mapping_quality(conn)
        for row in result:
            assert "doc_path" in row
            assert "standard_code" in row
            assert "found_keywords" in row
            assert "quality" in row

    def test_quality_values_are_valid(self):
        conn = _make_quality_db()
        result = cso.check_mapping_quality(conn)
        valid_qualities = {"OK", "NO_KEYWORDS", "NO_RULES"}
        for row in result:
            assert row["quality"] in valid_qualities

    def test_empty_db_returns_empty_list(self):
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE doc_standard_mapping (
                id INTEGER PRIMARY KEY,
                doc_path TEXT, standard_code TEXT,
                confidence REAL, match_reason TEXT
            )
        """)
        conn.commit()
        result = cso.check_mapping_quality(conn)
        assert result == []

    def test_sample_limit_respected(self):
        conn = _make_quality_db()
        result = cso.check_mapping_quality(conn, sample=1)
        assert len(result) <= 1

    def test_missing_file_does_not_crash(self):
        """Plik .md nie istnieje → quality='NO_RULES' lub 'NO_KEYWORDS', nie wyjątek."""
        conn = _make_quality_db()
        result = cso.check_mapping_quality(conn)
        # powinno wykonać się bez wyjątku
        assert isinstance(result, list)


# ---------------------------------------------------------------------------
# main() --offline
# ---------------------------------------------------------------------------


class TestMainOffline:
    def test_offline_mode_no_http_calls(self, tmp_path, monkeypatch):
        """--offline nie wywołuje requests.get."""
        db_path = tmp_path / "test.db"
        conn = sqlite3.connect(str(db_path))
        conn.execute("""
            CREATE TABLE standards (
                standard_id INTEGER PRIMARY KEY,
                standard_code TEXT,
                url TEXT
            )
        """)
        conn.execute("INSERT INTO standards (standard_code, url) VALUES ('ISO/IEC 27001', 'https://example.com')")
        conn.execute("""
            CREATE TABLE doc_standard_mapping (
                id INTEGER PRIMARY KEY,
                doc_path TEXT, standard_code TEXT,
                confidence REAL, match_reason TEXT
            )
        """)
        conn.commit()
        conn.close()

        monkeypatch.setattr(cso, "DB_PATH", db_path)

        http_called = []
        with patch("check_standards_online.requests.get",
                   side_effect=lambda *a, **kw: http_called.append(True)):
            import sys as _sys
            old_argv = _sys.argv
            _sys.argv = ["check_standards_online.py", "--offline"]
            try:
                cso.main()
            except SystemExit:
                pass
            finally:
                _sys.argv = old_argv

        assert len(http_called) == 0, "HTTP nie powinno być wywołane w trybie --offline"
