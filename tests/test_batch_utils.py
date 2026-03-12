"""
tests/test_batch_utils.py — testy dla itdoc._batch.batch_continue().

Cel: udokumentować i zabezpieczyć CELOWE zachowanie batch_continue.
Te testy odpowiadają na pytanie:
  "Dlaczego mamy miejsca gdzie łapiemy Exception i kontynuujemy?"

Odpowiedź: bo przetwarzamy tysiące plików/rekordów i jeden zły nie powinien
zatrzymywać całego przebiegu. Ale ważne jest żeby:
  1. Wyjątek był LOGOWANY (nawet cicho na DEBUG)
  2. W trybie ITDOC_STRICT=1 był RE-RAISED (dla debugowania)
  3. Zachowanie było PRZETESTOWANE (nie "zgadywane")
"""

import logging

import pytest

from itdoc._batch import batch_continue

# ---------------------------------------------------------------------------
# Testy trybu normalnego (bez ITDOC_STRICT)
# ---------------------------------------------------------------------------


class TestBatchContinueNormalMode:
    """batch_continue() w trybie normalnym (ITDOC_STRICT=0/brak)."""

    def test_no_exception_passes_through(self):
        """Jeśli nie ma wyjątku — działa normalnie."""
        results = []
        with batch_continue("test item"):
            results.append(42)
        assert results == [42]

    def test_exception_is_swallowed(self):
        """Wyjątek jest łapany — pętla kontynuuje, nie crashuje."""
        processed = []
        items = [1, 2, "bad", 4]

        for item in items:
            with batch_continue(f"item {item}"):
                processed.append(int(item))  # "bad" -> ValueError

        # 3 z 4 przetworzono — "bad" zostało pominięte
        assert processed == [1, 2, 4]

    def test_exception_is_logged_at_debug(self, caplog):
        """Połknięty wyjątek trafia do logu na poziomie DEBUG."""
        with caplog.at_level(logging.DEBUG, logger="itdoc._batch"):
            with batch_continue("my context"):
                raise ValueError("test error")

        # Powinien być wpis na DEBUG z kontekstem i typem wyjątku
        assert any("my context" in r.message and "ValueError" in r.message for r in caplog.records)

    def test_log_contains_exception_message(self, caplog):
        """Log zawiera treść wyjątku — wiadomo dlaczego pominięto."""
        with caplog.at_level(logging.DEBUG, logger="itdoc._batch"):
            with batch_continue("processing file.txt"):
                raise OSError("Permission denied")

        assert any("Permission denied" in r.message for r in caplog.records)

    def test_custom_logger_used(self, caplog):
        """Można podać własny logger (dla kontekstu modułu)."""
        custom_log = logging.getLogger("my.module")
        with caplog.at_level(logging.DEBUG, logger="my.module"):
            with batch_continue("ctx", logger=custom_log):
                raise RuntimeError("oops")

        assert any("my.module" in r.name for r in caplog.records)

    def test_batch_of_1000_continues_on_errors(self):
        """Batch 1000 elementów: błędy nie przerywają przetwarzania."""
        good = 0
        bad = 0
        for i in range(1000):
            with batch_continue(f"item {i}"):
                if i % 7 == 0:
                    raise ValueError(f"bad item {i}")
                good += 1

        # ~857 dobrych, ~143 złych
        assert good > 800
        assert good + bad < 1000  # złe zostały pominięte (nie policzone w bad)

    def test_returns_value_via_side_effect(self):
        """Context manager nie zwraca wartości — używaj zmiennej zewnętrznej."""
        result = None
        with batch_continue("compute"):
            result = 2 + 2
        assert result == 4


# ---------------------------------------------------------------------------
# Testy trybu ITDOC_STRICT=1 (tryb debugowania)
# ---------------------------------------------------------------------------


class TestBatchContinueStrictMode:
    """batch_continue() w trybie ITDOC_STRICT=1 — wszystkie wyjątki re-raised."""

    def test_strict_mode_reraises_exception(self, monkeypatch):
        """W trybie STRICT wyjątek jest re-raised (nie połykany)."""
        monkeypatch.setenv("ITDOC_STRICT", "1")

        with pytest.raises(RuntimeError, match="ITDOC_STRICT=1"):
            with batch_continue("strict test"):
                raise ValueError("this should propagate")

    def test_strict_mode_original_cause_preserved(self, monkeypatch):
        """Oryginalny wyjątek jest zachowany jako __cause__ (chain)."""
        monkeypatch.setenv("ITDOC_STRICT", "1")

        with pytest.raises(RuntimeError) as exc_info:
            with batch_continue("chain test"):
                raise ValueError("original error")

        assert exc_info.value.__cause__ is not None
        assert isinstance(exc_info.value.__cause__, ValueError)
        assert "original error" in str(exc_info.value.__cause__)

    def test_strict_mode_context_in_message(self, monkeypatch):
        """Komunikat zawiera context string — wiadomo gdzie pękło."""
        monkeypatch.setenv("ITDOC_STRICT", "1")

        with pytest.raises(RuntimeError) as exc_info:
            with batch_continue("processing row id=42"):
                raise KeyError("missing column")

        assert "processing row id=42" in str(exc_info.value)

    def test_strict_mode_off_by_default(self, monkeypatch):
        """Bez ITDOC_STRICT (lub ITDOC_STRICT=0) tryb jest normalny."""
        monkeypatch.delenv("ITDOC_STRICT", raising=False)

        # Nie powinno rzucać
        with batch_continue("normal"):
            raise RuntimeError("should be swallowed")

    def test_strict_mode_zero_is_normal(self, monkeypatch):
        """ITDOC_STRICT=0 to tryb normalny (nie strict)."""
        monkeypatch.setenv("ITDOC_STRICT", "0")

        # Nie powinno rzucać
        with batch_continue("normal zero"):
            raise RuntimeError("should be swallowed")


# ---------------------------------------------------------------------------
# Testy parametru reraise
# ---------------------------------------------------------------------------


class TestBatchContinueReraise:
    """Typy wyjątków które zawsze są propagowane (niezależnie od ITDOC_STRICT)."""

    def test_reraise_type_always_propagates(self):
        """Wyjątek z reraise jest zawsze re-raised nawet w trybie normalnym."""
        with pytest.raises(MemoryError):
            with batch_continue("mem test", reraise=(MemoryError,)):
                raise MemoryError("OOM")

    def test_other_exceptions_still_swallowed(self):
        """Inne wyjątki nadal są łapane gdy reraise dotyczy tylko niektórych."""
        with batch_continue("mixed", reraise=(MemoryError,)):
            raise ValueError("this is swallowed")  # OK

    def test_reraise_multiple_types(self):
        """Można podać kilka typów do reraise."""
        for exc_type in (MemoryError, KeyboardInterrupt):
            with pytest.raises(exc_type):
                with batch_continue("multi", reraise=(MemoryError, KeyboardInterrupt)):
                    raise exc_type()


# ---------------------------------------------------------------------------
# Testy integracyjne: symulacja rzeczywistych użyć z codebase
# ---------------------------------------------------------------------------


class TestBatchContinueRealWorldPatterns:
    """Symulacja wzorców rzeczywiście używanych w scripts/."""

    def test_file_processing_pattern(self, tmp_path):
        """Symuluje: przetwarzanie listy plików gdzie część jest uszkodzona."""
        # Utwórz pliki: 2 dobre, 1 pusty (parse error), 2 dobre
        good = [tmp_path / f"good_{i}.txt" for i in range(4)]
        for f in good:
            f.write_text("valid content")
        bad = tmp_path / "bad.txt"
        bad.write_bytes(b"\xff\xfe invalid utf8 \x00")  # nie UTF-8

        processed = []
        files = [good[0], good[1], bad, good[2], good[3]]

        for path in files:
            with batch_continue(f"read {path.name}"):
                path.read_text(encoding="utf-8")  # bad.txt -> UnicodeDecodeError
                processed.append(path.name)

        # 4 dobre przetworzone, bad.txt pominięty
        assert len(processed) == 4
        assert "bad.txt" not in processed

    def test_db_row_processing_pattern(self):
        """Symuluje: iteracja po wierszach DB gdzie część ma None w wymaganych polach."""
        import sqlite3

        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.execute("CREATE TABLE t (id INTEGER, val TEXT)")
        conn.executemany(
            "INSERT INTO t VALUES (?, ?)",
            [(1, "ok"), (2, None), (3, "ok"), (4, None), (5, "ok")],
        )

        results = []
        for row in conn.execute("SELECT * FROM t"):
            with batch_continue(f"row id={row['id']}"):
                # None.upper() -> AttributeError
                results.append(row["val"].upper())

        assert results == ["OK", "OK", "OK"]
        assert len(results) == 3  # 2 None pominięte

    def test_strict_mode_reveals_hidden_bugs(self, monkeypatch):
        """
        ITDOC_STRICT=1 pozwala wykryć błędy które normalnie są połykane.
        To jest wartość debugowa — bez strict mode ten błąd byłby niewidoczny.
        """
        monkeypatch.setenv("ITDOC_STRICT", "1")

        data = [1, 2, 0, 4]  # 0 spowoduje ZeroDivisionError
        results = []

        # W trybie strict pierwsza iteracja z błędem crashuje — to CELOWE
        with pytest.raises(RuntimeError):
            for x in data:
                with batch_continue(f"divide by {x}"):
                    results.append(100 // x)

        # Zobaczysz traceback i wiesz co naprawić
        # (bez strict mode byłoby: results = [100, 50, 25] bez żadnego ostrzeżenia)
