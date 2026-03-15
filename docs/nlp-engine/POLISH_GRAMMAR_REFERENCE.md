# Polish Grammar Reference — NLP Engine Implementation Guide

**Status:** Dokumentacja referencyjna dla implementatorów silnika NLP  
**Źródło:** Adaptacja `gramatyka_polska_reference.md` + `Główne części zdania.md`  
**Zastosowanie:** Konfiguracja modułów `MorphologicalAnalyzer`, `DependencyParser`, `SemanticRoleLabeler`, `ContextClassifier`

---

## 1. Dlaczego fleksja ma znaczenie dla NLP w języku polskim

Polski jest **językiem fleksyjnym** — funkcję gramatyczną słowa determinuje jego końcówka, nie pozycja w zdaniu. To oznacza:

- Zależności semantyczne (`kto robi co`) czytamy z **przypadków**, nie z szyku wyrazów
- Parser zależnościowy musi analizować **morfologię** przed budowaniem drzewa
- Dopasowywanie wzorców compliance (`kto odpowiada za X`) wymaga normalizacji do formy podstawowej

### 6 wariantów szyku wyrazów — wszystkie poprawne gramatycznie

| Układ | Skrót | Przykład | Funkcja stylistyczna |
|---|---|---|---|
| Subject–Verb–Object | **SVO** | *Janek czyta książkę.* | Szyk neutralny — domyślny, fakty |
| Object–Verb–Subject | **OVS** | *Książkę czyta Janek.* | Nacisk na wykonawcę; odpowiedź na „kto?" |
| Verb–Subject–Object | **VSO** | *Czyta Janek książkę.* | Szyk narracyjny, dynamiczny |
| Verb–Object–Subject | **VOS** | *Czyta książkę Janek.* | Silny nacisk na podmiot (zaskoczenie) |
| Subject–Object–Verb | **SOV** | *Janek książkę czyta.* | Poetycki/archaiczny; compliance: podkreślenie obiektu |
| Object–Subject–Verb | **OSV** | *Książkę Janek czyta.* | Najrzadszy; silna ekspresja przedmiotu |

> **Złota zasada (remat):** Nowa lub kluczowa informacja w zdaniu **zawsze wędruje na koniec**.  
> **Implikacja dla parsera:** Ostatni element zdania to najczęściej semantyczny fokus. Przy ekstrakcji ról compliance sprawdzaj element końcowy jako kandydata na `patient` / wymaganie.

---

## 2. Kategorie gramatyczne — referencja dla MorphologicalAnalyzer

### I. Przypadek (Casus) — 7

| Symbol | Nazwa | Pytanie | Rola w compliance NLP |
|---|---|---|---|
| **Nom** | Mianownik | kto? co? | Agent, Podmiot zdania |
| **Gen** | Dopełniacz | kogo? czego? | Posiadanie, zakresy, negacja egzystencjalna |
| **Dat** | Celownik | komu? czemu? | Beneficjent, adresat wymagania |
| **Acc** | Biernik | kogo? co? | Pacjent, obiekt działania |
| **Instr** | Narzędnik | kim? czym? | Narzędzie, środek techniczny |
| **Loc** | Miejscownik | o kim? o czym? | Zakres, kontekst |
| **Voc** | Wołacz | — | Marginalny dla compliance |

### II–IV. Liczba, Rodzaj, Osoba

| Kategoria | Wartości | Relevancja |
|---|---|---|
| **Liczba** | sg, pl, singularia tantum, pluralia tantum | Zakresy: „wszystkie systemy" vs „system" |
| **Rodzaj** | m1 (osobowy), m2 (żywotny), m3 (nieżywotny), f, n, virile, non-virile | Rozpoznanie aktorów (osoby vs systemy) |
| **Osoba** | 1sg, 2sg, 3sg | Tryb rozkazujący: 2sg imperatyw = obligacja |

### V. Czas (Tempus) — 4

| Symbol | Znaczenie | Compliance mapping |
|---|---|---|
| **praes** | Czas teraźniejszy | Aktualny stan systemu |
| **praet** | Czas przeszły | POST_EXEC — działanie już wykonane |
| **fut.simp** | Czas przyszły prosty | PRE_EXEC — planowane wymaganie |
| **fut.comp** | Czas przyszły złożony | PRE_EXEC — zobowiązanie w planie |

### VI. Aspekt (Aspectus) — kluczowy dla StateMatrix

| Symbol | Znaczenie | Compliance mapping |
|---|---|---|
| **perf** | Aspekt dokonany | Działanie zakończone / jednorazowe → weryfikowalne |
| **imperf** | Aspekt niedokonany | Działanie ciągłe / powtarzalne → monitorowalne |
| **biaspectual** | Dwuaspektowość | Wymaga kontekstu do interpretacji |

> **Zasada:** Aspekt dokonany (`zostanie zaszyfrowane`) → wymaganie testowalne.  
> Aspekt niedokonany (`jest szyfrowane`) → wymaganie ciągłe, wymaga monitoringu.

### VII. Tryb (Modus) — bezpośrednie mapowanie na StateMatrix

| Symbol | Tryb | Przykład | StateMatrix mood |
|---|---|---|---|
| **ind** | Oznajmujący | *System szyfruje dane* | `DECLARATIVE` |
| **imp** | Rozkazujący | *Zaszyfruj dane* | `IMPERATIVE` |
| **cond** | Warunkowy/Przypuszczający | *Dane powinny być szyfrowane* | `CONDITIONAL` |
| **opt** | Życzący (marginalny) | *Oby dane były bezpieczne* | — |

### VIII. Strona (Vox) — ekstrakcja agenta

| Strona | Przykład | Implikacja dla SRL |
|---|---|---|
| **Czynna** | *Administrator szyfruje dane* | Agent jawny — czytamy z mianownika |
| **Bierna analityczna** | *Dane są szyfrowane przez administratora* | Agent w narzędniku (`przez + Instr`) |
| **Bierna zwrotna** | *Dane szyfrują się* | Agent ukryty — prawdopodobnie system |
| **Medialna** | *System sam się autoryzuje* | Agent = Patient — reflexivum |

### IX–XII. Stopień, Żywotność, Formy nieosobowe

| Kategoria | Wartości kluczowe | Relevancja |
|---|---|---|
| **Stopień** | pos / comp / sup | Porównania w wymaganiach: „co najmniej 256-bit" |
| **Żywotność** | personale / animatum / inanimatum | Rozróżnienie: osoba vs system vs dane |
| **Formy nieosobowe** | inf, gerundium, part.praes.act, part.praet.pass, conv.sim, conv.ant | Bezokolicznik w obligacjach: „musi *szyfrować*" |

---

## 3. Relacje składniowe — konfiguracja DependencyParser (≈40)

Poniższe relacje odpowiadają kategoryzacji Universal Dependencies (UD) zaadaptowanej do polszczyzny.

### A. Relacje podmiotowo-orzeczeniowe (6)

| Relacja | UD tag | Opis |
|---|---|---|
| Podmiot gramatyczny | `nsubj` | Podmiot w mianowniku |
| Podmiot logiczny (semantyczny) | `nsubj:pass` | Podmiot w zdaniu biernym |
| Podmiot zerowy / domyślny | `nsubj:null` | Forma bezosobowa — podmiot domyślny |
| Podmiot nieokreślony | `nsubj:indef` | „Należy", „wymaga się" |
| Orzeczenie werbalne | `root` | Główny predykat zdania |
| Orzeczenie imienne | `cop` | Łącznik z orzecznikiem |

### B. Orzeczenia złożone (4)

| Relacja | UD tag | Przykład compliance |
|---|---|---|
| Modalne (`móc`, `musieć` + inf) | `aux:modal` | **musi** weryfikować → IMP + perf |
| Fazowe (`zacząć`, `przestać` + inf) | `aux:phase` | **przestaje** logować → zmiana stanu |
| Kauzatywne (`kazać` + inf) | `aux:caus` | polityka **nakazuje** szyfrować |
| Peryfrastyczne (analityczne) | `aux:periphr` | jest **zobowiązany** do |

### C. Dopełnienia — obiekty (7)

| Relacja | UD tag | Rola SRL |
|---|---|---|
| Dopełnienie bliższe (Acc) | `obj` | Bezpośredni Patient |
| Dopełnienie dalsze (Dat) | `iobj` | Beneficjent/Adresat |
| Dopełnienie w dopełniaczu | `obj:gen` | Negacja: `nie ma *klucza*` |
| Dopełnienie w narzędniku | `obl:instr` | Narzędzie: `szyfrować *kluczem*` |
| Dopełnienie w miejscowniku | `obl:loc` | Zakres: `przechowywać *w bazie*` |
| Dopełnienie przyimkowe | `obl:prep` | `odpowiada *za dane*` |
| Dopełnienie bezokolicznikowe | `xcomp` | `musi *szyfrować*` |

### D. Przydawki (8) — kluczowe dla NER

| Relacja | UD tag | Zastosowanie |
|---|---|---|
| Przymiotna | `amod` | „dane *wrażliwe*", „system *krytyczny*" |
| Rzeczowna w dopełniaczu | `nmod:gen` | „*systemu* autoryzacji" |
| Przyimkowa | `nmod:prep` | „baza *w chmurze*" |
| Apozycyjna | `appos` | „administrator, *właściciel danych*" |
| Liczebnikowa | `nummod` | „*256*-bitowy klucz" |
| Zdaniowa | `acl:relcl` | zdanie względne |
| Imiesłowowa | `acl` | „dane *szyfrowane* przez..." |
| Zaimkowa (dzierżawcza) | `det:poss` | „*jego* konto" |

### E. Okoliczniki (12)

| Symbol | Typ | UD tag | Compliance relevance |
|---|---|---|---|
| **Loc** | Miejsca | `obl:lmod` | Gdzie przechowywane |
| **Temp** | Czasu | `obl:tmod` | Kiedy / jak długo (retencja logów) |
| **Mod** | Sposobu | `obl:mmod` | Jak szyfrowane |
| **Caus** | Przyczyny | `obl:cause` | Dlaczego wymagane |
| **Fin** | Celu | `advcl:purp` | W jakim celu przetwarzane |
| **Cond** | Warunku | `advcl:cond` | Jeżeli... wówczas... |
| **Conc** | Przyzwolenia | `advcl:conc` | Mimo że... |
| **Grad** | Stopnia i miary | `advmod:deg` | „Co najmniej", „maksymalnie" |
| **Instr** | Narzędzia | `obl:instr` | Przy użyciu czego |
| **Com** | Towarzyszenia | `obl:com` | Wraz z... |
| **Consec** | Skutku | `advcl:consec` | Tak że... (implikacje) |
| **Resp** | Względu/zakresu | `obl:resp` | W zakresie danych... |

### F–J. Pozostałe relacje (13)

| Relacja | UD tag | Zastosowanie |
|---|---|---|
| Orzecznik podmiotu | `xcomp:pred` | „dane są *chronione*" |
| Orzecznik dopełnienia | `xcomp:obj` | „uznaje klucz za *bezpieczny*" |
| Koordynacja | `conj` | „szyfrowanie *i* uwierzytelnianie" |
| Apozycja luźna (parentetyczna) | `parataxis` | wtrącenia w wymaganiach |
| Zdanie podmiotowe | `csubj` | „*Szyfrowanie danych* jest wymagane" |
| Zdanie dopełnieniowe | `ccomp` | „wymagane jest, *aby*..." |
| Zdanie okolicznikowe | `advcl` | „*Jeśli* dane są wrażliwe, *muszą*..." |
| Negacja | `advmod:neg` | **„NIE"** — kluczowy trigger CompliancePlugin |
| Partykuła | `discourse` | „tylko", „jedynie" — zawężenie zakresu |
| Anaforyczne (zaimek) | `ref` | „system... *on*..." → koreferncja |
| Elipsa | `orphan` | brakujący orzecznik w zdaniu eliptycznym |

---

## 4. Akty mowy — mapowanie na ContextClassifier

Klasyfikacja aktów mowy (Austin/Searle, zaadaptowana do polszczyzny technicznej):

### Klasa I — Asertywne → `DECLARATIVE` w StateMatrix

| Akt | Przykład IT compliance | Implikacja |
|---|---|---|
| Asercja / twierdzenie | „System szyfruje dane TLS 1.3" | Weryfikowalny stan faktyczny |
| Zaprzeczenie / negacja | „Dane **nie są** szyfrowane" | ❌ GAP — wymaga wytknięcia |
| Stwierdzenie faktu | „Klucze mają 256 bitów" | Parametr konfiguracyjny |
| Opis | „Mechanizm operuje w trybie CBC" | Kontekst techniczny |
| Informowanie | „Administrator zarządza kluczami" | Rola → RBAC |

### Klasa II — Pytania → `QUERY` (ignorowane w compliance scan)

### Klasa III — Dyrektywne → `IMPERATIVE` w StateMatrix

| Akt | Przykład | Obligacja |
|---|---|---|
| Rozkaz / nakaz | „Zaszyfruj dane przed wysłaniem" | Bezwzględna — `MUST` |
| Prośba | „Prosimy o szyfrowanie..." | Opcjonalna — `SHOULD` |
| Rada / zalecenie | „Zaleca się użycie AES-256" | Rekomendowana — `RECOMMENDED` |
| **Zakaz** | „**Zabrania się** przechowywania haseł jawnych" | **Prohibicja — `MUST NOT`** |
| Pozwolenie | „Dozwolone jest..." | Permisja — `MAY` |
| Ostrzeżenie | „Uwaga: klucz wygasa po 90 dniach" | Alert — `WARNING` |

### Klasa IV — Komisywne → `COMMITMENT`

Obietnice i zobowiązania dostawców: „Gwarantujemy 99.9% dostępności", „Zapewniamy szyfrowanie end-to-end".

### Klasa V — Deklaratywne → `DECLARATION`

Performatywy instytucjonalne: „Niniejszym certyfikujemy zgodność z ISO/IEC 27001", „Zatwierdza się politykę..."

---

## 5. Implikacje dla implementacji

### MorphologicalAnalyzer

```python
# Pola TokenNode wymagające tych kategorii:
@dataclass
class TokenNode:
    text: str
    lemma: str          # forma podstawowa (lemmatyzacja)
    pos: str            # część mowy
    case: str           # Nom/Gen/Dat/Acc/Instr/Loc/Voc
    number: str         # sg/pl
    gender: str         # m1/m2/m3/f/n
    tense: str          # praes/praet/fut.simp/fut.comp
    aspect: str         # perf/imperf/biaspectual
    mood: str           # ind/imp/cond
    voice: str          # activa/passiva
    negated: bool       # obecność "nie" w zakresie
    sem_role: str       # AGENT/PATIENT/INSTRUMENT/LOCATION/BENEFICIARY/THEME
```

### DependencyParser — priorytety parsowania

1. **Najpierw:** Identyfikuj predykat modalny (`aux:modal`) — on determinuje obligatoryjność
2. **Potem:** Znajdź `nsubj` → Agent
3. **Następnie:** Znajdź `obj` lub `xcomp` → Patient / zakres obligacji
4. **Na końcu:** Sprawdź `advmod:neg` w zakresie predykatu → `negated=True`

### SemanticRoleLabeler — reguła rematu

```python
# Ostatnia fraza nominalna w zdaniu to najczęściej semantyczny fokus
if token.position == "sentence_final" and token.case in ("Nom", "Acc"):
    token.sem_role = "THEME"  # nowa informacja / wymaganie
```

### ContextClassifier — mapowanie aktów mowy

```python
MOOD_TO_STATE = {
    "assertivum": "DECLARATIVE",
    "negatio": "NEGATED_DECLARATIVE",
    "imperativum": "IMPERATIVE",
    "prohibitivum": "IMPERATIVE",  # MUST NOT
    "consilium": "CONDITIONAL",    # zalecenie
    "promissivum": "COMMITMENT",
    "declarativum": "DECLARATION",
}
```

---

## 6. Słownik terminów (PL ↔ EN ↔ UD tag)

| Polski termin | English | UD tag | Morfeusz2 tag |
|---|---|---|---|
| Przypadek | Case | `Case=` | `cas:` |
| Mianownik | Nominative | `Case=Nom` | `nom` |
| Dopełniacz | Genitive | `Case=Gen` | `gen` |
| Biernik | Accusative | `Case=Acc` | `acc` |
| Narzędnik | Instrumental | `Case=Ins` | `inst` |
| Aspekt dokonany | Perfective | `Aspect=Perf` | `perf` |
| Aspekt niedokonany | Imperfective | `Aspect=Imp` | `imperf` |
| Tryb rozkazujący | Imperative mood | `Mood=Imp` | `impt` |
| Tryb warunkowy | Conditional | `Mood=Cnd` | `cond` |
| Strona bierna | Passive voice | `Voice=Pass` | `pass` |
| Bezokolicznik | Infinitive | `VerbForm=Inf` | `inf` |
| Imiesłów bierny | Past passive participle | `VerbForm=Part\|Voice=Pass` | `ppas` |

---

*Źródła: `gramatyka_polska_reference.md`, `Główne części zdania.md`, `Główne działy języka polskiego.md`  
Zaadaptowane dla projektu IT-Dokumentacja-Compliance NLP Engine.*
