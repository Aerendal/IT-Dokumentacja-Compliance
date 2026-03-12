---
title: Healthcare IT Operations Runbook
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Healthcare IT Operations Runbook


## Metadane

- Właściciel: Clinical Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Operacyjny runbook dla systemów ochrony zdrowia (EHR/EMR, PACS, LIS/RIS, integracje HL7/FHIR). Ma zapewnić ciągłość, bezpieczeństwo i zgodność (HIPAA/RODO, lokalne przepisy), opisując procedury codzienne, incydentowe i zmianowe.


## Zakres i granice

- Obejmuje: monitoring, backup/DR, change management, release windows, patching, tożsamość/IAM (klinicyści, admini), integracje HL7/FHIR, obsługę incydentów (kliniczne/techniczne), zgłoszenia serwisowe, bezpieczeństwo (audyt, logi, dostępy uprzywilejowane), ciągłość działania (downtime procedures), komunikację z kliniką.
- Poza zakresem: szczegółowe instrukcje kliniczne, konfiguracje producentów sprzętu medycznego (chyba że w załącznikach), rozwój nowych funkcji.


## Użytkownicy i interesariusze

- IT Ops/SRE, Security/Compliance, Klinicyści/SME, Vendorzy, Service Desk.


## Wejścia i wyjścia

- Wejścia: inwentarz systemów i integracji (EHR/EMR/PACS/LIS/RIS), RTO/RPO, okna serwisowe, polityki bezpieczeństwa, listy kontaktów (klinika, dostawcy), dokumenty compliance (HIPAA/RODO), procedury downtime, CMDB/asset, runbooki vendorów.
- Wyjścia: harmonogramy zadań operacyjnych, procedury incydentów, checklisty backup/DR, instrukcje downtime, playbook komunikacji, lista kontaktów i eskalacji, log zmian/patchy.


## Założenia

- Dostępne są runbooki vendorów i aktualne listy kontaktów.
- Monitoring i backup są wdrożone w środowisku docelowym.


## Otwarte pytania

- Czy wszystkie integracje HL7/FHIR mają testy conformance?
- Jakie są lokalne wymagania prawne poza HIPAA/RODO?


## Powiązania (meta)

- Key Documents: incident_response, change_management, backup_dr, privacy/security policies, hl7_fhir_integration.
- Key Document Structures: harmonogram operacji, playbook incydentowy, komunikacja, checklisty.
- Document Dependencies: CMDB, IAM, monitoring/observability, compliance.


## Zależności dokumentu

Wymaga aktualnych RTO/RPO, krytyczności systemów, mapy integracji (HL7/FHIR/VPN), polityk bezpieczeństwa, listy kontaktów klinicznych i dostawców, oraz procedur downtime z kliniki. Bez nich DoR niezamknięte.


## Fazy cyklu życia

- Planowanie: aktualizacja inwentarza, RTO/RPO, okna serwisowe.
- Operacje bieżące: monitorowanie, backupy, patching, service desk, access requests.
- Incydenty: triage, eskalacje, komunikacja (klinika/pacjenci/dostawcy), raporty.
- DR/BCP: failover, restore, testy DR, powroty, walidacja kliniczna.
- Zmiany: CAB/approvals, release, walidacje post‑release.
- Audyt/Compliance: logi, ścieżki dowodów, raporty okresowe.



## Struktura sekcji (szkielet)

- Warunki wstępne i wymagania
- Kroki wykonania (krok po kroku)
- Weryfikacja poprawności
- Kroki rollback
- Typowe problemy i rozwiązania
- Log akcji

## Szybkie powiązania

- linkage_index.jsonl (health/ops/runbook)
- incident_response, change_management, backup_dr, privacy/security, hl7_fhir_integration


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)

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

1. Uzupełnij inwentarz systemów, RTO/RPO, kontakty.
2. Wpisz harmonogram operacji i patchy; progi monitoringu.
3. Dodaj procedury incydentów/downtime i komunikaty.
4. Sprawdź DoR/DoD; weryfikuj spójność cross‑doc.


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

- Downtime clinical — praca offline; kroki powrotu i walidacja kliniczna.
- RTO/RPO — czas przywrócenia / utrata danych akceptowalna.


## Przykłady użycia

- Awaria EHR: przełączenie na tryb downtime, komunikaty do kliniki, powrót i rekonsyliacja.
- Patch krytyczny: CAB, okno serwisowe, test po wdrożeniu, walidacja kliniczna.


## Ryzyka i ograniczenia

- Naruszenie HIPAA/RODO (logi, dostęp, dane w komunikatach).
- Brak walidacji klinicznej po incydencie/patchu → ryzyko kliniczne.


## Decyzje i uzasadnienia

- Kadencja raportów (tydzień/kwartał).  
- Kryteria go/no-go i required evidence.  
- Standard kanałów komunikacji (statuspage, e-mail, in-app).

## Powiązania z innymi dokumentami

- Incident Response Playbook (kliniczny/IT), Change Management, Backup & DR.
- IAM/Privileged Access Policy, Audit/Compliance plan.


## Powiązania z sekcjami innych dokumentów

- Privacy/Security → IAM/logi/szyfrowanie.
- HL7/FHIR Integration → Monitoring i testy interface’ów.


## Słownik pojęć w dokumencie

- EHR/EMR, PACS, LIS, RIS, HL7, FHIR, CAB, RTO/RPO.


## Wymagane odwołania do standardów

- HIPAA/RODO, lokalne przepisy zdrowotne, HL7/FHIR conformance, ISO 27799 (health infosec).


## Mapa relacji sekcja→sekcja

- Inwentarz → Monitoring/Backup/DR → Incydenty/Downtime → Audyt.


## Mapa relacji dokument→dokument

- Healthcare IT Ops Runbook → Incident Response → Change Mgmt → Audit/Compliance.


## Ścieżki informacji

- Alert/Incydent → Triage/Eskalacja → Komunikacja → Mitigacja → Walidacja kliniczna → Postmortem.
- Zmiana/Patch → CAB → Wdrożenie → Walidacja → Dokumentacja/audyt.


## Weryfikacja spójności

- [ ] RTO/RPO zgodne z backup/DR i downtime.
- [ ] IAM/polityki spójne z audytem i logowaniem.
- [ ] Komunikacja i kontakty aktualne i przetestowane.


## Lista kontrolna spójności relacji

- [ ] Każdy system ma monitoring, backup, właściciela i kontakty.
- [ ] Każda zmiana ma komunikację i walidację kliniczną.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Dashboardy, harmonogramy patch/backup, szablony komunikatów, listy kontaktów, logi audytu.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- IT Ops → Security/Compliance → Klinika → CAB/Owner sign‑off.


## Metryki jakości

- Dostępność (SLA), liczba incydentów klinicznych, czas reakcji/naprawy, sukces testów DR, wskaźniki audytu (log completeness, access recertification), defekty po patchach.

## Kryteria ukończenia

- [ ] Harmonogramy, playbooki i kontakty kompletne.
- [ ] Dowody backup/DR/testów dostępne.
- [ ] Dokument powiązany w linkage_index.jsonl i checklistach.


## Powiązania sekcja↔sekcja

- Inwentarz systemów → Harmonogram operacji/monitoring → Incydenty/DR.
- IAM/Uprawnienia → Incydenty bezpieczeństwa → Audyt/raportowanie.
- Change/Release → Komunikacja z kliniką → Downtime procedures.


## Struktura sekcji

1) Inwentarz systemów i integracji (krytyczność, RTO/RPO)
2) Monitoring i alerty (kategorie kliniczne/techniczne, progi, dashboardy)
3) Backup/DR (harmonogram, testy, dowody)
4) IAM i dostępy uprzywilejowane (wnioski, rotacja haseł/kluczy, recertyfikacja)
5) Zmiany i release (CAB, okna serwisowe, walidacja kliniczna)
6) Patching (OS/app/db, wyjątki, dowody)
7) Incydenty (kliniczne, bezpieczeństwa, infrastrukturalne) – triage, eskalacje, komunikacja
8) Downtime procedures (praca offline, powrót online, walidacja danych)
9) Vendor/3rd party coordination (SLA, kontakty, eskalacje)
10) Raportowanie/Audyt (HIPAA/RODO, logi, ścieżka dowodowa)
11) Role i odpowiedzialności (RACI)
12) Załączniki: listy kontaktów, szablony komunikatów, checklisty


## Wymagane rozwinięcia

- Monitoring: krytyczne transakcje kliniczne (rejestracja, laboratory, imaging), progi alertów.
- Downtime: scenariusze pracy papierowej, rejestr offline, kroki powrotu (rekonsyliacja danych).
- IAM: procedura nadawania/odbierania dostępu klinicystom/kontraktorom, MFA.


## Wymagane streszczenia

- HIPAA/RODO główne wymagania: logowanie dostępu, minimalizacja danych, szyfrowanie.
- Procedury vendorów: streszcz kluczowe kroki (SLA, kontakt, wymagane logi).


## Guidance (skrót)

- Ustal jedno źródło prawdy dla inwentarza i RTO/RPO.
- Używaj szablonów komunikacji (klinika/pacjenci) i trzymaj je aktualne.
- Testuj DR i downtime regularnie; zapisuj dowody dla audytu.
- Rygorystycznie loguj dostępy i zmiany; recertyfikuj uprawnienia.
- Po każdym incydencie wykonaj walidację kliniczną i postmortem.


## Checklisty Definition of Ready (DoR)

- [ ] Inwentarz, krytyczność, RTO/RPO zebrane.
- [ ] Polityki bezpieczeństwa i compliance dostępne.
- [ ] Lista kontaktów (klinika/dostawcy) aktualna.
- [ ] Procedury downtime istnieją lub zaznaczone jako N/A z planem.
- [ ] Struktura sekcji uzupełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Wszystkie sekcje wypełnione lub N/A z uzasadnieniem.
- [ ] Monitoring/backup/DR/patching mają harmonogram, właścicieli i dowody.
- [ ] Incydenty i komunikacja mają playbooki i eskalacje.
- [ ] Audyt/ślad dowodowy opisane; logi/raporty wskazane.
- [ ] Wersja/data/właściciel zaktualizowane; linki działają.

