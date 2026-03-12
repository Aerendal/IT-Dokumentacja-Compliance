---
title: "Polityka Systemów Sztucznej Inteligencji (ISO/IEC 42001)"
status: aktywny
aligned: ISO/IEC 42001
---

## Cel dokumentu
Ustanowić politykę zarządzania systemami sztucznej inteligencji (AI Policy) jako centralny dokument Systemu Zarządzania AI (AIMS) wymagany przez ISO/IEC 42001:2023 klauzula 5.2. Polityka określa: zobowiązanie organizacji do odpowiedzialnego rozwoju i wdrażania systemów AI, zakres AIMS, zasady AI governance (przejrzystość, sprawiedliwość, wyjaśnialność, bezpieczeństwo, prywatność), role odpowiedzialności za AI i cele polityki AI zgodne ze strategią organizacji.

## Zakres i granice
Polityka obowiązuje wszystkie systemy AI opracowywane lub wdrożone przez organizację — obejmując modele ML, systemy rekomendacyjne, systemy decyzyjne i automatyzację napędzaną AI. Dotyczy pracowników, zewnętrznych dostawców AI i partnerów.

## Wejścia i wyjścia
**Wejścia:**
- Strategia organizacji i kontekst (ISO/IEC 42001 klauzula 4)
- Inwentarz systemów AI (klauzula A.3.2 — AI System Catalogue)
- Ocena ryzyka AI (klauzula 6.1)
- Wymagania prawne: EU AI Act, RODO Art. 22, KSC

**Wyjścia:**
- Zatwierdzona AI Policy zakomunikowana w organizacji
- Zakres AIMS (systemy AI objęte zarządzaniem)
- Cele AI governance do mierzenia i raportowania

## Zasady odpowiedzialnego AI

### 1. Przejrzystość i wyjaśnialność
- Użytkownicy są informowani gdy wchodzą w interakcję z systemem AI
- Decyzje AI o wysokim wpływie muszą być wyjaśnialne (XAI)
- Dokumentacja systemów AI jest dostępna dla audytorów

### 2. Sprawiedliwość i brak dyskryminacji
- Systemy AI są testowane pod kątem stronniczości (bias testing) przed wdrożeniem
- Metryki fairness są monitorowane w produkcji (np. demographic parity, equalized odds)
- Dane treningowe są weryfikowane pod kątem reprezentatywności

### 3. Prywatność i ochrona danych
- Systemy AI przetwarzające dane osobowe podlegają ocenie DPIA (RODO Art. 35)
- Zasada data minimization w zbiorach treningowych
- Mechanizmy usuwania danych osobowych z modeli (right to erasure)

### 4. Bezpieczeństwo i niezawodność
- Systemy AI o wysokim ryzyku przechodzą Security Assessment przed wdrożeniem
- Monitoring anomalii i concept drift w produkcji
- Plan awaryjny (fallback) gdy system AI zawodzi lub produkuje błędne wyniki

### 5. Nadzór ludzki (Human Oversight)
- Decyzje AI o wysokim wpływie na osoby fizyczne podlegają weryfikacji ludzkiej
- Mechanizmy override umożliwiające człowiekowi nadpisanie decyzji AI
- Audyt logów decyzji AI

### 6. Odpowiedzialność (Accountability)
- Każdy system AI ma przypisanego AI System Owner
- Incydenty AI są rejestrowane i analizowane (klauzula A.9)
- Raportowanie incydentów AI do organu nadzorczego (gdy wymagane przez EU AI Act)

## Klasyfikacja ryzyka systemów AI

Organizacja klasyfikuje systemy AI wg EU AI Act:

| Kategoria | Przykłady | Wymagania |
|-----------|-----------|-----------|
| **Niedopuszczalne ryzyko** | Scoring społeczny, manipulacja podprogowa | Bezwzględny zakaz |
| **Wysokie ryzyko** | Rekrutacja, decyzje kredytowe, systemy krytyczne | Pełna dokumentacja, audyt, rejestracja EU AI Act |
| **Ograniczone ryzyko** | Chatboty, deep fake | Obowiązek przejrzystości |
| **Minimalne ryzyko** | Filtry spamu, AI w grach | Dobrowolne kodeksy postępowania |

## Role i odpowiedzialności AI

| Rola | Odpowiedzialność |
|------|-----------------|
| **AI Governance Board** | Nadzór strategiczny nad AIMS, zatwierdzanie polityki |
| **Chief AI Officer / AI Lead** | Właściciel AIMS, wdrożenie polityki, raportowanie do zarządu |
| **AI System Owner** | Odpowiedzialność za konkretny system AI (od koncepcji do dekommisji) |
| **AI Risk Manager** | Ocena ryzyka AI, rejestr ryzyk AI |
| **Data Science Team** | Implementacja zasad AI governance w modelach |
| **Legal & Compliance** | Zgodność z EU AI Act, RODO Art. 22, krajowymi przepisami |

## Wymagania dla wdrożenia systemu AI
Przed wdrożeniem każdego systemu AI wymagane są:
1. Rejestracja w AI System Catalogue (klauzula A.3.2)
2. AI Risk Assessment (klauzula 6.1 + Annex A)
3. DPIA (gdy przetwarza dane osobowe)
4. Bias Testing Report
5. Zatwierdzenie AI System Owner i AI Governance Board
6. Dokumentacja techniczna (architecture, data sources, performance metrics)

## Powiązania (meta)
- standardy-i-compliance: ISO/IEC 42001:2023, EU AI Act, RODO Art. 22, IEEE 7000, NIST AI RMF
- raci-i-role: Zarząd (Approver), Chief AI Officer (Owner), AI System Owners (Responsible), Legal (Consulted), wszyscy pracownicy (Informed)
