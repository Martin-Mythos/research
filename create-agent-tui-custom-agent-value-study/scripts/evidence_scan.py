from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
UP = ROOT / "artifacts/upstream"

checks = [
    ("tool display modes", "SKILL.md", "four tool display modes"),
    ("session persistence", "SKILL.md", "session persistence"),
    ("approval metadata", "SKILL.md", "approval"),
    ("layered config", "SKILL.md", "layered config"),
    ("three-layer architecture", "references-architecture.md", "three-layer"),
    ("server entry points", "references-server-entry-points.md", "entry point"),
    ("slash commands", "sample-src/commands.ts", "commands"),
    ("session file", "sample-src/session.ts", "session"),
]

findings = []
for label, rel, needle in checks:
    p = UP / rel
    txt = p.read_text(errors="ignore").splitlines()
    hit_line = None
    hit_text = None
    for i, line in enumerate(txt, start=1):
        if needle.lower() in line.lower():
            hit_line = i
            hit_text = line.strip()
            break
    findings.append({
        "label": label,
        "file": str(p.relative_to(ROOT)),
        "needle": needle,
        "found": hit_line is not None,
        "line": hit_line,
        "excerpt": hit_text,
    })

out = ROOT / "artifacts/results/evidence_scan.json"
out.write_text(json.dumps(findings, ensure_ascii=False, indent=2))
print(f"Wrote {out}")
