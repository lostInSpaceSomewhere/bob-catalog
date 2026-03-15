# Build Guidelines (Strict)

These rules are mandatory for all skills/connectors merged into this repository.

## 1) Manifest Quality

- `id` must be stable and unique.
- `version` must be semantic (`X.Y.Z`).
- `description` must state user-visible behavior and side effects.
- `manifest_path` in `catalog.json` must resolve to an existing file.

## 2) Permission Integrity

- Declare every required permission in `catalog.json`.
- Use `domain:action:scope` token format.
- Use least privilege.

Examples:
- `network:oauth:google`
- `integration:write:google`
- `file:read`

## 3) Safety Requirements

- Write/send/modify behavior must be explicit in docs and description.
- No hidden destructive behavior.
- Missing credential/dependency behavior must fail clearly and safely.

## 4) Documentation Requirements

Each connector/skill PR must include:
- Setup instructions
- Required tokens/credentials
- Common failure cases and fixes

## 5) Validation Requirements

Before merge:
- `scripts/validate_catalog.py` must pass
- CI `validate-catalog` must pass
- PR must include manual test evidence for read/write paths where applicable
