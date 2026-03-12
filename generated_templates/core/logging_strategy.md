---
title: Logging Strategy
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Logging Strategy


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować spójną strategię logowania aplikacyjnego/technicznego (non‑audit) wspierającą debugowanie, obserwowalność i koszty, komplementarną do logów audytowych.


## Zakres i granice

- Obejmuje: kategorie logów (app, infra, security non‑audit), poziomy i standardy formatów (structured/JSON), konwencje pól (trace/correlation id), sampling, retencję/koszt, redakcję PII, przesyłanie/agentów, routing do SIEM/observability, alerting bazujący na logach.  
- Poza zakresem: logi audytowe (audit_logging), metryki/trace (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania operacyjne/debug, SLO/latencje, polityki prywatności/PII, koszt/log volume, architektura usług i agentów, standardy tracingu.  
- Wyjścia: standard logów (format/pola), profile sampling/retencja, zasady redakcji PII, routing/forwarding, checklisty i linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: audit_logging, api_change_communication, design_bezpieczenstwa_api, strategia_wersjonowania_api, monitoring_strategy.  
- Key Document Structures: format/pola, poziomy, PII/redakcja, sampling/retencja, routing/alerty.  
- Document Dependencies: tracing/correlation, SIEM/observability stack, agent/log shipper, cost controls.



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
- Cele i KPI
- Filar/priorytety i inicjatywy
- Horyzonty/roadmapa i zależności
- Ryzyka i założenia
- Governance, finansowanie i raportowanie
## Szybkie powiązania

- linkage_index.jsonl (observability/logging_strategy)  
- audit_logging, monitoring_strategy, design_bezpieczenstwa_api


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Przyjmij schemat logu i poziomy; wprowadź masking/redakcję.  
2. Ustal sampling/retencję i routing do SIEM/observability; skonfiguruj alerty.  
3. Dokumentuj zmiany schematu, aktualizuj linkage_index, odhacz DoR/DoD.


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

- [ ] Logi są strukturalne, z trace id, bez PII/sekretów.  
- [ ] Sampling/retencja zgodne z budżetem; routing i retry działają.  
- [ ] Alerty nie generują nadmiernego szumu; linkage_index uzupełniony.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Schemat JSON logu, config agentów/shipperów, policy PII/redaction, sampling profiles, alert rules, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Koszt/GB logów, % logów ze trace id, odsetek logów z redakcją PII, liczba alertów szumowych vs actionables, dropout rate w shipperach.

## Kryteria ukończenia

- [ ] Strategia logowania wdrożona (format, PII, sampling, routing, alerty) i powiązana w linkage_index.


## Struktura sekcji

1) Format i pola (JSON, timestamp, level, service, env, trace/correlation id, user/tenant where safe)  
2) Poziomy i zasady logowania (DEBUG/INFO/WARN/ERROR/FATAL, kiedy używać, ograniczenia)  
3) PII i bezpieczeństwo (masking/redaction, allowlist pól, payload caps, secret handling)  
4) Sampling i retencja (per service/env, dynamic sampling, hot/warm/cold storage, koszt)  
5) Transport i routing (agenci/shipper, retry/backpressure, multi‑sink: SIEM + observability)  
6) Alerty i wykrywanie anomalii (log‑based alerts, error budgets, noise control)  
7) Governance (ownerzy, zmiany schematu logów, audyt użycia, waivery)  
8) Załączniki (schemat logu, przykłady, ADR/waiver log)


## Wymagane rozwinięcia

- Schemat logu z polami obowiązkowymi i dopuszczalnymi dodatkowymi; ograniczenia wielkości.  
- Zasady maskowania/redakcji PII i payloadów; lista blokowanych pól.  
- Profile sampling/retencja per środowisko i typ logu; budżet kosztowy.  
- Routing: retry/backpressure, kolejki, deduplikacja; zasady multi‑sink.  
- Procedura zmiany schematu logu i testów kompatybilności (backward).


## Wymagane streszczenia

- Executive: stan wdrożenia standardu logów, koszt/GB, główne ryzyka PII i szum/alert fatigue.


## Guidance (skrót)

- Logi strukturalne z trace id; bez PII/sekretów; limituj payload size.  
- Stosuj sampling na DEBUG/INFO w prod; ERROR powinny być pełne ale z redakcją wrażliwych pól.  
- Zawsze zapewnij retry/backpressure; unikaj drop bez metryk.  
- Zmiana schematu = wersja + kompatybilność; aktualizuj linkage_index i dokumentację.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania PII i polityka kosztu znane; tracing/correlation dostępne.  
- [ ] Agenci/stack logowania wybrane; ownerzy ustaleni.


## Checklisty Definition of Done (DoD)

- [ ] Schemat logu, poziomy, PII/masking, sampling/retencja i routing opisane; alerty skonfigurowane.  
- [ ] Linkage_index zaktualizowany; status/metadane aktualne; checklisty DoR/DoD odhaczone.  
- [ ] Procedura zmian schematu i audyt użycia gotowe.

