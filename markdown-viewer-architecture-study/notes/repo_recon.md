# Repository Reconnaissance

## Purpose
`markdown-viewer/skills` is a curated skill-library repository that provides domain-specific `SKILL.md` instruction bundles for AI agents to generate diagrams/visualizations in Markdown.

## Main tech stack
- Primary artifacts: Markdown (`SKILL.md`, examples, references, templates)
- Diagram grammars targeted: PlantUML, Vega/Vega-Lite, JSON Canvas, HTML/CSS snippets
- Packaging/distribution: skill directory conventions consumed by external agent runtimes (e.g., Codex/Claude/Cursor)

## Preliminary core components
1. **Top-level catalog** (`README.md`): routing table from use-case -> skill folder.
2. **Skill spec units** (`*/SKILL.md`): frontmatter metadata + critical syntax rules + examples.
3. **Reference corpora** (`references/`, `stencils/`, `layouts/`, `styles/`): reusable domain grammars and style templates.
4. **Example suites** (`examples/`): concrete prompt-output patterns.
5. **External renderer boundary**: Markdown Viewer/agent host interprets generated fenced blocks and renders.
