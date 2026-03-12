"""tests/test_anchor.py — testy jednostkowe funkcji to_anchor()."""

import pytest

from itdoc.anchor import to_anchor


class TestToAnchorBasic:
    def test_lowercase(self):
        assert to_anchor("Cel Dokumentu") == "cel-dokumentu"

    def test_spaces_to_dashes(self):
        assert to_anchor("zakres i granice") == "zakres-i-granice"

    def test_strip_leading_trailing(self):
        assert to_anchor("  Cel dokumentu  ") == "cel-dokumentu"

    def test_multiple_spaces_collapse(self):
        assert to_anchor("standardy  i  compliance") == "standardy-i-compliance"

    def test_multiple_dashes_collapse(self):
        # Myślniki w oryginalnym tekście → powinny być zkolapsowane
        assert to_anchor("a--b") == "a-b"

    def test_empty_string(self):
        assert to_anchor("") == ""

    def test_no_special_chars_preserved(self):
        # Znaki specjalne usunięte
        result = to_anchor("Wejścia: (meta)")
        assert "(" not in result
        assert ")" not in result
        assert ":" not in result

    def test_alphanumeric_preserved(self):
        result = to_anchor("iso 27001 controls")
        assert result == "iso-27001-controls"


class TestToAnchorPolishChars:
    """Polskie diakrytyki są USUWANE (nie transliterowane) — zgodnie z zachowaniem DB."""

    def test_a_ogonek_stripped(self):
        # 'ą' → strip (staje się '')
        result = to_anchor("zależności")
        assert "ą" not in result
        assert "e" not in result or "zaleno" in result  # 'ę' i 'ś' też stripped

    def test_mixed_polish(self):
        # Nagłówek "Użytkownicy i interesariusze" — polskie znaki usunięte
        result = to_anchor("Użytkownicy i interesariusze")
        assert "ż" not in result
        assert "ó" not in result
        assert "-i-" in result  # spójnik zachowany

    def test_result_is_ascii(self):
        # Wynik musi być czystym ASCII
        result = to_anchor("Właściciel dokumentu")
        assert result.isascii()

    def test_only_polish(self):
        # Wyraz składający się wyłącznie z polskich znaków → pusty lub myślnik
        result = to_anchor("ąęśźżóńćł")
        assert result == "" or result == "-"


class TestToAnchorPhaseFormat:
    """Nagłówki faz mają specjalny format: 'Faza N: ...' → 'phase-0N'."""

    def test_faza_3(self):
        assert to_anchor("Faza 3: Projekt / Design") == "phase-03"

    def test_faza_10(self):
        assert to_anchor("Faza 10: Archiwizacja") == "phase-10"

    def test_faza_1(self):
        assert to_anchor("Faza 1: Koncepcja i Wizja") == "phase-01"

    def test_faza_case_insensitive(self):
        # Lowercase "faza" też działa
        assert to_anchor("faza 5: implementacja") == "phase-05"


class TestToAnchorIdempotence:
    """to_anchor(to_anchor(x)) == to_anchor(x) — idempotentność."""

    @pytest.mark.parametrize(
        "text",
        [
            "Cel dokumentu",
            "Zakres i granice",
            "Standardy i compliance",
            "ISO 27001 Security Policy",
            "Faza 3: Design",
            "",
            "Użytkownicy i interesariusze",
        ],
    )
    def test_idempotent(self, text):
        once = to_anchor(text)
        twice = to_anchor(once)
        assert once == twice, f"Nie idempotentne dla: {text!r} → {once!r} → {twice!r}"
