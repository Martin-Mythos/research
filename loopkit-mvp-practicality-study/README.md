# 基于真实开发项目 MVP 的 AI 编码智能体 LoopKit 脚手架实用性实证研究

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## 研究问题
在真实的多文件业务项目（MVP）开发场景下，LoopKit 的自动化 Loop 与技能库能否有效提升 AI 智能体的一次性交付成功率并防止上下文断层？

## 方法概览
本研究在固定提交 `22101ff` 上侦察 Archive228/loopkit，读取 README、安装脚本、loop runner、`.claude` 治理文件和 33 个技能文件。随后构建一个 Python 标准库任务管理 API MVP，并注入跨层级认证授权需求：注册、登录、JWT、任务 owner_id 授权、未授权 401、跨用户 404。

## 核心发现
- 已验证：固定提交包含 33 个技能目录，安装器会写入 `.claude`、`.mcp.json`、`MEMORY.md` 和 `run.sh`；固定提交与来源信息见 `artifacts/source_snapshot.json`。
- 已验证：MVP 靶场完成了多文件功能新增，并包含未授权、跨用户隔离、token 防篡改和加盐密码散列测试。
- 模拟结果：研究协议明确选择 10/33 个相关技能；这是静态模拟，不是 Agent 运行时观测到的“触发率”。
- 未验证：没有无 LoopKit 的随机化对照组，也未运行真实 Claude CLI 循环，因此不能推断 LoopKit 提升了多少成功率或减少了多少无效修改。

## 复现状态
**部分复现 / 仅静态分析 + 高保真实真模拟**。MVP 代码和测试可完全复现；LoopKit 外部 LLM loop runner 未实际调用。

## 如何复现
```bash
cd loopkit-mvp-practicality-study/artifacts/mvp-target-codebase
python -m pytest -q tests
cd /workspace/research
git clone https://github.com/Archive228/loopkit /tmp/loopkit-pinned-source
git -C /tmp/loopkit-pinned-source checkout 22101ff114cbf80bf3d14d41c8c662f507b1b971
python loopkit-mvp-practicality-study/scripts/skill_trigger_scan.py \
  --skills-dir /tmp/loopkit-pinned-source/skills \
  --output loopkit-mvp-practicality-study/artifacts/skill_trigger_scan.json
```

## 主要产物
- `research_report.md`：完整中文研究报告。
- `experiment_plan.md`：实验设计。
- `run_log.md`：执行记录与失败路径。
- `evaluation_matrix.md`：中文量化评分矩阵。
- `notes/repo_recon.md`：目标仓库侦察。
- `artifacts/mvp-target-codebase/`：可运行 MVP 靶场。
