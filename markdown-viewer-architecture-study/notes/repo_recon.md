# Repository Reconnaissance

## Target snapshot

- Repository: `https://github.com/markdown-viewer/skills`
- Commit analyzed: `a3afd455b3ad37c0e71c05fa9407c4ec377226e3`
- Tracked files: 252
- Detected skill modules: 15
- App/build manifests detected: 0

## Project purpose

`markdown-viewer/skills` is a library of agent-facing skill specifications for producing visual artifacts in Markdown. It does not implement a rendering engine itself. Instead, it encodes routing guidance, syntax contracts, examples, references, styles, layouts, and stencils that an AI coding agent can use to emit renderer-specific diagram source.

## Main technology stack

| Layer | Evidence | Role |
|---|---|---|
| Skill metadata | `*/SKILL.md` YAML frontmatter | Identifies each skill and tells an agent when to use it. |
| Instruction contracts | `*/SKILL.md` body | Provides critical syntax rules, common pitfalls, and generation workflow. |
| Example corpora | `*/examples/*.md` | Shows valid domain-specific outputs. |
| Reference corpora | `references/`, `stencils/`, `layouts/`, `styles/` | Supplies reusable syntax, visual conventions, icon namespaces, and templates. |
| External renderer | Markdown Viewer / compatible host | Converts emitted PlantUML, DOT, JSON Canvas, Vega, or direct HTML/CSS into visuals. |

## Core components

1. **Catalog/router (`README.md`)** — maps user intent to skill choice and rendering engine family.
2. **Skill contract (`SKILL.md`)** — constrains generation with frontmatter, quick-start path, critical rules, and examples.
3. **Reference expansion** — skill-specific examples/references/stencils/layouts/styles provide additional context when the base contract is insufficient.
4. **Artifact emitter** — the AI agent creates Markdown containing a fenced source block (`plantuml`, `dot`, `canvas`, `vega-lite`, `vega`) or raw HTML/CSS.
5. **Renderer boundary** — Markdown Viewer or a compatible Markdown host parses and renders the emitted artifact.

## Important correction from the previous draft

The initial draft described 14 skills. The current target snapshot contains 15 skill modules because `graphviz/SKILL.md` is present. This correction is backed by `artifacts/skill_inventory.json` and `artifacts/skill_inventory_matrix.md`.
