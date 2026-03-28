# Przewodnik tworzenia szablonów dokumentacji IT

> **Język:** Polski  
> **Zasada:** Szablony zawierają *wskazówki i szkielet* — zero treści projektowych.  
> **Hard gate:** Zero emoji w plikach tekstowych.

---

## Spis treści

1. [Kiedy tworzyć nowy szablon?](#1-kiedy-tworzyć-nowy-szablon)
2. [Jak uruchomić wizard?](#2-jak-uruchomić-wizard)
3. [Struktura szablonu](#3-struktura-szablonu)
4. [Zasady guidance (wskazówek)](#4-zasady-guidance-wskazówek)
5. [Powiązanie z normami i standardami](#5-powiązanie-z-normami-i-standardami)
6. [Powiązania między dokumentami](#6-powiązania-między-dokumentami)
7. [Nazewnictwo i katalogi](#7-nazewnictwo-i-katalogi)
8. [Walidacja i pipeline](#8-walidacja-i-pipeline)
9. [Częste błędy](#9-częste-błędy)

---

## 1. Kiedy tworzyć nowy szablon?

Nowy szablon jest uzasadniony, gdy:

- Dokument reprezentuje *odrębny artefakt* procesu IT (np. "Raport z pentestów", "Macierz RACI projektu").
- Żaden z 7 944 istniejących szablonów nie obejmuje tego artefaktu.
- Dokument będzie produkowany *wielokrotnie* przez wiele projektów lub branż.

**Nie twórz nowego szablonu, gdy:**

- Istniejący szablon można rozszerzyć przez dodanie sekcji.
- Różnica dotyczy tylko branży — użyj mapowania ISIC w `doc_regulation_mapping`.

---

## 2. Jak uruchomić wizard?

```bash
cd dokumentacja
python3 scripts/new_template_wizard.py
```

Wizard poprowadzi przez:

1. Tytuł dokumentu (polski)
2. Krótki opis celu
3. Typ: `core`
4. Fazy cyklu życia (1–23)
5. Powiązane dokumenty
6. Standardy międzynarodowe
7. Polskie regulacje/normy

Po zakończeniu wizard:
- Generuje plik `.md` w `generated_templates/core/`
- Wstawia rekord do tabeli `docs` w bazie danych
- Dodaje podstawowe wpisy `doc_section_guidance`
- Opcjonalnie uruchamia pipeline walidacyjny

---

## 3. Struktura szablonu

Każdy szablon musi zawierać następujące sekcje (w tej kolejności):

```
---
title: Tytuł dokumentu
status: needs_content | aligned
aligned: false | true
---

# Tytuł dokumentu

## Metadane
## Cel dokumentu
## Zakres i granice
## Wejścia i wyjścia
## Powiązania (meta)
## Zależności dokumentu
## Fazy cyklu życia
### Faza N: Nazwa fazy
## Struktura sekcji (szkielet)
## Wymagane rozwinięcia
## Wymagane streszczenia
## Guidance (skrót)
## Szybkie powiązania
## Mające zastosowanie standardy i normy   ← opcjonalna, generowana automatycznie
## Jak używać dokumentu
## Checklisty Definition of Ready (DoR)
## Checklisty Definition of Done (DoD)
```

### Frontmatter YAML

| Pole | Wartości | Opis |
|------|----------|------|
| `title` | tekst | Tytuł dokumentu w języku polskim |
| `status` | `needs_content`, `aligned` | Czy sekcje mają guidance |
| `aligned` | `true`, `false` | Czy wersja jest zgodna z ostatnim pipeline |
| `aligned_rev` | liczba | Numer rewizji alignment |
| `aligned_at` | data ISO | Data ostatniego alignment |
| `aligned_by` | tekst | `codex`, `wizard`, `manual` |

---

## 4. Zasady guidance (wskazówek)

Każda sekcja szablonu powinna zawierać **wskazówkę** — krótki tekst wyjaśniający:
- Co wpisać w tej sekcji.
- Jakie decyzje wspiera.
- Jakie ryzyka minimalizuje.

**Dobra wskazówka:**
> Opisz cel i rolę dokumentu w procesie. Wyjaśnij, jakie decyzje wspiera i jakie ryzyka minimalizuje.

**Zła wskazówka (zbyt ogólna):**
> Opisz cel.

**Zasady:**
- Maksymalnie 3 zdania na sekcję w bloku `Guidance (skrót)`.
- Język: **polski** (nazwy własne standardów w oryginale angielskim).
- Zero emoji.
- Checklisty DoR/DoD — konkretne, weryfikowalne kryteria.

---

## 5. Powiązanie z normami i standardami

### Automatyczne mapowanie

Skrypt `scripts/map_standards_to_docs.py` automatycznie mapuje standardy na szablony na podstawie słów kluczowych w tytule i ścieżce. Uruchom po dodaniu wielu szablonów:

```bash
python3 scripts/map_standards_to_docs.py
```

### Ręczne przypisanie przez wizard

Wizard pyta o standardy i regulacje — wybierz te, które *bezpośrednio* obowiązują dany typ dokumentu:

| Sytuacja | Standardy |
|----------|-----------|
| Dokument testów | IEEE 829, ISO/IEC 12207 |
| Architektura systemu | IEEE 42010, TOGAF ADM, ISO/IEC 15288 |
| Bezpieczeństwo informacji | ISO/IEC 27001, ISO/IEC 27002, NIS2 |
| Zarządzanie usługami IT | ITIL 4, ISO 20000-1 |
| Ciągłość działania | ISO 22301, NIST CSF |
| Jakość oprogramowania | ISO/IEC 25010, ISO 9001 |
| Zarządzanie projektem | PMBOK 7, PRINCE2 7 |
| Dane osobowe | GDPR / RODO + UODO-PL |
| Sektor finansowy | DORA + KNF-REKOM-IT |
| Zamówienia publiczne | PZP-PL |
| Cyberbezpieczeństwo (PL) | KSC-PL, CERT-PL-WYTYCZNE |

### Sekcja w pliku .md

Po przypisaniu standardów sekcja `## Mające zastosowanie standardy i normy` jest wstawiana automatycznie. Możesz ją ręcznie rozszerzyć o komentarz kontekstowy.

---

## 6. Powiązania między dokumentami

### Szybkie powiązania (sekcja w .md)

Wymień nazwy (slugi) dokumentów, które:
- Dostarczają danych wejściowych do tego szablonu.
- Konsumują wyniki tego szablonu.
- Są naturalnie czytane razem z tym dokumentem.

```markdown
## Szybkie powiązania
- test_plan
- test_strategy_document
- wymagania_funkcjonalne
```

### Powiązania w bazie danych

Relacje sekcja↔sekcja są przechowywane w tabeli `content_links` (484 289 rekordów). Po wygenerowaniu nowego szablonu:

1. Dodaj relacje do `content_links` jeśli sekcje powiązane są krytyczne.
2. Uruchom `scripts/resolve_content_links_extended.py` aby zaktualizować `content_links_resolved`.

### Format referencji

```
document::Tytuł Dokumentu::section::Nazwa Sekcji
```

Przykład:
```
document::Test Plan::section::Zakres i granice
```

---

## 7. Nazewnictwo i katalogi

### Nazwy plików

- Slug tytułu: lowercase, ASCII, podkreślniki.
- Maksymalnie 80 znaków.
- Przykład: `plan_testow_regresji.md`

### Katalogi

| Katalog | Zastosowanie |
|---------|--------------|
| `generated_templates/core/` | Szablony dokumentów (> 7 000 plików) |

---

## 8. Walidacja i pipeline

Po dodaniu lub zmianie szablonów uruchom pipeline:

```bash
cd dokumentacja
python3 scripts/pipeline_run.py
```

Oczekiwany wynik: `{'status': 'PASS', ...}`

### Co sprawdza pipeline?

1. **Brak emoji** — hard gate, FAIL przy pierwszym znalezieniu.
2. **Pokrycie plików** — każdy plik `.md` musi mieć rekord w `documents_current`.
3. **Hash v2** — żaden plik nie może mieć NULL hash.
4. **Kolizje tytułów** — zduplikowane `title_norm` są raportowane.
5. **Duplikaty treści** — pliki o identycznej zawartości są raportowane.
6. **Snapshot** — po każdym PASS tworzony jest snapshot stanu.

### Typowe problemy

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `FAIL: emoji` | Plik zawiera emoji | Usuń emoji ze wszystkich plików .md |
| `FAIL: hash_v2 NULL` | Plik nie jest zaindeksowany | Uruchom `index_templates.py` |
| `database is locked` | Otwarta transakcja | Odczekaj i uruchom ponownie |

---

## 9. Częste błędy

### Błąd 1: Treść zamiast guidance

**Zle:**
```markdown
## Cel dokumentu
Ten dokument opisuje testy integracyjne systemu CRM XYZ wersja 3.2 wykonane w Q1 2025...
```

**Dobrze:**
```markdown
## Cel dokumentu
Opisz cel i zakres testów integracyjnych. Wyjaśnij, które interfejsy i przepływy danych są weryfikowane.
```

### Błąd 2: Emoji w treści

Zero emoji — to hard gate pipeline. Sprawdź:
```bash
grep -rn "[^\x00-\x7F]" generated_templates/ | grep -v "^Binary"
```

### Błąd 3: Brak sekcji Checklisty DoR/DoD

Każdy szablon musi mieć konkretne kryteria gotowości i zakończenia.

### Błąd 4: Pominięcie frontmatter

Frontmatter YAML jest wymagany przez pipeline do indeksowania. Szablon bez frontmatter spowoduje anomalię `MISSING_IN_OLD_DB`.

---

## Kontakt i historia zmian

- Projekt: IT_Dokumentacja
- Cel: 7 944 szablonów z guidance, bez treści projektowych
- Pipeline: `scripts/pipeline_run.py`
- Baza danych: `reports/it_doc_matrix.db`
- Status projektu: `AGENT.md`
