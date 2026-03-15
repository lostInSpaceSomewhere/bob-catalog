#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
PERM = re.compile(r"^[a-z0-9_-]+:[a-z0-9_-]+(?::[a-z0-9_-]+){0,2}$")
VALID_TYPES = {"skill", "workflow", "agent"}


def fail(msg: str) -> None:
    print(f"[catalog-validate] ERROR: {msg}")
    sys.exit(1)


def main() -> None:
    if not CATALOG.exists():
        fail("catalog.json not found")

    try:
        data = json.loads(CATALOG.read_text())
    except Exception as exc:
        fail(f"catalog.json is invalid JSON: {exc}")

    for key in ("catalog_version", "name", "items"):
        if key not in data:
            fail(f"missing top-level key '{key}'")

    if not isinstance(data["items"], list):
        fail("'items' must be an array")

    ids = set()
    for i, item in enumerate(data["items"]):
        ctx = f"items[{i}]"
        for key in ("id", "type", "name", "description", "version", "manifest_path", "permissions", "git_sha"):
            if key not in item:
                fail(f"{ctx}: missing '{key}'")

        item_id = item["id"]
        if item_id in ids:
            fail(f"{ctx}: duplicate id '{item_id}'")
        ids.add(item_id)

        if item["type"] not in VALID_TYPES:
            fail(f"{ctx}: invalid type '{item['type']}'")
        if not SEMVER.match(item["version"]):
            fail(f"{ctx}: version must be semver X.Y.Z")

        manifest = ROOT / item["manifest_path"]
        if not manifest.exists():
            fail(f"{ctx}: manifest_path does not exist: {item['manifest_path']}")

        perms = item["permissions"]
        if not isinstance(perms, list):
            fail(f"{ctx}: permissions must be an array")
        for p in perms:
            if not isinstance(p, str) or not PERM.match(p):
                fail(f"{ctx}: invalid permission token '{p}'")

    print("[catalog-validate] OK")


if __name__ == "__main__":
    main()
