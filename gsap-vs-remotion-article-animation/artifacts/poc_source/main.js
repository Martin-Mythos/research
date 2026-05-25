import { gsap } from 'https://cdn.jsdelivr.net/npm/gsap@3.15.0/index.js';

const tl = gsap.timeline({ defaults: { ease: 'power2.out' } });

tl
  .set('#intro', { autoAlpha: 1 })
  .from('#intro .title', { y: 40, autoAlpha: 0, duration: 0.9 })
  .from('#intro .body', { y: 24, autoAlpha: 0, duration: 0.7 }, '-=0.4')
  .to('#intro', { autoAlpha: 0, y: -30, duration: 0.8 }, '+=1.2')

  .set('#sec1', { autoAlpha: 1, y: 20 })
  .to('#sec1', { y: 0, duration: 0.4 })
  .from('#sec1 h2', { y: 30, autoAlpha: 0, duration: 0.7 }, '-=0.2')
  .from('#sec1 p', { y: 20, autoAlpha: 0, duration: 0.6 }, '-=0.3')
  .from('#sec1 li', { y: 12, autoAlpha: 0, stagger: 0.18, duration: 0.45 }, '-=0.25')
  .to('#sec1', { autoAlpha: 0, y: -30, duration: 0.8 }, '+=1.0')

  .set('#sec2', { autoAlpha: 1, y: 20 })
  .to('#sec2', { y: 0, duration: 0.4 })
  .from('#sec2 h2', { y: 30, autoAlpha: 0, duration: 0.7 }, '-=0.2')
  .from('#sec2 p', { y: 20, autoAlpha: 0, duration: 0.6 }, '-=0.3')
  .from('#sec2 li', { y: 12, autoAlpha: 0, stagger: 0.18, duration: 0.45 }, '-=0.25');

window.timeline = tl;
