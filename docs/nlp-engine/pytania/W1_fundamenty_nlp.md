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

- Jakie konkretne dane z NKJP pobrać do testów lematyzacji?
- Jak zintegrować Morfeusza z naszą strukturą modułów w Fazie 0?
- Pokaż jak zaimplementować funkcję get_lemma w fazie GREEN..
- Przedstaw model danych grafu wiedzy dla przykładu ze zwierzęciem..
- Jakie dokładnie dane z NKJP pobrać do testów lematyzacji?
- Jak zautomatyzować wyciąganie zdań z NKJP do datasetu testowego?
- Jak wdrożyć Mutation Score powyżej 60% dla modułu lematyzacji?
- Pokaż jak zintegrować Universal Dependencies z naszym pipeline testowym..
- Jakie są 3 fundamentalne bariery, które zatrzymały podobne projekty?
- Wyszukaj źródła i skrypty do automatyzacji ekstrakcji danych z NKJP..
- Pokażmy Fazę GREEN i implementację logiki get_lemma..
- Skonfigurujmy UDPipe jako parser składni zależności w modules..
- Pokaż skrypt integrujący Morfeusza z UDPipe w warstwie morfologii..
- Stwórz przykładowy JSON kontraktu danych między modułem morfologii a składni..
- Jakie biblioteki Python ułatwią parsowanie formatów XML z NKJP?
- Pokaż jak zintegrować Morfeusza z UDPipe w jednym module..
- Jak zintegrować Morfeusza z UDPipe w Fazie 1?
- Pokaż jak zdefiniować testy integracyjne dla warstwy lingwistycznej..
- Jakie są główne słabości modelu symbolicznego w porównaniu do LLM?
- Jak w Fazie 0 mierzyć Code Coverage i Mutation Score?
- Jakie narzędzia w Pythonie pomogą mi zautomatyzować ekstrakcję z NKJP?
- Przejdźmy do Fazy 1 i podepnijmy UDPipe do składni..
- Pokaż jak podpiąć UDPipe do warstwy składniowej..
- Pokaż przykład formatu JSON dla kontraktu danych modułu morfologii..
- Jakie są 3 fundamentalne bariery, które zatrzymują projekty lingwistyczne?
- Dlaczego język polski sprzyja budowie grafowych modeli semantycznych?
- Pokaż kod testu weryfikującego strukturę drzewa Universal Dependencies..
- Jakie są największe słabości symbolicznego modelu NLP?
- Dlaczego język polski sprzyja budowie systemów grafowych?
- Zaproponuj strukturę pliku JSONL dla datasetu testowego z NKJP..
- Jak zintegrować UDPipe w katalogu modules dla analizy składni?
- Zaprojektuj strukturę pliku JSONL dla datasetu testowego z NKJP..
- Jakie metryki, poza Mutation Score, warto mierzyć w Fazie 0?
- Pokaż przykład pliku JSONL z datasetem testowym z NKJP..
- Zintegrujmy UDPipe w modules/syntax, aby przejść do Fazy GREEN..
- Pokaż przykład wzorca fasady dla integracji Morfeusza z UDPipe..
- Zaprojektujmy strukturę pliku JSONL dla datasetu testowego z NKJP..
- Jak zbudować testy weryfikujące strukturę drzewa zależności w Pythonie?
- Jak zmierzyć Code Coverage i Mutation Score w spaCy?
- Pokaż szkielet testu własnościowego z użyciem biblioteki Hypothesis..
- Jakie są różnice między grafem znaczeń a embeddingami?
- Dodajmy do grafu pojęcia testów integracyjnych i E2E..
- Pokaż przykład kodu z BeautifulSoup do ekstrakcji tagów z NKJP.
- Jakie są zalety lxml w porównaniu do standardowego ElementTree?
- Jak zintegrować wyekstrahowane dane z NKJP z obiektami w Pythonie?
- Pokaż przykład kodu testu weryfikującego strukturę drzewa zależności..
- Jak zaplanować Faze REFACTOR dla modułu nlp_processor?
- Wyjaśnij różnicę między tematem a remą w grafie wiedzy..
- Pokaż szkielet testu w Hypothesis dla reguł ARCH i SEC..
- Dodajmy do grafu relacje dla testów integracyjnych..
- Pokaż przykład kodu dla testu kontraktowego formatu JSON..
- Pokaż jak napisać test kontraktowy dla wyjścia modułu morfologii..
- Jak stworzyć graf znaczeń dla wariantów testu integracyjnego?
- Pokaż kod testu weryfikującego strukturę drzewa zależności..
- Pokaż przykład kodu wyciągającego tekst z tagów TEI XML..
- Jakie są najczęstsze błędy przy tworzeniu ontologii dla zdarzeń?
- Jak stworzyć strukturę ontologii dla grafu znaczeń?
- Pokaż kod wyciągający tekst z NKJP używając Beautiful Soup..
- Pokaż skrypt Beautiful Soup do ekstrakcji par forma-lemat z NKJP..
- Jakie są różnice w tagowaniu między Panterą a UDPipe?
- Pokaż przykład analizy tekstu z NKJP przy użyciu lxml..
- Jak pobrać i przetworzyć NKJP za pomocą NLTK?
- Pokaż przykład XPath do wyciągania zdań z plików TEI..
- Przygotuj skrypt Beautiful Soup do ekstrakcji par lematów z NKJP..
- Jak wyliczyć metryki LAS i UAS dla drzew zależności?
- Pokaż jak przygotować dataset testowy z korpusu PDB-UD..
- Pokaż skrypt w Beautiful Soup do ekstrakcji par z NKJP..
- Jakie są zalety NLTK w porównaniu do API PELCRA?
- Przejdźmy do Fazy 2 i budowy grafu semantycznego..
- Pokaż jak zrefaktoryzować kod w Fazie REFACTOR..
- Pokaż jak napisać metodę dekodującą surowy wynik CoNLL-U na obiekty..
- Jak stworzyć mapę 50 kluczowych relacji semantycznych dla grafu?
- Chcę przejść do projektowania struktury grafu wiedzy dla lintera.
- Pokaż drugą część integracji: przekazanie CoNLL-U do silnika UDPipe.
- Jak zintegrować Morfeusza z taggerem Concraft zamiast UDPipe?
- Pokaż skrypt Beautiful Soup do ekstrakcji par z NKJP..
- Pokaż jak napisać testy kontraktowe dla formatu JSON..
- Jak zintegrować Universal Dependencies z potokiem testowym?
- Jak zaimplementować dekoder formatu CoNLL-U na obiekty grafu wiedzy?
- Pokaż jak zdefiniować testy kontraktowe dla formatu JSON między modułami..
- Czy możemy przejść do Fazy 2: budowy grafu relacji semantycznych?
- Jak wyciągnąć wykonawcę akcji z drzewa CoNLL-U?
- Jak obsłużyć błędy UDPipe w kaskadowym potoku?
- Jak zaimplementować funkcję wyliczającą dokładność LAS i UAS dla drzew?
- Pokaż jak zmapować wynik CoNLL-U na obiekty grafu wiedzy..
- Pokaż jak napisać dekoder formatu CoNLL-U na obiekty grafu..
- Jakie są metryki LAS i UAS dla oceny jakości parsera?
- Pokaż przykład analizy wymiarów dla zdania z raportu wojskowego.
- Pokaż przykład analizy zdania "Jan zabił zwierzę" w Twoim grafie..
- Jak zapisać ontologię dla Twojego modelu semantycznego?
- Jakie są 3 bariery hamujące rozwój systemów symbolicznych?
- Pokaż przykład implementacji funkcji wyliczającej metryki LAS i UAS..
- Pokaż szkielet testu w Pythonie przy użyciu biblioteki hypothesis.
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
- Które moduły warto zrealizować najpierw w planie 12-18 miesięcy?
- Jak stworzyć funkcję mapującą format CoNLL-U na graf wiedzy?
- Pokaż jak zintegrować Morfeusza z UDPipe przez format TEI P5..
- Jakie są 3 fundamentalne bariery projektów lingwistycznych?
- Jak skoordynować przekazywanie danych między Morfeuszem a UDPipe w pipeline?
- Pokaż skrypt Python do generowania pliku JSONL z NKJP.
- Przejdźmy do integracji podstawowych bibliotek NLP w Fazie 0..
- Pokaż skrypt konwertujący XML z NKJP na format JSONL..
- Jak zaimplementować regułę zaspokojenia dla intencji w pluginie?
- Pokaż skrypt Python do konwersji XML z NKJP na format JSONL..
- Pokaż przykład metody _adapt_to_parser_format w Pythonie..
- Jakie są różnice między grafem semantycznym a ontologią pojęć?
- Jakie są 3 fundamentalne bariery zatrzymujące projekty lingwistyczne?
- Jak napisać skrypt konwertujący XML z NKJP do JSONL?
- Jakie metadane z NKJP warto uwzględnić w pliku JSONL?
- Pokaż jak zintegrować tagi NER z NKJP w tym formacie..
- Pokaż skrypt Python konwertujący XML z NKJP do JSONL..
- Jak zaimplementować regułę sprawdzającą intencję w grafie?
- Jakie są główne różnice między formatami TEI P5 i JSONL?
- Pokaż skrypt Python do konwersji XML z NKJP na JSONL..
- Jak zapisać reguły zaspokojenia wymogów w formacie DRL?
- Dlaczego polska fleksja ułatwia budowę relacji w grafie?
- Pokaż jak napisać regułę wtyczki analyzer_engine dla tych relacji..
- W jaki sposób fleksja ułatwia budowę relacji w grafie?
- Jak wykorzystać polskie przedrostki do opisu stanów w ontologii?
- Jakie są różnice między podejściem Neuro-symbolic AI a Twoim?
- Jakie są 3 bariery, które zatrzymały komercyjne silniki logiczne?
- Jakie są zalety systemów symbolicznych nad LLM w analizie dokumentów?
- Jak wdrożyć testy mutacyjne w projekcie NLP?
- Jak zautomatyzować generowanie przypadków brzegowych dla polskiej fleksji?
- Jak algorytmicznie wyodrębnić wymiary kontekstu z innych zdań?
- Pokaż jak rozwiązać konflikt między modułami Unit i Security..
- Jakie są 3 fundamentalne bariery dla komercyjnych silników językowych?
- Pokaż przykład reguły DRL wiążącej UDPipe z testem integracyjnym..
- Jakie są 3 fundamentalne bariery w budowie takich silników?
- Jak algorytmicznie powiązać etykiety gramatyczne z rolami semantycznymi?
- Pokaż przykład implementacji parsera lxml dla TEI XML..
- Pokaż jak zapisać wymiary zdarzenia prawnego w DRL..
- Pokaż przykład testu integracyjnego dla parsera UDPipe..
- Jak wdrożyć testy złotego wzorca dla parsera w Pythonie?
- Jakie są 3 fundamentalne bariery w budowie systemów lingwistycznych?
- Jak UDPipe rozpoznaje podmiot niezależnie od pozycji w zdaniu?
- Jak zmapować relacje z UDPipe na role w Słowosieci?
- Jak automatycznie generować węzły pojęć z wyników parsera UDPipe?
- W jaki sposób język polski daje przewagę w modelu grafowym?
- Jak stworzyć korpus testowy z użyciem NKJP?
- Jakie są 3 bariery, które zatrzymały projekty symboliczne?
- Jak stworzyć Smoke Test sprawdzający drożność pipeline'u NLP?
- Jakie są główne poziomy innowacyjności w analizie krytycznej projektu?
- Pokaż przykładowy kod transformacji drzewa składniowego w graf..
- Pokaż przykład ontologii dla domen technicznych..
- Pokaż jak zmapować wynik z UDPipe na relacje WYMUSZA_TEST..
- Wdrożymy Smoke Test dla całego pipeline'u?
- Jak wyciągać pojęcia z Markdown dla Lintera?
- Jak stworzyć system mapujący klasy dokumentów na szablony walidacyjne?
- Pokaż przykład klasy TEIFile do automatyzacji przetwarzania wielu plików..
- Jak UDPipe wyodrębnia relacje semantyczne z szyku zdania?
- Jak w Fazie REFACTOR wydzielić reguły mapowania do słownika?
- Napisz czerwony test dla zdania w stronie biernej..
- Pokaż przykład automatycznej generacji węzła z wyników parsera..
- Jakie są główne zalety Słowosieci w modelu ontologicznym?
- Pokaż przykład pliku ann_morphosyntax.xml z Korpusu Narodowego..
- Jak połączyć wyciągnięty tekst z tagami w jeden obiekt?
- Czy BeautifulSoup obsłuży duże pliki XML z NKJP wydajnie?
- Jak dodać relację dla testu E2E?
- Jakie narzędzia w Pythonie pomożą mi zautomatyzować ekstrakcję z NKJP.
- Zintegrujmy UDPipe w modules-syntax, aby przejść do Fazy GREEN.
- Pokaż strukturę grafu dla zdania Jan zabił zwierzę.
- Napiszmy test jednostkowy dla relacji przed i po..
- Jakie reguły gramatyczne decydują o rodzaju m1 w Morfeuszu?
- Jak zaprojektować ontologię dla wielowymiarowej analizy zdarzenia „zabić”?
- Jakie są 3 fundamentalne bariery, które zatrzymują takie projekty?
- Jak zaimplementować test sprawdzający generowanie stanu końcowego dla akcji?
- Pokaż przykład implementacji reguły wywołującej stan 'nieżywe' w Pythonie..
- Stwórzmy test dla reguły narzędzia, np. 'Jan zabił zwierzę nożem'..
- Jakie są 3 fundamentalne bariery, które zatrzymują projekty tego typu?
- Jak zmniejszyć złożoność systemu o 80% przy analizie polszczyzny?
- Jak zintegrować model intencji z naszym potokiem NLP?
- Jak napisać test dla pytania "Gdzie znajduje się Jan?"?
- Jak rozbudować ontologię o relację posiadania dla akcji dać?
- Pokaż test dla pytania "Gdzie znajduje się Jan?".
- Jak zaimplementować regułę posiadania po akcji 'dać'?
- Jak rozbudować ontologię o wymiary narzędzia i intencji z Fazy 6?
- Jak zaimplementować klasyfikator intencji dla pytań typu 'Gdzie'?
- Jak rozbudować regułę o wymiar narzędzia (np. broń)?
- Jakie są 3 fundamentalne bariery w budowie systemów symbolicznych?
- Pokaż implementację logiki QUESTION dla zapytań o lokalizację Jana..
- Jak zintegrować zaprzeczenia z logiką posiadania w grafie?
- Jak rozbudować regułę o detekcję zaprzeczeń dla akcji dać?
- Pokaż jak sfinalizować architekturę i podsumować ten etap..
- Pokaż logikę wykrywania zaprzeczeń dla relacji posiadania..
- Pokaż strukturę ontologii dla wielodomenowej klasyfikacji zdarzeń..
- Jak załadować dane Słowosieci z plików tekstowych do silnika?
- Czy możemy zintegrować Morfeusza do głębszej analizy morfosyntaktycznej?
- Pokaż implementację reguły przedziałów czasowych start_time i end_time..
- Jak obsłużyć relację 'simultaneous' dla dwóch zdarzeń w grafie?
- Pokaż przykład analizy raportu o braku szyfrowania w API..
- Jak rozszerzyć linter o wykrywanie sprzeczności logicznych w dokumentacji?
- Pokaż przykład analizy przyczynowo-kontekstowej dla wymiaru intencji.
- Jakie błędy w tagach MSD najczęściej generują fałszywe alarmy?
- Dodajmy tagi YAML do dokumentacji Markdown projektu.
- dodatkowe od godziny 8:43.
- Jak dodać tagi YAML do moich plików Markdown?

## Pytania uzupełniające

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

### 5. Obsługa błędów

- Co robi `get_lemma()` dla nieznanych form (OOV — Out of Vocabulary)?
- Jak obsługiwać synkretyzm form (słowo "dam" = 1sg futurum LUB G.pl. "dama") bez UDPipe?
- Co zwrócić, gdy UDPipe nie może sparsować zdania (brak modelu, malformed input)?
- Jak logować błędy parsowania NKJP XML (uszkodzone tagi TEI, brakujące atrybuty)?
- Jak zachowuje się system przy polskich znakach diakrytycznych błędnie zakodowanych (ISO-8859-2)?

### 6. Integracja z innymi warstwami

- Jak W1 przekazuje `DependencyTree` do W2 — przez shared memory, plik JSONL, czy bezpośredni obiekt Python?
- Jak W0 (doc audit) skorzysta z lematyzacji W1 do poprawy wykrywania duplikatów?
- Jak W4 (Neo4j) przyjmie tokeny z W1 — bezpośrednio z obiektu czy przez serializację JSONL?
- Jak W1 powinno być wersjonowane, aby zmiana modelu UDPipe nie łamała testów W2?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Morfeusz zwraca listę interpretacji dla formy — błędny wybór = błędna lematyzacja = propagacja błędu do W2 (AGENT zamiast PATIENT). Konieczny WSD (W3) już w W1.
- **Pułapka 2:** NKJP XML (TEI P5) ma nieregularne warianty tagowania między podkorpusami — parser musi obsługiwać `ann_morphosyntax.xml` w różnych wersjach schematu.
- **Pułapka 3:** UDPipe model PDB-UD ma coverage ~92% dla współczesnej polszczyzny — pozostałe 8% trafia jako błędy do W2; potrzebny fallback (Concraft lub rule-based).

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
