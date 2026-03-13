# 17 — AI Agent Context Specification

**Wersja:** 1.0  
**Status:** Draft  
**Cel:** Eliminacja domysłów AI agentów przez dostarczenie pełnego, ustrukturyzowanego kontekstu na każdym etapie pracy.

---

## 1. Problem: Dlaczego AI "zgaduje"

Obecny `WorkPackage` dostarcza AI agentowi minimum:

```json
{ "doc_uid": "abc123", "template": "audit_plan", "assignee": "ai", "depends_on": ["xyz"] }
```

Brakuje odpowiedzi na pytania:
- **Co konkretnie mam wyprodukować?** (struktura szablonu)
- **Dlaczego ten szablon?** (uzasadnienie mapowania)
- **Jak wiem że skończyłem?** (measurable done)
- **Co już wiadomo o projekcie?** (kontekst z poprzednich pakietów)
- **Co zrobić gdy brief jest niejasny?** (disambiguation protocol)

---

## 2. Wzbogacony WorkPackage (`WorkPackageV2`)

### 2.1 Schema

```python
class WorkPackageV2(BaseModel):
    # --- Identyfikacja (bez zmian) ---
    id: str                          # UUID
    plan_id: str
    doc_uid: str
    template_name: str
    phase_id: int
    assignee_type: Literal["ai", "human", "review"]
    status: WorkPackageStatus        # patrz §4
    depends_on: list[str]            # IDs poprzednich pakietów

    # --- NOWE: Kontekst dla AI ---
    context: WorkPackageContext

class WorkPackageContext(BaseModel):
    # Skąd pochodzi ten dokument
    rationale: MappingRationale

    # Jak wygląda docelowy szablon
    template_preview: TemplatePreview

    # Czego oczekujemy jako output
    quality_gates: list[QualityGate]

    # Co zostało już ustalone w poprzednich pakietach
    project_facts: ProjectFacts

    # Co zrobić gdy czegoś brakuje
    disambiguation_hints: list[DisambiguationHint]
```

### 2.2 `MappingRationale` — dlaczego ten szablon

```python
class MappingRationale(BaseModel):
    confidence_score: float          # 0.0–1.0
    confidence_label: Literal["high", "medium", "low"]
    # high: >=0.70 | medium: 0.50–0.69 | low: <0.50 (wymaga review)

    matched_keywords: list[str]      # słowa kluczowe które spowodowały match
    matched_phases: list[str]        # fazy projektu z briefu -> fazy szablonu

    alternative_templates: list[AlternativeTemplate]  # top-3 alternatywy

class AlternativeTemplate(BaseModel):
    doc_uid: str
    template_name: str
    confidence_score: float
    reason_not_selected: str         # dlaczego nie ten
```

### 2.3 `TemplatePreview` — co wyprodukować

```python
class TemplatePreview(BaseModel):
    title: str
    category: str                    # np. "audit", "specification", "report"
    phase: str                       # np. "planning", "implementation"
    required_sections: list[TemplateSection]
    optional_sections: list[TemplateSection]
    estimated_pages: tuple[int, int] # min, max
    standards: list[str]             # normy których dotyczy

class TemplateSection(BaseModel):
    heading: str
    description: str                 # co powinno się tu znaleźć
    required: bool
    example_content: str | None      # przykładowa treść (gdy dostępna)
```

### 2.4 `QualityGate` — measurable done

```python
class QualityGate(BaseModel):
    criterion: str                   # np. "Sekcja 'Zakres' musi mieć >=3 zdania"
    check_type: Literal[
        "min_length",                # minimalna długość sekcji
        "required_field",            # pole musi być wypełnione
        "format_match",              # regex lub format
        "cross_reference",           # odniesienie do innego dokumentu
        "human_review",              # wymaga zatwierdzenia człowieka
    ]
    automated: bool                  # czy system może sprawdzić automatycznie
    severity: Literal["blocking", "warning"]
```

**Przykład quality gates dla szablonu "Plan Audytu":**
```json
[
  {"criterion": "Sekcja 'Zakres audytu' musi zawierać >=2 paragrafy", "check_type": "min_length", "automated": true, "severity": "blocking"},
  {"criterion": "Pole 'data_audytu' musi być uzupełnione", "check_type": "required_field", "automated": true, "severity": "blocking"},
  {"criterion": "Dokument musi odwoływać się do co najmniej 1 normy", "check_type": "cross_reference", "automated": true, "severity": "warning"},
  {"criterion": "Kierownik projektu zatwierdził zakres", "check_type": "human_review", "automated": false, "severity": "blocking"}
]
```

### 2.5 `ProjectFacts` — co już wiadomo

```python
class ProjectFacts(BaseModel):
    client_name: str | None
    project_type: str | None         # np. "system informatyczny", "wdrożenie ERP"
    industry: str | None             # np. "fintech", "healthcare"
    detected_phases: list[str]       # fazy wykryte z briefu
    known_constraints: list[str]     # ograniczenia z briefu (terminy, budżet itp.)
    completed_packages: list[CompletedPackageSummary]  # co już zrobiono

class CompletedPackageSummary(BaseModel):
    doc_uid: str
    template_name: str
    key_decisions: list[str]         # decyzje podjęte w tym dokumencie
    # np. ["Wybrany framework: Spring Boot", "Termin: Q3 2026"]
```

---

## 3. Disambiguation Protocol

### 3.1 Kiedy brief jest niewystarczający

AI agent MUSI sklasyfikować każdą niejasność jako jeden z typów:

| Typ | Definicja | Przykład | Działanie |
|---|---|---|---|
| `MISSING_CRITICAL` | Brak informacji bez której nie można wykonać pakietu | Brak opisu systemu | Zatrzymaj → poproś o uzupełnienie |
| `MISSING_OPTIONAL` | Brak informacji opcjonalnej | Brak preferowanego dostawcy | Użyj wartości domyślnej z szablonu |
| `AMBIGUOUS` | Informacja istnieje ale ma wiele interpretacji | "system ERP lub CRM" | Wybierz najbardziej prawdopodobną, udokumentuj założenie |
| `CONFLICTING` | Dwie informacje w briefie sobie przeczą | Termin Q1 vs "za 2 lata" | Użyj konserwatywnej (późniejszej) wartości, flaguj |
| `BELOW_THRESHOLD` | Confidence mapowania < 0.50 | Słowa kluczowe nie pasują | Eskaluj do human review |

### 3.2 Decision Tree

```
brief.word_count < 50?
  → ZATRZYMAJ: "Brief za krótki — minimum 50 słów"

confidence_score < 0.50?
  → ESKALACJA: human_review = True, uzasadnienie w rationale

Dla każdej niejasności:
  typ == MISSING_CRITICAL?
    → Dodaj do clarification_requests[], zatrzymaj pakiet
  typ == MISSING_OPTIONAL?
    → Użyj template_defaults[field], ustaw assumption_flag = True
  typ == AMBIGUOUS?
    → Wybierz interpretację z najwyższym prior (industry_defaults[])
    → Zapisz w assumptions[]: {"field": "...", "assumed": "...", "reason": "..."}
  typ == CONFLICTING?
    → Wybierz konserwatywną wartość
    → Zapisz w conflicts[]: {"field": "...", "v1": "...", "v2": "...", "resolved": "..."}

Wszystkie pakiety z assumption_flag = True → status = "needs_review" (nie "ready")
```

### 3.3 `ClarificationRequest` — pytanie do klienta

```python
class ClarificationRequest(BaseModel):
    id: str
    package_id: str
    field: str                       # jakie pole wymaga uzupełnienia
    question: str                    # pytanie do klienta w języku naturalnym
    context: str                     # dlaczego to pytanie jest potrzebne
    options: list[str] | None        # sugerowane odpowiedzi (gdy możliwe)
    required: bool                   # czy blokuje generowanie czy tylko ostrzega
    created_at: datetime
    answered_at: datetime | None
    answer: str | None
```

**Przykład:**
```json
{
  "field": "system_type",
  "question": "Czy wdrażany system to nowa aplikacja, czy migracja istniejącej?",
  "context": "Odpowiedź wpływa na wybór szablonu 'Plan migracji' vs 'Spec nowego systemu'",
  "options": ["Nowa aplikacja", "Migracja", "Modernizacja istniejącej"],
  "required": true
}
```

### 3.4 Unified `confidence_threshold`

Rozwiązanie konfliktu J-06 (4 różne wartości w spec docs):

| Próg | Label | Znaczenie | Działanie systemu |
|---|---|---|---|
| >= 0.70 | `HIGH` | Pewne dopasowanie | Auto-accept |
| 0.50–0.69 | `MEDIUM` | Prawdopodobne dopasowanie | Accept z flagą `assumption_flag=True` |
| 0.30–0.49 | `LOW` | Niepewne dopasowanie | Human review wymagany |
| < 0.30 | `REJECTED` | Brak dopasowania | Nie tworzy MappingItem |

> **Canonical source:** `settings.CONFIDENCE_THRESHOLD_*` — 4 stałe w konfiguracji, nie hardcoded.

---

## 4. State Machine dla `work_package.status`

### 4.1 Stany i przejścia

```
pending ──[assign]──→ in_progress
                           |
              ┌────────────┼──────────────┐
              |            |              |
         [complete]   [flag_review]  [flag_blocked]
              |            |              |
              v            v              v
           done        needs_review    blocked
                           |              |
                      [approve]      [unblock]
                           |              |
                           └──────────────┘
                                  |
                               done
```

### 4.2 Tabela przejść

| Stan źródłowy | Akcja | Stan docelowy | Warunek |
|---|---|---|---|
| `pending` | `assign` | `in_progress` | depends_on[] wszystkie `done` |
| `in_progress` | `complete` | `done` | Wszystkie blocking quality_gates zaliczone |
| `in_progress` | `flag_review` | `needs_review` | assumption_flag=True LUB warning quality_gate |
| `in_progress` | `flag_blocked` | `blocked` | clarification_requests[required=True] nieodpowiedziane |
| `needs_review` | `approve` | `done` | Human reviewer zatwierdził |
| `needs_review` | `reject` | `in_progress` | Human reviewer odrzucił z komentarzem |
| `blocked` | `unblock` | `in_progress` | Wszystkie clarification_requests[required] odpowiedziane |
| `done` | `reopen` | `in_progress` | Zależny pakiet wykrył konflikt |

### 4.3 Analogiczne state machines

**`brief.parse_status`:** `uploaded → parsing → parsed → mapping → mapped → error`  
**`mapping_result.status`:** `pending → running → done → error`  
**`estimation_report.status`:** `draft → accepted → rejected`  

Każde przejście wymaga: `changed_by` (user_id lub `"system"`), `changed_at`, opcjonalnie `reason`.

---

## 5. Brakujące algorytmy (E-07)

### 5.1 `_infer_doc_type(title: str) -> str`

```python
import re

DOC_TYPE_RULES = [
    # (regex_pattern, doc_type)
    (r'\baudit\b|\baudyt\b',              'audit'),
    (r'\bspecification\b|\bspecyfikacj',  'specification'),
    (r'\breport\b|\braport\b',            'report'),
    (r'\bplan\b|\bplanowanie\b',          'plan'),
    (r'\bprocedur',                       'procedure'),
    (r'\bpolicy\b|\bpolityk',             'policy'),
    (r'\bmanual\b|\binstrukcj',           'manual'),
    (r'\bcontract\b|\bumow',              'contract'),
    (r'\banalysis\b|\banaliz',            'analysis'),
]
DEFAULT_DOC_TYPE = 'general'

def _infer_doc_type(title: str) -> str:
    title_lower = title.lower()
    for pattern, doc_type in DOC_TYPE_RULES:
        if re.search(pattern, title_lower):
            return doc_type
    return DEFAULT_DOC_TYPE
```

### 5.2 `_domain_multiplier(industries: list[str]) -> float`

```python
DOMAIN_MULTIPLIERS = {
    'fintech':      1.3,   # regulacje, audyty
    'healthcare':   1.4,   # HIPAA, MDR, procesy kliniczne
    'legal':        1.35,  # compliance, dokumentacja prawna
    'government':   1.25,  # przetargi, RODO
    'energy':       1.2,   # BHP, normy ISO
    'default':      1.0,
}

def _domain_multiplier(industries: list[str]) -> float:
    """Zwraca max z multiplikatorów. Wiele branż → konserwatywnie max."""
    if not industries:
        return DOMAIN_MULTIPLIERS['default']
    return max(
        DOMAIN_MULTIPLIERS.get(ind.lower(), DOMAIN_MULTIPLIERS['default'])
        for ind in industries
    )
```

### 5.3 `_estimate_base_hours` — źródło prawdy: `spec10`

> **Ważne:** Kanoniczny algorytm szacowania godzin zdefiniowany jest w
> `10_estimation_engine_spec.md` §2.2 (`points_to_hours()` + `H_PER_POINT = 0.5`).  
> Poniższa tabela `BASE_HOURS_TABLE` służy wyłącznie do **wstępnego szacunku**
> w `WorkPackageContext.template_preview.estimated_pages` — przed uruchomieniem
> pełnego `EstimationEngine`. Nie zastępuje obliczeń z spec10.

```python
# Tylko do wstępnego podglądu w WorkPackageContext — nie do kosztorysu
BASE_HOURS_TABLE = {
    # doc_type: (min_h, likely_h, max_h) przy complexity=1.0
    'specification': (4.0,  8.0,  16.0),
    'audit':         (3.0,  6.0,  12.0),
    'report':        (2.0,  4.0,   8.0),
    'plan':          (3.0,  6.0,  10.0),
    'procedure':     (1.5,  3.0,   6.0),
    'policy':        (2.0,  4.0,   8.0),
    'manual':        (4.0,  8.0,  20.0),
    'contract':      (2.0,  4.0,   8.0),
    'analysis':      (3.0,  6.0,  12.0),
    'general':       (2.0,  4.0,   8.0),
}

def _estimate_base_hours(doc_type: str, complexity_multiplier: float) -> tuple[float, float, float]:
    min_h, likely_h, max_h = BASE_HOURS_TABLE.get(doc_type, BASE_HOURS_TABLE['general'])
    return (
        round(min_h    * complexity_multiplier, 1),
        round(likely_h * complexity_multiplier, 1),
        round(max_h    * complexity_multiplier, 1),
    )
```

---

## 6. Nowe / rozszerzone endpointy

### 6.1 `GET /planning/{plan_id}/packages/{pkg_id}/context`
Zwraca pełny `WorkPackageContext` — template preview, rationale, quality gates, project facts.

### 6.2 `POST /planning/{plan_id}/packages/{pkg_id}/clarify`
Odpowiada na `ClarificationRequest`. Jeśli wszystkie `required` odpowiedziane → automatycznie `unblock`.

### 6.3 `GET /planning/{plan_id}/packages/{pkg_id}/quality-check`
Uruchamia automated quality gates. Zwraca `{passed: [...], failed: [...], warnings: [...]}`.

### 6.4 `POST /brief/{brief_id}/disambiguate`
Uruchamia Disambiguation Protocol ręcznie. Zwraca `clarification_requests[]` bez blokowania.

---

## 7. Konfiguracja (nowe stałe)

```python
# settings.py — uzupełnienie
CONFIDENCE_THRESHOLD_HIGH:   float = 0.70
CONFIDENCE_THRESHOLD_MEDIUM: float = 0.50
CONFIDENCE_THRESHOLD_LOW:    float = 0.30
# < LOW → REJECTED, nie tworzy MappingItem

BRIEF_MIN_WORD_COUNT:        int   = 50
BRIEF_MAX_FILE_SIZE_MB:      int   = 50   # canonical (spec05: 10MB to dla ingestii)

QUALITY_GATE_AUTOCHECK:      bool  = True
ASSUMPTION_FLAG_REQUIRES_REVIEW: bool = True

# WorkPackage context
TEMPLATE_PREVIEW_ENABLED:    bool  = True
MAX_ALTERNATIVE_TEMPLATES:   int   = 3
PROJECT_FACTS_LOOKBACK_PACKAGES: int = 10  # ile poprzednich pakietów do kontekstu
```

---

## 8. Wpływ na istniejące moduły

| Moduł | Zmiana | Priorytet |
|---|---|---|
| `WorkPlanner` | Generuje `WorkPackageV2` z pełnym `context` | MVP |
| `SemanticMapper` | Zwraca `MappingRationale` z `matched_keywords`, `alternatives` | MVP |
| `EstimationEngine` | Używa `BASE_HOURS_TABLE` + `_domain_multiplier()` | MVP |
| `BriefParser` | Wykrywa `MISSING_CRITICAL` → tworzy `ClarificationRequest` | V1.1 |
| `WebhookService` | Emituje zdarzenia przy zmianie stanu work_package | V1.1 |
| `ItdocConnector` | Dostarcza `template_sections[]` dla `TemplatePreview` | MVP |

---

## 9. QualityGate Checker — implementacje

Sekcja definiuje konkretne klasy checkerów dla `automated=True` quality gates.

### 9.1 Base interface

```python
from abc import ABC, abstractmethod

class QualityGateChecker(ABC):
    @abstractmethod
    def check(self, content: dict[str, str]) -> tuple[bool, str | None]:
        """
        Args:
            content: dict sekcja→tekst (np. {"Zakres audytu": "Lorem ipsum..."})
        Returns:
            (passed: bool, error_message: str | None)
        """
```

### 9.2 Implementacje per `check_type`

```python
class MinLengthChecker(QualityGateChecker):
    """check_type = 'min_length'"""
    def __init__(self, section: str, min_chars: int = 0, min_paragraphs: int = 0):
        self.section = section
        self.min_chars = min_chars
        self.min_paragraphs = min_paragraphs

    def check(self, content: dict[str, str]) -> tuple[bool, str | None]:
        text = content.get(self.section, "")
        if self.min_chars and len(text) < self.min_chars:
            return False, f"Sekcja '{self.section}': {len(text)} znaków, wymagane {self.min_chars}"
        if self.min_paragraphs:
            count = len([p for p in text.split('\n\n') if p.strip()])
            if count < self.min_paragraphs:
                return False, f"Sekcja '{self.section}': {count} paragrafów, wymagane {self.min_paragraphs}"
        return True, None


class RequiredFieldChecker(QualityGateChecker):
    """check_type = 'required_field'"""
    def __init__(self, field: str):
        self.field = field

    def check(self, content: dict[str, str]) -> tuple[bool, str | None]:
        value = content.get(self.field, "").strip()
        if not value:
            return False, f"Pole '{self.field}' jest wymagane i nie może być puste"
        return True, None


class FormatMatchChecker(QualityGateChecker):
    """check_type = 'format_match'"""
    def __init__(self, field: str, pattern: str, description: str):
        import re
        self.field = field
        self.regex = re.compile(pattern)
        self.description = description

    def check(self, content: dict[str, str]) -> tuple[bool, str | None]:
        import re
        value = content.get(self.field, "")
        if not self.regex.search(value):
            return False, f"Pole '{self.field}' nie pasuje do formatu: {self.description}"
        return True, None


class CrossReferenceChecker(QualityGateChecker):
    """check_type = 'cross_reference'"""
    def __init__(self, required_references: list[str]):
        self.required = required_references

    def check(self, content: dict[str, str]) -> tuple[bool, str | None]:
        full_text = " ".join(content.values()).lower()
        missing = [ref for ref in self.required if ref.lower() not in full_text]
        if missing:
            return False, f"Brakujące odniesienia: {', '.join(missing)}"
        return True, None
```

### 9.3 Dispatcher

```python
CHECKER_REGISTRY: dict[str, type[QualityGateChecker]] = {
    "min_length":      MinLengthChecker,
    "required_field":  RequiredFieldChecker,
    "format_match":    FormatMatchChecker,
    "cross_reference": CrossReferenceChecker,
    # "human_review" — brak automatu; zawsze needs_review
}

def run_quality_checks(
    gates: list[QualityGate],
    content: dict[str, str]
) -> dict[str, list[str]]:
    """
    Uruchamia wszystkie automated quality gates.
    Returns: {"passed": [...criteria], "failed": [...criteria], "warnings": [...criteria]}
    """
    result = {"passed": [], "failed": [], "warnings": []}
    for gate in gates:
        if not gate.automated:
            result["warnings"].append(f"[human_review] {gate.criterion}")
            continue
        checker_cls = CHECKER_REGISTRY.get(gate.check_type)
        if not checker_cls:
            continue
        passed, msg = checker_cls(**gate.checker_params).check(content)
        key = "passed" if passed else ("failed" if gate.severity == "blocking" else "warnings")
        result[key].append(gate.criterion if passed else f"{gate.criterion} — {msg}")
    return result
```

> `gate.checker_params` to opcjonalne pole do dodania w `QualityGate` (dict z kwargs dla checkera).

---

*Spec 17 rozwiązuje znaleziska: E-01 (async spec), E-04 (state machine), E-07 (algorytmy), J-06 (confidence threshold), oraz rozszerza WorkPackage dla scenariusza AI-first.*
