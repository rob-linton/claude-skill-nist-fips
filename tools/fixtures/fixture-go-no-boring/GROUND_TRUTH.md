# Ground truth: fixture-go-no-boring

> Human-authored ground truth for the fixture. Not Claude-generated.

## What this fixture represents

A Go program that uses crypto primitives without enabling any FIPS mode
— neither Go 1.24 native FIPS (`GODEBUG=fips140=on`) nor Google's
BoringCrypto fork. Even though `crypto/aes` and `crypto/cipher` contain
only FIPS-approved primitives at the standard level, the module itself
is not CMVP-validated unless one of these FIPS modes is active.

## Expected scanner findings

| Severity | File | Line | Finding | Status | Notes |
|---|---|---|---|---|---|
| FAIL | go.mod | 3 | FIPS mode not enabled | missing-library | No `GODEBUG=fips140=on` in any build / run script; no BoringCrypto toolchain pinned |
| FAIL | main.go | N/A | Startup assertion missing | no-assertion | No `crypto/fips140.Enabled()` or `boring.Enabled()` check |
| OK | main.go | 8 | AES-256-GCM | APPROVED (at standard level) | Primitive is approved but the module it runs through is not in FIPS mode |

## Expected library-check result

| Language | Library | Expected | Present | Result |
|---|---|---|---|---|
| go | native Go FIPS 140-3 (1.24+) with GODEBUG=fips140=on | runtime-enabled | NOT enabled | FAIL |
| go | BoringCrypto fallback | either this or native FIPS | NOT present | — |

## Expected overall severity

**FAIL** — primitives are OK but neither FIPS enablement path is
configured, and no startup assertion exists.

## Sources

- `fips-libraries.json`: Go entries (native FIPS 140-3 + BoringCrypto)
- `FipsLibraries.md` §Go runtime assertion
- Workflow step 6 (AuditFipsCompliance.md): startup-assertion verification
