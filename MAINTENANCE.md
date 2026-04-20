# MAINTENANCE.md

Ownership, succession, and lifecycle policy for NistFipsCompliance.

---

## LEGAL NOTICE

This project is an **individual-maintainer, unaffiliated, non-endorsed** open
source project. See [`README.md`](README.md) §LEGAL NOTICE for the full
terms. The maintenance policy below does not create any warranty or
contractual relationship. Apache License 2.0 applies; provided AS-IS.

---

## Named maintainer

| Role | Name | Contact | Capacity |
|---|---|---|---|
| Primary maintainer | Rob Linton | `rob.linton@senetas.com` | Individual, best-effort |
| Backup maintainer | **VACANT — seeking volunteer** | — | — |

**Bus-factor-1 warning.** Until a backup maintainer is named, this project
operates under a BUS-FACTOR 1 policy:

- `README.md` carries a "SINGLE-MAINTAINER — BUS-FACTOR 1" banner.
- All downstream users are advised to mirror the repo locally and pin to a
  specific signed release, so that maintainer unavailability does not break
  their installations.

If you would like to volunteer as a backup maintainer, open an issue titled
`[MAINTAINER] Volunteer for backup role` describing your relevant background
(compliance engineering, FIPS, FedRAMP/CMMC experience preferred). No
formal commitment required — backup maintainers adopt the role informally
by merging PRs when the primary is unavailable.

---

## Availability and sunset policy

Automated checks run in GitHub Actions:

| Silence period | Action |
|---|---|
| 30 days | Status comment posted on the open-issues dashboard |
| 90 days | Auto-issue created: `[ATTENTION] No commits in 90 days` |
| 180 days | `README.md` auto-updates with `UNMAINTAINED — DO NOT RELY ON` banner |
| 365 days | Final archival release tagged, repo archived read-only |

The primary maintainer can reset these timers by committing any non-trivial
change (even a `MAINTENANCE.md` touch with a date note suffices, provided
the issue tracker is also triaged).

---

## Succession

If the primary maintainer becomes unavailable without a backup in place:

1. **Forking is explicitly encouraged.** Apache 2.0 allows unconditional
   forks. A fork under a new maintainer is the expected recovery path; the
   new fork should update its `NOTICE` to credit this project, rename the
   skill name to avoid collision, and independently validate the data
   files before re-release.

2. **Repo read-only archival.** The repository will be flagged read-only
   (GitHub `archived: true`). No new releases, no issue triage. The README
   will point downstream users to a successor fork if one is known.

3. **Key escrow.** Release-signing material is recorded below to allow
   successors to verify the authenticity of historic releases:

   - **GPG fingerprint**: (to be added at v0.1 tag cut)
   - **Sigstore OIDC identity**: `rob.linton@senetas.com` via GitHub OIDC
   - **Release-hash manifest**: `tools/RELEASES.sha256` (appended on each
     tag)

   *Successors cannot sign new releases under the primary maintainer's
   identity — they must issue a fresh signing key and document the rotation
   in `MAINTENANCE.md` of the successor fork.*

---

## Data refresh cadence

The skill's authoritative value depends on fresh data. The maintainer
commits to — and automation enforces — the following cadence:

| Source | Cadence | Automation |
|---|---|---|
| NIST OSCAL SP 800-53 Rev 5 | Monthly | `.github/workflows/data-refresh.yml` opens a PR if diff is non-empty |
| CMVP validated-modules list | Quarterly (manual) | Build fails if any cert expires within 90 days without a successor listed |
| FedRAMP Rev 5 baselines | Quarterly (manual) | Build fails if FedRAMP PMO publishes a delta not reflected here |
| FIPS 140-3 Implementation Guidance | Quarterly (manual) | Build fails if any algorithm's status changes |
| CMMC Assessment Guide | Quarterly (manual) | — |
| HIPAA OCR crosswalk | Annual (manual) | — |
| SOC 2 TSC (AICPA) | Annual (manual) | — |

"Manual" cadences are performed by the primary maintainer. If a cadence is
missed by more than 2x its period, the primary maintainer marks the
affected data file as `STALE` in `data/_meta.json`, and the
`validate-skill.py` check surfaces a warning on every run.

---

## Revision migration

When NIST publishes SP 800-53 Rev 6 (no public timeline as of 2026-04-20):

1. `main` branch begins tracking Rev 6 from the announcement date.
2. `rev5` branch is created at the last Rev 5 release, kept in maintenance
   mode for **24 months** after Rev 6 publication.
3. A `MIGRATION.md` is added to `main` explaining Rev 5 → Rev 6 mapping
   deltas.
4. All downstream users are advised to follow NIST's own transition timeline
   for their specific authorisation baseline — this skill does not make
   that decision for them.

FIPS 140-3 → 140-4 migration follows the same pattern when 140-4 is
finalised by NIST.

---

## Unresolved / known-risk areas

Topics the maintainer knows are incomplete and would accept PRs on:

- **Non-US frameworks.** ANSSI (France), BSI C5 (Germany), ISMAP (Japan),
  ENS (Spain), ISO 27001 — all out of scope and unlikely to be added by
  the primary maintainer without a volunteer.
- **Ed25519 FIPS status.** Approved in FIPS 186-5 (Feb 2023) but many CMVP
  modules shipped before 2024 do not list it. The skill treats Ed25519 as
  `conditionally_approved` with a module-check condition.
- **X25519/X448 in isolation.** Not yet approved standalone under 140-3 IG
  as of 2026-04. Approved as part of a hybrid KEM. The skill treats as
  `conditionally_approved`.
- **ML-KEM / ML-DSA / SLH-DSA CMVP rollout.** FIPS 203/204/205 are
  standards; actual CMVP-validated module implementations are rolling out
  gradually through 2026. The skill flags these as approved-per-standard
  but warns to verify your specific module's cert.
- **Inherited controls from CSPs.** Cross-maps ship for AWS GovCloud,
  Azure Government, and GCP Assured Workloads in v0.3+; GCP Assured
  Workloads data is the least mature.
