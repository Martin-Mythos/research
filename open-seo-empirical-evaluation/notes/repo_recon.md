# 仓库侦察笔记

## 项目核心定位

OpenSEO 自称是 Semrush 与 Ahrefs 的开源替代品，主张“自己托管应用 + 自带 DataForSEO API key + 按真实 API 用量付费”。README 明确写出其目标是面向用户与 AI Agent 的 all-in-one SEO 工具。

本次侦察基于目标仓库 `every-app/open-seo` 的浅克隆，提交：`e9955b46cb9311c02f905337ec580995eaba65de`。

## 宣称的 SEO 功能

README 与文档中宣称的主工作流包括：

- Keyword research（关键词研究）；
- Rank tracking（排名跟踪）；
- Competitor Insights（竞争对手洞察）；
- Backlinks（反链）；
- Site Audits（站点审计）；
- AI Visibility（AI 可见性）。

代码层面可见的功能模块包括：`src/server/features/keywords`、`rank-tracking`、`domain`、`backlinks`、`audit`、`ai-search`、`gsc`，说明这些不是纯营销文案，而是已有路由、服务和测试覆盖。

## 计费与数据获取原理

OpenSEO 的核心数据供应商是 DataForSEO。`src/server/lib/dataforseo/core.ts` 将 `DATAFORSEO_API_KEY` 作为 Basic Authorization header 注入所有 DataForSEO SDK 请求。自托管模式下 OpenSEO 本身不收费；API 费用由 DataForSEO 按请求/任务计费。

重要观察：

- `DATAFORSEO_API_KEY` 缺失时，代码通过 `getRequiredEnvValue("DATAFORSEO_API_KEY")` 懒加载读取；只有实际触发 DataForSEO 请求时才会失败，静态构建和多数单元测试不需要 key。
- hosted 模式下 `createDataforseoClient` 会把 DataForSEO 调用包裹进 Autumn/usage credits 计量；非 hosted 模式直接执行 DataForSEO 调用。
- 排名跟踪成本估算常量位于 `src/shared/rank-tracking.ts`：queued depth 50 每个关键词检查约 `0.0024 USD`，README 示例给出 100 个关键词每周 depth 50 约 `$1.20/month`。本研究用代码常量推导的 4 周近似为 `$0.96/month`，差异可能来自月均 4.33 周、进位或产品加价假设。

## AI/MCP 扩展能力

OpenSEO 提供 MCP server。文档 `web/content/docs/mcp.md` 描述 hosted endpoint 为 `https://app.openseo.so/mcp`，并说明 AI client 可调用关键词研究、SERP、domain research、backlink overview、saved keywords、rank tracking、Google Search Console 等工具。

代码层面 `src/server/mcp/server.ts` 明确注册多个 MCP tool，包括：

- `research_keywords`
- `get_serp_results`
- `get_domain_overview`
- `get_domain_keyword_suggestions`
- `get_backlinks_overview`
- `get_rank_tracker`
- `get_ranked_keywords`
- GSC performance / URL inspection tools

此外，`web/content/docs/skills/*` 和 README 中列出了 agent skills：`seo-project-setup`、`seo-coach`、`keyword-research`、`keyword-clustering`、`competitive-landscape`、`competitor-analysis`、`link-prospecting`。

## 部署栈与依赖要求

- 语言/框架：TypeScript、React 19、TanStack Start/Router、Vite。
- 后端运行时：Cloudflare Workers / Vite Cloudflare runtime。
- 数据库：Cloudflare D1 / Drizzle migrations。
- MCP：`@modelcontextprotocol/sdk` 与 `agents/mcp`。
- SEO API：`dataforseo-client`。
- 本地开发：Node.js 20+、pnpm；但实际 `wrangler d1 migrations apply` 在当前依赖版本下要求 Node.js 22+。
- Docker 自托管：`compose.yaml` 使用 `ghcr.io/every-app/open-seo:latest`，默认 `AUTH_MODE=local_noauth`，本地端口默认 3001。

## 侦察结论

OpenSEO 的功能面覆盖了传统 SEO 工具的核心集合，但其“商业平替性”依赖两个条件：

1. 用户接受 DataForSEO 作为底层数据源，而不是 Semrush/Ahrefs 自有索引；
2. 用户愿意用更工程化的部署/API-key 工作流换取成本透明、数据控制权与 Agent 集成能力。
