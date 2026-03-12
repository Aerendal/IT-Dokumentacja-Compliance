---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Design System / Component Library
**Design System / Component Library** (DESIGN_SYSTEM)

##  Metadane dokumentu

| Pole | Wartość |
|------|---------|
| **Kod** | `DESIGN_SYSTEM` |
| **Kategoria** | UI Design |
| **Faza główna** | Projekt UI/UX |
| **Wersja** | 1.0.0 |
| **Status** | DRAFT |
| **Data utworzenia** | 2026-01-30 |
| **Autor** | [Imię Nazwisko] |
| **Recenzent** | [Imię Nazwisko] |
| **Zatwierdzający** | [Imię Nazwisko] |
| **Typowa długość** | 50-200 stron |

##  Opis

Dokumentacja design systemu: tokens, komponenty, patterns, guidelines.

##  Cykl życia dokumentu

| Trigger | Warunek | Opis |
|---------|---------|------|
| `CREATED_WHEN` | design_phase_started → Faza DESIGN | Tworzony iteracyjnie |
| `REVIEW_REQUIRED` | quarterly | Kwartalny przegląd spójności |
| `UPDATE_REQUIRED` | new_component_added | Aktualizowany przy nowym komponencie |

##  Obowiązywanie w fazach projektu

| Faza | Wymagalność | Akcja | Uwagi |
|------|-------------|-------|-------|
| 3. Projekt UI/UX | Obowiązkowy | CREATE | Design System tworzony iteracyjnie |
| 4. Planowanie | Obowiązkowy | REFERENCE | Design System referencja dla estymacji |
| 5. Implementacja | Obowiązkowy | REFERENCE | Design System referencja dla komponentów |
| 5. Implementacja | Zalecany | UPDATE | Design System aktualizowany przy nowych komponentach |
| 13. Szkolenie / Onboarding | Obowiązkowy | REFERENCE | Design System jako materiał |

##  Powiązania z innymi dokumentami

### Dokumenty wejściowe (od których zależy)

| Dokument | Relacja | Obowiązkowy | Opis |
|----------|---------|-------------|------|
| [TOKENS_REF] Design Tokens Reference | Odwołuje się do |  | Design Tokens jest referencją dla Design System |
| [DESIGN_REVIEW] Design Review Notes | Odwołuje się do |  | Design Review jest referencją dla Design System |
| [UI_PATTERNS] UI/UX Patterns Library | Rozszerza |  | UI Patterns rozszerza Design System |

### Dokumenty wyjściowe (które od tego zależą)

| Dokument | Relacja | Obowiązkowy | Opis |
|----------|---------|-------------|------|
| [COMP_SPEC] Component Specification | Odwołuje się do |  | Design System jest referencją dla Component Spec |
| [CSS_GUIDE] CSS/Styling Guidelines | Rozszerza |  | Design System rozszerza CSS Guidelines |
| [COMP_LIB_DOC] Component Library Documentation | Produkuje |  | Design System produkuje Component Library Documentation |

##  Struktura dokumentu

### 1. Wprowadzenie *(wymagana)*

Cel i zakres design systemu, principles, governance.

**Wskazówki:** Opisz dlaczego design system istnieje, dla kogo jest przeznaczony.

**Przykład:**
```
Ten design system zapewnia spójność wizualną i funkcjonalną dla wszystkich produktów firmy X.
```

### 2. Design Principles *(wymagana)*

Fundamentalne zasady projektowania.

**Wskazówki:** Zdefiniuj 5-7 kluczowych zasad, które kierują wszystkimi decyzjami designu.

**Przykład:**
```
1. Accessibility First\n2. Consistency Over Novelty\n3. Performance Matters\n4. Progressive Enhancement
```

### 3. Design Tokens *(wymagana)*

Zmienne projektowe: colors, spacing, typography, shadows.

**Wskazówki:** Dokumentuj wszystkie tokeny z nazwami semantycznymi i wartościami.

**Przykład:**
```
color-primary: #0066CC\nspacing-md: 16px\nfont-size-body: 16px
```

### 3.1. Colors *(wymagana)*

Paleta kolorów: primary, secondary, semantic, neutrals.

**Wskazówki:** Uwzględnij contrast ratios dla każdej kombinacji (WCAG AA minimum).

**Przykład:**
```
Primary: #0066CC (contrast 4.5:1 on white)
```

### 3.2. Typography *(wymagana)*

Font families, sizes, weights, line-heights.

**Wskazówki:** Zdefiniuj skalę typograficzną i odpowiadające tokeny.

**Przykład:**
```
font-family-base: Inter, system-ui, sans-serif
```

### 3.3. Spacing *(wymagana)*

System odstępów i siatki.

**Wskazówki:** Użyj skali matematycznej (np. 4px base × 1, 2, 3, 4, 6, 8, 12).

**Przykład:**
```
spacing-unit: 4px\nspacing-sm: 8px\nspacing-md: 16px
```

### 3.4. Shadows & Elevation *(opcjonalna)*

Cienie i poziomy elevation.

**Wskazówki:** Zdefiniuj 3-5 poziomów elevation.

**Przykład:**
```
elevation-1: 0 1px 3px rgba(0,0,0,0.12)
```

### 4. Components *(wymagana)*

Biblioteka komponentów UI.

**Wskazówki:** Dla każdego komponentu: anatomy, variants, states, props, a11y, examples.

### 4.1. Atoms *(wymagana)*

Podstawowe elementy: Button, Input, Icon, Badge.

**Wskazówki:** Atomic Design Level 1 - niepodzielne elementy.

**Przykład:**
```
Button: primary, secondary, ghost, danger variants
```

### 4.2. Molecules *(wymagana)*

Kombinacje atomów: Form Field, Search Box, Card.

**Wskazówki:** Atomic Design Level 2 - proste kombinacje.

**Przykład:**
```
Form Field = Label + Input + Helper Text + Error Message
```

### 4.3. Organisms *(wymagana)*

Złożone sekcje: Navigation, Hero, Footer.

**Wskazówki:** Atomic Design Level 3 - sekcje strony.

**Przykład:**
```
Navigation = Logo + Nav Links + Search + User Menu
```

### 4.4. Templates *(opcjonalna)*

Layouty stron: Dashboard, Form Page, List Page.

**Wskazówki:** Atomic Design Level 4 - szablony stron.

### 5. Patterns *(opcjonalna)*

Wzorce interakcji i UX.

**Wskazówki:** Dokumentuj powtarzalne wzorce: forms, navigation, feedback.

**Przykład:**
```
Form Pattern: validation, error handling, submission states
```

### 6. Accessibility *(wymagana)*

Wymagania i wytyczne dostępności.

**Wskazówki:** WCAG 2.2 AA compliance requirements dla każdego komponentu.

**Przykład:**
```
Wszystkie interaktywne elementy: focus visible, min 44x44px touch target
```

### 7. Usage Guidelines *(wymagana)*

Jak używać design systemu.

**Wskazówki:** Installation, imports, theming, customization.

**Przykład:**
```
npm install @company/design-system
```

### 8. Contributing *(opcjonalna)*

Jak rozwijać design system.

**Wskazówki:** Process for proposing new components, review workflow.

### 9. Changelog *(wymagana)*

Historia zmian wersji.

**Wskazówki:** Semantic versioning: MAJOR.MINOR.PATCH

**Przykład:**
```
v2.1.0 - Added DatePicker component
```

##  Historia zmian

| Wersja | Data | Autor | Opis zmian |
|--------|------|-------|------------|
| 1.0.0 | 2026-01-30 | [Autor] | Wersja inicjalna |

##  Zatwierdzenia

| Rola | Osoba | Data | Podpis |
|------|-------|------|--------|
| Autor | | | |
| Recenzent | | | |
| Zatwierdzający | | | |
