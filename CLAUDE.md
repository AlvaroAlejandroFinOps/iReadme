# Claude Code & Desktop Guidelines: iReadme (`CLAUDE.md`)

This file guides Anthropic Claude (Claude Code CLI and Claude Desktop Projects) when working in this repository or applying the `iReadme` skill.

## System Mission
The `iReadme` engine enforces the **Enterprise Paper-Grade v2.0** standard for repository documentation. When generating or auditing `README.md` and `README_ES.md`, Claude must adhere strictly to institutional engineering norms.

## Critical Instructions for Claude
1. **Never Output Absolute Paths:**
   - Do NOT output paths containing `C:`, `D:`, `file:///`, or `/home/`.
   - Every reference must be relative to the repository root (e.g., `src/`, `skills/readme/SKILL.md`).
2. **Zero Emojis:**
   - Claude must never use emojis or informal exclamations in documentation artifacts.
3. **Dual Language Synchronization:**
   - Always produce or update both `README.md` (English) and `README_ES.md` (Spanish) simultaneously.
   - Maintain reciprocal header links:
     - `**Language:** [English](README.md) | [Español](README_ES.md)`
     - `**Idioma:** [English](README.md) | [Español](README_ES.md)`
4. **Vanguard Corporate & Paper-Grade Language:**
   - Section 1 must articulate: (1) Operational & Business Friction, (2) Strategic Value Proposition & TCO/ROI Impact, (3) Architectural Thesis.
   - Section 3 must express algorithms and analytical engines with formal $\LaTeX$ notation ($$...$$).
   - Section 4 must provide bimodal benchmarking (Systems Engineering + Business Governance).
5. **Execution Commands:**
   - Run tests: `python -m pytest`
   - Run documentation generator: `python scripts/init_readme.py`
   - Install skill globally: `python scripts/install_skill.py`
