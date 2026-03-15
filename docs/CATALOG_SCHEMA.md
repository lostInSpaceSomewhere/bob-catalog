# Catalog Schema

## `catalog.json`

Required top-level keys:
- `catalog_version` (string)
- `name` (string)
- `items` (array)

## Item schema

Each item requires:
- `id` (string)
- `type` (`skill` | `workflow` | `agent`)
- `name` (string)
- `description` (string)
- `version` (semver string)
- `manifest_path` (path string, file must exist)
- `permissions` (array of permission tokens)
- `git_sha` (string; release can update this)

## Permission token format

Pattern:
- `domain:action`
- `domain:action:scope`
- `domain:action:scope:detail` (allowed when needed)

All segments must be lowercase with `a-z`, `0-9`, `_`, or `-`.
