---
title: Procedury backup i recovery
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Procedury backup i recovery


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Opisać standardowe procedury tworzenia kopii zapasowych i odtwarzania, aby spełnić RPO/RTO i wymagania zgodności.


## Zakres i granice

- Obejmuje: klasyfikację danych/systemów, strategie backup (full/inc/diff, snapshot, immutability), harmonogramy, retencję, szyfrowanie, testy odtwarzania, monitoring, DR vs backup, dane testowe, role/odpowiedzialności, runbook recovery.
- Poza zakresem: projekt DR site (osobne dokumenty), architektura storage.


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

- Klasyfikacja danych/systemów i RPO/RTO
- Strategia backup (typy, harmonogram, retencja, lokalizacje)
- Szyfrowanie i dostęp
- Testy odtwarzania (częstotliwość, scenariusze)
- Monitoring i alerty
- Role i odpowiedzialności
- Runbook recovery (kroki, czas, kontakty)


## Szybkie powiązania

- Disaster Recovery, Data Retention Policy, Security/KMS, Change Management, Incident Response.


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
1. Wpisz aktualne RPO/RTO, harmonogramy, retencję i lokalizacje.
2. Dodaj dane kluczy (KMS/HSM), właścicieli i procedury break‑glass.
3. Podlinkuj runbooki i dowody testów restore/DR.
4. Zaktualizuj kontakty i eskalacje; domknij checklisty DoR/DoD.
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

- Wymagania RPO/RTO, klasyfikacja danych, polityki bezpieczeństwa/retencji, lista systemów, budżet storage, narzędzia backup.


## Wyjścia

- Plan backup/retencji, harmonogramy, konfiguracje, runbook recovery, raport testów odtwarzania.



## Jak używać (checklista)

- Sklasyfikuj systemy/dane i przypisz RPO/RTO.
- Wybierz strategię backup; ustaw harmonogram i retencję; włącz szyfrowanie.
- Skonfiguruj monitoring/alerty; zaplanuj i wykonuj testy odtwarzania.
- Uzupełnij runbook recovery; aktualizuj po testach/incydentach.


## Wymagane rozwinięcia / powiązania

- Tabela systemów/RPO/RTO, harmonogramy, konfiguracje backup, scenariusze testów, runbook recovery, checklisty audytu.


## Kryteria DoR

- Lista systemów i RPO/RTO znana; narzędzia backup dostępne; polityki retencji zatwierdzone.


## Kryteria DoD

- Backup działa wg harmonogramu; szyfrowanie/retencja ustawione; testy odtwarzania zaliczone; runbook zaktualizowany.


## Artefakty

- Plan backup, konfiguracje, logi, raporty testów, runbook, audyt.


## Walidacja

- Test restore, audyt retencji/szyfrowania, przegląd logów/alertów, porównanie z RPO/RTO.


## Metryki

- Sukces backup/restore, czas odtwarzania vs RTO, zgodność retencji, liczba incydentów utraty danych.


## Utrzymanie

- Przegląd kwartalny; test restore zgodnie z harmonogramem; aktualizacja po zmianach systemów/retencji.


## Zakończenie

Procedury backup/recovery chronią dane i dostępność; utrzymuj je z testami, szyfrowaniem i monitoringiem.

