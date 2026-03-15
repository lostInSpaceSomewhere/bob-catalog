# Google Connectors (M2)

This folder documents official Google connector content shipped in `catalog.json`.

## Implemented Skills

- `google-gmail-search` (read)
- `google-gmail-send` (write)
- `google-calendar-list-events` (read)
- `google-calendar-create-event` (write)
- `google-drive-list-files` (read)
- `google-drive-write-file` (write)

## Required Permissions

- All Google skills require: `network:oauth:google`
- Write/send/modify Google skills additionally require: `integration:write:google`

## Setup

1. In Bob app, configure Google OAuth settings for provider `google`:
   - `client_id`
   - `client_secret` (if required)
   - `auth_url`
   - `token_url`
   - `redirect_uri`
   - scopes required for Gmail, Calendar, and Drive operations
2. Start OAuth from Bob integration controls and complete code exchange.
3. Add/confirm the Bob Official catalog source.
4. Enable desired Google skills from Settings -> Catalogs.
5. Run a read skill first, then a write skill and verify approval prompts appear.

## Troubleshooting

- `Missing credentials for 'google'`: OAuth is not connected; complete OAuth first.
- `Credentials for 'google' are expired`: refresh token is missing/invalid; reconnect OAuth.
- Write action denied: expected behavior if approval is rejected.
- Catalog item missing in UI: run catalog sync and confirm `catalog.json` contains the item.
