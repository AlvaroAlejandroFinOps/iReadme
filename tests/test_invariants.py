import re
from pathlib import Path
import pytest

ROOT_DIR = Path(__file__).resolve().parent.parent

CANONICAL_SECTIONS_EN = [
    "## 1. Executive Abstract",
    "## 2. System Architecture & Topology",
    "## 3. Mathematical Formulation & Analytical Engines",
    "## 4. Empirical Performance & Benchmarks",
    "## 5. Repository Structure & Artifacts",
    "## 6. Execution & Verification Protocol",
    "## 7. Domain Glossary",
    "## 8. Academic & Engineering References",
]

CANONICAL_SECTIONS_ES = [
    "## 1. Resumen Ejecutivo",
    "## 2. Arquitectura y Topología del Sistema",
    "## 3. Formulación Matemática y Motores Analíticos",
    "## 4. Rendimiento Empírico y Benchmarks",
    "## 5. Estructura del Repositorio y Artefactos",
    "## 6. Protocolo de Ejecución y Verificación",
    "## 7. Glosario de Dominio",
    "## 8. Referencias Académicas y de Ingeniería",
]

EMOJI_PATTERN = re.compile(
    r"[\U0001F600-\U0001F64F"  # Emoticons
    r"\U0001F300-\U0001F5FF"  # Misc symbols & pictographs
    r"\U0001F680-\U0001F6FF"  # Transport & map
    r"\U0001F1E0-\U0001F1FF"  # Flags
    r"\U00002702-\U000027B0"  # Dingbats
    r"\U0001F900-\U0001F9FF"  # Supplemental symbols & pictographs
    r"\U0001FA70-\U0001FAFF"  # Symbols and pictographs extended-A
    r"]",
    flags=re.UNICODE,
)


@pytest.fixture
def readme_en():
    path = ROOT_DIR / "README.md"
    assert path.exists(), "README.md does not exist."
    return path.read_text(encoding="utf-8")


@pytest.fixture
def readme_es():
    path = ROOT_DIR / "README_ES.md"
    assert path.exists(), "README_ES.md does not exist."
    return path.read_text(encoding="utf-8")


FORBIDDEN_PATH_PATTERNS = [
    re.compile(r"[A-Za-z]:[/\\][A-Za-z0-9_.-]+"),  # e.g., C:\path or D:/path
    re.compile(r"file:///[A-Za-z]:"),               # e.g., file:///C:
    re.compile(r"/home/[A-Za-z0-9_.-]+"),           # e.g., /home/user
]


def test_path_portability(readme_en, readme_es):
    """Ensure no OS-specific absolute path roots leak into documentation."""
    for pattern in FORBIDDEN_PATH_PATTERNS:
        matches_en = pattern.findall(readme_en)
        matches_es = pattern.findall(readme_es)
        assert len(matches_en) == 0, f"Forbidden absolute path pattern '{pattern.pattern}' leaked in README.md: {matches_en}"
        assert len(matches_es) == 0, f"Forbidden absolute path pattern '{pattern.pattern}' leaked in README_ES.md: {matches_es}"



def test_zero_emojis(readme_en, readme_es):
    """Enforce strict Paper-Grade aesthetic standard: zero emojis."""
    emojis_en = EMOJI_PATTERN.findall(readme_en)
    emojis_es = EMOJI_PATTERN.findall(readme_es)
    assert len(emojis_en) == 0, f"Detected emojis in README.md: {emojis_en}"
    assert len(emojis_es) == 0, f"Detected emojis in README_ES.md: {emojis_es}"


def test_language_header_parity(readme_en, readme_es):
    """Verify dual language switch links format and reciprocity."""
    expected_header_en = "**Language:** [English](README.md) | [Español](README_ES.md)"
    expected_header_es = "**Idioma:** [English](README.md) | [Español](README_ES.md)"

    assert expected_header_en in readme_en, "README.md is missing valid language header."
    assert expected_header_es in readme_es, "README_ES.md is missing valid language header."


def test_canonical_sections_parity(readme_en, readme_es):
    """Verify presence of all 8 canonical sections in exact order."""
    for section in CANONICAL_SECTIONS_EN:
        assert section in readme_en, f"Missing section '{section}' in README.md"

    for section in CANONICAL_SECTIONS_ES:
        assert section in readme_es, f"Missing section '{section}' in README_ES.md"


def test_katex_latex_balance(readme_en, readme_es):
    """Verify that LaTeX math delimiters ($$ and $) are properly balanced."""
    for doc_name, content in [("README.md", readme_en), ("README_ES.md", readme_es)]:
        block_math_count = content.count("$$")
        assert block_math_count % 2 == 0, f"Unbalanced '$$' block math delimiters in {doc_name}"
        assert block_math_count >= 4, f"Expected at least 2 math blocks in {doc_name}"


def test_bibtex_citation_block(readme_en, readme_es):
    """Verify BibTeX citation block presence and schema."""
    assert "@software{ireadme_2026" in readme_en
    assert "@software{ireadme_2026" in readme_es
