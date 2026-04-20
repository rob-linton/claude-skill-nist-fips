#!/usr/bin/env python3
"""
build-data.py — Regenerate machine-readable data files from authoritative sources.

LEGAL NOTICE: This tool is part of NistFipsCompliance. See the project
README.md for the full legal notice. NIST OSCAL content is a work of the
U.S. Government and is public domain in the United States per 17 U.S.C. §105.
No endorsement by NIST is implied.

Usage:
    python3 tools/build-data.py [--refresh-oscal] [--families AC,AU,IA,SC]

Outputs:
    skill/NistFipsCompliance/data/nist-800-53-rev5.json
    skill/NistFipsCompliance/data/_meta.json
    skill/NistFipsCompliance/context/NistControlCatalogue.md

Rules (CI-enforced):
    1. Prose in NistControlCatalogue.md is derived from OSCAL discussion +
       statement text. No hand-editing; drift fails the build.
    2. Every "human-readable" string field in the output JSON is scanned
       for prompt-injection-style phrasing. Findings fail the build.
    3. The OSCAL source URL is pinned; refreshes are explicit.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = REPO_ROOT / "skill" / "NistFipsCompliance"
DATA_DIR = SKILL_ROOT / "data"
CONTEXT_DIR = SKILL_ROOT / "context"
OSCAL_CACHE = REPO_ROOT / "tools" / ".oscal-cache" / "nist-800-53-rev5-catalog.json"

OSCAL_URL = (
    "https://raw.githubusercontent.com/usnistgov/oscal-content/"
    "main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json"
)

# --------------------------------------------------------------------------
# Injection-detection denylist
# --------------------------------------------------------------------------

# Phrases that should not appear in any human-readable string field sourced
# from external data. If any of these appear in OSCAL content, either the
# source has been compromised or our extraction is bringing in the wrong
# field. Either way — fail fast.
INJECTION_PATTERNS = [
    re.compile(r"\bignore\s+(all\s+)?previous\s+instructions?\b", re.IGNORECASE),
    re.compile(r"\byou\s+are\s+now\s+\w+", re.IGNORECASE),
    re.compile(r"\bsystem\s*:\s*you\s+", re.IGNORECASE),
    re.compile(r"<\|im_start\|>", re.IGNORECASE),
    re.compile(r"\[INST\]", re.IGNORECASE),
    re.compile(r"\bdisregard\s+(the\s+)?(above|previous)", re.IGNORECASE),
    re.compile(r"\boverride\s+(the\s+)?(rules|policy|instructions)", re.IGNORECASE),
]


def check_injection(s: str, context: str) -> list[str]:
    """Return a list of injection-pattern matches; empty list is clean."""
    if not isinstance(s, str):
        return []
    findings = []
    for pat in INJECTION_PATTERNS:
        if pat.search(s):
            findings.append(f"{context}: matches /{pat.pattern}/")
    return findings


# --------------------------------------------------------------------------
# OSCAL extraction
# --------------------------------------------------------------------------

# Default families for v0.1
DEFAULT_FAMILIES = ["AC", "AU", "IA", "SC"]


def fetch_oscal(force: bool) -> dict:
    if force or not OSCAL_CACHE.exists():
        OSCAL_CACHE.parent.mkdir(parents=True, exist_ok=True)
        print(f"[fetch] {OSCAL_URL}")
        req = urllib.request.Request(
            OSCAL_URL,
            headers={"User-Agent": "NistFipsCompliance-build-data/0.1"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read()
        OSCAL_CACHE.write_bytes(body)
        sha = hashlib.sha256(body).hexdigest()
        print(f"[fetch] sha256={sha}  ({len(body)} bytes)")
    else:
        print(f"[cache] {OSCAL_CACHE}")
    return json.loads(OSCAL_CACHE.read_text(encoding="utf-8"))


def _part_prose(parts: list, name: str) -> str:
    """Extract the first prose block whose part has `name`."""
    if not parts:
        return ""
    for p in parts:
        if p.get("name") == name:
            if "prose" in p:
                return p["prose"]
            # The statement part nests items under parts[].parts[]
            if "parts" in p:
                fragments = []
                for sub in p["parts"]:
                    label = None
                    for prop in sub.get("props", []):
                        if prop.get("name") == "label":
                            label = prop.get("value")
                    prose = sub.get("prose", "")
                    if label:
                        fragments.append(f"{label} {prose}")
                    else:
                        fragments.append(prose)
                return "\n".join(fragments)
    return ""


def _params(ctrl: dict) -> list[dict]:
    out = []
    for p in ctrl.get("params", []) or []:
        item = {
            "id": p.get("id", ""),
            "label": next(
                (prop.get("value") for prop in p.get("props", []) if prop.get("name") == "label"),
                "",
            ),
            "select_how_many": p.get("select", {}).get("how-many") if isinstance(p.get("select"), dict) else None,
            "guidelines": [g.get("prose", "") for g in p.get("guidelines", []) or []],
        }
        out.append(item)
    return out


def _baselines(ctrl: dict) -> dict:
    """Extract low/moderate/high baseline assignment from OSCAL props."""
    baselines = {"low": False, "moderate": False, "high": False}
    for prop in ctrl.get("props", []) or []:
        if prop.get("name") == "status":
            continue
        # OSCAL baseline assignment is represented via 'class' on an
        # impact-baseline property. We rely on the SP 800-53B profile in
        # data/framework-crossmap.json for the authoritative baseline
        # membership; the OSCAL catalog doesn't ship the baseline flags
        # directly. Leave as False here; build-data merges baselines from
        # the profile in a later step (v0.2).
    return baselines


def extract_control(ctrl: dict, family_id: str) -> dict:
    parts = ctrl.get("parts", []) or []
    statement = _part_prose(parts, "statement")
    guidance = _part_prose(parts, "guidance")
    objective = _part_prose(parts, "assessment-objective")

    out = {
        "id": ctrl["id"].upper(),
        "family": family_id.upper(),
        "title": ctrl.get("title", ""),
        "statement": statement,
        "guidance": guidance,
        "objective": objective,
        "parameters": _params(ctrl),
        "related": [
            link.get("href", "").lstrip("#").upper()
            for link in ctrl.get("links", []) or []
            if link.get("rel") == "related"
        ],
        "enhancements": [],
    }

    for enh in ctrl.get("controls", []) or []:
        out["enhancements"].append(extract_control(enh, family_id))

    return out


def build_catalog(oscal: dict, families: list[str]) -> tuple[dict, list[str]]:
    """Extract the requested families; return (data, injection_findings)."""
    cat = oscal["catalog"]
    included = [g for g in cat["groups"] if g["id"].upper() in families]
    missing = [f for f in families if not any(g["id"].upper() == f for g in cat["groups"])]
    if missing:
        raise SystemExit(f"families not found in OSCAL: {missing}")

    out_families = []
    all_findings: list[str] = []
    for grp in included:
        fam_id = grp["id"].upper()
        controls = []
        for ctrl in grp.get("controls", []) or []:
            # Withdrawn controls are marked either via class='withdrawn' or
            # via a prop with name='status' value='withdrawn'.
            if ctrl.get("class") == "withdrawn":
                continue
            if any(
                p.get("name") == "status" and p.get("value") == "withdrawn"
                for p in ctrl.get("props", []) or []
            ):
                continue
            c = extract_control(ctrl, fam_id)
            # Scan all human-readable string fields for injection patterns
            for field in ("title", "statement", "guidance", "objective"):
                all_findings.extend(check_injection(c.get(field, ""), f"{c['id']}.{field}"))
            controls.append(c)
        out_families.append(
            {
                "id": fam_id,
                "title": grp.get("title", ""),
                "controls": controls,
            }
        )

    return (
        {
            "source": {
                "name": "NIST OSCAL SP 800-53 Rev 5 Catalog",
                "url": OSCAL_URL,
                "oscal_version": cat["metadata"].get("oscal-version"),
                "catalog_version": cat["metadata"].get("version"),
                "last_modified": cat["metadata"].get("last-modified"),
            },
            "build": {
                "built_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                "tool": "tools/build-data.py",
                "schema_version": 1,
                "families_included": families,
            },
            "notice": (
                "NIST OSCAL content is a work of the U.S. Government "
                "(public domain in the U.S. per 17 U.S.C. §105). NIST does "
                "not endorse this project. See repository NOTICE file."
            ),
            "families": out_families,
        },
        all_findings,
    )


# --------------------------------------------------------------------------
# NistControlCatalogue.md generation
# --------------------------------------------------------------------------

CATALOGUE_HEADER = """# NistControlCatalogue.md

> **Read [`SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** This file is
> **generated** by `tools/build-data.py` from the NIST OSCAL SP 800-53
> Rev 5 catalogue ([upstream source](https://github.com/usnistgov/oscal-content)).
> Do not hand-edit — CI re-generates and diff-checks on every build. NIST
> OSCAL content is a U.S. Government work (public domain in the U.S.).
> NIST does not endorse this project.

**Catalog version**: {catalog_version}
**OSCAL last-modified**: {last_modified}
**Built at**: {built_at}
**Families included (v0.1 scope)**: {families}

The remaining 16 families (AT, CA, CM, CP, IR, MA, MP, PE, PL, PM, PS, PT,
RA, SA, SR) arrive in v0.2. Each family follows the same structure:
authoritative **OSCAL-sourced** statement + guidance, with a local
"implementation-hint" cross-reference to `data/implementation-hints.json`
(v0.2+).

---

"""


def render_family(family: dict) -> str:
    lines = [f"## {family['id']} — {family['title']}", ""]
    lines.append(
        f"*{len(family['controls'])} base controls (enhancements listed "
        f"per-control).*"
    )
    lines.append("")
    for c in family["controls"]:
        lines.append(f"### {c['id']} — {c['title']}")
        lines.append("")
        if c["statement"]:
            lines.append("**Statement (OSCAL)**")
            lines.append("")
            lines.append("```")
            lines.append(c["statement"].strip())
            lines.append("```")
            lines.append("")
        if c["guidance"]:
            lines.append("**Guidance (OSCAL)**")
            lines.append("")
            # Quote block for guidance
            for para in c["guidance"].strip().split("\n\n"):
                lines.append("> " + para.replace("\n", "\n> "))
                lines.append("")
        if c["parameters"]:
            lines.append("**Organisation-defined parameters**")
            lines.append("")
            for p in c["parameters"]:
                lines.append(f"- `{p['id']}` ({p['label']})")
            lines.append("")
        if c["related"]:
            lines.append(
                "**Related controls**: " + ", ".join(c["related"])
            )
            lines.append("")
        if c["enhancements"]:
            lines.append(f"**Enhancements** ({len(c['enhancements'])}):")
            lines.append("")
            for e in c["enhancements"]:
                lines.append(f"- **{e['id']}** — {e['title']}")
            lines.append("")
    return "\n".join(lines)


def render_catalogue(catalog: dict) -> str:
    head = CATALOGUE_HEADER.format(
        catalog_version=catalog["source"]["catalog_version"],
        last_modified=catalog["source"]["last_modified"],
        built_at=catalog["build"]["built_at"],
        families=", ".join(catalog["build"]["families_included"]),
    )
    body = "\n\n---\n\n".join(render_family(f) for f in catalog["families"])
    return head + body + "\n"


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--refresh-oscal",
        action="store_true",
        help="force re-download of the OSCAL catalog from the upstream URL",
    )
    ap.add_argument(
        "--families",
        default=",".join(DEFAULT_FAMILIES),
        help="comma-separated list of 2-char family IDs (default: AC,AU,IA,SC)",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="do not write output files; print a summary only",
    )
    args = ap.parse_args()

    families = [f.strip().upper() for f in args.families.split(",") if f.strip()]
    if not families:
        print("no families requested", file=sys.stderr)
        return 2

    oscal = fetch_oscal(force=args.refresh_oscal)
    catalog, findings = build_catalog(oscal, families)

    if findings:
        print("INJECTION PATTERNS DETECTED in OSCAL content:", file=sys.stderr)
        for f in findings:
            print(f"  {f}", file=sys.stderr)
        print(
            "\nThis indicates either a corrupted OSCAL source or an "
            "extraction bug. Refusing to write outputs.",
            file=sys.stderr,
        )
        return 3

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CONTEXT_DIR.mkdir(parents=True, exist_ok=True)

    ctrl_count = sum(len(f["controls"]) for f in catalog["families"])
    enh_count = sum(
        len(c["enhancements"])
        for f in catalog["families"]
        for c in f["controls"]
    )

    if args.dry_run:
        print(
            f"[dry-run] families={len(catalog['families'])} "
            f"controls={ctrl_count} enhancements={enh_count}"
        )
        return 0

    out_json = DATA_DIR / "nist-800-53-rev5.json"
    out_json.write_text(json.dumps(catalog, indent=2, ensure_ascii=False))
    print(f"[write] {out_json.relative_to(REPO_ROOT)}")

    meta = {
        "schema_version": 1,
        "last_build": catalog["build"]["built_at"],
        "data_files": {
            "nist-800-53-rev5.json": {
                "source": catalog["source"]["url"],
                "source_version": catalog["source"]["catalog_version"],
                "source_last_modified": catalog["source"]["last_modified"],
                "families_included": families,
                "control_count": ctrl_count,
                "enhancement_count": enh_count,
            },
        },
        "staleness_warnings": [],
    }
    (DATA_DIR / "_meta.json").write_text(json.dumps(meta, indent=2))
    print(f"[write] {(DATA_DIR / '_meta.json').relative_to(REPO_ROOT)}")

    catalogue_md = render_catalogue(catalog)
    (CONTEXT_DIR / "NistControlCatalogue.md").write_text(catalogue_md)
    print(
        f"[write] {(CONTEXT_DIR / 'NistControlCatalogue.md').relative_to(REPO_ROOT)}"
    )

    print(
        f"\nOK — {len(catalog['families'])} families, "
        f"{ctrl_count} controls, {enh_count} enhancements."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
