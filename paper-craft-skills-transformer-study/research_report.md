# paper-craft-skills × Transformer 实证研究报告

## 结论摘要

本次研究验证了 `paper-craft-skills` 的核心价值不是“把论文翻译成 Markdown”，而是把论文重新组织为面向读者的解释链：读全文、定位代码、抽取机制、规划视觉、生成 HTML 或 slide prompt。对于《Attention Is All You Need》这种抽象度高、结构清晰、视觉要求严格的论文，Analyzer 和 Figure 路线最稳；Sketchnote 对教学友好但存在技术简化风险；Deck 的叙事和 prompt 工程完整，但由于其 V1 明确要求真实 raster image generation backend，本环境不能声称已生成 production-ready PPTX/PDF。

## 证据链

1. ArXiv 源：`https://arxiv.org/abs/1706.03762` 与 HTML 全文入口确认论文元信息、摘要、章节结构、Figure 1、Section 3.1-3.5、结果数字。
2. Repo 源：克隆 `https://github.com/zsyggg/paper-craft-skills`，阅读 README、中文 README、`skills/` 下核心 skill 文件与 deck references。
3. Prompt Plan：从 `paper-comic` 的方法图解步骤和 `paper-deck` 的 prompt template 生成 Transformer-specific prompt。
4. Visual Prompt：见 `artifacts/transformer_method_figure_prompts.txt`。
5. Artifact Outline：见 `artifacts/analyzer_transformer.html` 与 `artifacts/transformer_deck_outline.md`。

## Phase 1：仓库侦察

### Skill 架构

- `paper-analyzer`：强制 6 轮，包括获取论文全文、搜索开源代码、深度分析、询问风格、输出 HTML、自审。它将“文章质量”绑定到公式、图表、实验表和代码对照。
- `paper-comic`：实际承载 `paper-figure` 与 `sketchnote` 两种风格；仓库没有独立 `skills/paper-figure/` 或 `skills/sketchnote/` 目录。因此本报告把它们评估为 paper-comic 的两条 style path。
- `paper-deck`：raster-first slide workflow，必须先生成 analysis、deck brief、outline、per-slide prompts，再调用真实生图后端，最后合成 PPTX/PDF。
- Style presets：`journal-minimal`、`business-research`、`warm-notes`、`liquid-glass` 均在 deck style system 中定义。

## Phase 2：四项实验

### 2.1 paper-analyzer 深度解释

模拟命令：`/paper-analyzer https://arxiv.org/abs/1706.03762 --style=academic`。

观察：该技能要求同时读取 arXiv 摘要和 HTML 全文，并搜索代码。对 Transformer 而言，它应至少交叉引用：Figure 1 架构、Figure 2 attention、公式 `Attention(Q,K,V)`、MultiHead concat、decoder mask、position-wise FFN、positional encoding、WMT 结果。它的强项是会把公式后接“人话解释”，并把代码状态作为显式元信息。

产物：`artifacts/analyzer_transformer.html` 是 HTML 结构样例，包含元信息、机制重解释、公式解释、代码对照应有形态、实验表和 hallucination 风险标注。

### 2.2 paper-figure 方法图

模拟命令：`/paper-figure Transformer Architecture`。仓库实际入口应理解为 `/paper-comic ... --style paper-figure`。

观察：prompt engineering 的关键不是“画一个 Transformer”，而是保留事实关系：encoder stack、decoder stack、masked self-attention、encoder-decoder attention、FFN、Add & Norm、positional encoding、Linear/Softmax、scaled dot-product formula 和 multi-head concat。若模型只生成一个漂亮双塔图但漏掉 mask 或 Q/K/V，则属于 technical fidelity loss。

产物：`artifacts/transformer_method_figure_prompts.txt` 给出 paper-figure visual prompt，并指向仓库中已有 Transformer 示例图片路径作为参考。

### 2.3 sketchnote 手绘重构

模拟命令：`/sketchnote Attention Mechanism --style=warm-notes`。仓库实际入口应理解为 `/paper-comic ... --style sketchnote`，deck preset 中对应 `warm-notes`。

观察：sketchnote 的优势是用 token 卡片、Q/K/V 箭头、热力矩阵、softmax 高亮条和多 head 小面板降低理解门槛。缺点是很容易把 multi-head attention 画成“很多箭头同时看”，而没有表达不同投影子空间和 concat/output projection。

产物：同一 prompts 文件中包含 warm-notes prompt；本报告把未展示公式/维度的手绘图标记为 fidelity risk。

### 2.4 paper-deck PPTX 规划

模拟命令：`/paper-deck 1706.03762 --pages=10`。

观察：Deck skill 的逻辑透明度强，先做 brief 和 outline，再写每页 prompt。它还强制记录真实素材使用计划和 generation log。但本环境没有可用 raster image generation backend，且用户要求“模拟或执行（if environment allows）”，所以本研究只生成 10 页 deck outline，不冒充 PPTX/PDF 已生产。

产物：`notes/deck_structure.md` 和 `artifacts/transformer_deck_outline.md`。

## Phase 3：与 PDF-to-Markdown 的对比

标准 PDF-to-Markdown 的输出一般保留标题、段落、公式、图注和表格顺序。它擅长“忠实转写”，但不会自动决定哪些概念值得画、哪些数字适合进 deck、哪些图会诱发误解。

`paper-craft-skills` 的重新解释表现在三处：

1. **任务重排**：从论文顺序改为读者理解顺序，例如先讲 recurrence bottleneck，再讲 attention routing。
2. **视觉导演**：把 Figure 1 拆成 slide roles 和 prompt constraints，而不是复制原图。
3. **质量门禁**：主动标注不应 hallucinate 的事实，如 mask、cross-attention、BLEU 数字和训练成本。

## Verified visual logic vs AI hallucination

### Verified visual logic

- Transformer 是 encoder-decoder 架构。
- Encoder 层包含 multi-head self-attention 与 position-wise FFN，并带 residual + layer norm。
- Decoder 层额外包含 encoder-decoder attention，并在 self-attention 中使用 mask。
- Scaled dot-product attention 使用 `softmax(QK^T/sqrt(d_k))V`。
- Multi-head attention 使用并行 heads、concat 和输出投影。
- Positional encoding 是无 recurrence 情况下保留位置信息的关键部件。

### AI hallucination 风险

- 把 cross-attention 画成 decoder self-attention。
- 漏掉 causal mask，导致 decoder 能看未来 token。
- 把 multi-head attention 简化成多个相同 attention 的装饰性并排。
- 编造论文未报告的 benchmark、参数量或训练配置。
- 在 PPT 图里生成不可读中文、伪标签、假 logo 或假 UI。

## 最终评价

Analyzer 与 paper-figure 适合做高可信技术解读；sketchnote 适合教学但要加 fidelity checklist；Deck 的流程生产意识最强，但只有接入真实生图后端并检查 PPTX/PDF 后，才能称为 production-ready。
