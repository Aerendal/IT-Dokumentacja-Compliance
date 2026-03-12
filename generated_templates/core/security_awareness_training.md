---
title: Security Awareness Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Awareness Training


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Program szkolenia z bezpieczeństwa (awareness) dla wszystkich ról: cele, agenda, materiały, egzaminy oraz sposób mierzenia skuteczności.


## Zakres i granice

- Obejmuje: cele szkolenia, grupy docelowe, program/agenda, materiały i kanały dystrybucji, harmonogram i refresh, egzaminy/quizy, metryki ukończeń i skuteczności.
- Poza zakresem: szczegółowa implementacja kontrolek technicznych.


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: profil uczestników, poziom wejściowy, narzędzia/laby, materiały referencyjne, mentorzy.
- Wyjścia: sylabus, materiały, harmonogram, plan ewaluacji (quiz/lab/egzamin), feedback i plan utrzymania.
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
- Analiza potrzeb i profilu grupy.
- Projekt sylabusa i materiałów.
- Realizacja i wsparcie mentorskie.
- Ocena i follow-up (certyfikacja/mentoring).
## Struktura sekcji (szkielet)

- Streszczenie i cele szkolenia
- Grupy docelowe/persony i wymagania wstępne
- Program/agenda i formaty (e‑learning/live)
- Materiały, kanały i dostępność
- Harmonogram i częstotliwość refresh
- Egzaminy/quizy i kryteria zaliczenia
- Metryki skuteczności i raportowanie
- Ryzyka i plan ciągłego doskonalenia


## Szybkie powiązania
- security-awareness-training-plan
- security-training
- sustainability-awareness-training
- security-tools-training
- security-policy-training

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

- Wypisz grupy docelowe, cele i program; wybierz formaty (live/e‑learning).
- Podlinkuj materiały i ustaw egzaminy/quizy; sekcje N/A uzasadnij.
- Uzupełnij quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; po każdej edycji aktualizuj metryki i status.


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

- Polityki i standardy bezpieczeństwa, wymagania regulacyjne.
- Lista grup docelowych/person, ryzyka i incydenty z lessons learned.
- Dostępne kanały: e‑learning, warsztaty, webcasty, newslettery.


## Wyjścia

- Plan i program szkolenia per grupa docelowa.
- Materiały (slajdy, quizy, wideo), harmonogram i komunikacja.
- Metryki ukończeń, wyniki egzaminów, NPS/CSAT, plan refresh.
- Powiązania do polityk i runbooków.



## Szybkie powiązania (uzupełnij)

- security_awareness_training_plan.md
- security_policy_design.md
- security_best_practices.md
- security_incident_response.md
- logging_and_audit_trail.md
- hipaa_compliance_training.md


## Wymagane rozwinięcia / streszczenia

- Scenariusze modułów i przykładowe pytania quizowe.
- One-pager dla managerów: cele, wymagany czas, sposób mierzenia.


## Wymagane powiązania

- Polityki bezpieczeństwa, runbooki incydentów, wymagania regulacyjne.
- Rejestr ryzyk i lessons learned, aby aktualizować program.


## Kryteria DoR

- [ ] Polityki/regulacje zebrane; grupy docelowe opisane.
- [ ] Materiały wstępne i kanały dystrybucji dostępne.
- [ ] Owner szkolenia i harmonogram uzgodnione.


## Kryteria DoD

- [ ] Program i harmonogram opublikowane; materiały podlinkowane.
- [ ] Egzaminy/quizy aktywne, metryki zbierane.
- [ ] Plan refresh i komunikacja ustawione.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Program/agenda, slajdy, quizy.
- Harmonogram i plan komunikacji.
- Raport ukończeń, wyniki egzaminów, NPS/CSAT.


## Walidacja / testy

- Pilotaż na małej grupie; sprawdź czas trwania i zrozumienie.
- Peer review materiałów pod kątem zgodności z politykami.


## Metryki monitorowane

- % ukończenia i % zdanych egzaminów.
- Średni wynik quizów; NPS/CSAT szkolenia.
- Czas ukończenia vs plan; liczba zgłoszeń/pytań po szkoleniu.


## Utrzymanie i aktualizacje

- Refresh co 6–12 miesięcy lub po zmianach w politykach/incydentach.
- Aktualizuj przykłady i screeny, gdy zmieniają się narzędzia.


## Zakończenie

Po spełnieniu DoD opublikuj materiały, podlinkuj w intranecie/LM‑S, odhacz checklisty w `reports/checklist_atomic.jsonl` i ustaw termin następnego przeglądu.
- Przegląd materiałów; pilotaż szkolenia lub quiz; sanity metryk ukończeń.

