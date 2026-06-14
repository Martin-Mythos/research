# Experiment Plan

## Objective
Empirically test whether GSAP can quickly animate a 3-section markdown-style article, then compare the process against Remotion and HyperFrames as baselines.

## POC Design
1. Build a minimal static web composition (`index.html`, `styles.css`, `main.js`).
2. Represent article in 3 blocks: intro, section 1, section 2.
3. Use a single `gsap.timeline()` as orchestration backbone.
4. Sequence section entry/exit with overlap using position parameters.
5. Stagger list-item reveals to test micro-timing control.

## Verification Steps
- Serve the composition locally (`python3 -m http.server`).
- Confirm timeline script parses and runs in browser.
- Attempt frame-stage screenshot capture with Playwright at fixed timeline times.

## Comparison Matrix Plan
For GSAP, Remotion, HyperFrames score 1–5 on:
- Setup & Tooling
- Timeline Mental Model
- Dynamic Content Handling
- Output Exportability
- Engineering Quality

## Fairness Constraints
- GSAP evaluation is based on direct execution in this environment.
- Remotion/HyperFrames scoring is based on docs + architectural analysis (not fully executed here).
- Distinguish verified evidence vs inference in final report.
