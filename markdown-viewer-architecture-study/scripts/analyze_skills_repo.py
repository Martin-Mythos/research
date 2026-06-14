#!/usr/bin/env python3
"""Analyze markdown-viewer/skills repository structure without vendoring it."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def infer_engine(text: str, rel: str) -> str:
    lower = text.lower()
    if "```dot" in lower:
        return "Graphviz DOT"
    if "```vega-lite" in lower or "```vega" in lower:
        return "Vega/Vega-Lite"
    if "```canvas" in lower:
        return "JSON Canvas"
    if "```infographic" in lower or "template-based infographics" in lower or "available templates" in lower:
        return "Infographic template syntax"
    if "direct html" in lower or "<style scoped>" in lower or "never use code blocks" in lower:
        return "Direct HTML/CSS"
    if "plantuml" in lower or "@startuml" in lower or "@startmindmap" in lower:
        return "PlantUML"
    return "Unknown"


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: analyze_skills_repo.py <repo> <output-dir>", file=sys.stderr)
        return 2
    repo = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve()
    out.mkdir(parents=True, exist_ok=True)

    skill_files = sorted(repo.glob("*/SKILL.md"))
    rows = []
    for sf in skill_files:
        text = sf.read_text(encoding="utf-8")
        rel = sf.relative_to(repo).as_posix()
        meta = parse_frontmatter(text)
        folder = sf.parent
        rows.append({
            "skill": meta.get("name", sf.parent.name),
            "path": rel,
            "engine": infer_engine(text, rel),
            "description": meta.get("description", ""),
            "examples": len(list((folder / "examples").glob("*.md"))) if (folder / "examples").exists() else 0,
            "references": len(list((folder / "references").glob("*.md"))) if (folder / "references").exists() else 0,
            "layouts": len(list((folder / "layouts").glob("*.md"))) if (folder / "layouts").exists() else 0,
            "styles": len(list((folder / "styles").glob("*.md"))) if (folder / "styles").exists() else 0,
            "stencils": len(list((folder / "stencils").glob("*.md"))) if (folder / "stencils").exists() else 0,
        })

    manifests = []
    manifest_names = {"package.json", "requirements.txt", "pyproject.toml", "Cargo.toml", "go.mod", "Makefile", "Dockerfile"}
    for p in repo.rglob("*"):
        if p.is_file() and p.name in manifest_names:
            manifests.append(p.relative_to(repo).as_posix())

    data = {
        "repo": "https://github.com/markdown-viewer/skills",
        "commit": git(repo, "rev-parse", "HEAD"),
        "tracked_files": int(git(repo, "ls-files").count("\n") + 1) if git(repo, "ls-files") else 0,
        "skill_count": len(rows),
        "manifests": manifests,
        "skills": rows,
    }
    (out / "skill_inventory.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    md = ["# Skill Inventory Matrix", "", f"Source commit: `{data['commit']}`", "", f"Tracked files: {data['tracked_files']}", f"Detected skills: {data['skill_count']}", f"Runtime/build manifests detected: {len(manifests)}", "", "| Skill | Engine | Examples | References | Layouts | Styles | Stencils |", "|---|---|---:|---:|---:|---:|---:|"]
    for r in rows:
        md.append(f"| `{r['skill']}` | {r['engine']} | {r['examples']} | {r['references']} | {r['layouts']} | {r['styles']} | {r['stencils']} |")
    (out / "skill_inventory_matrix.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"commit": data["commit"], "skill_count": len(rows), "manifests": len(manifests)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
