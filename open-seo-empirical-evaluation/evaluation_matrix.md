# 评估矩阵

| 评估维度 | 描述说明 | 分数 (1-5) | 证据支撑 |
|---|---|---:|---|
| 部署便捷度 (Installability) | Docker 文档清晰，Node/pnpm 构建成功；但沙箱无 Docker，Wrangler 本地 D1 要求 Node 22+，实际 dev 未启动。 | 3 | `pnpm install`、`pnpm test`、`pnpm run build` 通过；`db:migrate:local` 因 Node 20.20.2 失败。 |
| 核心SEO能力 (Core SEO Features) | 代码层具备 keyword research、rank tracking、domain/competitor、backlinks、site audit、GSC 与 AI search 模块。无 key 条件下未验证真实 API 返回质量。 | 4 | README 宣称与 `src/server/features/*`、`src/server/lib/dataforseo/*`、MCP tools 均对应；测试 392 个通过。 |
| 商业成本优势 (Cost Efficiency) | 按需 API 成本对低频场景明显优于订阅；100 keywords weekly depth 50 约 $0.96-$1.20/月级别。站点审计成本需按 DataForSEO 实际任务单价确认。 | 4 | `scripts/cost_scenario.py` 输出 100 keywords 四周约 `$0.96`；README 示例约 `$1.20/month`；Semrush baseline `$129/mo`。 |
| AI工具链兼容 (Agent Integration) | MCP server 与 Agent Skills 是项目核心差异点，工具覆盖关键词、SERP、domain、backlink、rank tracking、GSC。 | 5 | `src/server/mcp/server.ts` 注册多项工具；`web/content/docs/mcp.md` 描述 Claude/Cursor/Codex 等接入。 |
| 工程规范度 (Engineering Quality) | TypeScript、Vitest、Drizzle、Cloudflare Workers 结构较完整；测试数量充足。风险是云平台耦合与本地运行门槛。 | 4 | 66 个测试文件 / 392 个测试通过；构建通过；存在生产 chunk size warning 与 Wrangler/Node 版本摩擦。 |

## 总评分判断

OpenSEO 在“开源、按需付费、Agent-ready SEO 工具”方向具有较高可行性。它更像是面向工程团队、独立站长和 AI workflow 的可控 SEO 数据工作台，而不是面向非技术营销人员的即开即用 Semrush/Ahrefs 完整替代。
