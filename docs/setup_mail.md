[← Back to setup](setup.md)

# Mailpit Setup

Mailpit is a local SMTP test server with a web inbox UI.

1. Install
   - macOS: `brew install mailpit`
   - Other platforms: see https://mailpit.axllent.org/docs/install/
2. Run: `mailpit`
   - SMTP listens on `localhost:1025`
   - Web UI on `http://localhost:8025`
3. Verify: open `http://localhost:8025` in a browser and confirm the inbox loads (empty is fine at this stage).
