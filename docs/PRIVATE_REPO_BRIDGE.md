# PEDROGRAD OS — Private Repository Routing Bridge

**Public metadata only.** This document is a safe bridge between the public `pedrograd/My-AI` discovery catalog and the owner's **private** code/policy repository. It does **not** grant access to that private repository, its documents, code, users, finance, or model memories.

## Authorized agent flow

1. Use `BOOTSTRAP.md`, `AGENTS.md` and `AI_KNOWLEDGE_BASE.md` to identify the task and likely repositories.
2. If the current assistant is already authenticated for the owner's private GitHub access, inspect `pedrograd/pedrograd-ai-os` directly, including `AGENTS.md`, `docs/REPOSITORY_INTEGRATIONS.md`, and `config/repository_routes.json` **after the private router PR is reviewed and merged**.
3. For a local authorized checkout of that private repo, run `python scripts/repo_router.py --brand CODEPIXL --task "responsive mobile motion"` or `--check` to get the intended target and a reviewed list of **reference-only** forks.
4. Independently verify the selected target's current language, framework, upstream licenses, security, test commands, current owner-provided requirements, operational state, and cost/permission boundaries.
5. Implement one scoped change in the **existing** target repository, with a dedicated branch, tests, rollback and a draft PR. Never write to public forks to store owner state.
6. Record verified outcome in the existing private non-sensitive handoff. No second task master or scheduling loop.

## Never treat a reference as a live installation

A fork, star, package name or GitHub repository means only that source metadata is discoverable. Do **not** auto-run `curl | bash`, install dependencies, copy third-party code to private sites, deploy OpenHands/Langflow/OpenClaw or initiate any billed API/trading action as a consequence of a routing suggestion. Check license, security advisories, provenance, dependencies and actual project fit first.

Public project catalog `generated/github_catalog.json` has fork fields for some public repos, but is a snapshot, can be stale, and intentionally does not include private code. When GitHub Actions has quota/billing restrictions, the catalog refresh cannot be presumed current.

**Current status (2026-11-09):** private integration router is prepared in a review branch and is **not merged or deployed**. This public bridge is also a draft until its PR is reviewed. Other LLMs do not automatically receive this text or private repository access.
