#!/usr/bin/env python3
"""
FastAPI REST wrapper dla IT Dokumentacja Compliance DB.

Uruchomienie:
  uvicorn scripts.api.main:app --reload --host 0.0.0.0 --port 8000

Dokumentacja: http://localhost:8000/docs
"""

import os
import sqlite3
from pathlib import Path
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Query, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .models import CoverageOut, ReviewIn, ReviewOut, TemplateOut, ViolationOut

app = FastAPI(
    title="IT Dokumentacja Compliance API",
    description="REST API dla biblioteki 9023 szablonów IT z mapowaniami compliance",
    version="1.0.0",
)

# DB path — can be overridden via env var IT_DOC_DB
DB_PATH = Path(
    os.getenv(
        "IT_DOC_DB", str(Path(__file__).parent.parent.parent / "reports" / "it_doc_matrix.db")
    )
)

# Auth token — set via IT_DOC_API_TOKEN env var (required for write endpoints)
API_TOKEN = os.getenv("IT_DOC_API_TOKEN", "change-me-before-production")

security = HTTPBearer(auto_error=False)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials is None or credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing API token")
    return credentials.credentials


# --- GET /templates ---
@app.get("/templates", response_model=list[TemplateOut], tags=["Templates"])
def list_templates(
    standard: Optional[str] = Query(None, description="Filter by standard_code"),
    min_confidence: float = Query(0.0, ge=0.0, le=1.0),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    conn: sqlite3.Connection = Depends(get_db),
):
    """List templates with their compliance mappings."""
    q = "SELECT doc_path, standard_code, confidence, match_reason, evidence FROM doc_standard_mapping WHERE confidence >= ?"
    params: list = [min_confidence]
    if standard:
        q += " AND standard_code = ?"
        params.append(standard)
    q += " ORDER BY standard_code, confidence DESC LIMIT ? OFFSET ?"
    params += [limit, offset]
    rows = conn.execute(q, params).fetchall()
    return [dict(r) for r in rows]


# --- GET /coverage/{standard_code} ---
@app.get("/coverage/{standard_code:path}", response_model=CoverageOut, tags=["Coverage"])
def get_coverage(standard_code: str, conn: sqlite3.Connection = Depends(get_db)):
    """Get compliance coverage metrics for a specific standard."""
    row = conn.execute(
        """
        SELECT standard_code,
               COUNT(*) as total_mappings,
               SUM(CASE WHEN confidence >= 0.5 THEN 1 ELSE 0 END) as high_conf_50,
               SUM(CASE WHEN confidence >= 0.7 THEN 1 ELSE 0 END) as high_conf_70
        FROM doc_standard_mapping
        WHERE standard_code = ?
        GROUP BY standard_code
    """,
        [standard_code],
    ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Standard '{standard_code}' not found")
    d = dict(row)
    total = d["total_mappings"] or 1
    d["coverage_pct_50"] = round((d["high_conf_50"] / total) * 100, 1)
    return d


# --- GET /mappings/{doc_path:path} ---
@app.get("/mappings/{doc_path:path}", response_model=list[TemplateOut], tags=["Templates"])
def get_mappings_for_doc(doc_path: str, conn: sqlite3.Connection = Depends(get_db)):
    """Get all standard mappings for a specific template."""
    rows = conn.execute(
        "SELECT doc_path, standard_code, confidence, match_reason, evidence FROM doc_standard_mapping WHERE doc_path = ? ORDER BY confidence DESC",
        [doc_path],
    ).fetchall()
    if not rows:
        raise HTTPException(status_code=404, detail=f"No mappings found for '{doc_path}'")
    return [dict(r) for r in rows]


# --- GET /violations ---
@app.get("/violations", response_model=list[ViolationOut], tags=["Schema"])
def list_violations(
    severity: Optional[str] = Query(None, description="ERROR or WARNING"),
    conn: sqlite3.Connection = Depends(get_db),
):
    """List template schema violations."""
    try:
        q = "SELECT path, violation_type, severity, details FROM template_violations"
        params: list = []
        if severity:
            q += " WHERE severity = ?"
            params.append(severity.upper())
        q += " ORDER BY severity, path"
        rows = conn.execute(q, params).fetchall()
        return [dict(r) for r in rows]
    except sqlite3.OperationalError:
        return []


# --- POST /review ---
@app.post("/review", response_model=ReviewOut, tags=["Review"])
def review_mapping(
    payload: ReviewIn,
    token: str = Depends(verify_token),
    conn: sqlite3.Connection = Depends(get_db),
):
    """Approve or reject a mapping (requires API token)."""
    row = conn.execute(
        "SELECT id, confidence FROM doc_standard_mapping WHERE id = ?", [payload.mapping_id]
    ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Mapping {payload.mapping_id} not found")

    evidence_note = f"expert approved: {payload.notes}" if payload.notes else "expert approved"

    if payload.approved:
        new_conf = (
            payload.confidence_override
            if payload.confidence_override is not None
            else max(row["confidence"] or 0.0, 0.8)
        )
        conn.execute(
            "UPDATE doc_standard_mapping SET match_reason='expert_reviewed', confidence=?, evidence=? WHERE id=?",
            [new_conf, evidence_note, payload.mapping_id],
        )
        conn.commit()
        return ReviewOut(
            mapping_id=payload.mapping_id,
            action="approved",
            new_confidence=new_conf,
            new_match_reason="expert_reviewed",
        )
    else:
        conn.execute("DELETE FROM doc_standard_mapping WHERE id=?", [payload.mapping_id])
        conn.commit()
        return ReviewOut(
            mapping_id=payload.mapping_id,
            action="rejected",
            new_confidence=None,
            new_match_reason=None,
        )


# --- GET /health ---
@app.get("/health", tags=["System"])
def health(conn: sqlite3.Connection = Depends(get_db)):
    """Health check — returns DB stats."""
    total = conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]
    null_c = conn.execute(
        "SELECT COUNT(*) FROM doc_standard_mapping WHERE confidence IS NULL"
    ).fetchone()[0]
    return {"status": "ok", "total_mappings": total, "null_confidence": null_c}
