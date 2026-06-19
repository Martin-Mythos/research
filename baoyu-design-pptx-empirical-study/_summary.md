This empirical study evaluates `JimLiu/baoyu-design` as an AI-assisted design and document generation workflow, focusing on design-system structure, editable PowerPoint export, and generated-image insertion. The core `gen-pptx` chain was reproduced locally with Playwright and PptxGenJS: a three-slide HTML deck was captured and exported to an editable `.pptx` containing native text bodies, shapes, picture objects, and speaker notes. A locally generated cybersecurity server-room PNG was inserted into the deck and preserved as a native PowerPoint picture object rather than flattening the whole slide to screenshots.

Key findings:
- The editable PPTX path is technically credible and locally reproduced with no exporter warnings.
- OOXML inspection confirms native PowerPoint objects (`p:txBody`, `p:sp`, `p:pic`) across the generated deck.
- Baoyu's own Image Generation API integration was not exercised; the study isolates the insertion/layout pipeline using a local generated image artifact.
