# workflows/AuditFipsCompliance.md

> **Read [`../SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** This workflow
> scans a codebase for non-FIPS crypto. A clean scan is necessary but not
> sufficient for FIPS 140-3 validation — validation is a CMVP activity
> for the crypto module, not for your application code.

## When to use this workflow

Use this when:

- You are preparing for an audit or assessment and want to find any
  non-FIPS crypto before the assessor does.
- You are reviewing a PR that touches `crypto`, `tls`, `kms`, `auth`,
  `password`, `jwt`, `hash`, `random`, `sign`, or `encrypt`.
- You are onboarding a new codebase and want a baseline FIPS audit
  before committing to a compliance matrix.

Do **not** rely on this as a substitute for:

- Loading a CMVP-validated cryptographic module.
- Asserting FIPS mode on application startup.
- Verifying CMVP certificate validity at audit time.

---

## Procedure

### Step 1 — Inventory the languages and runtimes

For each language in the target repo:

- Note whether the language has a FIPS-validated module option (see
  [`../context/FipsLibraries.md`](../context/FipsLibraries.md)).
- Note the *expected* library for that language (e.g., Rust → aws-lc-rs;
  Go 1.24+ → native FIPS).

### Step 2 — Read the allow/deny lists

- [`../context/FipsAlgorithms.md`](../context/FipsAlgorithms.md) — human-
  readable approved / disallowed lists.
- [`../data/fips-algorithms.json`](../data/fips-algorithms.json) — machine-
  readable, with per-language regex detection patterns.

### Step 3 — Scan for disallowed algorithm usage

For each entry in `fips-algorithms.json` with `status: DISALLOWED` or
`LEGACY_USE_ONLY`:

1. Take the language-specific detection pattern, or fall back to
   `regex_fallback`.
2. Grep the repository (respecting `exclude` globs — `docs/**`,
   `**/*_test.*`, `tests/**`, `fixtures/**`).
3. For each hit, record: file path, line number, matched pattern,
   disallowed algorithm name, severity, remediation ID.

For v0.1 (no hooks yet), Claude uses `Grep` tool directly. In v0.2 the
Go hook binary does this automatically on every pre-edit.

**Severity assignment**:

- `FAIL` (high confidence) — AST-based match (v0.2+) or unambiguous
  regex hit in `.rs` / `.go` / `.py` / `.ts` / `.java` source file.
- `WARN` (medium confidence) — regex hit but could be a string literal,
  comment, or variable name (heuristic).
- `INFO` — match in documentation or test fixture; likely benign.

### Step 4 — Verify the FIPS-validated library is actually in use

Language-specific verifications:

**Rust**:

```bash
# Must show only FIPS variant; if both aws-lc-sys and aws-lc-fips-sys
# appear, there are two crypto stacks.
cargo tree -i aws-lc-sys
cargo tree -i aws-lc-fips-sys

# No 'ring' in the tree
cargo tree -i ring
```

Expected: `aws-lc-fips-sys` present; `aws-lc-sys` **not** present as a
separate entry; `ring` not present at all.

**Go (1.24+)**:

```bash
go version -m <path-to-binary> | grep -E 'fips|BoringCrypto'
```

Expected: the binary reports FIPS-enabled.

Check runtime:

```bash
GODEBUG=fips140=on go run ./cmd/your-binary  # should not error
```

**Python**:

```bash
openssl list -providers  # should list 'fips'
python3 -c "import hashlib; print(hashlib.get_fips_mode())"
# Should print 1 on a FIPS-enabled RHEL 9 / Ubuntu Pro FIPS system.
```

### Step 5 — Verify TLS cipher-suite policy

Locate TLS configuration (rustls, Go `crypto/tls`, Python `ssl`, Node
`tls`, Java JCA).

Check that the allowed cipher suites are all in the `APPROVED` list in
`FipsAlgorithms.md §TLS`:

- TLS 1.3: `TLS_AES_128_GCM_SHA256`, `TLS_AES_256_GCM_SHA384` ✓
- Disallow: `TLS_CHACHA20_POLY1305_SHA256`
- TLS 1.2: `ECDHE-ECDSA-AES128-GCM-SHA256`, `ECDHE-ECDSA-AES256-GCM-SHA384`, `ECDHE-RSA-AES128-GCM-SHA256`, `ECDHE-RSA-AES256-GCM-SHA384` ✓
- Disallow everything below TLS 1.2.

### Step 6 — Verify startup FIPS-mode assertion

Locate the application startup code and confirm a FIPS-mode assertion
fires. Example patterns (from `data/fips-libraries.json`):

| Language | Pattern |
|---|---|
| Rust (rustls) | `rustls::crypto::default_fips_provider().install_default()` + `assert!(config.fips())` |
| Go | Check `crypto/fips140.Enabled()` (Go 1.24+) or `boring.Enabled()` |
| Python | `hashlib.get_fips_mode()` returns 1 |
| Node.js | `crypto.getFips()` returns 1 |
| Java (BC-FIPS) | `CryptoServicesRegistrar.isInApprovedOnlyMode()` returns true |

**If no startup assertion exists**, open a finding:

```
SEVERITY: FAIL
CONTROL: SC-13(2) - FIPS-Validated Cryptography
FINDING: Application does not assert FIPS mode at startup. Could be
         running in non-FIPS mode in production without detection.
REMEDIATION: Add startup assertion per FipsLibraries.md §Runtime assertion.
```

### Step 7 — Verify KMS / key lifecycle

Orthogonal to algorithm allow-list: verify that keys are managed properly
(SC-12, SC-12(3)):

- Keys generated via validated DRBG? (grep for `rand` usage vs.
  `aws_lc_rs::rand::SystemRandom` etc.)
- Envelope encryption used for at-rest? (data DEK wrapped by KMS KEK)
- Rotation mechanism present? (SC-12)
- Plaintext keys zeroised after use? (SC-28(1))

### Step 8 — Produce the report

Report structure:

```
=== FIPS 140-3 Audit Report ===
Repository: <path>
Target baseline: <fedramp-moderate|fedramp-high|...>
Audit date: <ISO-8601>

Summary:
- FIPS library in use: <aws-lc-rs #4816 | native Go FIPS | OpenSSL FIPS #4282>
- Startup assertion present: YES / NO
- Disallowed algorithms found: <count>
- Deprecated algorithms found: <count>
- Legacy-use-only algorithms found: <count>

Findings:

[FAIL] SC-13(2) - FIPS-Validated Cryptography
  File: src/crypto/aead.rs:22
  Pattern: ChaCha20Poly1305
  Algorithm: ChaCha20-Poly1305
  Status: DISALLOWED (not in FIPS 140-3 IG approved list)
  Remediation: Replace with Aes256Gcm from aws-lc-rs.
  Confidence: AST-high

[WARN] AU-10 - Non-Repudiation
  File: src/signing/mod.rs:45
  Pattern: Ed25519
  Algorithm: Ed25519
  Status: CONDITIONALLY_APPROVED (FIPS 186-5)
  Condition: Verify CMVP certificate of your module lists Ed25519.
  Confidence: regex-medium

[INFO] AU-3 - Documentation reference
  File: docs/architecture.md:88
  Pattern: "md5"
  Status: excluded (docs/** glob)
  Confidence: suppressed
```

Pass criteria (for a green audit):

- Zero `FAIL` findings.
- All `WARN` findings either have a suppression reason or are being
  tracked as PARTIAL/POAM entries in the matrix.
- Startup assertion present.
- FIPS library correctly selected per language.

Fail criteria: any `FAIL` finding, a missing startup assertion, or a
non-FIPS library in the dependency tree.

---

## Common false positives and how to handle them

| Pattern | Context where it's OK | Suppression |
|---|---|---|
| `md5` in `Cargo.lock` as a transitive of a non-crypto crate | Library uses MD5 for cache-busting, not security | Inline `// fips:ignore reason="cache only"` or repo-level exception |
| `sha1` in git-related tooling | Git uses SHA-1 for object hashing, not security | Same |
| `chacha20` in a test fixture verifying the scanner works | Test fixture | `tests/**` already excluded by default |
| `ed25519` in SSH key parsing library | Verifying existing SSH keys, not issuing new ones | Inline suppression with `reason="ssh key verification, legacy compatibility"` |
| `3des` string in documentation explaining what's disallowed | Documentation | `docs/**` excluded by default |

Always document the suppression reason — "why" matters when an assessor
reads the exception.

---

## Feeding the `/fips-audit` command

The command is a thin shell around this workflow. It:

1. Invokes the `fips-crypto-reviewer` subagent.
2. Agent follows this workflow.
3. Agent returns a structured report (same shape as Step 8 above).
4. Command renders the report as Markdown.

In v0.2+ the Go hook binary performs Steps 1–3 on every pre-edit, so
this whole-repo audit becomes an on-demand verification rather than a
scheduled chore.

---

## Limitations (be honest)

- **AST-based detection** is v0.2+. In v0.1, detection is regex-based
  with all the false-positive risk that entails.
- **Dependency-tree scanning** (detecting non-FIPS crypto in
  transitives) is v0.2+. In v0.1 you must manually run `cargo tree` etc.
- **CMVP cert freshness check** is a manual step — the build tool warns
  if any cert's `verified_on` date is older than 90 days, but does not
  re-verify against the CMVP website.
- **Go native FIPS cert number** is pending CMVP submission as of
  2026-04. Track this and update `fips-libraries.json` when issued.
