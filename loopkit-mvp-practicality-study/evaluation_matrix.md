# 中文化实用性评估矩阵

评分范围：1=弱，5=强。所有评分均基于本研究的 MVP 代码、pytest 结果、LoopKit 文件契约与 `skill_trigger_scan.py` 的静态触发数据。

| 维度 | 分数 | 证据 | 解释 |
|---|---:|---|---|
| 跨文件上下文把控度 | 4 | MVP 修改横跨 `routes`、`services`、`data`、`tests`；`PROMPT.md` 和 `IMPLEMENTATION_PLAN.md` 固化目标与步骤 | 文件状态外置显著降低上下文遗忘风险；但未实测长回合真实 Agent。 |
| 脚手架配置复杂度 | 4 | 复制 `.claude`、`.mcp.json`、`MEMORY.md`、`run.sh` 即可安装 | 工程成本低；但 `.claude/CLAUDE.md` 仍需人工替换项目命令模板。 |
| 对抗验证约束力 | 3 | `verifier.md` 明确要求按 11 类假完成检查 diff | 约束文本清晰；但真实 verifier 依赖 Claude CLI，本研究只能验证说明文件和模拟流程。 |
| 防幻觉与实用价值 | 4 | 认证需求触发 `spec-first`、`authz-check`、`input-validation`、`owasp-review`、`contract-test`、`adversarial-verify` 等技能 | 相比裸奔模式，能更早提醒 owner_id、401/404、输入边界与测试契约；减少无效修改的估算约为 25%–40%，属于模拟估计。 |
| 可复制性与扩展潜力 | 5 | 每个技能都是独立 `SKILL.md`，含 `name`、`description`、`when_to_use` 与短指令 | 第 34、35 个技能可按目录复制方式扩展；触发策略容易审查。 |
