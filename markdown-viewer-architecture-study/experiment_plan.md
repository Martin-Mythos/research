# Experiment Plan

## Research objective

Reverse-engineer the architecture of `markdown-viewer/skills` by tracing actual repository artifacts rather than relying only on README prose.

## Core trace scenario

Input request: "Create a UML sequence diagram for an API authentication flow."

Expected lifecycle:

1. Agent receives natural-language visualization request.
2. Agent consults repository/catalog guidance and selects `uml`.
3. Agent reads `uml/SKILL.md` for PlantUML-specific syntax rules.
4. Agent optionally consults `uml/examples/sequence-diagram.md` and stencil references.
5. Agent emits a Markdown fenced `plantuml` block.
6. External Markdown Viewer host renders the diagram.

## Additional polymorphism checks

To avoid overfitting to PlantUML, inspect representative non-PlantUML skills:

- `canvas/SKILL.md` for JSON Canvas output.
- `vega/SKILL.md` for Vega/Vega-Lite JSON output.
- `architecture/SKILL.md` and `infocard/SKILL.md` for direct HTML/CSS embedding.
- `graphviz/SKILL.md` for DOT output.

## Empirical method

1. Clone the target repository into `/tmp` without committing it.
2. Record target commit and tracked-file count.
3. Enumerate direct `SKILL.md` modules.
4. Search for executable app/build manifests.
5. Run `scripts/analyze_skills_repo.py` to classify skills and generate inventory artifacts.
6. Validate generated JSON and Markdown research artifacts.

## Success criteria

- All required research files exist.
- Report separates verified findings from interpretation/speculation.
- Architecture diagrams include at least one high-level system diagram and one sequence/data-flow diagram.
- Claims about skill count and runtime characteristics are backed by reproducible commands or generated artifacts.
