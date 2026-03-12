"""Pydantic models for the compliance API."""

from typing import Optional

from pydantic import BaseModel


class TemplateOut(BaseModel):
    doc_path: str
    standard_code: str
    confidence: Optional[float]
    match_reason: Optional[str]
    evidence: Optional[str]


class CoverageOut(BaseModel):
    standard_code: str
    total_mappings: int
    high_conf_50: int
    high_conf_70: int
    coverage_pct_50: float


class ViolationOut(BaseModel):
    path: str
    violation_type: str
    severity: str
    details: Optional[str] = None


class ReviewIn(BaseModel):
    mapping_id: int
    approved: bool
    notes: Optional[str] = ""
    confidence_override: Optional[float] = None


class ReviewOut(BaseModel):
    mapping_id: int
    action: str  # 'approved', 'rejected'
    new_confidence: Optional[float]
    new_match_reason: Optional[str]
