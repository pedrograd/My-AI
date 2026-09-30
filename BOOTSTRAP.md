# PEDROGRAD UNIVERSAL AI BOOTSTRAP

You are working for @pedrograd.

## Load order

For every substantial software, architecture, automation, debugging or repository task:

1. Read this file.
2. Read `AGENTS.md`.
3. Read `AI_KNOWLEDGE_BASE.md`.
4. Load only the rule files relevant to the current task.
5. Identify the target repository.
6. Inspect the target repository's current default branch, project instructions, tests, CI and runtime state when those sources are available.
7. Prefer reuse of an existing verified pattern over inventing a duplicate system.

Do not load the entire knowledge base when a narrow subset is sufficient.

## Source-of-truth priority

When sources disagree:

1. Live authorized runtime/provider state.
2. Current target repository default branch and CI.
3. Canonical database/application state where applicable.
4. Target repository project-state documentation.
5. This My-AI repository's curated knowledge.
6. Historical chats, old prompts and stale notes.

## Repository discovery

Before introducing a new framework, dependency, service or pattern:

- Search `AI_KNOWLEDGE_BASE.md`.
- Check the generated GitHub catalog if present.
- Inspect matching repositories natively through GitHub first.
- Reuse only after compatibility, license, maintenance and security checks.

GitIngest is an optional fallback for public repositories only. Never send private repository contents to a third-party ingestion service without explicit authorization.

## Safety and secrets

Never print, commit or copy secrets into this repository.
Use environment variables and secret managers.
Do not copy private repository source into this public repository.
Do not claim deployment, migration, fix or test success unless verified.

## Execution loop

INSPECT → RECONCILE → PLAN → IMPLEMENT → TEST → VERIFY → RECORD → REPORT

## Portable command

If you cannot automatically load repository files, open:

https://raw.githubusercontent.com/pedrograd/My-AI/main/BOOTSTRAP.md

Then continue from this document.
