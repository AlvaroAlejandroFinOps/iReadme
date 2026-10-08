from pathlib import Path
import pytest
from scripts.init_readme import atomic_write_text, generate_readmes


def test_atomic_write_creates_file(tmp_path: Path):
    target = tmp_path / "output" / "document.md"
    content = "# Test Content\n\n- Line 1\n- Line 2\n"
    
    atomic_write_text(target, content, encoding="utf-8")
    
    assert target.exists()
    assert target.read_text(encoding="utf-8") == content


def test_atomic_write_utf8_encoding_preservation(tmp_path: Path):
    target = tmp_path / "utf8_test.md"
    complex_text = "Ecosistema iReadme: Formulación Matemática $\\Phi = 1.0$ | Sincronización en Español: áéíóú ñ ¿¡"
    
    atomic_write_text(target, complex_text, encoding="utf-8")
    
    read_back = target.read_text(encoding="utf-8")
    assert read_back == complex_text


def test_atomic_write_safely_overwrites(tmp_path: Path):
    target = tmp_path / "overwrite.md"
    initial_content = "Initial Version"
    updated_content = "Updated Version 2.0"
    
    atomic_write_text(target, initial_content, encoding="utf-8")
    assert target.read_text(encoding="utf-8") == initial_content
    
    atomic_write_text(target, updated_content, encoding="utf-8")
    assert target.read_text(encoding="utf-8") == updated_content
    
    # Check no lingering temp files in directory
    temp_files = list(tmp_path.glob(".*.tmp_*"))
    assert len(temp_files) == 0, f"Lingering temp files found: {temp_files}"


def test_generate_readmes_to_custom_dir(tmp_path: Path):
    generate_readmes(root_dir=tmp_path)
    
    readme_en = tmp_path / "README.md"
    readme_es = tmp_path / "README_ES.md"
    
    assert readme_en.exists()
    assert readme_es.exists()
    assert "iReadme: Institutional Paper-Grade Documentation Engine" in readme_en.read_text(encoding="utf-8")
    assert "iReadme: Motor de Documentación Institucional Grado Paper" in readme_es.read_text(encoding="utf-8")
