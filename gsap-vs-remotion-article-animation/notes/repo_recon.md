# greensock/gsap-skills Recon

## What the project is
`greensock/gsap-skills` is an instruction/skills repository for coding agents (Codex, Cursor, Claude, Copilot) focused on correct GSAP usage patterns rather than a full application framework.

## Verified setup process
- Install skill package via `npx skills add https://github.com/greensock/gsap-skills`.
- For runnable examples:
  - Vanilla: serve `examples/vanilla` with a local ES module-capable server.
  - React/Vue/Nuxt examples provide standard framework setup commands.

## Core timeline mechanics observed
- The examples and README consistently emphasize:
  - `gsap.timeline()` for sequencing rather than delay-heavy standalone tweens.
  - defaults object for shared easing/duration.
  - position parameter (`"+=0.2"`, `"-=0.1"`) for overlap and rhythm.

## Text animation plugin context
- README states formerly paid plugins (including SplitText) are now available from public `gsap` package.
- In examples, text motion can be done without SplitText using standard transforms (`x`, `y`) and `autoAlpha`, which we used for portability.

## Staging / best practices observed
- Prefer transform properties (`x`, `y`) over layout-thrashing properties.
- Use `autoAlpha` for visibility + opacity transitions.
- Register plugins once (`gsap.registerPlugin(...)`).
- For scroll-linked sequences, place `ScrollTrigger` on timeline container; call `ScrollTrigger.refresh()` after layout changes.

## Files inspected
- `README.md`
- `examples/README.md`
- `examples/vanilla/main.js`
