---
title: "Ścieżki prześledzenia — end-to-end trace dla kluczowych scenariuszy"
docs_version: 1.0.0
tags: [traceability, end-to-end, causal-chain, dlaczego, flow]
---

# Ścieżki prześledzenia (Traceability Paths)

Każda ścieżka odpowiada na pytanie: **"dlaczego to jest potrzebne i co się sypie bez tego?"**

Format każdego kroku:
> `[Warstwa] CO robi` → `DLACZEGO` → `CO PRODUKUJE dla następnej warstwy`

---

## Ścieżka 1 — Analiza zdania z dokumentu kontraktowego: "Wykonawca dostarczył dokumentację techniczną z opóźnieniem."

> **Kontekst domenowy:** zdanie pochodzi z protokołu odbioru projektu IT. System ma ocenić czy naruszono klauzulę terminowości (CONS-02) i czy brakuje wymaganej polityki kar (RISK-01).

### Krok 0 — Dokument trafia do systemu (W0 / W8 inicjują)

> **CO:** `doc_auditor.py` (W0) klasyfikuje dokument jako `DELIVERY_PROTOCOL` (podtyp `AUDIT_REPORT`)
> **DLACZEGO:** tryb `POST_EXECUTION` decyduje że szukamy dowodów wykonania, nie planów — słowo "dostarczył" jest dowodem, nie hipotezą; gdyby to był `SRS` ten sam czasownik w czasie przeszłym byłby podejrzaną predetermination
> **PRODUKUJE dla W8:** `{doc_class: DELIVERY_PROTOCOL, validation_mode: POST_EXECUTION}`

*Bez W0:* W8 audytuje nie wiedząc czy to plan czy dowód — flaguje "dostarczył" jako błąd w SRS zamiast akceptować jako fakt w protokole.

---

### Krok 1 — Tokenizacja i morfologia (W1)

> **CO:** Morfeusz2 tokenizuje i lematyzuje
> **DLACZEGO:** "dostarczył/dostarczyła/dostarczymy/dostarczono" to formy tego samego lematu `dostarczyć`; bez lematyzacji W3 (Słowosieć) nie znajdzie synsetu bo szuka lematu, nie formy fleksyjnej; "opóźnieniu" ≠ "opóźnienie" dla słownika
> **PRODUKUJE dla W2:** `DependencyNode` per token z: `lemma`, `upos`, `feats`, `dep_rel`, `head`

```
Token: Wykonawca    | lemma: wykonawca    | upos: NOUN | feats: Case=Nom,Number=Sing,Gender=Masc
Token: dostarczył   | lemma: dostarczyć   | upos: VERB | feats: Tense=Past,Voice=Act,Number=Sing,Gender=Masc
Token: dokumentację | lemma: dokumentacja | upos: NOUN | feats: Case=Acc,Number=Sing,Gender=Fem
Token: techniczną   | lemma: techniczny   | upos: ADJ  | feats: Case=Acc,Number=Sing,Gender=Fem
Token: z            | lemma: z            | upos: ADP  | feats: —
Token: opóźnieniem  | lemma: opóźnienie   | upos: NOUN | feats: Case=Ins,Number=Sing
```

> **CO:** UDPipe buduje drzewo zależności składniowych
> **DLACZEGO:** szyk zdania w polskim jest dowolny ("Dokumentację techniczną Wykonawca dostarczył z opóźnieniem" = to samo znaczenie) — bez drzewa W2 nie wie który rzeczownik jest podmiotem, a który dopełnieniem
> **PRODUKUJE dla W2:** relacje `dostarczył.nsubj=Wykonawca`, `dostarczył.obj=dokumentację`, `dostarczył.obl=opóźnieniem`

*Bez W1:* W2 dostaje surowy tekst — nie może odróżnić AGENT od PATIENT w zdaniach z niestandardowym szykiem.
*Bez `feats.Case`:* "z opóźnieniem" (Case=Ins) i "do zamawiającego" (Case=Gen) wyglądają tak samo jako `obl` — INSTRUMENT/MANNER i DIRECTION nierozróżnialne.

---

### Krok 2 — Role semantyczne (W2)

> **CO:** `SemanticMapper` mapuje relacje składniowe na role semantyczne
> **DLACZEGO:** W5 (InferenceEngine) nie operuje na `nsubj` / `obj` — te kategorie są składniowe i zmieniają się przy zmianie strony; regułą DRL jest "IF AGENT == wykonawca AND action == dostarczyć AND MANNER == z_opóźnieniem THEN check CONS-02", nie "IF nsubj AND Tense=Past"

```
nsubj(Wykonawca)    + Voice=Act  → AGENT(Wykonawca)           [kto wykonał akcję]
obj(dokumentację)               → PATIENT(dokumentacja_techn) [co zostało dostarczone]
obl(opóźnieniem) + Case=Ins     → MANNER(opóźnienie)          [w jaki sposób]
```

> **DLACZEGO Case=Ins dla MANNER:** narzędnik w polskim wyraża zarówno narzędzie ("pismem" = INSTRUMENT) jak i okoliczność ("z opóźnieniem" = MANNER); `feats.Case=Ins` + prepozycja "z" daje sygnał MANNER; bez `feats` W2 nie może odróżnić "z opóźnieniem" (MANNER) od "pismem" (INSTRUMENT)

> **PRODUKUJE dla W4/W5:** `EventRoleDict = {action: dostarczyć, AGENT: Wykonawca, PATIENT: dokumentacja_techniczna, MANNER: opóźnienie}`

*Bez W2:* W5 musiałby parsować fleksję polską bezpośrednio w regułach DRL — każda zmiana modelu UDPipe łamie wszystkie reguły compliance.

**Uwaga — strona bierna:** "Dokumentacja techniczna została dostarczona z opóźnieniem" → `nsubj(Dokumentacja)` = PATIENT, nie AGENT (bo `Voice=Pass`); bez W2 rozumiejącego stronę, PATIENT staje się AGENT — błąd "kto odpowiada" = krytyczny dla audytu kontraktowego.

---

### Krok 3 — Wzbogacenie semantyczne (W3)

> **CO:** `SlowosiecAdapter` dodaje hypernimy i synset dla kluczowych tokenów
> **DLACZEGO:** W5 musi wnioskować generalnie — reguła CONS-02 ("naruszenie terminu → audit") musi zadziałać dla "opóźnienie", "zwłoka", "przekroczenie terminu", "uchybienie harmonogramowi"; bez W3 musiałby mieć ręczną listę synonimów; każdy nowy projekt prawniczy dodaje nowe synonimy

```
opóźnienie   → synset: [zwłoka, uchybienie_terminu] IS_A [naruszenie_zobowiązania, zdarzenie_prawne]
dostarczyć   → synset: [przekazać, wydać] → rama Walenty: [AGENT, PATIENT, RECIPIENT, MANNER]
dokumentacja → synset: [specyfikacja, dokumentacja_techniczna] IS_A [dokument, wytwór_intelektualny]
Wykonawca    → synset: [zleceniobiorca, wykonawca_umowy] IS_A [strona_umowy, podmiot_prawny]
```

> **DLACZEGO rama Walenty dla `dostarczyć`:** Walenty mówi że czasownik "dostarczyć" wymaga obligatoryjnie AGENT + PATIENT + RECIPIENT; jeśli RECIPIENT brakuje (komu dostarcza?) → W5 może flagować niekompletność zdarzenia jako lukę w dokumencie

*Bez W3:* W5 ma tylko "opóźnienie" — nie wie że "zwłoka" w §7 umowy i "opóźnienie" w protokole to semantycznie to samo naruszenie.

---

### Krok 4 — Graf wiedzy (W4)

> **CO:** `GraphDatabaseAdapter` zapisuje zdarzenie jako węzły i krawędzie w Neo4j
> **DLACZEGO:** W8 musi odpytać "czy w tym dokumencie są wszystkie zdarzenia wymagane przez umowę" — np. czy jest zdarzenie `dostarczenie` z RECIPIENT = Zamawiający; ta odpowiedź wymaga połączenia faktów z wielu zdań; relacyjna baza nie obsługuje tego zapytaniem ścieżkowym

```
(:Party {role: "Wykonawca"})-[:AGENT]->(:Event {action: "dostarczyć", doc_ref: "protokół §3"})
  -[:PATIENT]->(:Document {type: "dokumentacja_techniczna"})
  -[:MANNER]->(:Circumstance {type: "opóźnienie"})
  -[:IS_A]->(:LegalConcept {name: "naruszenie_zobowiązania"})
```

> **PRODUKUJE dla W5/W8:** grafowalny model zdarzenia kontraktowego, odpytywalny Cypher

*Bez W4:* każde zdanie jest izolowane; W5 nie może połączyć "Wykonawca dostarczył z opóźnieniem" (zdanie 3) z "Kara umowna wynosi 0,5% wartości" (zdanie 12) żeby wyliczyć naruszenie.

---

### Krok 5 — Wnioskowanie (W5)

> **CO:** `InferenceEngine` (Drools) odpala reguły DRL na grafie zdarzeń
> **DLACZEGO:** Compliance kontraktowy wymaga kaskadowania — "opóźnienie AND brak polityki kar → CONS-02 AND RISK-01 jednocześnie AND eskalacja severity=CRITICAL"; tego nie da się wyrazić SQL WHERE; Drools umożliwia deklaratywną logikę którą prawnik może czytać i weryfikować bez wiedzy o kodzie

```drools
rule "CONS-02: naruszenie terminu dostawy bez zdefiniowanej kary"
when
  $e: Event(action: "dostarczyć")
  $m: Circumstance(type: "naruszenie_zobowiązania") from $e.manner.hypernyms
  not ContractClause(type: "kara_umowna", covers: $e.patient.type)
then
  insert(new AuditFinding(rule_id: "CONS-02", severity: HIGH,
         evidence: $e.doc_ref, missing: "klauzula_kary_umownej"))
end
```

> **PRODUKUJE dla W7/W8:** `List<AuditFinding>` z `{rule_id: CONS-02, severity: HIGH, doc_ref: "protokół §3", missing: "klauzula_kary_umownej"}`

*Bez W5:* audytor musi ręcznie czytać każdy paragraf szukając naruszeń; niemożliwy audyt dokumentów 50+ stron.

---

### Krok 6 — Koreferencja (W6)

> **CO:** `CoreferenceResolver` rozwiązuje elipsę podmiotu i zaimki
> **DLACZEGO:** umowy i protokoły używają intensywnie zaimków i elipsy — "Wykonawca dostarczył dokumentację. Nie poinformował jednak o przeszkodach." — "Nie poinformował" ma eliptyczny podmiot (brakuje "Wykonawca" bo wynika z końcówki -ł masc.sg.); bez W6 W2 przypisze temu zdaniu AGENT = "brak" — wychodzi że nikt nie poinformował, czyli brak naruszenia
> **KIEDY:** W6 powinno działać PRZED lub RÓWNOLEGLE z W2 (ADR-02 nierozstrzygnięte)

```
"Nie poinformował jednak o przeszkodach."
  → W6: czasownik -ł, Gender=Masc, Sing → szuka antecedensa Masc.Sing z poprzednich zdań
  → antecedens: "Wykonawca" (z zdania 1, odległość: 1 zdanie, zgodność: Masc.Sing)
  → W2 (po W6): AGENT("Wykonawca") dla "poinformować"
```

> **PRODUKUJE:** zaktualizowane `EventRoleDict` z rozwiązaną elipsą; łańcuchy koreferencji dla W4

*Bez W6:* każde zdanie z elipsą podmiotu (typowe dla polskich dokumentów prawnych — 20-40% zdań) ma AGENT = nieznany → W5 nie wnioskuje o naruszeniu bo nie wie kto zaniechał.

---

### Krok 7 — API (W7)

> **CO:** FastAPI eksponuje `POST /nlp/audit` przyjmując dokument i zwracając `AuditFinding[]`
> **DLACZEGO:** Klient (system zewnętrzny, interfejs użytkownika) nie może bezpośrednio importować Pythona; API stanowi granicę systemową; umożliwia versjonowanie kontraktu niezależnie od wewnętrznej implementacji

> **PRODUKUJE dla klienta:** `{findings: [...], summary: {risk_count, cons_count, completeness_score}}`

*Bez W7:* użytkownik musi uruchamiać skrypty Python bezpośrednio; niemożliwa integracja z zewnętrznymi systemami klienta.

---

### Krok 8 — Audit compliance (W8)

> **CO:** `AuditEngine` + `NKJPBridge` + `GapAnalysisReport` generują końcowy raport
> **DLACZEGO:** Raport musi być audytowalny (kto co kiedy zaudytował), powiązany ze zdaniem źródłowym (evidence), i porównywalny w czasie (czy dokument się poprawił między rewizjami)
> **PRODUKUJE:** `GapAnalysisReport` z listą naruszeń + `TraceabilityMatrix` łącząca każde naruszenie z konkretnym zdaniem i regułą

*Bez W8:* mamy listę `AuditFinding` ale bez raportu, bez audit trail, bez mapy "jakie luki zostały wypełnione".

---

## Ścieżka 2 — Co się sypie gdy brakuje pola `feats.Case`

> **Scenariusz:** zdanie "Zamawiający odrzucił ofertę pismem z dnia 15 marca." — W1 zwraca `DependencyNode` bez pola `feats` dla tokenu "pismem" (UDPipe zawodzi dla ~8% zdań z formami niejednoznacznymi)

```
W1: pismem → dep_rel=obl, feats={}    ← BRAK Case=Ins

W2: obl bez feats → INSTRUMENT? LOCATION? TIME?  ← NIEROZRÓŻNIALNE
    → przypisuje domyślnie LOCATION("pismem")    ← BŁĄD

W4: zapisuje (Event)-[:LOCATION]->(pismo)         ← BŁĄD w grafie

W5: reguła "INSTRUMENT IS_A dokument_prawny → weryfikacja formalności CONS-02"
    → nie odpala (bo pismo jest LOCATION, nie INSTRUMENT)  ← CONS-02 POMINIĘTE

W8: raport nie zawiera CONS-02 dla tego zdarzenia  ← FAŁSZYWE NEGATYWNE
```

**Konkluzja:** brak `feats.Case` w W1 → cichy błąd propagujący przez W2→W4→W5 → fałszywie negatywny raport compliance. Zamawiający odrzucił ofertę "pismem" (= INSTRUMENT = formalna czynność prawna) — bez tej roli W5 nie może sprawdzić czy odrzucenie miało wymaganą formę pisemną (CONS-02: "odstąpienie wymaga formy pisemnej pod rygorem nieważności").

**Jak sprawdzić w kodzie:** test integracyjny: `assert all(node.feats.get("Case") for node in tree if node.upos == "NOUN" and node.dep_rel == "obl")`

---

## Ścieżka 3 — Co się sypie gdy W3 nie ma synsetu dla neologizmu

> **Scenariusz:** dokument używa słowa "konteneryzacja" (nieznane Słowosieci)

```
W1: konteneryzacja → lemma: konteneryzacja, upos: NOUN  ← OK

W3: get_synsets("konteneryzacja") → []   ← BRAK SYNSETU
    EnrichedToken.synsets = []           ← cichy brak

W2: mapuje rolę bez wsparcia WSD         ← ryzyko błędnego synsetu dla polisemicznych słów w kontekście

W4: węzeł (:Concept {lemma: "konteneryzacja"}) bez krawędzi IS_A  ← izolowany węzeł

W5: reguła "IF component IS_A technologia_IT THEN check SEC-01"
    → nie odpala (bo brak IS_A)          ← SEC-01 POMINIĘTE

W8: raport nie flaguje braku polityki bezpieczeństwa dla "konteneryzacja"
```

**Konkluzja:** W3 bez pokrycia neologizmów → W5 nie może generalizować reguł na nowe pojęcia → audyt niepełny.

**Mitygacja:** W3 musi logować każde `get_synsets()` → `[]` jako WARNING; W0 wykrywa wzrost liczby brakujących synsetów jako trend degradacji pokrycia.

---

## Mapa "co produkuje co dla kogo i dlaczego"

```
W0 (doc_auditor)
  → doc_class + validation_mode
  → DLA W8: żeby wiedzieć czy to plan czy dowód wykonania

W1 (Morfeusz + UDPipe)
  → DependencyNode[lemma, upos, feats, dep_rel, head]
  → DLA W2: żeby SemanticMapper miał podstawę do mapowania ról
  → DLA W3: żeby SlowosiecAdapter szukał lematów (nie form fleksyjnych)
  → DLA W4: żeby TokenNode w StateMatrix był wypełniony

W2 (SemanticMapper)
  → EventRoleDict[AGENT, PATIENT, INSTRUMENT, LOCATION, TIME]
  → DLA W4: żeby zdarzenie miało semantyczne krawędzie w grafie
  → DLA W5: żeby reguły DRL mogły opierać się na rolach nie fleksji

W3 (SlowosiecAdapter + WalentyCrawler)
  → EnrichedToken[synsets, hypernyms, valency_frame]
  → DLA W2: żeby WSD rozstrzygał polisemię przed mapowaniem ról
  → DLA W5: żeby reguły generalizowały ("nóż" → "narzędzie_ostre" → RISK-01)
  → DLA W4: żeby krawędzie IS_A w grafie miały wsparcie ontologiczne

W4 (Neo4jAdapter)
  → Graf: (:Entity)-[:ROLE]->(:Event), (:Concept)-[:IS_A]->(:Concept)
  → DLA W5: żeby InferenceEngine mógł odpytywać ścieżki grafowe
  → DLA W8: żeby AuditEngine miał persystentną historię zdarzeń

W5 (InferenceEngine / Drools)
  → AuditFinding[rule_id, severity, evidence_snippet]
  → DLA W7: żeby API mogło zwrócić wyniki klientowi
  → DLA W8: żeby GapAnalysisReport miał fakty do raportowania

W6 (CoreferenceResolver)
  → CoreferenceChain[pronoun → antecedent]
  → DLA W2 (przed/równolegle): żeby AGENT był "Wykonawca", nie "on_nierozwiązany"
  → DLA W4: żeby węzły osób były scalane (nie duplikowane per zdanie)

W7 (FastAPI)
  → REST: POST /nlp/audit → AuditFinding[]
  → DLA klienta: żeby mógł integrować audyt bez Pythona

W8 (AuditEngine + GapAnalysisReport)
  → GapAnalysisReport[rule_id, evidence, doc_path, sentence_id]
  → DLA klienta: żeby miał audytowalny, powiązany ze źródłem raport compliance
```
