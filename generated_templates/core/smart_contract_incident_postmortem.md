---
title: Smart Contract Incident Postmortem
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Smart Contract Incident Postmortem


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Udokumentować incydenty związane z inteligentnymi kontraktami (błędy logiki, exploit, gas spikes, upgrade failure) oraz działania zapobiegające powtórkom.


## Zakres i granice

- Obejmuje: opis zdarzenia i wpływu na środki/użytkowników, oś czasu, luka/exploit, RCA, audyty, działania naprawcze (patch/upgrade/pause), komunikację on-chain/off-chain, lesson learned, aktualizacje standardów review/testów.
- Poza zakresem: szczegółowe bezpieczeństwo infrastruktury node’ów (oddzielne dokumenty) i polityka treasury.


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia
- Wejścia: klasyfikacja incydentów, SLO/SLI, runbooki, kontakty on-call, dane krytycznych systemów, RACI.
- Wyjścia: plan reagowania, procedury komunikacji, checklisty, raport post-incident, lista działań naprawczych.
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
- Przygotowanie i testy scenariuszy.
- Detekcja i triage.
- Reakcja/mitigacja + komunikacja.
- Odbudowa/DR i weryfikacja usług.
- Postmortem, akcje zapobiegawcze i aktualizacja runbooków.
## Struktura sekcji (szkielet)

- Streszczenie i wpływ (środki, użytkownicy, protokół)
- Oś czasu (blok/tx)
- Luka/exploit i wektor
- RCA i czynniki współprzyczynowe (spec, implementacja, audit gaps)
- Działania: pause/upgrade/migration/compensation
- Komunikacja (on-chain, blog, social, regulator)
- Lesson learned i zmiany w standardach (testy, audits, bug bounty)
- Follow-up i właściciele


## Szybkie powiązania

- Smart Contract Security Guidelines, Audit Playbook, Incident Response, Bug Bounty, Key Management (multisig/guardian).


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SAFe 6.0** — Scaled Agile Framework

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

- Tx hash/logi, wydarzenia on-chain, alerty z monitoringu, raporty audytu, zgłoszenia społeczności, snapshot stanu kontraktów.


## Wyjścia

- Raport postmortem z planem remediacji i komunikacją.
- Aktualizacje testów/audytów/monitoringu oraz ewentualne migracje kontraktów.



## Jak używać (checklista)

- Zbierz tx/logi i stan kontraktu; odtwórz oś czasu.
- Opisz wpływ finansowy/operacyjny; oceń potrzebę pause/upgrade/migration.
- RCA: błąd specyfikacji, testów, audytu czy implementacji.
- Zaplanuj remediację i komunikację transparentną; uzgodnij z governance.
- Zaktualizuj testy, monitoring, standardy review i bounty scope.


## Wymagane rozwinięcia / powiązania

- Tabela zdarzeń on-chain, wzór komunikatu post-incident, checklisty pause/upgrade, kontakt do audytorów/guardianów.


## Kryteria DoR

- Zidentyfikowany incydent i dostęp do logów/tx; skład zespołu IR.


## Kryteria DoD

- Raport opublikowany, środki zabezpieczone lub zrekompensowane, testy/monitoring zaktualizowane, follow-up zaplanowany.


## Artefakty

- Raport (MD/PDF), linki do tx i eventów, patche/upgrade scripts, komunikaty publiczne, backlog zmian.


## Walidacja

- Potwierdzenie skuteczności patch/upgrade, brak dalszych exploitów, weryfikacja testów regresyjnych.


## Metryki

- Czas detekcji i reakcji, wartość narażonych/utraconych środków, % wdrożonych działań, liczba powtórek.


## Utrzymanie

- Przegląd szablonu po każdym incydencie; aktualizacja wraz ze zmianami w ekosystemie i standardach audytowych.


## Zakończenie

Postmortem smart contractów zwiększa bezpieczeństwo i zaufanie; utrzymuj go z bieżącymi standardami i praktykami bezpieczeństwa web3.

