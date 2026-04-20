# FipsLibraries.md

> **Read [`SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** CMVP certificate
> numbers are facts about *specific modules at specific versions*. They can
> expire, be revoked, or be superseded. Always verify the current status
> against the
> [CMVP validated modules list](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules)
> before relying on a cert claim in a compliance deliverable. The
> machine-readable data behind this file is in
> [`../data/fips-libraries.json`](../data/fips-libraries.json) with a
> `verified_on` date.

Per-language guidance on **which cryptographic library to adopt to obtain
FIPS 140-3 coverage**, how to build or configure it, and the common
gotchas.

---

## Meta: what "FIPS coverage" means for application code

FIPS 140-3 validation applies to a **cryptographic module** — a specific
software + configuration + platform combination. For application code, this
means three things must be true simultaneously:

1. You are *using* a cryptographic module that is on the CMVP validated
   list.
2. That module is *in its FIPS-approved mode of operation* (many modules
   have both FIPS and non-FIPS modes; you must explicitly enable FIPS).
3. Every crypto call in your application routes through the validated
   module — not a different library your dependency graph pulled in.

Item (3) is the most commonly missed. It is the source of "duplicate
crate", "duplicate jar", "duplicate wheel" bugs where a transitive
dependency pulls in a non-FIPS crypto path.

---

## Rust

### Primary recommendation

| Role | Library | CMVP cert | Build flag |
|---|---|---|---|
| Core primitives (AES, SHA, HMAC, RSA, ECDSA, PBKDF2, RBG) | [`aws-lc-rs`](https://github.com/aws/aws-lc-rs) | #4816 (AWS-LC FIPS) | `--features fips` |
| TLS stack | [`rustls`](https://github.com/rustls/rustls) | (inherits via aws-lc backend) | `--features fips` + use the FIPS crypto provider |

### Build / runtime assertions

```rust
use rustls::crypto::{CryptoProvider, default_fips_provider};

fn main() {
    // Install the FIPS-mode crypto provider as the process default.
    default_fips_provider()
        .install_default()
        .expect("failed to install FIPS provider");

    // When building a rustls ClientConfig or ServerConfig, assert FIPS.
    let config = /* build your config */ unimplemented!();
    assert!(config.fips(), "TLS config is not in FIPS mode");
}
```

### Gotchas

- **Linux only**. `aws-lc-rs` FIPS builds on Linux x86_64 and aarch64. macOS
  and Windows are not FIPS targets for this crate. Develop on Linux or use
  Docker.
- **GCC 14 breaks `aws-lc-fips-sys`**. Pin to GCC 13 or use Clang. GCC 15
  status unknown — retest at upgrade time.
- **Duplicate crates trap**. Run `cargo tree -i aws-lc-sys` and confirm
  only the FIPS variant appears. If you see both `aws-lc-sys` and
  `aws-lc-fips-sys`, or a transitive `ring`, you have two cryptographic
  stacks — one of which is not FIPS.
- **Don't use `ring` directly**. `ring` is not FIPS-validated as of
  2026-04. Many older Rust crypto crates transitively pull it in.
- **`rand` crate**. The default `rand` crate uses OS entropy (e.g.,
  `getrandom`). For FIPS-mode code, use `aws_lc_rs::rand::SystemRandom`
  which routes through the validated DRBG.

### Common anti-patterns

```rust
// BAD: ChaCha20-Poly1305 is not FIPS-approved.
use chacha20poly1305::{ChaCha20Poly1305, Key, Nonce};

// BAD: `ring` is not FIPS-validated.
use ring::aead;

// GOOD: aws-lc-rs AES-GCM.
use aws_lc_rs::aead::{Aad, LessSafeKey, UnboundKey, AES_256_GCM};
```

### CMVP cert verification

Current AWS-LC FIPS certificate is **#4816**. Verify at
https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules
before citing in an SSP.

---

## Go

### Primary recommendation (Go 1.24+)

Go 1.24 (released Feb 2025) ships with a native FIPS 140-3 module. This is
the **preferred** path for new Go code.

| Role | Mechanism | CMVP cert | Build flag |
|---|---|---|---|
| Core primitives | Go native FIPS module | pending / see CMVP | `GODEBUG=fips140=on` at runtime |

### Fallback (Go ≤ 1.23)

Use Google's BoringCrypto fork. This is Google-maintained; expect
version-lag behind mainline Go.

| Role | Mechanism | CMVP cert | Build flag |
|---|---|---|---|
| Core primitives | BoringCrypto | #4407 | `GOEXPERIMENT=boringcrypto` |

### Runtime assertion

Go's FIPS mode sets `GOFIPS` on the process. Assert on startup:

```go
import (
    "os"
    "strings"
    "log"
)

func assertFips() {
    // Go 1.24+ native FIPS
    if os.Getenv("GODEBUG") == "" || !strings.Contains(os.Getenv("GODEBUG"), "fips140=on") {
        // Fall back to BoringCrypto check
        if !boring.Enabled() {
            log.Fatal("Not running in FIPS mode")
        }
    }
}
```

### Gotchas

- **BoringCrypto is a fork of Go**, not a Go module. You must build with
  the BoringCrypto toolchain (`go1.20.5b7`, `go1.21.12b7`, etc.). Vanilla
  `go build` does not switch into FIPS mode.
- **Go native FIPS** (1.24+) is a build-time + runtime combination:
  compile with FIPS support (default in Go 1.24 official release), then
  enable at runtime with `GODEBUG=fips140=on`.
- **Many Go libraries use `golang.org/x/crypto`** which contains
  non-FIPS-approved primitives (e.g., `chacha20poly1305`, `nacl`,
  `curve25519` standalone). `go version -m binary` and
  `go list -deps -m all` can reveal these transitives.
- **`crypto/rand`** routes through the FIPS DRBG when the binary is in
  FIPS mode. Application code does not need to change.
- **TLS**: the standard `crypto/tls` honours FIPS mode by restricting
  cipher suites automatically.

### Common anti-patterns

```go
// BAD: chacha20poly1305 is not FIPS-approved.
import "golang.org/x/crypto/chacha20poly1305"

// BAD: curve25519 standalone (Ed25519/X25519 via x/crypto)
// Ed25519 is conditionally approved in FIPS 186-5; x/crypto's impl
// may not be the CMVP-validated one. Check your module.
import "golang.org/x/crypto/ed25519"  // suspect

// GOOD (Go 1.24+ FIPS): standard library routes through validated module
import "crypto/ecdsa"
import "crypto/elliptic"
```

---

## Python

### Primary recommendation

Python does not ship its own cryptographic module. It defers to the OpenSSL
that Python was compiled against. For FIPS:

| Component | Requirement |
|---|---|
| OpenSSL | Built with `--enable-fips` and a CMVP-validated FIPS provider loaded |
| Python `cryptography` package | Uses the Python `ssl`/`_hashlib` modules which route through the system/bundled OpenSSL |
| `hashlib`, `hmac` | Ditto — route through OpenSSL when available |

Most production FIPS Python deployments use **Red Hat Enterprise Linux**
or **Ubuntu Pro FIPS** with the OS-supplied FIPS OpenSSL.

| OS | OpenSSL CMVP cert | Activation |
|---|---|---|
| RHEL 9 FIPS | #4282 (OpenSSL 3.0 FIPS Provider) | `fips-mode-setup --enable` + reboot |
| Ubuntu 22.04 Pro FIPS | #4282 (OpenSSL 3.0 FIPS Provider) | Ubuntu Advantage / Pro subscription |
| RHEL 8 FIPS | #4282 | `fips-mode-setup --enable` |

### Runtime assertion

```python
import ssl, hashlib, sys

def assert_fips() -> None:
    # OpenSSL 3.0+ FIPS module check
    if not hasattr(ssl, "FIPS_mode"):
        # Python 3.9+ removed FIPS_mode() from ssl; check via the
        # OpenSSL provider list
        pass
    # hashlib.get_fips_mode() in Python ≥ 3.9 on FIPS-enabled OpenSSL
    try:
        fips_active = hashlib.get_fips_mode()
    except AttributeError:
        fips_active = False
    if not fips_active:
        print("NOT IN FIPS MODE", file=sys.stderr)
        sys.exit(2)
```

### Gotchas

- **No native macOS FIPS**. Python installed via Homebrew or python.org
  on macOS will not be in FIPS mode. Use a Linux container for FIPS
  development and testing.
- **`pycryptodome`, `pycrypto`**. These are **not FIPS-validated**. They
  implement their own AES/SHA/RSA. A FIPS codebase must not use them.
- **`passlib` with bcrypt / argon2 / scrypt** — disallowed under FIPS.
  Use `hashlib.pbkdf2_hmac()` (which routes through OpenSSL) with
  SHA-256 and a high iteration count.
- **Python's `secrets` module** — routes through OS entropy; OK in FIPS
  mode because the OS entropy feeds the CMVP DRBG, but strictly speaking
  `secrets.token_bytes()` does not call into the FIPS provider. For
  clarity prefer `os.urandom` / `secrets` on FIPS-enabled OS.
- **Wheels on PyPI**. Many pre-compiled wheels bundle their own OpenSSL
  (e.g., `cryptography` on some platforms). Check whether the wheel
  uses the system OpenSSL — use `python -c 'import cryptography; print(cryptography.hazmat.backends.default_backend().openssl_version)'`.

---

## Other languages / runtimes (v0.1 summary — full detail v0.2+)

v0.1 covers Rust / Go / Python in depth. The following are reference
pointers only; fuller treatment lands in v0.2.

| Language / Runtime | FIPS-validated library | CMVP cert | Build flag | v0.1 notes |
|---|---|---|---|---|
| Java | Bouncy Castle FIPS | #4616 | `-Dorg.bouncycastle.fips.approved_only=true` | JCA provider ordering matters; add BCFIPS before other providers |
| Node.js | Node w/ OpenSSL 3.0 FIPS | #4282 (inherits) | `--enable-fips` or `crypto.setFips(1)` | No native FIPS wheels on macOS; use Linux |
| .NET (Windows) | Windows CNG system FIPS mode | #4293 (Windows 10/11 CNG) | `FIPSAlgorithmPolicy` registry key | CLR honours the OS-level FIPS flag |
| .NET (Linux) | OpenSSL providers | #4282 (inherits) | Same as Linux Python | Via `System.Security.Cryptography` |
| iOS / macOS | Apple CoreCrypto FIPS | #4506 | System-provided | Must use approved APIs only; most `Security.framework` APIs route through it |
| Android | Google Conscrypt FIPS | #4477 | — | Android 10+ for best coverage; check per-OEM |

---

## Platform caveats

### macOS / Windows development

FIPS mode is available in production on Windows (CNG FIPS) and
iOS/macOS (CoreCrypto FIPS), but local development of **Linux-targeted**
FIPS software on macOS / Windows workstations typically requires a Linux
container or VM, because `aws-lc-rs` / BoringCrypto / OpenSSL-FIPS don't
build natively on every dev OS.

### Container deployments

- Use a **FIPS-branded base image**: RHEL UBI FIPS, Ubuntu Pro FIPS,
  Amazon Linux FIPS AMI. Do not try to retrofit FIPS onto a non-FIPS
  base image.
- Verify the module is active inside the container: `openssl list -providers`
  should list `fips`.
- Host kernel and container runtime should both be in FIPS mode — check
  `/proc/sys/crypto/fips_enabled` inside the container.

### Docker Desktop Linux-VM on macOS

Docker Desktop's Linux VM can host a FIPS-mode container for development,
but you are still responsible for the certificate validity of the OpenSSL
inside the container image.

---

## CMVP certificate verification workflow

Before citing a cert number in an SSP, evidence checklist, or POAM:

1. Visit https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules.
2. Search by the certificate number.
3. Verify:
   - Status is **Active** (not Historical, Revoked, or Sunset).
   - The module version matches the version you are deploying.
   - The tested configuration (OS, hardware) matches yours.
4. Record the verification date in your compliance matrix.

`tools/build-data.py` fails the build if any cert in
`data/fips-libraries.json` has a `verified_on` older than 90 days.

---

## Common mistakes summary

1. **Using a non-FIPS library because it was the default** (e.g., `ring`
   in Rust, `pycryptodome` in Python).
2. **Forgetting to enable FIPS mode at runtime** (Go 1.24 needs
   `GODEBUG=fips140=on`; OpenSSL 3 needs the FIPS provider loaded).
3. **Not asserting FIPS mode on startup** — the application happily runs
   in non-FIPS mode and you only discover it at audit.
4. **Stale CMVP certificate claims** — a cert that was valid at design
   time is revoked by the time of audit.
5. **Platform mismatch** — your cert is for Linux x86_64, you deploy on
   aarch64 — the cert doesn't cover you.
6. **Duplicate crypto stacks** — a transitive dependency pulls in a
   second crypto library that isn't FIPS-mode.
7. **Assuming TLS libraries "just work"** — they often accept
   non-approved cipher suites by default; restrict them explicitly.
