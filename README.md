# My-AI — Universal AI Control Plane

A vendor-neutral GitHub knowledge hub for @pedrograd.

This repository lets ChatGPT, Claude, Gemini, Perplexity, Codex, Cursor, Copilot, OpenHands and other AI tools consume the same durable rules, prompts, project map and reusable repository catalog.

## Universal bootstrap

Paste this into any AI that can open web links:

> Load and follow https://raw.githubusercontent.com/pedrograd/My-AI/main/BOOTSTRAP.md for this session. Use only the relevant rules and repositories for my current request, verify live project state before making changes, and never expose secrets.

For coding environments:

```bash
curl -fsSL https://raw.githubusercontent.com/pedrograd/My-AI/main/install.sh | bash
```

The installer adds lightweight adapters for common coding agents without copying private source code or secrets.

## Design

- `BOOTSTRAP.md` — one-file entry point for any AI.
- `AGENTS.md` — vendor-neutral engineering contract.
- `AI_KNOWLEDGE_BASE.md` — curated repository map and reuse policy.
- `rules/` — durable engineering/security/reuse rules.
- `adapters/` — Gemini, Claude, Copilot and Cursor compatibility files.
- `scripts/refresh_catalog.py` — generates a public GitHub catalog from owned/starred repositories.
- `.github/workflows/refresh-catalog.yml` — scheduled/manual refresh.

## Important limitation

No GitHub repository can force every unrelated AI service to remember it permanently. Persistence depends on each product's project/custom-instruction/connector features. The portable fallback is always the single bootstrap URL above.

## Security model

This public repository contains rules and repository metadata only. It must never contain API keys, tokens, credentials, private source code, customer data or copied private documents.
