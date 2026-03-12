---
title: Security Vision Statement
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Vision Statement


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować wizję bezpieczeństwa: kierunek, filary, KPI, horyzonty oraz ramy governance, aby wszystkie inicjatywy bezpieczeństwa były spójne i mierzalne.


## Zakres i granice

- Obejmuje: diagnozę stanu, cele/KPI, filary i inicjatywy, horyzonty czasowe, zależności, ryzyka, governance i mierzenie postępu.
- Poza zakresem: szczegółowa implementacja inicjatyw (opisana w planach wykonawczych/roadmapach produktowych).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: wizja, analizy rynku/konkurencji, benchmarki, ograniczenia regulacyjne/techniczne, oczekiwania interesariuszy.
- Wyjścia: mapa celów i KPI, portfel inicjatyw/filarów, roadmapa horyzontów, zasady governance/finansowania.
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
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Diagnoza i cele.
- Projekt filarów i inicjatyw.
- Plan wdrożenia i finansowania.
- Monitorowanie i rewizje okresowe.
## Struktura sekcji (szkielet)

- Streszczenie i wizja
- Diagnoza stanu i kontekst
- Cele i KPI (ambicja + targety)
- Filar/priorytety i inicjatywy
- Horyzonty/roadmapa i zależności
- Ryzyka i założenia
- Governance, finansowanie i raportowanie


## Szybkie powiązania
- testing-vision-statement
- sre-vision-statement
- project-vision-statement
- product-vision-statement
- pipeline-vision-statement

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

- Wypisz diagnozę i cele, następnie zmapuj filary i inicjatywy na horyzonty.
- Dodaj KPI z targetami oraz powiąż je z dashboardami/źródłami danych.
- Uzupełnij governance (fora, częstotliwość, właściciele) i podlinkuj w `reports/checklist_atomic.jsonl`.


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

- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania]
- [Dokument Z → Sekcja W] — [powód powiązania]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło]
- [Pojęcie 2] — [definicja i źródło]
- [Pojęcie 3] — [definicja i źródło]


## Wymagane odwołania do standardów

- [Standard 1] — [sekcja/fragment, którego dotyczy]
- [Standard 2] — [sekcja/fragment, którego dotyczy]


## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji]
- [Sekcja C] -> [Sekcja D] : [typ relacji]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]


## Ścieżki informacji

- [Wejście] → [Sekcja źródłowa] → [Sekcja rozwinięcia] → [Wyjście]
- [Wejście] → [Sekcja źródłowa] → [Sekcja streszczenia] → [Wyjście]


## Weryfikacja spójności

- [ ] Czy wszystkie ścieżki informacji są zamknięte?
- [ ] Czy istnieją pętle lub sprzeczne relacje?
- [ ] Czy sekcje krytyczne mają wskazane źródła i rozwinięcia?


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań (np. wzajemne wykluczanie)?
- [ ] Czy relacje cross‑doc mają uzasadnienie i są zgodne z fazą?
- [ ] Czy relacje wymagają rozwinięć lub streszczeń są odnotowane?


## Artefakty powiązane

- [Artefakt 1] — [opis i relacja do dokumentu]
- [Artefakt 2] — [opis i relacja do dokumentu]


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji

- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]


## Metryki jakości

- [Metryka 1] — [cel / próg]
- [Metryka 2] — [cel / próg]


## Kryteria ukończenia

- [ ] Kryterium 1 — [opis]
- [ ] Kryterium 2 — [opis]


## Wejścia

- Analizy stanu bezpieczeństwa, audyty, incydenty, benchmarki rynkowe.
- Ograniczenia regulacyjne/techniczne, apetyt na ryzyko, strategia firmy.
- Wymagania interesariuszy, budżet i zasoby.


## Wyjścia

- Statement wizji i filarów.
- Mapa celów i KPI z targetami/horyzontami.
- Portfel inicjatyw przypisany do filarów.
- Zasady governance, finansowania i raportowania postępów.



## Szybkie powiązania (uzupełnij)

- security_strategy.md
- security_roadmap.md
- security_policy_design.md
- risk_management_framework.md
- security_status_report.md


## Wymagane rozwinięcia / streszczenia

- Roadmapa (T1/T2/T3) z zależnościami i finansowaniem.
- Macierz priorytetów (wpływ × łatwość) dla inicjatyw.
- One-pager dla sponsorów: zakres, KPI, plan, data przeglądu.


## Wymagane powiązania

- Strategia korporacyjna/produktowa, apetyt na ryzyko.
- Rejestr ryzyk, program zgodności (compliance).
- Kluczowe inicjatywy w portfolio i ich właściciele.


## Kryteria DoR

- [ ] Diagnoza stanu i ograniczenia potwierdzone.
- [ ] Interesariusze i apetyt na ryzyko uzgodnione.
- [ ] Wstępne KPI i filary zebrane.
- [ ] Horyzonty i ograniczenia budżetowe znane.


## Kryteria DoD

- [ ] Wizja, filary i KPI opisane z targetami.
- [ ] Roadmapa/horyzonty oraz zależności wpisane.
- [ ] Governance, role i cykl raportowania określone.
- [ ] Artefakty podlinkowane, metadane i checklisty zaktualizowane.


## Artefakty do załączenia

- One-pager wizji i slajdy dla leadership.
- Mapa KPI i dashboard/źródła.
- Portfel inicjatyw + priorytetyzacja.
- Harmonogram przeglądów/gate’ów.


## Walidacja / testy

- Peer review z kluczowymi interesariuszami (produkt, risk, compliance).
- Sprawdzenie spójności KPI z dostępnymi źródłami danych.


## Metryki monitorowane

- Postęp inicjatyw per filar (green/amber/red).
- Realizacja KPI vs target w horyzontach T1/T2/T3.
- % inicjatyw z finansowaniem i właścicielem.
- Liczba krytycznych ryzyk bez planu mitygacji.


## Utrzymanie i aktualizacje

- Przegląd co kwartał lub po istotnych zmianach strategii/ryzyka.
- Synchronizuj z roadmapą produktową i budżetem.


## Zakończenie

Po spełnieniu DoD opublikuj wizję, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i ustaw cykl przeglądów.
- [Decyzja 1 — uzasadnienie]
- [Decyzja 2 — uzasadnienie]


## Monitoring i utrzymanie

- [Co monitorujemy] — [narzędzie / częstotliwość]
- [Kto utrzymuje] — [rola]


## Kontrola zmian

- [Zmiana] — [powód] — [data] — [akceptacja]


## Wymogi prawne i regulacyjne

- [Wymóg 1] — [źródło / akt prawny / standard]
- [Wymóg 2] — [źródło / akt prawny / standard]


## Zasady bezpieczeństwa informacji

- [Zasada 1] — [opis i wpływ na dokument]
- [Zasada 2] — [opis i wpływ na dokument]


## Ochrona danych i prywatność

- [Wymaganie 1] — [opis i sekcja docelowa]
- [Wymaganie 2] — [opis i sekcja docelowa]


## Wersjonowanie treści

- [Wersja] — [zmiana] — [autor] — [data]
- [Wersja] — [zmiana] — [autor] — [data]


## Historia zmian sekcji

- [Sekcja] — [zmiana] — [data]
- [Sekcja] — [zmiana] — [data]


## Wymagane aktualizacje

- [Sekcja] — [powód aktualizacji] — [termin]
- [Sekcja] — [powód aktualizacji] — [termin]


## Integracje i interfejsy

- [System / API] — [zakres integracji] — [wymagania]
- [System / API] — [zakres integracji] — [wymagania]


## Wymagania danych

- [Dane wejściowe] — [format] — [walidacja]
- [Dane wyjściowe] — [format] — [walidacja]


## Logowanie i audyt

- [Zdarzenie] — [poziom] — [retencja]
- [Zdarzenie] — [poziom] — [retencja]


## Utrzymanie i operacje

- [Procedura] — [cel] — [częstotliwość]
- [Procedura] — [cel] — [częstotliwość]


## KPI i SLA

- [KPI] — [cel] — [pomiar]
- [SLA] — [cel] — [pomiar]


## Scenariusze awaryjne

- [Scenariusz] — [objawy] — [reakcja]
- [Scenariusz] — [objawy] — [reakcja]


## Wpływ na inne systemy

- [System] — [rodzaj wpływu] — [ryzyko]
- [System] — [rodzaj wpływu] — [ryzyko]


## Zależności danych między systemami

- [Źródło danych] → [Odbiorca] — [opis]
- [Źródło danych] → [Odbiorca] — [opis]


## Harmonogram przeglądów

- [Obszar] — [częstotliwość] — [właściciel]
- [Obszar] — [częstotliwość] — [właściciel]


## Wymagania wydajnościowe

- [Wymaganie] — [metryka] — [próg]
- [Wymaganie] — [metryka] — [próg]


## Wymagania dostępnościowe

- [Wymaganie] — [SLA] — [metoda pomiaru]
- [Wymaganie] — [SLA] — [metoda pomiaru]


## Wymagania skalowalności

- [Wymaganie] — [cel] — [warunki]
- [Wymaganie] — [cel] — [warunki]


## Wymagania dostępności danych

- [Dane] — [częstotliwość dostępu] — [SLA]
- [Dane] — [częstotliwość dostępu] — [SLA]


## Retencja i archiwizacja

- [Dane] — [retencja] — [archiwizacja]
- [Dane] — [retencja] — [archiwizacja]


## Dostępność w sytuacjach awaryjnych

- [Scenariusz] — [zachowanie] — [priorytet]
- [Scenariusz] — [zachowanie] — [priorytet]


## Testy i weryfikacja

- [Test] — [cel] — [wynik oczekiwany]
- [Test] — [cel] — [wynik oczekiwany]


## Walidacja zgodności

- [Wymóg] — [metoda weryfikacji]
- [Wymóg] — [metoda weryfikacji]


## Audyty i przeglądy

- [Audyty] — [częstotliwość] — [odpowiedzialny]
- [Audyty] — [częstotliwość] — [odpowiedzialny]
