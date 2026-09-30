# Security and Secret Handling

- Never hardcode secrets, tokens, API keys, private keys, passwords or connection strings.
- Never commit .env files containing real credentials.
- Use environment variables and provider secret stores.
- Treat logs as potentially public: redact tokens, authorization headers and sensitive identifiers.
- Validate untrusted input at every external boundary.
- Apply least privilege for GitHub tokens, cloud credentials and service accounts.
- Do not copy private repository code or private user data into the public My-AI repository.
- Third-party repository ingestion is allowed only for public repositories unless explicitly approved.
- Destructive production actions require a verified backup/rollback path when applicable.
