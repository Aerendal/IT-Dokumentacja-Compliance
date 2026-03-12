---
title: "Polityka Systemu Zarządzania Ciągłością Działania (BCMS)"
status: aktywny
aligned: ISO 22301
---

## Cel dokumentu
Ustanowić i zatwierdzić politykę Systemu Zarządzania Ciągłością Działania (BCMS) organizacji jako wymaganie ISO 22301 klauzula 5.3 (Business Continuity Policy). Polityka określa: zaangażowanie kierownictwa w ochronę ciągłości działania, zakres BCMS (produkty, usługi, lokalizacje, procesy), cele ciągłości (RTO/RPO dla krytycznych usług), zobowiązanie do spełnienia wymagań i ciągłego doskonalenia BCMS — stanowiąc nadrzędny dokument systemu.

## Zakres i granice
Dokument obowiązuje wszystkie jednostki organizacyjne, procesy, usługi i zasoby objęte zakresem BCMS. Zakres BCMS należy zdefiniować zgodnie z ISO 22301 klauzula 4.3 (Scope of the BCMS).

## Wejścia i wyjścia
**Wejścia:**
- Kontekst organizacji (klauzula 4.1 ISO 22301)
- Potrzeby i oczekiwania zainteresowanych stron (klauzula 4.2)
- Analiza wpływu na działalność (BIA) i ocena ryzyka
- Wymagania prawne i regulacyjne dotyczące ciągłości działania

**Wyjścia:**
- Zatwierdzona polityka BCMS — komunikowana w organizacji i podmiotom zewnętrznym
- Cele ciągłości działania (RTO, RPO, MBCO dla krytycznych usług)
- Zakres BCMS do rejestracji jako informacja udokumentowana

## Właściciel i zatwierdzone przez
| Rola | Osoba |
|------|-------|
| Właściciel polityki | **[CISO / Dyrektor ds. Ryzyka]** |
| Zatwierdzone przez | **[Zarząd / CEO]** |
| Recenzent | **[BCM Manager]** |

## Zobowiązania polityki

### Zaangażowanie kierownictwa
Kierownictwo wyższego szczebla zobowiązuje się do:
- Zapewnienia zasobów niezbędnych do wdrożenia i utrzymania BCMS
- Promowania kultury ciągłości działania w całej organizacji
- Przeglądania i zatwierdzania wyników testów BCMS
- Podejmowania decyzji o uruchomieniu planów ciągłości działania

### Zakres BCMS
BCMS obejmuje:
- **Produkty i usługi:** [Wymienić krytyczne produkty/usługi]
- **Lokalizacje:** [Główna siedziba, data center, lokalizacje backup]
- **Procesy krytyczne:** [Wymienić procesy z BIA > RTO X godzin]
- **Łańcuch dostaw:** [Kluczowi dostawcy krytycznych usług]

### Cele ciągłości działania
| Usługa krytyczna | RTO | RPO | MBCO |
|-----------------|-----|-----|------|
| [Usługa 1] | [Xh] | [Xh] | [X%] |
| [Usługa 2] | [Xh] | [Xh] | [X%] |

*RTO = Recovery Time Objective, RPO = Recovery Point Objective, MBCO = Minimum Business Continuity Objective*

### Zasady systemu BCMS
1. Ciągłość działania jest priorytetem zarządczym — nie wyłącznie technicznym
2. Plany ciągłości działania są testowane minimum raz w roku
3. Wszyscy pracownicy są przeszkoleni w zakresie procedur awaryjnych
4. Wnioski z testów i incydentów są wdrażane jako ulepszenia BCMS
5. BCMS jest przeglądany przez kierownictwo minimum raz w roku

## Struktura systemu BCMS
- **BIA (Business Impact Analysis):** identyfikacja krytycznych procesów i ich zależności
- **Risk Assessment:** ocena ryzyk zagrażających ciągłości działania
- **BCP (Business Continuity Plan):** plany reagowania i odtwarzania
- **DRP (Disaster Recovery Plan):** odtwarzanie infrastruktury IT
- **Crisis Communication Plan:** komunikacja w sytuacjach kryzysowych
- **Exercise Programme:** program testów i ćwiczeń BCMS

## Wymagania prawne i regulacyjne
| Wymaganie | Zakres |
|-----------|--------|
| ISO 22301:2019 | Standard BCMS |
| [KSC — ustawa o KSC] | Operator Usługi Kluczowej |
| [NIS2] | Podmioty kluczowe/ważne |
| [Wymagania sektorowe] | [np. KNF, rekomendacja W] |

## Przegląd i aktualizacja
- Przegląd planowy: corocznie przez BCM Manager
- Przegląd nieplanowy: po poważnym incydencie lub zmianie zakresu
- Zatwierdza: Zarząd / CEO

## Powiązania (meta)
- standardy-i-compliance: ISO 22301:2019 klauzula 5.3, NIS2 Art. 21
- raci-i-role: CEO (Approver), CISO (Owner), BCM Manager (Reviewer), wszyscy pracownicy (Informed)
