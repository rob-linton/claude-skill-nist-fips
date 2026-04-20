# Changelog

All notable changes are recorded here. Format roughly follows [Keep a
Changelog](https://keepachangelog.com/en/1.1.0/). The project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) — but given the
content (compliance data) is the primary product, minor-version bumps will
also be triggered by material content updates (e.g., a NIST revision diff,
a new framework cross-map), not only by code changes.

## [Unreleased]

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
