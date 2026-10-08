# iReadme Universal Skill Installer (Windows PowerShell)
# Usage: powershell -ExecutionPolicy Bypass -File install.ps1

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " iReadme Enterprise Paper-Grade v2.0 - Universal Installer" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceSkill = Join-Path $RepoRoot "skills\readme\SKILL.md"

if (-not (Test-Path $SourceSkill)) {
    Write-Error "Source skill file not found: $SourceSkill"
    exit 1
}

# 1. Install to Google Antigravity / Gemini CLI
$AntigravityDir = Join-Path $env:USERPROFILE ".gemini\config\skills\readme"
try {
    if (-not (Test-Path $AntigravityDir)) {
        New-Item -ItemType Directory -Path $AntigravityDir -Force | Out-Null
    }
    Copy-Item -Path $SourceSkill -Destination (Join-Path $AntigravityDir "SKILL.md") -Force
    Write-Host "[OK] Google Antigravity / Gemini: Installed in $AntigravityDir\SKILL.md" -ForegroundColor Green
} catch {
    Write-Warning "Could not install to Antigravity directory: $_"
}

# 2. Install to Anthropic Claude Code
$ClaudeDir = Join-Path $env:USERPROFILE ".claude\skills\readme"
try {
    if (-not (Test-Path $ClaudeDir)) {
        New-Item -ItemType Directory -Path $ClaudeDir -Force | Out-Null
    }
    Copy-Item -Path $SourceSkill -Destination (Join-Path $ClaudeDir "SKILL.md") -Force
    Write-Host "[OK] Anthropic Claude Code: Installed in $ClaudeDir\SKILL.md" -ForegroundColor Green
} catch {
    Write-Warning "Could not install to Claude directory: $_"
}

Write-Host "`n[SUCCESS] iReadme skill is installed and ready to use via /readme across all platforms." -ForegroundColor Cyan
