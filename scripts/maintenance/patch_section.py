#!/usr/bin/env python3
"""
patch_section.py

Narzędzie do masowej edycji sekcji w plikach Markdown z obsługą YAML frontmatter,
atomic write, integracji z template_changelog oraz ThreadPool error handling.

Użycie:
    python3 patch_section.py --section "Standardy" --operation replace \\
        --old "stary tekst" --new "nowy tekst" --dry-run
    python3 patch_section.py --section "Standardy" --operation replace \\
        --old "stary tekst" --new "nowy tekst" --apply
    python3 patch_section.py --section "Wymagania" --operation append \\
        --content "- nowy punkt" --apply
    python3 patch_section.py --batch operacje.yaml
    python3 patch_section.py --report-matrix

Tryb domyślny to dry-run. Dodaj --apply aby zapisać zmiany.
"""

import argparse
import os
import re
import shutil
import json
import csv
import hashlib
import zipfile
import sqlite3
import threading
import sys
import difflib
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from collections import defaultdict

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

try:
    from jinja2 import Environment, BaseLoader
    JINJA_AVAILABLE = True
except ImportError:
    JINJA_AVAILABLE = False


# ---------------------------------------------------------------------------
# Stałe i ścieżki projektu
# ---------------------------------------------------------------------------

VERSION = "2.1.0"

_SCRIPT_DIR   = Path(__file__).parent
_PROJECT_ROOT = _SCRIPT_DIR.parent.parent          # dokumentacja/
DEFAULT_TEMPLATES_DIR = _PROJECT_ROOT / "generated_templates" / "core"
DEFAULT_DB_PATH       = _PROJECT_ROOT / "reports" / "it_doc_matrix.db"

ANSI_RESET  = "\033[0m"
ANSI_RED    = "\033[91m"
ANSI_GREEN  = "\033[92m"
ANSI_YELLOW = "\033[93m"
ANSI_CYAN   = "\033[96m"
ANSI_BOLD   = "\033[1m"
ANSI_DIM    = "\033[2m"

VALID_OPERATIONS = (
    "replace", "delete", "append", "prepend",
    "wrap", "rename", "extract", "normalize", "deduplicate",
)

AUDIT_LOG_FILE = "patch_audit.jsonl"

_print_lock = threading.Lock()


# ---------------------------------------------------------------------------
# TOP-LEVEL API (eksponowane dla testów i importu)
# ---------------------------------------------------------------------------

def strip_frontmatter(content: str) -> tuple:
    """Zwraca (frontmatter, body) — frontmatter = '' jeśli brak."""
    if content.startswith('---'):
        end = content.find('\n---\n', 3)
        if end != -1:
            return content[:end + 5], content[end + 5:]
    return '', content


def find_section(body: str, section_name: str) -> Optional[Tuple[int, int]]:
    """
    Zwraca (start_line, end_line) sekcji w body lub None.
    Numery linii są 1-indeksowane.
    Operuje TYLKO na body (bez frontmatter).
    """
    pattern = _build_section_pattern(section_name, None, None)
    match = pattern.search(body)
    if not match:
        return None
    start_line = body[: match.start()].count('\n') + 1
    end_line   = body[: match.end()].count('\n')
    return (start_line, max(start_line, end_line))


def apply_operation(body: str, section_name: str, operation: str, **kwargs) -> str:
    """
    Wykonuje operację na sekcji w body (bez frontmatter).

    Parametry kwargs zależne od operacji:
      replace  → content='...' lub old='...', new='...'
      append   → content='...'
      prepend  → content='...'
      delete   → (brak dodatkowych)
      rename   → new_name='...'
      wrap     → wrap_tag='>'
    """
    pattern = _build_section_pattern(section_name, None, None)

    old_text = kwargs.get('old', '')
    new_text_kw = kwargs.get('new', '')
    content_kw  = kwargs.get('content', '')

    if operation == 'replace' and old_text:
        # Podmiana podłańcucha wewnątrz sekcji
        match = pattern.search(body)
        if not match:
            return body
        section_body = match.group(2)
        if old_text not in section_body:
            return body
        new_section_body = section_body.replace(old_text, new_text_kw, 1)
        result, _ = _apply_action_raw(
            body, pattern, 'replace', new_section_body,
            new_name=kwargs.get('new_name'),
            wrap_tag=kwargs.get('wrap_tag', '>'),
        )
        return result if result is not None else body

    result, _ = _apply_action_raw(
        body, pattern, operation, content_kw,
        new_name=kwargs.get('new_name'),
        wrap_tag=kwargs.get('wrap_tag', '>'),
    )
    return result if result is not None else body


def build_diff(original: str, modified: str, filename: str) -> str:
    """Zwraca unified diff jako string (bez kolorów ANSI)."""
    old_lines = original.splitlines(keepends=True)
    new_lines  = modified.splitlines(keepends=True)
    diff = difflib.unified_diff(
        old_lines, new_lines,
        fromfile=f'a/{filename}',
        tofile=f'b/{filename}',
    )
    return ''.join(diff)


def atomic_write(path: Path, content: str) -> None:
    """Zapisuje plik atomowo przez plik tymczasowy .tmp."""
    tmp = path.with_suffix('.tmp')
    tmp.write_text(content, encoding='utf-8')
    tmp.rename(path)


def log_change(
    conn,
    template_path: str,
    change_type: str,
    diff_summary: str,
    patch_args: str,
) -> None:
    """Wstawia rekord do tabeli template_changelog."""
    conn.execute(
        "INSERT INTO template_changelog "
        "(template_path, changed_at, change_type, diff_summary, patch_args) "
        "VALUES (?, datetime('now'), ?, ?, ?)",
        (template_path, change_type, diff_summary[:500], patch_args),
    )
    conn.commit()


# ---------------------------------------------------------------------------
# Narzędzia pomocnicze
# ---------------------------------------------------------------------------

def colored(text: str, color: str) -> str:
    if not sys.stdout.isatty():
        return text
    return f"{color}{text}{ANSI_RESET}"


def safe_print(*args, **kwargs) -> None:
    with _print_lock:
        print(*args, **kwargs)


def file_hash(content: str) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]


def timestamp_str() -> str:
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def similarity_ratio(old: str, new: str) -> float:
    if not old and not new:
        return 1.0
    if not old or not new:
        return 0.0
    old_lines = set(old.splitlines())
    new_lines  = set(new.splitlines())
    common = old_lines & new_lines
    total  = old_lines | new_lines
    return len(common) / len(total) if total else 1.0


def unified_diff_ansi(old: str, new: str, filename: str, context: int = 3) -> str:
    """Generuje kolorowany unified diff."""
    old_lines = old.splitlines(keepends=True)
    new_lines  = new.splitlines(keepends=True)
    diff = list(difflib.unified_diff(
        old_lines, new_lines,
        fromfile=f'przed: {filename}',
        tofile=f'po:    {filename}',
        n=context,
    ))
    if not diff:
        return ''
    output = []
    for line in diff:
        if line.startswith('+++') or line.startswith('---'):
            output.append(colored(line.rstrip(), ANSI_BOLD))
        elif line.startswith('+'):
            output.append(colored(line.rstrip(), ANSI_GREEN))
        elif line.startswith('-'):
            output.append(colored(line.rstrip(), ANSI_RED))
        elif line.startswith('@@'):
            output.append(colored(line.rstrip(), ANSI_CYAN))
        else:
            output.append(colored(line.rstrip(), ANSI_DIM))
    return '\n'.join(output)


def count_diff_lines(old: str, new: str) -> Tuple[int, int]:
    old_lines = old.splitlines(keepends=True)
    new_lines  = new.splitlines(keepends=True)
    added = removed = 0
    for line in difflib.ndiff(old_lines, new_lines):
        if line.startswith('+ '):
            added += 1
        elif line.startswith('- '):
            removed += 1
    return added, removed


def _open_db(db_path: Optional[Path]) -> Optional[sqlite3.Connection]:
    if db_path is None:
        return None
    try:
        conn = sqlite3.connect(str(db_path))
        conn.execute(
            "CREATE TABLE IF NOT EXISTS template_changelog ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "template_path TEXT, "
            "changed_at TEXT, "
            "change_type TEXT, "
            "change_reason TEXT, "
            "diff_summary TEXT, "
            "patch_args TEXT"
            ")"
        )
        conn.commit()
        return conn
    except Exception as exc:
        safe_print(colored(f'[WARN] Nie można otworzyć DB: {exc}', ANSI_YELLOW))
        return None


# ---------------------------------------------------------------------------
# Wzorzec dopasowania sekcji (wewnętrzny)
# ---------------------------------------------------------------------------

def _build_section_pattern(
    section_name: Optional[str],
    section_regex: Optional[str],
    level: Optional[int],
) -> re.Pattern:
    """
    Buduje wzorzec regex dopasowujący sekcję Markdown.
    Grupa 1: nagłówek  Grupa 2: treść sekcji
    """
    if section_regex:
        header_pattern = section_regex
    else:
        header_pattern = re.escape(section_name)

    if level:
        hashes     = '#' * level
        header_re  = rf'^({re.escape(hashes)}\s+{header_pattern}\s*\n)'
    else:
        header_re  = rf'^(#+\s+{header_pattern}\s*\n)'

    return re.compile(
        rf'(?m){header_re}(.*?)(?=\n#+\s|\Z)',
        re.DOTALL,
    )


# ---------------------------------------------------------------------------
# Akcje na sekcjach (wewnętrzne)
# ---------------------------------------------------------------------------

def _apply_action_raw(
    body: str,
    pattern: re.Pattern,
    action: str,
    new_content: str,
    new_name: Optional[str] = None,
    wrap_tag: Optional[str] = None,
    template_vars: Optional[Dict[str, str]] = None,
    content_file: Optional[str] = None,
) -> Tuple[Optional[str], Optional[str]]:
    """
    Wykonuje akcję na dopasowanej sekcji w body.
    Zwraca (nowa_treść_body, komunikat) lub (None, None) jeśli sekcja nie znaleziona.
    """
    match = pattern.search(body)
    if not match:
        return None, None

    header = match.group(1)
    sec_body = match.group(2)

    if content_file and os.path.exists(content_file):
        with open(content_file, encoding='utf-8') as f:
            new_content = f.read()

    if template_vars and JINJA_AVAILABLE and new_content:
        try:
            # autoescape=False is intentional: we render Markdown, not HTML.
            # User-supplied template_vars come from CLI args (trusted operator input).
            _jinja_env = Environment(loader=BaseLoader(), autoescape=False)  # nosec B701
            new_content = _jinja_env.from_string(new_content).render(**template_vars)
        except Exception as exc:
            safe_print(colored(f'  [WARN] Błąd szablonu Jinja2: {exc}', ANSI_YELLOW))

    if action == 'delete':
        new_text = pattern.sub('', body)
        return new_text, 'Usunięto sekcję'

    elif action == 'replace':
        resolved = new_content if new_content.endswith('\n') else new_content + '\n'
        new_text = pattern.sub(lambda m: m.group(1) + resolved, body)
        return new_text, 'Zamieniono treść sekcji'

    elif action == 'append':
        new_sec_body = sec_body.rstrip() + f'\n{new_content}\n\n'
        new_text = body[: match.start(2)] + new_sec_body + body[match.end(2):]
        return new_text, 'Dopisano na końcu sekcji'

    elif action == 'prepend':
        new_sec_body = f'{new_content}\n' + sec_body
        new_text = body[: match.start(2)] + new_sec_body + body[match.end(2):]
        return new_text, 'Dopisano na początku sekcji'

    elif action == 'wrap':
        tag = wrap_tag or '>'
        wrapped_lines = '\n'.join(
            f'{tag} {line}' if line.strip() else ''
            for line in sec_body.strip().splitlines()
        )
        new_sec_body = wrapped_lines + '\n\n'
        new_text = body[: match.start(2)] + new_sec_body + body[match.end(2):]
        return new_text, f"Owinięto sekcję w '{tag}'"

    elif action == 'rename':
        if not new_name:
            return None, None
        level_match = re.match(r'^(#+)\s+', header)
        hashes = level_match.group(1) if level_match else '#'
        new_header = f'{hashes} {new_name}\n'
        new_text = body[: match.start(1)] + new_header + sec_body + body[match.end(2):]
        return new_text, f"Zmieniono nazwę nagłówka na '{new_name}'"

    elif action == 'normalize':
        lines = sec_body.splitlines()
        normalized = []
        for line in lines:
            line = line.expandtabs(4)
            line = re.sub(r'^\s*\*\s+', '- ', line)
            line = line.rstrip()
            normalized.append(line)
        while normalized and not normalized[-1]:
            normalized.pop()
        new_sec_body = '\n'.join(normalized) + '\n\n'
        new_text = body[: match.start(2)] + new_sec_body + body[match.end(2):]
        return new_text, 'Znormalizowano formatowanie sekcji'

    elif action == 'deduplicate':
        lines = sec_body.splitlines(keepends=True)
        seen = set()
        deduped = []
        for line in lines:
            stripped = line.strip()
            if stripped not in seen:
                seen.add(stripped)
                deduped.append(line)
        new_sec_body = ''.join(deduped)
        new_text = body[: match.start(2)] + new_sec_body + body[match.end(2):]
        return new_text, 'Usunięto zduplikowane linie w sekcji'

    return None, None


def _extract_section(
    body: str,
    pattern: re.Pattern,
    source_file: Path,
    output_dir: Path,
) -> Tuple[Optional[str], Optional[str]]:
    match = pattern.search(body)
    if not match:
        return None, None
    header   = match.group(1).strip()
    sec_body = match.group(2).strip()
    safe_name = re.sub(r'[^\w\-]', '_', header.lstrip('#').strip())
    out_path  = output_dir / f'{source_file.stem}_{safe_name}.md'
    out_path.write_text(f'{header}\n\n{sec_body}\n', encoding='utf-8')
    return str(out_path), f'Wyciągnięto sekcję do {out_path}'


# ---------------------------------------------------------------------------
# Filtry plików
# ---------------------------------------------------------------------------

def _filter_by_git_date(files: List[Path], days: int, base_dir: str) -> List[Path]:
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'log', f'--since={days} days ago', '--name-only',
             '--pretty=format:', '--diff-filter=AM'],
            capture_output=True, text=True, cwd=base_dir,
        )
        changed = set(result.stdout.strip().splitlines())
        return [f for f in files if str(f.relative_to(base_dir)) in changed or f.name in changed]
    except Exception:
        safe_print(colored('[WARN] Nie można filtrować przez Git.', ANSI_YELLOW))
        return files


def _filter_by_contains(files: List[Path], substring: str) -> List[Path]:
    result = []
    for f in files:
        try:
            if substring in f.read_text(encoding='utf-8', errors='replace'):
                result.append(f)
        except Exception:
            pass
    return result


def _filter_by_section_empty(files: List[Path], pattern: re.Pattern) -> List[Path]:
    result = []
    for f in files:
        try:
            _, body = strip_frontmatter(f.read_text(encoding='utf-8', errors='replace'))
            match = pattern.search(body)
            if match and not match.group(2).strip():
                result.append(f)
        except Exception:
            pass
    return result


def _filter_by_section_missing(files: List[Path], pattern: re.Pattern) -> List[Path]:
    result = []
    for f in files:
        try:
            _, body = strip_frontmatter(f.read_text(encoding='utf-8', errors='replace'))
            if not pattern.search(body):
                result.append(f)
        except Exception:
            pass
    return result


def _filter_by_section_length(
    files: List[Path],
    pattern: re.Pattern,
    min_length: Optional[int],
    max_length: Optional[int],
) -> List[Path]:
    result = []
    for f in files:
        try:
            _, body = strip_frontmatter(f.read_text(encoding='utf-8', errors='replace'))
            match = pattern.search(body)
            if not match:
                continue
            length = len(match.group(2).strip())
            if min_length is not None and length < min_length:
                result.append(f)
            elif max_length is not None and length > max_length:
                result.append(f)
            elif min_length is None and max_length is None:
                result.append(f)
        except Exception:
            pass
    return result


def _filter_by_if_section(
    files: List[Path],
    condition_section: str,
    condition_contains: str,
) -> List[Path]:
    cond_pattern = _build_section_pattern(condition_section, None, None)
    result = []
    for f in files:
        try:
            _, body = strip_frontmatter(f.read_text(encoding='utf-8', errors='replace'))
            match = cond_pattern.search(body)
            if match and condition_contains in match.group(2):
                result.append(f)
        except Exception:
            pass
    return result


# ---------------------------------------------------------------------------
# Audit trail
# ---------------------------------------------------------------------------

def _write_audit_record(
    audit_path: str,
    filepath: str,
    section: str,
    action: str,
    hash_before: str,
    hash_after: str,
    lines_added: int,
    lines_removed: int,
    dry_run: bool,
    session_id: str,
) -> None:
    record = {
        'timestamp':     datetime.now().isoformat(),
        'session_id':    session_id,
        'file':          str(filepath),
        'section':       section,
        'action':        action,
        'hash_before':   hash_before,
        'hash_after':    hash_after,
        'lines_added':   lines_added,
        'lines_removed': lines_removed,
        'dry_run':       dry_run,
    }
    with _print_lock:
        with open(audit_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')


def undo_session(audit_path: str, session_id: str) -> None:
    if not os.path.exists(audit_path):
        safe_print(colored(f'[BŁĄD] Brak pliku audytu: {audit_path}', ANSI_RED))
        return
    records = []
    with open(audit_path, encoding='utf-8') as f:
        for line in f:
            try:
                rec = json.loads(line.strip())
                if rec.get('session_id') == session_id and not rec.get('dry_run'):
                    records.append(rec)
            except json.JSONDecodeError:
                pass
    if not records:
        safe_print(colored(f"[WARN] Brak zapisanych operacji dla sesji '{session_id}'.", ANSI_YELLOW))
        return
    restored = 0
    for rec in records:
        filepath = rec['file']
        bak_candidates = sorted(
            Path(filepath).parent.glob(f"{Path(filepath).name}.bak_*"),
            reverse=True,
        )
        if bak_candidates:
            shutil.copy2(bak_candidates[0], filepath)
            restored += 1
            safe_print(f'  [OK] Przywrócono: {filepath} <- {bak_candidates[0].name}')
        else:
            safe_print(colored(f'  [WARN] Brak kopii dla: {filepath}', ANSI_YELLOW))
    safe_print(f'\n[PODSUMOWANIE] Przywrócono {restored}/{len(records)} plików.')


# ---------------------------------------------------------------------------
# Snapshot katalogu
# ---------------------------------------------------------------------------

def _snapshot_directory(directory: str, pattern: str) -> str:
    base     = Path(directory)
    zip_name = f'snapshot_{base.name}_{timestamp_str()}.zip'
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in base.rglob(pattern):
            zf.write(f, f.relative_to(base.parent))
    return zip_name


# ---------------------------------------------------------------------------
# Przetwarzanie pojedynczego pliku
# ---------------------------------------------------------------------------

def process_file(
    md_file: Path,
    pattern: re.Pattern,
    action: str,
    new_content: str,
    new_name: Optional[str],
    wrap_tag: Optional[str],
    template_vars: Optional[Dict[str, str]],
    content_file: Optional[str],
    dry_run: bool,
    backup: bool,
    interactive: bool,
    show_diff: bool,
    extract_dir: Optional[Path],
    session_id: str,
    audit_log: Optional[str],
    section_name: str,
    db_conn=None,
    patch_args: str = '',
) -> Dict[str, Any]:
    result = {
        'file':          str(md_file),
        'status':        'skipped',
        'message':       '',
        'lines_added':   0,
        'lines_removed': 0,
        'similarity':    1.0,
    }

    try:
        full_content = md_file.read_text(encoding='utf-8', errors='replace')
    except Exception as exc:
        result['status']  = 'error'
        result['message'] = str(exc)
        return result

    frontmatter, body = strip_frontmatter(full_content)

    if action == 'extract' and extract_dir:
        out_path, msg = _extract_section(body, pattern, md_file, extract_dir)
        if out_path:
            result['status']  = 'modified'
            result['message'] = msg or ''
        return result

    new_body, msg = _apply_action_raw(
        body, pattern, action, new_content,
        new_name=new_name,
        wrap_tag=wrap_tag,
        template_vars=template_vars,
        content_file=content_file,
    )

    if new_body is None:
        result['status'] = 'no_match'
        return result

    new_full = frontmatter + new_body

    if full_content == new_full:
        result['status'] = 'unchanged'
        return result

    lines_added, lines_removed = count_diff_lines(full_content, new_full)
    sim = similarity_ratio(full_content, new_full)
    result['lines_added']   = lines_added
    result['lines_removed'] = lines_removed
    result['similarity']    = sim

    if show_diff:
        diff_output = unified_diff_ansi(full_content, new_full, md_file.name)
        if diff_output:
            safe_print(f'\n{diff_output}')

    if sim < 0.3:
        safe_print(colored(
            f'  [WARN] Duża zmiana w {md_file.name} (podobieństwo: {sim:.0%}).',
            ANSI_YELLOW,
        ))

    if interactive and not dry_run:
        ans = input(colored(
            f'  [ZAPYTANIE] Zmodyfikować {md_file.name}? [T/n]: ', ANSI_BOLD,
        )).strip().lower()
        if ans == 'n':
            result['status']  = 'skipped'
            result['message'] = 'Pominięto przez użytkownika'
            return result

    existing_baks = sorted(md_file.parent.glob(f'{md_file.name}.bak_*'), reverse=True)
    if existing_baks and not dry_run:
        bak_mtime  = existing_baks[0].stat().st_mtime
        file_mtime = md_file.stat().st_mtime
        if file_mtime > bak_mtime + 5:
            safe_print(colored(
                f'  [WARN] Plik {md_file.name} był modyfikowany ręcznie od ostatniego backupu.',
                ANSI_YELLOW,
            ))

    hash_before = file_hash(full_content)
    hash_after  = file_hash(new_full)

    if not dry_run:
        if backup:
            bak_path = f'{md_file}.bak_{timestamp_str()}'
            shutil.copy2(md_file, bak_path)
        atomic_write(md_file, new_full)

        if db_conn is not None:
            diff_summary = build_diff(full_content, new_full, md_file.name)
            try:
                log_change(db_conn, str(md_file), action, diff_summary, patch_args)
            except Exception as exc:
                safe_print(colored(f'  [WARN] Błąd zapisu do DB: {exc}', ANSI_YELLOW))

    if audit_log:
        _write_audit_record(
            audit_log, str(md_file), section_name, action,
            hash_before, hash_after,
            lines_added, lines_removed,
            dry_run, session_id,
        )

    result['status']  = 'modified'
    result['message'] = msg or ''
    return result


# ---------------------------------------------------------------------------
# Główna funkcja patch_section
# ---------------------------------------------------------------------------

def patch_section(
    directory: str,
    section_name: Optional[str],
    section_regex: Optional[str],
    new_content: str,
    action: str = 'replace',
    file_pattern: str = '*.md',
    dry_run: bool = True,
    backup: bool = False,
    interactive: bool = False,
    show_diff: bool = False,
    level: Optional[int] = None,
    new_name: Optional[str] = None,
    wrap_tag: Optional[str] = None,
    template_vars: Optional[Dict[str, str]] = None,
    content_file: Optional[str] = None,
    only_if_empty: bool = False,
    only_if_missing: bool = False,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    changed_since_days: Optional[int] = None,
    only_if_contains: Optional[str] = None,
    if_section: Optional[str] = None,
    if_section_contains: Optional[str] = None,
    extract_dir: Optional[str] = None,
    audit_log: Optional[str] = AUDIT_LOG_FILE,
    session_id: Optional[str] = None,
    snapshot: bool = False,
    workers: int = 4,
    simulate_jsonl: Optional[str] = None,
    db_path: Optional[Path] = None,
) -> Dict[str, Any]:

    base_path = Path(directory)
    if not base_path.exists():
        safe_print(colored(f'[BŁĄD] Katalog {directory} nie istnieje.', ANSI_RED))
        return {}

    if not session_id:
        session_id = timestamp_str()

    pattern      = _build_section_pattern(section_name, section_regex, level)
    display_name = section_name or section_regex or '(regex)'
    patch_args_str = json.dumps({
        'section': display_name, 'action': action, 'dry_run': dry_run,
    }, ensure_ascii=False)

    if snapshot and not dry_run:
        zip_path = _snapshot_directory(directory, file_pattern)
        safe_print(colored(f'[INFO] Snapshot katalogu: {zip_path}', ANSI_DIM))

    all_files = list(base_path.rglob(file_pattern))
    safe_print(f"[INFO] Znaleziono {len(all_files)} plików pasujących do '{file_pattern}'...")

    if changed_since_days:
        all_files = _filter_by_git_date(all_files, changed_since_days, directory)
        safe_print(f'[INFO] Po filtrze git ({changed_since_days}d): {len(all_files)} plików')
    if only_if_contains:
        all_files = _filter_by_contains(all_files, only_if_contains)
        safe_print(f'[INFO] Po filtrze contains: {len(all_files)} plików')
    if only_if_empty:
        all_files = _filter_by_section_empty(all_files, pattern)
        safe_print(f'[INFO] Po filtrze section_empty: {len(all_files)} plików')
    if only_if_missing:
        all_files = _filter_by_section_missing(all_files, pattern)
        safe_print(f'[INFO] Po filtrze section_missing: {len(all_files)} plików')
    if min_length is not None or max_length is not None:
        all_files = _filter_by_section_length(all_files, pattern, min_length, max_length)
        safe_print(f'[INFO] Po filtrze długości: {len(all_files)} plików')
    if if_section and if_section_contains:
        all_files = _filter_by_if_section(all_files, if_section, if_section_contains)
        safe_print(f'[INFO] Po filtrze if_section: {len(all_files)} plików')

    if not all_files:
        safe_print('[INFO] Brak plików do przetworzenia po zastosowaniu filtrów.')
        return {}

    extract_path: Optional[Path] = None
    if action == 'extract' and extract_dir:
        extract_path = Path(extract_dir)
        extract_path.mkdir(parents=True, exist_ok=True)

    if simulate_jsonl:
        ops = []
        for f in all_files:
            try:
                _, body = strip_frontmatter(f.read_text(encoding='utf-8', errors='replace'))
                match = pattern.search(body)
                if match:
                    ops.append({
                        'file': str(f), 'section': display_name, 'action': action,
                        'body_preview': match.group(2)[:100].strip(),
                    })
            except Exception:
                pass
        with open(simulate_jsonl, 'w', encoding='utf-8') as jf:
            for op in ops:
                jf.write(json.dumps(op, ensure_ascii=False) + '\n')
        safe_print(colored(f'[OK] Symulacja zapisana do: {simulate_jsonl} ({len(ops)} operacji)', ANSI_GREEN))
        return {}

    db_conn = _open_db(db_path)

    file_kwargs = dict(
        pattern=pattern,
        action=action,
        new_content=new_content,
        new_name=new_name,
        wrap_tag=wrap_tag,
        template_vars=template_vars,
        content_file=content_file,
        dry_run=dry_run,
        backup=backup,
        interactive=interactive,
        show_diff=show_diff,
        extract_dir=extract_path,
        session_id=session_id,
        audit_log=audit_log,
        section_name=display_name,
        db_conn=db_conn,
        patch_args=patch_args_str,
    )

    results: List[Dict[str, Any]] = []
    stats: Dict[str, int] = defaultdict(int)
    errors: List[Tuple[Path, str]] = []

    if workers > 1 and not interactive:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(process_file, f, **file_kwargs): f for f in all_files}
            for future in as_completed(futures):
                try:
                    res = future.result()
                    results.append(res)
                    stats[res['status']] += 1
                    _print_result(res, dry_run, backup)
                except Exception as exc:
                    errors.append((futures[future], str(exc)))
                    safe_print(colored(f'  [BŁĄD wątku] {futures[future]}: {exc}', ANSI_RED))
    else:
        for f in all_files:
            res = process_file(f, **file_kwargs)
            results.append(res)
            stats[res['status']] += 1
            _print_result(res, dry_run, backup)

    if db_conn is not None:
        db_conn.close()

    total_added   = sum(r['lines_added'] for r in results)
    total_removed = sum(r['lines_removed'] for r in results)

    safe_print(f"\n{'=' * 60}")
    safe_print(colored('PODSUMOWANIE', ANSI_BOLD))
    safe_print(f"{'=' * 60}")
    safe_print(f"  Plików przetworzonych:  {len(all_files)}")
    safe_print(f"  Zmodyfikowanych:        {colored(str(stats['modified']), ANSI_GREEN)}")
    safe_print(f"  Brak dopasowania:       {stats['no_match']}")
    safe_print(f"  Bez zmian:              {stats['unchanged']}")
    safe_print(f"  Pominięto:              {stats['skipped']}")
    safe_print(f"  Błędy:                  {colored(str(stats['error'] + len(errors)), ANSI_RED) if (stats['error'] + len(errors)) else '0'}")
    safe_print(f'  Linie dodane:           +{total_added}')
    safe_print(f'  Linie usunięte:         -{total_removed}')
    if dry_run:
        safe_print(colored('  [DRY-RUN] Zmiany NIE zostały zapisane.', ANSI_YELLOW))
    safe_print(f'  Sesja ID:               {session_id}')
    safe_print(f"{'=' * 60}")

    return {
        'session_id':    session_id,
        'stats':         dict(stats),
        'total_added':   total_added,
        'total_removed': total_removed,
        'results':       results,
        'errors':        [(str(f), e) for f, e in errors],
    }


def _print_result(res: Dict[str, Any], dry_run: bool, backup: bool) -> None:
    status = res['status']
    if status == 'modified':
        mode      = 'DRY-RUN' if dry_run else ('ZAPISANO' + ('+BAK' if backup else ''))
        diff_info = f"+{res['lines_added']}/-{res['lines_removed']}"
        safe_print(
            f"  [{colored(mode, ANSI_GREEN if not dry_run else ANSI_YELLOW)}] "
            f"{res['message']} | {Path(res['file']).name} ({diff_info})"
        )
    elif status == 'error':
        safe_print(colored(f"  [BŁĄD] {res['file']}: {res['message']}", ANSI_RED))


# ---------------------------------------------------------------------------
# Raport macierzy sekcji
# ---------------------------------------------------------------------------

def report_matrix(
    directory: str,
    file_pattern: str = '*.md',
    output_csv: Optional[str] = None,
) -> None:
    base_path     = Path(directory)
    all_sections: Dict[str, set] = defaultdict(set)
    file_sections: Dict[str, set] = {}
    header_re     = re.compile(r'^#+\s+(.+)', re.MULTILINE)
    files         = list(base_path.rglob(file_pattern))

    for f in files:
        try:
            _, body = strip_frontmatter(f.read_text(encoding='utf-8', errors='replace'))
            sections = set(m.group(1).strip() for m in header_re.finditer(body))
            file_sections[str(f)] = sections
            for s in sections:
                all_sections[s].add(str(f))
        except Exception:
            pass

    all_headers = sorted(all_sections.keys())
    safe_print(f'\n[MACIERZ SEKCJI] {len(files)} plików, {len(all_headers)} unikalnych sekcji\n')

    common = [(h, len(v)) for h, v in all_sections.items() if len(v) > 1]
    common.sort(key=lambda x: -x[1])
    safe_print(colored('Top 20 najczęstszych sekcji:', ANSI_BOLD))
    for header, count in common[:20]:
        pct = count / len(files) * 100 if files else 0
        bar = '#' * min(int(pct / 2), 40)
        safe_print(f'  {count:4d}/{len(files)} ({pct:5.1f}%)  {bar:<40}  {header}')

    safe_print(colored('\nSekcje obecne w < 50% plików (luki):', ANSI_BOLD))
    gaps = [(h, len(v)) for h, v in all_sections.items() if len(v) / max(len(files), 1) < 0.5]
    gaps.sort(key=lambda x: x[1])
    for header, count in gaps[:10]:
        safe_print(f'  {header}: {count}/{len(files)} plików ma tę sekcję')

    safe_print(colored('\nNiespójne poziomy nagłówków (ta sama nazwa, różny poziom):', ANSI_BOLD))
    level_re = re.compile(r'^(#+)\s+(.+)', re.MULTILINE)
    level_map: Dict[str, set] = defaultdict(set)
    for f in files:
        try:
            _, body = strip_frontmatter(Path(f).read_text(encoding='utf-8', errors='replace'))
            for m in level_re.finditer(body):
                level_map[m.group(2).strip()].add(len(m.group(1)))
        except Exception:
            pass
    inconsistent = [(name, levels) for name, levels in level_map.items() if len(levels) > 1]
    if inconsistent:
        for name, levels in inconsistent[:10]:
            safe_print(f"  '{name}': poziomy {sorted(levels)}")
    else:
        safe_print('  Brak niespójności.')

    if output_csv:
        with open(output_csv, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)
            writer.writerow(['Plik'] + all_headers)
            for filepath, sections in sorted(file_sections.items()):
                row = [filepath] + ['1' if h in sections else '' for h in all_headers]
                writer.writerow(row)
        safe_print(colored(f'\n[OK] Macierz CSV zapisana do: {output_csv}', ANSI_GREEN))


# ---------------------------------------------------------------------------
# Tryb wsadowy z YAML
# ---------------------------------------------------------------------------

def run_batch(batch_file: str, global_dry_run: bool, db_path: Optional[Path] = None) -> None:
    if not YAML_AVAILABLE:
        safe_print(colored('[BŁĄD] Wymagany PyYAML: pip install pyyaml', ANSI_RED))
        return
    if not os.path.exists(batch_file):
        safe_print(colored(f'[BŁĄD] Brak pliku batch: {batch_file}', ANSI_RED))
        return

    with open(batch_file, encoding='utf-8') as f:
        batch = yaml.safe_load(f)

    global_vars = batch.get('variables', {})
    now_str = datetime.now().strftime('%Y-%m-%d')
    global_vars.setdefault('date', now_str)
    global_vars.setdefault('version', '1.0')

    operations = batch.get('operations', [])
    if not operations:
        safe_print('[WARN] Brak operacji w pliku batch.')
        return

    safe_print(f"[INFO] Batch: {len(operations)} operacji z '{batch_file}'")
    session_id    = timestamp_str()
    prev_modified = -1

    for i, op in enumerate(operations, 1):
        safe_print(f"\n{'=' * 60}")
        safe_print(colored(
            f"OPERACJA {i}/{len(operations)}: {op.get('action', 'replace')} / {op.get('section', '')}",
            ANSI_BOLD,
        ))
        safe_print(f"{'=' * 60}")

        stop_if_zero = op.get('stop_if_no_changes', False)
        if stop_if_zero and prev_modified == 0:
            safe_print(colored('[INFO] Poprzedni krok zmienił 0 plików. Zatrzymanie pipeline.', ANSI_YELLOW))
            break

        op_vars = {**global_vars, **op.get('variables', {})}
        content = op.get('content', '')
        if op_vars and content:
            for k, v in op_vars.items():
                content = content.replace('{{ ' + k + ' }}', str(v))

        op_dir = op.get('dir', str(DEFAULT_TEMPLATES_DIR))
        result = patch_section(
            directory=op_dir,
            section_name=op.get('section'),
            section_regex=op.get('section_regex'),
            new_content=content,
            action=op.get('action', 'replace'),
            file_pattern=op.get('pattern', '*.md'),
            dry_run=global_dry_run or op.get('dry_run', False),
            backup=op.get('backup', False),
            interactive=False,
            show_diff=op.get('show_diff', False),
            level=op.get('level'),
            new_name=op.get('new_name'),
            wrap_tag=op.get('wrap_tag'),
            template_vars=op_vars,
            content_file=op.get('content_file'),
            only_if_empty=op.get('only_if_empty', False),
            only_if_missing=op.get('only_if_missing', False),
            min_length=op.get('min_length'),
            max_length=op.get('max_length'),
            changed_since_days=op.get('changed_since_days'),
            only_if_contains=op.get('only_if_contains'),
            if_section=op.get('if_section'),
            if_section_contains=op.get('if_section_contains'),
            audit_log=op.get('audit_log', AUDIT_LOG_FILE),
            session_id=session_id,
            snapshot=op.get('snapshot', False),
            workers=op.get('workers', 4),
            db_path=db_path,
        )
        prev_modified = result.get('stats', {}).get('modified', 0) if result else 0

    safe_print(colored(f"\n[OK] Batch '{batch_file}' zakończony. Sesja: {session_id}", ANSI_GREEN))


# ---------------------------------------------------------------------------
# Eksport wyniku jako JSON
# ---------------------------------------------------------------------------

def output_json(result: Dict[str, Any]) -> None:
    safe_results = {
        'session_id':     result.get('session_id'),
        'stats':          result.get('stats'),
        'total_added':    result.get('total_added'),
        'total_removed':  result.get('total_removed'),
        'files_modified': [
            r['file'] for r in result.get('results', []) if r['status'] == 'modified'
        ],
        'errors': result.get('errors', []),
    }
    print(json.dumps(safe_results, ensure_ascii=False, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Masowa edycja sekcji w plikach Markdown.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('--dir', default=str(DEFAULT_TEMPLATES_DIR),
                        help='Katalog z szablonami')
    parser.add_argument('--db', default=str(DEFAULT_DB_PATH),
                        help='Ścieżka do bazy SQLite (template_changelog)')
    parser.add_argument('--pattern', default='*.md',
                        help='Wzorzec plików (glob)')
    parser.add_argument('--section',
                        help='Dokładna nazwa nagłówka sekcji')
    parser.add_argument('--section-regex',
                        help='Regex dla nazwy nagłówka (zamiast --section)')
    parser.add_argument('--operation', '--action', dest='operation',
                        choices=VALID_OPERATIONS, default='replace',
                        help='Operacja na sekcji')
    parser.add_argument('--content', default='',
                        help='Nowa treść sekcji (całkowita podmiana lub append/prepend)')
    parser.add_argument('--old',
                        help='Tekst do znalezienia wewnątrz sekcji (dla --operation replace)')
    parser.add_argument('--new', dest='new_text', default='',
                        help='Tekst zastępujący (dla --operation replace z --old)')
    parser.add_argument('--content-file',
                        help='Plik z nową treścią sekcji (zamiast --content)')
    parser.add_argument('--new-name',
                        help='Nowa nazwa nagłówka (dla --operation rename)')
    parser.add_argument('--wrap-tag', default='>',
                        help='Prefix owijania (dla --operation wrap)')
    parser.add_argument('--level', type=int,
                        help='Poziom nagłówka (1=# 2=## 3=### itd.)')
    parser.add_argument('--dry-run', action='store_true', default=False,
                        help='Tylko podgląd — nie zapisuje zmian (domyślnie: True jeśli brak --apply)')
    parser.add_argument('--apply', action='store_true',
                        help='Zapisz zmiany (bez tego flagi: dry-run)')
    parser.add_argument('--backup', action='store_true',
                        help='Twórz wersjonowane kopie .bak_TIMESTAMP')
    parser.add_argument('--interactive', action='store_true',
                        help='Pytaj przed każdą zmianą')
    parser.add_argument('--diff', action='store_true',
                        help='Pokazuj kolorowany diff przed zapisem')
    parser.add_argument('--snapshot', action='store_true',
                        help='Archiwum ZIP katalogu przed operacją')
    parser.add_argument('--workers', type=int, default=4,
                        help='Liczba równoległych wątków')
    parser.add_argument('--only-if-empty', action='store_true',
                        help='Tylko pliki gdzie sekcja jest pusta')
    parser.add_argument('--only-if-missing', action='store_true',
                        help='Tylko pliki bez tej sekcji')
    parser.add_argument('--min-length', type=int,
                        help='Filtruj sekcje krótsze niż N znaków')
    parser.add_argument('--max-length', type=int,
                        help='Filtruj sekcje dłuższe niż N znaków')
    parser.add_argument('--changed-since', type=int, dest='changed_since_days',
                        help='Tylko pliki zmienione przez Git w ostatnich N dniach')
    parser.add_argument('--only-if-contains',
                        help='Tylko pliki zawierające podany tekst (gdziekolwiek)')
    parser.add_argument('--if-section',
                        help='Filtr warunkowy: nazwa sekcji warunku')
    parser.add_argument('--if-section-contains',
                        help='Filtr warunkowy: sekcja musi zawierać ten tekst')
    parser.add_argument('--extract-dir',
                        help='Katalog docelowy dla --operation extract')
    parser.add_argument('--template-vars', nargs='*', metavar='KLUCZ=WARTOSC',
                        help='Zmienne dla szablonu Jinja2 (np. version=1.2 date=2025-01-01)')
    parser.add_argument('--audit-log', default=AUDIT_LOG_FILE,
                        help='Plik JSONL z historią operacji')
    parser.add_argument('--simulate-jsonl',
                        help='Zapisz symulację operacji do JSONL bez wykonywania')
    parser.add_argument('--batch',
                        help='Plik YAML z listą operacji wsadowych')
    parser.add_argument('--undo-session',
                        help='ID sesji do cofnięcia (z patch_audit.jsonl)')
    parser.add_argument('--report-matrix', action='store_true',
                        help='Raport macierzy sekcji w katalogu')
    parser.add_argument('--matrix-csv',
                        help='Eksport macierzy sekcji do CSV')
    parser.add_argument('--json-output', action='store_true',
                        help='Wynik operacji jako JSON (dla agentów)')
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    return parser


def main() -> None:
    parser = build_parser()
    args   = parser.parse_args()

    db_path: Optional[Path] = None
    if args.db and Path(args.db).parent.exists():
        db_path = Path(args.db)

    if args.undo_session:
        undo_session(args.audit_log, args.undo_session)
        return

    if args.report_matrix:
        report_matrix(args.dir, args.pattern, args.matrix_csv)
        return

    if args.batch:
        run_batch(args.batch, global_dry_run=not args.apply, db_path=db_path)
        return

    if not args.section and not args.section_regex:
        parser.error(
            'Wymagane --section lub --section-regex '
            '(chyba że używasz --batch lub --report-matrix).'
        )

    operation = args.operation

    # Ustal treść nową
    if args.old:
        # Podmiana podłańcucha — --content ignorowane
        if operation not in ('replace',):
            parser.error('--old/--new wymaga --operation replace.')
        new_content = ''   # nie używane bezpośrednio — obsługiwane przez --old/--new
    else:
        new_content = args.content

    if operation in ('replace', 'append', 'prepend') and not args.old and not new_content and not args.content_file:
        parser.error(f"--content lub --content-file jest wymagane dla --operation '{operation}'.")

    if operation == 'rename' and not args.new_name:
        parser.error('--new-name jest wymagane dla --operation rename.')

    if operation == 'extract' and not args.extract_dir:
        parser.error('--extract-dir jest wymagane dla --operation extract.')

    template_vars: Optional[Dict[str, str]] = None
    if args.template_vars:
        template_vars = {}
        for item in args.template_vars:
            if '=' in item:
                k, v = item.split('=', 1)
                template_vars[k.strip()] = v.strip()

    dry_run = not args.apply

    # Obsługa --old/--new przez apply_operation zamiast patch_section bezpośrednio
    if args.old:
        # Przetwarzamy pliki po jednym przez apply_operation
        base_path = Path(args.dir)
        all_files = list(base_path.rglob(args.pattern))
        db_conn   = _open_db(db_path)
        modified  = 0
        for md_file in all_files:
            try:
                full = md_file.read_text(encoding='utf-8', errors='replace')
                fm, body = strip_frontmatter(full)
                new_body = apply_operation(
                    body, args.section, operation,
                    old=args.old, new=args.new_text,
                )
                if new_body == body:
                    continue
                new_full = fm + new_body
                if args.diff:
                    diff_out = unified_diff_ansi(full, new_full, md_file.name)
                    if diff_out:
                        safe_print(f'\n{diff_out}')
                if not dry_run:
                    if args.backup:
                        shutil.copy2(md_file, f'{md_file}.bak_{timestamp_str()}')
                    atomic_write(md_file, new_full)
                    if db_conn is not None:
                        diff_summary = build_diff(full, new_full, md_file.name)
                        patch_args_s = json.dumps({
                            'section': args.section, 'old': args.old, 'new': args.new_text,
                        }, ensure_ascii=False)
                        try:
                            log_change(db_conn, str(md_file), operation, diff_summary, patch_args_s)
                        except Exception as exc:
                            safe_print(colored(f'  [WARN] Błąd zapisu do DB: {exc}', ANSI_YELLOW))
                mode = 'DRY-RUN' if dry_run else 'ZAPISANO'
                safe_print(f'  [{colored(mode, ANSI_YELLOW if dry_run else ANSI_GREEN)}] {md_file.name}')
                modified += 1
            except Exception as exc:
                safe_print(colored(f'  [BŁĄD] {md_file}: {exc}', ANSI_RED))
        if db_conn is not None:
            db_conn.close()
        safe_print(f'\n[OK] Zmodyfikowano {modified}/{len(all_files)} plików.')
        return

    result = patch_section(
        directory=args.dir,
        section_name=args.section,
        section_regex=args.section_regex,
        new_content=new_content,
        action=operation,
        file_pattern=args.pattern,
        dry_run=dry_run,
        backup=args.backup,
        interactive=args.interactive,
        show_diff=args.diff,
        level=args.level,
        new_name=args.new_name,
        wrap_tag=args.wrap_tag,
        template_vars=template_vars,
        content_file=args.content_file,
        only_if_empty=args.only_if_empty,
        only_if_missing=args.only_if_missing,
        min_length=args.min_length,
        max_length=args.max_length,
        changed_since_days=args.changed_since_days,
        only_if_contains=args.only_if_contains,
        if_section=args.if_section,
        if_section_contains=args.if_section_contains,
        extract_dir=args.extract_dir,
        audit_log=args.audit_log,
        simulate_jsonl=args.simulate_jsonl,
        snapshot=args.snapshot,
        workers=args.workers,
        db_path=db_path,
    )

    if args.json_output and result:
        output_json(result)


if __name__ == '__main__':
    main()
