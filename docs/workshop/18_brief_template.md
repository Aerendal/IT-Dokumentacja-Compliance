# 18 — Brief Template dla Klientów

**Wersja:** 1.0  
**Status:** Draft  
**Cel:** Ustrukturyzowany formularz briefu eliminujący domysły AI — im więcej wypełniono, tym precyzyjniejszy kosztorys.

> **Instrukcja:** Wypełnij sekcje oznaczone `[WYMAGANE]`. Pozostałe są opcjonalne — puste pola system uzupełni wartościami domyślnymi z oznaczeniem `[ZAŁOŻENIE]` w raporcie.

---

## SEKCJA A — Podstawowe informacje `[WYMAGANE]`

### A1. Opis projektu

```
Opisz w kilku zdaniach czego dotyczy projekt:
Co to jest? (np. "system do zarządzania zamówieniami")
Dla kogo? (np. "firma logistyczna, 50 pracowników")
Jaki problem rozwiązuje?

[Wpisz tutaj, minimum 50 słów]
```

### A2. Typ projektu

Zaznacz wszystkie pasujące:

- [ ] Nowa aplikacja / system od zera
- [ ] Rozbudowa istniejącego systemu
- [ ] Migracja (przeniesienie do nowej technologii / chmury)
- [ ] Integracja z zewnętrznymi systemami
- [ ] Audyt / dokumentacja istniejącego systemu
- [ ] Inne: _______________

### A3. Branża / Dziedzina

```
np. logistyka, e-commerce, fintech, healthcare, edukacja, produkcja, inne

[Wpisz tutaj]
```

---

## SEKCJA B — Zakres i wymagania `[WYMAGANE]`

### B1. Co system ma robić?

```
Wymień główne funkcje (przynajmniej 3):
1.
2.
3.
4. (opcjonalnie więcej)
```

### B2. Czego system NIE ma robić?

```
Wyraźne wykluczenia z zakresu pomagają uniknąć błędnych założeń:
np. "Nie obejmuje modułu kadrowego", "Nie integrujemy się z SAP"

[Wpisz tutaj lub wpisz "brak ograniczeń"]
```

### B3. Liczba użytkowników

```
Szacowana liczba użytkowników systemu:
- Równoczesnych (peak): ____
- Łącznie (zarejestrowanych): ____
- Typ: [ ] wewnętrzni pracownicy  [ ] klienci zewnętrzni  [ ] obydwoje
```

---

## SEKCJA C — Technologie i ograniczenia

### C1. Wymagane technologie `[jeśli masz preferencje]`

```
Język programowania:    np. Python, Java, .NET — lub "bez preferencji"
Baza danych:           np. PostgreSQL, MySQL, Oracle — lub "bez preferencji"
Infrastruktura:        np. AWS, Azure, on-premise — lub "bez preferencji"
Frameworki:            np. Django, Spring Boot — lub "bez preferencji"
```

### C2. Istniejące systemy do integracji

```
Podaj nazwy systemów, z którymi nowy musi się komunikować:
np. "ERP: SAP S/4HANA", "CRM: Salesforce", "sklep: Magento"

[Wpisz tutaj lub "brak integracji"]
```

### C3. Regulacje i compliance `[jeśli dotyczy]`

- [ ] RODO / GDPR
- [ ] PCI-DSS (płatności kartą)
- [ ] HIPAA (dane medyczne)
- [ ] KNF / regulacje finansowe
- [ ] ISO 27001
- [ ] Normy branżowe: _______________
- [ ] Brak wymagań compliance

---

## SEKCJA D — Harmonogram i budżet

### D1. Termin

```
Oczekiwana data dostarczenia:  ____________
Deadline twardy (nie można przesunąć)?  [ ] TAK  [ ] NIE
Planowany start:  ____________  lub "jak najszybciej"
```

### D2. Etapy / MVP

```
Czy projekt ma być realizowany etapami?  [ ] TAK  [ ] NIE

Jeśli TAK — co powinno być w pierwszym wydaniu (MVP)?
[Wpisz tutaj]

Co może poczekać na kolejne etapy?
[Wpisz tutaj]
```

### D3. Budżet `[opcjonalne, pomaga dopasować rozwiązanie]`

```
Widełki budżetowe:
[ ] do 10 000 PLN
[ ] 10 000 – 50 000 PLN
[ ] 50 000 – 200 000 PLN
[ ] 200 000 – 500 000 PLN
[ ] powyżej 500 000 PLN
[ ] Wolę nie podawać
```

---

## SEKCJA E — Dokumentacja i proces

### E1. Jakie dokumenty są potrzebne?

```
Zaznacz dokumenty których oczekujesz:
[ ] Specyfikacja wymagań
[ ] Projekt architektury technicznej
[ ] Dokumentacja API (OpenAPI)
[ ] Plan testów
[ ] Instrukcja wdrożenia
[ ] Dokumentacja użytkownika
[ ] Kosztorys i harmonogram
[ ] Inne: _______________
[ ] Zdecydujcie sami co jest potrzebne
```

### E2. Czy masz już jakieś dokumenty?

```
Podaj co już istnieje (np. wireframes, stary system, notatki ze spotkań):
[Wpisz tutaj lub "brak dokumentacji"]
```

### E3. Kto zatwierdza dokumenty?

```
Osoba decyzyjna po stronie klienta:
Imię i rola: _______________
Email: _______________

Czy konieczna jest dodatkowa akceptacja (np. zarząd, dział IT)?  [ ] TAK  [ ] NIE
```

---

## SEKCJA F — Dodatkowe informacje `[opcjonalne]`

### F1. Wzorcowe rozwiązania

```
Czy masz przykłady systemów które Ci się podobają lub chcesz naśladować?
np. "Interfejs jak w Notion", "Logika jak w Jira"

[Wpisz tutaj]
```

### F2. Czego bezwzględnie unikać?

```
Technologie, podejścia, rozwiązania które wykluczasz:
np. "Nie chcemy vendor lock-in", "Bez chmury publicznej", "Tylko open-source"

[Wpisz tutaj]
```

### F3. Inne uwagi

```
Cokolwiek co może być ważne a nie pasuje do powyższych kategorii:
[Wpisz tutaj]
```

---

## Jak system przetworzy ten brief

Po przesłaniu briefu system:

1. **Parsuje** — wykrywa typ projektu, branżę, fazy, ograniczenia
2. **Mapuje** — dopasowuje szablony dokumentów do zakresu briefu  
3. **Klasyfikuje niejasności** — oznacza brakujące dane jako `[ZAŁOŻENIE]` lub pyta o uzupełnienie
4. **Generuje raport** — kosztorys (godziny min/likely/max), lista dokumentów, harmonogram sprintów
5. **Czeka na akceptację** — dopiero po akceptacji rozplanowuje pracę AI szczegółowo

### Jak brief wpływa na precyzję kosztorysu

| Wypełnione sekcje | Precyzja kosztorysu |
|---|---|
| Tylko A (opis) | ±60% — bardzo przybliżony |
| A + B (zakres) | ±40% — przybliżony |
| A + B + C (tech) | ±25% — dobry |
| A + B + C + D (harmonogram) | ±15% — dokładny |
| Wszystkie sekcje | ±10% — bardzo dokładny |

---

*Spec 18 definiuje strukturę wejściową dla BriefParser (spec08) i SemanticMapper (spec09).*  
*Powiązania: `BRIEF_MIN_WORD_COUNT=50` (spec17 §7), disambiguation protocol (spec17 §3).*
