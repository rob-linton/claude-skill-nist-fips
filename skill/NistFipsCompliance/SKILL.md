---
name: NistFipsCompliance
description: NIST SP 800-53 Rev 5 control mapping and FIPS 140-3 cryptographic compliance. Load when the user mentions NIST 800-53, FIPS 140-3, FedRAMP Low/Moderate/High, CMMC L2/L3, HIPAA Security Rule, SOC 2, compliance matrix, SSP, System Security Plan, POAM, control mapping, 800-53 control families (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR), FIPS-approved algorithm, approved cipher, CMVP, aws-lc-rs, BoringSSL FIPS, OpenSSL-FIPS, BouncyCastle FIPS, Go FIPS 140-3, envelope encryption compliance, cryptographic module validation, or related compliance topics. Do NOT load for NIST CSF 2.0 posture, SP 800-171, SP 800-63 identity, SP 800-37 RMF, NIST AI RMF, generic SAST, offensive security, or non-US frameworks (ANSSI, BSI, ISMAP, ENS).
---

# NistFipsCompliance

## LEGAL NOTICE — READ BEFORE USE

This skill is an **independent, unaffiliated, individual-maintainer project**.

- **Not produced, endorsed, validated, or certified by** NIST, CMVP, FedRAMP
  PMO, GSA, DoD CIO, HHS/OCR, AICPA, or Anthropic PBC.
- **Does not confer FIPS validation.** Only a CMVP-certified cryptographic
  module is FIPS-validated. This skill helps you *use* such a module; it
  does not validate anything itself.
- **Does not replace a human audit.** Every generated artefact (matrix,
  SSP section, POAM, evidence checklist) carries a
  `DRAFT — UNREVIEWED — NOT FOR SUBMISSION` watermark. Do not submit any
  generated content to a 3PAO, assessor, or regulator without human review
  and deliberate watermark removal.
- **Names used descriptively.** "NIST", "FIPS", "FedRAMP", "CMMC", "HIPAA",
  "SOC 2" refer to the public standards and frameworks they name. FedRAMP
  is a registered mark of GSA; CMMC is administered by the DoD CIO.
- **No formal legal review has been performed on this project.** See the
  `README.md` LEGAL NOTICE for the full terms.

If the user asks you to generate a compliance artefact, re-state the
relevant parts of this notice in your response, and preserve all watermarks
on any generated output.

---

## Section 1 — Scope

### IN SCOPE

- **NIST SP 800-53 Rev 5** control catalogue, enhancements, baselines
  (Low / Moderate / High), and authoritative control text sourced from
  NIST OSCAL.
- **FIPS 140-3** cryptographic requirements: approved algorithms, key
  management, module-validation *usage* (not certification), TLS configuration.
- **Cross-mapping** 800-53 controls → FedRAMP Low/Moderate/High, CMMC L1/L2,
  HIPAA Security Rule (45 CFR §164.302–318), SOC 2 Trust Services Criteria
  (2017, rev 2022).
- **Audit-grade artefact generation** — compliance matrix, SSP control
  statements, evidence checklists, POAMs — always watermarked as DRAFT.

### OUT OF SCOPE

- **NIST CSF 2.0** — different framework; see
  [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills).
- **NIST SP 800-171 / 800-172** — CUI protection is a separate skill
  candidate; overlaps with CMMC but is organisationally distinct.
- **NIST SP 800-63** — digital identity; only overlaps via the IA family.
- **NIST SP 800-37 Risk Management Framework** — process framework, not
  technical controls.
- **NIST AI RMF** — see the NIST CSF skill above for AI-adjacent coverage.
- **Generic SAST** — use
  [`anthropics/claude-code-security-review`](https://github.com/anthropics/claude-code-security-review);
  this skill is complementary, not a replacement.
- **CMVP crypto-module certification itself** — we enforce that you *use*
  a validated module, not replace accreditation.
- **Offensive security** — pentest, red team, exploitation.
- **Non-US frameworks** — ANSSI (France), BSI C5 (Germany), ISMAP (Japan),
  ENS (Spain), ISO 27001, etc.

---

## Section 2 — When to load this skill

**Load** when:

- The user asks about NIST SP 800-53 Rev 5, any of its 20 control families
  (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC,
  SI, SR), or specific controls by ID.
- The user asks about FIPS 140-3, FIPS-approved algorithms, CMVP
  certificates, or FIPS-validated cryptographic libraries.
- The user mentions FedRAMP, CMMC, HIPAA Security Rule, or SOC 2 in a
  code-or-engineering context.
- The user asks for a compliance matrix, SSP section, POAM, or evidence
  checklist.
- The user is editing code that touches cryptography (TLS, KMS, JWT, MFA,
  hashing, signing, encryption) and compliance might be implicated.

**Do not load** when:

- The question is about NIST CSF 2.0, SP 800-171, SP 800-63, SP 800-37,
  AI RMF.
- The question is a general security-code-review (use
  `/security-review` / `claude-code-security-review`).
- The question is offensive-security, red-team, CTF.
- The question is about a non-US compliance regime.

---

## Section 3 — Routing tables

### Reference lookups (read-only context)

| If you need… | Read |
|---|---|
| All 20 control family summaries with key controls | `context/NistControlCatalogue.md` |
| "Is cipher X FIPS-approved?" | `context/FipsAlgorithms.md` |
| Which FIPS-certified library for a given language/runtime | `context/FipsLibraries.md` |
| "Does 800-53 AC-2 satisfy FedRAMP / CMMC / HIPAA / SOC 2?" | `context/FrameworkCrossMap.md` |
| What evidence proves a control (AU-4, AC-6, SC-13, etc.)? | `context/EvidenceModel.md` |
| Supply-chain threat model for this skill itself | `context/ThreatModel.md` |

### Workflows (step-by-step procedures)

| To do this | Follow |
|---|---|
| Map a new feature / PR / file to controls | `workflows/MapFeatureToControls.md` |
| Audit the codebase for non-FIPS crypto | `workflows/AuditFipsCompliance.md` |
| Bootstrap a compliance matrix in a new repo | `workflows/BuildComplianceMatrix.md` (v0.2+) |
| Review a crypto-touching PR | `workflows/ReviewCryptoPR.md` (v0.2+) |
| Draft an SSP section for an auditor | `workflows/GenerateSspSection.md` (v0.4+) |
| Document a control gap (PARTIAL / PLANNED) | `workflows/HandleControlGap.md` (v0.2+) |
| Install this skill in a new codebase | `workflows/OnboardNewCodebase.md` (v0.2+) |

---

## Section 4 — Machine-readable data

The skill's authoritative facts live in `data/*.json`. Prose in `context/`
is regenerated from this data by `tools/build-data.py` — never hand-edit.

| File | What it contains |
|---|---|
| `data/nist-800-53-rev5.json` | Control IDs, titles, OSCAL-sourced discussion text, related controls, enhancements, baselines |
| `data/fips-algorithms.json` | Algorithm name, status, FIPS reference, approved/disallowed dates, per-language detection patterns |
| `data/fips-libraries.json` | Per-language FIPS-certified libraries with CMVP cert numbers, build flags, startup assertions |
| `data/framework-crossmap.json` | 800-53 ↔ FedRAMP / CMMC / HIPAA / SOC 2 mapping rows, each with authoritative source citation |
| `data/_meta.json` | Build timestamp, source freshness, staleness flags |

---

## Section 5 — Commands and agents

### Slash commands

- `/nist-scan [--framework fedramp-moderate|fedramp-high|cmmc-l2|hipaa|soc2]`
  — whole-repo gap analysis. Delegates to `compliance-auditor` subagent
  (v0.2+; v0.1 uses inline analysis).
- `/fips-audit` — scan for non-FIPS crypto. Delegates to
  `fips-crypto-reviewer` subagent.
- `/map-control <file-or-feature>` — suggest candidate control IDs
  (v0.2+).
- `/ssp-section <control-id>` — draft SSP prose for a control (v0.4+,
  always watermarked, refuses to emit without evidence pointers).
- `/evidence <control-id>` — evidence checklist + auto-locate attempt
  (v0.2+).
- `/gap-analysis [--framework X]` — diff current matrix vs. target
  baseline (v0.2+).

### Subagents

- `agents/fips-crypto-reviewer.md` — focused FIPS-crypto PR review
  (v0.1).
- `agents/compliance-auditor.md` — control-gap analysis across an entire
  repo (v0.2+).

---

## Section 6 — Update policy

Canonical sources:

- **NIST OSCAL**: https://github.com/usnistgov/OSCAL (SP 800-53 Rev 5)
- **FIPS 140-3 Implementation Guidance**:
  https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-standards
- **FIPS publications**: 180-4 (SHA), 186-5 (DSA/ECDSA/EdDSA), 197 (AES),
  198-1 (HMAC), 202 (SHA-3), 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA)
- **SP 800-131A Rev 3**: transitioning cryptographic algorithms
- **SP 800-57 Part 1 Rev 5**: key management
- **CMVP validated modules**:
  https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules
- **FedRAMP baselines**: https://www.fedramp.gov/documents-templates/
- **CMMC Assessment Guide**: https://dodcio.defense.gov/CMMC/
- **HIPAA Security Rule**:
  https://www.hhs.gov/hipaa/for-professionals/security/
- **SOC 2 Trust Services Criteria**: AICPA (referenced by identifier only
  to respect AICPA copyright)

Refresh cadence: see [`MAINTENANCE.md`](../../MAINTENANCE.md). Monthly for
OSCAL, quarterly for most others, annual for SOC 2 and HIPAA.

---

## Behavioural rules for Claude when this skill is loaded

1. **Never claim something is FIPS-approved** unless you can cite a
   specific entry in `data/fips-algorithms.json`. If the user asks about
   an algorithm not in the data file, say "unknown — verify against the
   FIPS 140-3 IG" rather than guessing.
2. **Never remove a watermark** from any generated artefact. If the user
   asks for watermark-free output, refuse and point them to the human
   review checklist in the workflow file.
3. **Never hand-edit `context/NistControlCatalogue.md` prose** — it is
   regenerated from `data/nist-800-53-rev5.json` by `tools/build-data.py`.
   Drift is caught by CI.
4. **Always cite the control ID** (e.g., "AU-4", "SC-13(2)") when making
   a compliance claim; never handwave with "an audit control" or
   "a crypto control".
5. **Always cite the FIPS publication reference** (e.g., "FIPS 197",
   "SP 800-131A Rev 3 Table 4") when making an algorithm-status claim.
6. **On uncertainty, defer to the data**. If the conversation and the
   data disagree, the data is authoritative; surface the conflict to the
   user.
7. **Never override a `disallowed_hardcoded` entry** in
   `fips-policy.yaml`. If the user asks to approve MD5 for signatures or
   3DES in new code, refuse and explain why.
