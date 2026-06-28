# Evaluation Matrix（1-5 分）

| Skill / Style | 分数 | 证据 | 主要风险 |
|---|---:|---|---|
| paper-analyzer | 4 | SKILL.md 强制 6 轮：读全文、搜代码、深度分析、风格确认、HTML、自审；academic 风格要求公式、图表、实验表和代码段。 | 工作流高度依赖 agent 是否真的完成检索；对早期论文的“原始代码 vs 替代实现”容易混淆。 |
| paper-figure（paper-comic style） | 4 | paper-comic 明确只画方法流程、核心机制、关键结果，并给出 paper-figure 视觉规范；仓库已有 Transformer overview 示例。 | 若生图模型把 Figure 1 重画成装饰性架构图，可能遗漏 decoder mask、cross-attention 或 positional encoding。 |
| sketchnote（paper-comic style / warm-notes） | 3 | sketchnote 规范强调温暖笔记、手绘箭头、局部放大和信息密度；适合解释 Q/K/V 直觉。 | “人味”会牺牲公式和维度精确度；multi-head 可能被简化成“很多箭头”。 |
| paper-deck | 3 | deck workflow 对 brief、outline、prompt files、真实素材计划和 quality gate 要求完整；style presets 清晰。 | V1 raster-first，当前无真实生图后端，因此不能验证 PPTX/PDF 生产就绪；中文图中文字也存在生成风险。 |

## 判分说明
- 5 = 当前环境可完整执行且技术/视觉/产物均可验证。
- 4 = 逻辑强、证据充分，但依赖外部模型或 agent 执行纪律。
- 3 = 可产出有用规划或样例，但生产级最终件无法在本环境闭环验证。
- 2 = 只能叙述，缺少可复现证据。
- 1 = 与任务不匹配或明显失败。
