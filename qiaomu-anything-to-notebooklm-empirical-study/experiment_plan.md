# Experiment Plan

## Research Questions
1. 项目是否可在无付费密钥环境完成安装与最小运行？
2. 是否能把代表性输入（Markdown、本地文件、公共网页）转换为 NotebookLM 可用产物？
3. 输出结构、可复现性与研究工作流价值如何？
4. 在缺少 NotebookLM 认证时，失败模式是否清晰可诊断？
5. 相比手工基线流程是否显著降低步骤或提高质量？

## Hypotheses
- H1: 代码可安装但端到端流程依赖 `notebooklm` CLI 登录。
- H2: 对 URL/文件类型识别可离线验证。
- H3: 无登录状态下会在上传阶段失败，但错误信息可记录。

## Test Environment
- Ubuntu 24.04.4, Python 3.12.13, Node 20.20.2。
- 无 `gh` 命令；无 NotebookLM 预认证。

## Test Dataset / Input
- 本地样例 Markdown：`artifacts/sample_public_domain.md`
- 公共网页：`https://example.com`
- 错误输入：不存在的本地路径

## Steps
1. 克隆并静态侦察 README/SKILL/main.py/requirements。
2. 执行官方安装命令（`pip install -r requirements.txt`）。
3. 运行 `check_env.py` 记录环境诊断。
4. 运行 `main.py`：
   - 本地 Markdown
   - 公共网页 URL
   - 不存在路径（边界）
5. 构建手工基线：`curl` 抓网页+清洗成 markdown/txt。
6. 比较步骤数、失败点、可复现性与输出质量。

## Expected Observations
- 安装可能成功，但 notebooklm 可执行文件/登录状态缺失。
- 输入识别正常，上传/提问阶段报错。
- 手工基线可稳定产出 NotebookLM-ready 文本文件。

## Success Criteria
- 至少完成 1 次真实运行到“调用 notebooklm”阶段并记录日志。
- 生成可审计证据（命令、输出、样例文件、对比结果）。

## Failure Criteria
- 代码无法运行到核心路径（早期崩溃且无可修复线索）。
- 无法生成任何可比较输出。

## Comparison Baseline
- 手工流程：下载公共网页 → 提取正文 → 存为 markdown/txt（NotebookLM 可上传）。

## Evidence to Collect
- setup_log/run_log
- 终端原始输出
- 生成文件（样例输入、基线输出）
- 代码引用与行级证据
