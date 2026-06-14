# Understand-Anything for ASF 2026 site structure research

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

- 目标工具：`Lum1104/Understand-Anything`
- 目标语料：`xwbcl123/asf-site-v2`（私有）
- 复现状态：**partially reproduced**

## 摘要
本研究完成了 Understand-Anything 在可访问仓库上的端到端脚本验证（scan/import-map/batches），并记录了对 ASF 私有仓库访问失败证据，因此无法完成同语料完整对照。

## 关键发现
- 工具可生成结构化中间图数据。
- 私有仓库访问是当前最大阻塞。
- 测试套件存在一次 unhandled worker timeout。

## 主要文档
- `research_report.md`
- `experiment_plan.md`
- `run_log.md`
- `evaluation_matrix.md`
- `artifacts/*.log`
