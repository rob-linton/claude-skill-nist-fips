#!/usr/bin/env python3
"""
reference_scanner.py — Minimal regex-based FIPS scanner used as the
reference implementation for v0.1.

This is NOT the production hook. The production hook is a Go static binary
(v0.2+). This Python reference scanner exists solely to:

  1. Make the test fixtures meaningful in v0.1 (we can run it against a
     fixture and produce the structured findings that the fips-crypto-reviewer
     subagent would otherwise produce inline).
  2. Give Claude a concrete "here is what the finding shape looks like"
     example when running /fips-audit inline before hooks exist.

Usage:
    python3 tools/reference_scanner.py <fixture-dir> [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

DEFAULT_EXCLUDES = [
    "docs/**",
    "**/*_test.*",
    "tests/**",
    "fixtures/**",
    ".git/**",
    "target/**",
    "node_modules/**",
    "__pycache__/**",
]

SOURCE_EXTENSIONS = {
    ".rs": "rust",
    ".go": "go",
    ".py": "python",
    ".js": "node",
    ".ts": "node",
    ".java": "java",
    ".cs": "csharp",
    ".kt": "kotlin",
    ".toml": "rust",   # Cargo.toml
    ".mod": "go",      # go.mod (dep manifest)
}


def load_algorithms() -> dict:
    path = DATA_DIR / "fips-algorithms.json"
    return json.loads(path.read_text(encoding="utf-8"))


def path_matches_any(path: Path, globs: list[str]) -> bool:
    for g in globs:
        if path.match(g):
            return True
    return False


def iter_source_files(root: Path, excludes: list[str]):
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        if path_matches_any(rel, excludes):
            continue
        lang = SOURCE_EXTENSIONS.get(p.suffix)
        # Include Cargo.toml / go.mod by name
        if not lang and p.name in ("Cargo.toml",):
            lang = "rust"
        elif not lang and p.name in ("go.mod",):
            lang = "go"
        if not lang:
            continue
        yield p, lang


def scan_file(
    path: Path,
    lang: str,
    algorithms: dict,
) -> list[dict]:
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return findings
    lines = text.splitlines()

    # Python-specific heuristic: md5 with usedforsecurity=False is WARN,
    # without is FAIL. We implement this inline because it's tricky enough
    # to deserve special-case handling; full AST handling lands in v0.2.
    python_md5_line = re.compile(r"hashlib\.md5\s*\(")

    for algo in algorithms["algorithms"]:
        name = algo["name"]
        status = algo["status"]
        if status not in {"DISALLOWED", "LEGACY_USE_ONLY", "CONDITIONALLY_APPROVED", "DEPRECATED"}:
            continue

        patterns = algo.get("detection_patterns", {})
        lang_patterns = patterns.get(lang, [])
        fallback_patterns = patterns.get("regex_fallback", [])
        candidate_patterns = lang_patterns or fallback_patterns
        if not candidate_patterns:
            continue

        for pat_str in candidate_patterns:
            try:
                pat = re.compile(pat_str)
            except re.error:
                continue
            for lineno, line in enumerate(lines, start=1):
                if not pat.search(line):
                    continue
                # Python MD5 nuance
                severity = (
                    "FAIL"
                    if status == "DISALLOWED"
                    else (
                        "WARN"
                        if status in {"LEGACY_USE_ONLY", "CONDITIONALLY_APPROVED", "DEPRECATED"}
                        else "OK"
                    )
                )
                extra_note = None
                if (
                    lang == "python"
                    and name == "MD5"
                    and python_md5_line.search(line)
                ):
                    if "usedforsecurity=False" in line:
                        severity = "WARN"
                        extra_note = "hashlib.md5 with usedforsecurity=False (non-security use)"
                    else:
                        # any hashlib.md5(...) without the kwarg
                        severity = "FAIL"
                findings.append(
                    {
                        "severity": severity,
                        "confidence": "regex-medium",
                        "file": str(path.relative_to(path.parents[len(path.parts) - path.parts.index(path.parent.name) - 1])) if False else str(path.name),  # filled below
                        "line": lineno,
                        "pattern_matched": pat_str,
                        "algorithm": name,
                        "status": status,
                        "fips_reference": algo.get("fips_reference", ""),
                        "remediation_id": algo.get("remediation_id"),
                        "note": extra_note,
                    }
                )
    return findings


def scan_repo(root: Path, excludes: list[str] | None = None) -> dict:
    excludes = excludes or DEFAULT_EXCLUDES
    algorithms = load_algorithms()
    findings = []
    files_scanned = 0
    languages = set()
    for path, lang in iter_source_files(root, excludes):
        files_scanned += 1
        languages.add(lang)
        for finding in scan_file(path, lang, algorithms):
            finding["file"] = str(path.relative_to(root))
            findings.append(finding)

    summary_counts = {"FAIL": 0, "WARN": 0, "OK": 0}
    for f in findings:
        summary_counts[f["severity"]] = summary_counts.get(f["severity"], 0) + 1

    overall = (
        "FAIL"
        if summary_counts["FAIL"] > 0
        else ("WARN" if summary_counts["WARN"] > 0 else "OK")
    )

    return {
        "scan_metadata": {
            "root": str(root),
            "files_scanned": files_scanned,
            "languages_scanned": sorted(languages),
            "algorithms_data_version": algorithms.get("source", {}).get("last_reviewed"),
        },
        "findings": findings,
        "summary": {
            **summary_counts,
            "overall": overall,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", help="directory to scan")
    ap.add_argument("--json", action="store_true", help="print JSON; otherwise human-readable")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    result = scan_repo(root)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Scanned {result['scan_metadata']['files_scanned']} files in {root}")
        print(
            f"Languages: {', '.join(result['scan_metadata']['languages_scanned']) or '(none)'}"
        )
        print(f"Overall: {result['summary']['overall']}")
        print(
            f"  FAIL={result['summary']['FAIL']} "
            f"WARN={result['summary']['WARN']} "
            f"OK={result['summary']['OK']}"
        )
        for f in result["findings"]:
            print(
                f"[{f['severity']}] {f['file']}:{f['line']} "
                f"{f['algorithm']} ({f['status']})"
                + (f" — {f['note']}" if f.get("note") else "")
            )
    return 0 if result["summary"]["overall"] != "FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
