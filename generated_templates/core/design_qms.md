---
title: Design QMS
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Design QMS (Quality Management System)


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaprojektować system zarządzania jakością (QMS): procesy, dokumenty, role, audyty i zgodność (np. ISO 9001), aby zapewnić spójność i ciągłe doskonalenie.


## Zakres i granice

- Obejmuje: politykę jakości, strukturę procesów/Procedur/OI, zarządzanie dokumentacją i wersjami, role i odpowiedzialności, szkolenia/kompetencje, audyty i niezgodności, CAPA, ryzyka i doskonalenie, integracje z innymi systemami (HSE, ISMS).  
- Poza zakresem: szczegółowe instrukcje operacyjne dla poszczególnych linii (oddzielne OI).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania norm (ISO 9001/branżowe), procesy organizacji, ryzyka, rejestry niezgodności, polityki pokrewne (HSE/ISMS), narzędzia QMS/EDMS.  
- Wyjścia: architektura QMS (mapa procesów, repo dokumentów), RACI, procedury/audyty, plan szkoleń, CAPA workflow, wskaźniki jakości, linki w linkage_index.



## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

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

- linkage_index.jsonl (quality/qms_design)  
- dokumentacja_regulaminu, audit_logging, change_management_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

### Polskie normy i regulacje
- **PN-EN-ISO-9001** — PN-EN ISO 9001:2015-10 — Systemy Zarządzania Jakością
- **PN-EN-ISO-IEC-20000-1** — PN-EN ISO/IEC 20000-1:2019 — Zarządzanie Usługami IT
- **PN-ISO/IEC-27001** — PN-ISO/IEC 27001:2023-09 — Systemy Zarządzania Bezpieczeństwem Informacji

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

1. Zdefiniuj politykę i mapę procesów; zbuduj repo dokumentów i wersjonowanie.  
2. Zaprojektuj audyty/NCR/CAPA, role i szkolenia; ustaw KPI i raportowanie.  
3. Dodaj do linkage_index i checklisty; utrzymuj aktualność przy audytach/zmianach.


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

- [ ] Dokumentacja wersjonowana i kontrolowana; audyty/NCR/CAPA mają workflow i właścicieli.  
- [ ] Szkolenia/kompetencje aktualne; KPI monitorowane; linkage_index uzupełniony.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Polityka jakości, mapa procesów, rejestr dokumentów/wersji, plan audytów, NCR/CAPA rejestry, matryca kompetencji, KPI dashboard, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Liczba otwartych NCR/CAPA, czas zamknięcia NCR/CAPA, pokrycie szkoleń %, aktualność dokumentów, zgodność audytów.

## Kryteria ukończenia

- [ ] QMS zaprojektowany (dokumentacja, audyty, CAPA, role, KPI) i osadzony w linkage_index.


## Struktura sekcji

1) Polityka jakości i zakres QMS  
2) Mapa procesów i dokumentacja (procedury, instrukcje, formularze; wersjonowanie, kontrola zmian)  
3) Role i kompetencje (RACI, szkolenia, rejestr kompetencji)  
4) Audyty i niezgodności (plan, checklisty, raporty, NCR, CAPA)  
5) Ryzyka i doskonalenie (risk register, działania doskonalące, przeglądy zarządzania)  
6) Integracje systemowe (HSE, ISMS, EDMS, dane/metryki)  
7) Wskaźniki jakości i raportowanie (KPI, cele, dashboardy)  
8) Załączniki (szablony procedur, checklisty audytów, ADR/waiver log)


## Wymagane rozwinięcia

- Rejestr dokumentów i wersjonowanie; kontrola dostępu/udostępniania.  
- Plan audytów wewnętrznych/zewnętrznych; NCR/CAPA workflow.  
- Szkolenia i kompetencje: matryca, terminy odświeżeń.  
- KPI jakości i cele; cykl przeglądów zarządzania.  
- Integracja z EDMS/QMS tool; powiązanie z risk register.


## Wymagane streszczenia

- Executive: zakres QMS, status audytów, NCR/CAPA, kluczowe KPI i ryzyka.


## Guidance (skrót)

- Traktuj dokumentację jako produkt: wersjonuj, audytuj dostęp, utrzymuj jedno źródło prawdy.  
- Audyty + CAPA muszą być zamykane z weryfikacją skuteczności.  
- Metryki jakości powiąż z celami biznesowymi; używaj przeglądów zarządzania do decyzji.  
- Aktualizuj linkage_index i rejestry przy każdej zmianie procedur.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania norm/branżowe zebrane; procesy zidentyfikowane; EDMS/QMS narzędzia dostępne.  
- [ ] Polityka jakości i właściciele procesów uzgodnieni.


## Checklisty Definition of Done (DoD)

- [ ] Architektura QMS, procedury, audyty/NCR/CAPA, role/szkolenia i KPI opisane; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Checklisty DoR/DoD odhaczone; szablony/artefakty załączone.

