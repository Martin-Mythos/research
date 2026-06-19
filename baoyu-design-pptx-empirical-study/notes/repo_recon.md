# Repository Recon

Target: `https://github.com/JimLiu/baoyu-design`

Clone inspected at: `/tmp/baoyu-design-local`

## Project Shape

Baoyu-Design is distributed as an AI agent skill package rather than a conventional single-purpose web app or CLI. The repository contains:

- `skills/baoyu-design/SKILL.md`: skill entrypoint.
- `skills/baoyu-design/built-in-skills/`: user-facing workflows such as deck creation, design system authoring, image generation, and PPTX export.
- `skills/baoyu-design/starter-components/`: reusable components such as `deck-stage` and `image-slot`.
- `skills/baoyu-design/agents/`: local scripts and agents for design-system compilation/checking, Figma import, asset recording, and PPTX/video generation.

## PPTX Rendering Engine

Editable PPTX export is implemented in:

- `skills/baoyu-design/agents/gen-pptx/src/cli.ts`
- `skills/baoyu-design/agents/gen-pptx/src/browser/capture-editable.ts`
- `skills/baoyu-design/agents/gen-pptx/src/render/build-editable.ts`
- `skills/baoyu-design/agents/gen-pptx/src/render/render-node.ts`

Core dependencies:

- `playwright`: opens the served HTML deck and captures DOM/layout state.
- `pptxgenjs`: writes native PowerPoint objects.
- `esbuild`: bundles CLI and browser capture script.

The key architecture is:

```text
served HTML deck
  -> Playwright browser
  -> browser-side DOM capture
  -> captured slide tree
  -> media resolution/rasterization
  -> PptxGenJS native PPTX generation
```

## Image Insertion Integration Points

Image handling appears in:

- `starter-components/image-slot.js`: user-fillable image placeholder with persistent sidecar state.
- `built-in-skills/generate-images.md`: skill-level instructions for generating images.
- `gen-pptx/src/browser/capture-editable.ts`: captures `<img>`, `<canvas>`, `<svg>`, background image, gradient, and image-slot shadow DOM.
- `gen-pptx/src/render/media-cache.ts`: collects and resolves image/media references.
- `gen-pptx/src/render/render-node.ts`: maps captured media nodes into `slide.addImage()`.

The repository provides the insertion/rendering pipeline, but actual AI Image Generation depends on the host agent/runtime and model provider.

## Design System Integration Points

Relevant files:

- `built-in-skills/create-design-system.md`
- `built-in-skills/design-system-authoring-guide.md`
- `built-in-skills/use-design-system.md`
- `built-in-skills/design-system-preview.md`
- `agents/compile-design-system.mjs`
- `agents/check-design-system.mjs`
- `agents/import-design-system.mjs`
- `agents/lib/ds-core.mjs`
- `agents/lib/ds-prompt.mjs`

The repo clearly has a design-system workflow, including authoring, compile/check, import, preview, and prompt generation. This local experiment did not prove deterministic end-to-end natural language generation quality without an LLM runtime.

