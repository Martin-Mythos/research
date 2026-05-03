# 敏捷 SaaS 场景下 compound-engineering-plugin 架构实证报告

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## 1. 实验摘要 (Executive Summary)

**已验证结论**
- `compound-engineering-plugin` 的核心并非“单体执行器”，而是以 **SKILL.md 工作流规范 + 多代理调度约定 + 跨平台转换器** 组成的方法工程化层。它通过 `ce-plan`、`ce-brainstorm` 等技能把产品语言转为结构化计划，再由 `ce-work` 等技能执行。  
- 在“AI 协作 Markdown 编辑器”场景下，插件方法论对需求拆解的优势是：能够将“产品句子”强制映射为“范围边界、技术决策、测试场景、后续 issue/执行路由”。

**推演结论（非直接运行）**
- 若输入“多人实时协同编辑”，该体系会倾向生成“先调研/再选型/再实现”的工程化任务，而非直接输出空泛 TODO；是否能自动提到 CRDT/OT，取决于研究阶段上下文质量与代理执行质量。

## 2. 核心机制解析 (Mechanics & Codebase)

### 2.1 技术栈与结构
- 代码层：TypeScript + Bun CLI，入口为命令系统（如 `install`/`convert`）。
- 解析层：`src/parsers/claude.ts` 负责读取 `.claude-plugin/plugin.json`、agents/commands/skills，并把 SKILL/Agent 元数据转换为内部对象。
- 编排层：技能（尤其 `ce-plan`）在提示词里定义了严格的阶段化流程（Phase 0~5），包括澄清提问、来源文档继承、并行 research、confidence check、issue 创建路由。

### 2.2 为什么它像“AI PM 工程中间件”
- 其价值不在生成代码本身，而在于把“需求讨论”标准化为可复用协议：
  1) 输入归一（feature_description + 来源文档）
  2) 研究并行化（repo/learnings/web/issue intelligence）
  3) 输出模板化（计划文档、后续 issue/workflow）
- 这与配套指南中的 AI PM 思路一致：把 PM 思考过程拆成可重复、可验证、可追踪的步骤。

## 3. 实验执行记录与 Artifacts (Experiment Logs & Artifacts)

> 说明：由于沙盒内缺乏宿主 IDE Agent 运行时，本研究采用“源码级推演 + mock 外部集成”方案。

### 实验一：需求摄取测试

**输入**：`AI 幽灵补全（光标监听、防抖、LLM 流式接口）` 一句话 User Story。  
**观察点**：`ce-plan` 的参数进入 `<feature_description> #$ARGUMENTS`，随后触发文档检索与 bootstrap。  
**Artifact（配置/内部结构）**：`artifact-exp1-input-schema.json`

```json
{
  "experiment": "需求摄取",
  "entry_skill": "ce-plan",
  "normalized_input": {
    "domain": "software",
    "requires_clarification": false
  }
}
```

### 实验二：工程卡片拆解 (CRDT/实时协同)

**输入**：`多人实时协同编辑`。  
**推演输出**：5 张核心工程卡，覆盖算法选型、传输层、操作协议、光标同步、离线补偿。  
**Artifact**：`artifact-exp2-engineering-tickets.json`

**客观打分（架构师思维）**：8.5/10  
- 加分：触及 CRDT/OT、WebSocket 路由、op schema、presence、断网重连。  
- 扣分：未绑定具体技术栈时，仍依赖后续 research 质量，无法保证“一次性给出最优实现细节”。

### 实验三：模糊需求处理

**输入**：`让编辑器的响应速度变得很快`。  
**观察结论**：按 `ce-plan` 规范，理应先做澄清或基线测量（Spike），而不是直接编造缓存方案。  
**Artifact**：`artifact-exp3-edgecase-log.json`

**输出模式**：
- SPIKE：性能基线与指标定义
- SPIKE：瓶颈分析（如 flamegraph）
- TASK：在阈值明确后再进入实现

## 4. 局限性分析 (Limitations)

**已验证局限**
1. 插件本质偏“流程协议层”，不等于可直接运行的 PM 后端系统；强依赖宿主 agent 平台能力。  
2. 对复杂前端状态交互（协同编辑、离线冲突）的指导深度，受上下文喂料与研究代理质量波动影响明显。  
3. issue tracker（GitHub/Linear/Jira 类）更多是“后置路由与落单机制”，不是强事务性的项目管理引擎。

**推测局限**
- 在超大规模多团队协作下，若无统一 schema 与组织级规范，技能输出可能出现跨团队术语漂移与计划粒度不一致。

## 5. 生产环境落地建议 (Recommendations)

1. **先固化组织级输入模板**：在接入前统一需求输入 schema（目标、验收、约束、非目标），降低 LLM 在 Phase 0 的解释漂移。  
2. **把“Spike 任务”设为强制关卡**：对性能、协同、离线等高不确定特性，要求先产出可测基线，再允许进入实现卡片。  
3. **二次开发“票据后处理器”**：将 ce-plan 产物自动补齐为你们 Jira/Linear 的字段（组件、优先级、风险、依赖图），形成闭环追踪。

## 附：交付件清单
- `notes.md`：全流程研究笔记
- `generate_artifacts.py`：可复现实验产物生成脚本
- `artifact-exp1-input-schema.json`
- `artifact-exp2-engineering-tickets.json`
- `artifact-exp3-edgecase-log.json`
- `verification.log`

## 6. 复审修订（针对 PR 反馈的补强）

- 新增 `extract_evidence.py` 与 `artifact-source-evidence.json`，把关键结论改为“可程序化验真”：
  1) `loadClaudePlugin` 与 `.claude-plugin/plugin.json` 解析入口存在；
  2) `ce-plan` 使用 `<feature_description> #$ARGUMENTS` 注入输入；
  3) plan handoff 中存在 GitHub/Linear issue 创建路由命令。
- 该补强用于降低“主观推演”占比，提高可重复审计性。
