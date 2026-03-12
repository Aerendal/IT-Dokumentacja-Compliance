---
title: "Availability Policy"
status: aktywny
aligned: SOC 2
---

## Cel dokumentu
Zdefiniować politykę dostępności systemów i usług IT zgodnie z SOC 2 Trust Services Criteria (TSC) A1 — Availability. Polityka ustanawia wymagania dotyczące zapewnienia że systemy są dostępne w sposób zobowiązany przez umowy SLA: definiuje cel dostępności (Availability SLO), wymagania dotyczące monitorowania, procedury obsługi awarii (incident management), plany odtwarzania po awarii (DRP) i testowania gotowości — adresując ryzyko przerw w dostępności usług dla użytkowników i partnerów.

## Zakres i granice
Polityka obejmuje wszystkie systemy produkcyjne objęte zakresem audytu SOC 2, w tym: aplikacje SaaS, infrastrukturę cloud, API, bazy danych i usługi zależne. Dotyczy wszystkich pracowników zaangażowanych w utrzymanie systemów i reagowanie na awarie.

## Wejścia i wyjścia
**Wejścia:**
- Umowy SLA z klientami (Customer Agreements)
- Risk Assessment dotyczący dostępności
- Inwentarz systemów i infrastruktury
- Wyniki testów DRP/BCP

**Wyjścia:**
- Zatwierdzona polityka dostępności
- SLO (Service Level Objectives) — wewnętrzne cele dostępności
- Dowody monitorowania uptime dla audytora SOC 2

## Cele dostępności (Availability Commitments)

### Service Level Objectives
| System/Usługa | SLO Uptime | Okno serwisowe | RTO | RPO |
|--------------|------------|---------------|-----|-----|
| [Aplikacja główna] | 99.9% (8.7h/rok dopuszczalnego downtime) | Niedziela 02:00-06:00 | 4h | 1h |
| [API] | 99.95% | Niedziela 02:00-04:00 | 2h | 15min |
| [Baza danych] | 99.9% | Niedziela 02:00-04:00 | 4h | 1h |

### Wyłączenia z SLA
- Planowane okna serwisowe (z 48h notyfikacją)
- Zdarzenia force majeure
- Awarie po stronie klienta lub dostawców trzecich

## Wymagania techniczne dostępności

### Redundancja i wysoká dostępność
- Środowisko produkcyjne: multi-AZ (multi-Availability Zone) deployment
- Baza danych: replikacja synchroniczna (primary + replica), automatic failover
- Load balancer: active-active, health checks co 30 sekund
- CDN: dla zasobów statycznych i API regionalne (edge caching)

### Backupy i odtwarzanie
- Backupy pełne: codziennie, retencja 30 dni
- Backupy przyrostowe: co 4 godziny, retencja 7 dni
- Backupy offsite: szyfrowane kopie do innego regionu/providera
- Test odtwarzania: minimum raz na kwartał (udokumentowany wynik)

### Monitorowanie dostępności
- Synthetic monitoring z zewnętrznych lokalizacji: co 1 minuta
- Health endpoints: /health lub /status per serwis
- Alerting: PagerDuty/OpsGenie z eskalacją per severity
- Dashboard dostępności: widoczny dla klientów (Status Page)

## Incident Management (Availability)

### Klasyfikacja incydentów dostępności
| Severity | Wpływ | Response Time | Resolution Time |
|----------|-------|---------------|----------------|
| P1 (Critical) | Całkowity brak dostępności | 15 minut | 4 godziny |
| P2 (High) | Degradacja >50% użytkowników | 30 minut | 8 godzin |
| P3 (Medium) | Degradacja <50% użytkowników | 2 godziny | 24 godziny |

### Komunikacja podczas incydentu
- Wewnętrzna: kanał #incidents w komunikatorze
- Klientów: Status Page aktualizacja w ciągu 30 minut od P1/P2
- Key accounts: bezpośredni kontakt w ciągu 1 godziny od P1

## Disaster Recovery

### Strategia DRP
- Primary: [Region AWS/Azure/GCP]
- DR Site: [Inny region/provider]
- Failover: automatyczny (dla bazy) lub manualny (dla aplikacji) z RTO < [X]h

### Testy DRP
- Pełny DR Test: raz w roku (failover + failback)
- Tabletop Exercise: co kwartał
- Wyniki testów są dokumentowane i archiwizowane jako dowód dla audytora SOC 2

## Powiązania (meta)
- standardy-i-compliance: SOC 2 TSC Availability (A1.1–A1.3), ISO 22301, DORA Art. 11
- raci-i-role: CTO (Approver), Infrastructure Lead (Owner), DevOps/SRE (Responsible), Customer Success (Informed)
