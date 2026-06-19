# Setup Log

Date: 2026-06-19

## Environment

- OS: macOS 26.5.1, build 25F80
- Node.js: v26.0.0
- npm: 11.12.1
- npx: 11.12.1
- Python: 3.14.5
- LibreOffice/soffice: `/opt/homebrew/bin/soffice`
- Target repo clone: `/tmp/baoyu-design-local`
- Research folder: `baoyu-design-pptx-empirical-study/`

## Commands

```bash
git clone --depth 1 https://github.com/JimLiu/baoyu-design /tmp/baoyu-design-local
cd /tmp/baoyu-design-local/skills/baoyu-design/agents/gen-pptx
npm install
npm run build
npm test
npx playwright install chromium
```

## Setup Result

- `npm install`: success.
- `npm run build`: success; generated `dist/cli.mjs` and `dist/capture.iife.js`.
- `npm test`: success; 26 tests passed.
- `npx playwright install chromium`: success; installed Chromium for Testing 149.0.7827.55, Playwright Chromium v1228.
- npm reported 1 moderate severity vulnerability; no forced dependency upgrade was applied because that would change the tested dependency graph.

