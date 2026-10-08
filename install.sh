#!/usr/bin/env bash
# iReadme Universal Skill Installer (Linux / macOS)
# Usage: ./install.sh

set -euo pipefail

echo "================================================================"
echo " iReadme Enterprise Paper-Grade v2.0 - Universal Installer"
echo "================================================================"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_SKILL="$REPO_ROOT/skills/readme/SKILL.md"

if [ ! -f "$SOURCE_SKILL" ]; then
    echo "[ERROR] Source skill file not found: $SOURCE_SKILL" >&2
    exit 1
fi

# 1. Install to Google Antigravity / Gemini CLI
ANTIGRAVITY_DIR="$HOME/.gemini/config/skills/readme"
mkdir -p "$ANTIGRAVITY_DIR"
cp -f "$SOURCE_SKILL" "$ANTIGRAVITY_DIR/SKILL.md"
echo "[OK] Google Antigravity / Gemini: Installed in $ANTIGRAVITY_DIR/SKILL.md"

# 2. Install to Anthropic Claude Code
CLAUDE_DIR="$HOME/.claude/skills/readme"
mkdir -p "$CLAUDE_DIR"
cp -f "$SOURCE_SKILL" "$CLAUDE_DIR/SKILL.md"
echo "[OK] Anthropic Claude Code: Installed in $CLAUDE_DIR/SKILL.md"

echo ""
echo "[SUCCESS] iReadme skill is installed and ready to use via /readme across all platforms."
