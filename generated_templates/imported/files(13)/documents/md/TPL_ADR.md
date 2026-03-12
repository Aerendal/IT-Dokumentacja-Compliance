---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Architecture Decision Records
**Architecture Decision Records** (ADR)

##  Metadane dokumentu

| Pole | Wartość |
|------|---------|
| **Kod** | `ADR` |
| **Kategoria** | Architektura |
| **Faza główna** | Projekt / Design |
| **Wersja** | 1.0.0 |
| **Status** | DRAFT |
| **Data utworzenia** | 2026-01-30 |
| **Autor** | [Imię Nazwisko] |
| **Recenzent** | [Imię Nazwisko] |
| **Zatwierdzający** | [Imię Nazwisko] |
| **Typowa długość** | 1-3 stron |

##  Opis

Uzasadnione decyzje architektoniczne z kontekstem, opcjami i konsekwencjami (format MADR).

##  Cykl życia dokumentu

| Trigger | Warunek | Opis |
|---------|---------|------|
| `CREATED_WHEN` | architectural_decision_made → Faza DESIGN | Tworzony przy każdej decyzji |
| `DEPRECATED_WHEN` | decision_superseded → ADR | Przestarzały gdy zastąpiony |
| `SUPERSEDED_BY` | new_adr_accepted → ADR | Zastępowany nowym ADR |
| `VALID_FROM` | decision_accepted | Ważny od akceptacji decyzji |

##  Obowiązywanie w fazach projektu

| Faza | Wymagalność | Akcja | Uwagi |
|------|-------------|-------|-------|
| 3. Projekt / Design | Obowiązkowy | CREATE | Dokumentacja decyzji architektonicznych |
| 5. Implementacja | Zalecany | CREATE | Nowe ADR przy decyzjach implementacyjnych |
| 9. Operacje / Maintenance | Zalecany | CREATE | ADR przy zmianach operacyjnych |
| 22. Change Management | Zalecany | CREATE | ADR przy major changes |

##  Powiązania z innymi dokumentami

### Dokumenty wejściowe (od których zależy)

| Dokument | Relacja | Obowiązkowy | Opis |
|----------|---------|-------------|------|
| [ADL] Architecture Decision Log | Produkuje |  | ADR produkuje wpisy do Architecture Decision Log |

### Dokumenty wyjściowe (które od tego zależą)

| Dokument | Relacja | Obowiązkowy | Opis |
|----------|---------|-------------|------|
| [TDD] Technical Design Document | Rozszerza |  | ADR-y dokumentują decyzje z TDD |

##  Struktura dokumentu

### 1. Tytuł *(wymagana)*

Krótki tytuł decyzji w formie stwierdzenia lub pytania.

**Wskazówki:** Użyj formatu: "[context] [decision]" np. "Wybór bazy danych dla modułu użytkowników"

**Przykład:**
```
ADR-001: Wybór PostgreSQL jako głównej bazy danych
```

### 2. Status *(wymagana)*

Aktualny status ADR.

**Wskazówki:** Dopuszczalne wartości: proposed, accepted, deprecated, superseded

**Przykład:**
```
Status: accepted
```

### 3. Kontekst *(wymagana)*

Opis sytuacji i problemu wymagającego decyzji.

**Wskazówki:** Opisz siły (forces) wpływające na decyzję, ograniczenia techniczne i biznesowe.

**Przykład:**
```
System wymaga przechowywania danych użytkowników z wymaganiami ACID...
```

### 4. Decyzja *(wymagana)*

Podjęta decyzja w formie jasnego stwierdzenia.

**Wskazówki:** Zacznij od "Decydujemy, że..." lub "Wybieramy..."

**Przykład:**
```
Decydujemy, że użyjemy PostgreSQL 15+ jako głównej bazy danych.
```

### 5. Rozważane opcje *(wymagana)*

Lista rozważanych alternatyw.

**Wskazówki:** Wymień 2-5 realnych opcji które były brane pod uwagę.

**Przykład:**
```
1. PostgreSQL\n2. MySQL 8\n3. MongoDB\n4. CockroachDB
```

### 6. Analiza opcji *(opcjonalna)*

Szczegółowa analiza każdej opcji.

**Wskazówki:** Dla każdej opcji opisz pros/cons w kontekście wymagań.

**Przykład:**
```
### PostgreSQL\n- Pros: ACID, JSON support, mature\n- Cons: Horizontal scaling complexity
```

### 7. Konsekwencje *(wymagana)*

Pozytywne i negatywne skutki decyzji.

**Wskazówki:** Rozdziel na "Dobre" i "Złe" konsekwencje.

**Przykład:**
```
**Dobre:**\n- Pełne wsparcie transakcji\n**Złe:**\n- Wymaga DBA dla skalowania
```

### 8. Odnośniki *(opcjonalna)*

Linki do powiązanych dokumentów i zasobów.

**Wskazówki:** Dodaj linki do RFC, TDD, zewnętrznych benchmarków.

**Przykład:**
```
- RFC-003: Database Selection Criteria\n- PostgreSQL vs MySQL Benchmark 2024
```

##  Historia zmian

| Wersja | Data | Autor | Opis zmian |
|--------|------|-------|------------|
| 1.0.0 | 2026-01-30 | [Autor] | Wersja inicjalna |

##  Zatwierdzenia

| Rola | Osoba | Data | Podpis |
|------|-------|------|--------|
| Autor | | | |
| Recenzent | | | |
| Zatwierdzający | | | |
