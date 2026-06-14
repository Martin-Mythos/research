# Working Notes

## Original prompt / research question

Investigate `https://github.com/markdown-viewer/skills` empirically and answer: What foundational technical principles drive the project, and how can its system architecture and data flow be accurately visualized?

## Revision prompt

The previous PR was unsatisfactory. I attempted to check PR review comments, but the local repository has no GitHub remote and `gh` is not installed. I revised the research package to address likely review concerns: insufficient empirical evidence, stale skill counts, lack of reusable analysis code, shallow architecture mapping, and malformed setup-log output.

## Commands, scripts, data sources, and URLs actually used

- URL: `https://github.com/markdown-viewer/skills`
- `git clone https://github.com/markdown-viewer/skills /tmp/markdown-viewer-skills`
- `cd /tmp/markdown-viewer-skills && git rev-parse HEAD`
- `cd /tmp/markdown-viewer-skills && git ls-files | wc -l`
- `cd /tmp/markdown-viewer-skills && find . -maxdepth 2 -name SKILL.md | sort | sed 's#^./##'`
- `cd /tmp/markdown-viewer-skills && rg --files | rg 'package.json|requirements.txt|pyproject.toml|Cargo.toml|go.mod|Makefile|Dockerfile'`
- `scripts/analyze_skills_repo.py /tmp/markdown-viewer-skills artifacts`
- `python3 -m json.tool markdown-viewer-architecture-study/artifacts/skill_inventory.json >/tmp/skill_inventory.validated.json`
- Markdown fence-balance validation script embedded in `run_log.md`.

## Experiments attempted and outcomes

1. **Runtime-manifest discovery**
   - Outcome: no app/build manifests detected.
   - Interpretation: repository is not a runnable application; it is a skill/specification library consumed by external agent/rendering runtimes.
2. **Skill inventory extraction**
   - Outcome: 15 skills detected at commit `a3afd455b3ad37c0e71c05fa9407c4ec377226e3`.
   - Interpretation: prior report's 14-skill statement was stale and has been corrected.
3. **Renderer-engine inference**
   - Outcome: skills cluster into PlantUML, Direct HTML/CSS, Vega/Vega-Lite, JSON Canvas, and Graphviz DOT output contracts.
4. **Artifact validation**
   - Outcome: JSON inventory validates; Markdown fences are balanced.

## Failed paths and why abandoned

- Fetching PR review comments via `gh pr view` failed because `gh` is unavailable.
- Fetching comments from a configured GitHub remote failed because this local checkout has no remote configured.
- Running an application-level smoke test was abandoned because the target repository has no runnable app entry point or package manifest.

## Verification evidence worth preserving

- `run_log.md` records exact commands and outcomes.
- `artifacts/skill_inventory.json` records the target commit, tracked-file count, skill count, and per-skill engine classification.
- `artifacts/skill_inventory_matrix.md` provides human-readable evidence from the generated inventory.
