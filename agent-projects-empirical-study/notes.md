# 研究笔记

## 原始研究问题
- 基于仓库 `https://github.com/Arindam200/awesome-ai-apps` 中 5 个指定 AI Agent 项目，进行架构解析、实验设计与客观评估，并输出中文报告。

## 工作日志

### 2026-05-03
- 创建研究目录：`agent-projects-empirical-study`
- 初始化笔记文件。

- 命令：`rg --files`（确认当前仓库结构，避免污染其他研究目录）。
- 数据源URL：
  - `https://raw.githubusercontent.com/Arindam200/awesome-ai-apps/main/README.md`
  - `https://api.github.com/repos/Arindam200/awesome-ai-apps/git/trees/main?recursive=1`
  - 各项目 `README.md` 与核心 `.py` 文件 raw 地址（见 `artifacts/upstream/` 文件名映射）。
- 命令：`curl -L .../README.md` + `rg -n` 用于定位目标项目路径。
- 命令：Python 脚本调用 GitHub Tree API，导出 `artifacts/selected_paths.txt`（共 87 条关键文件路径样本）。
- 实验：抓取 5 个项目对应说明与代码入口，结果：
  - `deep_researcher_agent/main.py` 不存在（404），后续改抓取 `agents.py`/`server.py`/`app.py`。
  - `advanced_rag_with_reranking/app.py`、`retriever.py` 不存在（404），后续根据 tree 结果改为 `src/boeing_rag/*` 路径。
- 可复现实验脚本：`scripts_extract.py`，对抓取文件进行静态信号扫描，输出 `artifacts/static_signal_scan.json`。
- 验证证据：`python agent-projects-empirical-study/scripts_extract.py` 成功写出 13 个文件的统计结果。
