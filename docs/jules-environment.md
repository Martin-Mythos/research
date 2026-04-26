# Jules Environment Setup

This document records the recommended Jules environment configuration for this repository.

## Setup Script

Use this script in Jules **Environment -> Setup script**. Jules clones the repository into `/app`, so no clone command is needed.

```bash
set -euxo pipefail

cd /app

python3 -m venv .venv
. .venv/bin/activate

python -m pip install --upgrade pip wheel
python -m pip install -r requirements.txt

# Verify core repo files
test -f AGENTS.md
test -f README.md
test -f requirements.txt
test -d .agents/skills/open-research

# Verify Python CLI dependencies
cog --version
llm --version

# Lightweight skill contract check without requiring local aspg
python - <<'PY'
from pathlib import Path

skill = Path(".agents/skills/open-research/SKILL.md")
text = skill.read_text()

assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
assert "\nname: open-research\n" in text, "missing skill name"
assert "\ndescription:" in text, "missing skill description"
assert Path(".agents/skills/open-research/references/prompt-templates.md").exists()
assert Path(".agents/skills/open-research/references/research-contract.md").exists()
assert Path(".agents/skills/open-research/agents/openai.yaml").exists()

print("open-research skill contract OK")
PY

# If ASPG happens to be available in Jules, use it; otherwise skip.
if command -v aspg >/dev/null 2>&1; then
  aspg lint
  aspg doctor
  aspg compat open-research
else
  echo "aspg not installed; skipping ASPG checks"
fi

git diff --check

echo "Jules environment setup complete"
```

## Environment Variables

No environment variables are required for the default setup.

Do not add GitHub tokens or other credentials unless a specific research task needs authenticated API access. Jules environment variables are available during setup and may be visible to the agent during task execution when enabled.

## Network Access

Keep network access enabled. This repository is intended for open research workflows where agents may need to read documentation, fetch public repositories, install packages, or inspect public web resources.

## Why the Script Avoids `cog -r -P README.md`

The repository README automation can call `llm-github-models` to generate summaries. Running it during environment setup may require GitHub model credentials and may modify files, which makes the setup snapshot less deterministic.

The setup script only installs dependencies and verifies the repository contract. README regeneration should remain in GitHub Actions or be run intentionally during a task.
