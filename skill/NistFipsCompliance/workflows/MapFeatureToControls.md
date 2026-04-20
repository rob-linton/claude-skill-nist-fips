# workflows/MapFeatureToControls.md

> **Read [`../SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** This workflow
> helps you draft a compliance-matrix row for a feature. Drafts require
> human review before being used in an authorisation package.

## When to use this workflow

Use this when:

- A new feature has landed or is landing that has security, audit,
  access-control, or cryptographic implications.
- You are backfilling a compliance matrix for an existing codebase.
- A PR review raises "which controls does this satisfy?" and you need
  an answer with citations.

Do **not** use this for:

- General code review (use `/security-review`).
- Changes that are purely UX / cosmetic / documentation.
- Changes to test-only code that does not touch production crypto or
  authz paths.

---

## Procedure

### Step 1 — Classify the feature by domain

Identify the primary domain of the change. Use the domain → family hint
table below to narrow the control-family search space:

| Domain hint | Likely control families (800-53) |
|---|---|
| Authentication, login, MFA, password policy, SSO | IA (primary); AC-7, AC-11, AC-12 |
| Authorisation, RBAC, ABAC, ACL, permission engine | AC |
| Audit logging, log pipeline, SIEM integration, log retention | AU |
| Cryptography: TLS, KMS, JWT, hashing, signing, encryption | SC (primary); IA-5, IA-7 |
| Network boundaries, firewalls, ingress/egress policy, segmentation | SC-7 (boundary protection) |
| Data-at-rest encryption, envelope encryption | SC-28 (+ SC-13) |
| Data-in-transit, TLS config, cipher suites | SC-8 (+ SC-13) |
| Session management, session timeout, session revocation | AC-11, AC-12 |
| Input validation, SSRF protection, SQL-injection guards | SI-10 |
| Error handling, audit-log integration | SI-11, AU family |
| Account lifecycle (create / disable / delete) | AC-2 |
| Incident response, alerting | IR (+ SI-4, SI-5 — v0.2+) |
| Backup, DR, continuity | CP (v0.2+) |
| Supply chain, dependency audit, SBOM | SR, SI-7 (v0.2+) |

Usually a feature touches 2–4 controls. Rarely one, occasionally more.

### Step 2 — Cross-reference the control data

For each candidate control:

1. Read the relevant family section in
   [`../context/NistControlCatalogue.md`](../context/NistControlCatalogue.md).
   The OSCAL **statement** and **guidance** fields are authoritative text.
2. Read the control's row in
   [`../context/FrameworkCrossMap.md`](../context/FrameworkCrossMap.md)
   to check whether it's required at your target baseline (FedRAMP
   Low/Mod/High, CMMC L2, etc.).
3. If the control has **organisation-defined parameters** (ODPs), note
   them. The matrix row must record your org's values for each ODP.

### Step 3 — Determine status (PASS / PARTIAL / PLANNED / NA)

For each candidate control:

- **PASS** — the feature fully implements the control at the targeted
  baseline. At least one concrete evidence pointer (file:line).
- **PARTIAL** — feature implements some aspects but not all. Compensating
  controls or POAM entries should be documented.
- **PLANNED** — feature does not yet implement this control; a scheduled
  implementation plan exists.
- **NA** — the control does not apply to your scope
  (e.g., PE Physical Protection for a pure cloud service).

### Step 4 — Draft the matrix row

Use this template (matches `templates/compliance-matrix.md`):

```markdown
| Control ID | Title | Status | Rationale | Evidence Pointers | Responsibility | ODP Values |
|---|---|---|---|---|---|---|
| IA-2(1) | MFA for Privileged | PASS | TOTP + WebAuthn required for Admin/SuperAdmin roles at login | backend/crates/securedrop-api/src/routes/sessions.rs:142; tests/integration/test_mfa.rs:88 | customer | n/a |
| IA-5(1) | Password Policy | PARTIAL | 12+ chars / complexity enforced; blacklist check enforced; **breach-database check not yet implemented** | backend/crates/securedrop-auth/src/password.rs:22 | customer | min_length=12; complexity=upper+lower+digit+symbol |
```

- **Status** must be one of the four values.
- **Rationale** is 1–2 sentences of prose. No marketing language. No
  endorsement-implying claims (the
  `validate-skill.py` denylist applies here too when the matrix is in-repo).
- **Evidence Pointers** must follow the `PATH:LINE` format (see
  `EvidenceModel.md`). For a PASS status, **at least one pointer is
  mandatory.**
- **Responsibility** is `customer`, `shared`, `provider`, or `not-applicable`.
- **ODP Values** list your org's values for each parameter (e.g.,
  AC-7 `max_failed_attempts = 5`; `lockout_duration = 30min`).

### Step 5 — Handle parameters explicitly

Each ODP you encountered in Step 2 must be filled in. `data/nist-800-53-rev5.json`
lists the parameter IDs. Examples from AC family:

- AC-2 `ac-02_odp.04` — personnel or roles to review accounts
- AC-7 `ac-07_odp.01` — number of consecutive invalid login attempts
- AC-7 `ac-07_odp.02` — period of time
- AC-11 `ac-11_odp.01` — period of inactivity

Unspecified ODPs are the #1 cause of assessor findings. Fill them in
explicitly.

### Step 6 — Check framework applicability

Open `data/framework-crossmap.json`. For each control ID:

- If your target is FedRAMP Moderate and the row says `fedramp_moderate: true`
  — in scope, row is required.
- If it says `false` — not required at that baseline; can be omitted (or
  kept with `NA` status for completeness).
- If CMMC L2 / HIPAA / SOC 2 columns show `TODO`, those cross-maps are
  not in v0.1 — consult your assessor.

### Step 7 — If PARTIAL or PLANNED, create a POAM entry

Follow [`HandleControlGap.md`](HandleControlGap.md) (v0.2+). In v0.1 the
minimum is a matrix cell in `Rationale` stating:

```
PARTIAL — breach-database check not yet implemented. Compensating
control: rate-limit + lockout (AC-7). Target: Q3 2026.
```

### Step 8 — Commit

- Update the matrix file (`Documentation/compliance/compliance-matrix.md`
  or equivalent in your repo).
- Bump `last_updated` in its YAML header.
- Include the commit in the feature PR, not a separate PR — matrix drift
  and feature drift should stay in sync.

---

## Worked examples

### Example 1 — New authentication feature

**Feature**: Add WebAuthn / passkey support to `/login`.

**Classification**: Authentication → IA family.

**Candidate controls**:

- **IA-2** — base authentication. Already PASS in existing matrix.
- **IA-2(1)** MFA for Privileged — WebAuthn satisfies as a second
  factor. Update status if this is the first hardware-bound factor.
- **IA-2(8)** Replay-Resistant Authentication — WebAuthn's
  challenge-response satisfies.
- **IA-5** Authenticator Management — new authenticator type; add to
  the authenticator lifecycle procedure.
- **IA-7** Cryptographic Module Authentication — WebAuthn's
  cryptographic operations must go through a FIPS-validated module.
  Cross-reference `/fips-audit` output.

**Evidence pointers** (illustrative):

```
IA-2(8) | replay-resistance | backend/crates/securedrop-webauthn/src/ceremony.rs:44 | Challenge validated before signature check
IA-5    | authenticator-lifecycle | backend/crates/securedrop-api/src/routes/mfa.rs:201 | /mfa/webauthn/credentials CRUD
IA-7    | fips-module | backend/Cargo.toml:87 | aws-lc-rs fips feature (CMVP #4816)
```

### Example 2 — New audit-log field

**Feature**: Add `trace_id` to every audit event.

**Classification**: Logging → AU family.

**Candidate controls**:

- **AU-3** Content of Audit Records — `trace_id` extends the required
  content. Update rationale with the new field.
- **AU-3(1)** Additional Information — the `trace_id` is organisation-
  defined additional information. Record the ODP value.
- **AU-12** Audit Generation — no change; same generator.

**Evidence pointers**:

```
AU-3 | log-schema | backend/crates/securedrop-audit/src/event.rs:42 | AuditEvent struct now includes trace_id
AU-3(1) | odp-value | Documentation/compliance/compliance-matrix.md | trace_id added to additional_information list
```

### Example 3 — TLS cipher suite change

**Feature**: Remove `TLS_CHACHA20_POLY1305_SHA256` from the allowed cipher
suite list.

**Classification**: TLS → SC family.

**Candidate controls**:

- **SC-8** Transmission Confidentiality and Integrity — TLS policy
  change. Status likely already PASS; update rationale.
- **SC-8(1)** Cryptographic Protection — must use FIPS-approved
  algorithms. Removing ChaCha20 strengthens compliance.
- **SC-13(2)** FIPS-Validated Cryptography — audit that only approved
  suites remain.

**Evidence pointers**:

```
SC-8(1) | cipher-suite-list | backend/src/tls.rs:18 | Only TLS_AES_128_GCM_SHA256 and TLS_AES_256_GCM_SHA384
SC-13(2) | fips-module | backend/Cargo.toml:87 | rustls with fips provider; config.fips() asserted at startup
```

---

## Common mistakes

1. **Guessing at control IDs** without opening
   `NistControlCatalogue.md`. Always check the OSCAL statement before
   claiming a control applies.
2. **Skipping enhancements.** `IA-2(1)`, `SC-13(2)`, `AU-3(1)` etc. are
   the specific commitments. Saying "IA-2 PASS" without specifying which
   enhancements is insufficient at FedRAMP Moderate and above.
3. **Forgetting ODPs.** Every assessor will ask "what is your lockout
   duration?" — have the answer in the matrix row.
4. **Claiming PASS without evidence pointers.** A claim without a
   file:line pointer is not a compliance claim, it's a hope.
5. **Using endorsement language.** "NIST-approved", "FedRAMP-ready",
   "FIPS-certified" applied to the feature — all of these will be
   rejected by `validate-skill.py` and, more importantly, will
   invite scrutiny from an assessor.
