# 实验计划：Vocabulary Memorization App 多模型调度与成本优化

## 研究标题

Empirical Study of Shifu Framework on Multi-Model Dispatching and Cost Optimization

## 核心问题

Shifu 是否能在 `GPT5.6 Lula`、`GPT5.4 Mini`、`GPT5.3 Codex Spark` 之间智能路由任务，构建一个完整的“Vocabulary Memorization（背单词）”迷你应用，并显著降低成本？

## 安全与模型约束

- 仅使用 mocked/sandbox 模型名称：`GPT5.6 Lula`、`GPT5.4 Mini`、`GPT5.3 Codex Spark`。
- 不调用真实 LLM API，不使用真实 API key。
- 不运行目标仓库中不存在的未知脚本；目标仓库只作为 skill 文本分析与安装测试对象。

## 实验对象

目标应用采用最小 CLI 版本，功能包括：

1. 内置词库。
2. quiz 模式：显示英文，要求输入中文释义。
3. add 模式：追加词条到 JSON 文件。
4. stats 模式：显示学习统计。
5. 基础单元测试或 smoke test。

## 强制路由设计

| 子任务 | 期望模型 | 角色 |
|---|---|---|
| Planning/Architecture Subagent | GPT5.6 Lula | 需求拆分、架构设计、验收标准 |
| General Logic/Data Subagent | GPT5.4 Mini | 数据模型、词库、评分逻辑 |
| Coding/Formatting Subagent | GPT5.3 Codex Spark | 生成 CLI 代码、格式化、测试修复 |

## 测试 1：Smoke Test

目标：验证 Shifu 是否能安装/初始化多代理环境。

步骤：

1. 克隆 `vikingmute/shifu`。
2. 运行官方安装命令 `npx skills add vikingmute/shifu`。
3. 检查安装输出和本地 skill 文件。

判定：若 skill 可安装但没有可执行 router，则只记为“skill 安装成功”，不记为“多代理运行时初始化成功”。

## 测试 2：Core Capability Test

目标：验证上下文是否能在 Lula、Mini、Spark 三个 mocked agent 之间传递而不丢失关键 schema。

方法：编写本地 mock harness，模拟三个 agent 的输入/输出 JSON，包括 `task_id`、`model`、`input_context_hash`、`output_context_hash`、`parent_output_hash`、`schema_version`。逐阶段断言输入 hash 等于父阶段输出 hash，并检查 app 名称、功能列表、语言和验收标准等必需字段。

判定：该测试只能验证“我们设计的 mock 协议可保持上下文”，不能证明 Shifu 真实运行时具备此能力。

## 测试 3：Failure/Boundary Test

目标：模拟 `GPT5.3 Codex Spark` 生成语法错误，观察检测与修复路径。

方法：mock harness 先生成一个带语法错误的 Python CLI 文件，并用 AST/`python -m py_compile` 验证失败。随后执行 Spark 失败 → Lula 诊断 → Mini 生成修复 spec → Spark 输出修复版的明确链路。

判定：若 py_compile 从失败变为通过，说明实验 harness 能检测并修复；但 Shifu 仓库本身没有自动修复控制流，因此不能归功为 Shifu 的已实现能力。

## 测试 4：Comparison Baseline

目标：比较多模型模拟运行与单旗舰模型模拟运行的 token cost 与 latency。

方法：使用相同任务分解，按字符数近似 token（`ceil(chars/4)`），为 mocked 模型配置相对价格和固定延迟：

| 模型 | 输入单价/1K token | 输出单价/1K token | 模拟延迟 |
|---|---:|---:|---:|
| GPT5.6 Lula | 0.030 | 0.060 | 2.0s |
| GPT5.4 Mini | 0.006 | 0.012 | 0.8s |
| GPT5.3 Codex Spark | 0.004 | 0.008 | 0.7s |
| Single Flagship Baseline | 0.030 | 0.060 | 2.0s/step |

判定：baseline 必须对与多模型路径完全相同的 event/token workload 重新计价，并以自动测试验证算术。报告结果只能称为“假设驱动模拟差异”，不作为真实供应商价格、真实 latency 或 Shifu 实际节省证据。
