# 基于 ENISA SRP 复杂场景的 open-design 架构实证研究报告

## 1. 实验摘要 (Executive Summary)
`open-design` 的核心定位是“基于本地 coding agent CLI 的生成式设计工作台”，强调从 prompt/skill 出发快速生成可预览 artifact，而不是传统企业级前端中台或表单引擎。将其用于 ENISA SRP Demo（高合规、强字段约束、RBAC 细粒度控制）时，结论是：

- **可胜任**：设计探索、页面骨架原型、视觉 Token 草模、演示型页面快速生成。
- **不能单独胜任**：复杂字段验证、状态机一致性、后端 RBAC 强约束、审计可追溯等“系统级能力”。

**总体评价**：适合作为 SRP 项目“设计加速层（Design Accelerator）”，不适合作为“业务主框架（Application Core）”。

---

## 2. 架构解析 (Architecture Evaluation)

### 2.1 Design-to-Code 链路
基于仓库代码和文档，open-design 主链路可抽象为：

1. Web 界面收集需求（skill + design system + prompt）。
2. 本地 daemon 调度 CLI agent（Codex/Claude Code 等）。
3. agent 在工作目录产出 artifact（HTML/文档/模板等）。
4. 前端以 iframe/sandbox 进行即时预览。

这是一条“**Agentic 内容生产链**”，并非“业务组件渲染链”。

### 2.2 核心技术栈（观测）
- 前端：Next.js/React（交互工作台）。
- 后端/中枢：daemon + API（本地执行、代理、技能装配）。
- 资产层：skills、design-systems、prompt-templates（高度模板化）。
- 持久化：SQLite（会话与项目状态）。

### 2.3 与 SRP 目标的匹配度
- 与 P03 六组复杂表单：仅能提供“UI 草图与结构定义”层帮助。
- 与 P01-P08 EN/CN 切换：可通过外置 i18n 资源实现，但需宿主应用承担运行时切换。
- 与 P04 `demo_observer` 隐藏：可在渲染层实现，但必须加后端字段裁剪才合规。

---

## 3. 实验执行记录与 Artifacts (Experiment Logs & Artifacts)

> 说明：由于 open-design 并非现成 SRP 业务框架，实验采用“可执行配置 + 伪代码推演 + mock 数据约束”的方式闭环。

### 实验一：复杂业务实体的 Token 建模
**目标**：验证对 Group B（漏洞核心）与 SLA 语义的抽象能力。  
**Artifact 1**：`artifacts/tokens/srp-group-b.tokens.json`（颜色语义 + 字段约束元数据）  
**Artifact 2**：`artifacts/schemas/sla-timeline.schema.json`（T0 派生 24h/72h/final 的 schema 约束）

关键观察：
- Token 能表达严重度颜色、事件类型状态色。
- Schema 能表达条件必填（actively_exploited 时要求 corrective_measure_available_datetime）。
- 但“自动计算截止时间 + 提交前阻断”仍需业务代码执行，不是 token 原生能力。

### 实验二：i18n 双语机制解析
**目标**：验证 EN/CN 双语（默认 EN）如何落地。  
**Artifact**：
- `artifacts/i18n/en.json`
- `artifacts/i18n/zh-CN.json`
- `artifacts/i18n/i18n-binding.pseudo.ts`

关键观察：
- 双语资源字典可独立维护。
- 默认 EN 可在壳层配置（`userPreference ?? 'en'`）。
- open-design 本体更偏“生成内容”，并未直接提供企业级 i18n 运行时治理（如命名空间拆分、lazy loading、缺失键监控）。

### 实验三：RBAC 驱动的 UI 响应
**目标**：验证 `demo_observer` 角色敏感字段隐藏。  
**Artifact**：
- `artifacts/rbac/field-visibility.policy.json`
- `artifacts/rbac/case-detail-render.pseudo.tsx`

关键观察：
- 组件树可按角色隐藏 `exploitation_evidence` 等字段。
- 仅前端隐藏不安全，必须在 API 层对 `denyFields` 做服务端裁剪并禁用附件原文下载。

---

## 4. 局限性分析 (Limitations)

1. **业务表单能力缺口**：缺少开箱即用的复杂表单引擎（跨 Tab 校验、条件联动、审计级差异追踪）。
2. **RBAC 合规闭环不足**：open-design 关注“生成与预览”，不提供后端强制授权体系。
3. **状态机与 SLA 计算非内建**：SRP 的 24h/72h/final 时钟、Overdue 自动流转需另建服务。
4. **测试与可观测性不足**：仓库示例偏展示型，缺少针对企业 CRUD/审计场景的基准测试样例。

---

## 5. 生产环境落地建议 (Recommendations)

1. **采用“双层架构”**：
   - 上层：open-design 负责页面原型、视觉风格、设计资产生成。
   - 下层：Next.js + 表单状态管理（如 RHF/Zod）+ FastAPI/Node API 承担业务规则与 RBAC。

2. **把 SRP 规则写成机器可验证资产**：
   - 将 A-F 字段约束、SLA 推算、状态机迁移写成 JSON Schema + policy + 单元测试。
   - 所有“隐藏字段规则”必须服务端执行，前端仅作体验增强。

3. **建立“生成物准入门禁”**：
   - 对 open-design 生成页面执行自动化检查：i18n key 完整率、敏感字段暴露扫描、无障碍与性能基线。
   - 不通过门禁的 artifact 禁止进入主干。

---

## 已验证结论 vs 推测结论

### 已验证结论
- open-design 核心是 agent + skill + artifact 的生成式工作流，而非企业表单框架。
- 可用于 SRP 的 Token/文案/页面骨架生成，但不能替代后端 RBAC 与状态机。

### 推测结论（需后续 PoC）
- 若引入严格工程门禁，open-design 可显著缩短 P01-P08 初版 UI 交付周期。
- 在大规模多团队协作时，需评估 skill 演进治理成本与资产版本漂移风险。
