---
title: Backup and Recovery Guide
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Backup and Recovery Guide


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Zakres usług/danych: [lista]


## Cel dokumentu

Praktyczny przewodnik „how-to” do wykonywania backupów i odtwarzania: kroki operacyjne, wymagane dane, narzędzia, walidacja i eskalacje, zgodny ze strategią i DRP.


## Zakres i granice

- Zakres: instrukcje backup/restore (DB/plik/konfiguracja), scenariusze full/inc/diff/PITR, szyfrowanie/klucze, walidacja integralności/spójności, eskalacje i komunikacja, dowody audytowe.
- Poza zakresem: definiowanie strategii/architektury (w Strategy/Design) oraz runbooki specyficzne dla pojedynczych aplikacji.


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

1. Przygotowanie (dostępy, klucze, okno serwisowe, środowisko, pre-checki).
2. Backup: kroki dla typów (full/inc/diff/snapshot/log), parametry, retencja, szyfrowanie.
3. Restore: scenariusze (plik/DB/PITR/system), kroki, dane referencyjne, kolejność usług.
4. Walidacja: integralność (checksum/DB consistency), spójność aplikacyjna, czasy RPO/RTO.
5. Dokumentacja i dowody: logi, checksumy, bilety, lokalizacja dowodów.
6. Eskalacje i komunikacja: kogo powiadomić, kiedy, kanały i szablony.
7. Bezpieczeństwo: dostęp do backupów/kluczy, PII/sekrety, retencja i usuwanie.
8. Checklisty i action items: co musi być odhaczone przed/po, follow-up.


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

- W sekcji 1 przygotuj środowisko/klucze; w 2–3 wykonaj backup/restore zgodnie z wybranym scenariuszem; w 4 zweryfikuj wyniki.
- Zapisz dowody i czasy RPO/RTO, zgłoś incydenty/defekty, uaktualnij quick links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.


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

- Strategia/architektura backup, matryca RPO/RTO, lista systemów/danych, narzędzia i konta serwisowe, polityka kluczy (KMS/HSM), okna serwisowe, szablony komunikacji/eskalacji.


## Wyjścia

- Wykonane backupy/restore (logi, checksumy), raport z walidacji, czasy RPO/RTO z testu, zgłoszenia incydentów/defektów, dowody dla audytu, quick links w `linkage_index.jsonl`.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `backup_and_recovery_strategy.md`, `backup_and_recovery_design.md`
- [ ] `linkage_index.jsonl` → `backup_and_recovery_testing.md`, `backup_verification.md`, `checklista_weryfikacji_backupow.md`
- [ ] `linkage_index.jsonl` → `disaster_recovery_plan.md`, `business_continuity_plan.md`


## Wymagane rozwinięcia / streszczenia

- Szczegółowe kroki/komendy per narzędzie/typ backupu; tabela parametrów.
- Szablony komunikacji/eskalacji; streszczenie wyników (czy RPO/RTO spełnione).


## Wymagane powiązania

- Narzędzia backup/restore, KMS/HSM, runbooki aplikacji, monitoring/alerty, ticketing/audyt.


## Kryteria DoR (Definition of Ready)

- [ ] Dostępy/narzędzia/klucze przygotowane; okno serwisowe uzgodnione.
- [ ] Lista systemów/danych i scenariuszy gotowa; polityka PII/sekretów znana.


## Kryteria DoD (Definition of Done)

- [ ] Backup/restore wykonane, walidacja przeprowadzona; dowody zapisane.
- [ ] RPO/RTO zmierzone; incydenty/defekty zgłoszone; quick links/status zaktualizowane.
- [ ] Checklisty DoR/DoD odhaczone; metadane aktualne.


## Artefakty do załączenia

- Logi/raporty backup/restore, checksumy, bilety, szablony komunikacji, lista action items, waiver log.


## Walidacja / testy

- Smoke/consistency po restore; kontrola szyfrowania i dostępu do kluczy; test scenariuszy PITR jeżeli dotyczy.


## Metryki monitorowane

- Czas backup/restore, spełnienie RPO/RTO, sukces/fail, liczba incydentów/defektów, czas reakcji na eskalacje.


## Utrzymanie i aktualizacje

- Przegląd po zmianach narzędzi/procedur lub kwartalnie; rejestr zmian w `reports/change_log.jsonl`.
- Aktualizacja quick links po każdej zmianie przewodnika.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, dodaj powiązania w `linkage_index.jsonl` oraz wpis w `reports/checklist_atomic.jsonl`.
