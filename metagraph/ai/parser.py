"""AI-assisted parser — pattern-based, no LLM dependency."""
import re
from pathlib import Path
from typing import Optional


def extract_headings(text: str) -> list[dict]:
    """Wyciąga nagłówki Markdown jako sekcje."""
    sections = []
    current: Optional[dict] = None
    for line in text.splitlines():
        m = re.match(r"^(#{1,4})\s+(.+)", line)
        if m:
            if current:
                sections.append(current)
            current = {
                "level": len(m.group(1)),
                "title": m.group(2).strip(),
                "body": "",
                "section_id": None,
            }
        elif current:
            current["body"] += line + "\n"
    if current:
        sections.append(current)
    return sections


def detect_layer(text: str) -> str:
    """Heurystycznie wykrywa warstwę dokumentu."""
    text_lower = text.lower()
    pm_keywords = ["cel", "epika", "ryzyko", "milestone", "okr", "goal", "epic"]
    scrum_keywords = ["sprint", "story", "task", "backlog", "velocity", "standup"]
    docs_keywords = ["specyfikacja", "api", "endpoint", "tabela", "moduł", "architektura"]

    scores = {
        "pm": sum(text_lower.count(k) for k in pm_keywords),
        "scrum": sum(text_lower.count(k) for k in scrum_keywords),
        "docs": sum(text_lower.count(k) for k in docs_keywords),
    }
    return max(scores, key=scores.get)


def parse_finding_ids(text: str) -> list[dict]:
    """Wyciąga ID znalezisk w formacie [A-Z]-\\d+."""
    findings = []
    for m in re.finditer(r"\b([A-Z]-\d+)\b.*?(?:critical|important|minor)?", text, re.IGNORECASE):
        findings.append({"finding_id": m.group(1), "context": m.group(0)[:80]})
    return findings


def parse_markdown_file(file_path: str | Path) -> dict:
    """Parsuje plik Markdown i zwraca strukturę do ingestion."""
    path = Path(file_path)
    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "file_path": str(path),
        "layer": detect_layer(text),
        "sections": extract_headings(text),
        "findings": parse_finding_ids(text),
        "word_count": len(text.split()),
    }
