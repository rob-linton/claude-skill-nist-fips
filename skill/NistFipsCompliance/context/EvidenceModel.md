# EvidenceModel.md

> **Read [`SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** This file describes
> what kinds of evidence *typically* satisfy a control during an audit. What
> a specific assessor actually accepts depends on the framework, the
> authorisation boundary, and the assessor. Treat this as guidance, not
> law.

For each control family, what artefacts constitute audit-grade evidence,
and — where possible — how to auto-locate them in the codebase.

---

## Why this file exists

When the skill generates a compliance matrix row or an SSP section, every
claim must have at least one **evidence pointer**: a file path, a line
number, a config file, an audit-log sample, a configuration export, etc.
This file is the checklist of what counts.

The `/evidence <control-id>` command (v0.2+) uses the "auto-extract?" hints
below to try to locate evidence in the repo automatically.

---

## Access Control (AC)

| Control | Typical evidence | Auto-extract? |
|---|---|---|
| AC-2 Account Management | User creation / deletion SOP; IAM config export; account-lifecycle audit log sample | Partial — locate IAM/RBAC code paths |
| AC-3 Access Enforcement | ACL model implementation; authorisation middleware; policy engine | Yes — grep for `authz`, `rbac`, `abac`, `policy` modules |
| AC-5 Separation of Duties | Role matrix documenting mutually-exclusive duties | No |
| AC-6 Least Privilege | RBAC role definitions showing minimum permissions; review of default-deny posture | Yes — locate role/permission configs |
| AC-6(1) Authorise Access to Security Functions | Admin-only route enforcement | Yes — grep for admin-role guards |
| AC-7 Unsuccessful Login Attempts | Account lockout config (threshold, lock duration) | Yes — locate `lockout`, `failed_login_attempts`, `max_attempts` |
| AC-11 Session Lock | Session timeout config | Yes — locate session/JWT TTL |
| AC-12 Session Termination | Logout endpoint; session revocation mechanism | Yes — `/logout`, revocation store (Redis keys) |
| AC-17 Remote Access | VPN config; bastion host config; mutual-TLS config | Partial — CI/CD configs |

---

## Audit and Accountability (AU)

| Control | Typical evidence | Auto-extract? |
|---|---|---|
| AU-2 Event Logging | List of auditable events with audit-log schema | Yes — locate audit-event enum / types |
| AU-3 Content of Audit Records | Log record schema showing: timestamp, event_type, user_id, session_id, source_ip, result | Yes — grep for log schema definitions |
| AU-4 Audit Storage Capacity | Log volume estimate; storage capacity config; rotation policy | Partial — locate log-rotation config |
| AU-5 Response to Audit Logging Process Failures | Alerting on log-pipeline failures; disk-full behaviour | Partial — SI-4 monitoring overlap |
| AU-6 Audit Review, Analysis, and Reporting | SIEM config; log query examples; review cadence | No (operational) |
| AU-7 Audit Record Reduction and Report Generation | Log-aggregation tooling config (ELK, Splunk, Loki) | No (operational) |
| AU-8 Time Stamps | NTP config; timezone policy (UTC) | Yes — locate time-source config |
| AU-9 Protection of Audit Information | Log integrity (hash chain, WORM, signing); access controls on log store | Yes — locate integrity code |
| AU-10 Non-Repudiation | Signed log entries or hash chain | Yes — locate signature/hash code |
| AU-11 Audit Record Retention | Retention period config; archival procedure | Partial — locate retention config |
| AU-12 Audit Generation | Instrumentation coverage (every auditable event emits a record) | Yes — emission-site inventory |

---

## Identification and Authentication (IA)

| Control | Typical evidence | Auto-extract? |
|---|---|---|
| IA-2 Identification and Authentication (organizational users) | Authentication module (login flow, MFA integration) | Yes — locate login handler |
| IA-2(1) MFA for Privileged Accounts | MFA enforcement for admin roles | Yes — locate admin MFA guard |
| IA-2(2) MFA for Non-Privileged Accounts | MFA enforcement for all users | Yes — same |
| IA-2(8) Replay-Resistant Authentication | Use of nonces, challenges, TOTP time-windowing, WebAuthn | Yes — locate MFA implementation |
| IA-4 Identifier Management | User-ID lifecycle (create / assign / retire); no reuse | Partial |
| IA-5 Authenticator Management | Password policy; password hashing algo + iterations; recovery flow | Yes — locate password policy config + hash function |
| IA-5(1) Password-Based Authentication | Password policy config; complexity rules; blacklist check | Yes — password validator |
| IA-7 Cryptographic Module Authentication | Use of FIPS-validated module for authentication crypto | Yes — overlaps with FIPS audit |
| IA-8 Identification and Authentication (non-organizational users) | Federated SSO config (SAML/OIDC) | Yes — locate SSO module |

---

## System and Communications Protection (SC)

| Control | Typical evidence | Auto-extract? |
|---|---|---|
| SC-7 Boundary Protection | Network ACL / firewall config; ingress/egress rules | Partial — K8s NetworkPolicy, infra-as-code |
| SC-8 Transmission Confidentiality and Integrity | TLS config; allowed cipher suites; minimum TLS version | Yes — TLS config |
| SC-8(1) Cryptographic Protection | FIPS-validated TLS module; algorithm allow-list | Yes — FIPS audit overlap |
| SC-12 Cryptographic Key Establishment and Management | KMS config; key lifecycle; rotation frequency; envelope encryption | Yes — locate KMS code |
| SC-12(3) Asymmetric Keys | Key generation via validated DRBG; key-size policy | Yes — locate key-gen code |
| SC-13 Cryptographic Protection | Approved-algorithm list; FIPS-module assertion at startup | Yes — FIPS audit overlap |
| SC-13(2) FIPS-Validated or NSA-Approved Cryptography | CMVP cert number; active status | Yes — locate aws-lc-rs features, openssl providers, etc. |
| SC-17 Public Key Infrastructure Certificates | Certificate issuance policy; rotation procedure | Partial |
| SC-23 Session Authenticity | Session-binding to auth factors; anti-fixation | Yes — session management |
| SC-28 Protection of Information at Rest | Disk encryption, database encryption, envelope encryption | Yes — locate encryption-at-rest code |
| SC-28(1) Cryptographic Protection | FIPS-validated AES-256 at rest | Yes — FIPS audit overlap |

---

## System and Information Integrity (SI)

| Control | Typical evidence | Auto-extract? |
|---|---|---|
| SI-2 Flaw Remediation | Patching cadence; dependency update policy; CVE tracking | Partial — look at Dependabot / Renovate config |
| SI-3 Malicious Code Protection | Antivirus / endpoint-detection config | No (infra) |
| SI-4 System Monitoring | IDS/IPS config; log-pipeline monitoring; alerting rules | Yes — locate monitoring config |
| SI-5 Security Alerts, Advisories, and Directives | Subscription to advisories; triage process | No (operational) |
| SI-7 Software, Firmware, and Information Integrity | SBOM; integrity scanning; signed releases | Yes — locate SBOM workflow |
| SI-10 Information Input Validation | Input validation at API boundaries; SSRF protection; SQL-injection guards | Yes — locate validation code |
| SI-11 Error Handling | Error-handling policy (no info disclosure); error-log integration | Yes — locate error-handling middleware |

---

## Other families (v0.2+ full treatment)

| Family | Scope |
|---|---|
| AT | Awareness and Training — policy/SOP evidence, mostly non-technical |
| CA | Assessment, Authorization, and Monitoring — SSP, continuous-monitoring reports |
| CM | Configuration Management — baseline configs, change-management workflow |
| CP | Contingency Planning — backup/DR procedures, testing reports |
| IR | Incident Response — IR plan, runbooks, tabletop exercise logs |
| MA | Maintenance — patch logs, hardware maintenance records |
| MP | Media Protection — data-destruction SOP, media inventory |
| PE | Physical and Environmental Protection — facility access logs |
| PL | Planning — SSP, privacy-impact assessments |
| PM | Program Management — organisational, usually non-technical |
| PS | Personnel Security — background checks, role-based clearance |
| PT | PII Processing and Transparency — privacy notices, data-minimisation |
| RA | Risk Assessment — SAR, risk register |
| SA | System and Services Acquisition — SDLC policy, supply-chain due diligence |
| SR | Supply Chain Risk Management — SBOM, signed releases, vendor vetting |

v0.2 adds per-family detailed evidence tables following the pattern above.

---

## Cross-cutting: FIPS-grounded evidence

Any SC-12, SC-13, SC-28, IA-5, or IA-7 evidence that *claims FIPS coverage*
must satisfy **all** of the following before it counts as evidence:

1. Code uses a CMVP-validated cryptographic module (see
   `FipsLibraries.md`).
2. Module is in FIPS mode at runtime (startup assertion present).
3. Algorithm used is on the `APPROVED` list in `FipsAlgorithms.md`.
4. CMVP certificate is Active on the day of the audit (re-verified per
   `MAINTENANCE.md` data-refresh policy).

Failing any of (1)–(4) means the evidence is incomplete. The compliance
matrix row cannot be marked `PASS`; it must be `PARTIAL` with a POAM
entry.

---

## Evidence pointer format

When a workflow or command produces an evidence claim, the pointer format
is:

```
CONTROL_ID | EVIDENCE_TYPE | FILE_PATH[:LINE] | BRIEF_NOTE
```

Examples:

```
AU-3 | log-schema | backend/crates/securedrop-audit/src/event.rs:42 | AuditEvent struct with all required fields
IA-5 | password-hash | backend/crates/securedrop-auth/src/password.rs:88 | PBKDF2-HMAC-SHA-256 with 600,000 iterations
SC-13 | crypto-module | backend/Cargo.toml:87 | aws-lc-rs with fips feature enabled
SC-13 | startup-assertion | backend/src/main.rs:24 | default_fips_provider().install_default()
```

This format is enforced by the generator: every row in a generated matrix
and every paragraph in a generated SSP section must carry at least one
pointer in this shape.
