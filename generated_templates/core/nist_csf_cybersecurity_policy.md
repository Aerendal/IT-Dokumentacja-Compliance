---
title: "Polityka Cyberbezpieczeństwa (NIST CSF)"
status: aktywny
aligned: NIST CSF
---

## Cel dokumentu
Zdefiniować zasadniczą politykę cyberbezpieczeństwa organizacji strukturyzowaną wokół 6 funkcji NIST Cybersecurity Framework 2.0 (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER). Polityka wyraża zaangażowanie kierownictwa w zarządzanie ryzykiem cybernetycznym, ustala zakres programu cyberbezpieczeństwa, role odpowiedzialności (CISO, Risk Owner, Security Operations) i cele bezpieczeństwa wyrażone jako pożądany profil docelowy (Target Profile) NIST CSF.

## Zakres i granice
Polityka obejmuje całą organizację, wszystkie systemy informacyjne, infrastrukturę IT/OT, łańcuch dostaw i usługi zewnętrzne. Dotyczy pracowników, wykonawców i dostawców z dostępem do systemów organizacji.

## Wejścia i wyjścia
**Wejścia:**
- Current Profile NIST CSF (obecny poziom cyberbezpieczeństwa)
- Apetyt na ryzyko organizacji (Board-level decision)
- Wymagania regulacyjne (DORA, NIS2, KSC, NIST SP 800-53)
- Raporty z oceny ryzyka cybernetycznego

**Wyjścia:**
- Zatwierdzona polityka cyberbezpieczeństwa
- Target Profile NIST CSF — pożądany stan bezpieczeństwa
- Priorytety inwestycyjne cyberbezpieczeństwa

## Zasady polityki cyberbezpieczeństwa

### GOVERN (GV) — Zarządzanie cyberbezpieczeństwem
- Cyberbezpieczeństwo jest priorytetem strategicznym zatwierdzonnym przez Zarząd
- Ryzyko cybernetyczne jest zarządzane w ramach Enterprise Risk Management
- Role i odpowiedzialności cyberbezpieczeństwa są udokumentowane (RACI)
- Dostawcy i partnerzy spełniają wymagania bezpieczeństwa organizacji (Cybersecurity Supply Chain Risk Management)

### IDENTIFY (ID) — Identyfikacja
- Inwentarz aktywów jest utrzymywany i aktualizowany (hardware, software, dane)
- Ryzyko cybernetyczne jest oceniane regularnie (minimum rocznie) i po istotnych zmianach
- Polityki, procedury i plany bezpieczeństwa są zdefiniowane i zakomunikowane
- Ramy prawne i regulacyjne dotyczące cyberbezpieczeństwa są zidentyfikowane

### PROTECT (PR) — Ochrona
- Tożsamość i dostęp: MFA, zasada least privilege, przeglądy dostępu
- Szkolenia: regularne szkolenia cyberbezpieczeństwa dla wszystkich pracowników
- Ochrona danych: szyfrowanie, DLP, backup i weryfikacja odtwarzania
- Zabezpieczenie platform: hardening, patch management, konfiguracja bezpieczna
- Resilience: redundancja krytycznej infrastruktury

### DETECT (DE) — Wykrywanie
- Monitoring bezpieczeństwa: SIEM/SOC z regułami detekcji aktualnych zagrożeń
- Alerty anomalii: systemy EDR/XDR na urządzeniach końcowych
- Monitorowanie ciągłe: logi bezpieczeństwa przechowywane minimum 12 miesięcy
- Testy penetracyjne i Red Team: minimum raz w roku

### RESPOND (RS) — Reagowanie
- Incident Response Plan (IRP) jest udokumentowany i testowany
- Zespół reagowania (CSIRT/IRT) jest wyznaczony i przeszkolony
- Komunikacja w incydentach: do kierownictwa, regulatorów, mediów (Tabletop Exercise)
- Analiza głównych przyczyn (RCA) po każdym poważnym incydencie

### RECOVER (RC) — Odtwarzanie
- Plany odtwarzania (DRP/BCP) są udokumentowane i testowane
- Priorytety odtwarzania: systemy krytyczne pierwsza kolejność
- Komunikacja po incydencie: lekcje wyciągnięte wdrożone w politykach

## Cele cyberbezpieczeństwa (Target Profile)

| Funkcja NIST CSF | Obecny poziom (Tier) | Cel docelowy (Tier) | Termin |
|-----------------|---------------------|---------------------|--------|
| GOVERN | Tier [1-4] | Tier [2-4] | [Data] |
| IDENTIFY | Tier [1-4] | Tier [2-4] | [Data] |
| PROTECT | Tier [1-4] | Tier [2-4] | [Data] |
| DETECT | Tier [1-4] | Tier [2-4] | [Data] |
| RESPOND | Tier [1-4] | Tier [2-4] | [Data] |
| RECOVER | Tier [1-4] | Tier [2-4] | [Data] |

*Tier 1: Partial, Tier 2: Risk Informed, Tier 3: Repeatable, Tier 4: Adaptive*

## Role i odpowiedzialności

| Rola | Odpowiedzialność |
|------|-----------------|
| **Zarząd** | Zatwierdzenie polityki, akceptacja ryzyka cybernetycznego |
| **CISO** | Właściciel programu cyberbezpieczeństwa, reporting do Zarządu |
| **Risk Manager** | Ocena ryzyka cybernetycznego, rejestr ryzyk |
| **Security Operations (SOC)** | Monitoring, detekcja, reagowanie na incydenty |
| **IT Operations** | Wdrożenie kontroli technicznych, patch management |
| **HR** | Szkolenia, offboarding bezpieczeństwo |
| **Wszyscy pracownicy** | Przestrzeganie polityki, zgłaszanie incydentów |

## Naruszenia i egzekwowanie
Naruszenia polityki cyberbezpieczeństwa są traktowane poważnie i mogą skutkować: działaniami dyscyplinarnymi, odpowiedzialnością prawną, eskalacją do organów ścigania. Zgłaszanie podejrzanych zdarzeń: **[e-mail/kanał zgłoszeń]**

## Powiązania (meta)
- standardy-i-compliance: NIST CSF 2.0, NIST SP 800-53 Rev 5, NIS2 Art. 21, DORA Art. 6, ISO/IEC 27001
- raci-i-role: Zarząd (Approver), CISO (Owner), Security Manager (Author), wszyscy pracownicy (Informed)
