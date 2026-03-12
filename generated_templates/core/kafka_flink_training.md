---
title: Kafka & Flink Training
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Kafka & Flink Training


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Przygotować program szkoleniowy z Apache Kafka i Apache Flink (fundamenty, operacje, development), aby zespoły mogły projektować, wdrażać i utrzymywać niezawodne strumienie danych.


## Zakres i granice

- Obejmuje: podstawy publish/subscribe, topic design, partitioning/replication, schema management, security (SASL/ACL), monitoring, Flink API (DataStream/SQL), state management, checkpoint/savepoint, time semantics/watermarks, join/window patterns, testing, CI/CD, operacje (scaling, upgrades), antywzorce i problemy typowe.
- Poza zakresem: inne silniki stream (Spark/Faust), batch ETL.


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: potrzeby projektów, poziom uczestników, istniejąca architektura, standardy org (naming/ACL/schema registry), monitoring stack.
- Wyjścia: sylabus modułów, materiały/przykłady, laboratoria hands-on, checklisty DoR/DoD zadań, kryteria zaliczenia, harmonogram sesji, ankiety i metryki skuteczności.


## Założenia
- Narzędzia i logi dostępne.  
- Zespół akceptuje zasady wellbeing.  
- SLO/SLA są zdefiniowane.
## Otwarte pytania
- Jak obsłużyć różne strefy czasowe?  
- Jak mierzyć sukces (MTTR, customer impact)?  
- Czy potrzebny pageduty/inna platforma?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: standardy Kafka/Flink w organizacji, cluster configs, schema registry, security baseline, CI/CD, monitoring; brak – odnotuj.


## Fazy cyklu życia

- Plan: cele, poziomy, moduły, kadra.
- Przygotowanie: materiały, laby, dane przykładowe, środowiska.
- Wykonanie: sesje, laby, Q&A.
- Ocena: quizy, zadania praktyczne, feedback.
- Utrzymanie: aktualizacja treści, nowych wersji, best practices.


## Struktura sekcji (szkielet)

- Profil kompetencyjny i KPI szkolenia.
- Moduły Kafka (topics/partitions/retention/compaction, producers/consumers, exactly-once/idempotence, schema registry, ACL, monitoring).
- Moduły Flink (DataStream/SQL, state, time, windows, joins, checkpoints/savepoints, fault tolerance, patterns, connectors).
- Lab i ćwiczenia (scenariusze, dane, ocena).
- Narzędzia i środowiska (local, test cluster, observability).
- Bezpieczeństwo i compliance (ACL, audit, dane wrażliwe).
- Testing/CI/CD (integration, end-to-end, load, backpressure tests).
- Ocena i certyfikacja.
- Plan aktualizacji programu.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu

- Określ profil grupy; wybierz moduły; przygotuj laby; przeprowadź sesje; oceniaj; aktualizuj program.


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
- Alert fatigue: przeciążenie liczbą alertów.  
- Game day: ćwiczenie symulujące awarie.
## Przykłady użycia
- Szkolenie nowych SRE przed dołączeniem do rotacji.  
- Game day dla usługi krytycznej.  
- Retro po serii nocnych alertów.
## Ryzyka i ograniczenia
- Brak ćwiczeń → słaba reakcja.  
- Za dużo alertów → burnout/fatigue.  
- Nieaktualne runbooki → dłuższy MTTR.
## Decyzje i uzasadnienia
- Częstotliwość game day.  
- Limity alertów/osoba i rotacje.  
- Zakres uprawnień na dyżurach.
## Powiązania z innymi dokumentami
- escalation_procedure_design — ścieżki eskalacji.  
- communication_plan — komunikaty.  
- observability_plan — alerty.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód]
- [Dokument Z → Sekcja W] — [powód]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne polityki bezpieczeństwa i dostępu, PII.  
- Standardy SRE/ITIL jeśli przyjęte.
## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ]
- [Sekcja C] -> [Sekcja D] : [typ]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ]
- [Dokument C] -> [Dokument D] : [typ]


## Ścieżki informacji

- [Wejście] → [Źródło] → [Rozwinięcie] → [Wyjście]
- [Wejście] → [Źródło] → [Streszczenie] → [Wyjście]


## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane

- [Artefakt 1]
- [Artefakt 2]


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

Moduły → ćwiczenia → ocena; bezpieczeństwo → ACL/SASL; operacje → monitoring; time semantics → testy.


## Wymagane rozwinięcia

- Ćwiczenia → repo z kodem i datasetami.
- Monitoring → konkretne dashboardy/alerty.


## Wymagane streszczenia

- One-pager: moduły, cele, harmonogram, wymagania wstępne.


## Guidance

Cel: praktyczne, produkcyjne kompetencje Kafka+Flink. DoR: cele i uczestnicy znani, standardy org zebrane, środowiska lab gotowe. DoD: sylabus/ćwiczenia/próby/monitoring opisane, sekcje N/A uzasadnione, metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Cele i uczestnicy; [ ] Standardy org (naming/ACL/schema) i środowiska lab; [ ] Materiały bazowe zebrane.
- DoD: [ ] Sylabus, ćwiczenia i ocena gotowe; [ ] Monitoring/bezpieczeństwo uwzględnione; [ ] Sekcje N/A uzasadnione; metadane aktualne.

