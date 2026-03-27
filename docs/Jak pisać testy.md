Dobra, to całkiem rozległy temat — podzielę go na trzy części: **rodzaje testów z opisami**, **wzory matematyczne do kalkulacji pokrycia**, i **hierarchię pisania testów**. Zacznijmy od wizualizacji hierarchii, bo to fundament całego podejścia.---

## Pełna lista rodzajów i typów testów

### Testy jednostkowe (Unit Tests)

**Co wykrywają:** Błędy w logice pojedynczej funkcji lub metody w izolacji od reszty systemu. Weryfikują, czy dana jednostka kodu zwraca poprawny wynik dla określonego wejścia. Wykrywają edge case'y, błędy obliczeń i nieprawidłowe transformacje danych.

### Testy integracyjne (Integration Tests)

**Co wykrywają:** Błędy w komunikacji między dwoma lub więcej modułami — czy poprawnie wymieniają dane, czy kontrakt między nimi jest zachowany. Wykrywają rozbieżności w formatach danych, problemy z kolejnością wywołań i błędy w warstwie repozytorium/bazodanowej.

### Testy komponentów (Component Tests)

**Co wykrywają:** Czy cały moduł/komponent działa poprawnie jako czarna skrzynka, z podmocowanymi (mock) zależnościami zewnętrznymi. Weryfikują logikę biznesową w obrębie granicy modułu bez uruchamiania rzeczywistej infrastruktury.

### Testy kontraktowe (Contract Tests)

**Co wykrywają:** Czy API producenta i konsumenta rozumieją ten sam kontrakt — ten sam schemat JSON, te same kody statusu, te same typy pól. Wykrywają breaking changes zanim trafią na środowisko integracyjne. Szczególnie ważne w mikroserwisach.

### Testy API (API Tests / Service Tests)

**Co wykrywają:** Poprawność odpowiedzi HTTP — kody statusu, nagłówki, strukturę ciała odpowiedzi, obsługę błędów. Weryfikują, czy endpoint zachowuje się zgodnie ze specyfikacją dla różnych scenariuszy wejścia.

### Testy end-to-end (E2E Tests)

**Co wykrywają:** Czy pełna ścieżka użytkownika przez system działa od początku do końca — od UI/CLI przez backend aż do bazy. Wykrywają regresje widoczne tylko wtedy, gdy wszystkie warstwy działają razem. Najwolniejsze i najdroższe.

### Testy regresji (Regression Tests)

**Co wykrywają:** Czy naprawienie jednego błędu nie zepsuło czegoś, co działało wcześniej. To nie oddzielny typ — to zbiór testów (unit/integration) uruchamianych po każdej zmianie. Ich rola rośnie z wiekiem systemu.

### Testy akceptacyjne (Acceptance Tests / UAT)

**Co wykrywają:** Czy system spełnia wymagania biznesowe z perspektywy użytkownika końcowego lub właściciela produktu. Opisywane językiem domenowym (Gherkin/BDD), weryfikują "czy system robi to, co miał robić", a nie "czy kod jest poprawny".

### Testy wydajnościowe (Performance Tests)

**Co wykrywają:** Czy system spełnia wymagania czasowe pod określonym obciążeniem. Dzielą się na: load (normalne obciążenie), stress (powyżej limitu), soak/endurance (długotrwałe), spike (nagłe skoki). Wykrywają memory leaki, bottlenecki, degradację pod obciążeniem.

### Testy mutacyjne (Mutation Tests)

**Co wykrywają:** Czy Twoje testy są wystarczająco czujne — mutant to sztucznie wprowadzony błąd w kodzie produkcyjnym (`+` zamienione na `-`, `>` na `>=` itp.). Jeśli test nie wychwytuje mutanta, test jest słaby. Weryfikują jakość samych testów, nie kodu.

### Testy własnościowe / fuzz (Property-Based Tests)

**Co wykrywają:** Naruszenia niezmienników systemu dla losowo generowanych danych wejściowych. Zamiast testować "f(2) == 4", testujesz "f(x) zawsze zwraca wartość ≥ 0 dla dowolnego x". Wykrywają edge case'y, których ręcznie byś nie wymyślił.

### Testy bezpieczeństwa (Security Tests / SAST/DAST)

**Co wykrywają:** Podatności — SQL injection, XSS, CSRF, insecure deserialization, nieprawidłowe uprawnienia. SAST analizuje kod statycznie, DAST atakuje działającą aplikację. Wykrywają problemy, których żaden inny typ testu nie szuka.

### Testy smoke (Smoke Tests)

**Co wykrywają:** Czy system w ogóle startuje i podstawowe przepływy działają — "czy aplikacja się uruchamia, czy endpoint /health odpowiada". Uruchamiane jako pierwsze po deploymencie. Szybka selekcja: jeśli smoke failuje, reszta testów nie ma sensu.

### Testy snapshot (Snapshot Tests)

**Co wykrywają:** Niezamierzone zmiany w wyjściu — porównują obecne wyjście (HTML, JSON, CLI output) z zapisaną "złotą" wersją. Dobre do UI i serializacji, ale generują wiele false positive'ów przy celowych zmianach.

---

## Wzory matematyczne

**Pokrycie kodu (Code Coverage):**

```
CC = (liczba_linii_wykonanych / całkowita_liczba_linii) × 100%
```

CC powyżej 80% to minimalny próg. Uwaga: 100% CC ≠ brak błędów.

**Mutation Score (jakość testów):**

```
MS = (zabite_mutanty / wszystkie_mutanty) × 100%
```

MS poniżej 60% oznacza, że testy są zbyt słabe mimo wysokiego CC.

**Wskaźnik defektów wykrytych wczesnie (Defect Detection Efficiency):**

```
DDE = (błędy_wykryte_przed_produkcją / wszystkie_błędy) × 100%
```

Cel: DDE > 90%. Każdy błąd na produkcji to koszt 10–100× wyższy niż wykrycie w testach.

**Proporcja piramidy (reguła Google):**

```
Unit : Integration : E2E = 70 : 20 : 10
```

Lub dla systemów CLI/offline jak Twoje projekty, gdzie nie ma UI:

```
Unit : Integration : API/Component = 60 : 30 : 10
```

**Czas zwrotu z testów (ROI testu):**

```
ROI = (koszt_błędu_na_prod × prawdopodobieństwo) / koszt_napisania_testu
```

Jeśli ROI > 1, test się opłaca. Dla krytycznej logiki biznesowej ROI jest zawsze >> 1.

**Liczba przypadków testowych dla kombinacji wejść (pairwise testing):**

```
N_pairwise ≈ max_wartości² × log(liczba_parametrów)
```

Zamiast testować wszystkie kombinacje (`k^n`), pairwise redukuje to do `O(k² × log n)` — np. 4 parametry × 3 wartości = 81 kombinacji pełnych, ale tylko ~9 pairwise.

---

## Hierarchia pisania — jak nie podłożyć sobie nogi

Kolejność ma kluczowe znaczenie. Piszesz od dołu piramidy.

**Krok 1 — zanim napiszesz kod produkcyjny:** napisz test jednostkowy dla każdej nowej funkcji (TDD lub minimum test-after). Jeśli nie możesz napisać testu, bo funkcja jest zbyt splątana — to sygnał architektoniczny, że coś jest źle zaprojektowane.

**Krok 2 — przy łączeniu modułów:** test integracyjny dla każdego nowego interfejsu między modułami. Szczególnie dla warstwy danych (SQLite, pliki, JSONL w Twoich narzędziach) — tu najczęściej padają ukryte założenia o formatach.

**Krok 3 — przy publicznym API/CLI:** testy kontraktowe lub API-level. W Twoim ekosystemie CLI (changelog generator, patch editor itd.) — testy wejść/wyjść każdego tool'a jako czarnej skrzynki.

**Krok 4 — po stabilizacji modułu:** smoke test uruchamiany po każdym commicie jako gate w CI/CD.

**Krok 5 — przed releasem:** selektywne E2E dla najważniejszych ścieżek, testy regresji całego zestawu.

**Trzy zasady, które ratują projekty:**

Nigdy nie mockuj tego, co testujesz. Mock ma zastępować zależność zewnętrzną, nie testowaną jednostkę — to najczęstszy błąd, który daje zielone testy przy czerwonym kodzie.

Test musi failować z właściwego powodu. Przed zatwierdzeniem każdego testu — celowo zepsuj kod produkcyjny i sprawdź, czy test rzeczywiście wykrywa błąd. Test, który zawsze jest zielony, jest bezwartościowy.

Testy są pierwszorzędnym kodem. Ten sam standard czystości co kod produkcyjny — bez powtórzeń, czytelne nazwy, jeden assert per scenariusz. Zdegradowane testy to techniczny dług, który rośnie szybciej niż produkcyjny.
