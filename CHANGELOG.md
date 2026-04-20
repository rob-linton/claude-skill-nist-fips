# Changelog

All notable changes are recorded here. Format roughly follows [Keep a
Changelog](https://keepachangelog.com/en/1.1.0/). The project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) — but given the
content (compliance data) is the primary product, minor-version bumps will
also be triggered by material content updates (e.g., a NIST revision diff,
a new framework cross-map), not only by code changes.

## [Unreleased]

### Changed
- CI actions bumped to Node 24-compatible versions (GitHub deprecates
  Node 20 action runners on 2026-09-16, forces Node 24 default on
  2026-06-02). `actions/checkout` 4.2.2 → 4.3.1; `actions/setup-python`
  5.6.0 → 6.2.0. Both remain SHA-pinned per CONTRIBUTING.md
  supply-chain policy.
- `.claude-plugin/plugin.json` aligned with the Claude Code plugin
  installer schema. The installer rejects unknown keys, so the following
  were removed from the manifest: `$schema`, `skill`, `features`,
  `requirements`, `legal_notice`, `release_verification`, `keywords`.
  `repository` and `bugs` are now URL strings rather than objects.
- `tools/validate-skill.py` relaxed its `plugin.json` invariants to
  match. The `skill` and `legal_notice` keys are no longer required,
  and the `skill.path == "."` check is removed. Legal-notice prose
  enforcement continues unchanged via `check_legal_notice_presence()`
  against `README.md`, `SKILL.md`, and other prose files — that was
  always the functional check; the manifest field duplicated it.
- `README.md` installation section rewritten. Path #2 now documents
  installing as a first-class Claude Code plugin via a local
  marketplace (`claude plugin marketplace add` +
  `claude plugin install`), including the `marketplace.json` shape
  and the symlink pattern for out-of-tree skill directories.

### Fixed
- `claude plugin install` now succeeds against this repository's
  `.claude-plugin/plugin.json`. Previously it failed with
  "Unrecognized keys" and "repository: expected string, received
  object" validation errors.
- `tools/build-data.py` now produces byte-identical output on every
  rebuild against the same OSCAL revision. Previously the `built_at`
  field (propagated into `data/nist-800-53-rev5.json`,
  `data/_meta.json`, and the `Built at:` header of
  `context/NistControlCatalogue.md`) was set to wall-clock time, so
  every rebuild drifted by a few seconds and the CI reproducibility
  check (`build-data.py && git diff --exit-code`) failed on every
  push. `built_at` is now derived from OSCAL's
  `catalog.metadata.last-modified` — the build is a pure function of
  its input, which is the honest semantics the field always intended.

### Added
- Repository scaffold: `LICENSE` (Apache 2.0), `NOTICE`, `README.md` with
  LEGAL NOTICE, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  `MAINTENANCE.md`.
- `SKILL.md` routing hub with non-endorsement
  scope boundary.
- `context/FipsAlgorithms.md`, `context/FipsLibraries.md`,
  `context/EvidenceModel.md`, `context/ThreatModel.md`.
- `data/nist-800-53-rev5.json` generated from NIST OSCAL (AC, AU, IA, SC
  families for v0.1).
- `data/fips-algorithms.json`, `data/fips-libraries.json`,
  `data/framework-crossmap.json`.
- `context/NistControlCatalogue.md` (AC/AU/IA/SC) — generated from
  OSCAL data.
- `workflows/MapFeatureToControls.md`, `workflows/AuditFipsCompliance.md`.
- `commands/nist-scan.md`, `commands/fips-audit.md`.
- `agents/fips-crypto-reviewer.md` subagent.
- `.claude-plugin/plugin.json` manifest.
- `tools/build-data.py` OSCAL importer.
- `tools/validate-skill.py` disclaimer + watermark + endorsement-denylist
  enforcer.
- 5 test fixtures under `tools/fixtures/` with human-authored
  `GROUND_TRUTH.md`: `fixture-rust-chacha20`, `fixture-rust-aws-lc-ok`,
  `fixture-go-no-boring`, `fixture-python-md5-legacy`,
  `fixture-greenfield-no-matrix`.
- `tests/test_fips_scan.py`, `tests/test_data_integrity.py`,
  `tests/conftest.py`.
- `.github/workflows/ci.yml`.

### Known limitations
- No hooks yet (v0.2 will add Go-binary pre-edit hooks).
- No SSP/POAM generator (v0.4 milestone).
- Only 4 of 20 NIST families in initial data import (AC, AU, IA, SC);
  remaining 16 come in v0.2.
- Framework cross-map includes only FedRAMP Moderate stub entries for
  the v0.1 control set.
- Backup maintainer position is VACANT; project operates under
  bus-factor-1 until a volunteer is named.
- No formal legal review has been performed on this release.
