---
title: Metrics Dictionary
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Metrics Dictionary


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Stworzyć słownik metryk używanych w organizacji, zapewniając jednoznaczne definicje i odpowiedzialność.



## Zakres i granice
- Obejmuje: metryki biznesowe (oszczędność czasu/kosztu, SLA), operacyjne (awarie botów, retraje, lead time), jakościowe (defekt rate, accuracy ML), zgodności (audit trail, segregacja obowiązków), bezpieczeństwa (uprzywilejowane dane/dostępy), adopcji i zmian (liczba procesów włączonych, satysfakcja użytkowników).
- Poza zakresem: szczegółowe procedury budowy botów/procesów, pełne modele finansowe.
## Użytkownicy i interesariusze
- Automation CoE, Ops/SRE, Business Owners, Security/Compliance, Finance/FinOps.
## Wejścia i wyjścia
- Wejścia: katalog procesów z automatyzacją, definicje SLA/KPI biznesowych, logi RPA/orkiestratora, monitoring ML, dane kosztowe, polityki compliance (SoD, audyt), dane o incydentach.
- Wyjścia: zestaw metryk/KPI/KRI, definicje źródeł danych, dashboardy, progi/alerty, raporty cykliczne, kryteria go/hold dla nowych automatyzacji.
## Założenia
- Orkiestrator/logi dostępne; dane kosztowe z FinOps/ERP.
- Polityka SoD i audytu jest zdefiniowana.
## Otwarte pytania
- Czy mierzymy efekty uboczne (shadow IT, manual overrides)?
- Jak często rewizja progów i dashboardów?
## Powiązania (meta)
- Key Documents: automation_strategy, rpa_governance, ml_ops, security_baseline, change_management.
- Key Document Structures: katalog procesów, metryki, progi, alerty, raportowanie.
- Document Dependencies: monitoring/observability, CMDB procesów, IAM/SoD, koszt/FinOps.
## Zależności dokumentu
Wymaga aktualnego katalogu procesów i ich właścicieli, źródeł logów (orkiestrator, ML, API), kosztów (licencje, infra), wymagań SoD/audytu i polityki danych. Brak danych blokuje DoR.
## Fazy cyklu życia
- Planowanie: wybór metryk/KPI, progi, źródła danych.
- Implementacja: instrumentacja logów, zasilenie dashboardów, alerty.
- Operacje: monitoring ciągły, raporty cykliczne, aktualizacja progów.
- Retrospektywa: analiza trendów, decyzje o rozbudowie/wycofaniu automatyzacji.
## Struktura sekcji (szkielet)

1. Format wpisu: nazwa, opis, wzór, jednostka, zakres wartości, częstotliwość, źródło danych, właściciel.
2. Kategoryzacja: produkt, finansowe, operacyjne, bezpieczeństwo, ML/AI, wydajność.
3. Źródła i linie danych: dashboardy, systemy, eventy; linage.
4. Jakość metryk: walidacje, SLA świeżości, alerty odchyleń.
5. Governance: proces dodawania/zmian, wersjonowanie, review, deprecjacje.
6. Konsumpcja: gdzie dostępny słownik (repo/portal), API/eksporty.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

- [ ] Każda metryka ma wzór, źródło, właściciela i częstotliwość.
- [ ] Kategorie i tagi ułatwiają wyszukiwanie.
- [ ] SLA świeżości i walidacje zdefiniowane; alerty działają.
- [ ] Proces zmian/wersjonowania i dostęp (portal/API) zapewnione.

## Definicje robocze
- Throughput botów, Retry rate, Bot MTTR, Automation SLA, Drift ML, SoD hit.
## Przykłady użycia
- Raport miesięczny value i awaryjności dla zarządu.
- Alert: wzrost retraje > próg → analiza przyczyny i rollback wersji bota.
## Ryzyka i ograniczenia
- Metryki bez spójnych źródeł lub definicji → mylne decyzje.
- Brak SoD/audytu → ryzyko naruszeń compliance.
## Decyzje i uzasadnienia
- Wybór metryk/SLO na dashboardzie.  
- Progi i kanały eskalacji.  
- Layout (kolejność, grupowanie).  
- Retencja i wersjonowanie zmian.
## Powiązania z innymi dokumentami
- Automation Strategy, RPA Governance, ML Ops Runbook, Security Baseline, Change Mgmt.
## Powiązania z sekcjami innych dokumentów
- ML Ops → accuracy/drift; Security/SoD → access metrics; FinOps → cost/value.
## Słownik pojęć w dokumencie
- KPI/KRI, SLA/SLO, Drift, Retry, MTTR, SoD, Audit trail.
## Wymagane odwołania do standardów
- Polityki SoD, audyt (np. SOC2/ISO), wymagania prywatności danych procesów.
## Mapa relacji sekcja→sekcja
- Procesy → Metryki → Progi/alerty → Dashboardy → Decyzje → Action plan.
## Mapa relacji dokument→dokument
- Hyperautomation Metrics → Automation Strategy → Change/Release → Audit/Compliance.
## Ścieżki informacji
- Logi/monitoring → Agregacja → Dashboardy/alerty → Decyzje → Retrospektywa.
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
- Dashboardy (BI/observability), raporty cykliczne, definicje metryk, konfiguracje alertów.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Automation CoE → Security/Compliance → Business Owners → Exec sign‑off.
## Metryki jakości
- Coverage procesów (% z metrykami), alert fidelity (false positive/negative), aktualność danych, czas reakcji na alert, wartość biznesowa (czas/koszt saved), MTTR botów, drift ML.
## Kryteria ukończenia
- [ ] Metryki/progi/alerty działają i są raportowane.
- [ ] Dashboardy dostępne dla interesariuszy; instrukcje widoków opisane.
- [ ] Dokument powiązany w linkage_index i checklistach.
