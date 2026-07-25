# 基于真实开发项目 MVP 的 AI 编码智能体 LoopKit 脚手架实用性实证研究报告

## 1. 执行摘要 (Executive Summary)
本研究对 Archive228/loopkit 的固定提交 `22101ff114cbf80bf3d14d41c8c662f507b1b971` 进行了静态侦察、MVP 靶场构建和显式规则模拟。LoopKit 不是糖尿病闭环系统，而是以文件契约、按需技能和敌对验证组织 AI Coding Agent 的脚手架。本研究验证了固定提交的安装结构和 33 个技能目录，并在多文件任务管理 API 中完成了认证授权功能。由于没有运行外部 Agent CLI，也没有裸奔 Agent 对照组，本研究不能回答“是否提升一次性交付成功率”的因果问题；验证状态为“部分复现 / 静态分析 + 显式模拟”。

## 2. 目标仓库定位与核心 Claim 梳理
目标仓库声称提供 33 个实战技能，覆盖 Agent 治理、调试、安全、测试、重构、文档、数据与 Git/Ops。核心 claim 是：技能只在相关触发条件下加载，从而减少 token 噪音；`run.sh` 以 Plan→Act→Verify 循环推进；verifier 子代理通过敌对视角检查假完成。

## 3. 实验靶场设计：微型多文件应用 MVP 规格定义
MVP 是一个任务管理 API 内核，使用 Python 标准库实现，保留 Web API 的分层结构：路由层 `src/routes/api.py`，业务层 `src/services/auth.py` 与 `src/services/tasks.py`，数据层 `src/data/store.py`，测试层 `tests/test_api.py`。功能包括用户注册、登录、任务创建、列表、读取和更新。

## 4. 环境配置与实证运行追踪 (包含核心命令与模拟调用链)
核心命令包括：克隆 LoopKit、检出固定提交、创建 MVP、运行 pytest、运行技能模拟扫描。真实 `run.sh` 的调用链需要 `claude -p`，本研究未调用外部 LLM API，转而按相同磁盘契约写入 `PROMPT.md` 与 `IMPLEMENTATION_PLAN.md`。最终提交不包含完整外部仓库或复制的技能库；`scripts/install_pinned_loopkit.sh` 可在复现时安装固定快照。

## 5. 核心发现 (Findings)
### 5.1 经 MVP 开发实战验证的优势特性
- 规格先行有效：`PROMPT.md` 明确禁止新增依赖，并列出 401、404、全量测试等完成条件。
- 多文件靶场可运行：认证需求跨越路由、业务、数据、测试四层，最终 pytest 通过；这证明实现本身可运行，不证明 LoopKit 导致了成功。
- 安全技能与需求高度匹配：`authz-check`、`input-validation`、`owasp-review`、`contract-test` 对此类任务的提示价值明显。

### 5.2 暴露出实用性缺陷、死循环或部分验证的边界
- `run.sh` 对 Claude CLI 有硬依赖，缺少无 API key 的本地 dry-run 模式。
- `.claude/CLAUDE.md` 中项目命令是模板，需要使用者安装后手动替换。
- 技能触发规则以自然语言为主，不是严格可执行规则；不同 Agent 对 `when_to_use` 的执行一致性仍需更大样本测试。

### 5.3 33 种核心技能在复杂上下文中的触发行为分析
本研究读取固定快照的 33 个技能文件，并在实验协议中显式选择 10 个：`spec-first`、`context-budget`、`authz-check`、`input-validation`、`owasp-review`、`write-failing-test-first`、`contract-test`、`adversarial-verify`、`secret-scan`、`clean-commits`。10/33 是模拟选择率，不是 Agent 实际触发率。前端类技能与纯后端实验低相关，但由于没有 token 遥测，不能量化按需加载节省了多少上下文。

## 6. 脚手架量化评估矩阵 (Evaluation Matrix)
详见 `evaluation_matrix.md`。评分反映证据充分度：安装与扩展结构可直接检查；上下文、防幻觉和 verifier 的真实效果因未运行 Agent 对照实验而只能给低到中等证据评分。

## 7. 实用性横向对比 (LoopKit 脚手架模式 vs 原生 Agent 裸奔模式)
LoopKit 文本协议明确提醒 Agent 检查资源所有权、401/404、输入边界和测试契约，这些机制在理论上针对常见失败模式。然而，本研究没有运行同一模型、同一提示、相同随机条件下的裸奔组和 LoopKit 组，因此删除初版报告中“减少 25%–40% 无效修改”的无依据估算。现有证据只支持机制描述，不支持效果量或显著性结论。

## 8. 智能体工程落地最佳实践 (Token 消耗平衡、技能按需加载机制)
建议在项目初始化后立即替换 `.claude/CLAUDE.md` 的命令模板，保留短上下文；每个复杂任务写 `PROMPT.md`；每轮只推进一个计划项；安全、迁移、授权等高风险变更必须触发 verifier。

## 9. 技术局限性与风险评估 (对抗死锁风险、多语言环境兼容度)
如果 verifier 只指出问题但 maker 没有明确停止条件，可能形成反复修补的对抗死锁。技能文本对多语言项目总体通用，但部分技能如 SQL migration、frontend a11y 对具体栈仍需本地化补充。

## 10. 结论与下一步开放研究建议
固定快照显示 LoopKit 是一个结构轻量、容易审查和扩展的 Agent 工程脚手架；本次 MVP 证明其文件契约可以映射到真实跨层任务，但没有证明它提升了 Agent 结果。下一步应在具备 Claude/Codex/Cursor 真实 CLI 的环境中预注册实验，运行多轮配对对照，比较一次性交付成功率、diff 规模、回滚次数和 token 成本。

## 11. 独立复现指南 (Reproduction Guide)
1. 进入仓库根目录。
2. 查看 `loopkit-mvp-practicality-study/artifacts/mvp-target-codebase/`。
3. 执行：`cd loopkit-mvp-practicality-study/artifacts/mvp-target-codebase && python -m pytest -q tests`。
4. 执行：`bash loopkit-mvp-practicality-study/scripts/install_pinned_loopkit.sh loopkit-mvp-practicality-study/artifacts/mvp-target-codebase /tmp/loopkit-pinned-source`（会联网，并把脚手架安装到本地工作树；复现后不要提交复制文件）。
5. 执行：`python loopkit-mvp-practicality-study/scripts/skill_trigger_scan.py --skills-dir /tmp/loopkit-pinned-source/skills --output loopkit-mvp-practicality-study/artifacts/skill_trigger_scan.json`。

## 12. 产出产物与证据清单 (Artifacts List)
- `README.md`：中文摘要报告。
- `research_report.md`：完整研究报告。
- `experiment_plan.md`：实验计划。
- `run_log.md`：运行日志。
- `evaluation_matrix.md`：量化矩阵。
- `sources.md`：资料来源。
- `notes/repo_recon.md`：仓库侦察。
- `scripts/skill_trigger_scan.py`：技能触发扫描脚本。
- `artifacts/mvp-target-codebase/`：MVP 靶场代码。
- `artifacts/pytest_output.txt`：测试输出。
- `artifacts/skill_trigger_scan.json`：技能扫描结果。
- `artifacts/source_snapshot.json`：固定来源提交与技能目录计数。
- `scripts/install_pinned_loopkit.sh`：临时安装固定 LoopKit 快照的复现脚本。
