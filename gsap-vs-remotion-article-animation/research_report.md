# Empirical Study on Programmatic Article Animation: GSAP vs. Remotion and Hyperframe

## 1. Executive Summary
This study built a real GSAP proof-of-concept (POC) that animates a short 3-section article in the browser using `gsap.timeline()`. The GSAP implementation was completed and locally servable. Screenshot automation was attempted but blocked by Playwright browser-download network restrictions (403). Comparative analysis against Remotion and HyperFrames was performed using official documentation and architecture review.

## 2. Project Overview
Target repo: `greensock/gsap-skills` (agent skill repository for correct GSAP usage patterns and examples).
Research artifact: A vanilla HTML/CSS/JS animation sequence for article sections (intro, section 1, section 2).

## 3. Research Questions
How does developer experience, timeline control, and output artifact differ when animating article content with GSAP versus Remotion/HyperFrames?

## 4. Experiment Design
- Generate article markdown content.
- Build static GSAP composition.
- Sequence entrances/exits via one timeline.
- Attempt evidence capture with headless automation.
- Score GSAP vs Remotion vs HyperFrames using a 1–5 rubric.

## 5. Setup & Execution Evidence
Environment recorded in `setup_log.md`.
Core timeline excerpt:

```js
const tl = gsap.timeline({ defaults: { ease: 'power2.out' } });
tl
  .set('#intro', { autoAlpha: 1 })
  .from('#intro .title', { y: 40, autoAlpha: 0, duration: 0.9 })
  .to('#intro', { autoAlpha: 0, y: -30, duration: 0.8 }, '+=1.2')
  .set('#sec1', { autoAlpha: 1, y: 20 })
  .from('#sec1 li', { y: 12, autoAlpha: 0, stagger: 0.18, duration: 0.45 }, '-=0.25');
```

## 6. Findings (Verified, Failed, Surprising)
### Verified
- `gsap-skills` contains concrete examples and best practices for timelines/transforms/ScrollTrigger.
- GSAP POC was implemented with sequential section choreography and staggered text reveals.
- Local static serving works.

### Failed / Could Not Be Verified
- Automated screenshots could not be produced due to browser binary download restrictions in sandbox (Playwright install chromium returned HTTP 403 from CDN).

### Surprising
- GSAP setup cost is extremely low for browser-based article storytelling (single static page + CDN import).

## 7. Evaluation Matrix
See `evaluation_matrix.md`.

## 8. Comparison With Baseline
- **GSAP**: Imperative, direct timeline authoring over DOM nodes. Best for live web surfaces and interactive storytelling.
- **Remotion**: React-first composition and explicit frame model; excellent for deterministic video export pipelines.
- **HyperFrames**: HTML-to-video architecture emphasizing deterministic frame rendering and agent-friendly pipeline control.

## 9. Practical Use Cases
- Use GSAP when your output target is web/app UI with runtime interactivity.
- Use Remotion/HyperFrames when output target is repeatable video artifacts (MP4) for publishing pipelines.

## 10. Limitations & Risks
- No successful headless screenshot/video evidence due to sandbox network limits on browser binary retrieval.
- Remotion/HyperFrames were not fully executed in this run.

## 11. Recommendations
- For AI-agent generated article animations intended for websites: start with GSAP.
- For batch social/video generation: prefer Remotion or HyperFrames.
- Hybrid pattern: prototype timing in GSAP, production render in video-native framework.

## 12. Reproduction Guide
1. Open `artifacts/poc_source/`.
2. Run `python3 -m http.server 4173 --directory artifacts/poc_source` from project parent.
3. Open `http://127.0.0.1:4173`.
4. (Optional) run `node artifacts/poc_source/capture.js` after installing Playwright + browser binaries.

## 13. Artifacts List
- `notes/article_content.md`
- `notes/repo_recon.md`
- `experiment_plan.md`
- `evaluation_matrix.md`
- `artifacts/poc_source/index.html`
- `artifacts/poc_source/styles.css`
- `artifacts/poc_source/main.js`
- `artifacts/poc_source/capture.js`
- `setup_log.md`
- `run_log.md`
- `progress.md`
- `notes.md`
