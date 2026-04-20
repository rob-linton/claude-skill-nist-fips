"""Golden tests for the reference FIPS scanner against the human-authored
fixtures under tools/fixtures/.

These tests compare structural properties (overall severity, minimum
finding counts, algorithms present) rather than exact finding lists,
because the scanner's regex output will change as the detection patterns
evolve. Each fixture carries GROUND_TRUTH.md with the human rationale.
"""
from __future__ import annotations

import pytest

import reference_scanner as rs


def _scan(fixture_dir):
    return rs.scan_repo(fixture_dir)


def test_fixture_rust_chacha20_fails(fixtures_dir):
    result = _scan(fixtures_dir / "fixture-rust-chacha20")
    assert result["summary"]["overall"] == "FAIL", result
    assert result["summary"]["FAIL"] >= 1, "expected at least one FAIL"
    algos = {f["algorithm"] for f in result["findings"]}
    assert "ChaCha20-Poly1305" in algos, f"expected ChaCha20 hit; got {algos}"


def test_fixture_rust_aws_lc_ok_passes(fixtures_dir):
    result = _scan(fixtures_dir / "fixture-rust-aws-lc-ok")
    # Scanner may still flag if patterns overlap; critical check is zero FAIL
    assert result["summary"]["FAIL"] == 0, result
    assert result["summary"]["overall"] in {"OK", "WARN"}, result


def test_fixture_greenfield_no_crypto(fixtures_dir):
    """greenfield fixture has no crypto; scanner should produce zero findings."""
    result = _scan(fixtures_dir / "fixture-greenfield-no-matrix")
    assert result["summary"]["overall"] == "OK"
    assert result["summary"]["FAIL"] == 0
    assert result["summary"]["WARN"] == 0


def test_fixture_go_no_boring_algo_check(fixtures_dir):
    """The scanner only checks algorithms — AES-GCM is approved, so algo
    check is OK. Library-check (which would FAIL) is done by the
    subagent, not by this scanner. Document this in the test."""
    result = _scan(fixtures_dir / "fixture-go-no-boring")
    assert result["summary"]["FAIL"] == 0, (
        "AES-GCM itself is approved; FAIL would come from a separate "
        "library/startup-assertion check not implemented in v0.1 scanner"
    )


def test_fixture_python_md5_legacy_distinguishes_usedforsecurity(fixtures_dir):
    result = _scan(fixtures_dir / "fixture-python-md5-legacy")
    # Must have at least one FAIL for the bare hashlib.md5()
    assert result["summary"]["FAIL"] >= 1
    # Must have at least one WARN for the hashlib.md5(..., usedforsecurity=False)
    assert result["summary"]["WARN"] >= 1
    # The WARN should carry the note explaining why
    warn_notes = [f["note"] for f in result["findings"] if f["severity"] == "WARN" and f.get("note")]
    assert any("usedforsecurity=False" in n for n in warn_notes), (
        f"expected a WARN finding noting usedforsecurity=False; got {warn_notes}"
    )


@pytest.mark.parametrize(
    "fixture_name",
    [
        "fixture-rust-chacha20",
        "fixture-rust-aws-lc-ok",
        "fixture-go-no-boring",
        "fixture-python-md5-legacy",
        "fixture-greenfield-no-matrix",
    ],
)
def test_every_fixture_has_ground_truth(fixtures_dir, fixture_name):
    """The human-authored ground truth must exist for every fixture."""
    gt = fixtures_dir / fixture_name / "GROUND_TRUTH.md"
    assert gt.exists(), f"fixture {fixture_name} missing GROUND_TRUTH.md"
    text = gt.read_text(encoding="utf-8")
    assert "Human-authored" in text or "human-authored" in text, (
        f"{fixture_name}/GROUND_TRUTH.md must identify itself as human-authored"
    )


def test_scanner_findings_have_required_fields(fixtures_dir):
    result = _scan(fixtures_dir / "fixture-rust-chacha20")
    required = {"severity", "file", "line", "algorithm", "status", "fips_reference"}
    for f in result["findings"]:
        missing = required - set(f.keys())
        assert not missing, f"finding missing fields {missing}: {f}"
