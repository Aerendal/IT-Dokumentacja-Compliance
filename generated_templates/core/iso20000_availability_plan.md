---
title: "Availability Plan"
status: aktywny
aligned: ISO 20000-1
---

# Availability Plan

## Cel dokumentu
Opisać plan zarządzania dostępnością usług IT zgodnie z ISO 20000-1:2018 klauzula 8.3 (Service Availability, Service Continuity and Service Level Management). Plan definiuje: cele dostępności dla każdej usługi (Availability Targets), architekturę techniczną zapewniającą wymaganą dostępność, procesy monitorowania i raportowania dostępności, plan poprawy dostępności (Availability Improvement Plan) oraz zarządzanie zdarzeniami wpływającymi na dostępność — zapewniając spełnienie zobowiązań SLA wobec klientów.

## Zakres i granice
Plan obejmuje wszystkie usługi objęte zakresem SMS (Service Management System) organizacji. Jest integralną częścią Service Management Plan (SMP) i wchodzi w interakcję z Capacity and Performance Plan, IT Service Continuity Plan i Incident Management.

## Wejścia i wyjścia
**Wejścia:**
- Service Level Agreements (SLA) z klientami — wymagania dostępności
- Service Catalogue — lista zarządzanych usług
- Incident Records i Problem Records (historyczne dane dostępności)
- Configuration Management Database (CMDB)

**Wyjścia:**
- Zatwierdzony Availability Plan — informacja udokumentowana SMS
- Availability Targets per usługa (do umieszczenia w SLA)
- Availability Reports (miesięczne/kwartalne raportowanie)
- Availability Improvement Actions (wejście do CSI Register)

## Cele dostępności usług (Availability Targets)

| Usługa | Godziny usługi | Cel dostępności | Max dopuszczalny przestój/rok | Metoda pomiaru |
|--------|---------------|-----------------|-------------------------------|----------------|
| [Usługa A] | 24x7 | 99.9% | 8.7 godzin | Monitoring synthetics |
| [Usługa B] | 08:00-18:00 pn-pt | 99.5% | 25.2 godzin | Service desk tickets |
| [Usługa C] | 24x7 | 99.95% | 4.4 godziny | APM (Application Performance Monitoring) |

**Definicja dostępności:**
```
Dostępność (%) = ((Łączny czas usługi − Czas niedostępności) / Łączny czas usługi) × 100
```
Planowane okna serwisowe (uzgodnione z klientem) są wyłączone z pomiaru niedostępności.

## Architektura dostępności

### Komponenty krytyczne i ich redundancja
| Komponent | Architektura | SPOF (Single Point of Failure) | Mitygacja |
|-----------|-------------|-------------------------------|-----------|
| Web tier | Active-Active Load Balancer | Brak | Redundantne LB w dwóch DC |
| App tier | Clustered (min. 2 nodes) | Brak | Auto-scaling |
| Database | Primary + synchronous replica | Brak | Automatic failover <30s |
| Network | Dual uplink, BGP redundancja | Brak | Automatic failover |
| DC / hosting | Colocation lub multi-AZ | Brak | DR site |

### Planned Maintenance Windows
- Miesięczne okno serwisowe: **[Niedziela 02:00-06:00 CET]**
- Powiadomienie klientów: minimum **48 godzin** przed planowanym oknem
- Procedura change management: Change Request (Normal/Standard) wymagany

## Monitorowanie dostępności

### Narzędzia i metryki
| Metryka | Narzędzie | Interwał | Alert Threshold |
|---------|----------|---------|----------------|
| Availability (%) | [Pingdom/Datadog/Zabbix] | co 1 min | < SLO target |
| Response time (TTFB) | [APM tool] | co 1 min | > [X] ms |
| Error rate | [APM/logging] | real-time | > 1% requests |
| Infrastructure health | [monitoring platform] | co 5 min | CPU>80%, Mem>85% |

### Raportowanie dostępności
- Raport miesięczny do klienta: do 5. dnia następnego miesiąca
- SLA breach notification: natychmiast po wykryciu (automatyczny alert)
- Przegląd kwartalny z klientem: trend dostępności + plan poprawy

## Zarządzanie zdarzeniami dostępności

### Klasyfikacja wpływu na dostępność
| Klasa | Wpływ | Czas reakcji | Eskalacja |
|-------|-------|-------------|-----------|
| Critical | Całkowita niedostępność usługi | 15 min | Service Manager + klient |
| Major | Niedostępność >50% użytkowników | 30 min | Service Manager |
| Minor | Degradacja wydajności | 2 h | On-call engineer |

### Procedura po incydencie
1. Incident Record — udokumentowanie szczegółów przestoju
2. Root Cause Analysis (Problem Management) — jeśli P1/P2
3. Availability Incident Report — raport dla klienta jeśli naruszono SLA
4. Aktualizacja Availability Improvement Plan

## Availability Improvement Plan

| Zidentyfikowana luka | Działanie naprawcze | Właściciel | Termin | Status |
|---------------------|---------------------|-----------|--------|--------|
| [Single Point of Failure X] | [Redundancja / failover] | [IT Ops] | [Data] | [Planowane] |
| [Niedostateczny monitoring Y] | [Wdrożenie synthetic monitoring] | [NOC] | [Data] | [W trakcie] |

## Przegląd planu
Availability Plan jest przeglądany:
- Corocznie (planowy przegląd SMS)
- Po każdym poważnym incydencie dostępności
- Przy zmianie wymagań SLA klientów

## Powiązania (meta)
- standardy-i-compliance: ISO 20000-1:2018 klauzula 8.3, ITIL 4 Availability Management Practice, SOC 2 TSC A1
- raci-i-role: Service Manager (Owner/Approver), IT Operations (Responsible), Account Manager (Consulted), klienci (Informed via SLA)
