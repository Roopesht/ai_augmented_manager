[← Back to setup](setup.md)

# Configure Mailpit MCP in Claude Desktop

1. Open (create if missing): `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Add the `mailpit` server:

```json
{
  "mcpServers": {
    "mailpit": {
      "command": "/Users/roopesh/projects/ai_augmented_manager/mcp/.venv/bin/python",
      "args": ["/Users/roopesh/projects/ai_augmented_manager/mcp/server.py"]
    }
  }
}
```

3. Restart Claude Desktop.
4. Verify: in a new chat, ask Claude to list emails from Mailpit — it should call the `mailpit` tools.
