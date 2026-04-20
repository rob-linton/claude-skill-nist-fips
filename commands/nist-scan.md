---
name: nist-scan
description: Whole-repo NIST SP 800-53 Rev 5 gap analysis against a target baseline (FedRAMP Low/Moderate/High, CMMC L2, HIPAA, SOC 2). Delegates to the compliance-auditor subagent (v0.2+) or runs inline (v0.1). Produces a gap report with per-control status and evidence pointers.
---

# /nist-scan

> **Read [`../SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** The output of
> this command is a **draft** for human review — not an audit deliverable.

Scan the current repository and produce a NIST SP 800-53 Rev 5 gap
analysis against a target compliance baseline.

## Usage

```
/nist-scan
/nist-scan --framework fedramp-moderate
/nist-scan --framework fedramp-high
/nist-scan --framework cmmc-l2       # v0.2+
/nist-scan --framework hipaa         # v0.2+
/nist-scan --framework soc2          # v0.2+
/nist-scan --scope services/my-subdir/     # v0.2+ monorepo scoping
```

Default framework is `fedramp-moderate` if none specified.

## What it does

1. **Load the control catalogue** from
   `../data/nist-800-53-rev5.json` (in v0.1, AC/AU/IA/SC only).
2. **Load the framework cross-map** from
   `../data/framework-crossmap.json`. For the target framework, determine
   the required control set.
3. **Load the existing compliance matrix** if present in the repo
   (common paths: `Documentation/compliance/compliance-matrix.md`,
   `docs/compliance-matrix.md`, `compliance-matrix.md`). Parse the YAML
   header and matrix rows.
4. **Delegate to the `compliance-auditor` subagent** (v0.2+) to analyse
   each required control. In v0.1, Claude performs the analysis inline
   by reading the relevant files.
5. For each required control:
   - If the matrix has a PASS row with evidence pointers — verify the
     pointers resolve to existing code; report `VERIFIED`.
   - If the matrix has a PARTIAL/PLANNED row — report as such with the
     existing rationale.
   - If the matrix has no row — report `MISSING`.
   - If the matrix has a PASS row but evidence pointers are stale
     (file doesn't exist or line doesn't match) — report `STALE`.
6. **Produce a report** with summary counts and per-control detail.
7. **Do not modify the matrix.** The scan is read-only; human review
   is required before adding / editing rows.

## Output format

```
=== NIST SP 800-53 Rev 5 Gap Analysis ===
Repository: <path>
Target framework: fedramp-moderate
Scan date: <ISO-8601>
Catalog version: 5.2.0 (OSCAL last-modified 2025-08-26)

Summary:
- Required controls (FedRAMP Moderate): <N>
- Covered by v0.1 scope (AC/AU/IA/SC): <N>
- VERIFIED: <count>
- PARTIAL: <count>
- PLANNED: <count>
- MISSING: <count>
- STALE: <count>

Findings:

[MISSING] AC-6 - Least Privilege
  No row in compliance matrix. Required by FedRAMP Moderate.
  Next step: follow workflows/MapFeatureToControls.md to draft a row.

[STALE] AU-3 - Content of Audit Records
  Matrix row claims evidence at backend/src/audit.rs:42 but that file
  does not exist. Investigate whether the reference is outdated.

[VERIFIED] IA-2(1) - MFA for Privileged Accounts
  Matrix: PASS
  Evidence: backend/crates/securedrop-api/src/routes/sessions.rs:142 ✓
  ODP values: (n/a)

[PARTIAL] IA-5(1) - Password-Based Authentication
  Matrix: PARTIAL
  Rationale: Breach-database check not implemented. Compensating
             control: AC-7 rate limit + lockout. Target Q3 2026.
  POAM reference: (none found - consider adding)

... etc ...
```

## Behavioural rules for Claude when running this command

1. **Never invent a control row**. If the matrix has no row for a
   required control, report `MISSING` — do not draft a row yourself.
   Drafting is a follow-up human-reviewed action via
   `workflows/MapFeatureToControls.md`.
2. **Verify evidence pointers literally**. If a matrix row claims
   evidence at `src/foo.rs:42`, read that file and that line. Match
   the claimed description to what's actually there.
3. **Do not mark anything as `VERIFIED`** unless the claimed file:line
   exists and matches the description.
4. **Preserve the existing matrix prose verbatim** in the report. Do
   not rephrase, summarise, or correct — the matrix is the user's
   authored text.
5. **Report counts accurately.** The summary numbers must sum to the
   total required-control count.

## Limitations (v0.1)

- Only AC/AU/IA/SC families are covered in the v0.1 catalog data.
  Other families will be reported as "out of v0.1 scope".
- `--framework cmmc-l2|hipaa|soc2` are not functional in v0.1 (only
  FedRAMP Low/Moderate/High cross-maps populated).
- `--scope` monorepo flag is v0.2+.
- No auto-generation of missing rows (by design — that requires human
  review).
- The command is read-only; it does not modify the matrix or any code.

## See also

- [`workflows/MapFeatureToControls.md`](../workflows/MapFeatureToControls.md)
  — how to draft a matrix row for a feature.
- [`workflows/AuditFipsCompliance.md`](../workflows/AuditFipsCompliance.md)
  — FIPS crypto audit, complementary to this scan.
- [`context/FrameworkCrossMap.md`](../context/FrameworkCrossMap.md)
  — control-to-framework mapping authority.
