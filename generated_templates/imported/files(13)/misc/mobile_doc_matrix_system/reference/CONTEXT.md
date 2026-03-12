---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Mobile Development - Documentation Matrix
## ŚCIĄGA PROJEKTU - Pełny Kontekst

**Branża:** Mobile Development (iOS, Android, Cross-platform)
**Wersja:** 1.0
**Data:** 2026-01-31

---

##  STATYSTYKI

| Metryka | Wartość |
|---------|---------|
| Fazy projektu | 23 |
| Typy dokumentów | 129 |
| Relacje dokumentów | 64 |
| Mapowania do faz | 129 |
| Triggery cyklu życia | 62 |
| Kontrole OWASP MASVS | 30 |
| Metryki mobile | 25 |
| Urządzenia wspierane | 30 |

---

##  23 FAZ PROJEKTU MOBILE

| # | Kod | Nazwa | Grupa |
|---|-----|-------|-------|
| 1 | CONCEPT | Concept & Vision | PLANNING |
| 2 | REQUIREMENTS | Requirements Analysis | PLANNING |
| 3 | DESIGN | Design | PLANNING |
| 4 | PLANNING | Planning | PLANNING |
| 5 | IMPLEMENTATION | Implementation | DEVELOPMENT |
| 6 | TESTING | Testing / QA | QUALITY |
| 7 | SECURITY | Security / Compliance | QUALITY |
| 8 | DEPLOYMENT | Deployment | OPERATIONS |
| 9 | OPERATIONS | Operations / Maintenance | OPERATIONS |
| 10 | INCIDENT | Incident Management | OPERATIONS |
| 11 | MONITORING | Monitoring / Observability | OPERATIONS |
| 12 | REFERENCE | Reference Documentation | SUPPORT |
| 13 | TRAINING | Training / Onboarding | SUPPORT |
| 14 | STAKEHOLDER_COMM | Stakeholder Communication | SUPPORT |
| 15 | KNOWLEDGE | Knowledge Management | SUPPORT |
| 16 | RETROSPECTIVE | Retrospective / Postmortem | GOVERNANCE |
| 17 | BUDGETING | Budgeting / Cost Management | GOVERNANCE |
| 18 | VENDOR | Vendor / Procurement | GOVERNANCE |
| 19 | GOVERNANCE | Governance / Compliance | GOVERNANCE |
| 20 | DECOMMISSION | Decommissioning / EOL | GOVERNANCE |
| 21 | DISASTER_RECOVERY | Disaster Recovery / BCP | GOVERNANCE |
| 22 | CHANGE_MGMT | Change Management | GOVERNANCE |
| 23 | CAPACITY | Capacity Planning | GOVERNANCE |

---

##  KLUCZOWE DOKUMENTY MOBILE

### Architektura & Implementacja
- **MOB-ARC** - Mobile App Architecture (MVVM/MVI/Clean)
- **MOB-IOS** - iOS Implementation Guide (SwiftUI, Swift Concurrency)
- **MOB-AND** - Android Implementation Guide (Jetpack Compose, Kotlin)
- **MOB-FLT** - Flutter Implementation Guide (Dart, BLoC/Riverpod)
- **MOB-RNT** - React Native Implementation Guide (New Architecture)
- **MOB-SMD** - State Management Design

### Bezpieczeństwo
- **MOB-SEC** - Mobile Security Checklist (OWASP MASVS)
- **MOB-MSV** - MASVS Compliance Report
- **MOB-ENC** - Data Encryption Specification
- **MOB-PPM** - Privacy Policy for Mobile App

### Deployment & Store
- **MOB-ASG** - App Store Submission Guide (iOS)
- **MOB-GPG** - Google Play Submission Guide (Android)
- **MOB-ASC** - App Store Submission Checklist
- **MOB-GSC** - Google Play Submission Checklist

---

##  OWASP MASVS 2.0 CATEGORIES

| Kategoria | Opis | Kontrole |
|-----------|------|----------|
| MASVS-AUTH | Uwierzytelnianie i autoryzacja | 3 |
| MASVS-CODE | Jakość kodu i bezpieczeństwo | 4 |
| MASVS-CRYPTO | Kryptografia | 3 |
| MASVS-NETWORK | Bezpieczeństwo sieciowe | 3 |
| MASVS-PLATFORM | Interakcja z platformą | 4 |
| MASVS-PRIVACY | Prywatność użytkownika | 4 |
| MASVS-RESILIENCE | Odporność na reverse engineering | 4 |
| MASVS-STORAGE | Bezpieczne przechowywanie danych | 5 |

---

##  WZORCE ARCHITEKTONICZNE

### Model-View-ViewModel (MVVM)
- **Opis:** Separacja UI od logiki biznesowej z dwukierunkowym bindingiem
- **Use case:** Małe do średnich projektów, zalecane przez Google
- **Platformy:** iOS, Android

### Model-View-Intent (MVI)
- **Opis:** Jednokierunkowy przepływ danych, immutable state
- **Use case:** Kompleksowe UI, przewidywalne zarządzanie stanem
- **Platformy:** Android, iOS

### Clean Architecture (CLEAN)
- **Opis:** Warstwy: Presentation, Domain, Data z dependency rule
- **Use case:** Duże projekty, wysoka testowalność
- **Platformy:** iOS, Android, Flutter

### View-Interactor-Presenter-Entity-Router (VIPER)
- **Opis:** Separacja odpowiedzialności z routingiem
- **Use case:** Duże projekty iOS
- **Platformy:** iOS

### The Composable Architecture (TCA)
- **Opis:** Funkcyjne podejście do architektury SwiftUI
- **Use case:** SwiftUI apps, composable features
- **Platformy:** iOS

### Redux Pattern (REDUX)
- **Opis:** Unidirectional data flow, single store
- **Use case:** React Native, Flutter
- **Platformy:** Cross-platform

### Business Logic Component (BLOC)
- **Opis:** Pattern dla Flutter z separacją logiki
- **Use case:** Flutter applications
- **Platformy:** Flutter

### Riverpod State Management (RIVERPOD)
- **Opis:** Compile-safe dependency injection dla Flutter
- **Use case:** Flutter applications
- **Platformy:** Flutter

---

##  STANDARDY I FRAMEWORKI

| Standard | Wersja | Opis |
|----------|--------|------|
| APPLE_HIG | 2024 | Wytyczne Apple dla iOS/iPadOS... |
| APP_STORE_GUIDELINES | 2024 | Wytyczne Apple App Store... |
| FLUTTER | 3.24 | Dokumentacja Flutter... |
| GDPR | 2018 | Rozporządzenie o ochronie danych... |
| JETPACK_COMPOSE | 2024 | Wytyczne Jetpack Compose... |
| KOTLIN_GUIDE | 2.0 | Dokumentacja Kotlin dla Android... |
| MATERIAL_DESIGN_3 | 2024 | System designu Google dla Android... |
| OWASP_MASTG | 2024 | Przewodnik testowania bezpieczeństwa mobile... |
| OWASP_MASVS | 2.0 | Standard bezpieczeństwa aplikacji mobilnych... |
| OWASP_TOP10_MOBILE | 2024 | Top 10 zagrożeń mobilnych... |
| PLAY_STORE_POLICY | 2024 | Polityka Google Play Store... |
| REACT_NATIVE | 0.76 | Dokumentacja React Native... |
| SWIFTUI | 2024 | Dokumentacja SwiftUI... |
| SWIFT_6 | 6.0 | Dokumentacja Swift 6 z Strict Concurrency... |
| WCAG | 2.2 | Wytyczne dostępności... |

---

*Wygenerowano automatycznie przez Mobile Documentation Matrix System*