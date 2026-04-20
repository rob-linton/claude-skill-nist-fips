"""Shared pytest fixtures for the NistFipsCompliance test suite."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = REPO_ROOT / "skill" / "NistFipsCompliance"
DATA_DIR = SKILL_ROOT / "data"
CONTEXT_DIR = SKILL_ROOT / "context"
FIXTURES_DIR = REPO_ROOT / "tools" / "fixtures"

# Make tools/ importable so we can call reference_scanner / validate-skill
sys.path.insert(0, str(REPO_ROOT / "tools"))


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def skill_root() -> Path:
    return SKILL_ROOT


@pytest.fixture(scope="session")
def data_dir() -> Path:
    return DATA_DIR


@pytest.fixture(scope="session")
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture(scope="session")
def nist_catalog(data_dir) -> dict:
    return json.loads((data_dir / "nist-800-53-rev5.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def fips_algorithms(data_dir) -> dict:
    return json.loads((data_dir / "fips-algorithms.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def fips_libraries(data_dir) -> dict:
    return json.loads((data_dir / "fips-libraries.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def framework_crossmap(data_dir) -> dict:
    return json.loads((data_dir / "framework-crossmap.json").read_text(encoding="utf-8"))
