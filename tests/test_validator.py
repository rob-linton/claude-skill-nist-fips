"""Integration test: run validate-skill.py and expect exit 0."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def test_validate_skill_passes():
    result = subprocess.run(
        [sys.executable, "tools/validate-skill.py"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"validate-skill.py failed:\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )
    assert "ok" in result.stdout.lower()


def test_build_data_dry_run():
    """build-data.py --dry-run must succeed (no writes, just validates)."""
    result = subprocess.run(
        [sys.executable, "tools/build-data.py", "--dry-run"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"build-data.py --dry-run failed:\n{result.stderr}"
    )
