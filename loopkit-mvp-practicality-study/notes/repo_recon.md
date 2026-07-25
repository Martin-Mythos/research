# LoopKit 仓库侦察记录

## 已验证的仓库定位
本研究固定在提交 `22101ff114cbf80bf3d14d41c8c662f507b1b971`。该快照的 README 自称是“33 个 battle-tested skills”的集合，并附带最小 `.claude/` 治理套件、`MEMORY.md`、MCP 配置与 `run.sh`。README 声称这些技能会在相关触发条件出现时才加载；这是项目 claim，本研究没有运行时遥测来独立验证自动加载行为。

## Plan→Act→Verify 状态机
`run.sh` 的闭环非常小：循环调用 `claude -p "Read PROMPT.md and IMPLEMENTATION_PLAN.md. Do the next step. Commit on green."`，随后调用 `claude -p "/verify"`，当 `IMPLEMENTATION_PLAN.md` 出现 `STATUS: done` 时结束。也就是说，状态并不主要保存在聊天上下文中，而是保存在磁盘文件中。

`.claude/CLAUDE.md` 强调：先读现有文件再写、单一目的变更、不得在未运行 verifier 的情况下宣布完成。`.claude/agents/verifier.md` 要求 verifier 假定代码有问题，读取 `PROMPT.md` 与 diff，并按照 adversarial-verify 技能中的 11 类“假完成”捷径输出 JSON。

## 33 种技能的工程分类
- Agent/LLM 治理：`context-budget`、`spec-first`、`tool-restraint`、`subagent-fanout`。
- Debug：`systematic-debugging`、`read-the-trace`、`bisect-regression`。
- Security：`owasp-review`、`authz-check`、`input-validation`、`secret-scan`、`dependency-audit`。
- Frontend：`design-system`、`a11y-pass`、`loading-empty-error-states`。
- Testing：`write-failing-test-first`、`flaky-hunter`、`coverage-gaps`、`contract-test`。
- Refactor：`kill-dead-code`、`simplify`、`reduce-nesting`。
- Docs：`changelog-from-diff`、`decision-record`、`readme-audit`。
- Data：`sql-review`、`migration-writer`、`schema-diff`。
- Git/Ops：`clean-commits`、`pr-from-diff`、`rebase-safely`、`revert-surgical`。
- Review：`adversarial-verify`。

## 行为约束机制
LoopKit 的核心不是替代模型能力，而是把目标规格、计划状态、技能触发和敌对验证外置到文件与子代理说明中。它通过 `PROMPT.md` 限定目标，通过 `IMPLEMENTATION_PLAN.md` 限定下一步，通过技能的 `when_to_use` 提醒模型在相关场景执行专门检查，通过 verifier 防止“测试放松、硬编码、越权修改、只做 happy path”等常见错误。
