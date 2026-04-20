# Ground truth: fixture-greenfield-no-matrix

> Human-authored ground truth for the fixture. Not Claude-generated.

## What this fixture represents

A tiny Rust project that compiles to a single `hello world` binary. It
does NOT use any cryptography. It does NOT have a compliance matrix
file anywhere.

This represents the "greenfield" starting point for a team that is
starting to adopt the skill — they should see the following outcomes:

## Expected `/fips-audit` outcome

- **No crypto usage detected** — zero FAIL/WARN findings from
  algorithm scanning.
- **Library check**: no FIPS library required (no crypto). Report "no
  crypto detected; FIPS library check not applicable".
- **Startup assertion**: not required.
- **TLS policy**: not applicable.
- **Overall**: OK.

## Expected `/nist-scan --framework fedramp-moderate` outcome

- **No compliance matrix found** — the scan should emit a single
  informational finding instructing the user to run
  `workflows/BuildComplianceMatrix.md` (v0.2+) or manually create a
  matrix following `templates/compliance-matrix.md` (v0.2+).
- **All required FedRAMP Moderate controls in v0.1 scope (AC/AU/IA/SC)**
  are reported as `MISSING`.
- **Overall**: the user's next action is to bootstrap a matrix; the
  scan does not fail, it reports the starting state.

## Expected overall severity

**OK with missing-matrix info hint.** This is the expected output for
a team that has just installed the skill in a brand-new repo — it
shouldn't be alarming.

## Sources

- Workflow: `workflows/BuildComplianceMatrix.md` (v0.2+)
- Template: `templates/compliance-matrix.md` (v0.2+)
- `/nist-scan` behaviour rule 4: "If the matrix has no row for a
  required control, report MISSING — do not draft a row yourself."
