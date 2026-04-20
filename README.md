# NistFipsCompliance

> A Claude Code skill that helps engineering teams map features to **NIST SP
> 800-53 Rev 5** security controls and enforce **FIPS 140-3** cryptographic
> requirements at the code-review and edit-time level.

---

## LEGAL NOTICE — READ BEFORE USE

**This skill is an independent, unaffiliated, individual-maintainer project.**

- **Not produced, endorsed, validated, or certified by** NIST, the CMVP (Cryptographic Module Validation Program), the FedRAMP PMO, GSA, the DoD CIO, HHS/OCR, AICPA, or Anthropic PBC.
- **Names used descriptively only**: "NIST", "FIPS", "FedRAMP", "CMMC", "HIPAA", and "SOC 2" appear as references to the public standards and frameworks they name. FedRAMP is a registered mark of GSA; CMMC is administered by the DoD CIO. This skill makes no claim to those marks.
- **Does not confer FIPS validation.** FIPS 140-3 validation is granted only by the CMVP to specific cryptographic modules. This skill helps you *use* a validated module correctly — it does not validate anything itself.
- **Does not replace a human audit.** Generated matrices, SSP sections, evidence checklists, and POAMs are **drafts for human review only**. Every generated artefact carries a `DRAFT — UNREVIEWED — NOT FOR SUBMISSION` watermark. Do not submit any generated artefact to a 3PAO, assessor, or regulator without human review and watermark removal.
- **No formal legal review has been performed on this project.** Disclaimers and non-bypassable watermarking are the risk mitigation. Organisations with regulated authorisation exposure should conduct their own legal review before use.
- **No warranty.** Provided AS-IS under Apache License 2.0. See `LICENSE`.
- **Export control.** This repository contains cryptography-related guidance that is publicly available. Publication is consistent with EAR §740.13(e) TSU ("publicly available technology and software"). You are responsible for compliance with your own jurisdiction's export laws.
- **Known limitations.** English only. US-framework-centric: ANSSI (France), BSI (Germany), ISMAP (Japan), ENS (Spain), ISO 27001, and other non-US regimes are out of scope.

If you are not comfortable with these terms, do not install this skill.

---

## What it does

| You can… | Using |
|---|---|
| Ask "what controls does this PR satisfy?" | The `compliance-auditor` subagent reads the full NIST SP 800-53 Rev 5 catalogue as context |
| Ask "is ChaCha20-Poly1305 FIPS-approved?" | The `FipsAlgorithms.md` allow/deny reference, sourced from FIPS 140-3 IG, SP 800-131A, SP 800-57 Pt 1 |
| Ask "which FIPS-certified crypto library for Rust/Go/Python?" | The `FipsLibraries.md` per-language CMVP cross-reference |
| Bootstrap a compliance matrix for a new repo | `/nist-scan --framework fedramp-moderate` |
| Audit an existing codebase for non-FIPS crypto | `/fips-audit` |
| Generate a draft SSP section for a single control | `/ssp-section AC-2` (v0.4+, always watermarked) |

## What it explicitly does NOT do

- Validate cryptographic modules (that's CMVP's job).
- Replace a human audit or a 3PAO assessment.
- Generate submission-ready authorisation-package content without human review.
- Cover NIST CSF 2.0 (different framework — see [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)).
- Cover NIST SP 800-171/172, SP 800-63, SP 800-37 RMF, or NIST AI RMF.
- Do generic SAST — use [`anthropics/claude-code-security-review`](https://github.com/anthropics/claude-code-security-review) for that.

---

## Installation

Three install paths:

### 1. Local skill (recommended for individual developers)

```bash
cd ~/.claude/skills  # or your project's .claude/skills/ directory
git clone https://github.com/rob-linton/claude-skill-nist-fips NistFipsCompliance
cd NistFipsCompliance
# Optional: verify the release signature if installing from a tag
./tools/verify-release.sh
```

Claude Code picks the skill up the next time it starts. Trigger it by asking
questions about NIST 800-53, FIPS 140-3, FedRAMP, CMMC, HIPAA, or SOC 2
compliance, or by running one of the `/` commands listed above.

### 2. Claude Code plugin (recommended — registers slash commands)

Install as a proper Claude Code plugin so `/fips-audit`, `/nist-scan`, and the
`fips-crypto-reviewer` subagent register as first-class harness entities.
Dropping the files into `.claude/skills/` alone **does not** register the
slash commands — the harness only reads slash commands from `.claude/commands/`
or from installed plugin caches.

**Via a local marketplace** (works for vendored installs inside a repo):

1. Place the skill at `<repo>/.claude/skills/NistFipsCompliance/` (or anywhere
   you like — the path just has to be reachable by a marketplace entry).

2. Create `<repo>/.claude/plugin-marketplace/.claude-plugin/marketplace.json`:

   ```json
   {
     "name": "my-local",
     "owner": { "name": "You", "email": "you@example.com" },
     "metadata": { "version": "1.0.0", "description": "Local plugins" },
     "plugins": [
       {
         "name": "nist-fips-compliance",
         "version": "0.1.0",
         "description": "NIST SP 800-53 + FIPS 140-3 compliance skill",
         "source": "./plugins/nist-fips-compliance"
       }
     ]
   }
   ```

   Plugin `source` paths are resolved relative to the marketplace root (the
   directory **containing** `.claude-plugin/`) and **cannot** traverse upward
   with `..`. If the skill lives outside the marketplace directory, create a
   symlink inside the marketplace:

   ```bash
   mkdir -p <repo>/.claude/plugin-marketplace/plugins
   ln -s ../../skills/NistFipsCompliance \
     <repo>/.claude/plugin-marketplace/plugins/nist-fips-compliance
   ```

3. Validate, register, and install:

   ```bash
   claude plugin validate <repo>/.claude/plugin-marketplace
   claude plugin marketplace add <repo>/.claude/plugin-marketplace
   claude plugin install nist-fips-compliance@my-local
   ```

4. **Restart Claude Code** — slash commands and subagents from newly
   installed plugins are only registered on harness startup. After restart,
   tab-completing `/fips-` will reveal `/fips-audit`.

**Plugin manifest schema requirements.** Claude Code's installer validates
`.claude-plugin/plugin.json` with a strict schema: `name`, `description`,
`author`, plus optional `version`, `license`, `repository` (string URL —
**not** an object), `homepage`, `keywords`. Additional keys (`$schema`,
`skill`, `features`, `requirements`, etc.) are rejected. The manifest
shipped in this repo is kept minimal to stay compatible; richer metadata
lives in the marketplace.json entry instead.

**Via direct GitHub install** (if your Claude Code version supports it):

```bash
claude plugin marketplace add github:rob-linton/claude-skill-nist-fips
claude plugin install nist-fips-compliance@claude-skill-nist-fips
```

Submission to the Anthropic marketplace is not assumed. Community
marketplaces ([`buildwithclaude.com`](https://buildwithclaude.com/),
[awesomeclaude.ai](https://awesomeclaude.ai/)) are best-effort channels.

### 3. GitHub Action (CI-only, no Claude dependency)

```yaml
- uses: rob-linton/claude-skill-nist-fips/action@v0
  with:
    framework: fedramp-moderate
    mode: audit    # audit | scan | matrix
```

The Action runs the scanning tools against the repo under test and emits a
compliance report. No API keys required — it does not call Claude.

---

## Project status

| Version | Status | Scope |
|---|---|---|
| v0.1 | In development | Core skeleton: NIST catalogue (AC/AU/IA/SC families), FIPS algorithm + library refs (Rust/Go/Python), two workflows, two commands, one subagent, five test fixtures |
| v0.2 | Planned | Remaining 16 NIST families, monorepo support, Go-binary hooks, full fixture set |
| v0.3 | Planned | All framework cross-maps, remaining language guides, ODP + inheritance modelling |
| v0.4 | Planned | SSP/POAM generator with non-bypassable watermarking |
| v1.0 | Planned | External-expert review feedback incorporated, blog launch |

Maintainer: Rob Linton (individually). See [`MAINTENANCE.md`](MAINTENANCE.md)
for the bus-factor-1 policy, succession clause, and unmaintained-banner
auto-triggers.

---

## Repository layout

```
.
├── .claude-plugin/plugin.json          # skill manifest
├── SKILL.md                            # routing hub
├── context/                            # reference material
├── workflows/                          # step-by-step procedures
├── commands/                           # slash commands
├── agents/                             # subagent definitions
├── data/                               # machine-readable catalogues
├── tools/                              # build, validate, test tooling
│   ├── build-data.py                   # regenerate data/*.json from sources
│   ├── validate-skill.py               # disclaimer + watermark + denylist CI
│   └── fixtures/                       # ground-truth test repos
├── tests/                              # pytest suite
└── docs/                               # install, usage, customising
```

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). In short: PRs touching `data/*.json`
must cite the authoritative source (NIST OSCAL, FIPS publication, FedRAMP PMO
spreadsheet, etc.) in the commit message. PRs that introduce
endorsement-implying prose will fail the `validate-skill.py` CI check.

## Security

See [`SECURITY.md`](SECURITY.md) for the vulnerability-disclosure policy.

## License

Apache License 2.0 — see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
