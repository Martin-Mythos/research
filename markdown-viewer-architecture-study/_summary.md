This research examines the technical design and internal architecture of the [`markdown-viewer/skills`](https://github.com/markdown-viewer/skills) repository, revealing it as a declarative, contract-driven library rather than an executable application. The core workflow transforms user requests into well-defined, renderer-compatible Markdown artifacts, relying on strict syntax contracts and structured metadata per skill module. Rendering is intentionally outside the repository, delegated to external Markdown Viewer instances or compatible hosts, as the repository contains no runtime, build system, or app manifests. The architecture is characterized by a contract-first pattern, with each skill constraining output formats for multiple renderer families.

**Key findings:**
- The analyzed commit contains 15 distinct skill modules and 252 tracked files.
- Output formats supported include PlantUML, Graphviz DOT, JSON Canvas, Vega/Vega-Lite, HTML/CSS, and template-based infographics.
- No executable application entrypoint or build tool is present; repository serves only as a skill contract and template provider.
- Architecture diagrams and inventory artifacts are generated for reproducibility and visualization ([Mermaid diagrams](https://mermaid-js.github.io/), JSON inventories).
