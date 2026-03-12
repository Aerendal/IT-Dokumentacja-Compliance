---
title: Zgodność lotów dronów z przepisami
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Zgodność lotów dronów z przepisami


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zapewnić zgodność operacji dronów z przepisami (np. EASA/FAA/U‑Space), politykami bezpieczeństwa i prywatności.


## Zakres i granice

- Obejmuje: kategorie operacji (otwarta/szczególna/certyfikowana), rejestracja UAV/pilotów, uprawnienia i szkolenia, geofencing/NOTAM, plan lotu i zgody, identyfikacja zdalna, ubezpieczenie, logi lotów, prywatność/nagrania, checklisty przed/po locie, inspekcje, raportowanie incydentów.
- Poza zakresem: szczegółowe SOP misji technicznych (oddzielne dokumenty), serwis sprzętu (linkowane).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: rejestr czynności przetwarzania, klasyfikacja danych, cele przetwarzania, podstawy prawne, polityka retencji, wymagania bezpieczeństwa, lista podmiotów przetwarzających, procedury DSAR, plan reagowania na naruszenia.  
- Wyjścia: plan ochrony prywatności, checklisty privacy by design/DPIA, zasady retencji/anonimizacji, procedury DSAR i incydentów, linki w linkage_index.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Key Documents: privacy_policy, data_classification, incident_response_playbook, audit_logging, logging_strategy, design_bezpieczenstwa_api, procedury_reagowania_na_nieautoryzowany_dostep.  
- Key Document Structures: dane/cele, podstawy prawne/zgody, privacy by design/DPIA, retencja/anonimizacja, bezpieczeństwo, prawa podmiotów, incydenty.  
- Document Dependencies: IdP/IAM, data catalog, ROPA, ticketing DSAR, SIEM.
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)

- Klasyfikacja operacji i wymagania
- Rejestracja UAV/pilotów i uprawnienia
- Planowanie lotu: zgody, NOTAM, geozone, pogoda
- Identyfikacja zdalna i ubezpieczenie
- Checklisty przed/po locie, logi i raporty incydentów
- Prywatność/nagrania i retencja danych
- Szkolenia i recertyfikacja
- Audyt i inspekcje


## Szybkie powiązania

- Plan misji dronów, Data pipeline z dronów, Security/Safety, Insurance, Privacy/RODO.


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
- Rejestr danych/ROPA, DPIA, polityka retencji/anonimizacji, szablony DSAR, procedura naruszeń, logi audytu, ADR/waiver log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- SLA DSAR, liczba naruszeń i czas zgłoszenia, % danych z retencją/anonimizacją, liczba wyjątków od minimalizacji, audyt pass rate.
## Kryteria ukończenia
- [ ] Ochrona prywatności obywateli wdrożona (minimalizacja, DPIA, retencja, DSAR, bezpieczeństwo, naruszenia) i powiązana w linkage_index.
## Wejścia

- Aktualne przepisy (lokalne/UE/FAA), mapa przestrzeni, uprawnienia pilotów, specyfikacje dronów, polityka prywatności, ubezpieczenie.


## Wyjścia

- Procedury zgodności, checklisty, rejestry (piloci/UAV/loty), plan szkoleń, matryca uprawnień, instrukcje raportowania incydentów.



## Jak używać (checklista)

- Określ kategorię operacji; sprawdź uprawnienia pilota i rejestr UAV.
- Sprawdź NOTAM/geozony/pogodę; zaplanuj zgodnie z wymogami; odnotuj ubezpieczenie.
- Wykonaj checklisty pre/post-flight, loguj lot; zgłaszaj incydenty.
- Aktualizuj rejestry i szkolenia zgodnie z wymaganiami.


## Wymagane rozwinięcia / powiązania

- Checklisty pre/post-flight, wzory logów, matryca uprawnień, procedura zgłoszeń incydentów, polityka prywatności nagrań.


## Kryteria DoR

- Aktualne przepisy i geozony dostępne; lista UAV i pilotów z uprawnieniami.


## Kryteria DoD

- Procedury i checklisty zatwierdzone; rejestry prowadzone; piloci przeszkoleni.


## Artefakty

- Rejestry (UAV/pilotów/lotów), checklisty, dowody ubezpieczenia, raporty incydentów.


## Walidacja

- Audyt zgodności (dokumentacja + sample lotów), weryfikacja uprawnień i logów, test procedur zgłoszeń.


## Metryki

- Liczba lotów z pełną dokumentacją, incydenty/odchylenia, czas od zgłoszenia do zamknięcia, zgodność szkoleń.


## Utrzymanie

- Przegląd regulacyjny kwartalny; aktualizacja checklist po zmianach; recertyfikacja pilotów.


## Zakończenie

Dokument zapewnia zgodność operacji dronów; utrzymuj go wraz z aktualizacją przepisów i floty.
