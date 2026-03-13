"""tests/test_api_models.py

Unit testy dla modeli Pydantic z scripts/api/models.py.
Weryfikuje: wymagane pola, pola opcjonalne (None), typy, serialization.
"""

import pytest
from pydantic import ValidationError

from scripts.api.models import CoverageOut, ReviewIn, ReviewOut, TemplateOut, ViolationOut


class TestTemplateOut:
    def test_all_fields_populated(self):
        t = TemplateOut(
            doc_path="core/security/policy.md",
            standard_code="ISO/IEC 27001",
            confidence=0.85,
            match_reason="keyword_match",
            evidence="security policy keyword found",
        )
        assert t.doc_path == "core/security/policy.md"
        assert t.standard_code == "ISO/IEC 27001"
        assert t.confidence == 0.85
        assert t.match_reason == "keyword_match"
        assert t.evidence == "security policy keyword found"

    def test_optional_fields_accept_none(self):
        # W Pydantic v2: Optional[X] bez = None nadal wymaga podania None explicite
        t = TemplateOut(
            doc_path="core/policy.md",
            standard_code="ISO/IEC 27001",
            confidence=None,
            match_reason=None,
            evidence=None,
        )
        assert t.confidence is None
        assert t.match_reason is None
        assert t.evidence is None

    def test_required_doc_path_missing_raises(self):
        with pytest.raises(ValidationError):
            TemplateOut(standard_code="ISO/IEC 27001")

    def test_required_standard_code_missing_raises(self):
        with pytest.raises(ValidationError):
            TemplateOut(doc_path="core/policy.md")

    def test_dict_serialization(self):
        t = TemplateOut(
            doc_path="core/policy.md",
            standard_code="ISO/IEC 27001",
            confidence=0.9,
            match_reason="explicit_audit",
            evidence=None,
        )
        d = t.model_dump()
        assert d["doc_path"] == "core/policy.md"
        assert d["confidence"] == 0.9
        assert d["evidence"] is None


class TestCoverageOut:
    def test_all_fields(self):
        c = CoverageOut(
            standard_code="ISO/IEC 27001",
            total_mappings=150,
            high_conf_50=120,
            high_conf_70=90,
            coverage_pct_50=80.0,
        )
        assert c.standard_code == "ISO/IEC 27001"
        assert c.total_mappings == 150
        assert c.high_conf_50 == 120
        assert c.high_conf_70 == 90
        assert c.coverage_pct_50 == 80.0

    def test_required_fields_missing_raises(self):
        with pytest.raises(ValidationError):
            CoverageOut(standard_code="ISO/IEC 27001")

    def test_zero_values_valid(self):
        c = CoverageOut(
            standard_code="UNKNOWN",
            total_mappings=0,
            high_conf_50=0,
            high_conf_70=0,
            coverage_pct_50=0.0,
        )
        assert c.total_mappings == 0
        assert c.coverage_pct_50 == 0.0

    def test_serialization_fields(self):
        c = CoverageOut(
            standard_code="NIST",
            total_mappings=10,
            high_conf_50=5,
            high_conf_70=3,
            coverage_pct_50=50.0,
        )
        d = c.model_dump()
        assert set(d.keys()) == {
            "standard_code",
            "total_mappings",
            "high_conf_50",
            "high_conf_70",
            "coverage_pct_50",
        }


class TestViolationOut:
    def test_required_fields(self):
        v = ViolationOut(path="core/policy.md", violation_type="missing_section", severity="high")
        assert v.path == "core/policy.md"
        assert v.violation_type == "missing_section"
        assert v.severity == "high"
        assert v.details is None

    def test_with_details(self):
        v = ViolationOut(
            path="core/policy.md",
            violation_type="forbidden_placeholder",
            severity="medium",
            details="[Rola / interesariusz] found in body",
        )
        assert v.details == "[Rola / interesariusz] found in body"

    def test_missing_required_raises(self):
        with pytest.raises(ValidationError):
            ViolationOut(path="core/policy.md", violation_type="missing_section")


class TestReviewIn:
    def test_required_fields(self):
        r = ReviewIn(mapping_id=42, approved=True)
        assert r.mapping_id == 42
        assert r.approved is True
        assert r.notes == ""
        assert r.confidence_override is None

    def test_approved_false(self):
        r = ReviewIn(mapping_id=1, approved=False, notes="wrong mapping")
        assert r.approved is False
        assert r.notes == "wrong mapping"

    def test_with_confidence_override(self):
        r = ReviewIn(mapping_id=5, approved=True, confidence_override=0.95)
        assert r.confidence_override == 0.95

    def test_missing_required_raises(self):
        with pytest.raises(ValidationError):
            ReviewIn(mapping_id=1)  # approved missing

    def test_mapping_id_missing_raises(self):
        with pytest.raises(ValidationError):
            ReviewIn(approved=True)


class TestReviewOut:
    def test_required_fields(self):
        r = ReviewOut(mapping_id=10, action="approved", new_confidence=0.9, new_match_reason="explicit_audit")
        assert r.mapping_id == 10
        assert r.action == "approved"
        assert r.new_confidence == 0.9
        assert r.new_match_reason == "explicit_audit"

    def test_rejected_action(self):
        r = ReviewOut(mapping_id=3, action="rejected", new_confidence=None, new_match_reason=None)
        assert r.action == "rejected"
        assert r.new_confidence is None
        assert r.new_match_reason is None

    def test_missing_required_raises(self):
        with pytest.raises(ValidationError):
            ReviewOut(action="approved")  # mapping_id missing
