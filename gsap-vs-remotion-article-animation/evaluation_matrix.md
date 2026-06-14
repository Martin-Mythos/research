# Evaluation Matrix (1–5)

| Dimension | GSAP | Remotion | HyperFrames | Notes |
|---|---:|---:|---:|---|
| Setup & Tooling | 5 | 3 | 3 | GSAP POC required only static files + CDN import. Remotion/HyperFrames typically require project scaffolding and renderer setup. |
| Timeline Mental Model | 5 | 4 | 4 | GSAP imperative timeline is very direct for text choreography. Remotion/HyperFrames provide frame-driven declarative control, powerful but mentally heavier at first. |
| Dynamic Content Handling | 4 | 4 | 4 | DOM-based GSAP handles runtime content naturally but needs careful measurement for complex flow. Remotion/HyperFrames can model dynamic layouts but often demand explicit composition logic. |
| Output Exportability | 2 | 5 | 5 | GSAP is web-animation-native; video export requires extra tooling. Remotion/HyperFrames are built for deterministic video outputs. |
| Engineering Quality | 4 | 4 | 4 | All can be maintainable with good conventions; GSAP can become imperative-heavy at scale, while React/HTML-composition frameworks can be cleaner for larger systems. |

## Scoring caveat
- GSAP score is grounded in direct POC build here.
- Remotion/HyperFrames scores are informed by official docs and architecture analysis, not full local execution in this run.
