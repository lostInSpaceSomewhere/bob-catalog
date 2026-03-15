# Bob Official Catalog

Official catalog repository for Bob first-party and curated partner capabilities.

This repo contains **catalog content only**:
- Skills
- Workflows
- Agent roles
- Connector manifests and docs

This repo does **not** contain Bob app runtime code. Runtime/security/approval logic lives in:
- `lostInSpaceSomewhere/bob`

## Repository Layout

```text
.
├── catalog.json                  # index consumed by Bob app
├── skills/                       # skill manifests
├── workflows/                    # workflow manifests
├── agents/                       # agent role manifests
├── connectors/                   # provider-specific docs/assets
│   ├── google/
│   ├── apple/
│   └── messaging/
├── docs/
│   ├── BUILD_GUIDELINES.md       # strict contribution rules
│   ├── CATALOG_SCHEMA.md         # required index/manifest contracts
│   └── release-checklist.md      # release quality gate
├── scripts/
│   └── validate_catalog.py       # schema + policy validator
└── .github/workflows/
    └── validate-catalog.yml      # CI gate
```

## Core Rules

1. First-party connector content ships from this repository, not the Bob app repo.
2. Every catalog item must declare required permissions.
3. Destructive/write capabilities must be explicitly marked and documented.
4. `catalog.json` must pass CI validation before merge.

## Release Model

- `main` contains releasable catalog content.
- Tag releases as `vX.Y.Z` when connector bundles are ready.
- Keep changelog entries in PR descriptions and release notes.

## M2–M4 Parallel Tracks

- M2: Google (Gmail/Calendar/Drive)
- M3: Apple (Notes/Reminders/Mail)
- M4: Messaging (Telegram/iMessage/Signal)

Track details and strict acceptance criteria are in:
- `plans/m2-google-plan.md`
- `plans/m3-apple-plan.md`
- `plans/m4-messaging-plan.md`
Official Bob catalog repository for first-party skills and connectors
