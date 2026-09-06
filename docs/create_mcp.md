[← Back to setup](setup.md)

# Mailpit MCP

An MCP server that reads mail from Mailpit's REST API (`http://localhost:8025/api/v1`), exposing standard methods as tools. Implemented in Python at [mcp/server.py](../mcp/server.py):

- **list_messages** — list inbox messages, with pagination
- **search_messages** — search by query (sender, subject, date range, etc.)
- **get_message** — fetch a single message by ID (headers + body)
- **get_attachment** — fetch an attachment from a message

These map directly to Mailpit's existing REST endpoints — the MCP layer just wraps them as callable tools for Claude.

## Bring it up

```text
claude mcp add mailpit -- mcp/run.sh
```

[mcp/run.sh](../mcp/run.sh) creates the `.venv`, installs requirements, and runs the server.

Verify with `claude mcp list` (should show `mailpit` connected), then ask Claude something like "list the emails in Mailpit" to confirm the tools work.
