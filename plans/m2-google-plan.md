# M2 Plan: Google Connectors

## Scope

- Gmail read/search/send
- Calendar read/create/update
- Drive list/read/write

## Strict gates

- Must declare `network:oauth:google`
- Write actions must declare `integration:write:google`
- Setup + troubleshooting docs required in connector folder
- Read + write manual evidence required in PR
