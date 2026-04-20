# Ground truth: fixture-rust-chacha20

> Human-authored ground truth for the fixture. Not Claude-generated.
> Source citations are at the bottom.

## What this fixture represents

A small Rust crate that uses `chacha20poly1305` as its AEAD. This is a
common pattern in Rust because `chacha20poly1305` is a well-known
RustCrypto crate — but it is **not** FIPS-approved under FIPS 140-3
Implementation Guidance.

## Expected scanner findings

| Severity | File | Line | Algorithm | Status | Notes |
|---|---|---|---|---|---|
| FAIL | src/lib.rs | 4 | ChaCha20-Poly1305 | DISALLOWED | `use chacha20poly1305::ChaCha20Poly1305;` |
| FAIL | src/lib.rs | 11 | ChaCha20-Poly1305 | DISALLOWED | `ChaCha20Poly1305::new(...)` call site |
| FAIL | Cargo.toml | 9 | (dependency) | DISALLOWED | `chacha20poly1305 = "0.10"` dependency |

## Expected library-check result

| Language | Library | Expected | Present | Result |
|---|---|---|---|---|
| rust | aws-lc-rs (FIPS) | present | ABSENT | FAIL |
| rust | ring | absent | absent | ok |

## Expected overall severity

**FAIL** — at least one FAIL finding, and the required FIPS library is
not in the dependency tree.

## Sources

- `fips-algorithms.json`: ChaCha20-Poly1305 entry (status=DISALLOWED,
  fips_reference="not in FIPS 140-3 IG approved list")
- `fips-libraries.json`: Rust entry (primary-crypto-primitives =
  `aws-lc-rs` #4816)
- `FipsAlgorithms.md` §Symmetric encryption (ChaCha20 row)
