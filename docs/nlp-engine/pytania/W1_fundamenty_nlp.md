---
layer: W1
title: "Warstwa 1 — Fundamenty NLP (Morfologia i Składnia)"
phase: 1
status: planned
docs_version: 1.0.0
tags: [morfeusz, udpipe, nkjp, conll-u, tei, lematyzacja, tokenizacja, hypothesis, mutation-score]
---

# Warstwa 1 — Fundamenty NLP (Morfologia i Składnia)

## Przegląd

Warstwa 1 dostarcza podstawowych operacji lingwistycznych dla języka polskiego:
tokenizację, lematyzację (Morfeusz), tagowanie POS, parsowanie zależności składniowych (UDPipe)
oraz przetwarzanie zasobów NKJP (format TEI P5, CoNLL-U).
Jest fundamentem dla wszystkich warstw W2–W8.

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W1 istnieje bo język polski jest silnie fleksyjny — "dostarczył/dostarczy/dostarczał/dostarczyłem/dostarczyłaś" to formy tego samego lematu `dostarczyć`. Bez W1 żadna wyższa warstwa nie wie że te słowa znaczą "to samo". Morfeusz dostarcza lemat + morfologię (fleksja, przypadek, rodzaj), UDPipe buduje drzewo zależności składniowych (`nsubj`, `obj`, `obl`). Te dwie informacje razem są warunkiem koniecznym dla W2 żeby przypisać role semantyczne: bez `dep_rel` W2 nie wie że Wykonawca jest podmiotem, bez `feats.Case` W2 nie odróżnia INSTRUMENT (narzędnik) od LOCATION (miejscownik).

**Co się sypie bez tej warstwy:**
- W2 dostaje surowy tekst — próba mapowania ról bez fleksji to ~20-30% precision dla polskiego
- W3 szuka w Słowosieci form fleksyjnych zamiast lematów → 60-70% miss rate dla czasowników nieregularnych
- Cichy błąd: brak `feats.Case` → W2 przypisuje LOCATION zamiast INSTRUMENT → W5 nie odpala reguł RISK-01 → audyt compliance fałszywie negatywny

**Zależności:**
- Wchodzi: surowy tekst UTF-8
- Wychodzi do W2: `DependencyNode[lemma, upos, feats, dep_rel, head]` per token
- Wychodzi do W3: `lemma` jako klucz do słownika Słowosieci
- Wychodzi do W4: `TokenNode` jako baza węzłów w StateMatrix

## Diagram przepływu danych

```
Plik NKJP (XML/TEI P5)
       │
  lxml / BeautifulSoup  ← parsowanie XML, XPath
       │
       ▼
  Morfeusz2             ← tokenizacja, lematyzacja, tagowanie MSD
       │
       ▼
  CoNLL-U / UDPipe      ← parsowanie składniowe, drzewo zależności
       │
       ▼
  Pipeline NLP          ← obiekty Token, Sentence, DependencyTree
       │
  ┌────┴────┐
  ▼         ▼
 W2 (SRL)  W4 (Graf)    ← konsumenci W1
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Jak zaplanować Faze REFACTOR dla modułu nlp_processor?
- Jak stworzyć strukturę ontologii dla grafu znaczeń?
- Chcę przejść do projektowania struktury grafu wiedzy dla lintera.
- Które moduły warto zrealizować najpierw w planie 12-18 miesięcy?
- Pokaż jak rozwiązać konflikt między modułami Unit i Security..
- Pokaż strukturę grafu dla zdania 'Wykonawca dostarczył dokumentację techniczną z opóźnieniem'.
- Jak zaprojektować ontologię dla wielowymiarowej analizy zdarzenia „dostarczyć / odstąpić od umowy"?
- Pokaż jak sfinalizować architekturę i podsumować ten etap..
- Pokaż strukturę ontologii dla wielodomenowej klasyfikacji zdarzeń..
- Wybieram Głębokie Rozpoznawanie Nazw (DeepER/poldeepner) jako moduł NER w W1 — jakie encje są rozpoznawane: OSOBA, ORGANIZACJA, LOKALIZACJA, DATA, NUMER_UMOWY jako wejście do SemanticMapper?
- Jak NER jako krok W1.5 uzupełnia wyjście Morfeusza i UDPipe — rozpoznane encje nakładają się na tokeny CoNLL-U jako atrybut `ner_label` przekazywany do W2?

### 2. Kontrakty danych
- Stwórz przykładowy JSON kontraktu danych między modułem morfologii a składni..
- Pokaż przykład formatu JSON dla kontraktu danych modułu morfologii..
- Jak stworzyć funkcję mapującą format CoNLL-U na graf wiedzy?
- Pokaż jak zintegrować Morfeusza z UDPipe przez format TEI P5..
- Pokaż skrypt Python do generowania pliku JSONL z NKJP.
- Pokaż skrypt konwertujący XML z NKJP na format JSONL..
- Pokaż skrypt Python do konwersji XML z NKJP na format JSONL..
- Jak napisać skrypt konwertujący XML z NKJP do JSONL?
- Jakie metadane z NKJP warto uwzględnić w pliku JSONL?
- Pokaż skrypt Python konwertujący XML z NKJP do JSONL..
- Jakie są główne różnice między formatami TEI P5 i JSONL?
- Pokaż skrypt Python do konwersji XML z NKJP na JSONL..

### 3. Implementacja
- Przedstaw model danych grafu wiedzy dla przykładu z dokumentacją techniczną.
- Wyszukaj źródła i skrypty do automatyzacji ekstrakcji danych z NKJP..
- Skonfigurujmy UDPipe jako parser składni zależności w modules..
- Jak zaimplementować DependencyParser jako interfejs `parse(sentence: str) → List[DependencyNode]` — klasa abstrakcyjna `DependencyParser` z implementacjami `UDPipeParser` i `SpacyParser`?
- Jak DependencyParser buduje DependencyNode — każdy węzeł: `{id, form, lemma, upos, feats, head, dep_rel}` zgodnie ze schematem Universal Dependencies v2?
- Jak zapewnić zgodność wyników DependencyParser z schematem CoNLL-U — walidacja że każdy DependencyNode ma niepuste `dep_rel` i `head` zanim trafi do SemanticMapper W2?
- Jakie są zalety integracji spaCy-pl z klasą DependencyParserAdapter — spaCy-pl oferuje szybszy inference niż UDPipe dla krótkich zdań prawnych; adapter ukrywa różnicę API za wspólnym interfejsem?
- Jak zaimplementować `SpacyParser` jako backend DependencyParserAdapter — `nlp = spacy.load('pl_core_news_lg')`, token.dep_ → dep_rel, token.head.i → head, token.morph → feats?
- Jak porównać `UDPipeParser` i `SpacyParser` dla zdań prawnych — testy parametryczne z tymi samymi zdaniami, asercja że dep_rel AGENT/PATIENT zgadzają się w ≥ 90% przypadków?
- Czy spaCy-pl poradzi sobie ze swobodnym szykiem zdania w polskim — `pl_core_news_lg` trenowany na NKJP/PolEval; testuj inversję 'Dokumentację Wykonawca dostarczył' vs 'Wykonawca dostarczył dokumentację' i porównaj dep_rel?
- Jak UDPipe vs spaCy-pl radzi sobie ze swobodnym szykiem — oba opierają się na feats.Case zamiast pozycji tokenu, ale UDPipe (UD-Polish-PDB) może dawać lepsze wyniki dla inversji zdań prawnych?
- Jak spaCy-pl obsługuje zdanie z przeczeniem w niestandardowym szyku — 'Dokumentacji Wykonawca nie dostarczył': dep_rel 'nsubj' dla 'Wykonawca' nie zmienia się pomimo negacji i inwersji, ale token 'nie' powinien mieć dep_rel='advmod' jako modyfikator czasownika?
- Jak wykryć zdanie o niskiej pewności parsowania w spaCy-pl przy nietypowym szyku — token.dep_=='dep' (nieoznaczone relacje) jako sygnał że szyk jest zbyt nieregularny dla parsera; log jako UNKNOWN_STRUCTURE w KnowledgeGapTracker?
- Jak NER (DeepER/poldeepner) uzupełnia pipeline W1 — rozpoznane encje OSOBA/ORGANIZACJA są kandydatami do roli AGENT/PATIENT w SemanticMapper W2 przed analizą dep_rel?
- Jak zaimplementować `NERAdapter` jako wrapper dla DeepER — `recognize(sentence) → List[Entity]` gdzie Entity: `{form, label: OSOBA|ORGANIZACJA|LOKALIZACJA|DATA|UMOWA, start, end}`?
- Jak zintegrować DeepER do rozpoznawania nazw własnych — załaduj model `poldeepner.load('pl-nkjp')`, przekaż tokenizowane zdanie z Morfeusza, zmapuj span offsets na pozycje DependencyNode?
- Jak obsłużyć encje wielotokenowe w DeepER (np. 'Poczta Polska') — BIO tagi: B-ORG, I-ORG; scalaj tokeny z tym samym chunk_id do jednej Entity zanim przekażesz do SemanticMapper W2?
- Pokaż przykład analizy zdania technicznego przez SpacyParser — `parser.parse("Wykonawca dostarczył dokumentację projektową")` zwraca: node[0] `{form:'Wykonawca', dep_rel:'nsubj', head:1}`, node[1] `{form:'dostarczył', dep_rel:'root'}`, node[2] `{form:'dokumentację', dep_rel:'obj', head:1}`, node[3] `{form:'projektową', dep_rel:'amod', head:2}`?
- Jak SpacyParser tokenizuje zdanie techniczne z identyfikatorem dokumentu (np. 'CONS-02') — token 'CONS-02' rozpoznawany jako PROPN, dep_rel='nmod' gdy odnosi się do rzeczownika lub 'obj' gdy jest bezpośrednim dopełnieniem czasownika?
- Czy spaCy-pl poradzi sobie z idiomami (MWE) typu 'rzucić okiem' — model `pl_core_news_lg` nie rozkłada idiomów; 'okiem' dostanie dep_rel='obj' zamiast bycia częścią frazy; dodaj `IdiomDetector` jako pre-processing krok przed SpacyParser który zamienia znane idiomy na pojedynczy token?
- Jak zbudować słownik idiomów dla IdiomDetector w domenie prawno-technicznej — plik `idioms.json` z kluczem jako fraza wielowyrazowa i wartością jako forma kanonalna (np. 'wziąć pod uwagę' → 'uwzględnić') ładowany przez SlowosiecAdapter?
- Jak wdrożyć listę `POLISH_IDIOMS` do wykrywania idiomów — słownik `{trigger_token: [(pełna_fraza, forma_kanoniczna)]}` indeksowany pierwszym słowem frazy dla O(1) lookup; `IdiomDetector.detect(tokens)` iteruje tokeny i sprawdza czy kolejne tokeny tworzą znany idiom?
- Jak zaimplementować logikę mapowania ról semantycznych w `DependencyParserAdapter` — metoda `map_roles(nodes: List[DependencyNode]) → Dict[str, str]` iteruje nodes: `dep_rel=='nsubj'` → AGENT, `dep_rel=='obj'` → PATIENT, `dep_rel=='obl' and feats.Case='Ins'` → INSTRUMENT, zwraca `{role: lemma}`?
- Jak wygląda kompletny kod klasy `DependencyParserAdapter` z mapowaniem ról — `class DependencyParserAdapter: def __init__(self, backend: DependencyParser): self._p = backend` + `parse()` deleguje do `_p.parse()`, `map_roles()` buduje dict z `dep_rel` reguł?
- Jak wdrożyć DeepER NER do rozpoznawania specyficznych technologii w tekście — zdefiniuj etykietę TECHNOLOGIA w `NERAdapter.LABELS` i dotrenuj `poldeepner` na przykładach z 'Docker', 'REST API', 'OAuth'; encje TECHNOLOGIA trafiają do EventFrame jako INSTRUMENT jeśli w zdaniu brak innego narzędnika?
- Jak przejść do implementacji DeepER rozpoznawania nazw — kroki: (1) załaduj model `poldeepner.load('pl-nkjp')`, (2) tokenizuj przez Morfeusz, (3) uruchom `model.predict(tokens)`, (4) konwertuj BIO spans → `List[Entity]`, (5) scal wielotokenowe encje (B-X…I-X) do jednego Entity przed przekazaniem do SemanticMapper?
- Czy spaCy-pl poprawnie rozpoznaje polskie idiomy w drzewie zależności — `IdiomDetector.detect()` musi wywołać się PRZED `SpacyParser.parse()` bo drzewo zbudowane na nie-scalonych idiomach da błędne dep_rel; weryfikuj test: 'Wykonawca wziął pod uwagę wymagania' z idiomem i bez?
- Jak zintegrować DeepER NER ze Słowosiecią — po `ner_adapter.recognize(sentence)` dla każdej encji ORGANIZACJA wywołaj `SlowosiecAdapter.get_synset(entity.form)`, jeśli istnieje synset dodaj `entity.synset_id`; encje bez synsetu trafiają do `KGT.capture_ign(entity.form)` jako OOV?
- Jak rozróżnić fakt od wymagania za pomocą tagów Morfeusza — tag MSD `praet` (czas przeszły) lub `fin` (czas teraźniejszy) + brak leksemów modalnych → FACT; obecność leksemu 'musi/powinien/należy' z tagiem `fin` lub forma imperatywna (`impt`) → REQUIREMENT; Morfeusz zwraca pełny MSD string który SemanticMapper parsuje przez `feats['Mood']`?
- Jakie biblioteki Python ułatwią parsowanie formatów XML z NKJP?
- Jakie są główne słabości modelu symbolicznego w porównaniu do LLM?
- Jakie narzędzia w Pythonie pomogą mi zautomatyzować ekstrakcję z NKJP?
- Dlaczego język polski sprzyja budowie grafowych modeli semantycznych?
- Jakie są największe słabości symbolicznego modelu NLP?
- Dlaczego język polski sprzyja budowie systemów grafowych?
- Pokaż przykład wzorca fasady dla integracji Morfeusza z UDPipe..
- Jakie są różnice między grafem znaczeń a embeddingami?
- Pokaż przykład kodu z BeautifulSoup do ekstrakcji tagów z NKJP.
- Jakie są zalety lxml w porównaniu do standardowego ElementTree?
- Wyjaśnij różnicę między tematem a remą w grafie wiedzy..
- Pokaż przykład kodu wyciągającego tekst z tagów TEI XML..
- Jakie są najczęstsze błędy przy tworzeniu ontologii dla zdarzeń?
- Pokaż kod wyciągający tekst z NKJP używając Beautiful Soup..
- Pokaż skrypt Beautiful Soup do ekstrakcji par forma-lemat z NKJP..
- Jakie są różnice w tagowaniu między Panterą a UDPipe?
- Pokaż przykład analizy tekstu z NKJP przy użyciu lxml..
- Jak pobrać i przetworzyć NKJP za pomocą NLTK?
- Pokaż przykład XPath do wyciągania zdań z plików TEI..
- Przygotuj skrypt Beautiful Soup do ekstrakcji par lematów z NKJP..
- Pokaż skrypt w Beautiful Soup do ekstrakcji par z NKJP..
- Jakie są zalety NLTK w porównaniu do API PELCRA?
- Przejdźmy do Fazy 2 i budowy grafu semantycznego..
- Pokaż jak zrefaktoryzować kod w Fazie REFACTOR..
- Pokaż jak napisać metodę dekodującą surowy wynik CoNLL-U na obiekty..
- Jak stworzyć mapę 50 kluczowych relacji semantycznych dla grafu?
- Pokaż drugą część integracji: przekazanie CoNLL-U do silnika UDPipe.
- Pokaż skrypt Beautiful Soup do ekstrakcji par z NKJP..
- Jak zaimplementować dekoder formatu CoNLL-U na obiekty grafu wiedzy?
- Czy możemy przejść do Fazy 2: budowy grafu relacji semantycznych?
- Jak wyciągnąć wykonawcę akcji z drzewa CoNLL-U?
- Pokaż jak zmapować wynik CoNLL-U na obiekty grafu wiedzy..
- Pokaż jak napisać dekoder formatu CoNLL-U na obiekty grafu..
- Pokaż przykład analizy wymiarów dla zdania z raportu wojskowego.
- Pokaż przykład analizy zdania 'Wykonawca dostarczył dokumentację techniczną z opóźnieniem' w Twoim grafie..
- Jak zapisać ontologię dla Twojego modelu semantycznego?
- Jakie są 3 bariery hamujące rozwój systemów symbolicznych?
- Jakie są korzyści z połączenia LLM z systemem symbolicznym?
- Pokaż gotowy skrypt wczytujący plik z NKJP i wyciągający lematy..
- Jak zaimplementować dynamiczne pobieranie danych przez API PELCRA?
- Pokaż przykład dekodera CoNLL-U na obiekty grafu wiedzy..
- Jak zaimplementować dekoder CoNLL-U na obiekty grafu wiedzy?
- Jakie są kolejne etapy budowy grafu semantycznego?
- Pokaż skrypt parsujący pliki XML z NKJP do CoNLL-U..
- Jakie są 3 fundamentalne braki architektoniczne systemów NLP?
- Jak zaimplementować dekoder z formatu CoNLL-U na obiekty grafu?
- Jak zautomatyzować ekstrakcję danych z NKJP przez API PELCRA?
- Przejdźmy do integracji podstawowych bibliotek NLP w Fazie 0..
- Jak zaimplementować regułę zaspokojenia dla intencji w pluginie?
- Pokaż przykład metody _adapt_to_parser_format w Pythonie..
- Jakie są różnice między grafem semantycznym a ontologią pojęć?
- Jak zaimplementować regułę sprawdzającą intencję w grafie?
- Jak zapisać reguły zaspokojenia wymogów w formacie DRL?
- Dlaczego polska fleksja ułatwia budowę relacji w grafie?
- Pokaż jak napisać regułę wtyczki analyzer_engine dla tych relacji..
- W jaki sposób fleksja ułatwia budowę relacji w grafie?
- Jak wykorzystać polskie przedrostki do opisu stanów w ontologii?
- Jakie są różnice między podejściem Neuro-symbolic AI a Twoim?
- Jakie są zalety systemów symbolicznych nad LLM w analizie dokumentów?
- Jak zautomatyzować generowanie przypadków brzegowych dla polskiej fleksji?
- Jak algorytmicznie wyodrębnić wymiary kontekstu z innych zdań?
- Jak algorytmicznie powiązać etykiety gramatyczne z rolami semantycznymi?
- Pokaż przykład implementacji parsera lxml dla TEI XML..
- Pokaż jak zapisać wymiary zdarzenia prawnego w DRL..
- Jak UDPipe rozpoznaje podmiot niezależnie od pozycji w zdaniu?
- Jak zmapować relacje z UDPipe na role w Słowosieci?
- Jak automatycznie generować węzły pojęć z wyników parsera UDPipe?
- W jaki sposób język polski daje przewagę w modelu grafowym?
- Jakie są główne poziomy innowacyjności w analizie krytycznej projektu?
- Pokaż przykładowy kod transformacji drzewa składniowego w graf..
- Pokaż przykład ontologii dla domen technicznych..
- Jak wyciągać pojęcia z Markdown dla Lintera?
- Jak stworzyć system mapujący klasy dokumentów na szablony walidacyjne?
- Pokaż przykład klasy TEIFile do automatyzacji przetwarzania wielu plików..
- Jak UDPipe wyodrębnia relacje semantyczne z szyku zdania?
- Jak w Fazie REFACTOR wydzielić reguły mapowania do słownika?
- Pokaż przykład automatycznej generacji węzła z wyników parsera..
- Jakie są główne zalety Słowosieci w modelu ontologicznym?
- Pokaż przykład pliku ann_morphosyntax.xml z Korpusu Narodowego..
- Jak połączyć wyciągnięty tekst z tagami w jeden obiekt?
- Czy BeautifulSoup obsłuży duże pliki XML z NKJP wydajnie?
- Jakie narzędzia w Pythonie pomożą mi zautomatyzować ekstrakcję z NKJP.
- Jakie reguły gramatyczne decydują o rodzaju m1 w Morfeuszu?
- Pokaż przykład implementacji reguły wywołującej stan 'nieżywe' w Pythonie..
- Jak zmniejszyć złożoność systemu o 80% przy analizie polszczyzny?
- Jak rozbudować ontologię o relację posiadania dla akcji dać?
- Jak zaimplementować regułę posiadania po akcji 'dać'?
- Jak rozbudować ontologię o wymiary narzędzia i intencji z Fazy 6?
- Jak zaimplementować klasyfikator intencji dla pytań typu 'Gdzie'?
- Jak rozbudować regułę o wymiar narzędzia (np. pismo, pieczęć, podpis elektroniczny)?
- Pokaż implementację logiki QUESTION dla zapytań o lokalizację dokumentacji..
- Jak rozbudować regułę o detekcję zaprzeczeń dla akcji dać?
- Pokaż logikę wykrywania zaprzeczeń dla relacji posiadania..
- Jak załadować dane Słowosieci z plików tekstowych do silnika?
- Pokaż implementację reguły przedziałów czasowych start_time i end_time..
- Pokaż przykład analizy raportu o braku szyfrowania w API..
- Jak rozszerzyć linter o wykrywanie sprzeczności logicznych w dokumentacji?
- Pokaż przykład analizy przyczynowo-kontekstowej dla wymiaru intencji.
- Domknijmy NKJPPipeline do generowania raportów luk — pokaż kod metody close() i finalize_report().
- Jak NKJPPipeline zarządza cyklem życia (init → process → close) dla długich sesji przetwarzania?
- Jak NKJPPipeline buforuje wyniki pośrednie przed wygenerowaniem końcowego GapAnalysisReport?
- Jaki jest sygnał zakończenia pipeline'u — wszystkie dokumenty przetworzone, timeout, czy explicit close()?
- Jak obsłużyć przerwanie NKJPPipeline w połowie przetwarzania — checkpoint i resume od ostatniego dokumentu?
- Jak wdrożyć rekonstrukcję domyślnego podmiotu z końcówki czasownika — jakie pola feats.Person, feats.Number z Morfeusz są potrzebne?
- Jak Morfeusz taguje końcówki bezosobowe (dostarczono, podpisano) — jaki feats zwraca dla form pasywno-bezosobowych?
- Co oznacza znacznik `ign` w tagach MSD Morfeusza — token nieanalizowany, spoza słownika, potencjalny neologizm prawny lub techniczny?
- Jak technicznie powiązać znacznik `ign` z modułem aktywnego uczenia — tokeny z tagiem `ign` eksportowane do JSONL jako kandydaci do etykietowania przez eksperta?
- Jak zaimplementować KnowledgeGapTracker w warstwie W1 — każdy token z tagiem `ign` rejestrowany jako potencjalna luka wiedzy morfosyntaktycznej?
- Jak KnowledgeGapTracker przechwytuje token ign w W1 — hook po `morfeusz.analyse(token)` gdy wynik zawiera tag MSD 'ign': `tracker.capture_ign(token)`?
- Jak KnowledgeGapTracker łączy token ign z kontekstem zdaniowym — wpis UNKNOWN_WORD zawiera pozycję w zdaniu, sąsiednie tokeny i doc_id dla dalszego etykietowania?

### 4. Testowanie
- Jakie konkretne dane z NKJP pobrać do testów lematyzacji?
- Jakie dokładnie dane z NKJP pobrać do testów lematyzacji?
- Jak zautomatyzować wyciąganie zdań z NKJP do datasetu testowego?
- Pokaż jak zintegrować Universal Dependencies z naszym pipeline testowym..
- Pokaż jak zdefiniować testy integracyjne dla warstwy lingwistycznej..
- Pokaż kod testu weryfikującego strukturę drzewa Universal Dependencies..
- Zaproponuj strukturę pliku JSONL dla datasetu testowego z NKJP..
- Zaprojektuj strukturę pliku JSONL dla datasetu testowego z NKJP..
- Pokaż przykład pliku JSONL z datasetem testowym z NKJP..
- Zaprojektujmy strukturę pliku JSONL dla datasetu testowego z NKJP..
- Jak zbudować testy weryfikujące strukturę drzewa zależności w Pythonie?
- Pokaż przykład kodu testu weryfikującego strukturę drzewa zależności..
- Dodajmy do grafu relacje dla testów integracyjnych..
- Pokaż przykład kodu dla testu kontraktowego formatu JSON..
- Pokaż jak napisać test kontraktowy dla wyjścia modułu morfologii..
- Jak stworzyć graf znaczeń dla wariantów testu integracyjnego?
- Pokaż kod testu weryfikującego strukturę drzewa zależności..
- Jak wyliczyć metryki LAS i UAS dla drzew zależności?
- Pokaż jak przygotować dataset testowy z korpusu PDB-UD..
- Pokaż jak napisać testy kontraktowe dla formatu JSON..
- Jak zintegrować Universal Dependencies z potokiem testowym?
- Pokaż jak zdefiniować testy kontraktowe dla formatu JSON między modułami..
- Jak zaimplementować funkcję wyliczającą dokładność LAS i UAS dla drzew?
- Jakie są metryki LAS i UAS dla oceny jakości parsera?
- Pokaż przykład implementacji funkcji wyliczającej metryki LAS i UAS..
- Jak wdrożyć testy mutacyjne w projekcie NLP?
- Pokaż przykład reguły DRL wiążącej UDPipe z testem integracyjnym..
- Pokaż przykład testu integracyjnego dla parsera UDPipe..
- Jak wdrożyć testy złotego wzorca dla parsera w Pythonie?
- Jak stworzyć korpus testowy z użyciem NKJP?
- Jak stworzyć Smoke Test sprawdzający drożność pipeline'u NLP?
- Pokaż jak zmapować wynik z UDPipe na relacje WYMUSZA_TEST..
- Wdrożymy Smoke Test dla całego pipeline'u?
- Napisz czerwony test dla zdania w stronie biernej..
- Napiszmy test jednostkowy dla relacji przed i po..
- Jak zaimplementować test sprawdzający generowanie stanu końcowego dla akcji?
- Stwórzmy test dla reguły narzędzia (Case=Ins), np. 'Zamawiający odrzucił ofertę pismem z dnia 15 marca'..
- Jak napisać test dla pytania "Gdzie znajduje się Jan?"?
- Pokaż test dla pytania "Gdzie znajduje się Jan?".


#### GREEN — implementacja minimalna
- Pokaż jak zaimplementować funkcję get_lemma w fazie GREEN..
- Pokażmy Fazę GREEN i implementację logiki get_lemma..

#### Metryki jakości testów
- Jak wdrożyć Mutation Score powyżej 60% dla modułu lematyzacji?
- Jak w Fazie 0 mierzyć Code Coverage i Mutation Score?
- Jakie metryki, poza Mutation Score, warto mierzyć w Fazie 0?
- Jak zmierzyć Code Coverage i Mutation Score w spaCy?
- Pokaż szkielet testu własnościowego z użyciem biblioteki Hypothesis..
- Pokaż szkielet testu w Hypothesis dla reguł ARCH i SEC..
- Pokaż szkielet testu w Pythonie przy użyciu biblioteki hypothesis.

#### E2E
- Dodajmy do grafu pojęcia testów integracyjnych i E2E..
- Jak dodać relację dla testu E2E?

### 5. Obsługa błędów
- Jak obsłużyć błędy UDPipe w kaskadowym potoku?
- Jak obsłużyć relację 'simultaneous' dla dwóch zdarzeń w grafie?
- Jakie błędy w tagach MSD najczęściej generują fałszywe alarmy?
- Co się dzieje gdy Morfeusz zwróci pustą listę form dla tokena (nieznany leksem spoza słownika NKJP)?
- Jak obsłużyć błąd segmentacji zdania gdy UDPipe zwróci drzewo zależności z brakującym węzłem root?
- Co zrobić gdy tokenizacja zwróci token o długości 0 lub token zawierający tylko znaki specjalne?

### 6. Integracja z innymi warstwami
- Jak zintegrować Morfeusza z naszą strukturą modułów w Fazie 0?
- Pokaż skrypt integrujący Morfeusza z UDPipe w warstwie morfologii..
- Pokaż jak zintegrować Morfeusza z UDPipe w jednym module..
- Jak zintegrować Morfeusza z UDPipe w Fazie 1?
- Przejdźmy do Fazy 1 i podepnijmy UDPipe do składni..
- Pokaż jak podpiąć UDPipe do warstwy składniowej..
- Jak zintegrować UDPipe w katalogu modules dla analizy składni?
- Zintegrujmy UDPipe w modules/syntax, aby przejść do Fazy GREEN..
- Jak zintegrować wyekstrahowane dane z NKJP z obiektami w Pythonie?
- Jak zintegrować Morfeusza z taggerem Concraft zamiast UDPipe?
- Jak skoordynować przekazywanie danych między Morfeuszem a UDPipe w pipeline?
- Pokaż jak zintegrować tagi NER z NKJP w tym formacie..
- Zintegrujmy UDPipe w modules-syntax, aby przejść do Fazy GREEN.
- Jak zintegrować model intencji z naszym potokiem NLP?
- Jak zintegrować zaprzeczenia z logiką posiadania w grafie?
- Czy możemy zintegrować Morfeusza do głębszej analizy morfosyntaktycznej?
- Jak NKJPPipeline z W1 przekazuje przetworzony korpus do W0 (GapAnalysisReport) — batch czy streaming?
- Jakie dane z NKJP są niezbędne dla GapAnalysisReport — lematy, POS, feats, czy cały CoNLL-U?
- Jak weryfikować że pipeline NKJP → GapAnalysis nie traci dokumentów przy przetwarzaniu wsadowym?

### 7. Pułapki i ryzyka
- Jakie są 3 fundamentalne bariery, które zatrzymały podobne projekty?
- Jakie są 3 fundamentalne bariery, które zatrzymują projekty lingwistyczne?
- Jakie są 3 fundamentalne bariery projektów lingwistycznych?
- Jakie są 3 fundamentalne bariery zatrzymujące projekty lingwistyczne?
- Jakie są 3 bariery, które zatrzymały komercyjne silniki logiczne?
- Jakie są 3 fundamentalne bariery dla komercyjnych silników językowych?
- Jakie są 3 fundamentalne bariery w budowie takich silników?
- Jakie są 3 fundamentalne bariery w budowie systemów lingwistycznych?
- Jakie są 3 bariery, które zatrzymały projekty symboliczne?
- Jakie są 3 fundamentalne bariery, które zatrzymują takie projekty?
- Jakie są 3 fundamentalne bariery, które zatrzymują projekty tego typu?
- Jakie są 3 fundamentalne bariery w budowie systemów symbolicznych?
## Pytania uzupełniające
- **Pułapka 4:** Morfeusz2 jest biblioteką C++ z bindings Python — wersja bindings musi być skompilowana dla tej samej wersji Morfeusz2 co słownik; niezgodność wersji powoduje segfault, nie wyjątek.
- **Pułapka 5:** UDPipe model PDB-UD jest trenowany na prasie i literaturze — dla tekstów prawnych/technicznych (dokumentacja projektowa) LAS spada do ~78%, co jest poniżej kryterium akceptacji ≥88%.
- **Pułapka 6:** CoNLL-U numeruje tokeny od 1, Python od 0 — błąd off-by-one w `head` wskazującym na parent jest najczęstszym błędem implementacji dekodera drzewa.

### 1. Architektura

- Jak podzielić odpowiedzialność między `modules/morphology/`, `modules/syntax/`, `modules/corpus/`?
- Jaki wzorzec projektowy zastosować dla integracji Morfeusz ↔ UDPipe (Adapter, Facade, Pipeline)?
- Jak izolować zależność od zewnętrznych bibliotek (Morfeusz, UDPipe), aby dało się je zamienić bez zmiany W2?
- Jaka jest minimalna publiczna API warstwy W1 eksponowana dla W2 (lista metod + typy)?
- Jak obsłużyć brak dostępności Morfeusza w środowisku CI (mock/stub)?

### 2. Kontrakty danych

- Jaki jest formalny schemat JSON dla obiektu `Token` wychodzącego z W1 do W2?
- Jak reprezentować drzewo zależności CoNLL-U jako obiekt Pythona przekazywany dalej?
- Jakie pola MSD (Morfeusz) są obowiązkowe, a jakie opcjonalne w kontrakcie W1 → W2?
- Jak walidować format CoNLL-U przed przekazaniem do W2 (schema validation)?
- Jak zdefiniować typ `DependencyNode` z polami: `id, form, lemma, upos, feats, head, deprel`?

### 3. Implementacja

- Jak zaimplementować `get_lemma(form, context)` z ujednoznacznianiem przez Morfeusz?
- Jak zaimplementować dekoder CoNLL-U → lista obiektów Python (`parse_conllu(text) -> List[Sentence]`)?
- Jak skonfigurować UDPipe dla języka polskiego (model PDB-UD, punkt wejścia)?
- Jak zaimplementować ekstraktor danych z NKJP XML (TEI P5) do JSONL?
- Jak zaimplementować `_adapt_to_parser_format()` tłumaczący Morfeusz → UDPipe?

### 4. Testowanie

- Jak zbudować oracle dataset z NKJP do testowania dokładności lematyzacji (format JSONL)?
- Jak napisać test własnościowy (Hypothesis) sprawdzający `get_lemma(form)` — jakie niezmienniki?
- Jak wdrożyć pomiar LAS/UAS dla drzew zależności UDPipe na zbiorze testowym?
- Jak mierzyć Mutation Score ≥ 60% dla modułu lematyzacji?
- Jak pisać testy złotego wzorca dla parsera, których dane nie mogą być generowane przez LLM?
#### Kompletna hierarchia TDD
- Jak zrefaktoryzować `LemmatizationEngine` po fazie GREEN — wydzielić `MorfeuszAdapter`, `UDPipeAdapter` za interfejsem `ILemmatizer`?
- Zrefaktoryzuj moduł W1 tak aby `DependencyParser` i `Lemmatizer` były wymienialne — test powinien pozostać zielony po swapie.
- Jak napisać test integracyjny W1→W2: `tokenize('Wykonawca dostarczył dokumentację z opóźnieniem')` → sprawdź że W2 dostaje `dep_rel` per token?
- Jak wykryć że aktualizacja modelu UDPipe (v2→v3) regresuje quality metryki — co zautomatyzować w CI?
- Stwórz snapshot test lematyzacji: 100 zdań + oczekiwane lematy zapisane jako golden file — alarm gdy Morfeusz2 zwróci inny lemat.
- Jak przetestować W1 end-to-end na zdaniu wielozdaniowym (10 zdań) — sprawdzić że wszystkie tokeny mają `feats.Case` gdzie `upos=NOUN`?
- Stwórzmy plik `test_dependency_parser.py` z testami TDD — struktura: `TestUDPipeParser` (parse+CoNLL-U schema), `TestSpacyParser` (parse+dep_rel), `TestParserSwap` (ten sam wynik po wymianie backendu) jako trzy klasy w pytest?
- Dopiszmy testy dla idiomów takich jak 'wziąć pod uwagę' — `test_idiom_detection`: `IdiomDetector.detect(["wziął","pod","uwagę"])` zwraca `[{phrase:"wziąć pod uwagę", canonical:"uwzględnić", start:0}]`; następnie `SpacyParser.parse()` na scalonym tokenie daje poprawny dep_rel='obj' zamiast 'obl'?
- Jak napisać czerwony test TDD dla DependencyParser — `assert parser.parse("Wykonawca złożył ofertę")[0].dep_rel == 'nsubj'` przed implementacją SpacyParser, wtedy GREEN po dodaniu `token.dep_`→`dep_rel` mapping?

### 5. Obsługa błędów

- Co robi `get_lemma()` dla nieznanych form (OOV — Out of Vocabulary)?
- Jak system obsłuży brakujące pojęcia OOV w W1 — token `ign` z Morfeusza → `KnowledgeGapTracker.capture_ign(token)` → wpis do kolejki aktywnego uczenia zamiast wyjątku?
- Jak OOV token z W1 jest propagowany przez pipeline — `ign` tag w CoNLL-U oznacza low-confidence, InferenceEngine w W5 traktuje go jako UNKNOWN_WORD i nie emituje :CAUSES?
- Jak obsługiwać synkretyzm form (słowo "dam" = 1sg futurum LUB G.pl. "dama") bez UDPipe?
- Co zwrócić, gdy UDPipe nie może sparsować zdania (brak modelu, malformed input)?
- Jak logować błędy parsowania NKJP XML (uszkodzone tagi TEI, brakujące atrybuty)?
- Jak zachowuje się system przy polskich znakach diakrytycznych błędnie zakodowanych (ISO-8859-2)?
- Jak W1 obsługuje zdania z emotjami lub hashtagami (`#python`, `😀`) których Morfeusz nie rozpoznaje?
- Co zwrócić gdy plik NKJP XML jest niekompletny (urwany w połowie tagu TEI) — częściowy wynik czy błąd krytyczny?

### 6. Integracja z innymi warstwami

- Jak W1 przekazuje `DependencyTree` do W2 — przez shared memory, plik JSONL, czy bezpośredni obiekt Python?
- Jak W0 (doc audit) skorzysta z lematyzacji W1 do poprawy wykrywania duplikatów?
- Jak W4 (Neo4j) przyjmie tokeny z W1 — bezpośrednio z obiektu czy przez serializację JSONL?
- Jak W1 powinno być wersjonowane, aby zmiana modelu UDPipe nie łamała testów W2?
- Jak W1 obsługuje przypadek gdy W3 (zasoby leksykalne) zwróci uzupełnienie lematu po tokenizacji?
- Jak weryfikować że format CoNLL-U wychodzący z W1 spełnia kontrakt wejściowy W2?
- Jak W1 informuje W8 (compliance audit) o błędach tokenizacji które mogą wpłynąć na identyfikację naruszeń?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Morfeusz zwraca listę interpretacji dla formy — błędny wybór = błędna lematyzacja = propagacja błędu do W2 (AGENT zamiast PATIENT). Konieczny WSD (W3) już w W1.
- **Pułapka 2:** NKJP XML (TEI P5) ma nieregularne warianty tagowania między podkorpusami — parser musi obsługiwać `ann_morphosyntax.xml` w różnych wersjach schematu.
- **Pułapka 3:** UDPipe model PDB-UD ma coverage ~92% dla współczesnej polszczyzny — pozostałe 8% trafia jako błędy do W2; potrzebny fallback (Concraft lub rule-based).
- **Pułapka 4:** Morfeusz2 to biblioteka C++ z bindings Python — niezgodność wersji bindings ze słownikiem powoduje segfault, nie wyjątek Pythona.
- **Pułapka 5:** UDPipe PDB-UD trenowany na prasie — dla tekstów prawnych/technicznych LAS spada do ~78%, poniżej kryterium ≥88%.
- **Pułapka 6:** CoNLL-U numeruje tokeny od 1, Python od 0 — off-by-one w polu `head` to najczęstszy błąd dekodera drzewa.

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Dokładność lematyzacji na oracle NKJP | ≥ 95% |
| LAS (Labeled Attachment Score) dla UDPipe | ≥ 88% |
| UAS (Unlabeled Attachment Score) dla UDPipe | ≥ 92% |
| Czas przetwarzania 1000 zdań | < 30 s |
| Mutation Score testów | ≥ 60% |
| Pokrycie linii testami | ≥ 90% |

## Pytania o idempotentność i deterministyczność

- Czy `get_lemma("zabił", context)` zawsze zwraca to samo dla identycznego kontekstu?
- Czy wynik UDPipe dla identycznego zdania jest deterministyczny (wielokrotne wywołania)?
- Jak zapewnić deterministyczność przy batch processingu — czy kolejność zdań w JSONL ma znaczenie?

## Pytania o migrację i wersjonowanie

- Jak migrować oracle dataset gdy aktualizujemy model UDPipe (stare testy vs nowy model)?
- Jak wersjonować schemat `DependencyNode` gdy dodajemy nowe pola (feats, misc)?
- Jak zapewnić backwards-compatibility dla API W1 gdy W2 jest już zaimplementowane?

## Pytania o audytowalność

- Jak logować, który model UDPipe (wersja, hash pliku) wygenerował dany wynik?
- Jak zachować lad dowodowniczy: dla każdego tokenu — z jakiego zdania pochodzi, z jakiego dokumentu?
- Jak wygenerować raport "dlaczego lemat X zamiast Y" dla procesu wyjaśniającego klientowi?

---

## Rozszerzalność i skalowanie

### Stopniowe komplikowanie zdań (progressive sentence complexity)

- Jak W1 obsługuje sekwencję: zdanie proste → zdanie złożone → zdanie wielokrotnie złożone?
- Jak UDPipe radzi sobie ze zdaniem 80-tokenowym (typowe w dokumentach prawnych)?
- Jak testować W1 dla każdego poziomu kompleksji osobno — test suite per typ zdania?
- Jak zaimplementować `sentence_complexity_score(tree)` — metryka złożoności drzewa składniowego?
- Jak wykrywać zdania z eliptyczną strukturą (bez czasownika, bez podmiotu) w drzewie UDPipe?
- Jak stopniowo budować oracle dataset: najpierw 50 prostych zdań → 50 złożonych → 50 prawnych?

### Stopniowe rozszerzanie słownictwa (pipeline NKJP)

- Jak inkrementalnie dodawać nowe zdania z NKJP bez przetwarzania całego korpusu od nowa?
- Jak wykrywać nowe OOV (Out-of-Vocabulary) formy w nowych dokumentach i logować je?
- Jak zaimplementować `enrich_morfeusz(form, lemma, msd)` — dynamiczne dodawanie form?
- Jak pipeline NKJP radzi sobie z plikami XML o rozmiarach 1 MB / 100 MB / 1 GB?
- Jakie są techniki streamowego parsowania TEI XML (SAX zamiast DOM) dla dużych plików?

### Skalowanie batch processingu

- Jak przetworzyć 100k zdań z NKJP w trybie batch — równolegle czy sekwencyjnie?
- Jak zaimplementować `batch_lemmatize(sentences, workers=4)` z progress bar?
- Jakie są bottlenecks pipeline W1 przy 1000 zdań/s — Morfeusz, UDPipe czy I/O?
- Jak testować wydajność W1 dla różnych rozmiarów batch (1, 10, 100, 1000 zdań)?
- Jak zaimplementować checkpoint — zapis stanu przetwarzania co 1000 zdań (resume po crash)?

### Inkrementalne aktualizacje modeli

- Jak aktualizować model UDPipe bez przerywania działającego serwisu?
- Jak zachować backwards-compatibility testów gdy model lematyzacji jest ulepszony?
- Jak wersjonować pliki modeli (morfeusz.dict, udpipe.model) — hash SHA + git LFS?

---

## Luki zidentyfikowane przez audyt cross-warstwowy

### Kontrakt W1 → W2: pole `feats` (Case, Voice, Number)

- Które pola `feats` z Morfeusza są **obowiązkowe** w `DependencyNode` przekazywanym do W2 — minimum: `Case`, `Voice`, `Number`, `Gender`?
- Jak zakodować brak pola `feats` dla tokenów, których Morfeusz nie przeanalizował?
- Jak zwalidować, że `DependencyNode` ma wymagane `feats` zanim trafi do `SemanticMapper` (W2)?
- Dlaczego `Case=Ins` (narzędnik) jest krytyczny dla W2 — jakie role nie zadziałają bez tego pola?
- Jak testować, że `feats` są poprawnie propagowane przez cały pipeline (unit + integracyjny)?

### Fallback parser (gdy UDPipe zawodzi ~8% zdań)

- Kiedy pipeline ma przełączyć się z UDPipe na Concraft — jaki próg błędu (`parse_score < X`) triggeruje fallback?
- Jak zaimplementować `parse_with_fallback(sentence)` — try UDPipe → on failure → Concraft → on failure → rule-based?
- Jak mierzyć, ile % zdań w korpusie testowym wymaga fallbacku?
- Jak testować, że wynik fallbacku Concraft jest kompatybilny ze schematem `DependencyNode` oczekiwanym przez W2?
- Czy fallback ma być synchroniczny (w tym samym wywołaniu) czy asynchroniczny (flagowanie do re-analizy)?

### Hak W0 na lematyzację W1 (integracja zwrotna)

- Jak W0 (`doc_auditor.py`) podpina się pod lematyzację W1 jako wymienialny backend — interfejs czy bezpośredni import?
- Jak zdefiniować interfejs `ILemmatizer` który implementuje zarówno prosty stemmer W0 jak i Morfeusz W1?
- Jak W0 wykrywa, że W1 jest dostępne i przełącza się automatycznie (lub przez konfigurację)?
- Jak przetestować W0 z backendem W1 vs własnym TF-IDF — czy wyniki `completeness_score` się poprawiają?
