#!/usr/bin/env python3
r"""
iReadme Universal Skill Installer (`scripts/install_skill.py`)

Installs the iReadme Enterprise Paper-Grade v2.0 skill into:
  1. Google Antigravity / Gemini CLI (`~/.gemini/config/skills/readme/`)
  2. Anthropic Claude Code (`~/.claude/skills/readme/`)
  3. Current or target repository (`.agents/skills/readme/` or `skills/readme/`)

Usage:
  python scripts/install_skill.py [--all] [--antigravity] [--claude] [--target-dir PATH]
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_SKILL = REPO_ROOT / "skills" / "readme" / "SKILL.md"

def get_home_dir() -> Path:
    return Path.home()

def install_to_antigravity() -> bool:
    target_dir = get_home_dir() / ".gemini" / "config" / "skills" / "readme"
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        dest = target_dir / "SKILL.md"
        shutil.copy2(SOURCE_SKILL, dest)
        print(f"[OK] Google Antigravity / Gemini: Skill installed in {dest}")
        return True
    except Exception as e:
        print(f"[ERROR] Could not install to Antigravity: {e}", file=sys.stderr)
        return False

def install_to_claude() -> bool:
    target_dir = get_home_dir() / ".claude" / "skills" / "readme"
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        dest = target_dir / "SKILL.md"
        shutil.copy2(SOURCE_SKILL, dest)
        print(f"[OK] Anthropic Claude Code: Skill installed in {dest}")
        return True
    except Exception as e:
        print(f"[ERROR] Could not install to Claude: {e}", file=sys.stderr)
        return False

def install_to_directory(dest_path: Path) -> bool:
    try:
        dest_dir = dest_path.resolve()
        if dest_dir.name != "readme":
            dest_dir = dest_dir / "readme"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / "SKILL.md"
        shutil.copy2(SOURCE_SKILL, dest)
        print(f"[OK] Target Directory: Skill installed in {dest}")
        return True
    except Exception as e:
        print(f"[ERROR] Could not install to {dest_path}: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Universal Installer for iReadme Agent Skill")
    parser.add_argument("--all", action="store_true", help="Install to all detected AI environments")
    parser.add_argument("--antigravity", action="store_true", help="Install to Google Antigravity (~/.gemini/config/skills/readme/)")
    parser.add_argument("--claude", action="store_true", help="Install to Anthropic Claude (~/.claude/skills/readme/)")
    parser.add_argument("--target-dir", type=str, help="Install to a specific project directory")

    args = parser.parse_args()

    if not SOURCE_SKILL.exists():
        print(f"[FATAL] Source skill not found at {SOURCE_SKILL}", file=sys.stderr)
        sys.exit(1)

    print("================================================================")
    print(" iReadme Universal Agent Skill Installer (Enterprise Paper-Grade)")
    print("================================================================")

    # Default to --all if no specific flags provided
    if not (args.antigravity or args.claude or args.target_dir):
        args.all = True

    success = True
    if args.all or args.antigravity:
        success = install_to_antigravity() and success

    if args.all or args.claude:
        success = install_to_claude() and success

    if args.target_dir:
        success = install_to_directory(Path(args.target_dir)) and success

    if success:
        print("\n[SUCCESS] Installation complete! The /readme skill is ready across platforms.")
    else:
        print("\n[WARNING] Some installations encountered errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
