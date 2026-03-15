# Google Connector Manual Test Matrix (M2)

Use this matrix in PR evidence.

## Preconditions

- Bob runtime M1 integration plumbing is present in the app.
- Google OAuth provider config is set and connected.
- Bob Official catalog source is synced.

## Test Cases

1. Gmail read path
- Skill: `google-gmail-search`
- Expected: returns accepted integration result; no write approval required.

2. Gmail write path
- Skill: `google-gmail-send`
- Expected: approval prompt required; action proceeds only after approval.

3. Calendar read path
- Skill: `google-calendar-list-events`
- Expected: returns accepted integration result; no write approval required.

4. Calendar write path
- Skill: `google-calendar-create-event`
- Expected: approval prompt required.

5. Drive read path
- Skill: `google-drive-list-files`
- Expected: returns accepted integration result; no write approval required.

6. Drive write path
- Skill: `google-drive-write-file`
- Expected: approval prompt required.

## Failure Mode Checks

- Revoke OAuth and run any skill: clear missing-credentials error.
- Force expired token without refresh token: clear reconnect-required error.
