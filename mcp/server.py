import base64
import os

import httpx
from mcp.server.fastmcp import FastMCP

MAILPIT_URL = os.environ.get("MAILPIT_URL", "http://localhost:8025").rstrip("/")

mcp = FastMCP("mailpit")


def _get(path: str, params: dict | None = None) -> httpx.Response:
    resp = httpx.get(f"{MAILPIT_URL}/api/v1{path}", params=params, timeout=10)
    resp.raise_for_status()
    return resp


@mcp.tool()
def list_messages(limit: int = 50, start: int = 0) -> dict:
    """List messages in the Mailpit inbox, most recent first."""
    return _get("/messages", {"limit": limit, "start": start}).json()


@mcp.tool()
def search_messages(query: str, limit: int = 50, start: int = 0) -> dict:
    """Search messages, e.g. 'from:arjun.mehta@ojasamirai.local' or 'subject:leave'."""
    return _get("/search", {"query": query, "limit": limit, "start": start}).json()


@mcp.tool()
def get_message(id: str) -> dict:
    """Fetch a single message by ID, including headers and body."""
    return _get(f"/message/{id}").json()


@mcp.tool()
def get_attachment(id: str, part_id: str) -> dict:
    """Fetch an attachment from a message, base64-encoded."""
    resp = _get(f"/message/{id}/part/{part_id}")
    return {
        "content_type": resp.headers.get("content-type", "application/octet-stream"),
        "content_base64": base64.b64encode(resp.content).decode("ascii"),
    }


if __name__ == "__main__":
    mcp.run()
