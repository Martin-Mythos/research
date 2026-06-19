# Experiment Plan

## Research Question

Baoyu-Design 是否能稳定生成结构完整的 Design System，并导出包含 AI 生成图且高度可编辑的 PPTX 文件？

## Experiment 1: Smoke Test & Design System Generation

- Input: `Corporate Tech Branding - Ocean Blue & Minimalist`.
- Mechanism: inspect Baoyu's design-system skill prompts and scripts; build a deck that materializes palette, typography, spacing, and component tokens.
- Evidence:
  - `skills/baoyu-design/built-in-skills/create-design-system.md`
  - `skills/baoyu-design/agents/compile-design-system.mjs`
  - `skills/baoyu-design/agents/check-design-system.mjs`
  - slide 1 and slide 2 of the local empirical deck.
- Limit: this experiment validates the shipped workflow and generated deck representation, not a fully autonomous LLM run that writes a fresh production design system from natural language.

## Experiment 2: PPTX Generation & Editability Test

- Input: 3-slide local HTML deck with title, token grid, cards, metrics, bullets, gradient, and notes.
- Mechanism: run Baoyu's real `gen-pptx` CLI in editable mode.
- Evidence:
  - `artifacts/baoyu-design-imagegen-editable.pptx`
  - `artifacts/imagegen_pptx_ooxml_inspection.json`
  - `screenshots/baoyu-design-imagegen-editable.pdf`
- Success criteria:
  - CLI succeeds with no fatal errors.
  - OOXML contains native text bodies and shapes, not only slide-sized screenshots.
  - LibreOffice can parse and export the PPTX to PDF.

## Experiment 3: AI Image Generation & PPTX Injection Workflow

- Input: locally generated image for the prompt "A futuristic server room icon".
- Mechanism: use the built-in image generation result copied to `artifacts/local_deck/imagegen-server-room.png`, embedded in the deck as an `<img>`.
- Evidence:
  - slide 3 contains one native picture object (`p:pic=1`).
  - surrounding labels and bullets remain native text.
  - the exporter reports no `images_failed` warning.
- Limit: the target project's own Image Generation API integration was not called. This isolates the insertion/layout pipeline from target-project API authentication and cost.
