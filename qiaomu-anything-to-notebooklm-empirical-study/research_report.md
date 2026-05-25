# Qiaomu Anything-to-NotebookLM empirical research

## 1. Executive Summary
本研究在 Codex Cloud 沙箱对 `joeseesun/qiaomu-anything-to-notebooklm` 做了实证烟雾测试。结果：**部分复现**。项目可安装并识别输入类型，但在无 `notebooklm` CLI/认证的公共环境中无法完成上传与后续生成。

## 2. Project Overview
项目宣称支持网页、微信公众号、YouTube、播客、PDF、Markdown 等输入，自动上传到 NotebookLM 并产出多种格式内容。

## 3. Research Questions
见 `experiment_plan.md`。

## 4. Experiment Design
执行了安装、环境检查、核心运行、错误边界、手工基线对照。

## 5. Setup & Execution Evidence
- 环境与版本：`setup_log.md`
- 运行日志：`run_log.md`
- 样例与输出：`artifacts/`

## 6. Findings
### 6.1 Verified Findings
- 依赖可安装，`main.py` 可执行到上传步骤。
- 本地 Markdown 与 URL 输入均能被识别为对应类型。
- 缺少 `notebooklm` 命令会触发 `FileNotFoundError` 并终止。

### 6.2 Failed or Partially Verified Findings
- 未能在该环境验证真实上传到 NotebookLM。
- 无法验证“自动生成播客/PPT/思维导图”链路。

### 6.3 Unverified Claims
- README 中关于多平台深度处理与付费墙策略的稳定性与成功率。

### 6.4 Surprising Observations
- `check_env.py` 校验 `wexin-read-mcp` 路径，而仓库目录是 `feishu-read-mcp`，存在文档/代码漂移迹象。

## 7. Evaluation Matrix
见 `evaluation_matrix.md`。

## 8. Comparison With Baseline
- 工具流程：自动识别类型 + 调用 NotebookLM CLI（环境依赖强）。
- 手工基线：将本地样例清洗为纯文本/Markdown，可直接作为 NotebookLM 导入材料。
- 在本沙箱中，手工基线更可复现（无外部 CLI 依赖）。

## 9. Practical Use Cases
适合已经完成 NotebookLM CLI 认证、且希望批处理多源输入的个人研究工作流。

## 10. Limitations & Risks
外部依赖重、认证要求高、错误处理需增强；抓取相关行为需合规审查。

## 11. Recommendations
1. 提供无 NotebookLM 时的 dry-run 模式；
2. 将 `notebooklm` 缺失错误转为友好提示；
3. 修复 MCP 路径检查并增加 CI。

## 12. Reproduction Guide
1. `git clone` 目标仓库；
2. `python3 -m pip install -r requirements.txt`；
3. `python3 check_env.py`；
4. `python3 main.py <input> "<prompt>"`；
5. 若要端到端，需先满足 `notebooklm login`。

## 13. Artifacts
- `artifacts/sample_public_domain.md`
- `artifacts/baseline_local_clean.txt`
- `artifacts/baseline_local_clean.md`
- `artifacts/recon_raw.txt`

## 14. Appendix
- 网络请求 `curl https://example.com` 在本环境返回 `CONNECT tunnel failed, response 403`，因此公共网页实验改为本地样例对照。
