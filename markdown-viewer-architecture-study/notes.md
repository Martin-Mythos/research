# Working Notes

## Original prompt / research question
- Investigate architecture of `https://github.com/markdown-viewer/skills` and explain foundational technical principles and data flow with Mermaid diagrams.

## Commands, scripts, and sources used
- `git clone https://github.com/markdown-viewer/skills /tmp/markdown-viewer-skills`
- `rg --files | head -n 200`
- `rg --files | rg 'package.json|requirements.txt|pyproject.toml|Cargo.toml|go.mod|Makefile|Dockerfile'`
- `sed -n '1,220p' README.md`
- `sed -n '1,220p' uml/SKILL.md`
- `sed -n '1,220p' canvas/SKILL.md`
- Data sources: GitHub repository files only.

## Experiments attempted and outcomes
- Attempted runtime dependency detection via manifest scan: no package/build manifests found. Outcome: repository is content/spec-driven, not executable application.
- Smoke test scope changed from executable runtime to schema/syntax validation of representative skill files.

## Failed paths
- Looking for standard entry points (`index.js`, `main.py`) failed because repo contains markdown skill definitions only.

## Verification evidence
- Manifest scan returned no results (exit code 1), supporting "non-runnable content repository" classification.
- README and SKILL files show explicit rendering contracts and code-fence protocols.
