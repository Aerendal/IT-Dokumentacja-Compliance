"""Tests for pure functions in scripts/materialize_edges.py."""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from scripts.materialize_edges import norm, strength_from_required, utc_now_iso

pytestmark = pytest.mark.unit


class TestUtcNowIso:
    def test_returns_string(self):
        assert isinstance(utc_now_iso(), str)

    def test_format_matches_iso(self):
        result = utc_now_iso()
        assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", result)

    def test_ends_with_z(self):
        assert utc_now_iso().endswith("Z")

    def test_different_calls_not_equal(self):
        import time

        t1 = utc_now_iso()
        time.sleep(1.1)
        t2 = utc_now_iso()
        assert t1 != t2


class TestNorm:
    def test_lowercase(self):
        assert norm("HELLO WORLD") == "hello world"

    def test_strips_whitespace(self):
        assert norm("  hello  ") == "hello"

    def test_removes_emoji(self):
        result = norm("hello 🌍 world")
        assert "🌍" not in result
        assert "hello" in result

    def test_removes_numeric_prefix(self):
        result = norm("1. Introduction")
        assert result == "introduction"

    def test_removes_multi_numeric_prefix(self):
        result = norm("1.2. Sub section")
        assert "sub section" in result

    def test_collapses_spaces(self):
        result = norm("hello   world")
        assert result == "hello world"

    def test_none_safe(self):
        result = norm(None)
        assert result == ""

    def test_empty_string(self):
        assert norm("") == ""

    def test_plain_text_unchanged(self):
        assert norm("security policy") == "security policy"


class TestStrengthFromRequired:
    def test_required_one_returns_required(self):
        assert strength_from_required(1) == "required"

    def test_required_zero_returns_navigational(self):
        assert strength_from_required(0) == "navigational"

    def test_other_values_return_navigational(self):
        assert strength_from_required(2) == "navigational"
        assert strength_from_required(-1) == "navigational"

    def test_return_type_is_string(self):
        assert isinstance(strength_from_required(0), str)
        assert isinstance(strength_from_required(1), str)
