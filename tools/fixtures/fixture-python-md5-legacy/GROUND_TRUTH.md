# Ground truth: fixture-python-md5-legacy

> Human-authored ground truth for the fixture. Not Claude-generated.

## What this fixture represents

A Python script that uses `hashlib.md5()` for a non-security purpose
(cache-busting ETag). Since Python 3.9, `hashlib.md5(data,
usedforsecurity=False)` is the supported way to use MD5 in FIPS-enabled
Python without the module rejecting the call.

The scanner must detect the MD5 usage AND the `usedforsecurity=False`
keyword, and classify as WARN (legacy-ok) rather than FAIL, since the
use is explicitly non-security.

The scanner must also detect a separate MD5 call elsewhere in the file
that does NOT pass `usedforsecurity=False` — that call is a FAIL.

## Expected scanner findings

| Severity | File | Line | Pattern | Algorithm | Notes |
|---|---|---|---|---|---|
| WARN | etag.py | 7 | `hashlib.md5(...)` with `usedforsecurity=False` | MD5 | legacy-ok; cache-busting only; accept with inline suppression + CI audit |
| FAIL | etag.py | 12 | `hashlib.md5(...)` without `usedforsecurity=False` | MD5 | security-relevant use; DISALLOWED |

## Expected library-check result

| Language | Library | Expected | Present | Result |
|---|---|---|---|---|
| python | OpenSSL 3 FIPS provider | runtime-verifiable via `openssl list -providers` | UNKNOWN (no openssl tooling in fixture) | skipped |

## Expected overall severity

**FAIL** — the unsuppressed MD5 call is a FAIL. The suppressed call is a
WARN.

## Suppression-handling expectation

A future version of the fixture may add `# fips:ignore reason="etag cache
bust"` above line 12 to test suppression detection. v0.1 does not
implement inline-suppression parsing (Go hook v0.2+).

## Sources

- `fips-algorithms.json`: MD5 entry (status=DISALLOWED,
  `suppression_hint` mentions cache-busting scenario)
- `FipsAlgorithms.md` §Hash functions
- Python 3.9+ `hashlib` documentation:
  https://docs.python.org/3/library/hashlib.html#usedforsecurity
