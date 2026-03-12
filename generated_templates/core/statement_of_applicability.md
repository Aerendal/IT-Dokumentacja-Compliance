---
title: "Deklaracja Stosowania Zabezpieczeń (Statement of Applicability — SoA)"
status: aktywny
aligned: ISO/IEC 27001
---

## Cel dokumentu
Udokumentować decyzje dotyczące stosowania lub wyłączenia każdej z 93 kontroli bezpieczeństwa z ISO/IEC 27001:2022 Annex A — jako obowiązkowa informacja udokumentowana ISMS wymagana przez klauzula 6.1.3d. SoA jest kluczowym artefaktem certyfikacji: pokazuje audytorowi które kontrole są wdrożone, dlaczego wybrane, z jakim uzasadnieniem wyłączone i jakie są cele kontroli — łącząc wyniki Risk Treatment Plan z konkretnymi implementacjami.

## Zakres i granice
SoA obejmuje wszystkie 93 kontrole z ISO/IEC 27001:2022 Annex A (pogrupowane w 4 tematy: Organizational, People, Physical, Technological). Dla każdej kontroli: status (wdrożona/planowana/wyłączona), uzasadnienie wyboru i odniesienie do dowodów wdrożenia.

## Wejścia i wyjścia
**Wejścia:**
- Risk Assessment i Risk Treatment Plan (klauzula 6.1.2 i 6.1.3)
- Wymagania prawne, regulacyjne i kontraktowe
- Zakres ISMS (Scope Statement)
- Istniejące kontrole bezpieczeństwa w organizacji

**Wyjścia:**
- Kompletna SoA — informacja udokumentowana do certyfikacji ISO/IEC 27001
- Lista wdrożonych kontroli z dowodami (policy/procedure/record)
- Lista wyłączonych kontroli z uzasadnieniem dla audytora

## Legenda statusów
| Status | Opis |
|--------|------|
| **Wdrożona** | Kontrola jest w pełni zaimplementowana z dowodem |
| **Planowana** | Kontrola jest zaplanowana do wdrożenia (z datą) |
| **Wyłączona** | Kontrola nie ma zastosowania — uzasadnienie wymagane |

## Temat 5 — Kontrole Organizacyjne (37 kontroli)

| Kontrola | Tytuł | Status | Uzasadnienie / Dowód |
|----------|-------|--------|---------------------|
| 5.1 | Polityki bezpieczeństwa informacji | **[Wdrożona]** | Polityka ISMS v[X.Y], zatwierdzona [data] |
| 5.2 | Role i odpowiedzialności w bezpieczeństwie | **[Wdrożona]** | Opis stanowisk + RACI matrix |
| 5.3 | Rozdzielność obowiązków | **[Wdrożona/Planowana/Wyłączona]** | [Uzasadnienie] |
| 5.4 | Odpowiedzialności zarządcze | **[Wdrożona]** | Management Review Minutes |
| 5.5 | Kontakty z organami władzy | **[Wdrożona]** | Lista kontaktów emergency: CERT, UKE, UODO |
| 5.6 | Kontakty z grupami szczególnych zainteresowań | **[Wdrożona]** | Członkostwo w ISAC/CERT |
| 5.7 | Threat intelligence | **[Wdrożona/Wyłączona]** | [Uzasadnienie] |
| 5.8 | Bezpieczeństwo informacji w zarządzaniu projektami | **[Wdrożona]** | Security Checkpoint w SDLC |
| ... | *(kontynuuj dla 5.9–5.37)* | | |

## Temat 6 — Kontrole Dotyczące Ludzi (8 kontroli)

| Kontrola | Tytuł | Status | Uzasadnienie / Dowód |
|----------|-------|--------|---------------------|
| 6.1 | Screening (weryfikacja kandydatów) | **[Wdrożona]** | Procedura HR + background check |
| 6.2 | Warunki zatrudnienia | **[Wdrożona]** | Klauzule NDA/bezpieczeństwo w umowach |
| 6.3 | Szkolenia bezpieczeństwa | **[Wdrożona]** | Program szkoleń + dowody ukończenia |
| 6.4 | Proces dyscyplinarny | **[Wdrożona]** | Regulamin pracy |
| 6.5 | Odpowiedzialności po rozwiązaniu umowy | **[Wdrożona]** | Offboarding checklist |
| 6.6 | Umowy o zachowaniu poufności | **[Wdrożona]** | Wzór NDA |
| 6.7 | Praca zdalna | **[Wdrożona]** | Polityka pracy zdalnej + VPN |
| 6.8 | Raportowanie zdarzeń bezpieczeństwa | **[Wdrożona]** | Kanał zgłoszeń + procedura IH |

## Temat 7 — Kontrole Fizyczne (14 kontroli)

| Kontrola | Tytuł | Status | Uzasadnienie / Dowód |
|----------|-------|--------|---------------------|
| 7.1–7.14 | *(wymienić wszystkie 14 kontroli fizycznych)* | **[Status]** | [Dowód] |

## Temat 8 — Kontrole Technologiczne (34 kontrole)

| Kontrola | Tytuł | Status | Uzasadnienie / Dowód |
|----------|-------|--------|---------------------|
| 8.1 | Urządzenia końcowe użytkownika | **[Wdrożona]** | Polityka MDM/endpoint |
| 8.2 | Uprzywilejowane prawa dostępu | **[Wdrożona]** | PAM solution + zasada least privilege |
| 8.3 | Ograniczenie dostępu do informacji | **[Wdrożona]** | RBAC + recenzje dostępu |
| ... | *(kontynuuj dla 8.4–8.34)* | | |

## Podsumowanie
| Kategoria | Wdrożone | Planowane | Wyłączone | Razem |
|-----------|----------|-----------|-----------|-------|
| Organizacyjne (5.x) | [X] | [X] | [X] | 37 |
| Dotyczące ludzi (6.x) | [X] | [X] | [X] | 8 |
| Fizyczne (7.x) | [X] | [X] | [X] | 14 |
| Technologiczne (8.x) | [X] | [X] | [X] | 34 |
| **RAZEM** | **[X]** | **[X]** | **[X]** | **93** |

## Powiązania (meta)
- standardy-i-compliance: ISO/IEC 27001:2022 klauzula 6.1.3d, ISO/IEC 27002:2022 (guidance do każdej kontroli)
- raci-i-role: CISO (Owner/Approver), Security Manager (Author), Risk Manager (Consulted), audytor certyfikujący (Reviewer)
