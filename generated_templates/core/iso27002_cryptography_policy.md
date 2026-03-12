---
title: "Polityka Kryptografii (ISO/IEC 27002)"
status: aktywny
aligned: ISO/IEC 27002
---

## Cel dokumentu
Zdefiniować zasady stosowania kryptografii w celu ochrony poufności, integralności i dostępności informacji zgodnie z ISO/IEC 27002:2022 kontrola 8.24 (Use of Cryptography). Polityka określa: dopuszczalne algorytmy kryptograficzne i minimalne długości kluczy, zarządzanie cyklem życia kluczy kryptograficznych, wymagania dotyczące szyfrowania danych w tranzycie i spoczynku, oraz zakaz stosowania przestarzałych algorytmów (MD5, SHA1, DES, RC4, RSA<2048bit).

## Zakres i granice
Polityka obejmuje wszystkie systemy informacyjne, aplikacje, infrastrukturę sieciową i urządzenia końcowe organizacji, które przechowują, przetwarzają lub transmitują dane sklasyfikowane jako Poufne lub wyżej. Dotyczy pracowników, wykonawców i systemów automatycznych.

## Wejścia i wyjścia
**Wejścia:**
- Klasyfikacja danych i inwentarz aktywów informacyjnych
- Analiza ryzyka (wymagania ochrony poufności/integralności)
- Wymagania prawne (RODO Art. 32, dyrektywa NIS2)
- Standardy branżowe (NIST SP 800-57, BSI TR-02102)

**Wyjścia:**
- Zatwierdzona polityka kryptografii
- Rejestr kluczy kryptograficznych i certyfikatów
- Wyjątki od polityki (zatwierdzane przez CISO)

## Dopuszczalne algorytmy kryptograficzne

### Algorytmy symetryczne
| Algorytm | Minimalna długość klucza | Status |
|----------|--------------------------|--------|
| AES | 128-bit (preferowane 256-bit) | Dozwolony |
| ChaCha20-Poly1305 | 256-bit | Dozwolony |
| 3DES | - | Zabroniony |
| DES, RC4, RC2 | - | Zabroniony |

### Algorytmy asymetryczne
| Algorytm | Minimalna długość klucza | Status |
|----------|--------------------------|--------|
| RSA | 2048-bit (preferowane 4096-bit) | Dozwolony |
| ECDSA / ECDH | Krzywa P-256 lub wyższa | Dozwolony |
| EdDSA (Ed25519) | - | Dozwolony |
| DSA | - | Zabroniony |

### Funkcje skrótu (hash)
| Algorytm | Status |
|----------|--------|
| SHA-256, SHA-384, SHA-512 | Dozwolony |
| SHA-3 | Dozwolony |
| SHA-1, MD5 | Zabroniony (w nowych zastosowaniach) |

### Protokoły transmisji
| Protokół | Status |
|----------|--------|
| TLS 1.3 | Wymagany (preferowany) |
| TLS 1.2 | Dozwolony (z ograniczeniami cipher suites) |
| TLS 1.0/1.1, SSL | Zabroniony |

## Zarządzanie kluczami kryptograficznymi

### Cykl życia kluczy
1. **Generowanie:** kryptograficznie bezpieczny generator liczb losowych (CSPRNG), w HSM dla kluczy produkcyjnych
2. **Dystrybucja:** szyfrowane kanały, zakazany plaintext w e-mailach/plikach
3. **Przechowywanie:** HSM, Key Vault (np. HashiCorp Vault, Azure Key Vault) — zakaz plików lokalnych
4. **Rotacja:** AES-256 co 12 miesięcy, TLS co 1 rok, certyfikaty przed wygaśnięciem
5. **Unieważnianie:** natychmiastowe przy podejrzeniu kompromitacji, aktualizacja CRL/OCSP
6. **Zniszczenie:** certyfikowane usunięcie (NIST SP 800-88)

### Certyfikaty X.509
- Wydawane przez: **[Wewnętrzna CA / zewnętrzny CA — DigiCert/Sectigo/Let's Encrypt]**
- Minimalna ważność: **nie dłużej niż 398 dni** (zgodnie z Apple/Chrome policies)
- Monitorowanie wygasania: automatyczne alerty na **[X]** dni przed wygaśnięciem

## Szyfrowanie danych

### Dane w spoczynku (at rest)
- Bazy danych Poufne: AES-256 (Transparent Data Encryption lub column-level)
- Nośniki wymienne: AES-256 (BitLocker/VeraCrypt)
- Backupy: szyfrowanie przed transferem poza organizację

### Dane w tranzycie (in transit)
- Wszystkie połączenia zewnętrzne: TLS 1.2+ (obowiązkowo), TLS 1.3 (preferowane)
- Wewnętrzne API: TLS 1.2+ dla danych Poufnych
- E-mail Poufny: S/MIME lub PGP

## Wyjątki i odstępstwa
Wyjątki od polityki wymagają:
1. Wniosku z uzasadnieniem technicznym/biznesowym
2. Oceny ryzyka przez CISO
3. Zatwierdzenia przez CISO i Zarząd
4. Wpisu do Rejestru Wyjątków z datą przeglądu

## Naruszenia polityki
Naruszenia (np. użycie zakazanych algorytmów, przechowywanie kluczy w plaintext) są traktowane jako incydent bezpieczeństwa informacji i podlegają procedurze ISO/IEC 27035.

## Powiązania (meta)
- standardy-i-compliance: ISO/IEC 27002:2022 kontrola 8.24, NIST SP 800-57, FIPS 140-3, RODO Art. 32
- raci-i-role: CISO (Owner/Approver), Security Architect (Author), wszystkie zespoły IT (Consulted), pracownicy (Informed)
