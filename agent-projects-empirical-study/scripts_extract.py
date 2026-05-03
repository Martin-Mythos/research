import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = SCRIPT_DIR / "artifacts"
UPSTREAM_DIR = ARTIFACTS_DIR / "upstream"
OUTPUT_PATH = ARTIFACTS_DIR / "static_signal_scan.json"

files = list(UPSTREAM_DIR.glob("*.py")) + list(UPSTREAM_DIR.glob("*.md"))
report = {}
for f in files:
    t = f.read_text(errors="ignore")
    report[f.name] = {
        "oauth_mentions": len(re.findall(r"\b(?:oauth2?|bearer|auth(?:entication|orization)?)\b", t, re.I)),
        "mcp_mentions": len(re.findall(r"\bMCP\b|model context protocol", t, re.I)),
        "rerank_mentions": len(re.findall(r"\brerank(?:ing|er)?\b", t, re.I)),
        "sandbox_mentions": len(re.findall(r"\b(?:sandbox|docker|e2b)\b", t, re.I)),
    }

OUTPUT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False))
print("written", len(report), "->", OUTPUT_PATH)
