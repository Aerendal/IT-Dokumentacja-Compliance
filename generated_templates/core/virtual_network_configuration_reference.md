---
title: Virtual Network Configuration Reference
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Virtual Network Configuration Reference


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Dostarczyć referencję konfiguracji sieci wirtualnych (VPC/VNet/k8s CNI): adresacja, routing, bezpieczeństwo, łączność hybrydowa.


## Zakres i granice

- Obejmuje: CIDR/plan adresacji, subnety, routing, NAT, peering/VPN/DirectConnect, SG/NSG/ACL, microsegmentation, k8s CNI/pods/NetworkPolicy, DNS, load balancing, high availability, logging/flow logs, testy łączności.
- Poza zakresem: design fizycznej sieci on-prem (osobne dokumenty), polityki IAM (linkowane).


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia
- Wejścia: wymagania, projekt/ADR, inwentarz systemów/danych, okna wdrożeniowe, zasoby.
- Wyjścia: plan wdrożenia, skrypty/konfiguracje, walidacja/testy, plan rollback, lista ryzyk i właścicieli.
## Założenia
- Sieć/VLAN/QoS dostępne.  
- VMS/NVR wspiera wymagane protokoły.  
- Polityki prywatności obowiązują.
## Otwarte pytania
- Jakie są lokalne wymogi prawne dot. monitoringu?  
- Jakie są limity storage/bandwidth?  
- Czy potrzebna redundancja storage/cluster VMS?
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
- Przygotowanie/migracja danych.
- Rollout (pilot → fala → pełne wdrożenie).
- Walidacja i smoke testy.
- Stabilizacja/monitoring i przekazanie do operacji.
## Struktura sekcji (szkielet)

- Plan adresacji i subnety
- Routing, NAT, peering/VPN
- Bezpieczeństwo (SG/ACL, NetworkPolicy)
- DNS i LB
- Łączność hybrydowa
- Logging/flow logs i monitoring
- Testy łączności i checklisty


## Szybkie powiązania

- Network design, Security Hardening, IAM, Observability, DR/BCP.


## Mające zastosowanie standardy i normy


### Polskie normy i regulacje
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa
- **PT-PL** — Prawo Telekomunikacyjne (Ustawa o komunikacji elektronicznej)
- **UKE-WYTYCZNE** — Wytyczne UKE dot. bezpieczeństwa sieci telekomunikacyjnych

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
- VMS: Video Management System.  
- ONVIF: standard interoperacyjności kamer.  
- WORM: write-once-read-many (storage).
## Przykłady użycia
- Konfiguracja kamer w biurze/parkingu.  
- Audyt bezpieczeństwa istniejącej instalacji.  
- Przygotowanie do inspekcji regulatora prywatności.
## Ryzyka i ograniczenia
- Brak hardeningu → przejęcie kamer.  
- Zbyt wysoki bitrate → brak storage/QoS.  
- Nieaktualne patchy → podatności.
## Decyzje i uzasadnienia
- Profile bitrate/FPS per scenariusz.  
- Poziom szyfrowania i cert (self‑signed vs CA).  
- Retencja vs koszt storage.
## Powiązania z innymi dokumentami
- retention_policy — retencja.  
- security_requirements — hardening.  
- incident_response_runbook — incydenty.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Lokalne przepisy monitoringu/wideo, RODO/PII.  
- Wewnętrzne standardy bezpieczeństwa sieci.
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

- Wymagania aplikacji/SLA, ograniczenia adresacji on-prem, polityki bezpieczeństwa, architektura k8s/cloud, potrzeby hybrydowe.


## Wyjścia

- Plan adresacji i wzorce konfiguracji, checklisty bezpieczeństwa/routingu, przykłady k8s NetworkPolicy, procedury testów łączności.



## Jak używać (checklista)

- Wybierz i zarezerwuj CIDR; utwórz subnety i tagowanie.
- Skonfiguruj routing/NAT/peering; ustaw SG/NetworkPolicy.
- Skonfiguruj DNS/LB; włącz flow logs; przetestuj łączność (on-prem ↔ cloud ↔ k8s).


## Wymagane rozwinięcia / powiązania

- Tabela adresacji, przykłady SG/ACL, szablony NetworkPolicy, test plan łączności, polityka tagowania.


## Kryteria DoR

- Wymagania app/on-prem znane; polityki bezpieczeństwa dostępne.


## Kryteria DoD

- Plan adresacji uzgodniony; konfiguracje wzorcowe przygotowane; testy łączności opisane.


## Artefakty

- Plan adresacji, przykłady config, test cases, flow logs konfiguracja, checklisty.


## Walidacja

- Testy ping/traceroute/NAT; weryfikacja SG/ACL/NetworkPolicy; audyt adresacji/overlap.


## Metryki

- Liczba overlapów, incydenty sieciowe, czas provisioningu, zgodność security baselines.


## Utrzymanie

- Przegląd adresacji przy nowych VPC/VNet; update wzorców po zmianach chmury/k8s; audyt SG/ACL.


## Zakończenie

Referencja sieci wirtualnych ułatwia spójne i bezpieczne konfiguracje; utrzymuj ją z testami i audytami.

