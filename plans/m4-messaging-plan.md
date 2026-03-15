# M4 Plan: Messaging Connectors

## Scope

- Telegram end-to-end first
- iMessage send path
- Signal path with dependency gating

## Strict gates

- Write/send actions require provider write permission token
- Dependency checks and failure guidance required
- Channel setup docs required
- Manual evidence required for each implemented channel
