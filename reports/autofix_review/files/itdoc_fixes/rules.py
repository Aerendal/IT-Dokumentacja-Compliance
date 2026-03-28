"""
Rule definitions for the autofix engine.

V1 rules:
    DOC.SECTION.MISSING      — Required section not present        safe_autofix=True
    DOC.EMOJI.FORBIDDEN      — Emoji character in template file    safe_autofix=True
    DOC.FRONTMATTER.MISSING  — No YAML frontmatter block           safe_autofix=False
    DOC.FRONTMATTER.NO_TITLE — Frontmatter missing title field     safe_autofix=False
"""
from __future__ import annotations
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from itdoc.fixes.markdown_model import MarkdownDoc


REQUIRED_SECTIONS: list[str] = [
    "## Cel dokumentu",
    "## Zakres i granice",
    "## Wejścia i wyjścia",
]

SECTION_PLACEHOLDERS: dict[str, str] = {
    "## Cel dokumentu":    "<!-- TODO: Opisz cel dokumentu -->\n",
    "## Zakres i granice": "<!-- TODO: Opisz zakres i granice -->\n",
    "## Wejścia i wyjścia": "<!-- TODO: Opisz wejścia i wyjścia -->\n",
}


@dataclass(frozen=True)
class Rule:
    rule_id: str
    description: str
    severity: str        # "ERROR" | "WARNING"
    safe_autofix: bool   # True = can be applied automatically
    action: str          # "insert_section" | "strip_emoji" | "report_only"


@dataclass
class Finding:
    rule: Rule
    path: Path
    detail: dict  # rule-specific detail, e.g. {"section": "## Cel dokumentu"}


# V1 rule registry
RULES: dict[str, Rule] = {
    "DOC.SECTION.MISSING": Rule(
        rule_id="DOC.SECTION.MISSING",
        description="Required section is missing from template",
        severity="ERROR",
        safe_autofix=True,
        action="insert_section",
    ),
    "DOC.EMOJI.FORBIDDEN": Rule(
        rule_id="DOC.EMOJI.FORBIDDEN",
        description="Emoji character found in production template",
        severity="WARNING",
        safe_autofix=True,
        action="strip_emoji",
    ),
    "DOC.FRONTMATTER.MISSING": Rule(
        rule_id="DOC.FRONTMATTER.MISSING",
        description="YAML frontmatter block (---) is missing",
        severity="ERROR",
        safe_autofix=False,
        action="report_only",
    ),
    "DOC.FRONTMATTER.NO_TITLE": Rule(
        rule_id="DOC.FRONTMATTER.NO_TITLE",
        description="Frontmatter present but 'title:' field is missing",
        severity="WARNING",
        safe_autofix=False,
        action="report_only",
    ),
}


# Emoji Unicode ranges (matches check_no_emoji.py)
_EMOJI_RANGES = [
    (0x1F300, 0x1F5FF), (0x1F600, 0x1F64F), (0x1F680, 0x1F6FF),
    (0x1F700, 0x1F77F), (0x1F780, 0x1F7FF), (0x1F800, 0x1F8FF),
    (0x1F900, 0x1F9FF), (0x1FA00, 0x1FA6F), (0x1FA70, 0x1FAFF),
    (0x2600,  0x26FF),  (0x2700,  0x27BF),
    (0xFE00,  0xFE0F),  (0x1F1E6, 0x1F1FF),
]


def _is_emoji(ch: str) -> bool:
    cp = ord(ch)
    return any(lo <= cp <= hi for lo, hi in _EMOJI_RANGES)


def _has_emoji(text: str) -> bool:
    return any(_is_emoji(ch) for ch in text)


def _strip_emoji(text: str) -> str:
    return ''.join(ch for ch in text if not _is_emoji(ch))


def analyze(doc: "MarkdownDoc") -> list[Finding]:
    """
    Analyze a MarkdownDoc and return a list of Findings.
    Findings are ordered: frontmatter issues first, then section issues, then emoji.
    """
    from itdoc.fixes.markdown_model import section_headings

    findings: list[Finding] = []

    # DOC.FRONTMATTER.MISSING
    if not doc.has_frontmatter:
        findings.append(Finding(
            rule=RULES["DOC.FRONTMATTER.MISSING"],
            path=doc.path,
            detail={"message": "File does not start with --- YAML frontmatter block"},
        ))

    # DOC.FRONTMATTER.NO_TITLE (only if frontmatter exists)
    elif not doc.has_title_field:
        findings.append(Finding(
            rule=RULES["DOC.FRONTMATTER.NO_TITLE"],
            path=doc.path,
            detail={"message": "Frontmatter block has no 'title:' field"},
        ))

    # DOC.SECTION.MISSING — one Finding per missing required section
    present = section_headings(doc)
    for required in REQUIRED_SECTIONS:
        if required not in present:
            findings.append(Finding(
                rule=RULES["DOC.SECTION.MISSING"],
                path=doc.path,
                detail={"section": required, "placeholder": SECTION_PLACEHOLDERS[required]},
            ))

    # DOC.EMOJI.FORBIDDEN
    if _has_emoji(doc.raw):
        findings.append(Finding(
            rule=RULES["DOC.EMOJI.FORBIDDEN"],
            path=doc.path,
            detail={"message": "File contains emoji characters"},
        ))

    return findings
