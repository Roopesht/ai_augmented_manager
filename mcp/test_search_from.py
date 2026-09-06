from server import search_messages

result = search_messages("from:arjun")
messages = result.get("messages", [])
assert len(messages) > 0, "expected at least one message matching 'from:arjun'"
print(f"OK: found {len(messages)} messages matching 'from:arjun'")
