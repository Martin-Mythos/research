# Technical Principles and Architecture Reverse Engineering of Markdown-Viewer/Skills

## Final conclusion

`markdown-viewer/skills` is best understood as a **declarative, contract-driven skill library** rather than a runnable application. Its architecture turns a user's natural-language visualization request into a renderer-specific Markdown artifact by combining skill-selection metadata, strict syntax rules, examples, and references. Rendering is deliberately outside the repository boundary and is handled by Markdown Viewer or a compatible host.

## Research question and scope

**Question:** What foundational technical principles drive this project, and how can its system architecture and data flow be accurately visualized?

**Scope:** This study analyzes the repository structure, `SKILL.md` contracts, examples/references/templates, renderer families, and the request-to-artifact flow. It does not benchmark Markdown Viewer's renderer implementation because that renderer is not included in the target repository.

## Methods and sources

- Cloned `https://github.com/markdown-viewer/skills` into `/tmp/markdown-viewer-skills`.
- Analyzed commit `a3afd455b3ad37c0e71c05fa9407c4ec377226e3`.
- Enumerated tracked files, skill modules, manifests, renderer families, and support directories.
- Created `scripts/analyze_skills_repo.py` to reproduce the inventory.
- Generated `artifacts/skill_inventory.json` and `artifacts/skill_inventory_matrix.md`.

## Verified findings

1. The analyzed target snapshot contains **15 skill modules**.
2. The repository contains **252 tracked files** at the analyzed commit.
3. No standard app/build manifests were detected, so there is no local application runtime to start.
4. Skills dispatch to multiple output families: PlantUML, Graphviz DOT, JSON Canvas, Vega/Vega-Lite, direct HTML/CSS, and infographic template syntax.
5. The dominant design pattern is **contract-first generation**: each skill constrains the agent's output to a renderer grammar.

## Architecture artifacts

- `artifacts/architecture_diagrams.md` contains Mermaid system, sequence, and dispatch diagrams.
- `research_report.md` embeds and explains the core architecture and data-flow model.
- `evaluation_matrix.md` scores maintainability, scalability, clarity, runtime verifiability, extensibility, and reproducibility.

## Reproduction instructions

```bash
git clone https://github.com/markdown-viewer/skills /tmp/markdown-viewer-skills
/workspace/research/markdown-viewer-architecture-study/scripts/analyze_skills_repo.py /tmp/markdown-viewer-skills /workspace/research/markdown-viewer-architecture-study/artifacts
python3 -m json.tool /workspace/research/markdown-viewer-architecture-study/artifacts/skill_inventory.json >/tmp/skill_inventory.validated.json
```

## Limitations and risks

- PR review comments could not be fetched in this environment because no GitHub remote is configured and `gh` is unavailable.
- Renderer behavior is inferred from repository contracts and not from Markdown Viewer's implementation.
- Skill metadata is prose/Markdown-oriented; without a formal schema, some classification depends on text-pattern inference.

## Next steps

1. Add a CI job to validate `SKILL.md` frontmatter and required sections.
2. Add renderer smoke tests for representative fenced blocks (`plantuml`, `dot`, `canvas`, `vega-lite`) and direct HTML/CSS examples.
3. Generate a repository index from skill metadata to avoid stale README counts.
