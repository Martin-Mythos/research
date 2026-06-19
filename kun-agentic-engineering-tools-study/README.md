# Kun Chen Agentic Engineering Tools 经验研究报告

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## 1. 执行摘要

本研究用 `Talking Breads Tervuren` V1 静态网站作为真实开发实验，评估 Lavish / Treehouse / No Mistakes 组成的 `Plan-Code-Validate` agentic engineering 工具链。结论：**这个工具链的工作流方向有价值，但目前更适合“分阶段试用”，不适合一次性全量纳入 Martin 的日常生产流。** Lavish 的 HTML planning artifact 对把模糊需求变成可审阅规格最有即时价值；Treehouse 的核心 `Git worktree` 池思想扎实，测试通过，但对单人轻量项目的收益取决于并行 agent 数量；No Mistakes 的愿景最完整，但真实价值绑定 GitHub auth、远程 PR、CI、LLM/agent CLI 与 TUI/gate 流程，本沙箱只能验证源码测试和本地替代验证，不能证明其 AI code review 质量。

## 2. 一页建议

| 工具 | 建议 | 理由 |
|---|---:|---|
| Lavish / lavish-axi | **Trial（试用）** | 本地 HTML artifact 模式直接贴合 Plan 阶段；可离线生成 artifact。本环境源码 smoke 因 Node 版本/pnpm 依赖失败，但 README 模式清晰。 |
| Treehouse | **Trial（试用）** | Go 测试通过，概念与 raw `git worktree` 对齐；适合多 agent 并行。单人低并发时 raw worktree 足够。 |
| No Mistakes | **Watch / Limited trial（观察，小范围试用）** | 源码测试通过，但完整 gate 需要远程、auth、AI agent/API 与 PR 权限；不应先用于高风险仓库。 |
| 组合工具链 | **Trial with guardrails（带护栏试用）** | 能减少 context switching 并产出可审计 artifact，但 Validate 阶段仍需普通 CI、手动 review checklist 和 secret 权限边界。 |

## 3. 方法与证据边界

### 已验证事实

- `gh` 在环境中不可用，因此 GitHub CLI auth/repo metadata 步骤失败，已记录为 blocker。
- 三个目标仓库均成功 `git clone --depth 1` 到 `/tmp/kun-tools-recon`，未提交克隆仓库。
- Treehouse `go test ./...` 通过。
- No Mistakes `go test ./...` 通过。
- Lavish 源码 smoke 因当前 Node v20 与 pnpm/`node:sqlite` 依赖不兼容失败。
- Talking Breads V1 静态站已创建并通过测试/smoke；首次 build 因 TypeScript 7 deprecation 设置失败，修正后重新验证。

### 经验观察

- Lavish 的 artifact 模式比纯 Markdown 更适合把 UI/产品意图变成可审阅对象，尤其是首屏、CTA、非目标功能等容易 drift 的点。
- Treehouse 主要节省“多 worktree 生命周期管理”和依赖缓存复用成本；raw `git worktree` 已能覆盖小规模并行分支。
- No Mistakes 的门禁价值来自集成链路，而不是单个本地命令；没有 auth/API/远程 PR 时只能做静态 fallback。

### 工程推断

- 对 Martin 的个人 AI builder workflow，先采用 Lavish-style plan artifact + raw worktree + 明确 validation checklist，收益/风险比最高。
- 当并行 agent 长期超过 3-5 个时，再引入 Treehouse 管理池。
- No Mistakes 应先在低风险测试仓库试跑，确认权限、日志、自动修复和 PR 创建行为后再扩大使用。

## 4. Tool-by-tool findings

### 4.1 Lavish / Lavish AXI

**定位**：本地 HTML planning/editor artifact 工具。README 描述它把 agent 生成的 HTML artifact 放进本地浏览器 UI，并支持 annotation / polling feedback loop。

**安装与 smoke**：

- 推荐路径包括 `npx skills add kunchenguid/lavish-axi --skill lavish`、直接 `npx -y lavish-axi`、源码 `pnpm install --frozen-lockfile && pnpm run build`。
- 本环境源码 smoke 失败：pnpm 需要更新 Node 能力，报 `ERR_UNKNOWN_BUILTIN_MODULE: node:sqlite`。这说明 Lavish 对 Node/pnpm 版本较敏感。
- 仍用 README 模式制作了 `Talking Breads V1 规划 Artifact`，把首屏、内容模型、信任要素和禁止 live ordering/payment 约束放入可审阅 HTML。

**能力判断**：Lavish 最适合 Plan 阶段。它不直接生成更正确的代码，但能把需求、设计方向、约束和验收点变成更容易被人审查的 artifact，从而降低后续实现 drift。

**主要限制**：需要浏览器/本地 server 才能体验完整 annotation loop；非 loopback 绑定有明确安全风险；本环境 Node 版本不满足当前 pnpm 依赖。

### 4.2 Treehouse

**定位**：Git worktree 池管理 CLI，用可复用隔离 worktree 支持多个 agents/sessions 并行。

**安装与 smoke**：

- README 支持 curl installer、Nix、Go install、源码 `make install`。
- `go test ./...` 通过。
- `make build` 通过。
- 本研究对 Talking Breads subject project 运行 raw `git worktree` 创建 `site-baseline` 与 `site-polish`，并记录 duplicate branch collision。

**能力判断**：Treehouse 的价值在“复用已安装依赖和 build cache 的 worktree 池”以及 in-use 检测。对于 20-30 agents 的访谈规模，方向合理；对单人 1-2 个分支，raw `git worktree` 成本更低。

**主要限制**：完整 interactive subshell 流程在非交互环境不适合长跑；user-level hooks 能执行 shell，需要审计；repo 无远程时 `git fetch origin` 类流程可能受限。

### 4.3 No Mistakes

**定位**：Git proxy/gate + validation pipeline。README 宣称通过 `git push no-mistakes` 启动 disposable worktree 中的 review/test/docs/lint/push/PR/CI 流程。

**安装与 smoke**：

- README 支持 curl installer、Go/source、agent skill。
- `go test ./...` 通过。
- 未执行真实 `no-mistakes init` 和 `git push no-mistakes`，因为环境没有 `gh`、没有 GitHub auth/PR 权限、没有明确 LLM/API key/TUI 交互边界。
- 用 `scripts/validate_talking_breads.py` 作为 fallback 检查 PRD 关键项和 forbidden affordance。

**能力判断**：No Mistakes 可能是 Validate 阶段最强的一环，但也是依赖最多、权限最大的一环。本研究不能验证其 AI review 能否抓住 intentional issue，只能验证源码测试通过和替代静态检查有效。

**主要限制**：完整价值依赖远程仓库、PR 创建权限、agent/LLM CLI、CI 和人工批准策略；自动修复可能改变意图，必须保留 human-in-the-loop。

## 5. 集成工作流评估

### Plan

使用 Lavish-style HTML artifact 将 PRD 转成 `artifacts/lavish-plan/talking-breads-plan.html`。它明确突出：首屏身份、CTA、内容模型、过敏原、营业时间可更新、禁止 live ordering/payment。

### Code

构建 `artifacts/talking-breads-v1/`：Vite + React + TypeScript 静态网站。内容集中在 `src/content.ts`，包含菜单、价格 sample、促销、过敏原、hours、contact 和未来域名说明。用 raw `git worktree` 模拟 `site-baseline` 与 `site-polish` 两条并行路径，因为 Treehouse 完整 interactive workflow 不适合当前非交互沙箱。

### Validate

执行：

- `npm run build`：首次失败，修复 TypeScript 配置后重新运行。
- `npm test`：Vitest content model 测试通过。
- `npm run smoke`：PRD 关键内容与 forbidden affordance 检查通过。
- `scripts/validate_talking_breads.py`：手动 validation fallback 通过。
- No Mistakes 真实 gate 未运行，原因见 blocker。

## 6. 基线比较

| 维度 | 工具链 | 手动基线 |
|---|---|---|
| Plan artifact | Lavish-style HTML 更视觉化、可交互潜力强 | Markdown PRD 清晰但不直观 |
| Code 并行 | Treehouse 目标是池化 worktree 与依赖缓存 | raw `git worktree` 命令少但要自己清理 |
| Validate | No Mistakes 可望把 review/test/PR/CI 串起来 | `npm run build/test/smoke` + checklist 更透明 |
| 设置摩擦 | 三工具叠加依赖较多 | 基线依赖少 |
| 错误可见性 | Treehouse/Go 测试清晰；Lavish Node 版本问题清晰；No Mistakes 完整链路未测 | 本地命令直接、可复现 |
| 安全/auth 风险 | No Mistakes 和 hooks 需要权限审计 | 最小权限 |
| 防需求漂移 | Lavish artifact + validation script 有帮助 | 依赖 reviewer 记忆和 checklist |

## 7. 安全与运维风险

- Lavish：不要绑定 `0.0.0.0`，否则未认证本地文件服务可能暴露给网络。
- Treehouse：审计 user-level hooks；并发 agent 使用时要确认工作目录和进程清理逻辑。
- No Mistakes：先限制到低风险 repo；明确哪些 secrets 可见、哪些自动修复可接受、PR 创建权限如何授予、失败日志保留在哪里。
- 通用：不要把外部仓库克隆、`node_modules`、构建缓存、API key 或原始私有数据提交到研究仓库。

## 8. Martin 实用采用计划

1. **先试 Lavish-style planning**：每个模糊 UI/产品需求都生成一个 HTML artifact，里面明确 non-goals 和 acceptance checks。
2. **短期用 raw `git worktree`，中期试 Treehouse**：当同一 repo 同时跑多个 agent/session 时再引入 Treehouse 池。
3. **No Mistakes 只在 sandbox repo 试点**：先验证 `init -> push gate -> review -> PR` 全流程，再决定是否纳入 Life-OS 或 coding-agent workflow。
4. **必须自动化的部分**：build、typecheck、unit/smoke、PRD forbidden affordance 检查、提交前文件清单检查。
5. **暂不信任的部分**：AI review 的充分性、自动修复对产品意图的保真度、远程权限与 secret 隔离。

## 9. 评分矩阵

| 工具 | 安装可复现 | 文档清晰 | 核心成熟度 | 本地/离线价值 | Agent 集成 | 失败透明 | 安全姿态 | Martin 实用价值 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Lavish | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 4 |
| Treehouse | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| No Mistakes | 3 | 4 | 3 | 2 | 5 | 3 | 2 | 3 |
| 组合链路 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 4 |

组合链路附加评分：减少 human context switching = 4；增加 review confidence = 3；让并行 agent 更安全 = 4；产出可审计 artifact = 4；Martin realistically adopt = 3.5。

## 10. 未完成/阻塞项

- Google Doc 未直接读取；使用 prompt 中的 PRD fallback。
- `gh` 不存在，无法运行 `gh auth status` 与 `gh repo view`。
- Lavish 完整 browser annotation/poll loop 未运行；源码 smoke 因 Node/pnpm 版本失败。
- Treehouse interactive `treehouse get` subshell 未完整进入/退出；使用 Go tests、build 和 raw worktree fallback。
- No Mistakes 真实 `git push no-mistakes` gate、AI review、PR 创建、CI auto-fix 未运行；缺 GitHub auth/远程权限/LLM 或 agent CLI 配置。
- 未使用 browser tooling 保存真实 screenshot；保存了可直接打开的 HTML planning artifact。

## 11. 复现说明

```sh
cd kun-agentic-engineering-tools-study/artifacts/talking-breads-v1
npm install
npm run build
npm test
npm run smoke
cd ../..
python3 scripts/validate_talking_breads.py
```

外部工具源码测试复现需重新 clone 到临时目录，并 checkout 本研究记录的具体 commit 后运行对应命令。这样可以避免上游 `main` 在复现时已经移动，导致测试结果与本报告的 evidence 不一致。对应 commit 也保存在 `artifacts/*-topfiles.log`。

```sh
git clone --depth 1 https://github.com/kunchenguid/treehouse /tmp/treehouse
(cd /tmp/treehouse && git fetch --depth 1 origin 7f8e436b972af8e1de57b7859c3eade45713a2bd && git checkout 7f8e436b972af8e1de57b7859c3eade45713a2bd && go test ./...)
git clone --depth 1 https://github.com/kunchenguid/no-mistakes /tmp/no-mistakes
(cd /tmp/no-mistakes && git fetch --depth 1 origin f9c5b7f1e8bc5ad18d74667f00e9b7354d365304 && git checkout f9c5b7f1e8bc5ad18d74667f00e9b7354d365304 && go test ./...)
```

## 12. 证据附录

- 仓库侦察：`artifacts/repo-recon.md`
- 环境：`artifacts/environment.log`
- 克隆/顶层文件：`artifacts/*-clone.log`, `artifacts/*-topfiles.log`
- 工具 smoke：`artifacts/lavish-axi-smoke.log`, `artifacts/treehouse-smoke.log`, `artifacts/no-mistakes-smoke.log`
- Treehouse/raw worktree：`artifacts/raw-git-worktree-experiment.log`
- Lavish planning artifact：`artifacts/lavish-plan/talking-breads-plan.html`
- Subject project：`artifacts/talking-breads-v1/`
- Talking Breads verification：`artifacts/talking-breads-*.log`, `artifacts/manual-validation.log`
- No Mistakes fallback：`artifacts/no-mistakes-review-fallback.md`
- 安全笔记：`security_notes.md`
