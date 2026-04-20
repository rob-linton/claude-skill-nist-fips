# Ground truth: fixture-rust-aws-lc-ok

> Human-authored ground truth for the fixture. Not Claude-generated.

## What this fixture represents

A small Rust crate that uses `aws-lc-rs` with the `fips` feature for
AES-256-GCM encryption. This is the recommended v0.1 pattern for FIPS
140-3 coverage in Rust.

## Expected scanner findings

| Severity | File | Line | Algorithm | Status | Notes |
|---|---|---|---|---|---|
| OK | src/lib.rs | 4 | AES-256-GCM | APPROVED | `aws_lc_rs::aead::AES_256_GCM` |
| OK | Cargo.toml | 9 | (dependency) | APPROVED | `aws-lc-rs = { version = "1.6", features = ["fips"] }` |

## Expected library-check result

| Language | Library | Expected | Present | Result |
|---|---|---|---|---|
| rust | aws-lc-rs (FIPS) | present | present with features=["fips"] | OK |
| rust | ring | absent | absent | OK |

## Expected overall severity

**OK** — no FAIL/WARN findings. Example of a clean FIPS-mode Rust crate.

## Sources

- `fips-algorithms.json`: AES-256-GCM entry (status=APPROVED,
  fips_reference="FIPS 197; SP 800-38D")
- `fips-libraries.json`: aws-lc-rs entry (cmvp_certificate=4816)
