---
title: Change Impact Assessment
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Change Impact Assessment


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ocenić wpływ planowanej zmiany (produkt, architektura, proces, infrastruktura) na użytkowników, systemy, koszty, ryzyka i zgodność; określić zakres testów, komunikację, plan wdrożenia i kryteria akceptacji, aby zmiana była świadoma i kontrolowana.


## Zakres i granice

- Obejmuje: identyfikację interesariuszy, zależności systemowych, wpływ na SLA/UX/bezpieczeństwo, koszty i zasoby, plan testów i rollback, komunikację, harmonogram, kryteria wejścia/wyjścia, zgodność/regulacje.  
- Poza zakresem: szczegółowa realizacja techniczna (oddzielne plany), budżetowanie portfelowe.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: opis zmiany (RFC), backlog/ADR, architektura aktualna, lista systemów zależnych, wymagania biznesowe i zgodności, szacowanie ryzyka, plan release.  
- Wyjścia: arkusz oceny wpływu, mapa zależności, matryca ryzyk i kontroli, zakres testów/regresji, plan wdrożenia i rollback, plan komunikacji, checklisty DoR/DoD.


## Założenia

- CMDB i monitoring są aktualne.  
- Dostępne są środowiska testowe zbliżone do prod.  
- Interesariusze są dostępni do akceptacji i komunikacji.


## Otwarte pytania

- Jakie mierniki sukcesu zmiany (KPI) i horyzont obserwacji?  
- Czy potrzebne jest okno zwrotne (grace period) dla użytkowników?  
- Jak obsłużyć klientów/regulacje w innych regionach?  
- Jak wersjonować dokumentację zmian (linkage_index)?

## Powiązania (meta)

- Key Documents: change_management, risk_assessment, release_readiness_statement, rollback_runbook, service_dependency_map, security_assessment, compliance_architecture_review.  
- Key Document Structures: opis zmiany, wpływ, ryzyka/kontrola, testy, wdrożenie/rollback, komunikacja.  
- Document Dependencies: CMDB, monitoring, CI/CD, CAB proces, incident/problem records.


## Zależności dokumentu

Wymaga: aktualnej architektury i CMDB, listy interesariuszy, kryteriów SLA/UX, polityk bezpieczeństwa i zgodności, zasobów na testy, planu rollback. Braki = brak DoR.


## Fazy cyklu życia

- Scoping zmiany i identyfikacja wpływu.  
- Analiza ryzyk i kontroli.  
- Plan testów i wdrożenia (z rollbackiem).  
- Decyzja CAB/PO.  
- Wdrożenie, monitorowanie i walidacja.  
- Retrospektywa i aktualizacja procedur.



## Struktura sekcji (szkielet)
- Cel i zakres testów
- Założenia, ryzyka i priorytety
- Typy testów i macierz pokrycia
- Dane testowe i środowiska
- Scenariusze/skrpty testowe i automatyzacja
- Kryteria akceptacji/go-no-go
- Raportowanie defektów i wskaźniki jakości
- Plan regresji i utrzymania
## Szybkie powiązania

- linkage_index.jsonl (change/impact/assessment)  
- service_dependency_map, rollback_runbook, release_readiness_statement


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)

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

1. Wypełnij opis zmiany i mapę wpływu.  
2. Oceń ryzyka/kontrole, ustal testy i plan wdrożenia/rollback.  
3. Uzyskaj akceptacje (CAB/PO); poinformuj interesariuszy.  
4. Po wdrożeniu zweryfikuj metryki, zamknij DoD, zaktualizuj linkage_index.


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

- CAB: Change Advisory Board.  
- Kryteria stop: warunki, przy których wdrożenie jest zatrzymywane.  
- SLA/OLA: parametry usług i wewnętrzne umowy operacyjne.


## Przykłady użycia

- Zmiana schematu API wpływająca na aplikacje mobilne.  
- Migracja bazy danych do nowej wersji.  
- Włączenie nowej polityki bezpieczeństwa haseł.  
- Rebalans usług między regionami chmurowymi.


## Ryzyka i ograniczenia

- Niedoszacowany wpływ → awarie zależnych systemów.  
- Brak testów krytycznych ścieżek → regresje produkcyjne.  
- Słaba komunikacja → incydenty operacyjne i niezadowolenie klientów.  
- Niekompletny rollback → wydłużone przestoje.


## Decyzje i uzasadnienia

- Priorytet i okno serwisowe.  
- Zakres testów/regresji vs czas.  
- Kryteria stop/rollback i właściciele.  
- Akceptacja wyjątków zgodności/bezpieczeństwa.


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
- Formularz DPIA/PIA, DFD/transfer maps, tabela ryzyk/środków, decyzja/akceptacje, rejestr DPIA/ROP, umowy SCC/BCR/DPA, log waivers, plan wdrożenia środków.
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

## Powiązania sekcja↔sekcja

- Wpływ ↔ Ryzyka/kontrole ↔ Testy.  
- Zależności systemowe ↔ Plan wdrożenia ↔ Rollback.  
- Komunikacja ↔ Harmonogram ↔ Akceptacja interesariuszy.


## Struktura sekcji

1) Opis zmiany i cele  
2) Wpływ na użytkowników, SLA, bezpieczeństwo, zgodność  
3) Zależności i systemy dotknięte  
4) Ryzyka i środki kontrolne  
5) Zakres testów/regresji i dane testowe  
6) Plan wdrożenia i rollback (okno, kroki, kryteria stop)  
7) Komunikacja i akceptacje  
8) Kryteria akceptacji/DoR/DoD  
9) Otwarte pytania


## Wymagane rozwinięcia

- Macierz wpływu: system × wpływ (wys/śr/niski) + właściciel.  
- Plan testów: jakie testy (unit/integration/e2e/perf/sec) i kto wykonuje.  
- Wymagania zgodności i bezpieczeństwa oraz dowody.  
- Plan komunikacji: kogo, kiedy, jak informować; szablony.  
- Plan rollback: kroki, dane do backupu, punkty decyzji stop.


## Wymagane streszczenia

- Executive summary: cel zmiany, wpływ, ryzyko, decyzja.  
- Skrót harmonogramu i okna serwisowego.


## Guidance (skrót)

- Zawsze identyfikuj zależności w CMDB i mapie usług.  
- Włącz bezpieczeństwo/zgodność w ocenie wpływu; nie odkładaj.  
- Ustal jasne kryteria stop/rollback i odpowiedzialnych.  
- Testy dopasuj do wpływu; krytyczne ścieżki muszą mieć regresję.  
- Komunikuj wcześniej; potwierdzaj odbiór przez kluczowych użytkowników.  
- Dokumentuj decyzje CAB/PO wraz z uzasadnieniem.


## Checklisty Definition of Ready (DoR)

- [ ] Opis zmiany i cel biznesowy spisane.  
- [ ] Zidentyfikowane systemy zależne i właściciele.  
- [ ] Ocena ryzyka i wymagania zgodności gotowe.  
- [ ] Plan testów/regresji i dane dostępne.  
- [ ] Plan wdrożenia/rollback i komunikacji uzgodniony.


## Checklisty Definition of Done (DoD)

- [ ] Wdrożenie wykonane; testy i monitoring zielone.  
- [ ] Brak otwartych krytycznych incydentów po zmianie.  
- [ ] Dokumentacja wpływu, decyzji i dowodów uzupełniona.  
- [ ] Komunikaty wysłane; interesariusze potwierdzili.  
- [ ] linkage_index/CMDB zaktualizowane; retrospektywa zapisana.

