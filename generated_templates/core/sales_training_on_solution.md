---
title: Sales Training on Solution
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Sales Training on Solution


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Definiuje program szkoleniowy dla sprzedaży/CS/partnerów dotyczący rozwiązania: wiedza produktowa, use case’y, demo, bezpieczeństwo/compliance, pricing/packaging, konkurencja, oraz sposób mierzenia przyswojenia i skuteczności.


## Zakres i granice

- Obejmuje: cele szkolenia, zakres materiału (funkcje, use case’y, demo), moduły (produkt, bezpieczeństwo/compliance, pricing, konkurencja, proces sprzedaży), formaty (live/LMS/lab), wymagania zaliczenia, harmonogram, metryki skuteczności, plan aktualizacji.
- Poza zakresem: pełne playbooki sprzedażowe; szczegółowe SOP-y techniczne.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: product docs, roadmap, pricing/packaging, ICP/persony, konkurencja, compliance/bezpieczeństwo, proces sprzedaży, feedback z poprzednich szkoleń.
- Wyjścia: program i sylabus, materiały (deck, demo, labs, quizy), wymagania zaliczenia/certyfikacji, harmonogram sesji, KPI skuteczności (adoption, pass rate, win rate uplift), plan aktualizacji.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: sales_enablement_materials, go_to_market_strategy, product_strategy_document, pricing_engine_design, security/compliance notes, marketing_plan.
- Document Structures: moduł → materiał → ćwiczenie/lab → zaliczenie → KPI.
- Dependencies: aktualność produktu/roadmapy, environment demo/lab, narzędzia LMS/quiz, kanały feedbacku.


## Zależności dokumentu

- Upstream: product/roadmap, pricing, konkurencja, compliance, release calendar.
- Downstream: certyfikacje/rekordy w LMS/HR, readiness listy, enablement repo, KPI adoption/win rate.
- Zewnętrzne: partnerzy (materiały white-label), wymagania cert dla partnerów/platform.


## Fazy cyklu życia

- Design: cele, moduły, materiały, wymagania zaliczenia.
- Pilot: mała grupa, feedback, korekty.
- Rollout: cała sprzedaż/CS/partnerzy, harmonogram, certyfikacje.
- Utrzymanie: aktualizacje po release, retraining, KPI/feedback.



## Struktura sekcji (szkielet)

1) Streszczenie i cele szkolenia (KPI: adoption, pass rate, win rate uplift)
2) Zakres i moduły (produkt, use case, demo, bezpieczeństwo/compliance, pricing, konkurencja, proces sprzedaży)
3) Materiały i formaty (deck, demo, labs, FAQ, quizy, wideo, live/LMS)
4) Wymagania zaliczenia/certyfikacji (quiz, lab, demo assessment), progi i ważność
5) Harmonogram i logistyka (terminy, trenerzy, environment demo/lab, narzędzia)
6) KPI i pomiar skuteczności (adoption, pass rate, win rate/velocity uplift, feedback CSAT)
7) Plan aktualizacji i governance (cadence po release, właściciele modułów, wersjonowanie)
8) Ryzyka i założenia; decyzje (ADR) i otwarte pytania


## Szybkie powiązania

- sales_enablement_materials, go_to_market_strategy, product_strategy_document, pricing_engine_design, security/compliance notes, marketing_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

- [ ] Moduły pokrywają ICP/use case, pricing, bezpieczeństwo/compliance, konkurencję.
- [ ] Materiały są wersjonowane i powiązane z release; KPI i feedback są mierzone.
- [ ] Wymagania zaliczenia są jasne, progi i ważność zdefiniowane; środowisko demo/lab gotowe.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Sylabus, decki, demo scripts, labs, quizy, checklisty demo, dashboard KPI, ADR log, plan aktualizacji.


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

- ICP/use case → moduły/treści → demo/lab → quiz/certyfikacja → KPI (adoption, win rate, deal cycle).
- Release/feature → aktualizacja materiałów → komunikacja → retraining.


## Wymagane rozwinięcia

- Sylabus z modułami i ownerami, wymagania zaliczenia, linki do materiałów.
- Plan demo/lab (środowisko, dane testowe), checklisty demo.
- Plan quizów/ocen i progi, integracja z LMS/HR.
- KPI dashboard (adoption, pass rate, uplift) i kanał feedbacku.


## Wymagane streszczenia

- Executive summary: cele, moduły, forma, KPI, harmonogram.
- One-pager: co/kiedy/jak zdać, progi, link do materiałów.


## Guidance (skrót)

- DoR: aktualne product/roadmap, pricing, konkurencja, compliance; dostępne environment demo/lab; ownerzy modułów; LMS/quiz narzędzia gotowe.
- DoD: moduły/materiały opublikowane; wymagania zaliczenia/certyfikacji; harmonogram i trenerzy; KPI i feedback loop; plan aktualizacji; metadane aktualne; dokument w linkage_index.
- Spójność: moduły są spójne z messaging/pricing; materiały wersjonowane; KPI mierzą wpływ na wyniki sprzedaży.


## Checklisty Definition of Ready (DoR)

- [ ] Aktualne product/roadmap, pricing, konkurencja i compliance zebrane; środowisko demo/lab gotowe; ownerzy modułów.
- [ ] Narzędzia LMS/quiz oraz kanał feedbacku gotowe.


## Checklisty Definition of Done (DoD)

- [ ] Program, materiały, wymagania zaliczenia opublikowane; harmonogram/trenerzy; KPI/feedback działa; metadane aktualne; dokument w linkage_index.

