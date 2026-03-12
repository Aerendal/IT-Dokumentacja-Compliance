# 08 — Brief Parser Spec

**Status:** Draft v1.0  
**Powiązane dokumenty:** 03_architecture_overview, 05_module_interface_contracts, 07_llm_adapter_spec

---

## 1. Cel i zakres

Brief Parser przekształca surowy plik briefu klienta (dowolnego formatu) w znormalizowany, czysty tekst UTF-8 gotowy do dalszego przetwarzania przez LLM Adapter. Parser jest niezależny od LLM — jego wyjście to deterministyczny, powtarzalny tekst.

**Obsługiwane formaty:**
| Format | Wykrywanie | Biblioteka |
|--------|-----------|-----------|
| `.txt` | MIME `text/plain` lub rozszerzenie | native Python |
| `.md` | MIME `text/markdown` lub rozszerzenie | native Python |
| `.pdf` | MIME `application/pdf` | `pdfplumber` |
| `.docx` | MIME `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | `python-docx` |
| inne | → `"unknown"` | — |

---

## 2. Interfejs

```python
# workshop/api/services/brief_parser.py

from dataclasses import dataclass, field


@dataclass
class ParsedBrief:
    text:       str               # znormalizowany tekst UTF-8, stripped
    metadata:   dict              # {author, pages, word_count, detected_language, ...}
    chunks:     list[str]         # tekst podzielony na chunki ≤ CHUNK_MAX_CHARS
    format:     str               # "txt" | "md" | "pdf" | "docx"
    char_count: int = 0
    word_count: int = 0

    def __post_init__(self):
        self.char_count = len(self.text)
        self.word_count = len(self.text.split())


class BriefParser:

    CHUNK_MAX_CHARS: int = 12_000           # domyślny (OpenAI gpt-4: 128k ctx)
    CHUNK_MAX_CHARS_OLLAMA: int = 7_000     # Ollama llama3.2 default ctx: 4096 tokenów
    # ~7000 znaków PL ≈ ~2500 tokenów + ~300 tokenów prompt = ~2800 (bezpieczny margines)
    MAX_FILE_SIZE   = 50 * 1024 * 1024  # 50 MB

    def detect_format(self, filename: str, content: bytes) -> str:
        """
        Wykrywa format na podstawie MIME (python-magic) + rozszerzenia.
        MIME ma priorytet nad rozszerzeniem.
        
        Returns: "txt" | "md" | "pdf" | "docx" | "unknown"
        """

    def _get_chunk_size(self, provider: str) -> int:
        """Dobierz chunk size per LLM provider."""
        if provider == "ollama":
            return self.CHUNK_MAX_CHARS_OLLAMA
        return self.CHUNK_MAX_CHARS

    def parse(self, content: bytes, format: str, filename: str = "") -> ParsedBrief:
        """
        Parsuje plik do ParsedBrief.
        
        Raises:
          ParseError            — plik uszkodzony, zaszyfrowany, brak treści
          UnsupportedFormatError— format = "unknown"
          FileTooLargeError     — len(content) > MAX_FILE_SIZE
        """
```

---

## 3. Pipeline parsowania

### Etap 1: Wykrywanie formatu

```python
def detect_format(self, filename: str, content: bytes) -> str:
    # 1. Próba MIME detection (magic bytes)
    mime = magic.from_buffer(content, mime=True)
    
    mime_map = {
        "text/plain":       "txt",
        "text/markdown":    "md",
        "application/pdf":  "pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
    }
    
    if mime in mime_map:
        detected = mime_map[mime]
        # Jeśli MD → sprawdź czy rozszerzenie to .md (MIME dla MD bywa text/plain)
        ext = Path(filename).suffix.lower()
        if detected == "txt" and ext == ".md":
            return "md"
        return detected
    
    # 2. Fallback: rozszerzenie
    ext_map = {".txt": "txt", ".md": "md", ".pdf": "pdf", ".docx": "docx"}
    return ext_map.get(Path(filename).suffix.lower(), "unknown")
```

### Etap 2: Ekstrakcja tekstu (per format)

#### TXT / MD
```python
def _parse_text(self, content: bytes) -> tuple[str, dict]:
    # Próbuj UTF-8, fallback UTF-8-sig, fallback latin-1
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            text = content.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    
    metadata = {
        "encoding": encoding,
        "detected_language": self._detect_language(text),
    }
    return text, metadata
```

#### PDF
```python
def _parse_pdf(self, content: bytes) -> tuple[str, dict]:
    pages_text = []
    with pdfplumber.open(BytesIO(content)) as pdf:
        metadata = {
            "pages": len(pdf.pages),
            "author": pdf.metadata.get("Author"),
            "title":  pdf.metadata.get("Title"),
        }
        for page in pdf.pages:
            page_text = page.extract_text(x_tolerance=3, y_tolerance=3)
            if page_text:
                pages_text.append(page_text)
    
    # Sprawdź czy PDF nie jest zaszyfrowany lub skanem bez OCR
    if not pages_text:
        raise ParseError(
            "Nie udało się wyekstrahować tekstu z PDF. "
            "PDF może być zaszyfrowany lub zawierać wyłącznie skany (brak OCR)."
        )
    
    return "\n\n".join(pages_text), metadata
```

#### DOCX
```python
def _parse_docx(self, content: bytes) -> tuple[str, dict]:
    doc = Document(BytesIO(content))
    
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    
    # Wyciągnij też tabele
    table_texts = []
    for table in doc.tables:
        for row in table.rows:
            row_text = " | ".join(cell.text.strip() for cell in row.cells if cell.text.strip())
            if row_text:
                table_texts.append(row_text)
    
    all_text = "\n\n".join(paragraphs)
    if table_texts:
        all_text += "\n\n## Tabele\n" + "\n".join(table_texts)
    
    metadata = {
        "author":       doc.core_properties.author,
        "title":        doc.core_properties.title,
        "paragraph_count": len(paragraphs),
    }
    
    return all_text, metadata
```

### Etap 3: Normalizacja tekstu

```python
def _normalize(self, text: str) -> str:
    """
    Normalizacja tekstu do czystego UTF-8:
    1. Usuń null bytes i znaki kontrolne (poza \n, \t)
    2. Normalizuj Unicode do NFC
    3. Napraw mojibake (heurystyka dla polskich znaków)
    4. Złap nadmiarowe whitespace (>2 newlines → 2 newlines)
    5. Strip całego tekstu
    """
    import unicodedata
    
    # Usuń null bytes
    text = text.replace('\x00', '')
    
    # Usuń znaki kontrolne (zachowaj \n \t \r)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Cc' or c in '\n\t\r')
    
    # NFC normalization (polskie znaki: ą→ą, ę→ę)
    text = unicodedata.normalize('NFC', text)
    
    # Napraw typowy mojibake dla polskich znaków (latin-2 → UTF-8)
    mojibake_fixes = {
        'Ä\x85': 'ą', 'Ä\x87': 'ć', 'Ä™': 'ę', 'Å\x82': 'ł',
        'Å\x84': 'ń', 'Ã³': 'ó', 'Å\x9b': 'ś', 'Å¼': 'ż', 'Å¹': 'ź',
    }
    for bad, good in mojibake_fixes.items():
        text = text.replace(bad, good)
    
    # Normalizuj whitespace
    import re
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    
    return text.strip()
```

### Etap 4: Chunking

> **Uwaga Ollama:** Llama3.2 (7B) ma domyślnie context window 4096 tokenów. 
> Polski tekst = ~3-4 znaki/token. Przy `CHUNK_MAX_CHARS=12000` + prompt (~300 tok)
> ryzyko przekroczenia limitu. Używaj `CHUNK_MAX_CHARS_OLLAMA=7000` gdy `LLM_PROVIDER=ollama`.
> Aby zwiększyć ctx Ollama: dodaj `num_ctx: 8192` do parametrów wywołania.

> ⚠️ **WAŻNE: `_get_chunk_size()` MUSI być wywołana przy tworzeniu chunków.**
> Nie używaj hardcoded stałej `CHUNK_MAX_CHARS` bezpośrednio w `_chunk()`.
> Zawsze wywołaj helper per-provider:
> ```python
> def _chunk_text(self, text: str) -> list[str]:
>     chunk_size = self._get_chunk_size(self.provider)  # ← wywołaj helper!
>     # NIE używaj hardcoded stałej
>     return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
> ```
>
> **Wymagane testy:**
> - Dla `provider="ollama"`: każdy chunk musi mieć `len(chunk) <= 7000`
> - Dla `provider="openai"`: każdy chunk musi mieć `len(chunk) <= 12000`

```python
def _chunk(self, text: str) -> list[str]:
    """
    Dzieli tekst na chunki ≤ chunk_size (per provider, via _get_chunk_size).
    
    Strategia: podział na akapity (\n\n), łączenie w chunki do limitu.
    Jeśli akapit > limit: podział na zdania ('. ', '.\n').
    Zachowuje kontekst: ostatnie zdanie chunku N jest pierwszym zdaniem chunku N+1
    (overlap = 1 zdanie).
    """
    chunk_size = self._get_chunk_size(self.provider)  # ← ZAWSZE używaj helpera
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = []
    current_len = 0
    
    for para in paragraphs:
        # Obsługa akapitów dłuższych niż CHUNK_MAX_CHARS (ekstremalnie rzadkie)
        if len(para) > chunk_size:
            # Podziel na zdania (fallback: na znakach)
            sentences = re.split(r'(?<=[.!?])\s+', para)
            for sentence in sentences:
                if current_len + len(sentence) + 2 > chunk_size and current_chunk:
                    chunks.append('\n\n'.join(current_chunk))
                    current_chunk = []
                    current_len = 0
                current_chunk.append(sentence)
                current_len += len(sentence) + 2
            continue  # pomiń standardowe przetwarzanie tego akapitu

        if current_len + len(para) + 2 > chunk_size:
            if current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                # Overlap: ostatni akapit jako początek nowego chunka
                current_chunk = [current_chunk[-1]] if current_chunk else []
                current_len = len(current_chunk[0]) if current_chunk else 0
        
        current_chunk.append(para)
        current_len += len(para) + 2
    
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks if chunks else [text]
```

---

## 4. Wykrywanie języka

```python
def _detect_language(self, text: str) -> str:
    """
    Heurystyka wykrywania języka (bez zewnętrznych bibliotek):
    - Sprawdza gęstość polskich znaków diakrytycznych (ą,ę,ó,ś,ż,ź,ć,ń,ł)
    - Jeśli > 0.5% znaków to polskie diakrytyki → "pl"
    - Inaczej → "en" (domyślne)
    
    Dla v2: langdetect lub lingua
    """
    pl_chars = set('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ')
    if len(text) == 0:
        return "unknown"
    pl_density = sum(1 for c in text if c in pl_chars) / len(text)
    return "pl" if pl_density > 0.005 else "en"
```

---

## 5. Schemat wyjścia — ParsedBrief

Pełny przykład dla typowego briefu 4-stronicowego (.docx):

```json
{
  "text": "Projekt dotyczy budowy systemu płatności online...\n\nWymagania bezpieczeństwa...",
  "metadata": {
    "author": "Jan Kowalski",
    "title": "Brief Projektu Fintech",
    "paragraph_count": 87,
    "word_count": 1243,
    "char_count": 8421,
    "detected_language": "pl",
    "parse_duration_ms": 145
  },
  "chunks": [
    "Projekt dotyczy budowy systemu płatności online...",
    "Wymagania bezpieczeństwa: PCI DSS, szyfrowanie TLS 1.3..."
  ],
  "format": "docx",
  "char_count": 8421,
  "word_count": 1243
}
```

---

## 6. Obsługa błędów

| Wyjątek | Gdy | HTTP response |
|---------|-----|--------------|
| `FileTooLargeError` | `len(content) > 50 MB` | 413 |
| `UnsupportedFormatError` | format = "unknown" | 415 |
| `ParseError("zaszyfrowany")` | PDF bez tekstu | 422 |
| `ParseError("pusty")` | brak wyekstrahowanego tekstu | 422 |
| `ParseError("uszkodzony")` | wyjątek biblioteki (pdfplumber, docx) | 422 |

---

## 7. Zależności

```toml
# pyproject.toml — nowe zależności dla warsztatu
[project.optional-dependencies]
workshop = [
    "pdfplumber>=0.11",
    "python-docx>=1.1",
    "python-magic>=0.4",   # wykrywanie MIME (wymaga libmagic)
]
```

---

## 8. Metryki jakości parsowania

Logowane w `briefs.metadata`:

| Metryka | Opis |
|---------|------|
| `word_count` | Liczba słów w znormalizowanym tekście |
| `char_count` | Liczba znaków |
| `chunks_count` | Liczba chunków |
| `detected_language` | Wykryty język |
| `parse_duration_ms` | Czas parsowania |
| `empty_pages` | (tylko PDF) Liczba stron bez tekstu |

**Ostrzeżenie (nie błąd) gdy:**
- `word_count < 50` — brief bardzo krótki, wyniki mapowania mogą być niepewne
- `detected_language = "unknown"` — nieznany język
- `empty_pages > 0` — PDF ze skanami (brak OCR)
