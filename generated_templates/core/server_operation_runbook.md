---
title: Server Operation Runbook
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Server Operation Runbook


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Operacyjny runbook dla serwerów (bare metal/VM): provisioning, konfiguracja, patching, monitoring, backup/DR, bezpieczeństwo i procedury incydentowe. Ma zapewnić powtarzalne utrzymanie, zgodność i szybkie reakcje.


## Zakres i granice

- Obejmuje: standardy build (obrazy, IaC), sieć i storage, konfigurację systemu (OS, pakiety, hardening), IAM/SSH/klucze, patching i kernel updates, monitoring/logi/alerty, backup/snapshoty, kapacitę i lifecycle (commission/decommission), procedury incydentów (awarie hw/os/security), dokumentację/CMDB.
- Poza zakresem: spec aplikacyjne (link do runbooków usług), projekt sieci wysokiego poziomu.


## Użytkownicy i interesariusze

- SRE/Infra, Security, Compliance/Audit, Ops/Support, Product teams (konsumenci serwerów).


## Wejścia i wyjścia

- Wejścia: standardy obrazów/IaC, listy pakietów, polityki security/hardening, monitoring/logging profile, backup policy, CMDB, listy kontaktów/on-call, SLA.
- Wyjścia: checklisty provisioning/paching/decommission, konfiguracje, profile monitoringu, procedury incydentowe, wpisy CMDB, raporty zmian.


## Założenia

- Dostępne są narzędzia IaC, monitoring, backup; polityki security/IAM obowiązują.


## Otwarte pytania

- Czy wymagane są certyfikacje (SOC2/ISO) i jakie evidence? 
- Jakie SLA/okna dla patchy i reboots?


## Powiązania (meta)

- Key Documents: os_hardening_policy, iam_ssh_keys_policy, backup_and_recovery_procedure, monitoring_standards, incident_response_plan, change_management.
- Key Document Structures: build, konfiguracja, security, monitoring, backup, incydenty, lifecycle.
- Document Dependencies: IaC/provisioning tools, repo obrazów, CMDB, monitoring/logging, backup, access control, on-call roster.


## Zależności dokumentu

Wymaga standardów obrazów/IaC, polityk hardening/IAM, monitoring/logging profili, backup policy, CMDB i on-call. Bez tego DoR otwarte.


## Fazy cyklu życia

- Provisioning: build/IaC, konfiguracja, hardening, CMDB.
- Operacje: patching, monitoring, backup, capacity, zmiany.
- Incydenty: awarie hw/os/security, procedury, komunikacja.
- Decommission: backup/archive, wipe, CMDB, revokacje kluczy.



## Struktura sekcji (szkielet)
- Cel i kiedy używać runbooka
- Prerequisites (dostępy, sieć, narzędzia, wersje)
- Kroki podstawowe (numerowane, z oczekiwanym rezultatem)
- Walidacja / testy po wykonaniu
- Ścieżka awaryjna / rollback
- Eskalacja i kontakty
- Logowanie wykonania (co zapisać i gdzie)
## Szybkie powiązania

- linkage_index.jsonl (server/runbook)
- os_hardening_policy, iam_ssh_keys_policy, backup_and_recovery_procedure, monitoring_standards, incident_response_plan, change_management


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Uzupełnij standardy build/hardening i IAM/SSH.
2. Dodaj profile monitoring/backup i patching plan.
3. Wstaw checklisty provisioning/decommission i incydentowe.
4. Powiąż z CMDB/tagging i update po każdej zmianie; zamknij DoR/DoD.


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

- IaC, Golden Image, Hardening, Bastion, CMDB, Live patch, Wipe.


## Przykłady użycia

- Nowy serwer: IaC + golden image + hardening + monitoring + backup + CMDB wpis.
- Incydent dysk: alert → runbook → snapshot/restore → wymiana dysku → CMDB update.


## Ryzyka i ograniczenia

- Brak hardening/IAM → ryzyko security; brak backup/test restore → utrata danych; brak CMDB → chaos.


## Decyzje i uzasadnienia

- [Decyzja] Narzędzia IaC/monitoring/backup — uzasadnienie standardu i wsparcia.
- [Decyzja] Okna patchy i live patch — uzasadnienie SLA/ryzyka.


## Powiązania z innymi dokumentami

- OS Hardening, IAM/SSH Keys, Backup & Recovery, Monitoring Standards, Incident Response Plan, Change Mgmt.


## Powiązania z sekcjami innych dokumentów

- Security → hardening/IAM; Backup → restore; Incident Response → eskalacje; CMDB/Change → wpisy.


## Słownik pojęć w dokumencie

- IaC, Golden Image, Hardening, Bastion, CMDB, Live patch, Wipe.


## Wymagane odwołania do standardów

- CIS benchmarki, wewnętrzne polityki security/IAM, standardy compliance (SOC2/ISO) jeśli dotyczy.


## Mapa relacji sekcja→sekcja

- Build → Hardening/IAM → Monitoring/Backup → Patching → Incydenty → Decommission.


## Mapa relacji dokument→dokument

- Server Runbook → Security/Backup/Monitoring → Change/Incident → Audit/CMDB.


## Ścieżki informacji

- Build/IaC → Konfiguracja → Monitoring/Backup → Patching → Incydent/Decommission.


## Weryfikacja spójności

- [ ] Checklisty kompletne; monitoring/backup/test restore opisane; CMDB aktualne.
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy serwer ma build/hardening, monitoring, backup, CMDB wpis, plan patch/decommission.
- [ ] Każdy incydent ma playbook i kontakty; każda zmiana ma wpis w CMDB/change.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- IaC/golden image, checklisty, monitoring/alert config, backup policy, incident playbooks, CMDB wpisy.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- SRE/Infra → Security/Compliance → Ops/Support → Owner sign‑off.


## Metryki jakości

- Czas provisioningu, wskaźnik sukcesu patchy, backup/restore success, liczba incydentów security/os/hw, kompletność CMDB.

## Kryteria ukończenia

- [ ] Runbook kompletny; monitoring/backup/patch/CMDB opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Build/IaC → Konfiguracja/Hardening → Monitoring/Backup → Incydenty → CMDB.
- IAM/SSH → Incydenty security → Audyt/logi.


## Struktura sekcji

1) Standardy build/provisioning (obrazy, IaC, sieć/storage)  
2) Konfiguracja i hardening (pakiety, firewall, auditd, logrotate, sysctl)  
3) IAM/SSH/klucze (dostępy, rotacje, bastion)  
4) Monitoring/logi/alerty (metryki, logi, progi, kanały)  
5) Backup/snapshot/restore (zakres, częstotliwość, testy)  
6) Patching i maintenance (okna, automatyzacja, reboots, kernel live patch)  
7) Capacity i lifecycle (commission/decommission, tagging, CMDB)  
8) Incydenty i runbooki (hw/os/security, komunikacja, eskalacje)  
9) Dokumentacja i audyt (log zmian, evidence)  
10) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Checklisty provisioning/patching/decommission; profile monitoring/alertów; backup/test restore.
- Procedury incydentów hw/os/security; ścieżki eskalacji i komunikaty.
- CMDB/tagging wymagania i audyt dostępu/kluczy.


## Wymagane streszczenia

- Standard build/konfiguracji, monitoring/alerty, backup/patching, incydenty krytyczne i kontakty.


## Guidance (skrót)

- Używaj IaC i złotych obrazów; enforce hardening i IAM/SSH polityki.
- Monitoruj metryki (CPU/RAM/dysk/sieć), logi i backupy; testuj restore.
- Patching automatyzuj; kernel live patch gdy wymagane SLA.
- CMDB/tagging aktualizuj przy każdej zmianie; decommission z wipe i revokacją kluczy.
- Incydenty: przygotuj playbooki hw/os/security; eskalacje i komunikacja jasne.


## Checklisty Definition of Ready (DoR)

- [ ] Standard obrazu/IaC i hardening dostępne; IAM/SSH polityki gotowe.
- [ ] Monitoring/logging/backup profile zdefiniowane; CMDB/tagging działa.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Runbook zawiera checklisty provisioning/patching/decommission i incydenty.
- [ ] Monitoring/alerty/backup/test restore opisane; CMDB/tagging zaktualizowane.
- [ ] Eskalacje/kontakty podane; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

