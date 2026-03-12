---
title: Backup and Disaster Recovery
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Backup and Disaster Recovery


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Zakres usług/danych: [lista]


## Cel dokumentu

Ustalić spójny model kopii zapasowych i odtwarzania usług w scenariuszach awaryjnych, tak aby zapewnić wymagane RPO/RTO, zgodność regulacyjną i gotowość do DR (technicznie i operacyjnie).


## Zakres i granice

- Zakres: strategia backupu/replikacji, retencja, szyfrowanie/klucze, lokalizacja danych, testy odtwarzania, integracja z DRP/BCP/IR, RACI, monitoring i raportowanie.
- Poza zakresem: runbooki aplikacyjne i ewakuacja fizyczna (opisywane osobno).


## Użytkownicy i interesariusze
- SRE/Ops/DBA, Security/Compliance, Audyt, Właściciele usług.
## Wejścia i wyjścia
- Wejścia: matryca RPO/RTO, harmonogramy backupów, inwentarz lokacji (region/on‑prem/offsite), polityka retencji, polityka kluczy, wyniki testów restore/DR, lista kontaktów on‑call.
- Wyjścia: karta referencyjna (PDF/Confluence/MD) z parametrami aktualnymi, linkami i dowodami testów; sygnał dla audytu i operacji.
## Założenia
- System backup raportuje sukces/fail i ma API/raporty do pobrania.
- KMS/HSM dostępne i posiada procedurę odzyskania.
## Otwarte pytania
- Czy wszystkie wyjątki lokalizacji danych mają zgodę compliance?
- Jak często rotujemy klucze i testujemy restore z nowym kluczem?
## Powiązania (meta)
- Key Documents: backup_and_recovery_strategy/design/guide/procedure; drp/bcp; security_key_management.
- Key Document Structures: parametry, lokalizacje, retencja, klucze, kontakty, dowody.
- Document Dependencies: CMDB/asset, KMS/HSM, monitoring backupów, runbooki usług.
## Zależności dokumentu
Wymaga aktualnych RPO/RTO per usługa, harmonogramów/retencji z systemu backup, polityki kluczy (custody/escrow), listy kontaktów on‑call oraz ostatnich wyników testów restore/DR. Bez tych danych DoR jest otwarte.
## Fazy cyklu życia
- Planowanie: uzupełnienie parametrów, zgodność z BCP/DRP.
- Operacje: utrzymanie aktualności po zmianach usług, rotacje kluczy, zmiany retencji.
- Testy DR: aktualizacja po każdym teście/restore.
- Audyt/Compliance: potwierdzenie zgodności retencji/lokalizacji/kluczy.
- Decommission: archiwizacja kart i kluczy, potwierdzenie usunięcia danych.
## Struktura sekcji (szkielet)

1. Klasyfikacja danych/usług i cele RPO/RTO (matryca).
2. Strategia backup/replication (co, gdzie, jak często; warstwy DB/pliki/konfiguracja/IaC; retencja; szyfrowanie; lokalizacja/regiony).
3. Procedury odtwarzania high‑level (scenariusze partial/full/ransomware; kolejność usług; walidacja).
4. Zarządzanie kluczami i dostępem (KMS/HSM, rotacja, odzyskiwanie, custody/escrow).
5. Monitoring i alertowanie (SLO, wskaźniki, reakcja na błędy, eskalacja).
6. Testy i weryfikacja (częstotliwość, zakres, metryki, raportowanie, action items).
7. RACI i odpowiedzialności (właściciele usług, bezpieczeństwo, infra, DBA, on‑call).
8. Integracja z BCP/DRP/IR (punkty wyzwalające, komunikacja, wymagania regulatorów).
9. Ryzyka i decyzje (trade‑off koszt vs RPO/RTO, lokalizacja danych).
10. Plan aktualizacji i przeglądów (cykl, trigger po zmianie architektury/usług).


## Szybkie powiązania
- vm-backup-and-recovery-procedure
- backup-and-recovery-testing
- backup-and-recovery-strategy
- backup-and-recovery-reference
- backup-and-recovery-procedure

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO 22301** — System Zarządzania Ciągłością Działania (BCMS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

### Polskie normy i regulacje
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa
- **PN-ISO-22301** — PN-ISO 22301:2020-04 — Zarządzanie Ciągłością Działania

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

- Uzupełnij matrycę RPO/RTO i strategię backup/replication (sekcje 1–2), procedury high‑level i klucze (3–4).
- Skonfiguruj monitoring, testy i RACI (sekcje 5–7); opisz integrację z BCP/DRP/IR oraz ryzyka (sekcje 8–9).
- Zapisz plan przeglądów (sekcja 10); zaktualizuj quick links i checklisty w `reports/checklist_atomic.jsonl`.


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
- RPO (Recovery Point Objective) — maks. akceptowalna utrata danych.
- RTO (Recovery Time Objective) — maks. czas przywrócenia usługi.
- Break‑glass — procedura awaryjnego dostępu do kluczy.
## Przykłady użycia
- Szybkie sprawdzenie, które regiony mają offsite i jaką retencję.
- Audyt: dowody testów restore/DR i właściciele kluczy.
## Ryzyka i ograniczenia
- Nieaktualne RPO/RTO lub harmonogramy → fałszywe poczucie bezpieczeństwa.
- Brak dostępu do kluczy przy restore → wydłużone RTO lub utrata danych.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- Backup & Recovery Guide/Procedure, DR Plan, BCP, Security Key Management.
## Powiązania z sekcjami innych dokumentów
- DRP → RPO/RTO; Key Management → Szyfrowanie/klucze.
## Słownik pojęć w dokumencie
- Snapshot, Incremental, Differential, Offsite, WORM — dodaj definicje.
## Wymagane odwołania do standardów
- Wymagania regulatorów dot. retencji/lokalizacji, polityka szyfrowania.
## Mapa relacji sekcja→sekcja
- RPO/RTO → Harmonogramy/retencja → Lokalizacje → Klucze → Testy → Kontakty.
## Mapa relacji dokument→dokument
- Backup Reference → Guide/Procedure → DRP/BCP → Audit/Compliance.
## Ścieżki informacji
- Strategia/Design → Parametry → Karta referencyjna → Runbooki/DR → Audyt.
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
- Raporty z systemu backup, testy restore/DR, linki do runbooków, lista kontaktów.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Ops/DBA → Security/Compliance → Service Owners → Owner sign‑off.
## Metryki jakości
- Aktualność danych (dni od ostatniej aktualizacji), odsetek usług z kompletną kartą, sukces testów restore/DR, czas dostępu do kluczy, liczba wyjątków otwartych.
## Kryteria ukończenia
- [ ] Karta kompletna i zgodna z DRP/BCP; linki działają.
- [ ] Dowody testów i klucze opisane; kontakty aktualne.
- [ ] Dokument powiązany w linkage_index i checklistach.
## Wejścia

- Klasyfikacja danych/usług, wymagania RPO/RTO (BIA/BCP/DRP), inwentarz systemów i lokalizacji danych, wymagania regulatorów/klientów (retencja/lokalizacja), dostępne technologie backup/replication, SLA z dostawcami, polityka kluczy (KMS/HSM).


## Wyjścia

- Strategia backup/DR (warstwy danych/usług, częstotliwości, cele RPO/RTO, topologia), plan testów odtwarzania, plan kluczy i szyfrowania, matryca odpowiedzialności, wskaźniki monitoringu/raportowania, quick links w `linkage_index.jsonl`.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `backup_and_recovery_strategy.md`, `backup_and_recovery_design.md`
- [ ] `linkage_index.jsonl` → `backup_and_recovery_testing.md`, `backup_verification.md`, `checklista_weryfikacji_backupow.md`
- [ ] `linkage_index.jsonl` → `backup_and_recovery_procedure.md`, `vm_backup_and_recovery_procedure.md`
- [ ] `linkage_index.jsonl` → `disaster_recovery_plan.md`, `business_continuity_plan.md`, `incident_response_runbook.md`


## Wymagane rozwinięcia / streszczenia

- Matryca RPO/RTO z uzasadnieniem; plan testów odtwarzania i raportowania.
- Plan kluczy (rotacja, odzyskanie w DR, custody); streszczenie ryzyk i trade‑offów.


## Wymagane powiązania

- Runbooki backup/restore, KMS/HSM, monitoring/alerty, DRP/BCP/IR, rejestr wymagań regulatorów, SLA dostawców storage/replication.


## Kryteria DoR (Definition of Ready)

- [ ] RPO/RTO i klasyfikacja danych/usług dostępne; inwentarz systemów zebrany.
- [ ] Polityka kluczy i wymagania regulatorów znane; technologie backup/replication wybrane.


## Kryteria DoD (Definition of Done)

- [ ] Sekcje 1–10 uzupełnione; strategia spójna z DRP/BCP/IR; quick links zaktualizowane.
- [ ] Plan testów, monitoring i RACI opisane; ryzyka/trade‑offy udokumentowane; checklisty DoR/DoD odhaczone.


## Artefakty do załączenia

- Matryca RPO/RTO, topologia backup/replication, polityki retencji i kluczy, plan testów, decision log, wymagania regulatorów, wskaźniki monitoringu/alertów.


## Walidacja / testy

- Przegląd techniczny z właścicielami usług i bezpieczeństwem danych.
- Sprawdzenie zgodności z wymaganiami regulatorów (retencja/lokalizacja) i DRP/BCP.


## Metryki monitorowane

- Pokrycie RPO/RTO, sukces testów odtwarzania, czas dostępu do kluczy w DR, koszt storage vs budżet, liczba otwartych action items.


## Utrzymanie i aktualizacje

- Przegląd co kwartał lub po istotnej zmianie architektury/usług; rejestr zmian w `reports/change_log.jsonl`.
- Aktualizacja quick links po każdej zmianie.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, dodaj powiązania w `linkage_index.jsonl` oraz wpis w `reports/checklist_atomic.jsonl`.
