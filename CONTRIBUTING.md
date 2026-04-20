# CONTRIBUTING.md

Thank you for considering a contribution to NistFipsCompliance.

> **Read [`README.md`](README.md) §LEGAL NOTICE first.** By submitting a
> contribution, you acknowledge that this is an unaffiliated,
> non-endorsed, individual-maintainer project and that the Apache 2.0
> warranty disclaimer applies to your contribution.

---

## What the project will and won't accept

**Accepted without much debate:**

- Bug fixes with a reproducing test case.
- Data updates citing authoritative sources (NIST, FIPS, FedRAMP PMO,
  HHS/OCR, DoD CIO). The commit message must include the URL and
  publication date of the source.
- Language-specific additions to `FipsLibraries.md` (new CMVP-validated
  libraries with certificate numbers).
- Test fixtures with human-authored `GROUND_TRUTH.md`.
- Documentation improvements that don't introduce
  endorsement-implying language (see denylist below).

**Accepted with discussion first** (open an issue before the PR):

- New control families, frameworks, or cross-maps.
- New slash commands or subagents.
- Changes to hook behaviour.
- Schema changes to `data/*.json` files.

**Not accepted:**

- Claims that this skill is "NIST-approved", "FedRAMP-ready",
  "FIPS-certified", or similar — the
  `tools/validate-skill.py` denylist blocks these phrases.
- Code that would remove the `DRAFT — UNREVIEWED — NOT FOR SUBMISSION`
  watermark from generated-output templates, or add a `/remove-watermark`
  command.
- Hooks that make network calls or write outside the repo root.
- Adding runtime dependencies to the Python tooling beyond the stdlib,
  or to the hooks. (Go binaries when added in v0.2 may use Go stdlib +
  Tree-sitter.)
- Third-party skills/agents/commands that carry opinions about
  organisational policy not derivable from NIST/FIPS/FedRAMP/CMMC/HIPAA/
  SOC 2 authoritative sources.

---

## Contributor checklist

Before opening a PR:

1. **Run the validator**:
   ```bash
   python3 tools/validate-skill.py
   ```
   Must exit 0.

2. **Run the tests**:
   ```bash
   python3 -m pytest tests/
   ```
   All must pass.

3. **If you touched `data/*.json`**: the commit message must include an
   authoritative source URL and publication date. The data integrity
   tests (`tests/test_data_integrity.py`) must still pass.

4. **If you touched prose in `SKILL.md`, `README.md`, or `context/*.md`**:
   the endorsement-language denylist check must pass. The current
   denylist includes:
   - `NIST-approved` (applied to this skill or its data)
   - `FedRAMP-ready`
   - `FIPS-certified` (applied to this skill)
   - `CMVP-certified` (applied to this skill)
   - `audit-proof`, `audit-ready`, `compliance-guaranteed`
   - `production-validated` (applied to this skill's output)

   These phrases are acceptable only in well-bounded contexts
   (e.g., describing a library that *is* FIPS-certified in
   `FipsLibraries.md`). The validator uses regex with context
   heuristics; if it flags a legitimate use, discuss in the PR.

5. **If you added a new detection pattern** to
   `data/fips-algorithms.json`: add at least one fixture under
   `tools/fixtures/` that exercises it, with a human-authored
   `GROUND_TRUTH.md`.

---

## Ground-truth discipline

The skill's credibility is based on traceability. Every claim must trace
back to an authoritative source.

- **NIST control text** — extracted deterministically from NIST OSCAL by
  `tools/build-data.py`. Never hand-edited in `NistControlCatalogue.md`
  (CI fails if the generated prose drifts from the JSON data).
- **FIPS algorithm status** — every entry in `data/fips-algorithms.json`
  has a `fips_reference` field citing the FIPS publication
  (e.g., `FIPS 197 §5.2`, `SP 800-131A Rev 3 Table 4`).
- **CMVP certificate numbers** — every entry in `data/fips-libraries.json`
  has a `verified_on` date. `tools/build-data.py` warns if any cert is
  missing the current-status check.
- **Framework cross-maps** — every row in `data/framework-crossmap.json`
  has a `source` field citing the authoritative crosswalk document.

Contributions that fill in "TODO" cells without an authoritative source
will be rejected.

---

## Code of conduct

See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## License

By contributing you agree to license your contribution under Apache 2.0,
consistent with the rest of the project.
