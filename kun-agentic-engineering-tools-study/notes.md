# notes.md — Kun Chen Agentic Engineering Tools Study

## 原始研究问题

调查 Kun Chen 在 Peter Yang 访谈中提到的三个开源 agentic engineering 工具：Lavish / Lavish AXI、Treehouse、No Mistakes。核心问题：Lavish + Treehouse + No Mistakes 是否能实质改善个人 AI builder 的 `Plan -> Code -> Validate` 工作流？各工具在安装、可用性、安全性、可靠性和集成方面有哪些实践边界？

目标仓库：Martin-Mythos/research。目标工具仓库：
- https://github.com/kunchenguid/lavish-axi
- https://github.com/kunchenguid/treehouse
- https://github.com/kunchenguid/no-mistakes

实验项目：基于 Talking Breads Minimal PRD 构建 V1 静态网站。

## 工作日志

### 2026-06-14 初始化
- 使用 open-research 技能。
- 读取 `/workspace/research/AGENTS.md`。
- 创建研究目录 `kun-agentic-engineering-tools-study/`。

### 仓库侦察与 smoke
- 运行环境记录：`artifacts/environment.log`。
- `gh` 不存在，`gh auth status` 与 `gh repo view` 均失败；记录在各 `*-gh.log`。
- 三个仓库均用 `git clone --depth 1` 克隆到 `/tmp/kun-tools-recon/*`，未放入研究目录。
- 读取 README、package/Makefile、顶层文件，整理到 `artifacts/repo-recon.md`。
- 尝试运行 Lavish pnpm test、Treehouse go test、No Mistakes go test；原始输出保存为 `artifacts/*-smoke.log`。

### Talking Breads V1
- 在 `artifacts/talking-breads-v1/` 创建 Vite + React + TypeScript 静态站。
- 运行 `npm install`, `npm run build`, `npm test`, `npm run smoke`，输出保存到 `artifacts/talking-breads-*.log`。
- 删除 `node_modules` 与 `dist`，避免提交依赖和构建目录。

### Lavish planning artifact
- 根据 Lavish README 的 HTML artifact 模式创建 `artifacts/lavish-plan/talking-breads-plan.html`。
- 第三次 Talking Breads 验证加入 `@types/react` / `@types/react-dom` 后，`npm test` 与 `npm run smoke` 通过，但 build 仍因 CSS side-effect import declaration 缺失失败。
- 第四次 Talking Breads 验证加入 `src/vite-env.d.ts` CSS module declaration 后，`npm run build`、`npm test`、`npm run smoke` 均通过；删除 `node_modules` 与 `dist`。
