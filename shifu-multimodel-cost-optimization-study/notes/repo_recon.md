# 仓库侦察：vikingmute/shifu

## 数据源

- 目标仓库：<https://github.com/vikingmute/shifu>
- 本地克隆路径：`/tmp/shifu-target`
- 检查文件：`README.md`、`skills/shifu/SKILL.md`

## 已验证事实

1. 仓库内容极小，核心实现是一个 Agent Skill：`skills/shifu/SKILL.md`；根目录只有 README、LICENSE、`.gitignore` 与 skill 目录。
2. README 声称 Shifu 是“把复杂任务拆成自包含规格说明，再交给便宜模型执行”的 skill，而不是传统 npm/python 库。
3. `skills/shifu/SKILL.md` 的硬规则明确要求 Shifu 自身“不直接实现代码”，只写 `plans/` 或 `shifu-plans/` 下的计划文件。
4. Shifu 的执行策略是语义层的 `direct`、`worktree`、`explore`，并在文档中映射到 Cursor、Codex、Claude Code 等宿主环境的子代理能力。
5. 模型选择机制主要是 prompt/instruction 级别：用户可以通过 `/shifu execute ... --model <model>` 指定 worker model；skill 文本没有可执行的 API client、router、token meter 或 billing collector。

## 与研究问题相关的架构分析

### LLM API 配置

未发现传统 SDK 配置文件、环境变量加载代码或 API endpoint 配置代码。Shifu 依赖宿主 Agent 环境提供模型与 subagent API。也就是说，Shifu 自身没有可直接配置为 `GPT5.6 Lula`、`GPT5.4 Mini`、`GPT5.3 Codex Spark` 的 API 层。

### 子代理初始化

`SKILL.md` 描述了策略到宿主子代理类型的映射：在 Codex 中 `direct`/`worktree` 对应 `worker`，`explore` 对应 `explorer`。这属于自然语言操作规程，而非可调用的本地代码。

### 任务委派

Shifu 的主要产物是 `plans/*.md`：每个子任务包含上下文、步骤、验证命令、边界和 STOP 条件。委派是否真正发生取决于宿主是否支持 subagent，以及执行者是否遵守 skill 指令。

## 谨慎推断

- Shifu 更像“计划生成/委派协议”而不是“多模型调度框架”。
- 成本优化依赖人工或宿主 Agent 按 `--model` 选择较便宜模型；仓库未提供自动成本优化算法。
- 对多模型上下文传递的核心保障来自自包含 Markdown spec，而不是结构化消息 schema 或状态数据库。

## 未验证/无法验证

- 未验证真实模型 API 调用，因为仓库没有 API client，且研究要求仅使用 mocked/sandbox 模型。
- 未验证真实 token cost，因为没有接入真实 billing；后续只能使用模拟 token 与价格表比较。
- 未验证自动“语法错误检测后回路由给 Lula/Mini”的能力；仓库没有实现该自动控制流。
