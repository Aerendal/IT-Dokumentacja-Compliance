---
title: ELN Integration Design
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# ELN Integration Design


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaprojektować integrację z Electronic Lab Notebook (ELN): przepływy danych, interfejsy, bezpieczeństwo/prywatność, zgodność (GLP/GMP/21 CFR Part 11), wersjonowanie i audyt.


## Zakres i granice

- Obejmuje: dane eksperymentów/wyników/pliki/metadane, interfejsy API/SDK/import-export (formaty, wersjonowanie), bezpieczeństwo (PII/IP, szyfrowanie, IAM), podpisy elektroniczne/audyt/traceability, GLP/GMP/21 CFR Part 11 zgodność, synchronizację i konflikt resolution/locking, observability (logi/statusy/alerty), role/uprawnienia.  
- Poza zakresem: implementacja ELN core (dostarczana przez vendor) – opisujemy integrację.


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: wymagania R&D/QA, schemat danych ELN, API/SDK docs, polityki bezpieczeństwa/PII/IP, wymagania Part 11/GLP/GMP, istniejące systemy LIMS/SDMS/DMS, przepływy podpisów i audyt.  
- Wyjścia: projekt integracji (interfejsy, formaty, mapowanie danych), wymagania bezpieczeństwa/PII/IP, plan podpisów/audytu, strategia sync/locking/konfliktów, monitorowanie i alerty, RACI i plan wdrożenia/testów.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: data_governance_requirements, data_privacy_assessment, 21_cfr_part_11_compliance, glp_gmp_guidelines, security_requirements, integration_architecture, api_design_specification, logging_and_audit_trail.
- Key Document Structures: dane, interfejsy, bezpieczeństwo/compliance, sync/locking, observability, role.
- Document Dependencies: ELN API/SDK, LIMS/SDMS/DMS, IAM/IdP, KMS, audit trail, ticketing/monitoring.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery: doprecyzowanie problemu, warianty.
- Design: wybór wariantu, decyzje, model danych, integracje.
- Review: security/compliance/architecture board, koszty, performance.
- Implementation & Test: odbiór spełnienia projektu.
- Rollout & Ops: migracja, monitoring, zarządzanie zmianą.
## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania

- linkage_index.jsonl (eln/integration_design)
- data_governance_requirements, data_privacy_assessment, 21_cfr_part_11_compliance, glp_gmp_guidelines, security_requirements, integration_architecture, api_design_specification, logging_and_audit_trail


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.

## Standardy i compliance


Lista standardów i wymagań regulacyjnych mających zastosowanie do tego dokumentu.
Uzupełnij na podstawie sekcji "Mające zastosowanie standardy i normy" oraz tabeli `doc_standard_mapping`.

- Standard / norma: [kod i nazwa]
- Wymaganie regulacyjne: [kod i treść]
- Polityka wewnętrzna: [nazwa polityki]


## RACI i role


Macierz RACI (Responsible / Accountable / Consulted / Informed) dla działań związanych z tym dokumentem.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie | [rola]      | [rola]      | [rola]    | [rola]   |
| Przegląd  | [rola]      | [rola]      | [rola]    | [rola]   |
| Aktualizacja | [rola]   | [rola]      | [rola]    | [rola]   |
| Archiwizacja | [rola]   | [rola]      | [rola]    | [rola]   |

## Jak używać dokumentu

1. Opisz dane/interfejsy i mapowanie; dodaj bezpieczeństwo/Part 11.  
2. Zdefiniuj sync/locking i observability; przygotuj testy/QA/UAT.  
3. Zapisz ryzyka/waivery; zaktualizuj linkage_index/checklisty.


## Checklisty jakości

### Kompletność
- **Kryterium:** Wszystkie wymagane sekcje i pola są wypełnione
- **Metryka:** Odsetek wypełnionych sekcji do wymaganych
- **Próg OK:** 90%
- **Narzędzie:** template_auditor.py, checklist_atomic.jsonl

### Dokładność
- **Kryterium:** Informacje są poprawne merytorycznie i aktualne
- **Metryka:** Przegląd ekspercki; data ostatniej aktualizacji
- **Próg OK:** Przegląd co 3 mies.
- **Narzędzie:** regulation_updater.py

### Spójność
- **Kryterium:** Terminologia i struktura są spójne w całej bibliotece
- **Metryka:** Liczba niespójności terminologicznych i strukturalnych
- **Próg OK:** 0 niespójności
- **Narzędzie:** bulk_section_patcher.py

### Śledzalność
- **Kryterium:** Każda sekcja ma źródło (standard, regulacja, decyzja)
- **Metryka:** Odsetek sekcji z wypełnionymi standards_refs
- **Próg OK:** 80%
- **Narzędzie:** impact_analyzer.py

### Aktualność
- **Kryterium:** Dokument jest aktualny względem obowiązujących regulacji
- **Metryka:** Czas od ostatniej aktualizacji vs. częstotliwość przeglądów
- **Próg OK:** < 6 mies.
- **Narzędzie:** changelog_tracker.py

### Użyteczność
- **Kryterium:** Użytkownik końcowy może efektywnie wypełnić dokument na podstawie guidance
- **Metryka:** Ocena guidance (score z template_auditor); feedback użytkowników
- **Próg OK:** Score >= 70
- **Narzędzie:** template_auditor.py

## Definicje robocze

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

## Weryfikacja spójności

- [ ] Zgodność Part 11/GLP/GMP opisana; dane i bezpieczeństwo spójne; sync/locking zdefiniowane.  
- [ ] Monitoring/alerty działają; testy/QA/UAT zaplanowane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Schematy/formaty, payload samples, mapping, test cases, audit trail config, e‑sign policy, monitoring dashboards, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- SLA sync, liczba konfliktów/failed sync, czas rozwiązania, zgodność z Part 11 (brak findings), pokrycie testów walidacyjnych.

## Kryteria ukończenia

- [ ] Integracja zaprojektowana, bezpieczeństwo i zgodność potwierdzone, testy przygotowane; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres danych i systemów (ELN + integracje LIMS/SDMS/DMS)  
2) Interfejsy i formaty (API/SDK/import/export, wersjonowanie, schematy)  
3) Bezpieczeństwo i zgodność (PII/IP, szyfrowanie, IAM, e‑sign, audit trail, GLP/GMP/21 CFR 11)  
4) Synchronizacja i konflikt resolution (locking, wersje, retry/backoff)  
5) Observability (logi, statusy sync, alerty błędów, dashboardy)  
6) Role i uprawnienia (RBAC/ABAC, SoD, podpisy)  
7) Plan wdrożenia i testów (dry-run, walidacja Part 11/QA, UAT)  
8) Ryzyka i waivery (sunset/kompensacje)  
9) Załączniki (schematy danych, przykłady payloadów, mapping, test cases, RACI)


## Wymagane rozwinięcia

- Mapowanie danych (źródło→ELN) i transformacje; schematy/formaty; wersjonowanie.  
- Polityki podpisów elektronicznych i audit trail (Part 11); walidacja i logi.  
- Locking i rozwiązywanie konfliktów (merge rules, precedence); retry/backoff.  
- Monitoring: SLA sync, alerty błędów, log retention; testy walidacyjne.


## Wymagane streszczenia

- Executive: zakres integracji, status Part 11/GLP/GMP, ryzyka (PII/IP/sync), plan wdrożenia/testów.


## Guidance (skrót)

- Zapewnij traceability: kto/co/kiedy — podpisy i audit trail obowiązkowe.  
- Minimalizuj PII/IP w payloadach; szyfruj in transit/at rest; kontroluj klucze.  
- Projektuj na konflikt: locking + deterministic merge; loguj każdą zmianę.  
- Waliduj zgodność Part 11 i GLP/GMP; dokumentuj testy i wyjątki.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania R&D/QA, API/SDK, schematy danych, polityki bezpieczeństwa/Part 11 dostępne.  
- [ ] Ownerzy integracji i środowiska testowe wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Mapowanie danych, interfejsy, bezpieczeństwo/Part 11, sync/locking i observability opisane; testy/QA/UAT zaplanowane/wykonane; dokument w linkage_index; metadane aktualne.

