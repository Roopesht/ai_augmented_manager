[← Back to setup](setup.md)

# Generate Test Emails

For the 10 members in [setup_team.md](setup_team.md), generate ~100 emails dated 1-Aug to 31-Aug, sent via SMTP to Mailpit (`localhost:1025`), addressed to srikanth.devarapalli@ojasamirai.local:

- **~25 leave request emails** — mostly 1-day, a couple of longer ones (5-day, 10-day). Not every member takes leave (leave at least 2 out).
- **~75 standard emails** — regular work chatter (status updates, meeting notes, FYIs) to make the inbox realistic.

Each email should CC 1-3 people picked at random from [data/other_team.csv](../data/other_team.csv) (managers, HR, finance, client contacts, etc.) — not the recipient, just to mimic a realistic mail setup.

srikanth.devarapalli@ojasamirai.local is sometimes in **To**, sometimes in **Cc**. When he's in Cc, the **To** is someone from `other_team.csv` instead (e.g. a leave request addressed to HR, Srikanth cc'd for visibility).

## Output

- One file per email, under `docs/tests/`
- Format: raw `.eml` (RFC 822 — From/To/Cc/Subject/Date headers + plain-text body), ready to send via SMTP as-is
- Filename: `<seq>_<sender-name>.eml`, e.g. `001_arjun-mehta.eml`, `002_priya-nair.eml`

## Style (Indian corporate context)

- Leave type in subject/body: CL (Casual Leave), SL (Sick Leave), PL (Privilege/Earned Leave)
- Sign-off: "Thanks & Regards" / "Regards"
- Realistic reasons: family function/wedding/engagement at native place, festival travel (e.g. Raksha Bandhan, Janmashtami — both fall in Aug), medical appointment, child's school event
- Mention handover to a named colleague (from `team.csv`) and being reachable by phone for anything urgent
- Keep tone polite/formal ("Kindly approve", "Requesting one day of leave")

See [001_arjun-mehta.eml](tests/001_arjun-mehta.eml) as the reference sample.

## Prompt

```
Generate test email data for a Mailpit inbox demo.

Senders (name, email): data/team.csv
CC pool (name, email, role): data/other_team.csv

Recipient: srikanth.devarapalli@ojasamirai.local
Date range: 1-Aug-2025 to 31-Aug-2025

Produce two sets:

1. ~25 leave request emails, one per leave instance, spread across the
   team (skip at least 2 members entirely). Mostly single-day leave,
   with 2-3 longer ones (5 days, 10 days). Each email should state the
   sender's name, the leave date(s), and a one-line reason. Vary
   subject lines and phrasing naturally.

2. ~75 regular work emails from the same team members — status
   updates, meeting notes, quick FYIs — unrelated to leave, spread
   across the same date range, to make the inbox look realistic.

For every email, CC 1-3 random people from the CC pool.

Output each email as sender, date, subject, body, and cc list, ready
to be sent via SMTP to Mailpit.
```
