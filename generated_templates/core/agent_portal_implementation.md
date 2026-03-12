---
title: Agent Portal Implementation
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Agent Portal Implementation


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Opisać wdrożenie portalu agenta (obsługa klienta/sprzedaż), zapewniając funkcjonalność, bezpieczeństwo, wydajność i integracje z systemami back-office.


## Zakres i granice

- Obejmuje: funkcje (CRM/tickets/order/billing/knowledge), role i uprawnienia, UI/UX, integracje (CRM, billing, fulfillment, telephony/CCaaS), bezpieczeństwo (IAM, PII, audyt), wydajność/SLO, dostępność (a11y), raportowanie, rollout i szkolenia.
- Poza zakresem: szczegółowa konfiguracja systemów zewnętrznych (opisywana w ich dokumentach).


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: wymagania biznesowe i procesy agentów, systemy źródłowe, polityki PII/RODO, SLO, standardy UI/a11y, przepływy telephony/chat, backlog funkcji.
- Wyjścia: projekt i plan wdrożenia portalu, matryca ról/uprawnień, integracje i kontrakty API, plan bezpieczeństwa/testów, plan rollout/szkoleń, KPI (AHT, FCR, NPS), runbook operacyjny.


## Założenia

- [Założenie 1]
- [Założenie 2]


## Otwarte pytania

- [Pytanie 1]
- [Pytanie 2]


## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: systemy CRM/billing/fulfillment/telephony, polityki PII, standardy UI/a11y, SLO, IAM, katalog usług, incident/runbook; brak – odnotuj.


## Fazy cyklu życia

Discovery → Design → Implementacja → Testy (func/sec/perf/a11y/UAT) → Rollout → Operacje.



## Struktura sekcji (szkielet)

- Wymagania i przypadki użycia agentów.
- Role i uprawnienia, IAM, audyt.
- Architektura i integracje (API/event/ETL, telephony/CCaaS).
- Bezpieczeństwo i prywatność (PII, szyfrowanie, logi, RODO).
- UI/UX i dostępność (WCAG), performance i SLO.
- Raportowanie/KPI (AHT, FCR, NPS, backlog status).
- Rollout i szkolenia (pilotaż, fazy, materiały).
- Operacje/runbook (monitoring, incident, change, backup).
- Ryzyka i mitigacje.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)
- **UŚUDE-PL** — Ustawa o Świadczeniu Usług Drogą Elektroniczną

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

- Zbierz wymagania, zaprojektuj integracje i bezpieczeństwo, przygotuj rollout i szkolenia; testuj; uruchom; monitoruj KPI.


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

- [Termin 1]
- [Termin 2]
- [Termin 3]


## Przykłady użycia

- [Przykład 1]
- [Przykład 2]


## Ryzyka i ograniczenia

- [Ryzyko 1]
- [Ryzyko 2]


## Decyzje i uzasadnienia

- [Decyzja 1]
- [Decyzja 2]


## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód]
- [Dokument Z → Sekcja W] — [powód]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1]
- [Standard 2]


## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ]
- [Sekcja C] -> [Sekcja D] : [typ]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ]
- [Dokument C] -> [Dokument D] : [typ]


## Ścieżki informacji

- [Wejście] → [Źródło] → [Rozwinięcie] → [Wyjście]
- [Wejście] → [Źródło] → [Streszczenie] → [Wyjście]


## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane

- [Artefakt 1]
- [Artefakt 2]


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji

1. Autor przygotowuje wersję roboczą i przeprowadza samorecenzję.
2. Recenzent techniczny (Tech Lead / BA) weryfikuje merytorycznie.
3. Właściciel procesu zatwierdza treść i zakres.
4. PM / Scrum Master aktualizuje metadata (wersja, data, status).
5. Dokument trafia do repozytorium i jest linkowany w Szybkie powiązania.

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Funkcje → integracje; role → IAM; PII → bezpieczeństwo/a11y; KPI → rollout i szkolenia.


## Wymagane rozwinięcia

- Integracje → kontrakty API i schematy danych.
- Bezpieczeństwo → szczegóły PII/audytu.
- UI/a11y → komponenty i guideline.


## Wymagane streszczenia

- One-pager: funkcje, integracje, role, KPI, rollout.


## Guidance

Cel: funkcjonalny i bezpieczny portal agenta. DoR: wymagania, systemy, polityki PII/a11y, SLO. DoD: architektura/integracje/bezpieczeństwo/UI/KPI/rollout opisane; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Wymagania procesów; [ ] Systemy źródłowe i polityki PII/a11y; [ ] SLO/KPI.
- DoD: [ ] Architektura/integracje/IAM/bezpieczeństwo/UI/KPI/rollout opisane; [ ] Testy zaplanowane; [ ] Sekcje N/A uzasadnione; metadane aktualne.

