# Macierz pokrycia — pliki W_x

Zamiast checkboxów w poszczególnych plikach, ta macierz pokazuje które sekcje i tematy są pokryte
w których warstwach. Plik W_x pozostają **dokumentami projektowymi** (nie task-listami).

> **Zasada:** jeśli temat pojawia się we wszystkich warstwach → oznaczony `✓ (wszystkie)`.
> Jeśli tylko w niektórych → wskazane gdzie brakuje. Praca naprawcza opisana w ostatniej kolumnie.

---

## 1. Pokrycie obowiązkowych sekcji

| Sekcja | W0 | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | Status |
|--------|----|----|----|----|----|----|----|----|-----|--------|
| Przegląd | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| Diagram przepływu danych | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| Pytania źródłowe — sklasyfikowane | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| Pytania uzupełniające | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| Kryteria akceptacji | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| Pytania o idempotentność | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| Pytania o migrację i wersjonowanie | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| Pytania o audytowalność | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| **Rozszerzalność i skalowanie** | ✓* | ✓ | ✓ | ✓ | ✓ | ✓ | ✓* | ✓ | ✓ | ✓ wszystkie (*dodane 2026-03) |
| **Uzasadnienie istnienia warstwy** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie (dodano 2026-03) |
| **Luki cross-warstwowe** | — | ✓ | ✓ | — | — | ✓ | — | — | — | Tylko gdzie znaleziono luki |
| **7 podsekcji technicznych** (Arch/Kontrakty/…/Pułapki) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie |
| **Hierarchia TDD sec.4** (RED→GREEN→REFACTOR→E2E) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ wszystkie (dodano 2026-03) |

_* — sekcja dodana ręcznie w tej sesji, wcześniej brakowało_

---

## 2. Liczba pytań per warstwa

| Warstwa | Pytania (?) | Polecenia | Łącznie | Proporcja pytań |
|---------|-------------|-----------|---------|-----------------|
| W0 — doc audit | 71 | 44 | 115 | 62% |
| W1 — fundamenty NLP | 190 | 108 | 298 | 64% |
| W2 — role semantyczne | 100 | 52 | 152 | 66% |
| W3 — zasoby leksykalne | 111 | 56 | 167 | 66% |
| W4 — baza grafowa | 106 | 58 | 164 | 65% |
| W5 — silnik wnioskowania | 134 | 55 | 189 | 71% |
| W6 — koreferencja | 74 | 41 | 115 | 64% |
| W7 — API/integracja | 74 | 33 | 107 | 69% |
| W8 — compliance/audit | 92 | 70 | 162 | 57% |
| **SUMA** | **952** | **517** | **1469** | **~65%** |

> Liczby aktualne po: dodaniu sekcji Uzasadnienie, hiearchii TDD w sec.4, przesunięciu GREEN commands, wymianie przykładów off-domain (commit 6a538a9, 2026-03-15).
> W7 i W6 mają 107/115 pozycji — kandydaci do uzupełnienia przy implementacji tych warstw.

---

## 3. Pokrycie tematów przekrojowych (cross-cutting concerns)

Tematy które z natury powinny być omówione w **każdej** warstwie:

| Temat | Pokrycie | Uwagi |
|-------|----------|-------|
| Fallback / degraded mode | W1 ✓, W2 ✓, W5 ✓ | W6, W7 — nie opisano co się dzieje gdy warstwa wyżej nie odpowiada |
| Circuit breaker / timeout | W7 ✓ | Tylko W7 (API). Wewnętrzne warstwy nie omawiają |
| Structured logging (JSON) | W7 ✓, W8 ✓ | W1–W6 — zakłada się log, ale format nie jest opisany |
| Health check / liveness | W7 ✓ | Pozostałe warstwy nie opisują endpointów health |
| Metryki Prometheus | W7 ✓, W8 ✓ | W1–W6 — brak opisu jakie metryki eksportować |
| Contract test (Pact/schemata) | W1 ✓, W2 ✓ | W3–W6 — kontrakty opisane, ale brak pytań o automatyczne testy kontraktów |
| Blue/green deployment | — | Żadna warstwa nie omawia strategii wdrożeń bez downtime |
| Chaos testing | — | Żadna warstwa nie omawia odporności na awarie sąsiednich usług |

---

## 4. Luki cross-warstwowe — status ADR

Szczegóły w `INDEX.md` → sekcja ADR. Tu tylko status rozwiązania:

| ADR | Pytanie | Status |
|-----|---------|--------|
| ADR-01 | Pipeline: W3 przed W2 czy wewnątrz W2? | ⚠️ NIEROZSTRZYGNIĘTE |
| ADR-02 | Pipeline: W6 przed W2 czy po W2? | ⚠️ NIEROZSTRZYGNIĘTE |
| ADR-03 | W5 ← W3: callback/hot-reload/polling? | ⚠️ NIEROZSTRZYGNIĘTE |
| ADR-04 | W0 ← W1: ILemmatizer interface? | ⚠️ NIEROZSTRZYGNIĘTE |
| ADR-05 | W1 fallback parser: sync czy async? | ⚠️ NIEROZSTRZYGNIĘTE |

> Każde NIEROZSTRZYGNIĘTE ADR to blokada implementacji warstw których dotyczy.
> Przed rozpoczęciem kodowania danej warstwy odpowiednie ADR muszą mieć status `✅ PODJĘTE`.

---

## 5. Tematy wymagające rozbudowy (kandydaci do nowych pytań)

Tematy zidentyfikowane jako słabo pokryte na podstawie przeglądu wszystkich plików:

| Temat | Brakuje w | Priorytet |
|-------|-----------|-----------|
| Zero-anafora i elipsa | W6 | Wysoki — dotyczy języka polskiego |
| Named Entity Recognition (NER) integracja | W2, W3 | Wysoki — NER zasila role semantyczne |
| Obsługa wielojęzyczności (EN fallback gdy PL brak) | W0, W1 | Średni |
| GDPR / przetwarzanie danych osobowych | W8 | Wysoki (projekt zarobkowy) |
| Rate limiting / quota na API | W7 | Średni |
| Dokumentacja OpenAPI/Swagger auto-generowanie | W7 | Niski |
| Retry policy (exponential backoff) dla zewnętrznych zasobów | W3, W4 | Średni |
| Cache invalidation strategy (TTL vs event-driven) | W3, W4, W5 | Wysoki |
| Semantic versioning kontraktów danych | W1, W2 | Wysoki |

---

## 6a. Luki w pytaniach źródłowych — wynik klasyfikacji

Każde źródłowe pytanie sklasyfikowane do jednej z 7 kategorii. Poniżej: liczba pytań źródłowych per warstwa/kategoria.
Wartości **pogrubione** = luka (<5 pytań, wymaga uzupełnienia w "Pytania uzupełniające").

| Kategoria | W0 | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | Suma |
|-----------|----|----|----|----|----|----|----|----|-----|------|
| 1. Architektura | **1** | 9 | **3** | **2** | 10 | **2** | **1** | **2** | 5 | 35 |
| 2. Kontrakty danych | **0** | 12 | **0** | **0** | 7 | **0** | **0** | **0** | **1** | 20 |
| 3. Implementacja | 17 | 103 | 40 | 39 | 43 | 79 | 17 | 7 | 39 | 384 |
| 4. Testowanie | 19 | 48 | 14 | 12 | 7 | 7 | 8 | **3** | 12 | 130 |
| 5. Obsługa błędów | **0** | **3** | **2** | **1** | **0** | **1** | **2** | **0** | **4** | 13 |
| 6. Integracja | 5 | 16 | **3** | 15 | 12 | 5 | 8 | 12 | 6 | 82 |
| 7. Pułapki i ryzyka | **0** | 12 | **0** | **0** | **0** | **0** | **0** | **0** | **0** | 12 |
| **Suma** | 42 | 203 | 62 | 69 | 79 | 94 | 36 | 24 | 67 | **676** |

> Sekcja "Pytania uzupełniające" w każdym pliku ma już pełne 7 podsekcji.
> Powyższe luki dotyczą **pytań źródłowych** — wskazują gdzie sesje pracy skupiały się tylko na implementacji.

**Wnioski:**
- Kategoria 3 (Implementacja) dominuje wszędzie — ~57% wszystkich pytań źródłowych to "Pokaż/Zaimplementuj X"
- Kategoria 5 (Obsługa błędów) jest systematycznie pominięta — tylko 13 pytań w całym zbiorze
- Kategoria 7 (Pułapki) — 12 z nich jest tylko w W1; inne warstwy nie pytały o ryzyka
- Kategoria 2 (Kontrakty danych) — tylko W1 i W4 mają pytania kontraktowe w źródłach

## 6. Jak używać tej macierzy

1. **Przed implementacją warstwy** — sprawdź sekcję 4 (ADR) czy blokujące decyzje są podjęte
2. **Podczas code review** — sprawdź sekcję 3 (cross-cutting) czy dana warstwa opisuje swoje zachowanie
3. **Przed zamknięciem fazy** — sprawdź sekcję 5 (kandydaci do rozbudowy) dla danej warstwy
4. **Aktualizacja macierzy** — po uzupełnieniu pytań w W_x, zaznacz ✓ w odpowiedniej komórce tabeli 1

> **Nie** dodawaj checkboxów do plików W_x — one są dokumentami projektowymi, nie task-listami.
> Status implementacji śledź w `IMPLEMENTATION_STATUS.md` (do stworzenia gdy ruszy kodowanie).
