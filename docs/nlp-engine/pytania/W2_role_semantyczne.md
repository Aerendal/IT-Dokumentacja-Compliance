---
layer: W2
title: "Warstwa 2 — Role Semantyczne (SRL)"
phase: 2
status: planned
docs_version: 1.0.0
tags: [SemanticMapper, AGENT, PATIENT, INSTRUMENT, LOCATION, nsubj, SRL, koNLL-U, dep_rel]
---

# Warstwa 2 — Role Semantyczne (SRL)

## Przegląd

Warstwa 2 implementuje Semantic Role Labeling (SRL) dla języka polskiego.
Na wejściu przyjmuje `DependencyTree` z W1, na wyjściu produkuje strukturę zdarzenia z rolami:
AGENT, PATIENT, INSTRUMENT, LOCATION, TIME, CAUSE, GOAL.

Kluczowe klasy: `SemanticMapper`, `SlowosiecAdapter` (WSD dla ról).

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W2 istnieje bo drzewo zależności składniowych z W1 mówi o strukturze zdania, nie o znaczeniu. `nsubj` to "podmiot gramatyczny" — ale w stronie biernej podmiot gramatyczny jest PATIENT, nie AGENT ("Dokumentacja techniczna została odrzucona" → `nsubj(Dokumentacja)` = PATIENT, nie AGENT — Zamawiający jest pominięty lub w `obl` z "przez"). W2 tłumaczy strukturę składniową na semantykę zdarzenia: kto (AGENT) zrobił co (ACTION) komu (PATIENT) czym (INSTRUMENT) gdzie (LOCATION) kiedy (TIME). Ta struktura jest tym czego potrzebuje W5 (Drools) do wnioskowania i W4 (Neo4j) do budowania grafu semantycznego.

**Co się sypie bez tej warstwy:**
- W5 musi samodzielnie dekodować fleksję polską żeby pisać reguły DRL — logika biznesowa miesza się z lingwistyką; zmiana modelu UDPipe łamie wszystkie reguły
- W4 zapisuje strukturę składniową zamiast semantycznej — Cypher nie może pytać "kto był AGENT zabiecia" tylko musi dekodować `nsubj` + strona + rodzaj
- Polisemia ról jest nierozstrzygalna bez W3 (WSD): `obl` bez Case może być INSTRUMENT lub LOCATION

**Zależności:**
- Wchodzi z W1: `DependencyNode[dep_rel, feats, lemma, upos]`
- Wchodzi z W3 (opcjonalnie/równolegle, ADR-01): `EnrichedToken[synsets]` do WSD
- Wchodzi z W6 (opcjonalnie/równolegle, ADR-02): `CoreferenceChain` do rozwiązania zaimków przed mapowaniem ról
- Wychodzi do W4: `EventRoleDict[AGENT, PATIENT, INSTRUMENT, LOCATION, TIME, action]`
- Wychodzi do W5: ta sama struktura jako wejście dla reguł DRL

## Diagram przepływu danych

```
DependencyTree (CoNLL-U z W1)
       │
  SemanticMapper
  ┌────────────────────────────────┐
  │ nsubj → AGENT                  │
  │ obj   → PATIENT                │
  │ obl (narzędnik) → INSTRUMENT   │
  │ obl (przyimki: w/na/przy) → LOCATION│
  │ obl (przed/po/podczas) → TIME  │
  └────────────────────────────────┘
       │
  SlowosiecAdapter   ← WSD dla polisemicznych słów
       │
       ▼
  EventRoleDict: {AGENT: "Wykonawca", PATIENT: "dokumentacja_techniczna", ...}
       │
       ▼
  W4 (Neo4j) / W5 (InferenceEngine)
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Jak zaprojektować model danych grafu dla relacji agent-akcja-obiekt?
- Jak zmapować relację AGENT na strukturę grafową?
- Pokaż strukturę ontologii dla ról AGENT, PATIENT i INSTRUMENT.
- Jaki wzorzec projektowy stosuje SemanticMapper — Strategy (różne strategie mapowania per typ predykatu)?
- Jak wyglądają granice W2 — co dostarcza W1 (CoNLL-U z feats) a co W2 produkuje dla W4 (EventFrame)?
- Jak W2 obsługuje predykaty złożone (czasowniki fazowe: zacząć dostarczać, przestać zobowiązywać)?
- Jakie są wzorce fallback gdy rola semantyczna nie może być jednoznacznie przypisana?

### 2. Kontrakty danych
_brak pytań źródłowych w tej kategorii_
- Jaki jest format wyjściowy SemanticMapper — lista obiektów EventFrame w JSON?
- Jakie pola są wymagane w strukturze EventFrame przekazywanej do W4 (baza grafowa)?
- Jak zdefiniować kontrakt dla roli OPTIONAL vs. REQUIRED w strukturze predykatu — null, absent, czy empty list?
- Czy EventFrame posiada wersjonowanie schematu — jak obsłużyć nowe role bez łamania starych rekordów w grafie?
- Jak wygląda przykładowy obiekt EventFrame dla zdania "Wykonawca dostarczył dokumentację z opóźnieniem" — pokaż JSON?
- Jak stworzyć model danych dla relacji semantycznej w kontekście prawnym — EventFrame z polami AGENT="Wykonawca", ACTION="przekazać", PATIENT="dokumentacja"?
- Jak reprezentować relację INSTRUMENT w modelu danych EventFrame — opcjonalne pole vs. osobna krawędź :HAS_ROLE(INSTRUMENT)?
- Jak walidować kompletność modelu danych EventFrame — które role są obligatoryjne (AGENT, ACTION) a które opcjonalne (INSTRUMENT, LOCATION)?

### 3. Implementacja
- Jak stworzyć formalną ontologię dla relacji agent-akcja-obiekt?
- Pokaż implementację mapowania ról semantycznych na graf..
- Jak mapować etykiety Universal Dependencies na role semantyczne?
- Jak zaimplementować mapowanie etykiet nsubj i obj na role Agent i Patient?
- Jak powiązać tagi UDPipe z rolami Agent i Patient?
- Pokaż jak zamienić nsubj i obj na role Agent i Patient..
- Pokaż przykładowy kod ekstraktora ról semantycznych..
- Pokaż algorytm mapowania tagów UDPipe na role semantyczne..
- Jak algorytmicznie mapować tagi UDPipe na role Agent i Patient?
- Jak algorytmicznie mapować tagi nsubj i obj na role Agent i Patient?
- Jakie narzędzia polecasz do wizualizacji ról semantycznych w grafie?
- Jak UDPipe pomaga w mapowaniu ról agent-akcja-obiekt?
- Jak algorytmicznie rozwiązać konflikt między relacjami LOCATION a TIME?
- Jakie są najczęstsze błędy parsera UDPipe przy relacji INSTRUMENT?
- Stwórzmy klasę SemanticMapper dla mapowania ról AGENT i PATIENT..
- Jak rozszerzyć ontologię o relacje czasowe i przestrzenne?
- Jak dodać relacje INSTRUMENT i LOCATION do SemanticMapper?
- Jakie reguły zastosować dla relacji czasowych przed i po?
- Jak stworzyć słownik mapujący nsubj na AGENT?
- Pokaż przykład logiki mapowania przyimka na relację LOCATION..
- Czy do mapowania ról semantycznych wystarczą tylko etykiety dep?
- Pokaż kod implementacji SemanticMapper dla agenta i pacjenta..
- Jak dodać do mappera regułę dla instrumentu (np. młotkiem)?
- Jak zmapować przyimki na relacje czasowe w SemanticMapper?
- Dodajmy reguły dla relacji INSTRUMENT i LOCATION..
- Zaimplementujmy model danych grafu dla relacji AGENT-ACTION-PATIENT..
- Jak rozbudować mapowanie o relacje czasowe before i after?
- Pokaż jak zaimplementować wykrywanie relacji LOCATION na podstawie przyimków.
- Rozbudujmy metodę map_roles o analizę przyimków case dla okoliczników.
- Pokaż przykład implementacji relacji INSTRUMENT i LOCATION w kodzie.
- Pokaż jak zmapować nsubj:pass na rolę PATIENT.
- Stwórzmy listę 20 przyimków dla SemanticMapper.
- Pokaż pythonową logikę dla LOCATION i PART_OF.
- Czy Walenty obsługuje role semantyczne dla gatunków chronionych?
- Pokaż jak zamodelować relacje TIME i LOCATION w ontologii..
- Pokaż jak dodać relacje czasowe i przestrzenne do grafu..
- Jak rozbudować relacje czasowe i przestrzenne w grafie?
- Pokaż implementację relacji czasowych przed i po zdarzeniu..
- Jak zmapować przyimki 'z', 'do' na relacje source i destination?
- Jak rozbudować ontologię o relacje czasowe i przestrzenne?
- Zaktualizujmy logikę analizy intencji aktów mowy w SemanticMapper — jak rozróżnić ZOBOWIĄZANIE od WYKONANIA jako wymiar EventFrame?
- Jak dodać pole speech_act do EventFrame — enum: ZOBOWIĄZANIE, POTWIERDZENIE, ZAPRZECZENIE, OSTRZEŻENIE, POLECENIE?
- Jak wymiar intencji łączy się z rolami semantycznymi — AGENT+ZOBOWIĄZANIE = osoba zobowiązana, AGENT+POLECENIE = zleceniodawca w kontrakcie?
- Jak wymiar narzędzia (INSTRUMENT) z SemanticMapper mapuje się do Neo4j — tag `inst` (narzędnik) z Morfeusza → INSTRUMENT → :HAS_ROLE {role:'INSTRUMENT'} w W4?
- Jak mapować rolę ENVIRONMENT z tagu locative — `dep_rel='obl'` + `feats.Case='Loc'` + przyimek 'w/na/przy' → rola LOCATION (środowisko zdarzenia) w `map_roles()`; przykład: 'Wykonawca pracował w środowisku produkcyjnym' → `LOCATION='środowisko_produkcyjne'` zamiast obl bez roli?
- Jakie reguły gramatyczne odróżniają FACT od REQUIREMENT w polskim — FACT: czasownik w czasie przeszłym/teraźniejszym trybu oznajmującego ('dostarczył', 'jest') → `speech_act=POTWIERDZENIE`; REQUIREMENT: czasownik modalny ('musi', 'powinien', 'należy') lub tryb rozkazujący → `speech_act=ZOBOWIĄZANIE`; wykrywane przez SemanticMapper na podstawie `feats.Mood` i listy leksemów modalnych?
- Jak rozszerzyć EventFrame o wielowymiarowy kontekst sytuacyjny — pole `context: SituationalContext` z sub-polami temporal (BEFORE/AFTER/DURING), spatial (LOCATION/SOURCE/DESTINATION), causal (CAUSE/EFFECT)?
- Jak wielowymiarowy kontekst sytuacyjny EventFrame wpływa na reguły DRL — reguła aktywuje się tylko gdy `context.temporal='BEFORE'` i `speech_act='ZOBOWIĄZANIE'` jednocześnie?
- Jak SemanticMapper wydobywa wymiar temporal z zależności składniowych — przyimek 'przed' → temporal=BEFORE, 'po' → AFTER, 'podczas' → DURING mapowane z dep_rel nmod/obl?
- Jak zmapować parę podmiot-orzeczenie na obiekt EventFrame — `create_event_frame(nsubj: Token, verb: Token) → EventFrame(predicate=verb.lemma, agent=nsubj.form, doc_id=doc_id, speech_act=DEFAULT)`?
- Jak SemanticMapper tworzy EventFrame z drzewa zależności — wyodrębnia `root` jako predicate, `nsubj` jako AGENT, `obj` jako PATIENT, `obl` + feats.Case jako MANNER/INSTRUMENT/LOCATION?
- Jak wpiąć DependencyParserAdapter do metody generującej EventFrame — `SemanticMapper.__init__(self, parser: DependencyParser)` dependency injection, `parser.parse(sentence)` zwraca `List[DependencyNode]` przetwarzane przez `map_roles()`?
- Jak wpiąć NERAdapter do generowania EventFrame — przed `map_roles()` wywołaj `ner_adapter.recognize(sentence)`, scalaj wyniki z DependencyNode przez `token.ner_label = ner_result[token.start]`?
- Zaktualizujmy klasę EventFrame o automatyczne mapowanie ról z parsera — metoda fabryczna `EventFrame.from_dep_tree(nodes: List[DependencyNode]) → EventFrame` wypełnia AGENT (nsubj), PATIENT (obj), INSTRUMENT (obl + feats.Case=Ins) bez potrzeby zewnętrznego SemanticMapper?
- Jak `EventFrame.from_dep_tree()` obsługuje zdania bez nsubj — AGENT=None, `confidence=0.5`, flaga `roles_incomplete=True` zamiast ValueError; `KGT.capture_orphan(event)` gdy flaga ustawiona zanim trafi do InferenceEngine?
- Jak wdrożyć `EventFrame.from_roles(roles: Dict[str, str], predicate: str, doc_id: str) → EventFrame` do grafu zdarzeń — przyjmuje gotowy słownik `{AGENT: 'Wykonawca', PATIENT: 'dokumentacja'}` z `DependencyParserAdapter.map_roles()` i buduje EventFrame bez ponownego parsowania?
- Jak zmapować role AGENT/PATIENT na wymiary analizy kontekstowej — AGENT + `speech_act='ZOBOWIĄZANIE'` → wymiar `context.causal.responsible_party`, PATIENT + `context.temporal='BEFORE'` → `context.causal.affected_object` w SituationalContext?

### 4. Testowanie
- Zdefiniujmy test integracyjny dla relacji agent-patient w tym modelu..
- Jak rozbudować test o relacje instrument i location?
- Pokaż jak Hypothesis testuje relacje agent-akcja-obiekt..
- Jak zaprojektować system testów dla relacji agent-akcja-obiekt — parametryczny pytest z listą zdań wzorcowych `[(zdanie, expected_agent, expected_action, expected_patient)]` pokrywający co najmniej 5 wariantów szyku?
- Napiszmy test sprawdzający role semantyczne dla różnych szyków zdania — `@pytest.mark.parametrize` z parami `(zdanie_SVO, zdanie_OVS, zdanie_VSO)` i asercją że `frame.agent == expected_agent` niezależnie od kolejności tokenów?
- Stwórz testy dla ról semantycznych w zdaniach OVS — `SemanticMapper.map("Dokumentację Wykonawca dostarczył")` → `frame.agent == 'Wykonawca'` i `frame.patient == 'dokumentacja'`; weryfikacja że spaCy-pl poprawnie identyfikuje nsubj w zdaniu z wyprzedzonym obiektem?
- Stwórz testy jednostkowe dla różnych szyków zdania SVO/OVS/VSO — `@pytest.mark.parametrize("sentence,exp_agent,exp_patient", [("Wykonawca złożył ofertę","Wykonawca","oferta"), ("Ofertę złożył Wykonawca","Wykonawca","oferta"), ("Złożył Wykonawca ofertę","Wykonawca","oferta")])` z asercją że AGENT stały dla wszystkich wariantów?
- Stwórzmy testy jednostkowe dla klasy SemanticMapper w cyklu TDD..
- Napiszmy czerwony test dla SemanticMapper mapujący AGENT i PATIENT.
- Napiszmy testy dla klasy SemanticMapper.
- Czy do testu dodać też walidację relacji czasowych i lokalizacji?
- Pokaż testy dla roli INSTRUMENT z użyciem obl i narzędnika..
- Wdróżmy ten kod i sprawdźmy testy AGENT/PATIENT.
- Stwórzmy teraz czerwony test dla SlowosiecAdaptera..
- Jak zaprojektować testy integracyjne łączące Słowosieć z SemanticMapperem?
- Pokaż test integracyjny dla SemanticMapper i PhraseologyDetector..
- Zaprojektujmy test integracyjny łączący SemanticMapper i SlowosiecAdapter..
- Pokaż kod testu dla SemanticMapper z regułami Walentego..

### 5. Obsługa błędów
- Jak obsłużyć relacje czasowe before i after w SemanticMapperze?
- Jak obsłużyć wieloznaczność ról semantycznych przy użyciu słownika Walenty?
- Co zwrócić gdy zdanie wejściowe nie zawiera żadnego predykatu rozpoznawalnego przez SemanticMapper?
- Jak logować błędy mapowania roli bez ujawniania treści umowy w logach?
- Jak obsłużyć zdanie o długości przekraczającej limit tokenów modelu NLP?
- Co się dzieje gdy CoNLL-U wejściowe jest niepoprawnie sformatowane — wyjątek czy partial parse?

### 6. Integracja z innymi warstwami
- Pokaż jak zintegrować SemanticMapper z głównym pipeline przetwarzania..
- Jak zintegrować synsety Słowosieci z rolami AGENT i PATIENT?
- Jak zintegrować słownik Walenty, aby poprawnie przypisywać role semantyczne?
- Jakie konkretne pola CoNLL-U z W1 są wymagane przez SemanticMapper — feats, deprel, head, upos?
- Jak W2 przekazuje EventFrame do W4 — bezpośrednie wywołanie, kolejka zdarzeń, czy shared memory?
- Jak W2 współpracuje z W3 (Słowosieć) przy rozróżnianiu INSTRUMENT od LOCATION dla tego samego lematu?
- Jak W6 (koreferencja) powiadamia W2 gdy antecedent roli AGENT zostaje zaktualizowany?

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Jakie jest ryzyko gdy SemanticMapper błędnie przypisze AGENT zamiast PATIENT w zdaniu biernym?
- Jak uniknąć synkretyzmu fleksyjnego (ta sama forma — różne przypadki) przy rozpoznawaniu roli INSTRUMENT?
- Co się dzieje gdy zdanie zawiera dwa AGENT-y (podmiot współrzędny, np. "Wykonawca i Podwykonawca") — jak prioritizować?
- Jak obsłużyć elipsę semantyczną gdy PATIENT jest domyślny i nie pojawia się explicite w zdaniu?
- Jakie są konsekwencje błędnego mapowania roli semantycznej dla silnika wnioskowania w W5?
- Czy istnieje ryzyko pętli referencyjnej gdy rola COREFERENCE_OF wskazuje na inny EventFrame tego samego dokumentu?
- Jak walidować że przypisane role są spójne ze strukturą predykatu opisaną w słowniku Walenty?

## Pytania uzupełniające
- **Pułapka 3:** Role semantyczne są przypisywane per-zdanie — `SemanticMapper` nie zna kontekstu poprzednich zdań; AGENT w zdaniu 2 może być tym samym bytem co PATIENT w zdaniu 1, ale `map_roles()` tego nie widzi.
- **Pułapka 4:** Polskie zdania z czasownikami modalnymi ("może", "powinien") — `nsubj` jest przy modalnym, nie przy głównym predykacie; naiwne mapowanie `nsubj→AGENT` da błędną rolę.
- **Pułapka 5:** Imiesłowy przymiotnikowe bierne ("złamany kij") mają `nsubj:pass` — mapowanie `nsubj→AGENT` bez sprawdzenia `Voice=Pass` przypisuje błędną rolę do pacjensa.
- **Pułapka 6:** Reguły mapowania zakodowane w słowniku `deprel→role` są kruche — dla 5% zdań w NKJP relacja `obl` może oznaczać 3 różne role (INSTRUMENT, LOCATION, TIME) bez dodatkowego WSD.

### 1. Architektura

- Jak `SemanticMapper` komunikuje się z `SlowosiecAdapter` — synchronicznie czy przez interfejs?
- Czy `SemanticMapper` powinien być klasą stateless (czysta funkcja) czy stateful (słownik ról)?
- Jak podzielić mapowanie składniowe (nsubj/obj) od mapowania semantycznego (WSD)?
- Jak `SemanticMapper` obsługuje zdania wieloklauzu (zdania podrzędne, orzeczenie imienne)?
- Jaka jest granica odpowiedzialności między W2 a W3 (Słowosieć) przy ujednoznacznianiu?

### 2. Kontrakty danych

- Jaki jest schemat JSON `EventRoleDict` wychodzącego z W2 do W4/W5?
- Jak walidować, że każdy `EventRoleDict` ma przynajmniej jedno AGENT i ACTION?
- Jak kodować brak roli (np. brak INSTRUMENT w zdaniu) — null, pominięcie pola, czy pusty string?
- Jak przechowywać pewność przypisania roli (confidence score 0–1)?
- Jak reprezentować role w zdaniach wieloaktorowych (wiele AGENT)?

### 3. Implementacja

- Jak zaimplementować słownik mapowania `nsubj → AGENT`, `obj → PATIENT` w Pythonie?
- Jak zaimplementować `map_roles(dep_tree) -> dict` obsługując stronę bierną (`nsubj:pass → PATIENT`)?
- Jak rozbudować `map_roles` o analizę przyimków case (w, na, przy → LOCATION; przed, po → TIME)?
- Jak zbudować listę 20 kluczowych przyimków lokalizacyjnych i czasowych w `SemanticMapper`?
- Jak zaimplementować detekcję INSTRUMENT przez case narzędnikowy (morph feature `Case=Ins`)?

### 4. Testowanie

- Jak napisać czerwony test TDD dla `SemanticMapper.map_roles("Wykonawca dostarczył dokumentację techniczną z opóźnieniem")` → `{AGENT: "Wykonawca", PATIENT: "dokumentacja_techniczna", MANNER: "opóźnienie"}`?
- Jak testować stronę bierną: `map_roles("Dokumentacja techniczna została odrzucona przez Zamawiającego")` → `{AGENT: "Zamawiający", PATIENT: "dokumentacja_techniczna"}`?
- Jak zbudować oracle dataset 100 zdań z ręcznie annotowanymi rolami semantycznymi?
- Jak mierzyć Precision/Recall/F1 dla SRL na oracle datasecie?
- Jak testować relacje czasowe `before`/`after` w zdaniach z "przed" i "po"?
#### Kompletna hierarchia TDD
- Jak zaimplementować minimalną wersję `SemanticMapper` żeby przejść test RED — mapowanie tylko nsubj→AGENT i obj→PATIENT bez obsługi strony biernej?
- Zaimplementuj Fazę GREEN dla `SemanticMapper` — minimalny kod który mapuje `nsubj+Voice=Act → AGENT` i `obj → PATIENT`.
- Jak zrefaktoryzować `SemanticMapper` po GREEN — zastąpić if-elif kaskadę tablicą priorytetów ról (`RoleMapping` dataclass)?
- Zrefaktoryzuj `SemanticMapper` — każda reguła mapowania (nsubj→AGENT, obl+Case=Ins→INSTRUMENT) jako osobny `RuleHandler` z testem jednostkowym.
- Jak napisać test jednostkowy dla `_map_obl_to_role()` izolując od W1 — mock `DependencyNode` z różnymi `feats.Case`?
- Jak napisać test integracyjny W1→W2: podaj zdanie → sprawdź że `EventRoleDict.AGENT` ma właściwą wartość dla strony czynnej i biernej?
- Jak zmierzyć Mutation Score dla `SemanticMapper` — które reguły mapowania ról są najtrudniejsze do pokrycia mutantami?
- Jak zabezpieczyć się przed regresją precyzji ról gdy zmieniamy wersję modelu UDPipe — golden file z 100 zdaniami i oczekiwanymi rolami?
- Stwórz test regresyjny `SemanticMapper`: corpus 50 zdań kontraktowych z oczekiwanymi rolami jako golden file — CI fail przy F1 < 0.90.
- Jak przetestować W1→W2→W4 end-to-end: zdanie → `EventRoleDict` → graf Neo4j — sprawdzić krawędzie AGENT/PATIENT/INSTRUMENT?

### 5. Obsługa błędów

- Co zwraca `map_roles()` gdy `DependencyTree` nie ma żadnego `nsubj`?
- Jak obsługiwać synkretyzm: `obl` może być INSTRUMENT lub LOCATION w zależności od przypadka?
- Co robić, gdy `SlowosiecAdapter` zwraca brak synsetów dla słowa?
- Jak logować nierozwiązane przypisania ról (tokeny bez roli)?
- Jak obsługiwać zdania eliptyczne (brak podmiotu wyrażonego — domyślny podmiot)?
- Jak `map_roles()` zachowuje się dla zdań z dwoma predykatami (zdanie złożone współrzędnie) — jedna mapa czy dwie?
- Co zwrócić gdy W1 przekazał `DependencyTree` z `head=None` dla korzenia (uszkodzone CoNLL-U)?

### 6. Integracja z innymi warstwami

- Jak W2 przekazuje `EventRoleDict` do W4 (Neo4j) — bezpośrednia serializacja czy przez W5?
- Jak W3 (Słowosieć/Walenty) poprawia jakość mapowania ról w W2?
- Jak W5 (InferenceEngine) używa ról z W2 do budowania reguł wnioskowania?
- Jak W6 (koreferencja) wpływa na role — jeśli "on" → "Jan", czy W2 dostaje już rozwiązany zaimek?
- Jak W2 obsługuje EventFrame który musi być zaktualizowany po rozwiązaniu koreferencji przez W6?
- Jak weryfikować że EventFrame wychodzący z W2 spełnia kontrakt wejściowy W4 (baza grafowa)?
- Jak W2 przekazuje informację o pewności (confidence) mapowania roli do W5 (silnik wnioskowania)?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Polska fleksja powoduje, że ta sama forma może być narzędnikiem (INSTRUMENT) lub nomen (AGENT) — bez `Case=Ins` z Morfeusza błąd propaguje się do W4.
- **Pułapka 2:** Mapowanie wyłącznie przez `nsubj/obj` pomija ~15% zdań z niestandardową kolejnością — konieczna analiza `feats` z W1.
- **Pułapka 3:** Walenty ma niepełne pokrycie dla nowych czasowników (neologizmy, slang techniczny) — potrzebny fallback MFS (Most Frequent Sense).
- **Pułapka 4:** Polskie zdania z czasownikami modalnymi ("może", "powinien") — `nsubj` jest przy modalnym, nie przy predykacie głównym; naiwne `nsubj→AGENT` daje błędną rolę.
- **Pułapka 5:** Imiesłowy bierne (`nsubj:pass`) — mapowanie `nsubj→AGENT` bez sprawdzenia `Voice=Pass` przypisuje błędną rolę pacjensowi.
- **Pułapka 6:** Reguły `deprel→role` są kruche — dla ~5% zdań `obl` może oznaczać INSTRUMENT, LOCATION lub TIME bez dodatkowego WSD.

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Precision SRL na oracle datasecie | ≥ 90% |
| Recall SRL na oracle datasecie | ≥ 85% |
| F1 SRL | ≥ 87% |
| Pokrycie relacji czasowych (before/after) | ≥ 80% |
| Czas przetwarzania 1000 zdań | < 10 s |

## Pytania o idempotentność i deterministyczność

- Czy `map_roles(tree)` dla identycznego drzewa zawsze zwraca identyczny `EventRoleDict`?
- Czy `SlowosiecAdapter.get_synsets(word)` jest deterministyczny przy identycznym kontekście?
- Jak zapewnić stabliność wyników gdy Słowosieć jest aktualizowana (nowe synsety)?

## Pytania o migrację i wersjonowanie

- Jak migrować oracle dataset ról gdy dodajemy nową rolę (np. BENEFICIARY)?
- Jak wersjonować `SemanticMapper`, aby zmiany reguł mapowania nie łamały W4/W5?
- Jak zachować backwards-compatibility dla `EventRoleDict` gdy W5 już używa starszego schematu?

## Pytania o audytowalność

- Jak logować "dlaczego Jan=AGENT" — ścieżka decyzji: `nsubj → Case=Nom → brak nsubj:pass → AGENT`?
- Jak przechowywać confidence score przypisania roli dla raportu do klienta?
- Jak śledzić, który model UDPipe + która wersja Morfeusza wygenerowały dane role?

---

## Rozszerzalność i skalowanie

### Stopniowe dodawanie nowych ról semantycznych

- Jak dodać nową rolę (np. BENEFICIARY, MANNER, CAUSE) do `SemanticMapper` bez łamania istniejących testów?
- Jak zaimplementować `register_role(name, dep_labels, case_features)` — dynamiczne role?
- Jak testować regresję po dodaniu nowej roli — czy stare zdania nadal mają poprawne AGENT/PATIENT?
- Jakie są kryteria decydujące, że rola wymaga nowego pola w `EventRoleDict` vs nowej krawędzi w grafie?
- Jak stopniowo rozszerzać mapowanie: najpierw AGENT/PATIENT → potem INSTRUMENT/LOCATION → potem TIME/CAUSE?

### Skalowanie na złożone struktury zdań
- Jak `SemanticMapper` obsługuje zdania z wieloma AGENT (podmiot zbiorowy: "Wykonawca i Podwykonawca dostarczyli")?
- Jak mapować role dla nominalizacji ("naruszenie zobowiązania przez Wykonawcę" — kto jest AGENT)?
- Jak obsługiwać strony bierne wielokrotne ("Dokumentacja została odrzucona i zarchiwizowana")?
- Jak testować W2 na zdaniach prawnych (zdania wieloklauzowe, pasywne, z nominalnym orzecznikiem)?
- Jak stopniowo rozszerzać słownik przyimków z 20 do 100 (kolejne domeny: medyczna, wojskowa, prawna)?

### Inkrementalne reguły mapowania

- Jak hot-add nową regułę przyimkową do `SemanticMapper` bez restartu pipeline?
- Jak wersjonować zestaw reguł mapowania osobno od kodu (YAML/JSON reguły vs Python logika)?
- Jak mierzyć coverage reguł — ile % zdań jest pokrytych przez aktualne reguły przyimkowe?

---

## Luki zidentyfikowane przez audyt cross-warstwowy

### Kolejność W3 vs W2 w pipeline (niepodjęta decyzja architektoniczna)

- Czy W3 (WSD / Słowosieć) musi działać **przed** W2 (SemanticMapper) — czy `EnrichedToken` z synset_id jest prerequisite dla mapowania ról?
- Jeśli TAK: pipeline ma formę `W1 → W3 → W2`. Jak `SemanticMapper` przyjmuje `EnrichedToken` zamiast surowego `Token`?
- Jeśli NIE: `SemanticMapper` wywołuje W3 wewnętrznie. Jak zdefiniować tę granicę żeby nie było cyklicznej zależności W2↔W3?
- Jaka jest formalna decyzja architektoniczna i gdzie jest udokumentowana (ADR — Architecture Decision Record)?
- Jak przetestować oba scenariusze (W3-before vs W3-inside) żeby wybrać lepszy?

### Kolejność W6 vs W2 w pipeline (koreferencja przed rolami)

- Czy `CoreferenceResolver` (W6) musi działać **przed** `SemanticMapper` (W2) — decyzja: `W1 → W6 → W2` czy `W1 → W2 → W6 → aktualizacja ról`?
- Co się dzieje, gdy W2 dostaje zaimek "on" bez rozwiązania — czy mapuje AGENT="on" czy zwraca `AGENT=UNRESOLVED`?
- Jak `SemanticMapper` oznacza nieroz wiązane zaimki żeby W6 mogło je później scalić?
- Jak testować scenariusz, w którym koreferencja zmienia przypisanie roli (zaimek był PATIENT, po rozwiązaniu okazuje się tym samym bytem co AGENT)?
