import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
use_cases = json.loads((ROOT / "data/use_cases.json").read_text())

# Capability inventory from inspected create-agent-tui docs/sample code.
custom_agent_capabilities = {
    "basic_chat": 1,
    "tool_use": 1,
    "approval_flow": 1,
    "session_persistence": 1,
    "config_layers": 1,
    "streaming_ui": 1,
    "structured_logs": 1,
    "slash_commands": 1,
    "terminal_tui": 1,
    "tool_visibility_modes": 1,
    "server_entrypoint": 1,
    "modular_architecture": 1,
}

# Baseline comparison: generic chat app / direct API wrapper with no custom harness.
baseline_chat_capabilities = {
    "basic_chat": 1,
    "tool_use": 0,
    "approval_flow": 0,
    "session_persistence": 0,
    "config_layers": 0,
    "streaming_ui": 0,
    "structured_logs": 0,
    "slash_commands": 0,
    "terminal_tui": 0,
    "tool_visibility_modes": 0,
    "server_entrypoint": 0,
    "modular_architecture": 0,
}

def score(case, caps):
    reqs = case["requirements"]
    got = sum(caps.get(r, 0) for r in reqs)
    return {
        "covered": got,
        "total": len(reqs),
        "coverage": round(got / len(reqs), 2),
    }

rows = []
for c in use_cases:
    custom = score(c, custom_agent_capabilities)
    base = score(c, baseline_chat_capabilities)
    rows.append(
        {
            "id": c["id"],
            "name": c["name"],
            "requirements": c["requirements"],
            "custom_agent": custom,
            "baseline_chat": base,
            "delta": round(custom["coverage"] - base["coverage"], 2),
        }
    )

out = {
    "assumptions": {
        "baseline": "No custom harness; only basic chat completion UX",
        "custom_agent": "Capabilities declared in create-agent-tui docs and sample",
    },
    "results": rows,
}

result_path = ROOT / "artifacts/results/capability_matrix.json"
result_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))

md_lines = [
    "# Capability Coverage Experiment",
    "",
    "| Use case | Custom agent coverage | Baseline coverage | Delta |",
    "|---|---:|---:|---:|",
]
for r in rows:
    md_lines.append(
        f"| {r['name']} | {r['custom_agent']['covered']}/{r['custom_agent']['total']} ({r['custom_agent']['coverage']:.2f}) | "
        f"{r['baseline_chat']['covered']}/{r['baseline_chat']['total']} ({r['baseline_chat']['coverage']:.2f}) | {r['delta']:.2f} |"
    )

(ROOT / "artifacts/results/capability_matrix.md").write_text("\n".join(md_lines) + "\n")
print(f"Wrote {result_path}")
