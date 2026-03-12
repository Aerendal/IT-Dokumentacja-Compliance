---
title: Runbook provisioning
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Runbook provisioning


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Operacyjny runbook provisioning (VM/infra resources): kroki, walidacje, obserwowalność i rollback, aby zapewnić spójne i bezpieczne uruchamianie zasobów.


## Zakres i granice

- Obejmuje: przyjmowanie żądań, wybór szablonu/flavor, sieć/SG/IAM, tagging/CMDB, IaC/CI/CD, walidacje (quota, koszt, compliance), monitoring/backup w momencie tworzenia, testy smoke, dokumentację/log działań, rollback/deprovision.  
- Poza zakresem: provisioning kontenerów i bare-metal (osobne runbooki).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: ticket/żądanie, wymagania zasobu, approved images/flavors, polityki sieci/SG/IAM, tagowanie/CMDB, limity kosztowe, IaC repo, secret manager.  
- Wyjścia: utworzony zasób z monitoring/backup/tagami/CMDB, raport z walidacji/smoke, log działań, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: procedury_provisioning_vm, security_hardening_vm, logging_strategy, audit_logging, cmdb_policy, backup_and_disaster_recovery.  
- Key Document Structures: intake, konfiguracja, IaC/CI/CD, walidacje/testy, monitoring/backup, rollback/deprovision.  
- Document Dependencies: IaC pipeline, cloud/virtualization platform, CMDB, monitoring/backup tools, secret manager.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie runbooka: wersja, właściciel, testowane ścieżki.
- Egzekucja: krokowo z dowodami.
- Postmortem: usprawnienia runbooka i monitoringu.
## Struktura sekcji (szkielet)
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka
## Szybkie powiązania

- linkage_index.jsonl (infra/runbook_provisioning)  
- procedury_provisioning_vm, security_hardening_vm, cmdb_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
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

1. Zweryfikuj żądanie i zatwierdzenia; przygotuj IaC z tagami/SG/IAM.  
2. Uruchom pipeline, wykonaj smoke/compliance, włącz monitoring/backup; zarejestruj w CMDB.  
3. Zapisz log działań i dodaj do linkage_index; przygotuj rollback/deprovision plan jeśli potrzebny.


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

- [ ] Każdy zasób ma tagi/owner/koszt center, monitoring/backup włączone, SG/IAM zgodne z polityką.  
- [ ] Policy-as-code i drift detection działają; log działań dostępny.  
- [ ] Linkage_index uzupełniony; rollback/deprovision opisany.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Ticket/żądanie, IaC skrypty, log pipeline, smoke/compliance raporty, CMDB wpis, backup/monitoring config, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % provisioning przez IaC, % zasobów z monitoring/backup/tagi/CMDB, czas provisioning, liczba driftów, compliance pass rate.

## Kryteria ukończenia

- [ ] Runbook provisioning zapewnia spójny, bezpieczny i zgodny proces; powiązany w linkage_index.


## Struktura sekcji

1) Intake i weryfikacja (ticket, wymagania, zatwierdzenia, quota/koszt)  
2) Konfiguracja (szablon/obraz, sieć/SG/IAM, tagi/CMDB, sekrety)  
3) IaC/CI/CD (repo, PR/review, pipeline, policy-as-code, drift detection)  
4) Tworzenie i walidacje (run pipeline, smoke test, compliance checks)  
5) Monitoring/backup (logi/metryki/trace, alerty, backup/snapshots, restore test)  
6) Dokumentacja i log działań (czas, parametry, wyniki testów, kto wykonał)  
7) Rollback/deprovision (kroki, kiedy, cleanup tagów/CMDB/sekretów)  
8) Załączniki (checklisty, skrypty, ADR/waiver log)


## Wymagane rozwinięcia

- Szablon intake (wymagania, SLA, owner, koszt), kryteria zatwierdzeń.  
- Checklista konfiguracji (SG/IAM/sekrety/tagi), testy smoke i compliance.  
- Policy-as-code i drift detection; log działań z timestampami.  
- Plan rollback/deprovision i cleanup (tagi, CMDB, klucze, snapshoty).


## Wymagane streszczenia

- Executive: wolumen provisioning, standard compliance (monitoring/backup/tagi), główne ryzyka (drift, brak backup), plan usprawnień.


## Guidance (skrót)

- Provisioning wyłącznie IaC + policy-as-code; bez tego brak zgody.  
- Monitoring/backup/tagi/CMDB muszą być włączone w chwili tworzenia.  
- Smoke test i compliance check przed przekazaniem do użytkownika.  
- Każdy zasób ma owner i koszt center; log działań obowiązkowy.  
- Aktualizuj linkage_index i checklisty po zmianach procesu.


## Checklisty Definition of Ready (DoR)

- [ ] Ticket/żądanie zatwierdzone; wymagania i budżet znane; approved images/flavors gotowe.  
- [ ] IaC repo/pipeline, secret manager, tag/CMDB policy dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Zasób utworzony IaC, z SG/IAM/sekretami, monitoring/backup/tagi/CMDB aktywne; smoke/compliance zaliczone; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Log działań i ewentualny plan rollback/deprovision zapisane; checklisty DoR/DoD odhaczone.

