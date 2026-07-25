# 工作笔记

## 原始研究问题

标题：OpenSEO 核心能力实证验证与商业平替性分析

核心问题：OpenSEO 在真实部署中能提供哪些切实可行的 SEO 优化能力，其按需付费与私有部署模式相较于收费商业产品（如 Semrush/Ahrefs）具备哪些核心优势？

## 工作约束

- 所有生成文件、笔记、日志、评估矩阵和最终报告使用简体中文。
- 若没有 `DATAFORSEO_API_KEY`，必须使用 mock/dry-run 或静态数据流分析，不绕过认证。
- 最终提交仅包含研究目录及必要小型产物。

## 命令记录

- `cat /workspace/research/.agents/skills/open-research/SKILL.md`：读取 open-research 技能说明。
- `find . -maxdepth 2 -type d | sort | sed 's#^./##' | head -100`：确认目标研究目录不存在。
- `cat AGENTS.md`：确认研究仓库写作与提交约束。
- `git status --short`：确认工作区初始无未提交变更。
- `mkdir -p open-seo-empirical-evaluation/notes open-seo-empirical-evaluation/artifacts open-seo-empirical-evaluation/scripts`：创建研究目录结构。

## 数据源与 URL

- 目标仓库：https://github.com/every-app/open-seo
- 研究仓库本地路径：`/workspace/research`

## 实验与结果

- 待记录。

## 失败路径

- 待记录。

## 验证证据

- 待记录。

- `date -u; uname -a; cat /etc/os-release; node --version; npm --version; pnpm --version; yarn --version; bun --version; docker --version; docker compose version; git --version`：记录环境信息。

- `git clone --depth 1 https://github.com/every-app/open-seo /tmp/open-seo-target`：克隆目标仓库，提交 `e9955b46cb9311c02f905337ec580995eaba65de`。
- `rg -n "DATAFORSEO|dataforseo|keyword|audit|MCP|mcp|Semrush|Ahrefs|price|pricing|docker|compose|site audit|rank" ...`：定位核心文档与代码路径。
- `sed -n ... README.md docs/SELF_HOSTING_DOCKER.md docs/LOCAL_DEVELOPMENT.md package.json`：审查 README、Docker、自托管、本地开发和依赖脚本。
- `pnpm install --frozen-lockfile`：安装依赖，成功，日志保存到 `artifacts/pnpm-install.log`。
- `pnpm test`：运行测试，66 个测试文件、392 个测试通过，日志保存到 `artifacts/pnpm-test.log`。
- `pnpm run build`：生产构建成功，有 chunk size warning，日志保存到 `artifacts/pnpm-build.log`。
- `pnpm run db:migrate:local && DATAFORSEO_API_KEY= AUTH_MODE=local_noauth pnpm dev --host 127.0.0.1 --port 4177`：尝试本地运行，因 Wrangler 要求 Node.js >=22 而失败，日志保存到 `artifacts/local-dev-no-key.log`。
- `python3 open-seo-empirical-evaluation/scripts/cost_scenario.py`：计算 100 keywords weekly rank tracking 成本，输出保存到 `artifacts/cost_scenario_output.txt`。

## 实验与结果

- 安装：成功。
- 单元测试：成功，392/392 通过。
- 构建：成功，但报告了大 chunk warning。
- Docker：未执行，原因是沙箱没有 Docker。
- 本地 dev：未启动，原因是 Wrangler 要求 Node.js 22+，当前为 Node.js 20.20.2。
- DataForSEO 真实调用：未执行，原因是未提供 `DATAFORSEO_API_KEY`。

## 验证证据

- `artifacts/pnpm-test.log` 末尾显示 `Test Files 66 passed (66)` 与 `Tests 392 passed (392)`。
- `artifacts/pnpm-build.log` 末尾显示 `EXIT:0`。
- `artifacts/local-dev-no-key.log` 显示 `Wrangler requires at least Node.js v22.0.0. You are using v20.20.2.`。

## 2026-07-25 GitHub Review 修复

### 原始修复请求

- 检查 GitHub review comments 并修复 PR #22 中的问题。

### Review 数据源与 URL

- GitHub Pull Request API：`https://api.github.com/repos/Martin-Mythos/research/pulls/22/comments`
- PR #22：https://github.com/Martin-Mythos/research/pull/22
- Inline comment `3488153047`：复现命令没有固定被评估的 OpenSEO revision。
- Inline comment `3488153049`：复现指南进入 `/tmp/open-seo-target` 后，成本脚本的相对路径失效。

### 实际使用的命令

- `curl ... https://api.github.com/repos/Martin-Mythos/research/pulls?state=all&per_page=100`：定位 OpenSEO PR #22。
- `curl ... https://api.github.com/repos/Martin-Mythos/research/pulls/22/comments`：读取两条 inline review comments。
- `jq -r ... /tmp/pulls-22-comments.json`：提取 comment 路径、正文和 URL。

### 修复结果

- 在 `README.md` 与 `research_report.md` 中增加固定 revision `e9955b46cb9311c02f905337ec580995eaba65de` 的 fetch、detached checkout 和 SHA 断言。
- 在切换目录前保存 `RESEARCH_REPO="$(pwd)"`，成本脚本改用研究仓库的绝对路径，避免在 OpenSEO clone 中查找不存在的文件。

### 验证证据

- 在新的临时目录 `/tmp/open-seo-review-repro.NSJWvn` 中逐条执行修订后的 clone/fetch/checkout 命令，最终输出 `VERIFIED_REVISION=e9955b46cb9311c02f905337ec580995eaba65de`。
- 在该临时 OpenSEO clone 目录内执行绝对路径形式的成本脚本，成功输出 `rank_tracking_100_keywords_weekly_approx_month_usd=0.96`，证明工作目录切换后路径仍有效。
