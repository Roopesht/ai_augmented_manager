from server import search_messages

result = search_messages("subject:leave")
messages = result.get("messages", [])
assert len(messages) > 0, "expected at least one message matching 'subject:leave'"
print(f"OK: found {len(messages)} messages matching 'subject:leave'")
