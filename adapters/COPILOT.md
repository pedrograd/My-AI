# GitHub Copilot Adapter

Repository-level Copilot instructions should follow the same shared contract:

1. Read the local project architecture and instructions.
2. Apply PEDROGRAD reuse/security/testing principles from My-AI.
3. Search existing code and repository catalog before introducing new dependencies.
4. Never expose secrets.
5. Verify tests and CI after changes.

The installer creates a lightweight .github/copilot-instructions.md pointer.
