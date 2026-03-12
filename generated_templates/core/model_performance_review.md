---
title: Model Performance Review
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Model Performance Review


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Przeprowadzić cykliczny przegląd wydajności modeli ML (jakość, drift, koszty, ryzyka), ustalić działania korygujące i plan ulepszeń, zapewniając zgodność z wymaganiami biznesowymi i regulacyjnymi.


## Zakres i granice

- Obejmuje: metryki jakości (accuracy, AUC, F1, regresja), stabilność i drift (dane/koncept), bias/fairness, bezpieczeństwo (adversarial), koszty (latency, koszt inferencji, zużycie zasobów), zgodność (dane wrażliwe, audyt), MLOps (monitoring, alerty, versioning), decyzje go/rollback.
- Poza zakresem: definicja nowych feature’ów/datasetów (osobne dokumenty), architektura modelu (projekt pierwotny).


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: aktualne metryki z produkcji, baseline/kontrakt jakości, logi inference, dane referencyjne, wyniki monitoringu drift/bias, koszty chmurowe/infra, SLA/latency, wymagania compliance, feedback użytkowników.
- Wyjścia: raport przeglądu, lista działań (retrain/tuning/threshold/feature cleanup/rollback), decyzje go/conditional/no-go, aktualizacje konfiguracji, plan eksperymentów, aktualizacje rejestrów ryzyka/exception.


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

Jeśli brak danych: wskaż dependency na model card/model registry, data catalog, monitoring stack, risk register, compliance (AI Act/RODO), runbooki MLOps; brak – odnotuj.


## Fazy cyklu życia

- Przygotowanie: zbiór danych/metryk, ustalenie agendy.
- Przegląd: analiza jakości/drift/bias/kosztów, dyskusja ryzyk.
- Decyzje: go/conditional/rollback, plan działań i właściciele.
- Wdrożenie: realizacja działań, monitorowanie efektów.
- Retrospektywa: ocena skuteczności działań.



## Struktura sekcji (szkielet)

- Zakres modeli i wersji objętych przeglądem.
- Metryki jakości i stabilności vs baseline/SLO.
- Drift danych i konceptu; feature health.
- Bias/fairness i compliance (AI Act/RODO, dane wrażliwe).
- Bezpieczeństwo (adversarial, model stealing/leakage).
- Koszty i wydajność (latency, throughput, koszt inferencji, zużycie GPU/CPU/RAM).
- Incydenty/alerty i ich status.
- Decyzje i plan działań (retrain, tuning, thresholds, rollback, eksperymenty).
- Ryzyka i akceptacje/waivery.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
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

- Zbierz metryki i alerty; porównaj z SLO/baseline.
- Oceń drift/bias/bezpieczeństwo/koszt; podejmij decyzje.
- Zaplanuj działania i monitoruj efekty; zamykaj DoR/DoD po cyklu.


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

- [Termin 1] — [definicja robocza]
- [Termin 2] — [definicja robocza]
- [Termin 3] — [definicja robocza]


## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania]
- [Przykład 2 — krótki opis sytuacji i zastosowania]


## Ryzyka i ograniczenia

- [Ryzyko 1 — wpływ i sposób ograniczenia]
- [Ryzyko 2 — wpływ i sposób ograniczenia]


## Decyzje i uzasadnienia

- [Decyzja 1] — [uzasadnienie]
- [Decyzja 2] — [uzasadnienie]


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

1. Autor przygotowuje wersję roboczą i przeprowadza samorecenzję.
2. Recenzent techniczny (Tech Lead / BA) weryfikuje merytorycznie.
3. Właściciel procesu zatwierdza treść i zakres.
4. PM / Scrum Master aktualizuje metadata (wersja, data, status).
5. Dokument trafia do repozytorium i jest linkowany w Szybkie powiązania.

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Np. metryki → decyzja go/rollback; drift → retrain; bias → działania fairness; koszty → optymalizacje/auto-scaling.


## Wymagane rozwinięcia

- Metryki → definicje i źródła (monitoring, batch eval).
- Compliance/bias → procedury ocen i audytu.
- Bezpieczeństwo → testy adversarial/abuse.


## Wymagane streszczenia

- Tabela modeli: metryki vs SLO, drift, koszt, decyzja, działania.


## Guidance

- Cel: upewnić się, że modele spełniają SLO i regulacje, a działania są zaplanowane.
- Wejścia: monitoring, eval, koszty, feedback, compliance.
- Wyjścia: decyzje, plan działań, aktualizacje rejestrów.
- DoR: metryki i baseline, dane drift/bias, koszty, compliance zebrane; właściciele na miejscu.
- DoD: decyzje i działania zdefiniowane, sekcje N/A uzasadnione, metadane aktualne, linki do artefaktów.


## Checklisty jakości (DoR/DoD skrót)

- DoR:
  - [ ] Metryki jakości/stabilności, drift/bias i koszty zebrane; modele/wersje zidentyfikowane.
  - [ ] Wymagania compliance i właściciele obecni; artefakty monitoringu dostępne.
- DoD:
  - [ ] Decyzje go/conditional/rollback podjęte; plan działań z właścicielami i terminami.
  - [ ] Sekcje N/A uzasadnione; metadane aktualne; linki do eval/monitoringu działają.

