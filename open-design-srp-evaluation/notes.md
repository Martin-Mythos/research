# 研究笔记

## 原始问题
研究 GitHub 开源项目 `nexu-io/open-design` 的架构机制与工程落地能力，并以 ENISA SRP Demo PRD 作为实验标的，完成三项实验（复杂表单 Token 建模、i18n 双语机制、RBAC 动态字段隐藏）。

## 数据源与命令记录
- `git clone --depth 1 https://github.com/nexu-io/open-design /tmp/open-design`
  - 结果：成功克隆，用于离线代码审阅。
- `cd /tmp/open-design && rg --files | head -n 80`
  - 结果：仓库包含 `apps/`, `packages/`, `skills/`, `design-systems/`, `prompt-templates/` 等目录。
- `cd /tmp/open-design && sed -n '1,220p' README.md`
  - 结果：确认项目定位为“面向 AI 设计代理的开源工作台”，并非传统企业表单前端框架。
- `cd /tmp/open-design && rg -n "i18n|locale|language|translations|react-intl|next-intl" apps packages`
  - 结果：未发现完整企业级 i18n 框架接入，更多是文案与模板驱动。
- `cd /tmp/open-design && rg -n "skills|artifact|proxy|daemon|iframe|sqlite|BYOK" apps packages docs | head -n 120`
  - 结果：确认核心链路为 web UI -> daemon -> coding agent CLI -> artifact 输出。
- `cd /tmp/open-design && sed -n '1,260p' apps/daemon/src/server.ts`
  - 结果：确认 daemon 提供 API，并承担本地执行/代理能力。
- `cd /tmp/open-design && sed -n '1,260p' apps/web/src/app/page.tsx`
  - 结果：确认前端主界面偏“任务驱动 + 生成式交互”，非业务表单中台。

## 实验与结果
1. 复杂业务实体 Token 建模（SRP Group B + SLA）
   - 方案：在本研究目录构造 `artifacts/tokens/srp-group-b.tokens.json` 与 `artifacts/schemas/sla-timeline.schema.json`，模拟可被 open-design skill 消费的配置资产。
   - 结果：可以表达颜色语义、状态映射、字段元数据；但 open-design 原生未提供“表单约束执行引擎”，需业务层补齐。

2. i18n 双语机制实验（默认 EN）
   - 方案：构造 `artifacts/i18n/en.json` 与 `artifacts/i18n/zh-CN.json`，并提供 `artifacts/i18n/i18n-binding.pseudo.ts` 绑定伪代码。
   - 结果：双语资源可定义，但 open-design 主定位是“生成 artifact”，非“应用运行时 i18n 中间件”；要满足 P01-P08 一致切换，需在宿主应用层实现。

3. RBAC 敏感字段隐藏实验（demo_observer）
   - 方案：提供 `artifacts/rbac/field-visibility.policy.json` 与 `artifacts/rbac/case-detail-render.pseudo.tsx`。
   - 结果：可在组件树实现按角色渲染；但若只前端隐藏仍有越权风险，必须后端裁剪数据。

## 失败路径与放弃原因
- 尝试将 open-design 当作“现成企业 UI 组件库”直接映射 A-F 表单：
  - 放弃原因：其核心是 agentic design workflow，不是 Ant Design/Material UI 这类“字段级验证+表单状态管理”框架。
- 尝试在仓库内找到现成 SRP 类 RBAC 表单示例：
  - 放弃原因：仓库示例聚焦 marketing/deck/prototype，缺少复杂合规表单现成模板。

## 可复现实证证据
- 关键验证命令：
  - `cd /tmp/open-design && rg -n "i18n|locale|language|translations|react-intl|next-intl" apps packages`
  - `cd /tmp/open-design && rg -n "skills|artifact|proxy|daemon|iframe|sqlite|BYOK" apps packages docs | head -n 120`
- 结论证据文件：
  - `/tmp/open-design/README.md`
  - `/tmp/open-design/apps/daemon/src/server.ts`
  - `/tmp/open-design/apps/web/src/app/page.tsx`
