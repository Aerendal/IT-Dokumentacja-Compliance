---
title: Data Privacy Checklist
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Data Privacy Checklist


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Lista kontrolna spełnienia wymogów prywatności dla produktu/systemu/feature – do szybkiej walidacji przed release lub audytem.


## Zakres i granice

- Obejmuje: dane i cele, podstawy prawne, notice/zgody, prawa osób (DSAR), rejestry (ROP/DPIA), transfery i umowy (SCC/BCR/DPA), retencję/usuwanie, bezpieczeństwo danych, logi/audyt, szkolenia, waivery i wyjątki.
- Poza zakresem: pełne raporty DPIA/PIA i polityka prywatności (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: opis systemu/feature, modele danych/DFD, kategorie i źródła danych, cele i podstawy prawne, transfery (kraje/podmioty/SCC/BCR), procesorzy i kontrakty, mechanizmy zgód/notice, polityki retencji/bezpieczeństwa, rejestr czynności, ryzyka znane.
- Wyjścia: raport DPIA/PIA (ryzyka i środki), plan działań/mitigacji z ownerami/terminami, decyzja go/conditional/no-go i warunki, aktualizacje rejestru czynności/DPIA log, wymagania kontraktowe/klauzule, log waivers/exception.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Key Documents: records_of_processing, privacy_policy, data_retention_policy, data_classification, security_requirements, vendor_risk_assessment, incident_response_runbook, access_control_policy.
- Document Dependencies: IAM/consent/DSAR narzędzia, DLP, logging/audit, SCC/BCR/DPA, asset/CMDB dla przepływów.
- Key Structures: dane→cel/podstawa→ryzyka→środki→decyzja→rejestry.
## Zależności dokumentu
- Upstream: opis danych/DFD/transferów, podstawy prawne, lista procesorów i umów, polityki retencji/bezpieczeństwa, rejestr czynności.
- Downstream: wdrożenie środków (security/produkt), aktualizacja rejestrów i klauzul, akceptacje/waivery, komunikacja privacy, plany testów bezpieczeństwa.
- Zewnętrzne: procesorzy/dostawcy, organy nadzorcze (w razie konsultacji), przepływy transgraniczne.
## Fazy cyklu życia
- Identyfikacja i opis przetwarzania.
- Ocena ryzyk i środków mitigacji.
- Decyzja (go/conditional/no-go) i wdrożenie środków.
- Przeglądy okresowe lub po zmianie (feature/dane/transfery/incydenty).
## Struktura sekcji (szkielet)
1) Kontekst i zakres DPIA/PIA  
2) Dane i cele (kategorie, źródła, odbiorcy, minimalizacja, retencja)  
3) Podstawy prawne i notice/zgody  
4) Diagramy przepływu i transfery (kraje, podmioty, SCC/BCR, lokalizacja)  
5) Ryzyka dla osób (impact/likelihood, profilowanie/automatyzacja)  
6) Środki techniczne/organizacyjne (minimizacja, retencja, IAM, szyfrowanie, DLP, logi, DSAR, privacy by design)  
7) Plan działań i akceptacje (owner, termin, status; warunki)  
8) Decyzja go/conditional/no-go i warunki/waivery (z sunset)  
9) Raportowanie i rejestry (ROP, DPIA log, kontrakty)  
10) Ryzyka, decyzje, otwarte pytania
## Szybkie powiązania

- user-data-privacy
- student-data-privacy
- simulation-data-privacy
- player-data-privacy
- donor-data-privacy

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **ISO/IEC 27701** — Zarządzanie Informacjami o Prywatności (PIMS)

### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.


## Standardy i compliance


Lista standardów i wymagań regulacyjnych mających zastosowanie do tego dokumentu.
Uzupełnij na podstawie sekcji "Mające zastosowanie standardy i normy" oraz tabeli `doc_standard_mapping`.

- Standard / norma: [kod i nazwa]
- Wymaganie regulacyjne: [kod i treść]
- Polityka wewnętrzna: [nazwa polityki]


## RACI i role


Macierz RACI (Responsible / Accountable / Consulted / Informed) dla działań związanych z tym dokumentem.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie | [rola]      | [rola]      | [rola]    | [rola]   |
| Przegląd  | [rola]      | [rola]      | [rola]    | [rola]   |
| Aktualizacja | [rola]   | [rola]      | [rola]    | [rola]   |
| Archiwizacja | [rola]   | [rola]      | [rola]    | [rola]   |

## Jak używać dokumentu

Wypełniaj każdą sekcję zgodnie z rzeczywistym stanem dokumentowanego systemu lub projektu.
- Sekcje obowiązkowe: Cel dokumentu, Zakres i granice, Wejścia i wyjścia.
- Sekcje oznaczone [opcjonalnie] wypełnij gdy masz dane; wpisz 'Nie dotyczy' jeśli sekcja nie ma zastosowania.
- Po wypełnieniu przekaż do przeglądu zgodnie z macierzą RACI; zaktualizuj metadata (wersja, data, autor).
- Śledź zmiany przez system kontroli wersji; podlinkuj powiązane dokumenty w sekcji 'Szybkie powiązania'.

## Checklisty jakości

### Kompletność
- **Kryterium:** Wszystkie wymagane sekcje i pola są wypełnione
- **Metryka:** Odsetek wypełnionych sekcji do wymaganych
- **Próg OK:** 90%
- **Narzędzie:** template_auditor.py, checklist_atomic.jsonl

### Dokładność
- **Kryterium:** Informacje są poprawne merytorycznie i aktualne
- **Metryka:** Przegląd ekspercki; data ostatniej aktualizacji
- **Próg OK:** Przegląd co 3 mies.
- **Narzędzie:** regulation_updater.py

### Spójność
- **Kryterium:** Terminologia i struktura są spójne w całej bibliotece
- **Metryka:** Liczba niespójności terminologicznych i strukturalnych
- **Próg OK:** 0 niespójności
- **Narzędzie:** bulk_section_patcher.py

### Śledzalność
- **Kryterium:** Każda sekcja ma źródło (standard, regulacja, decyzja)
- **Metryka:** Odsetek sekcji z wypełnionymi standards_refs
- **Próg OK:** 80%
- **Narzędzie:** impact_analyzer.py

### Aktualność
- **Kryterium:** Dokument jest aktualny względem obowiązujących regulacji
- **Metryka:** Czas od ostatniej aktualizacji vs. częstotliwość przeglądów
- **Próg OK:** < 6 mies.
- **Narzędzie:** changelog_tracker.py

### Użyteczność
- **Kryterium:** Użytkownik końcowy może efektywnie wypełnić dokument na podstawie guidance
- **Metryka:** Ocena guidance (score z template_auditor); feedback użytkowników
- **Próg OK:** Score >= 70
- **Narzędzie:** template_auditor.py

## Definicje robocze

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

## Weryfikacja spójności

- [ ] Czy wszystkie ścieżki informacji są zamknięte (każde wejście ma wyjście)?
- [ ] Czy istnieją pętle lub sprzeczne relacje między sekcjami?
- [ ] Czy sekcje kluczowe mają wskazane źródła i odbiorców?
- [ ] Czy terminologia jest spójna z sekcją "Słownik pojęć"?

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane
- Formularz DPIA/PIA, DFD/transfer maps, tabela ryzyk/środków, decyzja/akceptacje, rejestr DPIA/ROP, umowy SCC/BCR/DPA, log waivers, plan wdrożenia środków.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Struktura checklisty (przykładowe sekcje)

1) Dane i cele  
2) Podstawy prawne i notice/zgody  
3) Prawa osób (DSAR) i SLA  
4) Rejestry (ROP, DPIA)  
5) Transfery i umowy (SCC/BCR/DPA)  
6) Retencja i usuwanie/deidentyfikacja  
7) Bezpieczeństwo (IAM, szyfrowanie, DLP, logi, backup/DR)  
8) Logi/audyt i monitoring  
9) Szkolenia/komunikacja  
10) Waivery/wyjątki i kompensacje  


## Przykładowe punkty DoR/DoD (do oznaczenia /N/A)

- [ ] Dane/kategorie i cele zidentyfikowane; podstawa prawna wskazana.  
- [ ] Notice/zgody wdrożone; UI/treści zatwierdzone.  
- [ ] DSAR: proces, narzędzia, SLA/logi działają.  
- [ ] ROP i DPIA aktualne; zmiany odnotowane.  
- [ ] Transfery/podmioty: SCC/BCR/DPA podpisane; lokalizacja danych znana.  
- [ ] Retencja/usuwanie/depers: polityka i implementacja, dowody.  
- [ ] Bezpieczeństwo: IAM, szyfrowanie, DLP, logi, backup/DR; kontrolki testowane.  
- [ ] Logi/audyt dostępne; monitoring KPI/KRI prywatności.  
- [ ] Szkolenia/awareness wykonane; rekordy szkoleń.  
- [ ] Waivery/wyjątki mają sunset i kompensacje.  


## Guidance (skrót)

- Używaj checklisty jako pre-release/audit gate; oznacz N/A z uzasadnieniem.  
- Każdy punkt powinien mieć dowód (link, ticket, dokument); jeśli brak – zapisz action item.  
- Aktualizuj checklistę po zmianach funkcji/danych/transferów i po incydentach.  

