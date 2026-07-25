# 实验计划

## 目标

验证 OpenSEO 在无 DataForSEO API key 的沙箱环境中，能否完成安装、构建、测试、静态数据流验证，并对核心 SEO 能力做可复现实证评估。

## 实验 1：Smoke Test

- 克隆目标仓库到 `/tmp/open-seo-target`。
- 运行 `pnpm install --frozen-lockfile`。
- 运行 `pnpm test`。
- 运行 `pnpm run build`。
- 尝试本地 D1 migration + dev server；若受 Node/Wrangler 或 Docker 环境限制，记录失败原因。

## 实验 2：核心 SEO 能力验证

在没有 `DATAFORSEO_API_KEY` 的条件下不调用真实 DataForSEO API，改用以下证据：

- 单元测试是否覆盖 DataForSEO envelope、MCP tools、keyword research、rank tracking、site audit capacity 等逻辑。
- 静态检查 DataForSEO client、keyword research service、audit service、MCP tool registry。
- 复制 `.env.example` 作为配置样本。

## 实验 3：成本收益情景

情景：

- 100 个 keyword tracking tasks，按 depth 50 queued SERP 估算；
- 1 次 site audit，按默认 `maxPages=50` 与 `auto` Lighthouse 策略描述资源用量，但不虚构未确认单价；
- 与用户给定 Semrush base `$129/mo` 比较，同时记录 2026-06-28 在线检索到的 Semrush Pro 月付约 `$139.95/mo`。

## 实验 4：商业产品基线

- Semrush/Ahrefs：功能基线包括 keyword research、rank tracking、site audit、backlinks、competitor research。
- OpenSEO 对比维度：部署控制权、成本透明度、MCP/Agent 集成、数据源依赖、工程成熟度。
