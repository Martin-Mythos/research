# Understand-Anything for ASF 2026 site structure research

## 1. Executive Summary
本研究对 Understand-Anything 进行了实证执行。核心结论：工具链在可访问仓库上可运行并输出结构化图谱中间结果；但目标语料 `asf-site-v2` 因私有访问失败，故本次为“部分复现”。

## 2. Project Overview
目标工具是一个代码理解插件生态，含扫描、导入图构建、批次聚类及可视化 dashboard。

## 3. Research Questions
见 `experiment_plan.md`。

## 4. Experiment Design
包含 smoke/core/代表场景/失败边界/手工基线。

## 5. Setup & Execution Evidence
详见 `setup_log.md`、`run_log.md` 与 `artifacts/*.log`。

## 6. Findings
### 6.1 Verified Findings
- 可克隆并安装 Understand-Anything。
- 可运行 `scan-project`、`extract-import-map`、`compute-batches` 并生成 JSON。

### 6.2 Failed or Partially Verified Findings
- 无法克隆 `asf-site-v2`，错误为 GitHub 用户名/凭据读取失败。
- `pnpm test` 虽测试通过，但 vitest worker timeout 导致总任务失败。

### 6.3 Unverified Claims
- 未验证对 ASF 2026 站点仓库的真实页面路由/内容数据源映射能力。

### 6.4 Surprising Observations
- 文档级别不总是覆盖脚本输入 schema，需要查源码修正调用方式。

## 7. Evaluation Matrix
见 `evaluation_matrix.md`。

## 8. Comparison With Baseline
- 期望基线：对 asf-site-v2 进行 tree/find/rg + package/README 侦察。
- 实际：因私有仓库不可访问，仅完成“访问失败证据”采集，无法做同一语料对照。

## 9. Practical Use Cases
- 在可访问仓库中快速生成文件分类与依赖关系，辅助 reviewer 进入代码结构。

## 10. Limitations & Risks
- 私有仓库认证依赖外部环境；测试稳定性受执行器并发/超时影响。

## 11. Recommendations
- 优先补齐私有仓库认证，再复跑代表场景。
- 为 `extract-import-map` 增加更明确 CLI 入参校验文档。

## 12. Reproduction Guide
按 `setup_log.md` 环境，执行 `run_log.md` 命令序列。

## 13. Artifacts
见 `artifacts/`。

## 14. Appendix
见 `notes.md`、`notes/repo_recon.md`。
