# 10 — Estimation Engine Spec

**Status:** Draft v1.0  
**Powiązane dokumenty:** 09_semantic_mapper_spec, 05_module_interface_contracts, 11_work_planner_spec

---

## 1. Cel i zakres

Estimation Engine przekształca `MappingResult` w `EstimationReport` — ustrukturyzowany kosztorys projektu z przedziałami min/likely/max roboczogodzin, podziałem na fazy SDLC i uzasadnieniem podstaw dedukcji.

**Założenia modelu:**
- Jednostka: roboczogodziny (h) — nie koszty finansowe (to zadanie PM-a)
- Model statystyczny: punkty złożoności → h (nie LLM)
- Deterministyczny: te same dane wejściowe → ten sam raport
- Przejrzysty: każda cyfra ma udokumentowaną podstawę

---

## 2. Model punktów złożoności

### 2.1 Punkty bazowe per typ dokumentu

Typ dokumentu wywnioskowany z `doc_path` / `doc_title` przez proste reguły:

```python
DOCUMENT_TYPE_POINTS: dict[str, float] = {
    # Strategiczne / Architektury (złożone)
    "architecture":      8.0,
    "design":            6.0,
    "strategy":          6.0,
    "roadmap":           5.0,
    "requirements":      5.0,
    
    # Compliance / Audit (złożone, dużo treści)
    "audit":             8.0,
    "compliance":        7.0,
    "risk_assessment":   7.0,
    "policy":            5.0,
    "rodo":              6.0,
    "nis2":              6.0,
    
    # Techniczne standardowe
    "specification":     4.0,
    "procedure":         3.0,
    "runbook":           3.0,
    "test_plan":         4.0,
    "test_report":       3.0,
    
    # Lekkie
    "checklist":         1.5,
    "meeting_notes":     1.0,
    "status_report":     1.5,
    "changelog":         1.0,
    
    # Domyślne (nieznany typ)
    "default":           3.0,
}
```

### 2.2 Przelicznik punktów → godziny

```python
H_PER_POINT = 0.5    # 1 punkt złożoności = 0.5h pracy
                     # Konfigurowalne przez app_settings: "estimation_h_per_point"

# Przedziały (wariancja modelu: -30% / +50%)
def points_to_hours(points: float) -> tuple[float, float, float]:
    """Zwraca (h_min, h_likely, h_max)"""
    h_likely = points * H_PER_POINT
    h_min    = h_likely * 0.7   # -30% (prosta treść, szablon wypełniony)
    h_max    = h_likely * 1.5   # +50% (złożona treść, wiele iteracji)
    return (round(h_min, 1), round(h_likely, 1), round(h_max, 1))
```

### 2.3 Mnożniki modyfikujące punkty

```python
COMPLEXITY_MULTIPLIERS: dict[str, float] = {
    # Mnożnik bazowy
    "base":                1.0,
    
    # Mnożnik confidence — wyższy confidence = dokument bardziej potrzebny = standardowa wycena
    # Niski confidence = może nie być potrzebny = wycena discount
    "confidence_high":     1.0,     # confidence ≥ 0.8
    "confidence_medium":   0.9,     # confidence 0.6–0.79
    "confidence_low":      0.7,     # confidence 0.4–0.59 (poniżej progu domyślnego)
    
    # Mnożnik is_required — wymagane przez standard/regulację = +20%
    "required_by_standard": 1.2,
    
    # Mnożnik domeny projektu — niektóre domeny są bardziej złożone
    "domain_fintech":      1.3,     # regulacje + compliance + security
    "domain_healthcare":   1.4,     # 21 CFR, HIPAA, rygor
    "domain_government":   1.3,     # procedury, formalizm
    "domain_saas":         1.0,     # standardowy
    "domain_internal_tool":0.8,    # uproszczony
}
```

### 2.4 Algorytm wyceny

```python
def estimate_document(
    item: MappingItem,
    entities: ExtractedEntities,
    settings: EstimationSettings
) -> DocumentEstimate:
    
    # 1. Determine document type from path/title
    doc_type = _infer_doc_type(item.doc_title, item.doc_path)
    base_points = DOCUMENT_TYPE_POINTS.get(doc_type, DOCUMENT_TYPE_POINTS["default"])
    
    # 2. Confidence multiplier
    if item.confidence >= 0.8:
        conf_mult = COMPLEXITY_MULTIPLIERS["confidence_high"]
    elif item.confidence >= 0.6:
        conf_mult = COMPLEXITY_MULTIPLIERS["confidence_medium"]
    else:
        conf_mult = COMPLEXITY_MULTIPLIERS["confidence_low"]
    
    # 3. Required multiplier
    req_mult = COMPLEXITY_MULTIPLIERS["required_by_standard"] if item.is_required else 1.0
    
    # 4. Domain multiplier (z projektu)
    domain_mult = _domain_multiplier(entities.domains)
    
    # 5. Final points
    final_points = base_points * conf_mult * req_mult * domain_mult
    
    # 6. Convert to hours
    h_min, h_likely, h_max = points_to_hours(final_points)
    
    return DocumentEstimate(
        doc_uid=item.doc_uid,
        doc_title=item.doc_title,
        doc_path=item.doc_path,       # przekazywane z MappingItem
        phase_id=item.phase_id,        # przekazywane z MappingItem
        phase_name=item.phase_name,    # przekazywane z MappingItem
        is_required=item.is_required,  # przekazywane z MappingItem
        h_estimate=h_likely,
        h_likely=h_likely,             # alias dla czytelności w agregacjach
        h_min=h_min,
        h_max=h_max,
        doc_type=doc_type,
        base_points=base_points,
        final_points=round(final_points, 2),
    )
```

---

## 2.5 Specyfikacja _infer_doc_type i _domain_multiplier

```python
def _infer_doc_type(self, doc_title: str, doc_path: str | None) -> str:
    """
    Mapuje tytuł dokumentu na klucz z DOCUMENT_TYPE_POINTS.
    Algorytm: sprawdź czy dowolny klucz z DOCUMENT_TYPE_POINTS jest
    substringiem title.lower(). Kolejność priorytetu: od bardziej
    specyficznych do ogólnych.
    Fallback: 'default'.

    Przykłady:
    - "Plan audytu bezpieczeństwa" → "audit" (zawiera "audit")
    - "Functional Requirements Specification" → "specification" (zawiera "spec")
    - "Raport z wdrożenia" → "report" (zawiera "report")
    - "Nieznany dokument" → "default"
    """
    title_lower = doc_title.lower()
    path_str = (doc_path or "").lower()
    # Priorytetowa kolejność (bardziej specyficzne pierwsze)
    for key in ["audit", "specification", "architecture", "test", "report", "plan", "policy"]:
        if key in title_lower:
            return key
    return "default"


def _domain_multiplier(self, domains: list[str]) -> float:
    """
    Oblicza mnożnik dla zestawu domen.
    Algorytm: bierz MAX z mnożników per domena.
    Uzasadnienie: jeden projekt nie może należeć do dwóch domen jednocześnie;
    najsurowsza (droga) domena determinuje złożoność.

    Przykłady:
    - ["fintech"] → 1.3
    - ["healthcare"] → 1.4
    - ["fintech", "healthcare"] → max(1.3, 1.4) = 1.4 (NIE 1.3*1.4=1.82)
    - [] → 1.0 (brak domeny = domyślna złożoność)
    """
    if not domains:
        return 1.0
    multipliers = [DOMAIN_MULTIPLIERS.get(d, 1.0) for d in domains]
    return max(multipliers)
```

> **Uwaga:** `DOMAIN_MULTIPLIERS` mapuje nazwy domen na wartości z `COMPLEXITY_MULTIPLIERS`
> (sekcja 2.3): `{"fintech": 1.3, "healthcare": 1.4, "government": 1.3, "saas": 1.0, "internal_tool": 0.8}`.

---

## 3. Klasyfikacja złożoności projektu

```python
def classify_complexity(total_h_likely: float, total_docs: int) -> str:
    """
    Zwraca: "low" | "medium" | "high" | "critical"
    """
    if total_h_likely < 80 and total_docs < 30:
        return "low"
    elif total_h_likely < 250 and total_docs < 80:
        return "medium"
    elif total_h_likely < 600 and total_docs < 200:
        return "high"
    else:
        return "critical"
```

---

## 4. Organizacja po fazach i critical path

```python
def organize_by_phases(
    doc_estimates: list[DocumentEstimate],
    phases_order: list[Phase]   # 24 fazy z itdoc, posortowane wg ordinal
) -> list[PhaseEstimate]:
    
    phase_groups: dict[int, list[DocumentEstimate]] = defaultdict(list)
    for doc in doc_estimates:
        phase_groups[doc.phase_id].append(doc)
    
    result = []
    for phase in phases_order:
        if phase.phase_id not in phase_groups:
            continue
        
        docs = phase_groups[phase.phase_id]
        ph_h_min    = sum(d.h_min for d in docs)
        ph_h_likely = sum(d.h_likely for d in docs)
        ph_h_max    = sum(d.h_max for d in docs)
        
        # Critical path: fazy z wymaganymi dokumentami + fazy w sekwencji rytmu
        is_critical = any(d.is_required for d in docs) or phase.phase_id in CRITICAL_PHASES
        
        result.append(PhaseEstimate(
            phase_id=phase.phase_id,
            phase_name=phase.phase_name,
            doc_count=len(docs),
            h_min=round(ph_h_min, 1),
            h_likely=round(ph_h_likely, 1),
            h_max=round(ph_h_max, 1),
            is_critical_path=is_critical,
            documents=docs,
        ))
    
    return result

# Fazy zawsze na critical path (wymagane dla podstawowej spójności projektu)
CRITICAL_PHASES = {3, 4, 6, 7, 14, 20}
# 3=Architecture, 4=Design, 6=Development, 7=Integration, 14=Documentation, 20=Risk
# Wartości 1-based odpowiadające LLM phase_id.
```

---

## 5. Podstawy dedukcji (DeductionBasis)

Każdy raport zawiera czytelne uzasadnienie skąd wzięły się liczby:

```python
def build_deduction_basis(
    entities: ExtractedEntities,
    mapping: MappingResult,
    phase_estimates: list[PhaseEstimate],
) -> list[DeductionPoint]:
    
    basis = []
    
    # 1. Standard coverage
    if entities.standards:
        std_docs = sum(1 for item in mapping.items if any(
            s.startswith("standard:") for s in item.match_sources
        ))
        basis.append(DeductionPoint(
            type="standard_coverage",
            description=f"Standardy [{', '.join(entities.standards)}] wymagają "
                       f"{std_docs} szablonów dokumentów (mandatory coverage).",
            weight=0.35,
        ))
    
    # 2. Regulation overlap
    if entities.regulations:
        reg_docs = sum(1 for item in mapping.items if any(
            s.startswith("regulation:") for s in item.match_sources
        ))
        basis.append(DeductionPoint(
            type="regulation_overlap",
            description=f"Regulacje [{', '.join(entities.regulations)}] nakładają "
                       f"obowiązek {reg_docs} dokumentów compliance.",
            weight=0.25,
        ))
    
    # 3. Phase sequence
    critical_phases = [p for p in phase_estimates if p.is_critical_path]
    if critical_phases:
        phase_names = ", ".join(p.phase_name for p in critical_phases[:3])
        basis.append(DeductionPoint(
            type="phase_sequence",
            description=f"Fazy krytyczne ({phase_names}...) muszą być wykonane "
                       f"sekwencyjnie wg modelu SDLC — determinuje minimalny czas projektu.",
            weight=0.20,
        ))
    
    # 4. Domain complexity
    domain_mults = {d: _domain_multiplier([d]) for d in entities.domains}
    if any(m > 1.0 for m in domain_mults.values()):
        heavy_domains = [d for d, m in domain_mults.items() if m > 1.0]
        basis.append(DeductionPoint(
            type="domain_complexity",
            description=f"Domeny [{', '.join(heavy_domains)}] wymagają zwiększonego "
                       f"nakładu pracy (mnożnik {max(domain_mults.values()):.1f}x) "
                       f"ze względu na rygor regulacyjny.",
            weight=0.15,
        ))
    
    # 5. Confidence distribution
    low_conf = sum(1 for i in mapping.items if i.confidence < 0.7)
    if low_conf > 0:
        basis.append(DeductionPoint(
            type="uncertainty_buffer",
            description=f"{low_conf} dokumentów ma confidence < 0.7 — "
                       f"wycena zawiera bufor niepewności (+50% h_max).",
            weight=0.05,
        ))
    
    return basis
```

> **Uwaga o wagach:** Wagi punktów dedukcji (`weight`) są wartościami cząstkowymi 
> (nie sumują się do 1.0 gdy nie wszystkie warunki zachodzą). Podczas prezentacji 
> raportu PM lub klientowi należy je traktować jako *wskaźniki istotności*, 
> nie jako procenty. Implementacja może opcjonalnie normalizować wagi 
> (`w_i = w_i / sum(w_j)`) przed zwróceniem w `EstimationReport`.

---

## 6. Pełna klasa EstimationEngine

```python
class EstimationEngine:
    
    def __init__(self, itdoc_connector: ItdocConnector, settings: Settings):
        self._itdoc = itdoc_connector
        self._settings = settings
    
    async def generate_report(self, mapping_id: UUID) -> EstimationReport:
        """Alias calculate() z guardem statusu projektu — główny entry point."""
        # Guard: sprawdź status projektu przed generowaniem raportu
        project = await self._get_project_for_mapping(mapping_id)
        if project.status in ('archived', 'cancelled'):
            raise ProjectStatusError(
                f"Cannot generate estimation for project with status '{project.status}'"
            )
        mapping = await self._get_mapping(mapping_id)
        return await self.calculate(mapping)
    
    async def calculate(
        self,
        mapping: MappingResult,
        confidence_threshold: float = 0.6,
        include_phases: list[int] | None = None,
    ) -> EstimationReport:
        
        # 1. Pobierz fazy z itdoc
        all_phases = await self._itdoc.get_phases()
        
        # 2. Filtruj mapping items
        items = [i for i in mapping.items if i.confidence >= confidence_threshold]
        if include_phases:
            items = [i for i in items if i.phase_id in include_phases]
        
        if not items:
            raise InsufficientMappingError(
                f"Brak zmapowanych szablonów z confidence ≥ {confidence_threshold}"
            )
        
        # V-06: Limit dokumentów per raport
        # Konfigurowalny przez env WORKSHOP_MAX_DOCS_ESTIMATION (domyślnie 500)
        MAX_DOCS = int(os.getenv("WORKSHOP_MAX_DOCS_ESTIMATION", "500"))
        truncation_warning: str | None = None
        total_before_truncation = len(items)
        if len(items) > MAX_DOCS:
            # Sortuj wg confidence DESC przed truncation
            items = sorted(items, key=lambda i: i.confidence, reverse=True)[:MAX_DOCS]
            truncation_warning = (
                f"Report truncated: {total_before_truncation} documents found, "
                f"showing top {MAX_DOCS}"
            )
        
        # 3. Wycena per dokument
        doc_estimates = [
            self.estimate_document(item, mapping.extracted_entities, self._settings)
            for item in items
        ]
        
        # 4. Agregacja sumaryczna
        total_h_min    = sum(d.h_min    for d in doc_estimates)
        total_h_likely = sum(d.h_likely for d in doc_estimates)
        total_h_max    = sum(d.h_max    for d in doc_estimates)
        
        # 5. Organizacja po fazach
        phase_estimates = self.organize_by_phases(doc_estimates, all_phases)
        
        # 6. Klasyfikacja złożoności
        complexity = self.classify_complexity(total_h_likely, len(doc_estimates))
        
        # 7. Podstawy dedukcji
        deduction_basis = self.build_deduction_basis(
            mapping.extracted_entities, mapping, phase_estimates
        )
        
        return EstimationReport(
            mapping_id=mapping.id,
            project_id=mapping.project_id,   # przekazywane z MappingResult
            total_docs=len(doc_estimates),
            total_h_min=round(total_h_min, 1),
            total_h_likely=round(total_h_likely, 1),
            total_h_max=round(total_h_max, 1),
            complexity_level=complexity,
            by_phase=phase_estimates,
            deduction_basis=deduction_basis,
            truncation_warning=truncation_warning,  # None gdy brak truncation
            status="draft",
        )
```

---

## 7. Przykład raportu kosztorysowego

```
# Raport kosztorysowy — Projekt Fintech ABC S.A.
Generowany: 2026-03-11 11:30:00

## Podsumowanie
| Metryka            | Wartość    |
|--------------------|------------|
| Dokumenty łącznie  | 87         |
| Nakład (min)       | 183.0 h    |
| Nakład (likely)    | 261.0 h    |
| Nakład (max)       | 391.5 h    |
| Złożoność projektu | HIGH       |
| Fazy SDLC          | 9 aktywnych|

## Podział po fazach
| Faza              | Dokumenty | Min h | Likely h | Max h | Krytyczna |
|-------------------|-----------|-------|----------|-------|-----------|
| Architecture (3)  | 12        | 28.0  | 40.0     | 60.0  | ✓         |
| Development (5)   | 15        | 22.5  | 32.5     | 48.5  | ✓         |
| Security (13)     | 23        | 54.0  | 77.0     | 115.5 | ✓         |
| Compliance (19)   | 19        | 42.5  | 60.5     | 90.5  | ✓         |
| ...               | ...       | ...   | ...      | ...   | ...       |

## Podstawy dedukcji
1. [waga 35%] Standardy [PCI DSS, ISO/IEC 27001] wymagają 47 szablonów dokumentów.
2. [waga 25%] Regulacje [RODO, KSC] nakładają obowiązek 31 dokumentów compliance.
3. [waga 20%] Fazy krytyczne (Architecture, Security, Compliance) muszą być wykonane 
   sekwencyjnie wg modelu SDLC.
4. [waga 15%] Domeny [fintech] wymagają zwiększonego nakładu (mnożnik 1.3x).
5. [waga 5%]  12 dokumentów z confidence < 0.7 — bufor niepewności (+50% h_max).
```
---

## 8. Wyjątki

| Wyjątek | Kiedy rzucany | HTTP |
|---------|--------------|------|
| `InsufficientMappingError` | Brak zmapowanych szablonów z confidence ≥ threshold | 422 |
| `ProjectStatusError` | Projekt ma status `archived` lub `cancelled` | 409 |

```python
class ProjectStatusError(ValueError):
    """Rzucany gdy projekt ma status uniemożliwiający generowanie raportu."""
    pass
```

---

## 9. Pochodzenie i kalibracja mnożników

### 9.1 Źródło wartości baseline

Wartości w `DOCUMENT_TYPE_POINTS` i `COMPLEXITY_MULTIPLIERS` są **wstępnymi założeniami
eksperckimi**, nie danymi empirycznymi. Muszą być traktowane jako punkt startowy i kalibrowane
na podstawie rzeczywistych realizacji.

| Parametr | Wartość startowa | Uzasadnienie |
|----------|-----------------|--------------|
| `H_PER_POINT = 0.5` | 30 min/punkt | Szacunek: docs AI pisze 2× szybciej niż człowiek; człowiek = 1.0h/pkt |
| `architecture = 8.0 pkt` | 4h | Empirycznie: document architektury wymaga ~3-5h dla AI + review |
| `checklist = 1.5 pkt` | 45 min | Szablon + wypełnienie = ~30-60 min |
| `domain_healthcare = 1.4×` | +40% | Rygor 21 CFR, HIPAA, więcej walidacji i przeglądów |
| `domain_fintech = 1.3×` | +30% | Compliance regulacyjny (KSC, PSD2) + security documentation |

### 9.2 Mechanizm kalibracji (po wdrożeniu MVP)

System **nie uczy się automatycznie** w v1 — kalibracja jest manualna. Po zebraniu
danych z pierwszych 10+ projektów PM może zaktualizować wartości przez `app_settings`:

```python
# Nadpisanie globalne przez DB (tabela project_settings, klucz = h_per_point)
# Pierwsze projekty: loguj (doc_uid, estimated_h, actual_h) do tabeli actual_hours
# Po 10+ obserwacjach: oblicz avg_ratio = mean(actual/estimated) per doc_type
# Jeśli avg_ratio > 1.2 → zwiększ H_PER_POINT lub konkretny doc_type multiplier

# Przykład po kalibracji:
# Okazało się że 'architecture' w healthcare zajmuje ~7h nie 4h
# → doc_type_points["architecture"] = 14.0 (7h / 0.5 h_per_point)
```

### 9.3 Per-projekt override przez PM

```python
# Tabela project_settings (dok.04):
# klucz: "estimation_h_per_point"    wartość: "0.4"   → szybszy AI agent
# klucz: "domain_multiplier_override" wartość: "1.5"  → trudniejszy projekt
# klucz: "confidence_threshold"       wartość: "0.45" → bardziej liberalny próg

# EstimationEngine przy tworzeniu raportu sprawdza project_settings PRZED globalnymi:
settings_value = await db.get_project_setting(project_id, "estimation_h_per_point")
h_per_point = float(settings_value) if settings_value else H_PER_POINT
```
