"""
Lightweight Markdown document model for autofix engine.
Parses YAML frontmatter and section headings using stdlib only.
"""
from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Section:
    """A ## heading and its content within a Markdown document."""
    heading: str          # e.g. "## Cel dokumentu"
    content: str          # all text after the heading until next heading (may be empty)
    line_number: int      # 0-indexed line number of the heading line


@dataclass
class MarkdownDoc:
    """Parsed representation of a Markdown template file."""
    path: Path
    raw: str
    has_frontmatter: bool          # True if file starts with ---\n...\n---
    has_title_field: bool          # True if frontmatter contains 'title:'
    frontmatter_end_line: int      # 0-indexed last line of closing ---, or -1 if no frontmatter
    sections: list[Section] = field(default_factory=list)


_FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
_TITLE_RE = re.compile(r'^\s*title\s*:', re.MULTILINE)
_HEADING_RE = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)


def parse(path: Path) -> MarkdownDoc:
    """Parse a Markdown file and return a MarkdownDoc."""
    raw = path.read_text(encoding='utf-8', errors='replace')
    lines = raw.splitlines()

    # Detect frontmatter
    has_frontmatter = False
    has_title_field = False
    frontmatter_end_line = -1

    fm_match = _FRONTMATTER_RE.match(raw)
    if fm_match:
        has_frontmatter = True
        has_title_field = bool(_TITLE_RE.search(fm_match.group(1)))
        # Count lines consumed by frontmatter
        fm_text = fm_match.group(0)
        frontmatter_end_line = fm_text.count('\n') - 1  # 0-indexed last line

    # Parse sections: collect ## headings and their content
    sections: list[Section] = []
    body_start_line = frontmatter_end_line + 1 if has_frontmatter else 0
    body = '\n'.join(lines[body_start_line:])

    # Split by any heading (# through ######)
    heading_positions: list[tuple[int, str, int]] = []  # (char_offset, heading_text, line_no)
    for m in _HEADING_RE.finditer(body):
        heading_text = m.group(0)  # full "## Foo" line
        # Calculate line number relative to full file
        chars_before = body[:m.start()]
        relative_line = chars_before.count('\n')
        abs_line = body_start_line + relative_line
        heading_positions.append((m.start(), heading_text, abs_line))

    for i, (start, heading, line_no) in enumerate(heading_positions):
        # Content is everything after this heading until next heading
        if i + 1 < len(heading_positions):
            next_start = heading_positions[i + 1][0]
            content_raw = body[start + len(heading):next_start]
        else:
            content_raw = body[start + len(heading):]
        content = content_raw.strip()
        sections.append(Section(
            heading=heading.strip(),
            content=content,
            line_number=line_no,
        ))

    return MarkdownDoc(
        path=path,
        raw=raw,
        has_frontmatter=has_frontmatter,
        has_title_field=has_title_field,
        frontmatter_end_line=frontmatter_end_line,
        sections=sections,
    )


def section_headings(doc: MarkdownDoc) -> set[str]:
    """Return the set of heading strings in the document."""
    return {s.heading for s in doc.sections}
