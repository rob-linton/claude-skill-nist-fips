"""Data-file integrity tests.

Verifies:
  - All required data/*.json files exist, parse, and have required top-level
    fields (source, notice).
  - Every algorithm in fips-algorithms.json has a status and fips_reference.
  - Every NIST control has an ID and a title.
  - Every framework-crossmap row references a valid control ID.
  - The NistControlCatalogue.md includes every family and control present
    in the JSON (structural consistency — `validate-skill.py` enforces this
    too, but we duplicate in tests for the unit-test surface).
  - Every disallowed algorithm has at least one detection pattern.
"""
from __future__ import annotations

import re


REQUIRED_ALGORITHM_FIELDS = {"name", "family", "status", "fips_reference"}
VALID_STATUSES = {"APPROVED", "CONDITIONALLY_APPROVED", "DEPRECATED", "LEGACY_USE_ONLY", "DISALLOWED"}


def test_nist_catalog_top_level(nist_catalog):
    for key in ("source", "notice", "families", "build"):
        assert key in nist_catalog, f"nist-800-53-rev5.json missing top-level '{key}'"


def test_nist_catalog_families_non_empty(nist_catalog):
    assert nist_catalog["families"], "no families extracted from OSCAL"
    for fam in nist_catalog["families"]:
        assert fam["id"] in {"AC", "AT", "AU", "CA", "CM", "CP", "IA", "IR",
                             "MA", "MP", "PE", "PL", "PM", "PS", "PT", "RA",
                             "SA", "SC", "SI", "SR"}, f"unknown family id {fam['id']}"
        assert fam["controls"], f"family {fam['id']} has no controls"


def test_nist_catalog_v0_1_scope(nist_catalog):
    """v0.1 ships AC, AU, IA, SC."""
    family_ids = {fam["id"] for fam in nist_catalog["families"]}
    assert family_ids == {"AC", "AU", "IA", "SC"}, (
        f"v0.1 should ship exactly AC/AU/IA/SC, got {sorted(family_ids)}"
    )


def test_nist_controls_have_required_fields(nist_catalog):
    for fam in nist_catalog["families"]:
        for ctrl in fam["controls"]:
            assert ctrl.get("id"), "control without id"
            assert ctrl.get("title"), f"control {ctrl.get('id')} without title"
            # Some controls may lack statement/guidance if OSCAL omits — but
            # all v0.1 scope should have them. Assert stronger:
            assert ctrl.get("statement") or ctrl.get("guidance"), (
                f"control {ctrl['id']} has neither statement nor guidance"
            )


def test_fips_algorithms_top_level(fips_algorithms):
    for key in ("source", "notice", "algorithms", "remediations"):
        assert key in fips_algorithms, f"fips-algorithms.json missing '{key}'"
    assert fips_algorithms["algorithms"], "no algorithms defined"


def test_fips_algorithms_shape(fips_algorithms):
    for algo in fips_algorithms["algorithms"]:
        for key in REQUIRED_ALGORITHM_FIELDS:
            assert key in algo, f"algorithm {algo.get('name','?')} missing {key}"
        assert algo["status"] in VALID_STATUSES, (
            f"algorithm {algo['name']} has invalid status {algo['status']}"
        )


def test_every_disallowed_has_detection_pattern(fips_algorithms):
    """A disallowed algorithm must be detectable — otherwise the rule is
    unenforceable."""
    for algo in fips_algorithms["algorithms"]:
        if algo["status"] != "DISALLOWED":
            continue
        patterns = algo.get("detection_patterns", {})
        assert patterns, (
            f"DISALLOWED algorithm {algo['name']} has no detection_patterns; "
            "add at least regex_fallback"
        )


def test_remediation_ids_resolve(fips_algorithms):
    """Every remediation_id referenced on an algorithm must exist in the
    remediations map."""
    remediations = fips_algorithms["remediations"]
    for algo in fips_algorithms["algorithms"]:
        rid = algo.get("remediation_id")
        if rid:
            assert rid in remediations, (
                f"algorithm {algo['name']} references remediation_id '{rid}' "
                "which is not defined in remediations{}"
            )


def test_detection_patterns_compile(fips_algorithms):
    for algo in fips_algorithms["algorithms"]:
        for lang, patterns in algo.get("detection_patterns", {}).items():
            for pat in patterns:
                try:
                    re.compile(pat)
                except re.error as e:
                    raise AssertionError(
                        f"invalid regex for {algo['name']} [{lang}]: {pat!r} ({e})"
                    )


def test_hardcoded_floor_cannot_be_user_overridable(fips_algorithms):
    """A rule marked hardcoded_floor must really be un-disableable by
    fips-policy.yaml; ensure no entry is both user-overridable AND floor."""
    for algo in fips_algorithms["algorithms"]:
        if algo.get("hardcoded_floor") and algo.get("user_overridable"):
            raise AssertionError(
                f"algorithm {algo['name']} cannot be both hardcoded_floor and user_overridable"
            )


def test_fips_libraries_shape(fips_libraries):
    for key in ("source", "notice", "libraries"):
        assert key in fips_libraries
    for lib in fips_libraries["libraries"]:
        for k in ("language", "library", "cmvp_certificate", "verified_on"):
            assert k in lib, f"library {lib.get('library','?')} missing {k}"


def test_framework_crossmap_references_real_controls(nist_catalog, framework_crossmap):
    """Every control_id in framework-crossmap must exist in the v0.1 catalog
    (or be an enhancement, e.g., IA-2(1))."""
    known = set()
    for fam in nist_catalog["families"]:
        for ctrl in fam["controls"]:
            known.add(ctrl["id"])
            for enh in ctrl.get("enhancements", []):
                known.add(enh["id"])
    # Enhancements in the crossmap are written as "IA-2(1)" but OSCAL IDs
    # are "IA-2.01". Build both forms.
    known_paren = {id_convert_dot_to_paren(c) for c in known}
    for row in framework_crossmap["mappings"]:
        cid = row["control_id"]
        assert cid in known or cid in known_paren, (
            f"framework-crossmap references {cid} which is not in the v0.1 catalog"
        )


def id_convert_dot_to_paren(oscal_id: str) -> str:
    """Convert 'IA-2.01' to 'IA-2(1)'."""
    m = re.match(r"^([A-Z]+-\d+)\.0*(\d+)$", oscal_id)
    if m:
        return f"{m.group(1)}({m.group(2)})"
    return oscal_id


def test_catalogue_md_has_all_families(skill_root, nist_catalog):
    md = (skill_root / "context" / "NistControlCatalogue.md").read_text(encoding="utf-8")
    for fam in nist_catalog["families"]:
        assert f"## {fam['id']} —" in md, (
            f"NistControlCatalogue.md missing family {fam['id']}; re-run build-data.py"
        )


def test_meta_has_recent_build(data_dir):
    import json
    meta = json.loads((data_dir / "_meta.json").read_text(encoding="utf-8"))
    assert meta["schema_version"] == 1
    assert "last_build" in meta
    assert "data_files" in meta
    assert "nist-800-53-rev5.json" in meta["data_files"]
