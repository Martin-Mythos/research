# Notes: paper-craft-skills Transformer study

## Original prompt / research question
Investigate https://github.com/zsyggg/paper-craft-skills using Attention Is All You Need (arXiv:1706.03762), focusing on skill robustness, visual fidelity, artifact quality, and logic transparency. Produce Chinese reports and artifacts under `Martin-Mythos/research/paper-craft-skills-transformer-study/`.

## Commands, sources, and URLs actually used
- `cat /workspace/research/.agents/skills/open-research/SKILL.md && pwd && find .. -name AGENTS.md -print`
- `cat AGENTS.md; find . -maxdepth 3 -type f | sed 's#^./##' | head -80; node --version || true; npx --version || true; git status --short`
- Sources requested: GitHub repo https://github.com/zsyggg/paper-craft-skills ; arXiv https://arxiv.org/abs/1706.03762
- Environment: Node.js v20.20.2; npx 11.4.2.

## Experiments attempted and outcomes
- Workspace created with `artifacts/`, `notes/`, and `external/` subdirectories.

## Failed paths / abandoned paths
- None yet.

## Verification evidence
- Node and NPX are available; command output recorded above.
- `git clone --depth 1 https://github.com/zsyggg/paper-craft-skills external/paper-craft-skills`
- `find external/paper-craft-skills -maxdepth 3 -type f | sort`
- Read `README.md`, `README.zh.md`, `skills/paper-analyzer/SKILL.md`, `skills/paper-comic/SKILL.md`, `skills/paper-deck/SKILL.md`, `skills/paper-deck/references/style-system.md`, `skills/paper-deck/references/prompt-template.md`.
- Recon finding: repository exposes `paper-comic` with `paper-figure` and `sketchnote` as styles, not separate `paper-figure`/`sketchnote` skill directories.
- ArXiv direct `curl` failed with HTTP 403; browser tool successfully opened abs/html pages and confirmed metadata and section structure.
- Created artifacts: `analyzer_transformer.html`, `analyzer_demo.html`, `transformer_method_figure_prompts.txt`, `transformer_deck_outline.md`, `notes/deck_structure.md`, `evaluation_matrix.md`, `research_report.md`, `README.md`.
- Experiment outcome: repo source supports simulation; no actual raster image generation backend was invoked for paper-deck, so PPTX/PDF production-readiness remains unverified.
