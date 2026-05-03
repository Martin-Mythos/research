# tw93/kami 设计系统解析与 Web 视觉重构实验报告

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## 1. 实验摘要 (Executive Summary)
Kami 的设计语言并不追求“组件繁多”，而是通过少量稳定 Token 形成统一阅读气质：纸感背景、近黑正文、品牌蓝强调、衬线主字体与克制留白。工程上它通过变量先行、模板复用、轻度语义类名来保持一致性，减少了视觉噪声与样式分叉。

将其应用到极简主页与 Web-PPT 时，体验是：**排版决定信息效率，Token 决定风格连续性**。即使不用复杂框架，仅 HTML + 内联 CSS 也能快速构建高辨识度页面。

## 2. Kami 的美学与工程解析 (Aesthetics & Engineering)

### 2.1 CSS 变量体系（Design Tokens）
从 `kami` 模板可提炼出高复用 Token：
- 色彩：`--parchment #f5f4ed`、`--near-black #141413`、`--olive #504e49`、`--stone #6b6a64`、`--brand #1B365D`。
- 字体：`--serif` 通常以 Charter/Georgia 与中日韩衬线回退组成。
- 结构：大量模板采用“纸感底色 + 近黑文本 + 蓝色强调 + 细边线”。

这种体系的优势是：低饱和、大对比、极少强调色，长文阅读疲劳更低。

### 2.2 Typography 规则
Kami 的排版不是“字号堆叠”，而是靠节奏控制：
- 标题常见更紧凑行高（约 1.05~1.15）与轻微负字距。
- 正文多在 1.45~1.55 行高区间，维持连续阅读流。
- 标签与小字常加大字距，增强信息分区感。

### 2.3 暗黑模式与色彩哲学
在本次检索范围内，Kami 更偏向固定浅底主题，未看到统一全局 dark mode 自动切换规则（如系统级 `prefers-color-scheme` 总入口）。这意味着：
- 优点：打印与文档风格高度稳定。
- 代价：若要深色主题，需在项目侧补充 Token 映射层（例如 `:root[data-theme="dark"]`）。

## 3. 实验执行记录与 Artifacts (Experiment Logs & Artifacts)

### Artifact 1：极简主页 (Lux 风格复刻)
实现要点：
- 使用 Kami 风格 Token（纸感底色、品牌蓝、衬线栈）。
- 使用大留白与左侧细品牌线，建立视觉锚点。
- 控制链接区装饰密度，仅保留细虚线下边框。

完整代码见：`index.html`。

### Artifact 2：AI 趋势 Web-PPT
实现要点：
- 采用 `scroll-snap-type: y mandatory` 做全屏滚动切页。
- 单页结构统一：kicker（高字距）、主标题、3 条关键 bullet。
- 内容聚焦 9 页：Agent 工作流、多模态推理、长上下文、端侧模型、推理成本、治理、开源生态、组织能力。

完整代码见：`presentation.html`。

## 4. 局限性与定制化建议 (Limitations & Recommendations)

### 局限性
1. Kami 强于阅读型页面，不直接覆盖复杂交互状态体系（表单校验、组件状态机、可访问性动态反馈）。
2. 复杂数据可视化场景中，仅靠当前 Token 不足以表达高密度图表语义层级。
3. 暗黑模式需要额外工程封装，跨端一致性需单独验证。

### 生产建议
1. 保留 Kami 的基础 Token 层，外扩一层“产品语义 Token”（成功/告警/错误/交互态）。
2. 针对表单与图表补充组件级规范：焦点环、禁用态、错误态、图例/网格/对比度阈值。
3. 引入可视回归（Playwright + 截图基线）确保版式在不同设备上的稳定性。
4. 为深浅主题建立同构变量映射，避免写死颜色导致维护成本上升。
