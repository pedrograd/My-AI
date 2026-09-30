#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${MY_AI_BASE_URL:-https://raw.githubusercontent.com/pedrograd/My-AI/main}"
TARGET="${1:-.}"

mkdir -p "$TARGET/.ai/my-ai" "$TARGET/.cursor/rules" "$TARGET/.github"

fetch() {
  local src="$1"
  local dst="$2"
  curl -fsSL "$BASE_URL/$src" -o "$TARGET/$dst"
}

fetch "BOOTSTRAP.md" ".ai/my-ai/BOOTSTRAP.md"
fetch "AGENTS.md" ".ai/my-ai/AGENTS.md"
fetch "AI_KNOWLEDGE_BASE.md" ".ai/my-ai/AI_KNOWLEDGE_BASE.md"
fetch "rules/REUSE.md" ".ai/my-ai/REUSE.md"
fetch "rules/SECURITY.md" ".ai/my-ai/SECURITY.md"
fetch "adapters/CURSOR.mdc" ".cursor/rules/pedrograd-my-ai.mdc"

append_block() {
  local file="$1"
  local begin="# >>> PEDROGRAD MY-AI >>>"
  local end="# <<< PEDROGRAD MY-AI <<<"
  local block="$begin
Read .ai/my-ai/BOOTSTRAP.md first for shared repository-aware engineering rules.
Use the target project's current instructions and architecture as the local source of truth.
$end"

  touch "$TARGET/$file"
  if ! grep -Fq "$begin" "$TARGET/$file"; then
    printf "\n%s\n" "$block" >> "$TARGET/$file"
  fi
}

append_block "AGENTS.md"
append_block "GEMINI.md"
append_block "CLAUDE.md"
append_block ".github/copilot-instructions.md"

printf '%s\n' "Installed Pedrograd My-AI adapters into: $TARGET"
printf '%s\n' "Bootstrap: $TARGET/.ai/my-ai/BOOTSTRAP.md"
