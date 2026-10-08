# Universal Agent Directive: iReadme System (`AGENTS.md`)

This repository implements the **iReadme** engine and the canonical **Enterprise Paper-Grade v2.0** documentation standard for Autonomous AI Coding Agents.

## Agent Role & Mission
When instructed to create, format, or synchronize repository documentation (`README.md` and `README_ES.md`), the agent must follow the rules defined in `skills/readme/SKILL.md`.

## Mandatory Engineering Rules
1. **Zero Path Leakage (Absolute Portability):**
   - Strictly forbidden to include OS-specific absolute paths (`C:\`, `D:\`, `file:///`, `/home/`).
   - Every file link must be relative to the workspace root (`src/`, `config/`, `skills/`, `docs/`, `tests/`).
   - Dual-language header must use relative links:
     - In `README.md`: `**Language:** [English](README.md) | [Español](README_ES.md)`
     - In `README_ES.md`: `**Idioma:** [English](README.md) | [Español](README_ES.md)`
2. **Zero Emojis & Strict Institutional Tone:**
   - No emojis, conversational filler, or informal icons.
   - Dense, strategic, and high-engineering tone (IEEE / ACM Systems Paper + Enterprise Architecture).
3. **Formal Mathematical LaTeX ($\LaTeX$):**
   - Use KaTeX/LaTeX for all analytical engines, algorithms, cost functions, invariant bounds, and data transformations (`$$...$$` and `$...$`).
4. **ASCII Architecture Topology:**
   - Architectural and data flow diagrams must be clean, symmetric ASCII/Unicode boxes.
   - Distinguish Control Plane from Data/Analytical Plane.
5. **Canonical 8-Section Layout:**
   - Both `README.md` and `README_ES.md` must implement the exact 8 canonical sections:
     1. Executive Abstract (Resumen Ejecutivo)
     2. System Architecture & Topology (Arquitectura y Topología del Sistema)
     3. Mathematical Formulation & Analytical Engines (Formulación Matemática y Motores Analíticos)
     4. Empirical Performance & Benchmarks (Rendimiento Empírico y Benchmarks)
     5. Repository Structure & Artifacts (Estructura del Repositorio y Artefactos)
     6. Execution & Verification Protocol (Protocolo de Ejecución y Verificación)
     7. Domain Glossary (Glosario de Dominio)
     8. Academic & Engineering References (Referencias Académicas y de Ingeniería)

## Installation & Skill Execution
- Canonical Skill location: `skills/readme/SKILL.md`
- Documentation generator: `python scripts/init_readme.py`
- Test suite: `python -m pytest`
