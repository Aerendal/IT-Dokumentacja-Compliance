# 07 — LLM Adapter Spec

**Status:** Draft v1.0  
**Powiązane dokumenty:** 03_architecture_overview, 05_module_interface_contracts, 13_security_and_config_spec

---

## 1. Cel i zakres

LLM Adapter to warstwa abstrakcji między Warsztatem a zewnętrznymi/lokalnymi modelami językowymi. Realizuje **wzorzec Strategy** — każdy dostawca to osobna implementacja wspólnego interfejsu. Podmiana dostawcy nie wymaga zmian w kodzie biznesowym.

Odpowiada za:
- Ekstrakcję semantycznych encji z treści briefu
- Generowanie szkieletów szablonów ze specyfikacji
- Reranking wyników mapowania (opcjonalny, dla poprawy precision)
- Logowanie wywołań (audit, cache, koszty)

---

## 2. Interfejs bazowy

```python
# workshop/api/services/llm_adapter.py

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


@dataclass
class ExtractedEntities:
    domains:      list[str]
    standards:    list[str]
    regulations:  list[str]
    phases:       list[int]  # 1-based (1–24); konwersja na 0-based dla DB w SemanticMapper
    keywords:     list[str]
    project_type: str | None = None


@dataclass
class MappingCandidate:
    doc_uid:    str
    doc_title:  str
    phase_id:   int
    match_reason: str


@dataclass
class LLMScoredCandidate:
    """
    Wynik rerankingu zwracany przez LLM Adapter (rerank_mapping).
    Nazwa różna od SemanticMapper.ScoredCandidate (dok.09) celowo —
    ta klasa to tymczasowy wynik parsowania odpowiedzi LLM przed blendingiem.
    """
    doc_uid:    str
    score:      float        # 0.0–1.0 (zwracane przez LLM)
    reason:     str


@dataclass
class LLMResponse:
    content:       str
    model:         str
    input_tokens:  int
    output_tokens: int
    latency_ms:    int
    cached:        bool  = False
    finish_reason: str   = "stop"  # "stop" | "length" | "content_filter"
    # Uwaga: finish_reason == "length" oznacza ucięty output — wywołujący MUSI obsłużyć


class BaseLLMAdapter(ABC):
    """Interfejs strategii LLM. Każdy dostawca implementuje tę klasę."""

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Nazwa dostawcy: 'openai', 'anthropic', 'ollama'"""

    @property
    @abstractmethod
    def model_name(self) -> str:
        """Nazwa modelu: 'gpt-4o', 'claude-3-5-sonnet-20241022', 'llama3.2'"""

    @abstractmethod
    async def extract_entities(
        self,
        text: str,
        max_tokens: int = 2000
    ) -> ExtractedEntities:
        """
        Wyciąga encje semantyczne z tekstu briefu.
        
        Kontrakt:
          - text nie może być pusty
          - text ≤ 100 000 znaków (chunking po stronie wywołującego)
          - Zawsze zwraca ExtractedEntities (puste listy jeśli nic nie znaleziono)
          - Loguje wywołanie w llm_calls_log
        
        Raises:
          LLMTimeoutError    — brak odpowiedzi > 30s
          LLMRateLimitError  — HTTP 429 od providera
          LLMProviderError   — inne błędy HTTP/sieci
        """

    @abstractmethod
    async def generate_template(
        self,
        spec_text: str,
        standard_code: str | None = None,
        hint_title:    str | None = None
    ) -> str:
        """
        Generuje szkielet szablonu Markdown z YAML frontmatter.
        
        Kontrakt:
          - Zwraca poprawny Markdown z blokiem --- YAML ---
          - Frontmatter zawiera co najmniej: title, category, phase_id, standards[]
          - Sekcje szablonu oparte na strukturze itdoc
        
        Raises: LLMTimeoutError, LLMProviderError
        """

    @abstractmethod
    async def rerank_mapping(
        self,
        brief_text:     str,
        candidates:     list[MappingCandidate],
        max_candidates: int = 50
    ) -> list[ScoredCandidate]:
        """
        Opcjonalny reranking kandydatów mapowania (LLM-as-judge).
        
        Kontrakt:
          - Zwraca listę posortowaną malejąco wg score
          - len(result) ≤ max_candidates
          - score ∈ [0.0, 1.0]
        """
```

---

## 3. Implementacje dostawców

### 3.1 OpenAI

```python
class OpenAIAdapter(BaseLLMAdapter):
    """
    Dostawca: OpenAI (gpt-4o, gpt-4o-mini, gpt-4-turbo)
    Wymagane env: OPENAI_API_KEY
    Opcjonalne env: OPENAI_MODEL (default: gpt-4o), OPENAI_TIMEOUT (default: 30)
    """

    def __init__(self, settings: Settings):
        self._client = AsyncOpenAI(api_key=settings.openai_api_key)
        self._model  = settings.openai_model or "gpt-4o"

    @property
    def provider_name(self) -> str: return "openai"

    @property
    def model_name(self) -> str: return self._model

    async def extract_entities(self, text: str, max_tokens: int = 2000) -> ExtractedEntities:
        prompt = EXTRACT_ENTITIES_PROMPT.format(text=text)
        response = await self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            max_tokens=max_tokens,
            timeout=30,
        )
        raw = json.loads(response.choices[0].message.content)
        return ExtractedEntities(**raw)
```

### 3.2 Anthropic

```python
class AnthropicAdapter(BaseLLMAdapter):
    """
    Dostawca: Anthropic (claude-3-5-sonnet, claude-3-haiku)
    Wymagane env: ANTHROPIC_API_KEY
    Opcjonalne env: ANTHROPIC_MODEL (default: claude-3-5-sonnet-20241022)
    """

    def __init__(self, settings: Settings):
        self._client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
        self._model  = settings.anthropic_model or "claude-3-5-sonnet-20241022"
```

### 3.3 Ollama (lokalny)

```python
class OllamaAdapter(BaseLLMAdapter):
    """
    Dostawca: Ollama (lokalne LLM, brak opłat per token)
    Wymagane env: OLLAMA_BASE_URL (default: http://localhost:11434)
    Opcjonalne env: OLLAMA_MODEL (default: llama3.2)
    
    Uwaga: Ollama jest synchroniczne — wrapper przez asyncio.run_in_executor.
    Precision może być niższa niż GPT-4o dla złożonych briefów.
    """

    def __init__(self, settings: Settings):
        self._base_url = settings.ollama_base_url or "http://localhost:11434"
        self._model    = settings.ollama_model or "llama3.2"
```

---

## 4. Factory — wybór dostawcy

```python
# workshop/api/services/llm_adapter.py

def create_llm_adapter(settings: Settings) -> BaseLLMAdapter:
    """
    Fabryka zwracająca adapter na podstawie LLM_PROVIDER z .env.
    
    Kolejność fallback:
      1. settings.llm_provider ("openai" | "anthropic" | "ollama")
      2. Jeśli klucz API brak → ValueError z jasnym komunikatem
    """
    provider = settings.llm_provider.lower()
    match provider:
        case "openai":
            if not settings.openai_api_key:
                raise ValueError("OPENAI_API_KEY nie jest ustawiony. Sprawdź plik .env")
            return OpenAIAdapter(settings)
        case "anthropic":
            if not settings.anthropic_api_key:
                raise ValueError("ANTHROPIC_API_KEY nie jest ustawiony.")
            return AnthropicAdapter(settings)
        case "ollama":
            return OllamaAdapter(settings)
        case _:
            raise ValueError(f"Nieznany dostawca LLM: {provider}. Dostępne: openai, anthropic, ollama")
```

---

## 5. Prompt templates

Szablony promptów są przechowywane w `workshop/api/services/prompts/` jako pliki `.txt`. Parametryzowane przez `str.format()`.

### 5.1 `extract_entities.txt`

```
Jesteś ekspertem analizy wymagań IT. Przeanalizuj poniższy brief projektu i wyciągnij:
1. Domeny techniczne (np. fintech, cloud, mobile, security, data-engineering)
2. Standardy/normy wymienione lub sugerowane (np. ISO 27001, PCI DSS, OWASP)
3. Regulacje prawne (np. RODO, KSC, NIS2, AI Act)
4. Fazy cyklu życia projektu (podaj numery 0-23: 0=Conception, 1=Requirements, 
   2=Architecture, 3=Design, 4=Development, 5=Testing, 6=Integration, 7=UAT,
   8=Deployment, 9=Operations, 10=Monitoring, 11=Maintenance, 12=Security,
   13=Documentation, 14=Training, 15=Support, 16=BCP, 17=Governance, 
   18=Compliance, 19=Risk, 20=Data, 21=ProjectMgmt, 22=Decommission, 23=Phase24)
5. Słowa kluczowe techniczne (max 20)
6. Typ projektu (greenfield_saas / migration / integration / audit / modernization / other)

Odpowiedz TYLKO jako JSON:
{{
  "domains": [...],
  "standards": [...],
  "regulations": [...],
  "phases": [...],
  "keywords": [...],
  "project_type": "..."
}}

BRIEF:
{text}
```

### 5.2 `generate_template.txt`

```
Jesteś ekspertem dokumentacji IT. Na podstawie poniższej specyfikacji wygeneruj szablon 
dokumentu w formacie Markdown z YAML frontmatter (zgodny ze standardem biblioteki itdoc).

Wymagania szablonu:
- Blok frontmatter między --- a ---
- Frontmatter musi zawierać: title, category, phase_id, standards (lista)
- Sekcje: Cel dokumentu, Zakres, Definicje, [sekcje specyficzne], Powiązane dokumenty
- Każda sekcja z krótkim opisem (2-3 zdania placeholder)
- Bez emoji, bez znaków specjalnych poza standardowym Markdown
{hint_standard}
{hint_title}

SPECYFIKACJA:
{spec_text}

Wygeneruj TYLKO Markdown szablonu (bez dodatkowych komentarzy):
```

### 5.3 `rerank_candidates.txt`

```
Oceń trafność poniższych szablonów dokumentów dla danego projektu IT.
Zwróć JSON z listą wyników posortowaną malejąco wg score.

BRIEF PROJEKTU (skrót):
{brief_summary}

KANDYDACI (maksymalnie {max_candidates}):
{candidates_json}

Odpowiedź JSON:
[{{"doc_uid": "...", "score": 0.0-1.0, "reason": "..."}}]
```

---

## 6. Cache wywołań LLM

Aby ograniczyć koszty API, wyniki wywołań LLM są cachowane w tabeli `llm_calls_log` na podstawie SHA256 promptu.

```python
async def _get_cached_response(self, prompt_hash: str) -> str | None:
    """Sprawdź cache. Zwróć None jeśli brak lub stary (>24h)."""

async def _save_to_cache(self, prompt_hash: str, response: str, ...) -> None:
    """Zapisz wynik + metadata do llm_calls_log."""
```

**Polityka cache:**
- Ważność: 24 godziny (konfigurowalne przez `LLM_CACHE_TTL_HOURS`)
- Klucz: `SHA256(prompt_text + provider_name + model_name)` — **NIE** samo SHA256(prompt)
  - Zmiana modelu z `gpt-4o` na `gpt-4o-mini` → inny hash → brak false cache hit
- `force_rerun=True` pomija cache

```python
def _make_cache_key(self, prompt: str) -> str:
    """Cache key uwzględnia provider i model aby unikać kolizji przy zmianie modelu."""
    import hashlib
    payload = f"{prompt}|{self.provider_name}|{self.model_name}"
    return hashlib.sha256(payload.encode()).hexdigest()
```

---

## 7. Obsługa błędów i retry

```python
# Dekorator retry dla wywołań LLM
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(LLMRateLimitError),
    reraise=True
)
async def _call_with_retry(self, ...):
    ...
```

**Polityka retry:**
| Błąd | Retry | Zachowanie |
|------|-------|-----------|
| `LLMRateLimitError` (429) | 3x, exponential backoff 2-10s | Re-raise po 3 próbach |
| `LLMTimeoutError` | 2x, czekaj 5s | Re-raise po 2 próbach |
| `LLMProviderError` (5xx) | 1x, czekaj 2s | Re-raise po 1 próbie |
| `LLMProviderError` (4xx poza 429) | 0x | Natychmiast re-raise |

**Obsługa `json.loads` — nigdy bez try/except:**

```python
def _parse_llm_json(self, content: str, operation: str) -> dict:
    """Parsuj JSON z odpowiedzi LLM. Rzuca LLMParseError zamiast ValueError."""
    try:
        return json.loads(content)
    except (json.JSONDecodeError, ValueError) as e:
        raise LLMParseError(
            f"LLM ({operation}) zwróciło nie-JSON: {content[:200]}..."
        ) from e
```

**Obsługa uciętego outputu (`finish_reason == "length"`):**

```python
if response.finish_reason == "length":
    logger.warning(
        f"LLM output ucięty (finish_reason=length) dla operacji '{operation}'. "
        f"Tokens użyte: {response.output_tokens}. "
        f"Rozważ zwiększenie max_tokens lub skrócenie promptu."
    )
    # NIE rzucaj wyjątku — spróbuj parsować co się dało
    # Wywołujący powinien sprawdzić finish_reason w LLMResponse
```

---

## 8. Konfiguracja (zmienne środowiskowe)

```ini
# .env — LLM Provider
LLM_PROVIDER=openai                    # openai | anthropic | ollama

# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o                    # gpt-4o | gpt-4o-mini | gpt-4-turbo
OPENAI_TIMEOUT=30                      # sekundy

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# Ollama (lokalny)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Cache
LLM_CACHE_TTL_HOURS=24
LLM_CACHE_ENABLED=true
```

---

## 9. Logowanie w llm_calls_log

Każde wywołanie (cache miss lub cache hit) jest zapisywane:

```python
await self._log_call(
    provider=self.provider_name,
    model=self.model_name,
    operation="extract_entities",          # "extract_entities" | "generate_template" | "rerank_mapping"
    prompt_hash=sha256(prompt),
    input_tokens=response.input_tokens,
    output_tokens=response.output_tokens,
    latency_ms=elapsed_ms,
    status="ok",                           # "ok" | "error" | "cached"
    response_cached=False,
    entity_id=mapping_id,                  # powiązany UUID z bazy
)
```

---

## §10 — Rozszerzenie: Plugin System (entry_points)

Aktualnie nowy LLM provider wymaga edycji `create_llm_adapter()`.

**Docelowo (v2+):** Entry-points based discovery:

```toml
# pyproject.toml zewnętrznego pakietu
[project.entry-points."workshop.llm_adapters"]
gemini = "my_workshop_gemini:GeminiAdapter"
bedrock = "my_workshop_bedrock:BedrockAdapter"
```

```python
from importlib.metadata import entry_points

def create_llm_adapter(settings: Settings) -> BaseLLMAdapter:
    eps = entry_points(group="workshop.llm_adapters")
    if settings.llm_provider in eps:
        adapter_cls = eps[settings.llm_provider].load()
        return adapter_cls(settings)
    # Fallback do wbudowanych adapterów
    ...
```

Korzyść: Zewnętrzni dostawcy mogą dodać własne adaptery bez forku repozytorium.
