---
title: Backup and Recovery Testing
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Backup and Recovery Testing


## Metadane

- Właściciel: QA Lead
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Zakres systemów/danych: [lista]


## Cel dokumentu

Zaplanować i wykonywać testy backupu/odtwarzania, aby potwierdzić możliwość przywrócenia danych w założonych RPO/RTO, wykrywać luki i zapewnić dowody zgodności (audyt/regulator).


## Zakres i granice

- Zakres: scenariusze testowe (plik/DB/konfiguracja, partial/full, ransomware/tampering), kryteria wejścia/wyjścia, role, metryki i raportowanie, action items po testach, plan komunikacji.
- Poza zakresem: pełne procedury DR (w DRP) i runbooki aplikacyjne.


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

1. Zakres testu i cele (dane/usługi, RPO/RTO do weryfikacji).
2. Scenariusze i środowiska (partial/full/PITR, ransomware, utrata DC; środowisko testowe/prod z oknem).
3. Zespół i role (koordynator, właściciele systemów, DBA/infra, bezpieczeństwo, audyt).
4. Plan testu (kroki restore, weryfikacja integralności/spójności, pomiar czasu, klucze).
5. Kryteria wejścia/wyjścia i akceptacji (gotowość danych/środowisk, progi RPO/RTO, bezpieczeństwo danych).
6. Walidacja po odtworzeniu (smoke/app checks, akceptacja biznesowa, logi).
7. Raportowanie i action items (wyniki, odchylenia, właściciele, terminy, priorytety).
8. Harmonogram testów (częstotliwość per system/klasa danych, wymagania regulacyjne).
9. Lessons learned i aktualizacja strategii/DRP/runbooków.


## Szybkie powiązania
- vm-backup-and-recovery-procedure
- failure-and-recovery-testing
- backup-and-recovery-strategy
- backup-and-recovery-reference
- backup-and-recovery-procedure

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 22301** — System Zarządzania Ciągłością Działania (BCMS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
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

- Zbierz dane wejściowe (sekcje 1–3), przygotuj plan testu (sekcja 4) i kryteria (sekcja 5).
- Wykonaj testy, wypełnij sekcje 6–7; zaktualizuj harmonogram (sekcja 8) i lessons learned (sekcja 9).
- Odhacz checklisty DoR/DoD w `reports/checklist_atomic.jsonl`; uzupełnij quick links.


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

- Strategia backupu/replikacji, matryca RPO/RTO, inwentarz danych/backupów, polityka kluczy (KMS/HSM), okna serwisowe, właściciele systemów, wymagania regulatorów/klientów.


## Wyjścia

- Plan testu (scenariusz, kroki, środowisko), log przebiegu, wyniki (RPO/RTO zmierzone), błędy/incydenty, action items z owner/terminem, raport audytowy, wpis w `linkage_index.jsonl`.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `backup_and_recovery_strategy.md`, `backup_and_recovery_reference.md`
- [ ] `linkage_index.jsonl` → `backup_verification.md`, `checklista_weryfikacji_backupow.md`
- [ ] `linkage_index.jsonl` → `disaster_recovery_plan.md`, `business_continuity_plan.md`


## Wymagane rozwinięcia / streszczenia

- Macierz RPO/RTO i sposób pomiaru w testach; tabela scenariuszy z ownerami i oknami.
- Lista kluczy KMS/HSM użytych przy restore + procedura break‑glass.
- Streszczenie wyników testów (RPO/RTO osiągnięte, główne incydenty) i zmian do wdrożenia.


## Wymagane powiązania

- KMS/HSM i procedury odzyskania kluczy, runbooki usług, DRP/BCP, ticketing/audyt.
- Monitoring/alerty backupu, system backup/restore, środowiska testowe.


## Kryteria DoR (Definition of Ready)

- [ ] RPO/RTO i zakres testu zdefiniowane; dane/backupy dostępne; klucze przygotowane.
- [ ] Okna serwisowe i właściciele systemów potwierdzeni; scenariusze opisane.


## Kryteria DoD (Definition of Done)

- [ ] Testy wykonane; wyniki i dowody zapisane; RPO/RTO ocenione.
- [ ] Action items z owner/terminem, follow‑up zaplanowany; quick links zaktualizowane.
- [ ] Status/metadane aktualne; checklisty DoR/DoD odhaczone.


## Artefakty do załączenia

- Plan testu, logi/raporty, pomiary RPO/RTO, checklisty, dowody (checksumy/zrzuty), ticket audytowy, lista action items, waiver log.


## Walidacja / testy

- Testy restore wg scenariuszy (full/partial/PITR/ransomware); weryfikacja integralności/spójności; pomiar RPO/RTO.
- Audyt dostępów do backupów/kluczy; kontrola logów i alertów.


## Metryki monitorowane

- Sukces/fail testów, czas odtwarzania vs RTO, punkt odzysku vs RPO, liczba incydentów/błędów, czas zamknięcia action items.


## Utrzymanie i aktualizacje

- Przegląd po każdym cyklu testów lub kwartalnie; rejestr zmian w `reports/change_log.jsonl`.
- Aktualizacja quick links po każdej iteracji testów.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, dodaj powiązania w `linkage_index.jsonl` oraz wpis w `reports/checklist_atomic.jsonl`.
