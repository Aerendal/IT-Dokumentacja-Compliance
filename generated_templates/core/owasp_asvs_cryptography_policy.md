---
title: "Cryptography Policy (App Level)"
status: aktywny
aligned: OWASP ASVS
---

## Cel dokumentu
Zdefiniować wymagania kryptograficzne na poziomie aplikacji zgodnie z OWASP Application Security Verification Standard (ASVS) V6 — Cryptography (Level 1-3). Polityka określa: dopuszczalne algorytmy kryptograficzne w aplikacjach (nie na poziomie infrastruktury), wymagania bezpiecznego generowania liczb losowych, zarządzanie sekretami aplikacyjnymi (API keys, tokeny, hasła), ochronę danych wrażliwych w kodzie oraz zakaz stosowania przestarzałej kryptografii — stanowiąc implementation checklist dla deweloperów przy weryfikacji ASVS.

## Zakres i granice
Polityka obejmuje wszystkie aplikacje webowe, mobilne i API podlegające weryfikacji ASVS. Dotyczy kodu aplikacji (nie warstwy infrastruktury — tę obejmuje ISO/IEC 27002 Cryptography Policy).

## Wejścia i wyjścia
**Wejścia:**
- OWASP ASVS V6 Cryptography Requirements (poziom weryfikacji L1/L2/L3)
- Data Classification — jakie dane aplikacja przetwarza
- Threat Model aplikacji
- Security testing results (DAST/SAST)

**Wyjścia:**
- Wymagania kryptograficzne aplikacji — wejście do Security Design Review
- Checklist ASVS V6 do weryfikacji przez QA/pentest
- Dowody spełnienia wymagań dla audytora ASVS

## Wymagania ASVS V6 — Kryptografia aplikacji

### V6.1 — Klasyfikacja danych
| Wymaganie | Poziom | Wymaganie |
|-----------|--------|-----------|
| V6.1.1 | L1 | Wrażliwe dane osobowe (PII) NIE są przechowywane w logach/diagnostics |
| V6.1.2 | L2 | Klucze prywatne i sekrety NIE są hardcoded w kodzie |
| V6.1.3 | L2 | Hasła NIE są przechowywane w systemach zarządzania konfiguracją w plaintext |

### V6.2 — Algorytmy
| Wymaganie | Poziom | Opis |
|-----------|--------|------|
| V6.2.1 | L1 | Aplikacja NIE używa MD4, MD5, SHA1, DES, 3DES, RC4 w nowych funkcjonalnościach |
| V6.2.2 | L1 | Moduły losowe używają CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) |
| V6.2.3 | L2 | Szyfrowanie asymetryczne: RSA min. 2048-bit lub ECDSA/ECDH min. P-256 |
| V6.2.4 | L2 | Szyfrowanie symetryczne: AES-128 minimum (preferowane AES-256) |
| V6.2.5 | L2 | Tryby szyfrowania: GCM/CCM/SIV (authenticated encryption) — zakaz ECB, CBC bez MAC |
| V6.2.6 | L3 | Post-quantum safe algorytmy dla danych wrażliwych (kiedy dostępne) |

### V6.3 — Wartości losowe
| Wymaganie | Poziom | Opis |
|-----------|--------|------|
| V6.3.1 | L1 | Generowanie tokenów, CSRF tokens, session IDs używa CSPRNG (nie Math.random) |
| V6.3.2 | L2 | GUID/UUID generowane z CSPRNG (UUID v4) — nie przewidywalne pseudo-random |
| V6.3.3 | L2 | Seed dla PRNG jest odpowiednio losowy i nieprzewidywalny |

### V6.4 — Zarządzanie sekretami aplikacji
| Wymaganie | Poziom | Opis |
|-----------|--------|------|
| V6.4.1 | L2 | Sekrety (API keys, passwords, tokens) są przechowywane w Secret Manager (Vault/AWS Secrets Manager/Azure Key Vault) |
| V6.4.2 | L2 | Sekrety NIE są commitowane do repozytorium kodu (pre-commit hooks, git-secrets) |
| V6.4.3 | L2 | Sekrety mają skonfigurowaną rotację (manual lub automatyczną) |
| V6.4.4 | L3 | Sekrety aplikacji w produkcji są injectowane przez environment variables lub mounted secrets — nie przez pliki konfiguracyjne |

### V6.5 — Walidacja kryptografii
| Wymaganie | Poziom | Opis |
|-----------|--------|------|
| V6.5.1 | L1 | Podpisy cyfrowe i MAC są weryfikowane przed użyciem danych |
| V6.5.2 | L2 | Certyfikaty TLS klientów/serwerów są walidowane (CN, SANs, expiry, revocation) |
| V6.5.3 | L2 | Błędy kryptograficzne NIE ujawniają szczegółów implementacji w odpowiedziach |

## Implementacja w popularnych stack'ach

### JavaScript/TypeScript (Node.js)
```javascript
// OK: Poprawne — CSPRNG
const crypto = require('crypto');
const token = crypto.randomBytes(32).toString('hex');

// ZLE: Niepoprawne — przewidywalne
const token = Math.random().toString(36);
```

### Java
```java
// OK: Poprawne — SecureRandom
SecureRandom random = new SecureRandom();
byte[] token = new byte[32];
random.nextBytes(token);

// OK: AES-GCM
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
```

### Python
```python
# Cryptography Policy (App Level)
import secrets
token = secrets.token_hex(32)  # CSPRNG

# OK: AES-GCM z cryptography library
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
```

## Weryfikacja zgodności
Checklist ASVS V6 jest weryfikowany podczas:
- Security Design Review (przed implementacją)
- Code Review (checklist dla PR z kryptografią)
- Penetration Test (ASVS Level 1-3 scope)
- Pre-release Security Gate

## Powiązania (meta)
- standardy-i-compliance: OWASP ASVS 4.0 V6 Cryptography, OWASP MASVS MSTG-CRYPTO-1 to MSTG-CRYPTO-6, NIST SP 800-57
- raci-i-role: Security Architect (Owner), Deweloperzy (Responsible), QA/Pentest (Reviewer), CISO (Approver)
