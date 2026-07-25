# Empirical Study of Shifu Framework on Multi-Model Dispatching and Cost Optimization

## 1. 执行摘要

本研究对 `vikingmute/shifu` 进行了克隆、静态审查、官方安装命令验证，并构建了一个本地 mock harness 来模拟 `GPT5.6 Lula`、`GPT5.4 Mini`、`GPT5.3 Codex Spark` 三模型协作生成“背单词 CLI 应用”。

核心结论：Shifu 当前可验证为一个 Agent Skill，而不是完整的多模型 API 调度框架。它的主要产物是自包含 Markdown spec，用来帮助强模型规划、弱/便宜模型执行。研究未发现可执行的 API router、真实模型成本采集、自动 token 计量或自动错误恢复控制流。

在本研究自建 mock harness 中，多模型策略相对单旗舰模型基线显示 70.69% 的模拟成本节省，并成功检测/修复一次故意注入的 Python 语法错误。但这属于“策略可行性模拟”，不能归因于 Shifu 仓库已有的可执行能力。

## 2. Subagent Routing Architecture

### 目标项目声称

Shifu README 声称其工作流是：高能力模型负责理解任务、判断拆分边界、编写清晰 spec；便宜模型负责执行。`SKILL.md` 将执行策略抽象为：

- `direct`：当前目录执行。
- `worktree`：隔离 worktree 执行。
- `explore`：只读探索。

它还描述了在 Codex 环境中 `direct/worktree` 对应 `worker`，`explore` 对应 `explorer`。

### 本研究直接验证

- 官方安装命令 `npx skills add vikingmute/shifu` 成功。
- 仓库核心实现是 `skills/shifu/SKILL.md`。
- 未发现 JavaScript/Python/Rust 等传统 runtime 代码。
- 未发现 endpoint 配置、API key 加载、模型价格表、token counter 或 dispatch scheduler。

### 谨慎推断

Shifu 的 routing architecture 是 instruction-level orchestration：它通过给宿主 Agent 的自然语言规则来引导模型选择和任务委派，而不是在仓库内实现一个可独立运行的 router。

## 3. 实验证据：日志与成本指标

### 安装/初始化

- 命令：`npx skills add vikingmute/shifu`
- 结果：安装成功，输出显示 `✓ shifu (copied)`。
- 限制：安装的是 skill 文件，不是多模型服务。

### Vocabulary App mock 产物

本研究生成了：

- `artifacts/vocab_app_bad.py`：故意包含语法错误的 Spark 输出。
- `artifacts/vocab_app.py`：修复后的背单词 CLI。
- `artifacts/vocab_data.json`：小型词库。
- `artifacts/mock_routing_logs.json`：mock routing、token、cost、latency 记录。

验证命令：

```bash
python3 -m py_compile shifu-multimodel-cost-optimization-study/artifacts/vocab_app.py
python3 shifu-multimodel-cost-optimization-study/artifacts/vocab_app.py stats
python3 shifu-multimodel-cost-optimization-study/artifacts/vocab_app.py quiz --answer 放弃
```

输出：

- `stats`：`{"total_words": 2}`
- `quiz --answer 放弃`：`correct`

### 模拟成本

| 路径 | 成本估计 | 延迟估计 |
|---|---:|---:|
| 多模型 mock run | 0.012628 | 6.2s |
| 单旗舰 baseline | 0.043080 | 10.0s |
| 差异 | 节省 70.69% | 节省 38.0% |

这些数字来自本地脚本中的相对价格表和 token 近似算法，并非真实供应商账单。

## 4. Findings（Verified vs. Failed）

### 已验证

1. Shifu 仓库可以克隆。
2. Shifu 可以通过 `npx skills add vikingmute/shifu` 安装为 Agent Skill。
3. Shifu 文档明确主张“强模型规划、便宜模型执行”的成本优化模式。
4. Shifu 的 skill 文本包含自包含 spec、验证门、边界、STOP 条件、prompt injection 防护提醒等工程约束。
5. 本研究 mock harness 可模拟三模型 handoff、检测语法错误并生成可运行 CLI。

### 失败或无法验证

1. 无法验证 Shifu 自身真实调用 `GPT5.6 Lula`、`GPT5.4 Mini`、`GPT5.3 Codex Spark`，因为仓库没有模型 API client。
2. 无法验证 Shifu 自身真实 token 成本降低，因为没有 telemetry 或 billing integration。
3. 无法验证自动“Spark 语法错误 → Lula/Mini 修复 → Spark 重写”的框架内控制流，因为该逻辑不在目标仓库代码中。
4. 无法验证真实 subagent context schema，因为 Shifu 的上下文传递主要是 Markdown spec，而非机器校验 schema。

### 谨慎推断

- 如果宿主 Agent 严格执行 Shifu 的 spec 规范，并允许用户指定低价模型，那么 Shifu 可能帮助降低人工规划/执行混用场景的成本。
- 成本收益大小高度依赖任务分解质量、模型价格、返工率、上下文长度和宿主 Agent 的 subagent 能力。

### 仍未知

- 在真实 Codex/Cursor/Claude Code 多代理环境中，Shifu 的长期成功率、返工率和上下文漂移率。
- 大型真实代码库中的计划粒度是否稳定。
- skill 指令是否足以抵御复杂 prompt injection 与恶意仓库内容。

## 5. Evaluation Matrix

见 `evaluation_matrix.md`。综合评价：Shifu 是清晰的计划/委派 skill，但不是已完整实现的多模型成本优化 runtime。

## 6. R&D 与网络安全视角

### 可维护性

优点：

- Markdown spec 可读、可审查、可复制。
- STOP 条件和验证门降低小模型即兴发挥风险。
- 计划文件与代码实现分离，便于 code review。

风险：

- 缺少 schema validation，worker 是否保留关键上下文只能靠 prompt 约束。
- 缺少强制路由审计，无法证明某个模型实际执行了某个任务。
- 缺少自动成本/延迟采集，成本优化结论很难复现。

### 安全性

优点：

- `SKILL.md` 明确要求把仓库内容视为 data，而不是 instructions。
- 明确要求不复现 secret 值。

风险：

- prompt injection 防护是文本规则，不是 sandbox/policy engine。
- 如果 worker 直接执行 spec 中生成的命令，仍可能受到恶意 repo 文件影响。
- 建议增加 secret scanning、allowlist command policy、structured handoff schema 和 append-only audit log。

## 7. 建议

1. 把 Shifu 定位为“Agent Skill for decomposition”，不要宣传为已经具备独立多模型 dispatch runtime。
2. 增加机器可读 plan schema，例如 `plans/index.json`，记录 task id、strategy、model、input hash、output hash、verification gates。
3. 增加可选成本估算脚本，至少基于 token 近似与用户配置价格表生成 reproducible report。
4. 增加 failure-loop 示例：worker 失败后如何把错误报告回 planner 并生成修订 spec。
5. 增加安全基线：命令 allowlist、secret pattern redaction、prompt injection test fixture。
