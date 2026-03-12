---
title: Policy Data Corruption Response
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Policy Data Corruption Response


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Ustandaryzować reakcję na przypadki korupcji danych: kroki, role, komunikacja, walidacja, rollback i metryki jakości.


## Zakres i granice

- Obejmuje: scope danych/systemów, role/RACI, wykrycie i potwierdzenie korupcji, izolację i rollback, walidację/rekonsyliację, komunikację/eskalacje, dokumentację i raportowanie.
- Poza zakresem: długofalowe zmiany architektury (opisywane w planach technicznych).


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia
- Wejścia: alert/incydent, klasyfikacja danych i jurysdykcji, logi/artefakty, kontrakty SLA/DPA, polityki notyfikacji, lista kontaktów (PR/Legal/CS/Regulator), matryca ryzyka i szablony komunikatów.
- Wyjścia: decyzja o naruszeniu (breach/not), zakres danych/osób, notyfikacje wysłane, raport regulatorowi, plan remediacji, dowody i chain-of-custody, postmortem.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Key Documents: incident_response_plan, privacy_policy, dpa_scc_register, communication_plan_crisis, bcp_drp, forensic_procedure.
- Key Document Structures: wykrycie/triage, containment, notyfikacje, remediacja, postmortem.
- Document Dependencies: CMDB/data inventory, IAM/logging/SIEM, legal registry jurysdykcji, DPA/SCC, contracts SLA, PR/Comms.
## Zależności dokumentu
Wymaga inwentarza danych/systemów, klasyfikacji jurysdykcji, kontaktów regulatorów/partnerów, szablonów komunikatów, procedur forensics i chain-of-custody. Bez nich DoR otwarte.
## Fazy cyklu życia
- Wykrycie/Triage: kwalifikacja zdarzenia, PII/PHI/PCI?, wstępny wpływ.
- Containment/Eradication: izolacja, reset kluczy/tokens, odcięcie źródła.
- Notyfikacje: regulator, klienci, partnerzy, wewnętrzne, PR.
- Remediacja: poprawki, rotacja sekretów, wzmacnianie kontroli.
- Postmortem: RCA, lekcje, zmiany w kontrolach/procedurach.
## Struktura sekcji (szkielet)

- Kontekst i zakres danych/systemów
- Detekcja i potwierdzenie korupcji (kryteria, dowody)
- Izolacja i zabezpieczenie dowodów
- Rollback/restore i walidacja (checksum, rekonsyliacja)
- Komunikacja/eskalacja i log decyzji
- Raportowanie i dokumentacja
- Działania zapobiegawcze i lekcje


## Szybkie powiązania
- spatial-data-corruption
- data-retention-policy
- data-loss-response
- data-governance-policy
- data-breach-response

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)

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

- Wybierz zakres incydentu, wykonaj kroki detekcja→izolacja→restore→walidacja→komunikacja; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Po zakończeniu podlinkuj raport, dowody i action log.


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

- Polityki/standardy, runbooki DB/backup, lista systemów/danych krytycznych.
- Narzędzia: backup/restore, walidacja/rekonsyliacja, monitoring/logi.
- Role i kontakty (DBA/SRE/owner biznesowy/IR).


## Wyjścia

- Wykonany proces z dowodami, raportem i metrykami.
- Decyzje i eskalacje udokumentowane.
- Plan działań zapobiegawczych/lekcji.



## Szybkie powiązania (uzupełnij)

- policy_renewal_procedure.md
- data_recovery_runbook.md
- logging_and_audit_trail.md
- security_incident_response.md
- security_posture_monitoring.md
- policy_metrics_monitoring.md


## Wymagane rozwinięcia / streszczenia

- Checklisty detekcji/walidacji/rekonsyliacji.
- Streszczenie decyzji i wpływu na dane/użytkowników.


## Wymagane powiązania

- Runbooki backup/restore, walidacja danych, monitoring/logi.
- Rejestr incydentów, compliance/gdpr jeśli dotyczy.


## Kryteria DoR

- [ ] Zakres danych/systemów i role potwierdzone.
- [ ] Dostępne backupy i narzędzia walidacji.
- [ ] Kanały komunikacji/eskalacji przygotowane.


## Kryteria DoD

- [ ] Proces wykonany; dowody i raport uzupełnione.
- [ ] Rekonsyliacja/walidacja zakończona; decyzje/eskalacje zapisane.
- [ ] Action log i lesson learned wpisane; quick-links/checklisty zaktualizowane.


## Artefakty do załączenia

- Dowody korupcji (logi, checksumy), raport rekonsyliacji.
- Log działań/eskalacji, komunikaty.
- Plan działań zapobiegawczych.


## Walidacja / testy

- Peer review dowodów i rekonsyliacji.
- Test przywracania na próbce; sanity after-restore.


## Metryki monitorowane

- Czas wykrycia i przywrócenia (MTTD/MTTR dla korupcji danych).
- % danych zweryfikowanych po restore; liczba FP.
- Liczba incydentów korupcji vs okres; przyczyny powtarzalne.


## Utrzymanie i aktualizacje

- Przegląd po każdym incydencie i cyklicznie (np. kwartalnie).
- Aktualizuj narzędzia/checklisty po zmianach w danych/architekturze.


## Zakończenie

Po spełnieniu DoD podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i zaktualizuj runbooki/monitoring.
