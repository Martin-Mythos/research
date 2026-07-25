# 基于真实开发项目 MVP 的 AI 编码智能体 LoopKit 脚手架实用性实证研究

## 研究问题
在真实的多文件业务项目（MVP）开发场景下，LoopKit 的自动化 Loop 与技能库能否有效提升 AI 智能体的一次性交付成功率并防止上下文断层？

## 方法概览
本研究克隆并侦察 Archive228/loopkit，读取 README、安装脚本、loop runner、`.claude` 治理文件和 33 个技能文件。随后构建一个 Python 标准库任务管理 API MVP，并注入跨层级认证授权需求：注册、登录、Bearer token、任务 owner_id 授权、未授权 401、跨用户 404。

## 核心发现
- 已验证：LoopKit 的文件契约非常轻量，复制 `.claude`、`.mcp.json`、`MEMORY.md`、`run.sh` 即可落地到新项目。
- 已验证：MVP 靶场完成了多文件功能新增，`python -m pytest -q tests` 结果为 `3 passed in 0.04s`。
- 已验证：33 个技能覆盖面广，认证授权任务与安全、测试、规格先行和敌对验证类技能高度匹配。
- 部分验证：`run.sh` 的真实 Claude CLI 循环未运行；本研究采用磁盘契约复刻和静态触发模拟，不声称测得真实 token 成本或真实 Agent 成功率。

## 复现状态
**部分复现 / 仅静态分析 + 高保真实真模拟**。MVP 代码和测试可完全复现；LoopKit 外部 LLM loop runner 未实际调用。

## 如何复现
```bash
cd loopkit-mvp-practicality-study/artifacts/mvp-target-codebase
python -m pytest -q tests
cd /workspace/research
python loopkit-mvp-practicality-study/scripts/skill_trigger_scan.py
```

## 主要产物
- `research_report.md`：完整中文研究报告。
- `experiment_plan.md`：实验设计。
- `run_log.md`：执行记录与失败路径。
- `evaluation_matrix.md`：中文量化评分矩阵。
- `notes/repo_recon.md`：目标仓库侦察。
- `artifacts/mvp-target-codebase/`：可运行 MVP 靶场。
