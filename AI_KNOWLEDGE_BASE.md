# AI KNOWLEDGE BASE

Curated repository map for @pedrograd. This is metadata and guidance, not a mirror of private code.

## Canonical active projects

### pedrograd/telegram-ai-sales
Role: primary backend / Telegram sales and business orchestrator.
Classification: PRODUCTION PROJECT.
Policy: inspect existing architecture before adding services; do not duplicate customer/payment/application state.

### pedrograd/Pedrograd
Role: owner PWA / control center.
Classification: PRODUCTION PROJECT.
Policy: owner-facing operations and reporting UI belong here unless the current architecture says otherwise.

### pedrograd/Acnoctem
Role: public web/funnel.
Classification: PRODUCTION PROJECT.
Policy: public web/funnel changes belong here; do not turn it into a duplicate backend.

### pedrograd/NeuraLogy-AI-
Role: React Native / Expo AI personal-development application.
Classification: ACTIVE APPLICATION.
Useful for: mobile AI app structure, Zustand, React Query and service-layer patterns.

## Reusable AI / engineering repositories

### pedrograd/agent-rules
Classification: REFERENCE / RULE LIBRARY.
Useful for: context priming, bug fixing, implementation workflow, PR review, changelog, code analysis and MCP practices.
Policy: select relevant rules; do not bulk-import everything.

### pedrograd/Prompt-book
Classification: PROMPT LIBRARY.
Useful for: specialist roles and prompt patterns.
Policy: route to a relevant prompt on demand; do not inject the entire prompt collection into every session.

### pedrograd/cursor-memory-bank
Classification: REFERENCE.
Useful for: durable task state, context loading and planning/implementation/reflection/archive workflow.

### pedrograd/auto_PRD
Classification: TEMPLATE / REFERENCE.
Useful for: PRD generation, implementation planning and project bootstrapping.

### pedrograd/OpenHands
Classification: SERVICE / TOOLING.
Useful for: self-hosted coding-agent control plane, agent automation and multiple agent backends.

### pedrograd/langflow
Classification: SERVICE / TOOLING.
Useful for: visual agent workflows, API/MCP prototypes and multi-agent orchestration.

### pedrograd/vibe-tools
Classification: TOOLING / REFERENCE.
Useful for: agent tools, MCP, testing and browser automation patterns.

### pedrograd/how-to-build-a-coding-agent
Classification: EDUCATIONAL REFERENCE.
Useful for: agent event loops, tool registries and file/shell/edit/search tool design.

### pedrograd/awesome-cursorrules
Classification: REFERENCE.
Useful for: project-specific AI rule examples.

### pedrograd/system-prompts-and-models-of-ai-tools
Classification: RESEARCH ONLY.
Useful for: studying prompt structures and AI-tool behavior.
Policy: never blindly copy external system prompts into production instructions.

### pedrograd/My-AI
Classification: AI KNOWLEDGE / GOVERNANCE HUB.
Role: portable rules, bootstrap instructions, repository catalog and AI adapters.
Policy: this is not a production backend or canonical application-state store.

## Additional owned repositories

The account also contains repositories such as REPL, myGame, War-Thunder, MoneyPrinterTurbo, devin.cursorrules, FansPilots, minikoyunlar, AInfluencer, ComfyUI_examples, CodePixl, FatmaTerzi, e-book, documents, tgbot, prompts.chat and public-apis.

Their role must be discovered from current repository content before reuse. Do not infer production status from name alone.

## Generated catalog

When available, see `generated/github_catalog.json` for automatically refreshed public owned/starred repository metadata. Curated entries in this file override automated classification.
