# Working Notes

## Original prompt / research question
- Investigate `greensock/gsap-skills` empirically and build a POC animating an article.
- Compare GSAP workflow to Remotion and HyperFrames for developer experience, timeline control, and output artifacts.

## Commands, scripts, data sources, URLs used
- `git clone --depth 1 https://github.com/greensock/gsap-skills.git tmp-gsap-skills`
- `node -v`, `npm -v`, `python3 --version`, `uname -a`
- `npx playwright --version`
- `python3 -m http.server 4173 --directory gsap-vs-remotion-article-animation/artifacts/poc_source`
- `node gsap-vs-remotion-article-animation/artifacts/poc_source/capture.js`
- URLs:
  - https://github.com/greensock/gsap-skills
  - https://openai.com/index/work-with-codex-from-anywhere/
  - https://openai.com/index/codex-for-almost-everything/
  - https://openai.com/index/introducing-codex/
  - https://cloudrun.remotion.dev/
  - https://hyperframes.video/docs/getting-started/introduction

## Experiments attempted and outcomes
- Built vanilla HTML/CSS/JS GSAP timeline article animator: success.
- Ran local HTTP server and used Playwright screenshot capture at 3 timestamps: success.
- Direct video export with GSAP-only stack: not attempted; GSAP is DOM animation library, not native renderer.

## Failed paths / abandoned
- `npx puppeteer --version` did not provide a usable quick version output in this environment; switched to Playwright for browser automation.

## Verification evidence
- Captured screenshots:
  - `screenshots/stage-1-title.png`
  - `screenshots/stage-2-section1.png`
  - `screenshots/stage-3-section2.png`
- Confirmed source and docs content from cloned repo and official docs pages.
