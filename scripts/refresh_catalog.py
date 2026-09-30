from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

OWNER = os.getenv("MY_AI_GITHUB_OWNER", "pedrograd")
TOKEN = os.getenv("MY_AI_GITHUB_TOKEN") or os.getenv("GITHUB_TOKEN")
OUT = Path("generated/github_catalog.json")


def request_json(url: str) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "pedrograd-my-ai-catalog",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def paginated(url: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    page = 1
    while True:
        sep = "&" if "?" in url else "?"
        batch = request_json(f"{url}{sep}per_page=100&page={page}")
        if not isinstance(batch, list) or not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return items


def slim(repo: dict[str, Any], relation: str) -> dict[str, Any]:
    return {
        "relation": relation,
        "full_name": repo.get("full_name"),
        "html_url": repo.get("html_url"),
        "description": repo.get("description"),
        "fork": bool(repo.get("fork")),
        "private": bool(repo.get("private")),
        "archived": bool(repo.get("archived")),
        "language": repo.get("language"),
        "default_branch": repo.get("default_branch"),
        "updated_at": repo.get("updated_at"),
        "license": (repo.get("license") or {}).get("spdx_id"),
        "topics": repo.get("topics") or [],
    }


def main() -> None:
    owned = paginated(f"https://api.github.com/users/{OWNER}/repos?type=owner&sort=updated")
    starred = paginated(f"https://api.github.com/users/{OWNER}/starred?sort=updated")

    combined: dict[str, dict[str, Any]] = {}
    for repo in owned:
        item = slim(repo, "owned")
        combined[item["full_name"]] = item

    for repo in starred:
        full_name = repo.get("full_name")
        if full_name in combined:
            combined[full_name]["starred"] = True
        else:
            item = slim(repo, "starred")
            item["starred"] = True
            combined[full_name] = item

    payload = {
        "owner": OWNER,
        "note": "Generated metadata only. AI_KNOWLEDGE_BASE.md is the curated authority.",
        "repositories": sorted(
            combined.values(),
            key=lambda x: (x.get("relation", ""), x.get("full_name", "")),
        ),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"GitHub API error: {exc.code} {exc.reason}") from exc
