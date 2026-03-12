---
title: "Zakres Systemu Zarządzania Bezpieczeństwem Informacji (ISMS Scope Statement)"
status: aktywny
aligned: ISO/IEC 27001
---

## Cel dokumentu
Zdefiniować i udokumentować zakres Systemu Zarządzania Bezpieczeństwem Informacji (ISMS) jako wymaganie ISO/IEC 27001:2022 klauzula 4.3 (Determining the Scope of the ISMS). Dokument precyzuje: granice organizacyjne ISMS (jednostki, lokalizacje, procesy, systemy, produkty objęte certyfikacją), interfejsy z podmiotami zewnętrznymi, uzasadnienie granic zakresu i odniesienie do kontekstu organizacji (klauzula 4.1) — stanowiąc kluczowy artefakt dla audytora certyfikującego.

## Zakres i granice
Dokument jest obowiązkową informacją udokumentowaną ISMS (klauzula 4.3). Zakres musi być zgodny z wynikami analizy kontekstu organizacji (klauzula 4.1) i potrzebami zainteresowanych stron (klauzula 4.2).

## Wejścia i wyjścia
**Wejścia:**
- Analiza kontekstu organizacji (wewnętrzne i zewnętrzne czynniki)
- Potrzeby i oczekiwania zainteresowanych stron (klauzula 4.2)
- Mapa procesów i systemów informacyjnych
- Inwentarz aktywów informacyjnych
- Wymagania prawne i regulacyjne (RODO, KSC, NIS2)

**Wyjścia:**
- Dokument zakresu ISMS — informacja udokumentowana do rejestru ISMS
- Granice zakresu certyfikacji ISO/IEC 27001
- Lista interfejsów i zależności poza zakresem

## Definicja zakresu ISMS

### Jednostki organizacyjne objęte ISMS
| Jednostka | Lokalizacja | Status |
|-----------|-------------|--------|
| [Dział IT / Security Operations] | [Adres siedziby] | W zakresie |
| [Dział Finansów] | [Adres] | W zakresie |
| [Oddział zagraniczny] | [Kraj] | Poza zakresem / W zakresie |

### Usługi i procesy objęte ISMS
| Usługa/Proces | Opis | Uzasadnienie włączenia |
|--------------|------|----------------------|
| [Usługa/produkt 1] | [Opis] | [Wrażliwość danych / wymaganie klienta] |
| [System IT kluczowy] | [Opis] | [Krytyczność dla ciągłości działania] |

### Systemy informacyjne objęte ISMS
| System | Platforma | Klasyfikacja | Status |
|--------|-----------|--------------|--------|
| [ERP] | [On-premise / Cloud] | [Poufny/Wewnętrzny] | W zakresie |
| [CRM] | [SaaS] | [Poufny] | W zakresie |

### Technologie i lokalizacje
- **Lokalizacje fizyczne:** [Wymienić data center, biura, zdalnych pracowników]
- **Infrastruktura chmurowa:** [AWS/Azure/GCP — regiony, usługi w zakresie]
- **Pracownicy zdalni:** [Tak / Nie — polityka VPN i endpoint]

## Uzasadnienie granic zakresu

### Co jest POZA zakresem ISMS i dlaczego
| Wyłączony element | Uzasadnienie |
|------------------|--------------|
| [Podmiot zależny X] | [Odrębna certyfikacja / brak przetwarzania poufnych danych] |
| [Lokalizacja Y] | [Brak systemów IT / wyłącznie magazyn] |
| [Produkt Z] | [Nieistotny z perspektywy bezpieczeństwa informacji] |

**Uwaga:** wyłączenia muszą być uzasadnione — nie można wyłączać procesów tylko dlatego że są trudne do objęcia ISMS, jeśli mają znaczenie dla bezpieczeństwa informacji organizacji.

## Interfejsy z podmiotami zewnętrznymi
| Podmiot zewnętrzny | Typ relacji | Relevancja dla ISMS |
|-------------------|-------------|---------------------|
| [Dostawca chmury] | Podmiot przetwarzający | Dane Poufne w chmurze — DPA + SLA bezpieczeństwo |
| [Klient instytucjonalny] | Usługobiorca | Wymagania bezpieczeństwa kontraktowe |
| [Zewnętrzne SOC] | Monitorowanie bezpieczeństwa | Dostęp do logów systemów w zakresie |

## Historia wersji zakresu
| Wersja | Data | Zmiana | Zatwierdził |
|--------|------|--------|-------------|
| 1.0 | [Data] | Pierwsza definicja zakresu | [CISO] |
| [X.Y] | [Data] | [Rozszerzenie/zawężenie zakresu] | [CISO] |

## Powiązania (meta)
- standardy-i-compliance: ISO/IEC 27001:2022 klauzula 4.3, ISO/IEC 27001:2022 klauzula 9.2 (zakres audytu)
- raci-i-role: CISO (Owner), Zarząd (Approver), Team Leader IT (Consulted), jednostki objęte zakresem (Informed)
