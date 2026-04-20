---
name: fips-audit
description: Scan the current repository for non-FIPS cryptographic usage. Follows AuditFipsCompliance.md. Delegates to the fips-crypto-reviewer subagent. Produces a line-level findings report with OK/WARN/FAIL severity, confidence rating, and remediation hints per disallowed algorithm.
---

# /fips-audit

> **Read [`../SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** A clean scan
> is necessary but not sufficient for FIPS 140-3 validation — validation
> is a CMVP activity for the crypto module, not for your application code.

Scan the current repository for **non-FIPS cryptographic usage** and
produce a findings report against the FIPS 140-3 approved-algorithm list.

## Usage

```
/fips-audit
/fips-audit --scope services/my-subdir/     # v0.2+ monorepo scoping
/fips-audit --strict                        # treat all WARN as FAIL
/fips-audit --lang rust,go                  # limit scan to specific languages
```

## What it does

1. **Load allow/deny lists** from
   [`../data/fips-algorithms.json`](../data/fips-algorithms.json).
2. **Inventory languages** in the repo (Rust `.rs`, Go `.go`, Python
   `.py`, Node `.ts`/`.js`, Java `.java`, etc.).
3. **Scan source files** for detection patterns (per-language patterns
   first, `regex_fallback` otherwise). Excludes `docs/**`, `**/*_test.*`,
   `tests/**`, `fixtures/**` by default.
4. **Check FIPS library presence** in dependency trees
   (`cargo tree -i aws-lc-sys`, `go list -deps -m all`, etc.) when
   tooling is available in the environment.
5. **Locate startup FIPS assertion** — grep for the expected pattern
   per language from
   [`../data/fips-libraries.json`](../data/fips-libraries.json).
6. **Check TLS cipher-suite configuration** — locate TLS config and
   verify allowed suites are all in the `APPROVED` list.
7. **Delegate to `fips-crypto-reviewer` subagent** for line-level
   analysis of each hit (severity, confidence, remediation).
8. **Produce the report** (format in Step 8 of
   [`../workflows/AuditFipsCompliance.md`](../workflows/AuditFipsCompliance.md)).

## Output format

```
=== FIPS 140-3 Audit Report ===
Repository: <path>
Scan date: <ISO-8601>
Scanned languages: rust, go, python

Library check:
  rust: aws-lc-rs #4816 FIPS — PRESENT (Cargo.toml:87 features=["fips"])
  rust: ring — NOT PRESENT (good)
  rust: aws-lc-sys (non-FIPS variant) — NOT PRESENT (good)
  go: native FIPS 140-3 module — PRESENT (go.mod go 1.24)
  python: OpenSSL FIPS provider — UNKNOWN (system-dependent, verify at deploy)

Startup assertion:
  rust: src/main.rs:24 — default_fips_provider().install_default() ✓
  go: cmd/server/main.go:15 — crypto/fips140.Enabled() check ✓
  python: NOT FOUND — no hashlib.get_fips_mode() assertion detected

TLS cipher suite policy:
  src/tls.rs:18: ["TLS_AES_128_GCM_SHA256", "TLS_AES_256_GCM_SHA384"] ✓

Findings:

[FAIL] src/crypto/aead.rs:22
  Pattern: ChaCha20Poly1305
  Algorithm: ChaCha20-Poly1305
  Status: DISALLOWED (not in FIPS 140-3 IG)
  Confidence: AST-high (v0.2+) / regex-medium (v0.1)
  Remediation: Replace with Aes256Gcm from aws-lc-rs. See remediation
               "replace-chacha-with-aes-gcm" in fips-algorithms.json.

[WARN] src/signing/mod.rs:45
  Pattern: Ed25519PrivateKey
  Algorithm: Ed25519
  Status: CONDITIONALLY_APPROVED (FIPS 186-5)
  Confidence: regex-medium
  Condition: Verify your CMVP module's cert lists Ed25519 signature
             generation. Most modules shipped before 2024 do not.

[WARN] go.mod:7
  Pattern: golang.org/x/crypto
  Context: transitive-dependency
  Note: x/crypto contains non-FIPS primitives (chacha20poly1305,
        curve25519). Verify your code does not import the non-FIPS
        sub-packages directly.

[FAIL] src/main.py (no line — file missing)
  Finding: No startup assertion for FIPS mode found.
  Remediation: Add hashlib.get_fips_mode() check at startup.
               See FipsLibraries.md §Python runtime assertion.

Summary:
  FAIL: 2
  WARN: 2
  OK / verified: 3
  Suppressed (docs, tests, fixtures): 0

Overall result: FAIL (non-zero FAIL findings).
```

## Exit semantics

- **`OK`** — zero FAIL findings, startup assertions present, FIPS
  library correctly selected.
- **`WARN-ONLY`** — WARN findings exist (deprecated algorithms,
  conditionally-approved algorithms without module-cert verification).
  Acceptable for active development; not acceptable at audit time.
- **`FAIL`** — at least one FAIL finding. Must be resolved or explicitly
  suppressed with documented reason before proceeding.

With `--strict`, all WARN findings become FAIL.

## Behavioural rules for Claude when running this command

1. **Never fabricate file paths or line numbers.** Every finding must
   have a real `file:line` that `Read` can open.
2. **Never mark a finding as resolved** based on a comment near it.
   Resolution requires code change + re-scan.
3. **When ambiguous**, escalate to WARN and describe the ambiguity;
   do not silently pick FAIL or OK.
4. **Remediation is informational.** Do not auto-apply remediations —
   the user reviews and applies.
5. **If the target library is not detectable** (e.g., no `go.mod` /
   `Cargo.toml`), surface that as a finding — do not assume FIPS mode.

## Limitations (v0.1)

- Detection is regex-based (from
  `data/fips-algorithms.json:detection_patterns`). AST-based detection
  with Tree-sitter is v0.2+.
- Dependency-tree scanning requires local tooling
  (`cargo`, `go`, `openssl`) — if unavailable, those checks are skipped
  and noted in the report.
- `--scope` is v0.2+.
- `--strict` is v0.2+.
- Python startup-assertion detection is string-based; the heuristic is
  imperfect.

## See also

- [`../workflows/AuditFipsCompliance.md`](../workflows/AuditFipsCompliance.md)
  — full procedure this command follows.
- [`../context/FipsAlgorithms.md`](../context/FipsAlgorithms.md)
  — allow/deny lists with citations.
- [`../context/FipsLibraries.md`](../context/FipsLibraries.md)
  — per-language FIPS libraries + build flags.
