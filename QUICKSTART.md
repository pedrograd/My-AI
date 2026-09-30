# Quick Start — One Hub, Many AIs

## Phone / tablet / normal chat apps

Paste this one line:

> Load and follow https://raw.githubusercontent.com/pedrograd/My-AI/main/BOOTSTRAP.md for this session. Use the My-AI knowledge base when relevant to my request.

Use the same line in ChatGPT, Claude, Gemini, Perplexity or another AI that can open public web links.

For persistence, put that same line once in the product's Project / Custom Instructions / Space / equivalent feature when the product supports one. If a product cannot open links, paste BOOTSTRAP.md directly or attach the repository/files.

## Desktop coding agents

From the root of any project:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrograd/My-AI/main/install.sh | bash
```

This installs lightweight local pointers for:
- AGENTS.md
- GEMINI.md
- CLAUDE.md
- GitHub Copilot repository instructions
- Cursor rules

It preserves existing files and adds a marked My-AI block instead of replacing project-specific instructions.

## Update the installed rules

Run the same command again. Managed copies under `.ai/my-ai/` and the Cursor rule are refreshed; pointer blocks are not duplicated.

## Repository catalog

The scheduled GitHub workflow refreshes public owned/starred repository metadata. A repository found in the generated catalog is only a candidate; agents must still inspect and validate it before reuse.

## Private projects

My-AI is public. Keep private source, credentials and sensitive documents in their original private repositories. The hub may name a private project and describe its role, but must not mirror its source code.

## Reality check

There is no universal standard that makes every independent AI vendor automatically and permanently read one GitHub repository. This project provides the closest portable pattern:

1. one stable public bootstrap URL for chat apps,
2. one installer command for coding agents,
3. vendor adapters for tools that support repository instructions,
4. one automatically refreshed GitHub catalog.
