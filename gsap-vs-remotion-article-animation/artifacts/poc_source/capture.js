const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto('http://127.0.0.1:4173', { waitUntil: 'networkidle' });

  const shots = [
    ['stage-1-title.png', 700],
    ['stage-2-section1.png', 4200],
    ['stage-3-section2.png', 7600],
  ];

  for (const [name, t] of shots) {
    await page.evaluate((ms) => window.timeline.seek(ms / 1000), t);
    await page.screenshot({ path: `../../screenshots/${name}` });
  }

  await browser.close();
})();
