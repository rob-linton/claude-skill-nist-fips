# SECURITY.md

Vulnerability disclosure policy for NistFipsCompliance.

---

## Supported versions

Security fixes are provided for the latest minor release only (e.g., if
`v0.3.2` is current, `v0.3.x` receives fixes; `v0.2.x` does not).

The `rev5` long-term maintenance branch (tracking NIST SP 800-53 Rev 5 after
Rev 6 launches, per [`MAINTENANCE.md`](MAINTENANCE.md)) also receives
security fixes for 24 months after Rev 6 publication.

---

## How to report a vulnerability

**Preferred**: GitHub private vulnerability reporting.

1. Go to this repository's `Security` tab.
2. Click `Report a vulnerability`.
3. Describe the issue in the confidential advisory form.

**Alternative**: email `rob.linton@senetas.com` with the subject line
`[SECURITY] NistFipsCompliance <short description>`. For encrypted
communication, see the maintainer's public key on keys.openpgp.org under
that email address.

---

## What counts as a vulnerability

High / critical:

- **Injection / escape of guard rails**: A way to get the skill's hook
  binary to skip a check it should not skip, or to persuade Claude (via
  crafted `data/*.json` content) to approve a cryptographic algorithm the
  skill should deny.
- **Prompt injection via data files**: Any string in `data/*.json` that
  causes Claude to override its rules when the skill is loaded.
- **Tampering resistance**: Any way a malicious `fips-policy.yaml` can
  suppress a `disallowed_hardcoded` rule (e.g., MD5 for signing).
- **Watermark bypass**: Any way to produce SSP/POAM/matrix output from
  the skill without the mandatory `DRAFT — UNREVIEWED — NOT FOR
  SUBMISSION` watermark.
- **Hook exfiltration**: Any hook behaviour that opens a network socket,
  sends telemetry, or writes outside the repo root.
- **Supply-chain**: Typosquatted marketplace entries, malicious PRs to
  data files, etc.

Medium:

- **False negatives**: An approved-list entry that should be disallowed
  (e.g., a newly-deprecated algorithm missed in a refresh). Please report
  with a citation to the authoritative NIST/FedRAMP/CMMC source.
- **Stale CMVP certificate claims**: Certificate numbers in
  `FipsLibraries.md` that have expired without notation.

Low:

- **False positives** on AST-high-confidence detections. (Regex-based
  detection false positives are expected — report them as regular issues,
  not security issues.)
- **Documentation errors** that do not affect enforcement behaviour.

---

## Not in scope

- **Claude hallucination itself.** The skill mitigates hallucination
  through grounding in authoritative data and watermarking of generated
  artefacts. Residual hallucination is a known, disclosed risk; see the
  LEGAL NOTICE in `README.md`. Reports that Claude produced incorrect
  compliance prose in some interaction are not security vulnerabilities
  of this skill — they are limitations of language models.
- **Generic Claude Code CLI vulnerabilities** unrelated to this skill.
  Report those upstream to Anthropic.
- **Disagreements about non-US compliance frameworks.** These are out of
  scope per `MAINTENANCE.md`.

---

## Response timeline (best-effort, single maintainer)

| Stage | Target |
|---|---|
| Initial acknowledgement | 5 business days |
| Triage decision (in scope / out of scope / duplicate) | 10 business days |
| Fix for critical vulnerabilities | 30 days |
| Fix for high vulnerabilities | 60 days |
| Fix for medium vulnerabilities | 90 days |
| Public disclosure after fix | Coordinated, typically 7 days post-release |

Per the bus-factor-1 policy, these are targets — not guarantees. If the
maintainer is unavailable, the above schedule may slip. Users with
production reliance on timely security fixes should consider this when
adopting the skill.

---

## Acknowledgements

Vulnerability reporters will be credited in `CHANGELOG.md` with their
consent. Credit can be under a real name, a handle, or anonymous — your
choice.

No bug bounty is offered. This is an unfunded individual-maintainer
project.
