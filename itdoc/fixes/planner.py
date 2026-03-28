"""
Fix plan generation for the autofix engine.

A FixPlan is a JSON-serializable record of all proposed changes,
generated BEFORE any files are modified.
"""
from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


@dataclass
class Change:
    """A single proposed file change."""
    file: str           # relative path from repo root
    rule_id: str
    severity: str       # "ERROR" | "WARNING"
    action: str         # "insert_section" | "strip_emoji" | "report_only"
    detail: dict        # rule-specific, e.g. {"section": "## Cel dokumentu"}
    safe_autofix: bool


@dataclass
class FixPlan:
    """Complete plan of proposed changes for a directory scan."""
    schema_version: str
    run_id: str          # ISO timestamp
    mode: str            # "analyze" | "dry-run" | "apply"
    root: str            # scanned root directory
    total_files: int
    changes: list[Change] = field(default_factory=list)

    def safe_changes(self) -> list[Change]:
        """Return only changes marked safe_autofix=True."""
        return [c for c in self.changes if c.safe_autofix]

    def unsafe_changes(self) -> list[Change]:
        """Return changes that require manual review."""
        return [c for c in self.changes if not c.safe_autofix]

    def by_file(self) -> dict[str, list[Change]]:
        """Group changes by file path."""
        result: dict[str, list[Change]] = {}
        for c in self.changes:
            result.setdefault(c.file, []).append(c)
        return result


def build_plan(root: Path, mode: str) -> FixPlan:
    """
    Scan root for .md files, analyze each, and return a FixPlan.
    Does NOT modify any files.
    """
    from itdoc.fixes.markdown_model import parse
    from itdoc.fixes.rules import analyze

    run_id = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    md_files = sorted(root.rglob('*.md'))
    changes: list[Change] = []

    for md_path in md_files:
        try:
            doc = parse(md_path)
        except Exception as e:
            # Non-parseable file: record as report_only
            changes.append(Change(
                file=str(md_path),
                rule_id="DOC.PARSE.ERROR",
                severity="ERROR",
                action="report_only",
                detail={"error": str(e)},
                safe_autofix=False,
            ))
            continue

        findings = analyze(doc)
        for finding in findings:
            changes.append(Change(
                file=str(md_path),
                rule_id=finding.rule.rule_id,
                severity=finding.rule.severity,
                action=finding.rule.action,
                detail=finding.detail,
                safe_autofix=finding.rule.safe_autofix,
            ))

    return FixPlan(
        schema_version="1.0",
        run_id=run_id,
        mode=mode,
        root=str(root),
        total_files=len(md_files),
        changes=changes,
    )


def save_plan(plan: FixPlan, output: Path) -> None:
    """Serialize FixPlan to a JSON file."""
    output.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "schema_version": plan.schema_version,
        "run_id": plan.run_id,
        "mode": plan.mode,
        "root": plan.root,
        "total_files": plan.total_files,
        "changes": [asdict(c) for c in plan.changes],
    }
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def load_plan(path: Path) -> FixPlan:
    """Deserialize a FixPlan from a JSON file."""
    data = json.loads(path.read_text(encoding='utf-8'))
    changes = [Change(**c) for c in data.get('changes', [])]
    return FixPlan(
        schema_version=data['schema_version'],
        run_id=data['run_id'],
        mode=data['mode'],
        root=data['root'],
        total_files=data['total_files'],
        changes=changes,
    )
