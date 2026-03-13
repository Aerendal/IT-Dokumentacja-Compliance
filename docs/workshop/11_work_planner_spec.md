# 11 — Work Planner Spec

**Status:** Draft v1.0  
**Powiązane dokumenty:** 10_estimation_engine_spec, 12_itdoc_integration_spec, 05_module_interface_contracts

---

## 1. Cel i zakres

Work Planner to Side 4 — ostatni etap przepływu danych. Aktywuje się po akceptacji raportu kosztorysowego przez klienta. Przekształca zaakceptowany `EstimationReport` w szczegółowy `WorkPlan` złożony z listy `WorkPackage` — atomowych zadań gotowych do wykonania przez AI-agentów.

**Cel Work Planner:**
- Zdekompozycja 87 szablonów na sekwencję zadań z jednoznacznymi wejściami/wyjściami
- Ustalenie kolejności na podstawie `rhythm_edges` z biblioteki itdoc
- Przypisanie typów wykonawców (AI writer / AI reviewer / human)
- Zapewnienie że każdy task-unit ma jasno określone gate warunki wejścia

---

## 2. WorkPackage — model danych

```python
@dataclass
class WorkPackage:
    id:             UUID
    plan_id:        UUID
    doc_uid:        str            # UID szablonu z itdoc
    doc_title:      str
    phase_id:       int
    phase_name:     str
    sequence_order: int            # globalny porządek wykonania (1, 2, 3, ...)
    inputs_json:    list[str]      # co musi istnieć przed tym zadaniem
    outputs_json:   list[str]      # co zadanie dostarcza
    gates_json:     list[str]      # warunki wejścia (checklist)
    assignee_type:  str            # "ai_agent_writer" | "ai_agent_reviewer" | "human"
    h_estimate:     float | None   # z EstimationEngine
    status:         str            # Canonical enum — patrz §2.1 poniżej
    depends_on:     list[UUID]     # IDs poprzednich WorkPackage (UUID, nie doc_uid — patrz §2.2)
```

### 2.1 WorkPackageStatus — canonical enum

```python
class WorkPackageStatus(str, Enum):
    PENDING      = "pending"       # oczekuje na poprzedniki
    IN_PROGRESS  = "in_progress"   # w trakcie realizacji
    NEEDS_REVIEW = "needs_review"  # gotowe, czeka na akceptację (assumption_flag=True lub warning gate)
    BLOCKED      = "blocked"       # zatrzymane przez ClarificationRequest[required=True]
    DONE         = "done"          # zaakceptowane, quality gates przeszły
```

> Przejścia stanów i warunki: `17_ai_agent_context_spec.md` §4.

### 2.2 Konwersja `doc_uid` → `UUID` w `depends_on`

Wewnętrznie `_build_dependency_graph()` operuje na `doc_uid` (string), ale
`WorkPackage.depends_on` przechowuje `UUID` pakietów. Konwersja przez
`uid_to_package_id: dict[str, UUID]` budowany przy tworzeniu pakietów:

```python
# Budowany sekwencyjnie podczas pętli tworzenia pakietów:
uid_to_package_id: dict[str, UUID] = {}

# Po utworzeniu pakietu dla doc_uid:
uid_to_package_id[doc_uid] = pkg.id

# Konwersja podczas tworzenia:
depends_on_uids = deps.get(doc_uid, [])          # list[str] — doc_uids poprzedników
depends_on_ids  = [uid_to_package_id[u]           # list[UUID] — UUIDs pakietów
                   for u in depends_on_uids
                   if u in uid_to_package_id]     # guard: poprzednik już przetworzony
# Uwaga: "if u in uid_to_package_id" jest bezpieczne bo topologiczne sortowanie
# gwarantuje że poprzednik zawsze pojawia się wcześniej w ordered_pairs.
```

---

## 3. Algorytm sekwencjonowania

### Etap 1: Budowa grafu zależności

```python
async def _build_dependency_graph(
    self,
    doc_uids: list[str],
    connector: ItdocConnector
) -> dict[str, list[str]]:
    """
    Buduje graf: doc_uid → [doc_uids które muszą być przed nim]
    
    Źródła zależności (według priorytetu):
    1. rhythm_upstream() z it_doc_matrix.db — bezpośrednie zależności dokumentowe
    2. Kolejność faz SDLC — dokumenty fazy N mogą zacząć się dopiero po fazie N-1
    3. Reguły domenowe (hardcoded) — np. Requirements przed Architecture
    """
    
    deps: dict[str, list[str]] = {uid: [] for uid in doc_uids}
    doc_set = set(doc_uids)
    
    for uid in doc_uids:
        # Zapytaj o upstream (poprzedzające) w bibliotece itdoc
        upstream = await connector.rhythm_upstream(uid, depth=1)
        
        for upstream_doc in upstream:
            # Uwzględnij tylko zależności wewnątrz naszego zestawu dokumentów
            if upstream_doc.doc_uid in doc_set:
                deps[uid].append(upstream_doc.doc_uid)
    
    return deps
```

### Etap 2: Topologiczne sortowanie (Kahn's algorithm)

```python
def _topological_sort(
    self,
    doc_uids: list[str],
    deps: dict[str, list[str]]
) -> list[str]:
    """
    Sortowanie topologiczne z uwzględnieniem faz SDLC jako tiebreaker.
    Gwarantuje że dokument pojawia się po wszystkich swoich upstream.
    
    Jeśli istnieje cykl (rhythm_edges mogą mieć cykle) → przerwij cykl
    na krawędzi o najniższym weight (fallback: lexicographic).
    """
    
    in_degree = {uid: 0 for uid in doc_uids}
    for uid, prerequisites in deps.items():
        in_degree[uid] = len(prerequisites)
    
    # Kolejka: docs bez zależności, posortowane wg phase_id (ASC)
    queue = sorted(
        [uid for uid, degree in in_degree.items() if degree == 0],
        key=lambda uid: self._get_phase_id(uid)
    )
    
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current)
        
        # Znajdź dokumenty które mają current jako zależność
        for uid in doc_uids:
            if current in deps[uid]:
                in_degree[uid] -= 1
                if in_degree[uid] == 0:
                    # Wstaw posortowany wg fazy
                    _insert_sorted_by_phase(queue, uid, self._get_phase_id)
    
    # Obsługa cykli: pozostałe nieprzetworzone docs dodaj na koniec (wg fazy)
    remaining = [uid for uid in doc_uids if uid not in result]
    result.extend(sorted(remaining, key=lambda uid: self._get_phase_id(uid)))
    
    return result
```

### Etap 3: Wzbogacenie o kontrakty i RACI

```python
async def _enrich_with_contracts(
    self,
    doc_uid: str,
    connector: ItdocConnector,
    phase_id: int
) -> tuple[list[str], list[str], list[str]]:
    """
    Pobiera inputs/outputs/gates z itdoc contracts.
    Fallback jeśli contract = None (stub): generuj na podstawie fazy.
    """
    
    contract = await connector.get_contract(doc_uid)
    
    if contract and contract.inputs:
        inputs  = contract.inputs
        outputs = contract.outputs
        gates   = contract.gates
    else:
        # Fallback: reguły oparte na fazie SDLC
        contract_data = PHASE_DEFAULT_CONTRACTS.get(phase_id)
        if contract_data is None:
            # Faza nieznana — bezpieczny fallback
            inputs, outputs, gates = [], [], []
        else:
            inputs  = contract_data.get("inputs", [])
            outputs = contract_data.get("outputs", [])
            gates   = contract_data.get("gates", [])
    
    return inputs, outputs, gates


# Domyślne kontrakty per faza (gdy kontrakt w itdoc jest pusty)
# Klucze są 1-based (zgodne z LLM output). WorkPlanner.create_plan() konwertuje
# phase_id API (1-based) do phases.phase_id DB (0-based) przez `db_phase_id = api_phase_id - 1`.
PHASE_DEFAULT_CONTRACTS: dict[int, dict] = {
    1: {  # Phase 1 — Vision/Initiation
        "inputs": ["business_requirements", "stakeholder_brief"],
        "outputs": ["vision_document", "feasibility_study"],
        "gates": ["stakeholder_approval"]
    },
    2: {  # Phase 2 — Requirements
        "inputs": ["vision_document", "stakeholder_feedback"],
        "outputs": ["FRS", "NFR", "use_cases"],
        "gates": ["requirements_sign_off"]
    },
    3: {  # Phase 3 — Architecture
        "inputs": ["FRS", "NFR"],
        "outputs": ["architecture_document", "ADR", "tech_stack_decision"],
        "gates": ["architecture_review"]
    },
    4: {  # Phase 4 — Design
        "inputs": ["architecture_document"],
        "outputs": ["system_design", "database_schema", "API_design"],
        "gates": ["design_review"]
    },
    5: {  # Phase 5 — Planning
        "inputs": ["system_design"],
        "outputs": ["sprint_plan", "task_breakdown", "estimates"],
        "gates": ["planning_approval"]
    },
    6: {  # Phase 6 — Development/Coding
        "inputs": ["sprint_plan", "task_breakdown"],
        "outputs": ["source_code", "unit_tests", "code_review"],
        "gates": ["code_review_passed", "unit_tests_green"]
    },
    13: { # Phase 13 — Testing/QA
        "inputs": ["source_code", "test_plan"],
        "outputs": ["test_report", "bug_list", "QA_sign_off"],
        "gates": ["all_critical_bugs_fixed"]
    },
    19: { # Phase 19 — Deployment/Release
        "inputs": ["QA_sign_off", "deployment_plan"],
        "outputs": ["deployed_system", "deployment_report"],
        "gates": ["smoke_tests_passed"]
    },
    23: {  # Phase 23 — Maintenance
        "inputs": ["deployed_system"],
        "outputs": ["maintenance_log", "update_releases"],
        "gates": []
    },
    24: {  # Phase 24 — Retirement/Closure
        "inputs": ["maintenance_log", "closure_request"],
        "outputs": ["closure_report", "data_archival_plan"],
        "gates": ["stakeholder_sign_off"]
    },
}
# Nazwy faz są orientacyjne. Faktyczne nazwy: GET /health itdoc.phases lub tabela `phases` w it_doc_matrix.db.
# Fazy bez explicite kontraktu (7-12, 14-18, 20-22) używają fallbacku:
# inputs=[], outputs=[], gates=[]
```

### Etap 4: Przypisanie assignee_type

```python
ASSIGNEE_RULES: list[tuple[str, str]] = [
    # (pattern w doc_title lub doc_path, assignee_type)
    ("audit",               "human"),          # Audyty wymagają człowieka
    ("review",              "ai_agent_reviewer"),
    ("approval",            "human"),
    ("sign_off",            "human"),
    ("meeting",             "human"),
    ("interview",           "human"),
    ("architecture",        "human"),          # Architektura = decyzja człowieka
    ("strategy",            "human"),
    ("checklist",           "ai_agent_writer"),
    ("runbook",             "ai_agent_writer"),
    ("report",              "ai_agent_writer"),
    ("specification",       "ai_agent_writer"),
    ("procedure",           "ai_agent_writer"),
    ("policy",              "ai_agent_writer"),
    ("plan",                "ai_agent_writer"),
    ("log",                 "ai_agent_writer"),
    ("register",            "ai_agent_writer"),
    # Domyślne
    ("*",                   "ai_agent_writer"),
]

def _assign_assignee(self, doc_title: str, doc_path: str) -> str:
    text = f"{doc_title} {doc_path or ''}".lower()
    # doc_path może być None (brak kolumny 'path' w it_doc_matrix.db, patrz dok.12 §0)
    for pattern, assignee in ASSIGNEE_RULES:
        if pattern == "*" or pattern in text:
            return assignee
    return "ai_agent_writer"
```

---

## 4. Pełny algorytm WorkPlanner

```python
class WorkPlanner:
    
    def __init__(self, itdoc_connector: ItdocConnector, settings: Settings):
        self._itdoc = itdoc_connector
        self._settings = settings
    
    async def create_plan(self, report: EstimationReport) -> WorkPlan:
        """
        Cała operacja musi być wykonana w jednej transakcji bazodanowej:
        - BEGIN TRANSACTION przed pierwszym INSERT
        - COMMIT po ostatnim INSERT pakietów
        - ROLLBACK przy dowolnym błędzie

        ```python
        async def create_plan(self, report_id: UUID) -> WorkPlan:
            # V-01: Guard — sprawdź status projektu
            report = await self._get_report(report_id)
            project = await self._get_project(report.project_id)
            if project.status in ('archived', 'cancelled'):
                raise ProjectStatusError(
                    f"Cannot create work plan for project with status '{project.status}'"
                )

            async with db.transaction():  # atomowe — rollback przy błędzie
                # V-02: Archiwizuj poprzedni plan jeśli istnieje
                await db.execute("""
                    UPDATE work_plans 
                    SET status = 'archived', updated_at = NOW()
                    WHERE project_id = $1 AND status NOT IN ('archived')
                """, project.id)

                # Utwórz nowy plan
                plan = await db.insert(work_plans, {...})
                for pkg_data in packages:
                    await db.insert(work_packages, {...})
                return plan
        ```

        Kolumna `work_plans.status`: `active | archived` (dodaj do schematu jeśli nie istnieje).
        """
        
        # 0. Utwórz WorkPlan z nowym ID — plan_id musi istnieć przed tworzeniem pakietów
        plan_id = uuid4()
        
        # 1. Zbierz wszystkie doc_uid z raportu
        all_docs: list[DocumentEstimate] = []
        for phase in report.by_phase:
            all_docs.extend(phase.documents)
        
        doc_uids = [d.doc_uid for d in all_docs]
        # UWAGA: Jeden dokument może być zmapowany do wielu faz (document_phase_mapping).
        # Używamy composite key (doc_uid, phase_id) aby uniknąć nadpisywania duplikatów.
        # Klucz composite (doc_uid, phase_id) obsługuje dokumenty mapowane do wielu faz
        doc_map  = {(d.doc_uid, d.phase_id): d for d in all_docs}
        
        # 2. Zbuduj graf zależności (itdoc rhythm_upstream)
        # Budowanie listy tupli dla topological sort
        ordered_pairs_input: list[tuple[str, int]] = [(d.doc_uid, d.phase_id) for d in all_docs]
        deps = await self._build_dependency_graph(doc_uids)
        
        # 3. Topologiczne sortowanie na parach (doc_uid, phase_id)
        ordered_pairs = self._topological_sort_pairs(ordered_pairs_input, deps)
        
        # 4. Utwórz WorkPackage dla każdego dokumentu
        packages = []
        uid_to_package_id: dict[str, UUID] = {}
        
        for sequence_order, (doc_uid, phase_id) in enumerate(ordered_pairs, start=1):
            doc_est = doc_map.get((doc_uid, phase_id))
            
            inputs, outputs, gates = await self._enrich_with_contracts(
                doc_uid, self._itdoc, doc_est.phase_id
            )
            
            depends_on_uids = deps.get(doc_uid, [])
            depends_on_ids  = [uid_to_package_id[u] for u in depends_on_uids
                               if u in uid_to_package_id]
            
            pkg = WorkPackage(
                id=uuid4(),
                plan_id=plan_id,   # plan_id musi być przekazane do create_plan() przed tworzeniem pakietów
                doc_uid=doc_uid,
                doc_title=doc_est.doc_title,
                phase_id=doc_est.phase_id,
                phase_name=doc_est.phase_name,
                sequence_order=sequence_order,
                inputs_json=inputs,
                outputs_json=outputs,
                gates_json=gates,
                assignee_type=self._assign_assignee(doc_est.doc_title, doc_est.doc_path or ""),
                h_estimate=doc_est.h_estimate,   # h_estimate = h_likely z DocumentEstimate
                status="pending",
                depends_on=depends_on_ids,
            )
            
            packages.append(pkg)
            uid_to_package_id[doc_uid] = pkg.id
        
        return WorkPlan(
            report_id=report.id,
            project_id=report.project_id,
            total_packages=len(packages),
            status="draft",
            packages=packages,
        )
```

---

## 5. Format WorkPackage — przykład JSON

```json
{
  "id": "4a7f...",
  "plan_id": "2b3e...",
  "doc_uid": "42",
  "doc_title": "Plan audytu bezpieczeństwa",
  "phase_id": 13,
  "phase_name": "Security",
  "sequence_order": 34,
  "inputs_json": [
    "Polityka bezpieczeństwa informacji (zatwierdzona)",
    "Rejestr ryzyk (faza 20)",
    "Wyniki poprzednich audytów (jeśli dostępne)"
  ],
  "outputs_json": [
    "Plan audytu bezpieczeństwa (dokument)",
    "Lista kontrolna audytu",
    "Harmonogram audytu"
  ],
  "gates_json": [
    "Architekt bezpieczeństwa zatwierdził zakres audytu",
    "Dostępne wymagania regulacyjne (PCI DSS §12)",
    "Zespół audytorski zidentyfikowany"
  ],
  "assignee_type": "human",
  "h_estimate": 4.0,
  "status": "pending",
  "depends_on": ["3f9a...", "7c1b..."]
}
```

---

## 6. Widok Gantt (sekwencja faz)

Endpoint `GET /planning/{plan_id}/gantt` zwraca:

```markdown
# Plan pracy — Projekt Fintech ABC S.A.
Łączne pakiety: 87 | Fazy aktywne: 9

## Faza 3 — Architecture (12 pakietów)
| # | Dokument                     | Typ wykonawcy     | h    | Zależy od |
|---|------------------------------|-------------------|------|-----------|
| 3 | Diagram architektury systemu | human             | 5.0  | #1, #2    |
| 4 | ADR — wybór bazy danych      | human             | 3.5  | #3        |
| 5 | Specyfikacja API             | ai_agent_writer   | 2.0  | #4        |

## Faza 13 — Security (23 pakiety)
| # | Dokument                     | Typ wykonawcy     | h    | Zależy od |
|---|------------------------------|-------------------|------|-----------|
|34 | Plan audytu bezpieczeństwa   | human             | 4.0  | #3, #20   |
|35 | Polityka haseł               | ai_agent_writer   | 1.5  | #34       |
...

## Podsumowanie wg wykonawcy
| Typ                | Pakiety | Godziny |
|--------------------|---------|---------|
| ai_agent_writer    | 61      | 122.0   |
| ai_agent_reviewer  | 12      | 24.0    |
| human              | 14      | 115.0   |
| **RAZEM**          | **87**  | **261.0**|
```

---

## 7. Konfiguracja

```ini
# .env
RHYTHM_DEPTH_PLANNING=2        # głębokość ekspansji rhythm_upstream przy budowie grafu
ENABLE_PHASE_ORDERING=true     # wymuszaj kolejność faz SDLC jako tiebreaker
HUMAN_ASSIGNEE_PATTERNS=audit,approval,strategy,architecture,sign_off,interview
```

---

## 8. Sequencing Algorithm — szczegółowy opis

### 8.1 `_insert_sorted_by_phase(queue, uid, get_phase_fn)`

Stabilne wstawianie do kolejki z zachowaniem rosnącego `phase_id`:

```python
def _insert_sorted_by_phase(
    queue: list[str],
    uid: str,
    get_phase_fn: Callable[[str], int]
) -> None:
    """Wstaw uid do queue w miejscu gdzie phase_id jest >= phase_id(uid)."""
    target_phase = get_phase_fn(uid)
    for i, existing in enumerate(queue):
        if get_phase_fn(existing) > target_phase:
            queue.insert(i, uid)
            return
    queue.append(uid)  # największy phase_id → na końcu
```

### 8.2 Cycle Detection i Break Strategy

`rhythm_edges` mogą zawierać cykle. Algorytm Kahna naturalnie je wykrywa
przez `remaining = [uid for uid in doc_uids if uid not in result]`.

Gdy `remaining` niepuste po BFS → cykl istnieje. Strategia przerwania:

```python
def _break_cycles(
    self,
    remaining: list[str],
    deps: dict[str, list[str]],
    edge_weights: dict[tuple[str,str], float]  # (from_uid, to_uid) → weight
) -> dict[str, list[str]]:
    """
    Usuwa krawędź o najniższym weight z każdego cyklu.
    Fallback gdy weight nieznany: leksykograficznie (from_uid < to_uid).
    Zwraca zmodyfikowany deps bez krawędzi tworzących cykl.
    """
    modified_deps = {uid: list(prereqs) for uid, prereqs in deps.items()}

    for uid in remaining:
        cycle_edges = [
            (uid, prereq) for prereq in modified_deps[uid]
            if prereq in remaining
        ]
        if cycle_edges:
            # Wybierz krawędź do usunięcia: najniższy weight lub leksykograficznie
            weakest = min(
                cycle_edges,
                key=lambda e: (edge_weights.get(e, 1.0), e[1])
            )
            modified_deps[weakest[0]].remove(weakest[1])
            logger.warning(
                f"Cycle broken: removed edge {weakest[0]} → {weakest[1]} "
                f"(weight={edge_weights.get(weakest, 'unknown')})"
            )

    return modified_deps
```

Po `_break_cycles()` uruchom `_topological_sort()` ponownie — wynik będzie acykliczny.

### 8.3 Walidacja wyniku sortowania

```python
def _validate_sequence(
    self,
    ordered: list[str],
    deps: dict[str, list[str]]
) -> list[str]:
    """
    Weryfikuje że każdy prerequisite pojawia się przed swoim dependentem.
    Zwraca listę naruszeń (pary [prereq, dependent]) lub [] jeśli OK.
    """
    position = {uid: i for i, uid in enumerate(ordered)}
    violations = []
    for uid, prereqs in deps.items():
        for prereq in prereqs:
            if prereq in position and position[prereq] > position[uid]:
                violations.append(f"{prereq} powinien być przed {uid}")
    return violations
```

---

## 9. Edge Cases

### 9.1 Cycle w `WorkPackage.depends_on` (różne od cykli w rhythm_edges)

`rhythm_edges` definiuje zależności na poziomie dokumentów (itdoc). Ale `WorkPackage.depends_on`
jest budowane na podstawie `rhythm_upstream` — jeśli dane w `rhythm_edges` zawierają cykl A→B→A,
`_build_dependency_graph()` może go przejąć. `_break_cycles()` łamie najsłabszą krawędź i
loguje ostrzeżenie. **Implementacja `create_plan()` musi zawsze uruchamiać cycle detection
przed topological sort**, nawet gdy rhythm_edges jest pozornie acykliczne (dane mogą być
niespójne przy ręcznym wypełnieniu bazy).

```python
# Wymagany guard w create_plan() — PRZED topological sort:
deps = await self._build_dependency_graph(doc_uids)
deps = self._break_cycles(deps)          # zawsze, bez warunków
ordered = self._topological_sort(deps)
violations = self._validate_sequence(ordered, deps)
if violations:
    logger.error(f"Topological sort violations: {violations}")  # nie rzucaj — kontynuuj
```

### 9.2 Ostrzeżenie przy truncacji planu

Kiedy `SemanticMapper` zwraca mniej dopasowań niż żądano (np. limit 100 ale LLM przyciął output),
`WorkPlanner` tworzy plan z ograniczoną liczbą pakietów. Należy to zalogować wyraźnie:

```python
requested = len(report.all_documents_requested)   # ile klient chciał
received  = len(all_docs)                          # ile dotarło do WorkPlanner

if received < requested:
    logger.warning(
        f"WorkPlan truncated: klient oczekiwał {requested} dokumentów, "
        f"plan zawiera tylko {received}. "
        f"Sprawdź MappingResult i LLMResponse.finish_reason."
    )
    # Pole w WorkPlan: total_packages_requested = requested
    # Pozwala front-endowi pokazać ostrzeżenie użytkownikowi
```

Pole `WorkPlan.total_packages_requested: int | None` — `None` gdy nie znamy limitu,
`int` gdy znamy. Jeśli `total_packages_requested > total_packages` → truncation warning
dla front-endu.

---

## 10. Plan Invalidation — zmiana mappingu po akceptacji

### 10.1 Wybrana strategia: Rebuild z archiwizacją

Po analizie 3 wzorców (block, incremental, rebuild) wybrano **pełny rebuild z archiwizacją**
poprzedniego planu. Uzasadnienie: incremental update przy zmianie mappingu może zostawić
nieaktualny graf zależności; blokada edycji jest zbyt restrykcyjna dla PM.

### 10.2 Warunki triggera

| Akcja PM | Skutek dla WorkPlan |
|----------|---------------------|
| Zmiana confidence_threshold w zaakceptowanym raporcie | WorkPlan → `status="stale"`, powiadomienie PM |
| Ręczna korekta MappingItem (dodanie/usunięcie doc) | WorkPlan → `status="stale"` |
| Re-run mapowania dla istniejącego briefu | WorkPlan → `status="stale"` |
| Zmiana project_settings (mnożniki) | **Nie** invaliduje planu — tylko EstimationReport |

### 10.3 Algorytm rebuild

```python
async def rebuild_plan_if_stale(
    self,
    report_id: UUID,
    reason: str
) -> WorkPlan:
    """
    Wywoływane gdy MappingResult lub EstimationReport zmienił się po akceptacji.
    
    Strategia: archiwizuj stary plan → utwórz nowy.
    NIE usuwa poprzednich planów — zostają z status='stale' jako historia.
    """
    async with db.transaction():
        # 1. Oznacz istniejący plan jako stale
        await db.execute("""
            UPDATE work_plans
            SET status = 'stale',
                stale_reason = $2,
                updated_at = NOW()
            WHERE report_id = $1 AND status NOT IN ('stale', 'archived')
        """, report_id, reason)

        # 2. Pobierz świeży raport i zbuduj nowy plan
        fresh_report = await self._get_report(report_id)
        new_plan = await self.create_plan(fresh_report)

        # 3. Aktywuj nowy plan
        await db.execute("""
            UPDATE work_plans SET status = 'active' WHERE id = $1
        """, new_plan.id)

    return new_plan
```

### 10.4 Statusy WorkPlan

| Status | Znaczenie |
|--------|-----------|
| `draft` | Właśnie utworzony, przed akceptacją przez PM |
| `active` | Zaakceptowany, trwa praca |
| `stale` | Zastąpiony przez nowszy (mapping zmieniony) — tylko do historii |
| `archived` | Manualnie zarchiwizowany przez PM |
