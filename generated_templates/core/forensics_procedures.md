---
title: Forensics Procedures
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Forensics Procedures


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Opisać procedury informatyki śledczej (digital forensics) na potrzeby incydentów: zabezpieczenie dowodów, analiza, łańcuch dowodowy i raportowanie.


## Zakres i granice

- Obejmuje: przygotowanie (narzędzia, kontenery dowodowe), zabezpieczenie miejsca zdarzenia cyfrowego, akwizycję (disk/memory/logs/network), łańcuch dowodowy, hash/niezmienność, analiza artefaktów, timeline, malware triage, raportowanie, współpracę z IR/Legal/LEA, retencję dowodów.
- Poza zakresem: pełne reverse engineering malware (osobne playbooki), śledztwa fizyczne.


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia
- Wejścia: definicja triggera/scenariusza, wymagane uprawnienia/narzędzia, dane wejściowe, RACI i kontakty.
- Wyjścia: wykonane kroki z timestamp, dowody/artefakty, status (sukces/niepowodzenie), decyzje i eskalacje.
## Założenia
- Monitoring/alerting istnieje i jest zintegrowany z pagerem.  
- Kanały komunikacji są dostępne i ćwiczone.  
- Organizacja akceptuje audyt eskalacji.
## Otwarte pytania
- Czy potrzebne są różne ścieżki dla regionów/produktów?  
- Jakie SLA/OLA wymagają klienci?  
- Jak mierzyć skuteczność eskalacji (escape rate, satisfaction)?
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
- Przygotowanie runbooka: wersja, właściciel, testowane ścieżki.
- Egzekucja: krokowo z dowodami.
- Postmortem: usprawnienia runbooka i monitoringu.
## Struktura sekcji (szkielet)

- Przygotowanie i narzędzia
- Zabezpieczenie dowodów i łańcuch dowodowy
- Akwizycja (disk/memory/logs/network)
- Analiza (artefakty, timeline, malware triage)
- Raportowanie i współpraca z IR/Legal/LEA
- Retencja i przechowywanie dowodów
- Kontrole jakości i audyt


## Szybkie powiązania

- Cybersecurity Incident Response, Audit Trail, Evidence handling policy, Legal/Compliance, Backup/DR.


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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
- MTTA/MTTR: Mean Time To Acknowledge/Resolve.  
- Escape: incydent wykryty przez klienta zamiast monitoringu.  
- Duty manager: rola koordynatora eskalacji.
## Przykłady użycia
- Eskalacja krytycznego incydentu produkcyjnego.  
- Eskalacja problemu klienta enterprise do warstwy produktowej/exec.  
- Dry‑run procedury przed sezonem szczytu.
## Ryzyka i ograniczenia
- Niejasne kryteria → over/under‑escalation.  
- Brak danych przy eskalacji → wolne decyzje.  
- Nieaktualne on‑call → „dead pager”.
## Decyzje i uzasadnienia
- Progi severity i kanały (pager/chat/voice).  
- Kto wysyła komunikaty zewnętrzne i kiedy.  
- Jakie dane są wymagane minimalnie przy eskalacji.
## Powiązania z innymi dokumentami
- incident_response_runbook — działania techniczne.  
- communication_plan — komunikaty.  
- risk_register — ryzyka z eskalacji.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne polityki incident/change i komunikacji.  
- Wymogi klientów/regulatorów jeśli dotyczy.
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

- Polityka IR, lista systemów, narzędzia forensics, matryca ról, wymagania prawne/regulatora, playbooki incydentów.


## Wyjścia

- Procedury akwizycji/analizy, szablony łańcucha dowodowego i raportu, checklisty, rejestr dowodów.



## Jak używać (checklista)

- Przygotuj narzędzia/pojemniki; zabezpiecz system i wykonaj hash.
- Przeprowadź akwizycję zgodnie z łańcuchem dowodowym; dokumentuj każdy krok.
- Analizuj artefakty; buduj timeline; raportuj do IR/Legal.
- Przechowuj dowody zgodnie z retencją; audytuj łańcuch dowodowy.


## Wymagane rozwinięcia / powiązania

- Checklisty akwizycji, wzór łańcucha dowodowego, szablon raportu, lista narzędzi, procedury retencji.


## Kryteria DoR

- Incydent sklasyfikowany; dostęp do systemów; narzędzia gotowe; rola forensics przydzielona.


## Kryteria DoD

- Dowody zebrane i zahashowane; raport sporządzony; łańcuch dowodowy kompletny; dowody zdeponowane.


## Artefakty

- Łańcuch dowodowy, obrazy/artefakty, raport forensics, log działań.


## Walidacja

- Audyt łańcucha dowodowego; weryfikacja hash; peer review raportu.


## Metryki

- Czas akwizycji, kompletność łańcucha, liczba naruszeń procedury, czas raportowania.


## Utrzymanie

- Aktualizacja narzędzi i checklist; ćwiczenia tabletop; przegląd procedur po incydentach.


## Zakończenie

Procedury forensics zapewniają spójne i zgodne prawnie dowody; utrzymuj je z narzędziami, szkoleniami i audytami.

