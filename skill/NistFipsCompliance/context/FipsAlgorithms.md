# FipsAlgorithms.md

> **Read [`SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** This file references
> the FIPS 140-3 status of cryptographic algorithms. It does **not** certify
> or validate any implementation. Only a CMVP-certified cryptographic module
> is FIPS-validated. Algorithm status changes; always verify against the
> authoritative sources cited below before relying on a claim in a
> compliance deliverable.

Canonical FIPS 140-3 approved / disallowed algorithm reference, grounded in:

- **FIPS 140-3 Implementation Guidance** (IG) — the CMVP's living document,
  `https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-standards`
- **SP 800-131A Rev 3** — Transitioning Cryptographic Algorithms and Key
  Lengths (2024)
- **SP 800-57 Part 1 Rev 5** — Recommendation for Key Management (2020)
- **FIPS 180-4** (SHA), **FIPS 186-5** (digital signatures),
  **FIPS 197** (AES), **FIPS 198-1** (HMAC), **FIPS 202** (SHA-3),
  **FIPS 203** (ML-KEM), **FIPS 204** (ML-DSA), **FIPS 205** (SLH-DSA)

Every entry in this file has a counterpart in
[`../data/fips-algorithms.json`](../data/fips-algorithms.json) with the same
`fips_reference` citation and machine-readable detection patterns. The prose
and the data never disagree; CI enforces this.

---

## Status legend

| Code | Meaning |
|---|---|
| `APPROVED` | Approved for use in FIPS mode under the cited FIPS publication. |
| `CONDITIONALLY_APPROVED` | Approved **only** under specific conditions (e.g., hybrid use, specific key sizes, your CMVP module lists it). |
| `DEPRECATED` | Approved today but scheduled for disallowance. Avoid in new code. |
| `LEGACY_USE_ONLY` | Permitted only for verification of existing material (e.g., SHA-1 for HMAC verification on historical records). Never for new generation. |
| `DISALLOWED` | Not approved. Cannot be used in a FIPS-mode module. |

**"Approved" means approved at the standard level** — you still need a
CMVP-certified module that implements the algorithm. Two different
conformances.

---

## Symmetric encryption

| Algorithm | Status | FIPS reference | Notes |
|---|---|---|---|
| AES-128-GCM | APPROVED | FIPS 197; SP 800-38D | GCM is the preferred AEAD |
| AES-192-GCM | APPROVED | FIPS 197; SP 800-38D | |
| AES-256-GCM | APPROVED | FIPS 197; SP 800-38D | |
| AES-128-CCM / 192 / 256 | APPROVED | FIPS 197; SP 800-38C | |
| AES-128-CTR / 192 / 256 | APPROVED | FIPS 197; SP 800-38A | Unauthenticated — pair with HMAC |
| AES-128-CBC / 192 / 256 | APPROVED | FIPS 197; SP 800-38A | Unauthenticated — pair with HMAC; subject to padding-oracle risks |
| AES-KW / KWP | APPROVED | FIPS 197; SP 800-38F | AES Key Wrap |
| AES-XTS-128 / 256 | APPROVED | FIPS 197; SP 800-38E | Storage encryption only; not for general-purpose data |
| **ChaCha20-Poly1305** | **DISALLOWED** | — | Not in FIPS 140-3 IG approved-algorithms list |
| **XChaCha20-Poly1305** | **DISALLOWED** | — | Same as above |
| **3DES / TDEA** | **DISALLOWED** | SP 800-131A Rev 3 | Disallowed after 2023 |
| **DES** | **DISALLOWED** | — | Never approved in 140-3 |
| **RC4** | **DISALLOWED** | — | Never approved |
| **Blowfish, Twofish, Camellia, SM4** | **DISALLOWED** | — | Not in IG approved list |

---

## Hash functions

| Algorithm | Status | FIPS reference | Notes |
|---|---|---|---|
| SHA-224 | APPROVED | FIPS 180-4 | |
| SHA-256 | APPROVED | FIPS 180-4 | |
| SHA-384 | APPROVED | FIPS 180-4 | |
| SHA-512 | APPROVED | FIPS 180-4 | |
| SHA-512/224 | APPROVED | FIPS 180-4 | |
| SHA-512/256 | APPROVED | FIPS 180-4 | |
| SHA3-224 | APPROVED | FIPS 202 | |
| SHA3-256 | APPROVED | FIPS 202 | |
| SHA3-384 | APPROVED | FIPS 202 | |
| SHA3-512 | APPROVED | FIPS 202 | |
| SHAKE128 / SHAKE256 | APPROVED | FIPS 202 | XOFs |
| **SHA-1 for digital signature generation** | **DISALLOWED** | SP 800-131A Rev 3 | Disallowed after 2013 for generation; disallowed after 2030 even for verification of new material |
| SHA-1 for HMAC | LEGACY_USE_ONLY | SP 800-131A Rev 3 | Legacy verification only; not for new HMAC generation |
| SHA-1 for KDF | LEGACY_USE_ONLY | SP 800-131A Rev 3 | |
| SHA-1 for non-digital-signature (e.g., hash-only integrity tag not serving as signature) | DEPRECATED | SP 800-131A Rev 3 | Strongly avoid |
| **MD5** | **DISALLOWED** | — | Never approved |
| **MD4, MD2, RIPEMD** | **DISALLOWED** | — | Never approved |

---

## Message authentication (MAC)

| Algorithm | Status | FIPS reference | Notes |
|---|---|---|---|
| HMAC-SHA-224 / 256 / 384 / 512 | APPROVED | FIPS 198-1 + FIPS 180-4 | Key size ≥ 112 bits |
| HMAC-SHA3-224 / 256 / 384 / 512 | APPROVED | FIPS 198-1 + FIPS 202 | |
| KMAC128, KMAC256 | APPROVED | SP 800-185 | SHA-3-based KMAC |
| CMAC-AES-128 / 192 / 256 | APPROVED | SP 800-38B | |
| GMAC-AES | APPROVED | SP 800-38D | GCM without ciphertext |
| **HMAC-MD5** | **DISALLOWED** | — | MD5 never approved |
| **HMAC-SHA-1 (new generation)** | **DISALLOWED** | SP 800-131A Rev 3 | Legacy verification only |

---

## Digital signatures

| Algorithm | Status | FIPS reference | Notes |
|---|---|---|---|
| RSA PKCS#1 v1.5, key ≥ 2048 | APPROVED | FIPS 186-5 | 2048/3072/4096 all approved; 15360 for >128-bit security |
| RSA PSS, key ≥ 2048 | APPROVED | FIPS 186-5 | PSS preferred over v1.5 |
| ECDSA on P-256 | APPROVED | FIPS 186-5 | |
| ECDSA on P-384 | APPROVED | FIPS 186-5 | |
| ECDSA on P-521 | APPROVED | FIPS 186-5 | |
| **Ed25519** | **CONDITIONALLY_APPROVED** | FIPS 186-5 (Feb 2023) | Approved at standard level but many CMVP modules shipped before 2024 do not list Ed25519. **Verify your module's current cert.** |
| **Ed448** | **CONDITIONALLY_APPROVED** | FIPS 186-5 (Feb 2023) | Same caveat as Ed25519 |
| ML-DSA-44 / 65 / 87 | APPROVED | FIPS 204 | Module-Lattice DSA (post-quantum) |
| SLH-DSA-SHA2-128s / 128f / 192s / 192f / 256s / 256f | APPROVED | FIPS 205 | Stateless hash-based DSA (post-quantum) |
| SLH-DSA-SHAKE-128s / 128f / 192s / 192f / 256s / 256f | APPROVED | FIPS 205 | |
| **DSA (FIPS 186-4)** | **DISALLOWED** | SP 800-131A Rev 3 | Disallowed for signature generation after 2023 |
| **RSA-1024** | **DISALLOWED** | SP 800-131A Rev 3 | Disallowed after 2013 |
| **ECDSA P-192** | **DISALLOWED** | SP 800-131A Rev 3 | |

---

## Key establishment (KEM / KA)

| Algorithm | Status | FIPS reference | Notes |
|---|---|---|---|
| RSA-OAEP, key ≥ 2048 | APPROVED | FIPS 186-5; SP 800-56B Rev 2 | |
| ECDH on P-256 / P-384 / P-521 | APPROVED | SP 800-56A Rev 3 | |
| DH (finite field) ≥ 2048-bit MODP groups | APPROVED | SP 800-56A Rev 3 | RFC 7919 groups preferred |
| **X25519 (standalone)** | **CONDITIONALLY_APPROVED** | — | Not yet approved as standalone in 140-3 IG D.F/D.G as of 2026-04. Approved when used as part of a hybrid KEM. |
| **X448 (standalone)** | **CONDITIONALLY_APPROVED** | — | Same as X25519 |
| ML-KEM-512 | APPROVED | FIPS 203 | Post-quantum KEM |
| ML-KEM-768 | APPROVED | FIPS 203 | |
| ML-KEM-1024 | APPROVED | FIPS 203 | |
| Hybrid X25519MLKEM768 | APPROVED | FIPS 203 + SP 800-56C | Both halves are approved (X25519 as classical half under SP 800-56C KDF) |
| Hybrid P-256MLKEM768 | APPROVED | FIPS 203 + SP 800-56A | |
| **Kyber (pre-ML-KEM)** | **DISALLOWED** | — | Pre-standardisation; use ML-KEM instead |
| **RSA-1024 OAEP** | **DISALLOWED** | SP 800-131A Rev 3 | Key size too small |

---

## Random bit generation (RBG / DRBG)

| Algorithm | Status | FIPS reference | Notes |
|---|---|---|---|
| CTR_DRBG (AES-128 / 192 / 256) | APPROVED | SP 800-90A Rev 1 | Most common |
| Hash_DRBG (SHA-256 / 384 / 512) | APPROVED | SP 800-90A Rev 1 | |
| HMAC_DRBG (SHA-256 / 384 / 512) | APPROVED | SP 800-90A Rev 1 | |
| **`/dev/urandom` direct use** | **DISALLOWED** | — | Must go through a CMVP-validated DRBG; the module will typically seed its DRBG from the OS entropy source, but application code must call the module's RBG API, not the OS directly |
| **`rand()`, `srand()`** | **DISALLOWED** | — | Not cryptographic |
| **Non-DRBG PRNGs (MT19937, xorshift, etc.)** | **DISALLOWED** | — | Not cryptographic |

---

## Key derivation functions (KDF)

| Algorithm | Status | FIPS reference | Notes |
|---|---|---|---|
| HKDF with approved hash | APPROVED | SP 800-56C Rev 2 | SHA-2 or SHA-3 |
| PBKDF2-HMAC with approved hash | APPROVED | SP 800-132 | Iteration count ≥ 1,000 minimum (NIST); ≥ 600,000 for PBKDF2-HMAC-SHA-256 per OWASP 2023 guidance; use hardware-token-backed KDF where possible |
| KBKDF (SP 800-108) | APPROVED | SP 800-108 Rev 1 | |
| X9.63 KDF | APPROVED | SP 800-56A Rev 3 | |
| SP 800-56C two-step KDF | APPROVED | SP 800-56C Rev 2 | |
| **Scrypt** | **DISALLOWED** | — | Not in FIPS approved-algorithms list |
| **Argon2 (i/d/id)** | **DISALLOWED** | — | Not in FIPS approved-algorithms list; PQC-adjacent discussions ongoing but not approved as of 2026-04 |
| **bcrypt** | **DISALLOWED** | — | Not in FIPS approved-algorithms list |

> The PBKDF2 iteration count floor of 1,000 is the NIST **minimum**; current
> industry practice is much higher (OWASP recommends ≥ 600,000 for
> PBKDF2-HMAC-SHA-256, ≥ 210,000 for PBKDF2-HMAC-SHA-512). Match your
> threat model.

---

## TLS

FIPS-approved cipher suites for TLS 1.2:

- `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
- `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
- `TLS_DHE_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`

FIPS-approved cipher suites for TLS 1.3:

- `TLS_AES_128_GCM_SHA256` — APPROVED
- `TLS_AES_256_GCM_SHA384` — APPROVED
- `TLS_AES_128_CCM_SHA256` — APPROVED
- `TLS_AES_128_CCM_8_SHA256` — APPROVED (truncated tag, constrained-device use)
- **`TLS_CHACHA20_POLY1305_SHA256`** — **DISALLOWED** (ChaCha20 not approved)

Disallowed TLS protocol versions:

- SSLv2, SSLv3 — DISALLOWED
- TLS 1.0, TLS 1.1 — DISALLOWED (SP 800-52 Rev 2, disallowed after 2024)
- Only TLS 1.2 and TLS 1.3 are approved per SP 800-52 Rev 2.

---

## Post-quantum cryptography (PQC)

As of 2026-04, the three finalised PQC FIPS standards are:

| Standard | Name | Use | Approved variants |
|---|---|---|---|
| FIPS 203 | ML-KEM | Key encapsulation | ML-KEM-512, ML-KEM-768, ML-KEM-1024 |
| FIPS 204 | ML-DSA | Digital signatures | ML-DSA-44, ML-DSA-65, ML-DSA-87 |
| FIPS 205 | SLH-DSA | Digital signatures (hash-based) | 12 parameter sets (SHA2 & SHAKE, 128s/f, 192s/f, 256s/f) |

**Transition guidance** (CNSA 2.0 for NSS, NIST for general use):

- Hybrid key establishment (classical + PQC) is the recommended migration
  path for key exchange until fully PQC-only endpoints are prevalent.
- Pure PQC signatures are acceptable today where both endpoints support them.
- **Kyber** (the pre-standardisation candidate) is **disallowed** — use
  ML-KEM; they are not wire-compatible.
- **Dilithium** (pre-standardisation) — use ML-DSA; not wire-compatible.

CMVP validation for ML-KEM, ML-DSA, and SLH-DSA implementations is rolling
out through 2026. Verify your specific module's cert lists the PQC
parameter sets you rely on.

---

## Transition dates (condensed)

| Algorithm / parameter | Disallowed after |
|---|---|
| RSA < 2048 for signatures | 2013 (legacy verify to 2030) |
| SHA-1 for signature generation | 2013 |
| DSA (FIPS 186-4) signature generation | 2023 |
| 3DES / TDEA encryption | 2023 |
| TLS 1.0 / 1.1 | 2024 |
| Two-key TDEA | 2015 (long deprecated) |
| SHA-1 even for legacy verification of new material | 2030 (per SP 800-131A Rev 3) |

Always cross-check current dates against SP 800-131A (latest revision) and
the FIPS 140-3 IG before relying on this table.

---

## Common code-smell detection patterns

These are hints — real scanning lives in `data/fips-algorithms.json` and
the Go hook binary. The patterns below are the quick heuristic version.

| Language | Smell | Likely issue |
|---|---|---|
| Rust | `chacha20poly1305`, `ChaCha20Poly1305` | DISALLOWED AEAD |
| Rust | `XChaCha20` | DISALLOWED AEAD variant |
| Rust | `ring::rand::SystemRandom` | Not FIPS unless `ring` itself is swapped for `aws-lc-rs` |
| Rust | `md5`, `Md5::new()` | DISALLOWED hash |
| Rust | `sha1`, `Sha1::new()` | Suspect; check if it's for signatures |
| Rust | `ed25519_dalek`, `ed25519-compact` | Ed25519 — conditionally approved (module-dependent) |
| Rust | `rust-crypto` (crate) | Unmaintained; almost certainly not FIPS |
| Go | `chacha20poly1305` | DISALLOWED |
| Go | `crypto/md5`, `crypto/sha1` | DISALLOWED / LEGACY_USE_ONLY |
| Go | `crypto/rand` | OK *if* GOFIPS140 is on in Go 1.24+, or if BoringCrypto build |
| Go | `golang.org/x/crypto/chacha20poly1305` | DISALLOWED |
| Python | `hashlib.md5(...)` without `usedforsecurity=False` | DISALLOWED for security-relevant use |
| Python | `Crypto.Cipher.ARC4` / `Crypto.Hash.MD5` | DISALLOWED (pycryptodome often lacks FIPS mode) |
| Python | `cryptography.hazmat.primitives.ciphers.algorithms.ChaCha20` | DISALLOWED |
| Python | `bcrypt`, `scrypt`, `argon2` for PBKDF | DISALLOWED for FIPS (use PBKDF2) |
| Node | `crypto.createCipheriv('chacha20-poly1305', ...)` | DISALLOWED |
| Java | `Cipher.getInstance("ChaCha20/Poly1305/NoPadding")` | DISALLOWED |
| Java | `MessageDigest.getInstance("MD5")` | DISALLOWED for security-relevant use |

---

## How to use this file

- When reviewing a PR that touches cryptography: look up every algorithm
  name in this file, cross-check with `data/fips-algorithms.json`, and
  flag anything that isn't `APPROVED`.
- When designing a new feature: start from the `APPROVED` rows only. Do
  not assume an algorithm is approved just because a well-known library
  offers it (especially relevant for ChaCha20 and Ed25519 in modern Rust
  and Go crypto stacks).
- When responding to a user question "is X FIPS-approved?": quote the
  row from this table, cite the `fips_reference`, and link to
  `data/fips-algorithms.json` for the authoritative machine-readable
  source.
- When in doubt: cite [FIPS 140-3 IG](https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-standards)
  and flag uncertainty to the user rather than guessing.
