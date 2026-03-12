---
title: Backup and Recovery Strategy
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Backup and Recovery Strategy


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Zakres usług/danych: [lista]


## Cel dokumentu

Zaprojektować spójną strategię backupu i odtwarzania, spełniającą RPO/RTO, wymagania regulacyjne oraz integrującą się z DRP/BCP i runbookami usług.


## Zakres i granice

- Zakres: klasyfikacja danych/usług, cele RPO/RTO, topologia backupów/replikacji (DB/pliki/konfiguracja/IaC), retencja, szyfrowanie/klucze, lokalizacja danych, monitoring/alerty, testy odtwarzania, RACI i zgodność ze standardami.
- Poza zakresem: szczegółowe runbooki per aplikacja (oddzielne dokumenty), bezpieczeństwo fizyczne.


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
2. Strategia backup/replikacji (warstwy, topologia, lokalizacje, retencja, szyfrowanie).
3. Procedury odtwarzania high‑level (kolejność usług, walidacja, dane referencyjne).
4. Zarządzanie kluczami (KMS/HSM, rotacja, odzyskanie w DR, custody/escrow).
5. Monitoring i alertowanie (wskaźniki, SLO, progi reakcji, eskalacja).
6. Testy odtwarzania (zakres, częstotliwość, metryki, raportowanie, wnioski).
7. RACI i odpowiedzialności (ownerzy usług, bezpieczeństwo, DBA/infra, on‑call).
8. Zgodność i audyt (wymagania regulatorów/klientów, artefakty dowodowe, cykl przeglądów).


## Szybkie powiązania
- vm-backup-and-recovery-procedure
- backup-and-recovery-testing
- backup-and-recovery-reference
- backup-and-recovery-procedure
- backup-and-recovery-guide

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

- Uzupełnij matrycę RPO/RTO (sekcja 1) i strategię backup/replikacji (sekcja 2).
- Opisz procedury high‑level i klucze (sekcje 3–4); zdefiniuj monitoring i testy (sekcje 5–6).
- Przypisz role (sekcja 7) i wymagania zgodności (sekcja 8); zaktualizuj quick links i checklisty w `reports/checklist_atomic.jsonl`.


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

- BIA/BCP/DRP (RPO/RTO, krytyczność), inwentarz systemów/danych, wymagania regulatorów/klientów (retencja/lokalizacja), dostępne technologie backup/replication, SLA dostawców, polityki bezpieczeństwa danych/KMS.


## Wyjścia

- Strategia backup/replikacji (cele, częstotliwości, klasy danych), plan odtwarzania na poziomie usług, matryca RPO/RTO, plan testów odtwarzania, polityka kluczy, wskaźniki monitoringu/alertów, plan zgodności (audyt, raporty), quick links w `linkage_index.jsonl`.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `backup_and_recovery_reference.md`, `backup_and_recovery_testing.md`
- [ ] `linkage_index.jsonl` → `backup_verification.md`, `checklista_weryfikacji_backupow.md`
- [ ] `linkage_index.jsonl` → `disaster_recovery_plan.md`, `business_continuity_plan.md`


## Wymagane rozwinięcia / streszczenia

- Matryca RPO/RTO z uzasadnieniem (BIA/BCP); mapa danych i lokalizacji.
- Plan testów odtwarzania (częstotliwość, scenariusze, kryteria zaliczenia).
- Plan zarządzania kluczami (rotacja, odzyskanie w DR, custody/escrow); streszczenie ryzyk.


## Wymagane powiązania

- Runbooki backup/restore, KMS/HSM, monitoring/alerty, SLA dostawców storage/replication, rejestr wymagań regulatorów.


## Kryteria DoR (Definition of Ready)

- [ ] RPO/RTO i klasyfikacja danych/usług dostępne; inwentarz systemów zebrany.
- [ ] Polityka kluczy i wymagania regulatorów znane; technologie backup/replication wybrane.


## Kryteria DoD (Definition of Done)

- [ ] Sekcje 1–8 uzupełnione; strategia spójna z DRP/BCP; quick links zaktualizowane.
- [ ] Plan testów i monitoring zdefiniowane; role i zgodność opisane; checklisty DoR/DoD odhaczone.


## Artefakty do załączenia

- Matryca RPO/RTO, topologia backup/replikacji, polityki retencji i kluczy, wskaźniki monitoringu/alertów, plan testów, lista wymagań regulatorów.


## Walidacja / testy

- Przegląd strategii z BCP/DRP i bezpieczeństwem danych; sanity check konfiguracji z realnymi możliwościami.
- Weryfikacja zgodności z wymaganiami regulatorów (retencja/lokalizacja).


## Metryki monitorowane

- Pokrycie RPO/RTO przez strategię, czas aktualizacji RPO/RTO po zmianie systemu, sukces testów restore, czas dostępu do kluczy w DR.


## Utrzymanie i aktualizacje

- Przegląd strategii co kwartał lub po istotnej zmianie architektury/usług; rejestr zmian w `reports/change_log.jsonl`.
- Aktualizacja quick links po każdej zmianie strategii/testów.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, dodaj powiązania w `linkage_index.jsonl` oraz wpis w `reports/checklist_atomic.jsonl`.
