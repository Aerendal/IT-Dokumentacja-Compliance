# 01 — Vision & Scope: AI Documentation Workshop

**Status:** Draft v1.0  
**Powiązane dokumenty:** 02_system_state_description, 03_architecture_overview  
**Zasada nadrzędna:** Biblioteka `itdoc` (szablony + kod) pozostaje bez zmian — warsztat działa obok, nie wewnątrz.

---

## 1. Cel systemu

**AI Documentation Workshop** (dalej: _Warsztat_) to zestaw niezależnych mikroserwisów zbudowanych obok istniejącej biblioteki `itdoc`. Celem jest zamknięcie luki między:

- **stanem obecnym:** biblioteka 7 941 szablonów z grafem wiedzy (standardy, regulacje, fazy SDLC, zależności)
- **potrzebą:** narzędzie, które na wejściu przyjmuje brief klienta, a na wyjściu dostarcza:
  - mapę potrzebnych dokumentów i ich kolejność
  - kosztorys pracy (min/likely/max)
  - plan pracy dla AI-agentów gotowy do wykonania

Warsztat działa jak **zespół inżynierów analitycznych** przed rozpoczęciem projektu: zbiera dane wejściowe, dedukcją ustala zakres, szacuje nakład, dostarcza raport decyzyjny.

---

## 2. Persony użytkowników

### P1 — AI Agent (główny konsument)
- Wywołuje endpointy REST API Warsztatu (POST brief, GET report, GET work_plan)
- Oczekuje danych strukturalnych (JSON) gotowych do dalszego przetworzenia
- Nie ma dostępu do bazy `it_doc_matrix.db` bezpośrednio
- Przykład: agent Claude/GPT-4 pracujący nad projektem klienta

### P2 — Project Manager / Analityk
- Wgrywa brief klienta przez API lub narzędzie CLI
- Czyta raporty kosztorysowe i podejmuje decyzje go/no-go
- Akceptuje scope → uruchamia planowanie pracy (Side 4)
- Oczekuje czytelnych raportów Markdown/JSON

### P3 — Inżynier ds. wiedzy (Knowledge Engineer)
- Dodaje nowe szablony przez Side 1 (Ingestion)
- Wgrywa specyfikacje z oficjalnych źródeł (ISO, NIST, OWASP, etc.)
- Sprawdza jakość zmapowanych szablonów i korekty confidence scoring

### P4 — Klient końcowy
- Nie ma bezpośredniego dostępu do systemu
- Otrzymuje raport kosztorysowy wygenerowany przez Side 3
- Podejmuje decyzję akceptacji/odrzucenia zakresu

---

## 3. Use Cases

### UC-01: Analiza briefu klienta
```
Aktor: P1 (AI Agent) lub P2 (PM)
Wejście: plik briefu (.txt/.md/.pdf/.docx)
Kroki:
  1. Wgraj brief → POST /brief/upload
  2. Uruchom mapowanie → POST /brief/{id}/map
  3. Pobierz wyniki → GET /brief/{id}/mapping
Wyjście: MappingResult (lista szablonów + confidence + uzasadnienie)
```

### UC-02: Generowanie kosztorysu
```
Aktor: P2 (PM)
Wejście: MappingResult z UC-01
Kroki:
  1. Żądaj raportu → POST /reports/estimate/{brief_id}
  2. Pobierz raport → GET /reports/{report_id}
Wyjście: EstimationReport (min/likely/max h, fazy SDLC, podstawy dedukcji)
```

### UC-03: Planowanie pracy po akceptacji
```
Aktor: P1 (AI Agent)
Wejście: report_id (po akceptacji klienta)
Kroki:
  1. Zainicjuj plan → POST /planning/create/{report_id}
  2. Pobierz work packages → GET /planning/{plan_id}/packages
Wyjście: lista WorkPackage (task-units, kolejność, assignee, gates)
```

### UC-04: Ingestia nowych szablonów
```
Aktor: P3 (Knowledge Engineer)
Wejście: spec z oficjalnego źródła (tekst lub URL)
Kroki:
  1. Prześlij spec → POST /ingestion/spec
  2. Przejrzyj propozycję szablonu → GET /ingestion/{job_id}
  3. Zatwierdź lub odrzuć → POST /ingestion/{job_id}/approve
Wyjście: nowy szablon zapisany w katalogu (nie w it_doc_matrix.db)
```

### UC-05: Konfiguracja dostawcy LLM
```
Aktor: P3 lub DevOps
Wejście: zmienne środowiskowe (.env)
Kroki: ustaw LLM_PROVIDER=openai|anthropic|ollama + klucze API
Wyjście: Warsztat używa skonfigurowanego dostawcy dla wszystkich operacji LLM
```

---

## 4. Granice systemu

### W zakresie (In Scope)
- REST API FastAPI z 4 routerami jako niezależnymi modułami
- Parsowanie briefów klientów: `.txt`, `.md`, `.pdf`, `.docx`
- Semantyczne mapowanie treści briefu na szablony z biblioteki `itdoc`
- Generowanie raportów kosztorysowych z uzasadnieniem
- Planowanie pracy dla AI-agentów w formacie WorkPackage JSON
- Ingestia nowych szablonów ze specyfikacji zewnętrznych
- Persystencja stanu w PostgreSQL (projekty, mapowania, raporty, plany)
- Konfigurowalna abstrakcja LLM (OpenAI, Anthropic, Ollama)
- Uruchomienie lokalne przez Docker Compose

### Poza zakresem (Out of Scope)
- ❌ Modyfikowanie istniejących szablonów w `generated_templates/`
- ❌ Modyfikowanie kodu biblioteki `itdoc` (`itdoc/*.py`)
- ❌ Zapis do bazy `it_doc_matrix.db`
- ❌ Wykonywanie pracy dokumentacyjnej (Warsztat tylko planuje, nie pisze)
- ❌ UI webowy (API-first; UI może być zbudowany osobno)
- ❌ Zarządzanie użytkownikami / wielodostęp (v1: single-tenant)
- ❌ Integracja z systemami zewnętrznymi (Jira, Confluence, GitHub Issues)
- ❌ Szacowanie kosztów finansowych (tylko nakład pracy w roboczogodzinach)

---

## 5. Metryki sukcesu

| Metryka | Cel v1 |
|---------|--------|
| Czas od uploadu briefu do MappingResult | < 30 s (przy GPT-4o) |
| Precision mapowania (ocena manualna próbki) | ≥ 75% trafnych mapowań przy confidence ≥ 0.7 |
| Pokrycie faz SDLC w raporcie kosztorysowym | 100% faz z ≥ 1 dokumentem |
| Czas generowania WorkPackage plan | < 10 s (operacja DB-only) |
| Dostępność API | 99% w środowisku lokalnym (Docker) |
| Czas ingestii nowego szablonu | < 60 s |

---

## 6. Założenia projektowe

1. **itdoc jako read-only oracle:** Warsztat pyta bibliotekę o wiedzę (`find_by_standard`, `rhythm_upstream`, `get_contract`) ale nigdy jej nie modyfikuje.
2. **LLM jest opcjonalny dla Side 1 i Side 4:** Ingestia i planowanie mogą działać bez LLM (rule-based fallback); LLM wymagany dla Side 2 (mapowanie semantyczne).

   **LLM-free fallback mode (gdy `LLM_PROVIDER=none` lub LLM niedostępny):**
   - Side 1 (Ingestion): szablony ingestowane przez parsowanie nazw plików + reguły regex bez LLM ✅
   - Side 2 (Mapping): **tryb keyword-only** — pomija ekstrakcję encji przez LLM, przechodzi
     od razu do L4 (keyword fallback) + L5 (phase fallback) z `spec09 §11`. Jakość mapowania
     spada do ~40-50% (brak rozpoznania standardów/regulacji). Wynik MappingResult dostaje
     `status="llm_free"` — front-end powinien pokazać ostrzeżenie.
   - Side 3 (Estimation): nie używa LLM — działa normalnie ✅
   - Side 4 (Planning): nie używa LLM — działa normalnie ✅

   Konfiguracja: `LLM_PROVIDER=none` lub `LLM_ENABLED=false` → SemanticMapper używa
   `_extract_keywords_without_llm()` (spec07 §11.4) zamiast `llm_adapter.extract_entities()`.
3. **Brief to niestrukturyzowany tekst:** System musi działać z niedoskonałymi, nieformalnymi briefami — nie wymaga ustrukturyzowanego wejścia od klienta.
4. **PostgreSQL jako single source of truth:** Stan projektów, sesji, mapowań i raportów jest w `workshop.db` (PostgreSQL), nie w plikach.
5. **Atomowość operacji:** Każdy z 4 mikroserwisów może działać niezależnie — awaria jednego nie blokuje pozostałych.

---

## 7. Ryzyka i ograniczenia v1

| Ryzyko | Mitygacja |
|--------|-----------|
| Niskie precision mapowania dla niszowych briefów | Confidence score + możliwość ręcznej korekty przez P3 |
| Koszt API LLM przy dużych briefach | Chunking + cache wyników LLM w PostgreSQL |
| Drift między biblioteką itdoc a schematem Warsztatu | Integration Spec (dok. 12) definiuje stabilny interfejs read-only |
| Brak obsługi języków innych niż polski | v1 działa w PL; EN jako rozszerzenie v2 |
