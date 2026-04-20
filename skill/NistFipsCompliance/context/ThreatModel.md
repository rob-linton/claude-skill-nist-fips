# ThreatModel.md

> **Read [`SKILL.md`](../SKILL.md) §LEGAL NOTICE first.**

STRIDE analysis of the **skill itself** — the artefact you are reading. A
skill that tells Claude what crypto is FIPS-approved *must* consider the
supply-chain threat of that guidance being tampered with or spoofed.

---

## Why model the threat to the skill?

This skill is loaded into Claude's context and treated as authoritative by
downstream users working under regulated compliance regimes. If an
attacker can:

- publish a lookalike skill,
- persuade a user to install a tampered copy,
- merge a malicious PR to `data/*.json`,
- or embed prompt-injection strings in control discussions,

then downstream users may inherit false compliance claims at real
regulatory cost. The defences below are in response to those threats.

---

## STRIDE

### Spoofing

**Threat**: A malicious actor publishes `NistFipsCompliance-pro` or
`NistFipsCompliance2` with subtly altered rules, relying on name
collision or typosquatting.

**Mitigations**:

- Release artefacts signed with Sigstore (cosign) using the primary
  maintainer's GitHub OIDC identity.
- `plugin.json` carries a SHA-256 hash of the release tarball.
- `README.md` LEGAL NOTICE and `MAINTENANCE.md` specify the canonical
  repo URL and GPG fingerprint.
- `tools/verify-release.sh` (ships with the repo) validates signature
  + hash on install.
- Users are instructed (in installation docs) to verify the repo URL
  matches the canonical one.

**Residual risk**: Typosquatting on community marketplaces outside the
maintainer's control. Partially mitigated by the LEGAL NOTICE being
reproduced verbatim in SKILL.md (any typosquat that removes it loses
credibility on inspection).

### Tampering

**Threat**: Malicious PR to `data/nist-800-53-rev5.json`,
`data/fips-algorithms.json`, etc. Attacker flips a `DISALLOWED` entry to
`APPROVED`, or embeds a prompt-injection string in a control discussion.

**Mitigations**:

- `tools/build-data.py` rejects prompt-injection-style strings in any
  human-readable field (denylist: `ignore previous`, `you are now`,
  instruction-like phrasing).
- Schema validation enforces shape and value-set constraints.
- `tools/build-data.py` pulls NIST OSCAL from the upstream canonical
  source on every build; diff against committed data surfaces
  unexplained edits.
- Every `data/*.json` row has a `source` field with an authoritative
  URL; CI rejects rows without a source.
- Branch-protection rules (required review, required signatures) on
  the canonical repo.
- Release SHA-256 manifests published with each tag; downstream users
  can verify what they have matches what was released.

**Residual risk**: Social-engineering a reviewer into merging a
plausible-looking PR that shifts an edge-case rule. Mitigated by the
data/prose drift test: `NistControlCatalogue.md` is generated from
`data/nist-800-53-rev5.json`, so tampering with the data causes visible
diffs in the human-readable prose on every build — review burden is
redirected to the diff.

### Repudiation

**Threat**: A contributor commits a malicious change and later denies
authorship. Or the maintainer's account is compromised and the
compromise is disputed.

**Mitigations**:

- All commits must be signed (GPG or Sigstore).
- Release tags are signed.
- Maintainer's GitHub account has 2FA mandatory.
- Audit trail of all `data/*.json` changes visible via `git log`.

**Residual risk**: Signed commits do not prove the signer's intent — a
signing key could still be compromised without the owner's knowledge.
Mitigated by revocation + rotation procedures documented in
`MAINTENANCE.md`.

### Information disclosure

**Threat**: Skill hooks exfiltrate local source code or secrets via
network calls.

**Mitigations**:

- Hooks do not make network calls at all. Enforced by:
  - `tests/test_hooks.py` runs hooks under `strace -f -e trace=network`
    and fails on any socket syscall.
  - Hooks ship as Go static binaries with no net/http linkage.
- Hooks do not write outside the repo root. Enforced by:
  - `strace -f -e trace=openat` test.
  - Hooks use only relative paths from the policy-config root.
- Hooks do not emit telemetry.

**Residual risk**: If the primary maintainer's release pipeline is
compromised, a malicious version could include an exfiltrating binary.
Mitigated by reproducible builds (Go) and binary hash publication.

### Denial of service

**Threat**: Hook takes too long, blocking edits or causing developer
frustration; or malicious `fips-policy.yaml` with a catastrophic regex
makes the hook hang.

**Mitigations**:

- Hooks have a 2-second soft timeout. On timeout, the hook exits
  cleanly with a "hook skipped" notice rather than blocking the edit.
- Regex input is length-limited and pre-validated; patterns with
  catastrophic-backtracking risk are rejected by schema.
- Tree-sitter AST parsing is used for languages where available;
  regex fallback is used only for quick-and-dirty pattern matching
  with conservative timeouts per pattern.

**Residual risk**: A sufficiently large diff could still exceed the
2-second budget. Mitigated by diff chunking — hooks process per-edit,
not per-batch.

### Elevation of privilege

**Threat**: Hooks execute arbitrary code through a crafted
`fips-policy.yaml` or malicious data file.

**Mitigations**:

- YAML parsing uses safe-load only (no Python object instantiation).
- JSON parsing is stdlib-only with no custom decoders.
- Hooks do not invoke a shell; all command invocations (when AST
  parser is available) go through explicit argv arrays without
  shell interpretation.
- `tests/test_hooks.py` attempts a known privilege-escalation payload
  and asserts the hook rejects it.

**Residual risk**: A 0-day in the Go runtime or Tree-sitter grammar.
Mitigated by depending on recent stable versions and by the hooks
having no elevated privileges themselves — they inherit the
developer's normal permissions.

---

## Threat model of users of this skill

Two adversary models worth separating:

### Adversary A — External attacker

Wants to get compromised code into the downstream user's repo by
manipulating the skill. All the STRIDE mitigations above address this.

### Adversary B — Insider / sloppy developer

Wants the hook to pass so they can merge a PR that uses non-FIPS crypto.

**Mitigations**:

- `disallowed_hardcoded` rules cannot be overridden by local
  `fips-policy.yaml` exceptions.
- `exceptions[]` entries in `fips-policy.yaml` require a reason, an
  expiry date, and an approver email — surfaces in code review.
- Hook output goes to Claude which can push back; also appears in the
  PR review channel.
- `/fips-audit` can be run in CI regardless of local-hook state — the
  CI run is the authoritative enforcement surface.

---

## Non-mitigated risks (accepted)

These are risks we do **not** mitigate in the current design and that
users should be aware of:

1. **Claude hallucination** as a substitute for reading the data files.
   The skill reduces hallucination by grounding Claude in the data
   files, but does not eliminate it. Watermarking on generated
   artefacts is the mitigation at the *output* layer; LEGAL NOTICE is
   the mitigation at the *trust* layer.
2. **Stale data**. The maintainer could be unavailable and the
   monthly OSCAL refresh could fail. The `MAINTENANCE.md` staleness
   policy surfaces this with a banner, but the data can still be
   stale for weeks or months before the 180-day unmaintained banner
   fires.
3. **Individual-maintainer bus factor**. See `MAINTENANCE.md` Bus
   Factor 1 policy.
4. **Downstream misuse**. A user who removes watermarks and submits
   an unreviewed SSP section to a regulator has defeated the
   protection mechanism. The skill's defence is making this
   deliberate (human action, friction-ful) rather than automatic.
