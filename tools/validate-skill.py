#!/usr/bin/env python3
"""
validate-skill.py — CI-enforced invariants for NistFipsCompliance.

This script implements the non-bypassable protections that substitute for
a formal legal review (per the project's release-gate policy):

  1. SKILL.md, README.md, and every file under the skill directory
     must contain a LEGAL NOTICE (or clearly delegate to the README's one).
  2. Endorsement-implying language (regex denylist) is rejected in any
     prose file under the skill directory and the top-level
     README/CHANGELOG/NOTICE/MAINTENANCE.
  3. Every data/*.json file parses and has the required top-level
     'source' and 'notice' fields.
  4. NistControlCatalogue.md is structurally consistent with
     data/nist-800-53-rev5.json (same families, same control IDs).
  5. plugin.json parses and satisfies the Claude Code plugin installer
     schema (name, version, license=Apache-2.0). The previous `skill`
     and `legal_notice` keys were dropped: the installer rejects them
     as unrecognized, the `skill` block was documentary only (Claude
     Code discovers files by convention), and legal-notice prose is
     already enforced by check #1 against README.md/SKILL.md.

Exits non-zero on any violation. Run from repo root:

    python3 tools/validate-skill.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = REPO_ROOT
DATA_DIR = SKILL_ROOT / "data"
CONTEXT_DIR = SKILL_ROOT / "context"

# -------------------------------------------------------------------------
# Endorsement-implying language denylist
# -------------------------------------------------------------------------
# The phrases below are rejected when they refer to *this skill* or to
# *the skill's output*. Citing that a third-party library is FIPS-certified
# is fine and needed; claiming the skill or its output is NIST-approved is
# not. The regex tries to approximate this with context heuristics.

ENDORSEMENT_DENYLIST = [
    # Claims the skill itself is endorsed
    (r"\bthis\s+skill\s+is\s+(NIST|FIPS|FedRAMP|CMMC|HIPAA)[-\s]?(approved|certified|ready|validated|endorsed)\b", "skill-is-endorsed"),
    (r"\bNIST[-\s]?approved\s+skill\b", "skill-is-endorsed"),
    (r"\bFIPS[-\s]?certified\s+skill\b", "skill-is-endorsed"),
    (r"\bFedRAMP[-\s]?ready\s+skill\b", "skill-is-endorsed"),

    # Claims the skill's output is audit-ready
    (r"\baudit[-\s]?proof\b", "audit-proof"),
    (r"\baudit[-\s]?ready\s+(SSP|POAM|matrix|deliverable)\b", "audit-ready-output"),
    (r"\bcompliance[-\s]?guaranteed\b", "compliance-guaranteed"),
    (r"\bproduction[-\s]?validated\s+(SSP|POAM|matrix|output)\b", "production-validated-output"),
    (r"\bsubmission[-\s]?ready\b", "submission-ready"),

    # Claims of certification by association
    (r"\bCMVP[-\s]?certified\s+(skill|tool|output)\b", "cmvp-certified-skill"),
    (r"\bNIST[-\s]?endorsed\b", "nist-endorsed"),
    (r"\bofficially\s+(approved|endorsed|blessed)\s+by\s+(NIST|CMVP|FedRAMP|AICPA|DoD)\b", "official-endorsement-claim"),
]

# Files exempt from the endorsement denylist (they intentionally discuss
# the denylist or negate it).
DENYLIST_EXEMPT_FILES = {
    REPO_ROOT / "tools" / "validate-skill.py",       # this file
    REPO_ROOT / "CONTRIBUTING.md",                    # describes the denylist
    REPO_ROOT / "README.md",                          # LEGAL NOTICE references the denylist
    REPO_ROOT / "SECURITY.md",                        # describes watermark-bypass as vulnerability
    REPO_ROOT / "CHANGELOG.md",                       # may mention the denylist in release notes
}

# -------------------------------------------------------------------------
# LEGAL NOTICE invariant
# -------------------------------------------------------------------------
# Every skill file (SKILL.md + context/* + workflows/* + commands/* +
# agents/*) must either contain the words "LEGAL NOTICE" or reference the
# parent SKILL.md's §LEGAL NOTICE, so readers always see the disclaimer
# in the same session.

LEGAL_NOTICE_MARKER_REGEX = re.compile(r"(LEGAL\s+NOTICE|§LEGAL\s+NOTICE|SKILL\.md.*LEGAL\s+NOTICE)", re.IGNORECASE)


# -------------------------------------------------------------------------

def check_endorsement_denylist() -> list[str]:
    errors = []
    prose_extensions = {".md", ".yaml", ".yml"}
    roots = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "MAINTENANCE.md",
        REPO_ROOT / "NOTICE",
        SKILL_ROOT,
    ]
    for root in roots:
        if root.is_file():
            candidates = [root]
        elif root.is_dir():
            candidates = [p for p in root.rglob("*") if p.is_file() and (p.suffix in prose_extensions or p.name in ("NOTICE",))]
        else:
            candidates = []
        for path in candidates:
            if path in DENYLIST_EXEMPT_FILES:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except Exception as e:
                errors.append(f"read-error: {path.relative_to(REPO_ROOT)}: {e}")
                continue
            for pattern, rule_id in ENDORSEMENT_DENYLIST:
                if re.search(pattern, text, re.IGNORECASE):
                    errors.append(
                        f"endorsement-denylist [{rule_id}] in "
                        f"{path.relative_to(REPO_ROOT)}: pattern /{pattern}/ matched"
                    )
    return errors


def check_legal_notice_presence() -> list[str]:
    errors = []
    roots = [
        (SKILL_ROOT / "SKILL.md", True),
    ]
    for sub in ("context", "workflows", "commands", "agents"):
        d = SKILL_ROOT / sub
        if d.is_dir():
            for p in sorted(d.glob("*.md")):
                # workflow / command / agent files must reference LEGAL NOTICE
                roots.append((p, False))
    for path, is_canonical in roots:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if not LEGAL_NOTICE_MARKER_REGEX.search(text):
            errors.append(
                f"legal-notice-missing: {path.relative_to(REPO_ROOT)} must "
                "contain a LEGAL NOTICE block or a reference to SKILL.md's one"
            )
    return errors


def check_data_file_shape() -> list[str]:
    errors = []
    required_data_files = [
        "nist-800-53-rev5.json",
        "fips-algorithms.json",
        "fips-libraries.json",
        "framework-crossmap.json",
        "_meta.json",
    ]
    for name in required_data_files:
        path = DATA_DIR / name
        if not path.exists():
            errors.append(f"data-file-missing: {path.relative_to(REPO_ROOT)}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"json-parse-error: {path.relative_to(REPO_ROOT)}: {e}")
            continue
        # _meta.json has its own shape
        if name == "_meta.json":
            for k in ("schema_version", "last_build", "data_files"):
                if k not in data:
                    errors.append(f"meta-missing-key: {k} in {name}")
            continue
        if "source" not in data:
            errors.append(f"data-missing-source: {name} lacks 'source' object")
        if "notice" not in data:
            errors.append(f"data-missing-notice: {name} lacks 'notice' string")
    return errors


def check_catalogue_consistency() -> list[str]:
    errors = []
    catalogue_md = CONTEXT_DIR / "NistControlCatalogue.md"
    catalogue_json = DATA_DIR / "nist-800-53-rev5.json"
    if not (catalogue_md.exists() and catalogue_json.exists()):
        errors.append("catalogue-missing: both .md and .json must exist")
        return errors
    data = json.loads(catalogue_json.read_text(encoding="utf-8"))
    md = catalogue_md.read_text(encoding="utf-8")
    for family in data["families"]:
        fam_id = family["id"]
        if f"## {fam_id} —" not in md:
            errors.append(
                f"catalogue-drift: family {fam_id} present in JSON but "
                "missing from NistControlCatalogue.md; re-run build-data.py"
            )
        for ctrl in family["controls"]:
            ctrl_header = f"### {ctrl['id']} — "
            if ctrl_header not in md:
                errors.append(
                    f"catalogue-drift: control {ctrl['id']} missing from "
                    "NistControlCatalogue.md; re-run build-data.py"
                )
    return errors


def check_plugin_manifest() -> list[str]:
    errors = []
    manifest = REPO_ROOT / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        errors.append("plugin-manifest-missing")
        return errors
    try:
        m = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"plugin-manifest-invalid-json: {e}")
        return errors
    required = ["name", "version", "license"]
    for k in required:
        if k not in m:
            errors.append(f"plugin-manifest-missing-key: {k}")
    if m.get("license") != "Apache-2.0":
        errors.append("plugin-manifest-license-not-apache-2.0")
    return errors


def main() -> int:
    all_errors: list[str] = []
    sections = [
        ("LEGAL-NOTICE", check_legal_notice_presence),
        ("ENDORSEMENT-DENYLIST", check_endorsement_denylist),
        ("DATA-FILES", check_data_file_shape),
        ("CATALOGUE-CONSISTENCY", check_catalogue_consistency),
        ("PLUGIN-MANIFEST", check_plugin_manifest),
    ]
    for name, fn in sections:
        errs = fn()
        if errs:
            print(f"[{name}] {len(errs)} violation(s):", file=sys.stderr)
            for e in errs:
                print(f"  - {e}", file=sys.stderr)
        else:
            print(f"[{name}] ok")
        all_errors.extend(errs)

    if all_errors:
        print(
            f"\nvalidate-skill FAILED with {len(all_errors)} total violation(s).",
            file=sys.stderr,
        )
        return 1
    print("\nvalidate-skill OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
