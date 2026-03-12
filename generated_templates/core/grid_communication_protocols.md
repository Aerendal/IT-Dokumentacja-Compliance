---
title: Grid Communication Protocols
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Grid Communication Protocols


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje stosowane protokoły komunikacyjne w sieciach energetycznych (smart grid/SCADA/AMI) oraz ich wymagania bezpieczeństwa, interoperacyjność, monitoring i zgodność. Ma zapewnić niezawodną, bezpieczną i zgodną komunikację w sieci.


## Zakres i granice

- Obejmuje: protokoły (IEC 61850, DNP3, Modbus, MQTT, DLMS/COSEM, OPC UA), profile bezpieczeństwa (TLS/VPN, auth, certy), topologie (RTU/IED/GW/Headend), wymagania latency/reliability, time sync (PTP/NTP), addressing/namespace, interoperacyjność, testy zgodności, monitoring i alerty, zarządzanie kluczami/certami, regulacje sektorowe.
- Poza zakresem: projekt fizycznej sieci/medium (RF/PLC/FO) – linkowane; szczegółowy design OT security (oddzielny dokument).


## Użytkownicy i interesariusze

- OT/Network, Security, Compliance/Regulator, Operations, Vendors.


## Wejścia i wyjścia

- Wejścia: architektura grid/OT, lista urządzeń i ról (RTU/IED/Headend), wymagania regulatora (np. NERC CIP), polityka bezpieczeństwa OT, profile latency/reliability, istniejące protokoły i wersje, wymagania integracyjne (EMS/DMS/MDMS), time sync wymagania.
- Wyjścia: wybór/profil protokołów, wymagania bezpieczeństwa, wytyczne interoperacyjności, plan testów zgodności i monitoring, zasady kluczy/certów, mapowanie do architektury i urządzeń.


## Założenia

- Możliwość konfiguracji urządzeń; dostęp do PKI i lab; wsparcie regulatora.


## Otwarte pytania

- Jakie wersje protokołów są dopuszczalne przez regulatora/utility? 
- Czy wymagane są lokalne CA czy centralne?


## Powiązania (meta)

- Key Documents: ot_security_baseline, time_sync_policy, device_onboarding_ot, integration_guidelines_ot, regulatory_compliance_architecture (ot), network_segmentation_ot.
- Key Document Structures: protokoły, bezpieczeństwo, interoperacyjność, testy, monitoring.
- Document Dependencies: inventory OT, PKI/certy, NMS/monitoring, lab do testów, regulator requirements.


## Zależności dokumentu

Wymaga inwentarza urządzeń/rol, wymagań regulatora, polityk OT security, PKI/certy, mapy integracji EMS/DMS/MDMS, time sync. Bez tego DoR otwarte.


## Fazy cyklu życia

- Analiza: urządzenia/protokoly/wymagania/regulacje.
- Projekt: wybór profilów/protokołów, bezpieczeństwo, time sync, namespace.
- Testy: interoperacyjność, zgodność, bezpieczeństwo, latency.
- Wdrożenie: konfiguracje, certy/klucze, monitoring/alerty.
- Operacje: rotacje certów, aktualizacje wersji, audyty, monitoring.



## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (ot/grid_protocols)
- ot_security_baseline, time_sync_policy, device_onboarding_ot, integration_guidelines_ot, regulatory_compliance_architecture, network_segmentation_ot


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

1. Zbierz inwentarz i wymagania/regulacje; wybierz protokoły/profil.
2. Zdefiniuj bezpieczeństwo/time sync/namespace; przygotuj testy.
3. Wdróż z certami/monitoringiem; aktualizuj dokument i linkage_index.


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

- IEC 61850, DNP3, Modbus, MQTT, DLMS/COSEM, OPC UA, PTP, NTP, PKI.


## Przykłady użycia

- AMI: DLMS/COSEM + TLS, headend z cert rotacją, monitoring cert expiry i latency.
- SCADA: DNP3-SA, PTP sync, OPC UA do integracji EMS, test conformance w labie.


## Ryzyka i ograniczenia

- Legacy/cleartext protokoły → ryzyko; brak rotacji certów → awarie; brak testów → brak interoperacyjności.


## Decyzje i uzasadnienia

- [Decyzja] Protokoły i profile — uzasadnienie urządzeń/regulacji.
- [Decyzja] PKI/time sync — uzasadnienie SLA/bezpieczeństwa.


## Powiązania z innymi dokumentami

- OT Security Baseline, Time Sync Policy, Device Onboarding OT, Integration Guidelines OT, Regulatory Compliance Architecture, Network Segmentation OT.


## Powiązania z sekcjami innych dokumentów

- Security → TLS/auth; Time Sync → PTP/NTP; Integration → OPC UA/namespace.


## Słownik pojęć w dokumencie

- IEC 61850, DNP3, Modbus, MQTT, DLMS/COSEM, OPC UA, PTP, NTP, PKI.


## Wymagane odwołania do standardów

- IEC/EN standardy, NERC CIP (jeśli dotyczy), wytyczne regulatora lokalnego.


## Mapa relacji sekcja→sekcja

- Protokoły → Bezpieczeństwo → Interoperacyjność → Testy → Monitoring → Audyt.


## Mapa relacji dokument→dokument

- Grid Protocols → OT Security/Integration/Compliance → Monitoring/Operations.


## Ścieżki informacji

- Wymagania → Wybór protokołu → Bezpieczeństwo → Testy → Wdrożenie → Monitoring.


## Weryfikacja spójności

- [ ] Protokoły/profil bezpieczeństwa/time sync spójne z wymaganiami; testy/monitoring opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy protokół ma profil security/time sync/testy/monitoring i owner.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Konfiguracje protokołów, profile bezpieczeństwa, testy conformance, raporty monitoringu, PKI polityki.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- OT/Network → Security/Compliance → Regulator (jeśli dot.) → Owner sign‑off.


## Metryki jakości

- Uptime/latency komunikacji, cert expiry incidents, liczba luk/legacy protokołów, wyniki testów conformance, incydenty bezpieczeństwa OT.

## Kryteria ukończenia

- [ ] Protokoły/profil bezpieczeństwa/time sync opisane; testy i monitoring gotowe; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Protokoły → Bezpieczeństwo → Interoperacyjność → Testy → Monitoring.
- Time sync → Latency/reliability → SLA.


## Struktura sekcji

1) Zakres i architektura OT (urządzenia, role, topologia)  
2) Protokoły i profile (IEC 61850, DNP3, Modbus, MQTT, DLMS/COSEM, OPC UA)  
3) Bezpieczeństwo (TLS/VPN, auth, certy/PKI, hardening, secure defaults)  
4) Time sync i QoS (PTP/NTP, latency, jitter, SLA)  
5) Interoperacyjność i namespace (mapowanie, modele danych, profilowanie)  
6) Testy zgodności i bezpieczeństwa (lab, conformance, fuzzing)  
7) Monitoring i alerty (health, errors, latency, cert expiry)  
8) Zarządzanie kluczami/certami i cykl życia (provisioning, rotacja, revoke)  
9) Regulacje i audyt (NERC CIP/IEC/EN), dokumentacja, ryzyka, decyzje


## Wymagane rozwinięcia

- Wybór protokołów per rola/urządzenie; profile bezpieczeństwa i time sync.
- Test plan conformance/interoperacyjność/bezpieczeństwo; monitoring KPI.
- Zasady PKI/certy (CA, rotacja, CRL/OCSP) i zarządzanie wersjami protokołów.


## Wymagane streszczenia

- Wybrane protokoły/profile, wymagania bezpieczeństwa/time sync, plan testów i monitoring.


## Guidance (skrót)

- Preferuj bezpieczne warianty (DNP3-SA, TLS, auth); minimalizuj plaintext.
- Uzgodnij profile/namespace i testuj interoperacyjność w labie przed wdrożeniem.
- Zapewnij PTP/NTP wg wymagań latency; monitoruj cert expiry i błędy protokołu.


## Checklisty Definition of Ready (DoR)

- [ ] Inwentarz OT i wymagania regulatora; polityki OT security/time sync dostępne.
- [ ] Lab/test tools i PKI/certy dostępne; struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Protokoły/profil bezpieczeństwa/time sync opisane; testy zaplanowane/wykonane.
- [ ] Monitoring/alerty i PKI/certy cykl życia opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.

