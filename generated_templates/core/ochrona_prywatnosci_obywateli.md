---
title: Ochrona prywatności obywateli
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Ochrona prywatności obywateli


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić prywatność danych obywateli w usługach publicznych/cyfrowych, zgodnie z regulacjami i zasadami etyki (RODO itp.).


## Zakres i granice

- Obejmuje: kategorie danych/PII i minimalizację, podstawy prawne i zgody, privacy by design i DPIA, pseudonimizację/anonimizację, retencję i prawa podmiotów danych, bezpieczeństwo (szyfrowanie/dostęp/audyt/segmentacja/third-party), obsługę praw (DSAR), monitoring incydentów i zgłoszenia organom.  
- Poza zakresem: polityka cookies i marketing automation (osobne dokumenty).


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
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (privacy/citizen_data_protection)  
- privacy_policy, incident_response_playbook, procedury_reagowania_na_nieautoryzowany_dostep


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **ISO/IEC 27701** — Zarządzanie Informacjami o Prywatności (PIMS)

### Polskie normy i regulacje
- **CYBERSEC-STRATEGIA-PL** — Strategia Cyberbezpieczeństwa RP 2019-2024 (aktualizacja 2025+)
- **MC-INTEROP-PL** — Wytyczne Ministerstwa Cyfryzacji dot. interoperacyjności systemów publicznych
- **PZP-PL** — Prawo Zamówień Publicznych
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)

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

1. Skataloguj dane/cele i podstawy prawne; uruchom DPIA i minimalizację.  
2. Ustal retencję/anonimizację i środki bezpieczeństwa; wdroż DSAR proces.  
3. Przygotuj procedurę naruszeń; zaktualizuj linkage_index i checklisty.


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

- [ ] Dane i cele zminimalizowane; podstawy prawne opisane.  
- [ ] Retencja/anonimizacja egzekwowana; DSAR działa w SLA.  
- [ ] Szyfrowanie/RBAC/audyt aktywne; procedura naruszeń gotowa; linkage_index uzupełniony.


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


## Struktura sekcji

1) Zakres danych i minimalizacja (kategorie, wrażliwe, cele, ograniczenie celu)  
2) Podstawy prawne i zgody (informowanie, zgody, rejestrowanie, withdrawal)  
3) Privacy by design i DPIA (analiza ryzyka, pseudonimizacja/anonimizacja, domyślne prywatne, retencja)  
4) Bezpieczeństwo danych (szyfrowanie in transit/at rest, dostęp/RBAC/SoD, audyt, segmentacja, third-party risk)  
5) Prawa podmiotów danych (dostęp/sprostowanie/usunięcie/ograniczenie/przenoszenie/sprzeciw; SLA/kanaly)  
6) Monitoring i incydenty (detekcja wycieków, procedura naruszeń, zgłoszenia do organów/klientów)  
7) Załączniki (checklisty DPIA, szablony DSAR, rejestr retencji, ADR/waiver log)


## Wymagane rozwinięcia

- Rejestr kategorii danych/PII i celów; mapa przepływów danych.  
- Szablon DPIA i progi, kiedy wymagane; lista środków minimalizacji.  
- Polityka retencji i anonimizacji; harmonogram kasowania.  
- Procedura DSAR (kanały, SLA, weryfikacja tożsamości, logowanie żądań).  
- Procedura naruszeń (czas detekcji/zgłoszenia, kogo informować, szablony).


## Wymagane streszczenia

- Executive: zakres danych, podstawy prawne, status DPIA/retencji, główne ryzyka i plan mitigacji.


## Guidance (skrót)

- Minimalizuj dane i cel; domyślnie prywatne ustawienia.  
- Szyfruj, pseudonimizuj, trzymaj RBAC i audyt; ogranicz third-party access.  
- Zawsze prowadź DPIA, gdy ryzyko wysokie; egzekwuj retencję i anonimizację.  
- DSAR i naruszenia muszą mieć SLA i szablony komunikacji; loguj wszystko.


## Checklisty Definition of Ready (DoR)

- [ ] Rejestr danych/ROPA dostępny; podstawy prawne zidentyfikowane.  
- [ ] Kanały DSAR i polityka retencji/anonimizacji znane; narzędzia bezpieczeństwa dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Plan ochrony prywatności opisany; DPIA/retencja/DSAR i bezpieczeństwo zdefiniowane; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Procedura naruszeń i szablony komunikacji gotowe; checklisty DoR/DoD odhaczone.

