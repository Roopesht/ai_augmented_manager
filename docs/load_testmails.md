[← Back to setup](setup.md)

# Load Test Emails into Mailpit

Send the generated `.eml` files from [docs/tests/](tests/) into Mailpit via SMTP (`localhost:1025`).

```bash
for f in docs/tests/*.eml; do
  from=$(grep '^From:' "$f" | sed -E 's/.*<(.+)>/\1/')
  to=$(grep '^To:' "$f" | sed -E 's/.*<(.+)>/\1/')
  cc=$(grep '^Cc:' "$f" | sed -E 's/.*<(.+)>/\1/')
  rcpts=(--mail-rcpt "$to")
  [ -n "$cc" ] && rcpts+=(--mail-rcpt "$cc")
  curl -s smtp://localhost:1025 --mail-from "$from" "${rcpts[@]}" --upload-file "$f"
done
```

Verify: open `http://localhost:8025` and confirm all emails show up in the inbox, with To/Cc as expected.
