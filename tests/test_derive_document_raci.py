"""
tests/test_derive_document_raci.py — unit tests for pure utility functions
in scripts/derive_document_raci.py.

Covers: parse_raci_table, default_raci_for_title
"""

import pytest

pytestmark = pytest.mark.unit


class TestDefaultRaciForTitle:
    def test_security_keyword(self):
        from scripts.derive_document_raci import default_raci_for_title

        r, a, c, i = default_raci_for_title("Polityka bezpieczeństwa IT")
        assert r == "SEC"
        assert a == "CISO"

    def test_architecture_keyword(self):
        from scripts.derive_document_raci import default_raci_for_title

        r, a, c, i = default_raci_for_title("Dokument architektury systemu")
        assert r == "ARCH"
        assert a == "CTO"

    def test_test_keyword(self):
        from scripts.derive_document_raci import default_raci_for_title

        r, a, c, i = default_raci_for_title("Plan testowania aplikacji")
        assert r == "QA"
        assert a == "PM"

    def test_incident_keyword(self):
        from scripts.derive_document_raci import default_raci_for_title

        r, a, c, i = default_raci_for_title("Procedura incident management")
        assert r == "SRE"
        assert a == "CISO"

    def test_change_keyword(self):
        from scripts.derive_document_raci import default_raci_for_title

        r, a, c, i = default_raci_for_title("Zarządzanie zmianami")
        assert r == "PM"
        assert a == "CTO"

    def test_data_keyword(self):
        from scripts.derive_document_raci import default_raci_for_title

        r, a, c, i = default_raci_for_title("Dane aplikacji systemowej")
        assert r == "DPO"
        assert a == "CISO"

    def test_requirements_keyword(self):
        from scripts.derive_document_raci import default_raci_for_title

        r, a, c, i = default_raci_for_title("Wymagania systemowe projektu")
        assert r == "BA"
        assert a == "PM"

    def test_compliance_keyword(self):
        from scripts.derive_document_raci import default_raci_for_title

        r, a, c, i = default_raci_for_title("Procedura zgodnosci z regulacjami")
        assert r == "AUDIT"
        assert a == "CISO"

    def test_default_fallback(self):
        from scripts.derive_document_raci import DEFAULT_RACI, default_raci_for_title

        result = default_raci_for_title("Nieznany dokument XYZ")
        assert result == DEFAULT_RACI

    def test_returns_four_tuple(self):
        from scripts.derive_document_raci import default_raci_for_title

        result = default_raci_for_title("Some title")
        assert len(result) == 4

    def test_empty_title_returns_default(self):
        from scripts.derive_document_raci import DEFAULT_RACI, default_raci_for_title

        result = default_raci_for_title("")
        assert result == DEFAULT_RACI


class TestParseRaciTable:
    SIMPLE_TABLE = """
| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|---------|
| Tworzenie dokumentu | DEV | PM | BA | OPS |
| Przegląd dokumentu | QA | PM | BA | DEV |
"""

    def test_parses_basic_raci_table(self):
        from scripts.derive_document_raci import parse_raci_table

        rows = parse_raci_table(self.SIMPLE_TABLE)
        assert len(rows) == 2

    def test_first_row_values(self):
        from scripts.derive_document_raci import parse_raci_table

        rows = parse_raci_table(self.SIMPLE_TABLE)
        action, resp, acc, cons, inf = rows[0]
        assert "Tworzenie" in action
        assert resp == "DEV"
        assert acc == "PM"

    def test_second_row_values(self):
        from scripts.derive_document_raci import parse_raci_table

        rows = parse_raci_table(self.SIMPLE_TABLE)
        action, resp, acc, cons, inf = rows[1]
        assert "Przegląd" in action
        assert resp == "QA"

    def test_no_table_returns_empty(self):
        from scripts.derive_document_raci import parse_raci_table

        text = "This text has no RACI table at all."
        rows = parse_raci_table(text)
        assert rows == []

    def test_empty_string_returns_empty(self):
        from scripts.derive_document_raci import parse_raci_table

        assert parse_raci_table("") == []

    def test_skips_very_long_action_rows(self):
        from scripts.derive_document_raci import parse_raci_table

        long_action = "X" * 101
        text = f"""
| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|---------|
| {long_action} | DEV | PM | BA | OPS |
| Short action | QA | PM | BA | DEV |
"""
        rows = parse_raci_table(text)
        # Long row should be skipped; only "Short action" row
        assert len(rows) == 1
        assert "Short action" in rows[0][0]

    def test_polish_header_keywords(self):
        from scripts.derive_document_raci import parse_raci_table

        text = """
| Czynność | Realizujący | Akceptujący | Konsultujący | Informowany |
|----------|------------|------------|-------------|------------|
| Wdrożenie | DEV | CTO | BA | OPS |
"""
        rows = parse_raci_table(text)
        assert len(rows) == 1
        assert rows[0][1] == "DEV"

    def test_rows_are_tuples_of_five(self):
        from scripts.derive_document_raci import parse_raci_table

        rows = parse_raci_table(self.SIMPLE_TABLE)
        for row in rows:
            assert len(row) == 5

    def test_table_stops_at_non_pipe_line(self):
        from scripts.derive_document_raci import parse_raci_table

        text = """
| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|---------|
| Action 1 | DEV | PM | BA | OPS |

This breaks the table.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|---------|
| Action 2 | QA | PM | BA | DEV |
"""
        rows = parse_raci_table(text)
        # Should only capture first table
        assert len(rows) == 1
        assert "Action 1" in rows[0][0]
