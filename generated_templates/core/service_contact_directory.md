---
title: Service Contact Directory
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Service Contact Directory


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zapewnić aktualny katalog kontaktów operacyjnych dla usług/systemów: on-call, właściciele, dostawcy, eskalacje.


## Zakres i granice

- Obejmuje: kontakty on-call (24/7), właścicieli usług, SME, eskalacje, dostawców i SLA, kanały komunikacji, strefy czasowe, procedurę aktualizacji.
- Poza zakresem: treść runbooków i kontraktów (linkowane), dane osobowe spoza kontekstu operacyjnego.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: wymagania, projekt/ADR, inwentarz systemów/danych, okna wdrożeniowe, zasoby.
- Wyjścia: plan wdrożenia, skrypty/konfiguracje, walidacja/testy, plan rollback, lista ryzyk i właścicieli.
## Założenia
- Zespoły architektury/ops/security dostępne do review.  
- Narzędzia CI/CD/monitoringu są dostępne.  
- Polityki bezpieczeństwa i PII obowiązują.
## Otwarte pytania
- Czy potrzebne są warianty architektury na różne rynki/regulacje?  
- Jakie limity kosztowe/skalowalności są akceptowalne?  
- Jakie są wymagania klientów na SLO/raportowanie?
## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie/migracja danych.
- Rollout (pilot → fala → pełne wdrożenie).
- Walidacja i smoke testy.
- Stabilizacja/monitoring i przekazanie do operacji.
## Struktura sekcji (szkielet)

- Zasady utrzymania i częstotliwość przeglądu
- Format/widok katalogu (tabela, filtrowanie po usłudze/roli/strefie)
- Kontakty on-call i eskalacje
- Kontakty właścicieli/SME
- Dostawcy i SLA + punkty kontaktu
- Kanały komunikacji i awaryjne obejścia
- Procedura aktualizacji i wersjonowania


## Szybkie powiązania

- Incident Management, Runbooki, CMDB, Supplier Management, BCP/DR, Security contacts.


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
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
- SLO/SLA: cele jakości/usługi i umowy na poziom usług.  
- ADR: zapis decyzji architektonicznych.  
- FinOps: praktyki kontroli kosztów w chmurze/usługach.
## Przykłady użycia
- Nowa usługa API B2B.  
- Modernizacja istniejącej usługi monolitu → mikroserwis.  
- Przygotowanie do audytu/DR testu.
## Ryzyka i ograniczenia
- Brak SLO → brak priorytetyzacji operacji.  
- Nieudokumentowane interfejsy → regresje i integracyjne błędy.  
- Niedoszacowany koszt → przekroczenia budżetu.
## Decyzje i uzasadnienia
- Wybór architektury (mono vs micro) ze względu na SLO/koszt.  
- Wersjonowanie API/eventów.  
- Poziom redundancji i DR vs budżet.
## Powiązania z innymi dokumentami
- architecture_decision_records — decyzje kluczowe.  
- observability_plan — monitoring i SLO.  
- dr_plan — odporność i testy.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne standardy architektury, bezpieczeństwa, PII, DR/BCP.  
- Branżowe regulacje, jeśli dotyczy (fin/health/public).
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

- [ ] Czy wszystkie ścieżki informacji są zamknięte (każde wejście ma wyjście)?
- [ ] Czy istnieją pętle lub sprzeczne relacje między sekcjami?
- [ ] Czy sekcje kluczowe mają wskazane źródła i odbiorców?
- [ ] Czy terminologia jest spójna z sekcją "Słownik pojęć"?

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- [Artefakt 1, np. diagram architektury] — [opis i relacja do tego dokumentu]
- [Artefakt 2, np. schemat bazy danych] — [opis i relacja do tego dokumentu]

## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Wejścia

- CMDB/inventory usług, listy zespołów, umowy z dostawcami, matryca eskalacji, polityki prywatności.


## Wyjścia

- Aktualny katalog kontaktów z atrybutami (rola, system, kanał, godziny, strefa, priorytet), wersjonowany i dostępny w trybie read-only dla operacji.



## Jak używać (checklista)

- Wyszukaj kontakt po usłudze/roli; sprawdź kanał i godzinę dostępności.
- W incydencie: stosuj matrycę eskalacji; dokumentuj próbę kontaktu.
- Aktualizuj wpisy wg procedury; oznacz wersję i datę przeglądu.


## Wymagane rozwinięcia / powiązania

- Tabela kontaktów (CSV/MD) z polami: usługa, rola, imię, kanał, strefa, godziny, priorytet, ostatnia weryfikacja; matryca eskalacji.


## Kryteria DoR

- Lista usług/zespołów i właścicieli; polityka prywatności/udostępniania danych kontaktowych.


## Kryteria DoD

- Katalog kompletny i opublikowany; daty przeglądu ustawione; proces aktualizacji działa.


## Artefakty

- Plik katalogu, matryca eskalacji, log zmian, linki do runbooków.


## Walidacja

- Przegląd próbki kontaktów (aktywny numer/kanał); test eskalacji; zgodność z polityką prywatności.


## Metryki

- % kontaktów zweryfikowanych w ostatnich 30/90 dniach.
- Liczba nieudanych prób kontaktu w incydentach.


## Utrzymanie

- Przegląd miesięczny/kwartalny; automatyczne przypomnienia; rotacja on-call.


## Zakończenie

Aktualny katalog kontaktów przyspiesza reakcję operacyjną; utrzymuj go zgodnie z matrycą eskalacji i polityką prywatności.
