---
title: Procedury przekazania projektu
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Procedury przekazania projektu


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać przekazanie projektu do utrzymania/BAU lub innego zespołu, zapewniając komplet materiałów, dostępy i gotowość operacyjną (hypercare/escalacje).


## Zakres i granice

- Obejmuje: zakres przekazania (komponenty, środowiska, SLA, właściciele docelowi), materiały (dokumentacja tech/runbooki/architektura/kontrakty/listy dostępu), szkolenia i KT (sesje, nagrania, reverse KT, checklisty gotowości), dostępy i narzędzia (konta/repo/monitoring/ticketing/klucze), kryteria akceptacji (checklista, testy operacyjne, podpis), okres przejściowy (hypercare, on-call, eskalacje).  
- Poza zakresem: renegocjacja kontraktów komercyjnych (osobne).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: lista komponentów/środowisk/SLA, dokumentacja/runbooki, listy dostępu/sekrety, plan szkoleń, kontrakty/usługi, risk register, plan change.  
- Wyjścia: komplet materiałów, przeprowadzone KT, aktywne dostępy/monitoring, wypełniona checklista akceptacji, podpis przekazania, plan hypercare/escalacji.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: runbook_operacyjny, architektura_systemu, risk_register, change_management_plan, communication_plan, incident_response_playbook, monitoring_strategy_document, access_control_policy.
- Key Document Structures: zakres, materiały, KT, dostępy, akceptacja, hypercare.
- Document Dependencies: repo/doc/runbooki, IAM/sekrety, monitoring/ticketing, kontrakty/SLA, on-call schedule.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Zbieranie danych i walidacja.
- Analiza i interpretacja.
- Rekomendacje i plan działań.
- Follow-up i przegląd wyników.
## Struktura sekcji (szkielet)
1. Zakres i cele: obszary testów, ryzyka, definicje jakości, kryteria exit.
2. Strategie testowe: unit/integration/e2e/performance/security/usability, poziomy środowisk.
3. Narzędzia i dane: frameworki, test data, mocki, CI/CD, raportowanie.
4. Role i odpowiedzialności: QA, dev, PO, bezpieczeństwo; RACI.
5. Harmonogram: fazy testów, regression cadence, smoke dla release, go/no-go.
6. Metryki i raporty: coverage, defect rate, escape rate, trend, komunikacja.
## Szybkie powiązania

- linkage_index.jsonl (handover/project)
- runbook_operacyjny, architektura_systemu, risk_register, change_management_plan, communication_plan, incident_response_playbook, monitoring_strategy_document, access_control_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **SCRUM Guide** — Przewodnik Scrum

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

1. Uzupełnij zakres/materiały/dostępy; zaplanuj KT i hypercare.  
2. Wykonaj KT, testy operacyjne i checklistę; zbierz podpis.  
3. Utrzymuj log szkoleń/akceptacji; zaktualizuj linkage_index/checklisty.


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

- [ ] Materiały i dostępy kompletne; KT wykonane; testy operacyjne zaliczone; hypercare/eskalacje opisane.  
- [ ] Podpisy/akceptacje zapisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Checklista akceptacji, log KT/szkoleń, listy dostępu/sekretów, runbooki, podpis przekazania, plan hypercare, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % elementów checklista „pass”, liczba braków po hypercare, czas hypercare, liczba eskalacji, czas uzupełnienia braków.

## Kryteria ukończenia

- [ ] Przekazanie zakończone (podpis, hypercare), dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres przekazania (komponenty, środowiska, SLA, właściciele docelowi)  
2) Materiały (dokumentacja tech, runbooki, architektura, kontrakty, listy dostępu)  
3) Szkolenia i KT (sesje, nagrania, Q&A, reverse KT, checklisty)  
4) Dostępy i narzędzia (konta, repo, monitoring, ticketing, klucze/secrets)  
5) Kryteria akceptacji (checklista, testy operacyjne, zgody, podpis przekazania)  
6) Okres przejściowy (hypercare, wsparcie on-call, punkty eskalacji, czas trwania)  
7) Załączniki (checklista akceptacji, log szkoleń, listy dostępu, podpis)


## Wymagane rozwinięcia

- Checklista akceptacji; testy operacyjne; log szkoleń/KT; listy dostępu/sekretów.  
- Plan hypercare (czas, on-call, eskalacje); podpis i repo dowodów.


## Wymagane streszczenia

- Executive: zakres, status materiałów/KT, data podpisu, plan hypercare, otwarte ryzyka.


## Guidance (skrót)

- Materiały i dostępy muszą być kompletne przed podpisem; brak → brak akceptacji.  
- KT z nagraniem i reverse KT; loguj obecność i pytania.  
- Hypercare z jasnym czasem i on-call; eskalacje z kontaktami.


## Checklisty Definition of Ready (DoR)

- [ ] Zakres/SLA, materiały i listy dostępu zebrane; plan KT/hypercare ustalony.  
- [ ] Ownerzy docelowi potwierdzeni; on-call/escalacje wstępnie opisane.


## Checklisty Definition of Done (DoD)

- [ ] Materiały/dostępy/KT/testy operacyjne kompletne; checklista i podpis wykonane; hypercare ustawione; dokument w linkage_index; metadane aktualne.

