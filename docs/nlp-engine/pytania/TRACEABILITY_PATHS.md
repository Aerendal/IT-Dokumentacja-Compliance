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

## Ścieżka 1 — Analiza zdania prostego: "Jan zabił zwierzę nożem."

### Krok 0 — Dokument trafia do systemu (W0 / W8 inicjują)

> **CO:** `doc_auditor.py` (W0) klasyfikuje dokument jako `SRS` lub `AUDIT_REPORT`
> **DLACZEGO:** tryb `PRE_PRODUCTION` vs `POST_EXECUTION` decyduje co jest błędem a co normatywem — słowo "przetestowano" w SRS jest błędem, w raporcie wykonawczym jest wymagane
> **PRODUKUJE dla W8:** `{doc_class: SRS, validation_mode: PRE_PRODUCTION}`

*Bez W0:* W8 audytuje dokument nie wiedząc czy szuka planów czy dowodów — 40%+ fałszywych alarmów.

---

### Krok 1 — Tokenizacja i morfologia (W1)

> **CO:** Morfeusz2 tokenizuje i lematyzuje: `["Jan", "zabił", "zwierzę", "nożem"]`
> **DLACZEGO:** Polski język jest silnie fleksyjny — "zabił/zabije/zabijał" to ten sam lemat `zabić`; bez lematyzacji W3 (Słowosieć) nie znajdzie synsetu bo szuka lematu, nie formy
> **PRODUKUJE dla W2:** `DependencyNode` każdego tokenu z: `lemma`, `upos`, `feats`, `dep_rel`, `head`

```
Token:  Jan       | lemma: Jan   | upos: PROPN | feats: Case=Nom,Number=Sing,Gender=Masc
Token:  zabił     | lemma: zabić | upos: VERB  | feats: Tense=Past,Voice=Act,Number=Sing
Token:  zwierzę   | lemma: zwierzę | upos: NOUN | feats: Case=Acc,Number=Sing
Token:  nożem     | lemma: nóż   | upos: NOUN  | feats: Case=Ins,Number=Sing
```

> **CO:** UDPipe buduje drzewo zależności składniowych
> **DLACZEGO:** W2 (SemanticMapper) nie może przypisać roli AGENT/PATIENT bez wiedzy że `Jan` jest `nsubj` (podmiot) a `zwierzę` jest `obj` (dopełnienie); szyk zdania w polskim jest dowolny ("Zwierzę zabił Jan nożem" = to samo znaczenie) — tylko drzewo jest niezmiennicze
> **PRODUKUJE dla W2:** relacje `zabił.nsubj=Jan`, `zabił.obj=zwierzę`, `zabił.obl=nożem`

*Bez W1:* W2 dostaje surowy tekst — nie może mapować ról bez wiedzy o fleksji i strukturze zdania.
*Bez `feats.Case`:** W2 nie odróżni narzędnika (INSTRUMENT) od mianownika (AGENT) — "nożem" i "Jan" będą nierozróżnialne.

---

### Krok 2 — Role semantyczne (W2)

> **CO:** `SemanticMapper` mapuje relacje składniowe na role semantyczne
> **DLACZEGO:** "kto zrobił co z czym" jest potrzebne W5 (InferenceEngine) do wnioskowania; samo drzewo składniowe mówi o strukturze zdania, nie o znaczeniu; W4 (Neo4j) przechowuje zdarzenia jako węzły z rolami — bez ról graf byłby tylko strukturą składniową bez semantyki

```
nsubj(Jan)        + Voice=Act  → AGENT(Jan)       [kto wykonał akcję]
obj(zwierzę)                   → PATIENT(zwierzę)  [kto/co ucierpiało]
obl(nożem) + Case=Ins          → INSTRUMENT(nożem) [za pomocą czego]
```

> **DLACZEGO Case=Ins:** narzędnik (`nożem`, `nożem = Case=Ins`) w polskim jest gramatycznym markerem narzędzia/środka — bez `feats.Case=Ins` z W1 `obl` można by być LOCATION lub TIME

> **PRODUKUJE dla W4/W5:** `EventRoleDict = {action: zabić, AGENT: Jan, PATIENT: zwierzę, INSTRUMENT: nóż}`

*Bez W2:* W5 dostaje drzewo składniowe — musi sam dekodować fleksję polską; logika biznesowa miesza się z lingwistyką.
*Bez `feats` z W1:* "nożem" i "w lesie" wyglądają tak samo (`obl`) — INSTRUMENT i LOCATION nierozróżnialne.

---

### Krok 3 — Wzbogacenie semantyczne (W3)

> **CO:** `SlowosiecAdapter` dodaje hypernimy i synset dla każdego kluczowego tokenu
> **DLACZEGO:** W5 musi wnioskować generalnie, nie tylko o "nożu" — reguła "INSTRUMENT_NIEBEZPIECZNE → audit RISK-01" musi zadziałać dla "nóż", "pistolet", "miecz"; bez Słowosieci musiałby mieć ręcznie listę wszystkich narzędzi niebezpiecznych
> **PRODUKUJE dla W4/W5:** `nóż → synset("narzędzie_ostre") IS_A "narzędzie" IS_A "obiekt_fizyczny"`

```
nóż → hypernimy: [narzędzie_ostre, narzędzie, obiekt_fizyczny, byt]
zabić → synset: [zabójstwo, pozbawienie_życia] → IS_A [działanie, zdarzenie]
zwierzę → synset: [organizm_żywy, istota_żywa] → IS_A [byt_biologiczny]
```

> **DLACZEGO W3 musi być PRZED W2 lub WEWNĄTRZ W2 (ADR-01):** `SemanticMapper` potrzebuje synsetów żeby rozstrzygnąć polisemię ("zamek" = budowla lub mechanizm); bez WSD z W3 rola może być przypisana do złego znaczenia słowa

*Bez W3:* W5 ma tylko "nóż" — musi mieć regułę dla każdego narzędzia z osobna; system nie generalizuje.

---

### Krok 4 — Graf wiedzy (W4)

> **CO:** `GraphDatabaseAdapter` zapisuje zdarzenie jako węzły i krawędzie w Neo4j
> **DLACZEGO:** W5 (InferenceEngine) potrzebuje grafowej struktury do wnioskowania przez ścieżki (np. "Jan → AGENT → zabić → PATIENT → zwierzę → IS_A → istota_żywa"); relacyjna baza nie obsługuje zapytań ścieżkowych wydajnie; W8 (compliance) odpytuje graf żeby znaleźć wzorce RISK-01

```
(:Person {name: "Jan"})-[:AGENT]->(:Event {action: "zabić"})-[:PATIENT]->(:Animal {lemma: "zwierzę"})
(:Event)-[:INSTRUMENT]->(:Object {lemma: "nóż"})-[:IS_A]->(:Concept {name: "narzędzie_ostre"})
```

> **PRODUKUJE dla W5/W8:** grafowalny model zdarzenia, odpytywalny przez Cypher

*Bez W4:* W5 musi trzymać wszystkie fakty w pamięci; brak persystencji między zdaniami; W8 nie może sprawdzić historii zdarzeń w dokumencie.

---

### Krok 5 — Wnioskowanie (W5)

> **CO:** `InferenceEngine` (Drools) odpala reguły DRL na grafie zdarzeń
> **DLACZEGO:** Wzorce compliance (RISK-01, CONS-02) wymagają logiki warunkowej której nie da się wyrazić prostym SQL; reguły mogą kaskadować (zdarzenie A → wniosek B → trigger reguły C); Drools umożliwia deklaratywne wyrażenie "IF agent EXISTS AND instrument IS_A narzędzie_niebezpieczne THEN flag RISK"

```drools
rule "RISK-01: niebezpieczne narzędzie bez polityki bezpieczeństwa"
when
  $e: Event(action: "zabić" || "zniszczyć")
  $i: Concept(name: "narzędzie_ostre" || "broń") from $e.instrument.hypernyms
  not Policy(type: "bezpieczeństwo", scope covers $e.doc_class)
then
  insert(new AuditFinding(rule_id: "RISK-01", severity: HIGH, evidence: $e))
end
```

> **PRODUKUJE dla W7/W8:** `List<AuditFinding>` z `{rule_id, severity, evidence_snippet, sentence_id}`

*Bez W5:* W8 musi kodować każdą regułę jako if-else w Pythonie; nie ma kaskadowania; zmiana reguły = zmiana kodu.

---

### Krok 6 — Koreferencja (W6)

> **CO:** `CoreferenceResolver` rozwiązuje zaimki do antecedensów
> **DLACZEGO:** W zdaniu "Jan zabił zwierzę. On uciekł." — "on" musi być powiązane z "Jan"; bez W6 W2 przypisze "on" jako AGENT bez wiedzy że to Jan; W5 nie może wnioskować że Jan uciekł (kolejne zdanie)
> **KIEDY:** W6 powinno działać PRZED lub RÓWNOLEGLE z W2 (ADR-02 nierozstrzygnięte)

```
"On uciekł."
  → W6: "On" → antecedens: "Jan" (zgodność: Number=Sing, Gender=Masc, z poprzedniego zdania)
  → W2 (po W6): AGENT("Jan") zamiast AGENT("on_nierozwiązany")
```

> **PRODUKUJE:** zaktualizowane `EventRoleDict` z rozwiązanymi zaimkami; łańcuchy koreferencji dla W4

*Bez W6:* każde zdanie z zaimkiem ma AGENT/PATIENT "nieznany"; W5 nie może łączyć zdarzeń z różnych zdań w jedną historię.

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

> **Scenariusz:** W1 zwraca `DependencyNode` bez pola `feats` (UDPipe zawodzi dla 8% zdań)

```
W1: nożem → dep_rel=obl, feats={}    ← BRAK Case=Ins

W2: obl bez feats → INSTRUMENT? LOCATION? TIME?  ← NIEROZRÓŻNIALNE
    → przypisuje domyślnie LOCATION("nożem")     ← BŁĄD

W4: zapisuje (Event)-[:LOCATION]->(nóż)           ← BŁĄD w grafie

W5: reguła "INSTRUMENT IS_A narzędzie_niebezpieczne → RISK-01"
    → nie odpala (bo nóż jest LOCATION, nie INSTRUMENT)  ← RISK-01 POMINIĘTE

W8: raport nie zawiera RISK-01 dla tego zdania    ← FAŁSZYWE NEGATYWNE
```

**Konkluzja:** brak `feats.Case` w W1 → cichy błąd propagujący przez W2→W4→W5 → fałszywie negatywny raport compliance. To jest właśnie ryzyko dla projektu zarobkowego z odpowiedzialnością cywilną.

**Jak sprawdzić w kodzie:** test integracyjny: `assert all(node.feats.get("Case") for node in tree if node.upos == "NOUN")`

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
  → DLA W2 (przed/równolegle): żeby AGENT był "Jan", nie "on_nierozwiązany"
  → DLA W4: żeby węzły osób były scalane (nie duplikowane per zdanie)

W7 (FastAPI)
  → REST: POST /nlp/audit → AuditFinding[]
  → DLA klienta: żeby mógł integrować audyt bez Pythona

W8 (AuditEngine + GapAnalysisReport)
  → GapAnalysisReport[rule_id, evidence, doc_path, sentence_id]
  → DLA klienta: żeby miał audytowalny, powiązany ze źródłem raport compliance
```
