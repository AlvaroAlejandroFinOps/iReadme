from pathlib import Path
import pytest

ROOT_DIR = Path(__file__).resolve().parent.parent
GOLDEN_DIR = ROOT_DIR / "tests" / "golden"


def test_readme_en_golden_regression():
    """Verify README.md against golden reference snapshot for exact regression determinism."""
    active_path = ROOT_DIR / "README.md"
    golden_path = GOLDEN_DIR / "README_golden.md"

    assert active_path.exists(), "Active README.md does not exist."
    assert golden_path.exists(), "Golden reference README_golden.md does not exist."

    active_content = active_path.read_text(encoding="utf-8").strip()
    golden_content = golden_path.read_text(encoding="utf-8").strip()

    assert active_content == golden_content, (
        "README.md has deviated from golden snapshot. "
        "If this was an intentional architecture change, update tests/golden/README_golden.md."
    )


def test_readme_es_golden_regression():
    """Verify README_ES.md against golden reference snapshot for exact regression determinism."""
    active_path = ROOT_DIR / "README_ES.md"
    golden_path = GOLDEN_DIR / "README_ES_golden.md"

    assert active_path.exists(), "Active README_ES.md does not exist."
    assert golden_path.exists(), "Golden reference README_ES_golden.md does not exist."

    active_content = active_path.read_text(encoding="utf-8").strip()
    golden_content = golden_path.read_text(encoding="utf-8").strip()

    assert active_content == golden_content, (
        "README_ES.md has deviated from golden snapshot. "
        "If this was an intentional architecture change, update tests/golden/README_ES_golden.md."
    )
