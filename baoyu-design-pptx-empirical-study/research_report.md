# Baoyu-Design 设计系统与可编辑 PPTX 生成能力实证研究报告

## 1. 执行摘要 (Executive Summary)

本地复现实验已跑通 Baoyu-Design 的核心可编辑 PPTX 导出链路：`HTML deck -> Playwright capture -> PptxGenJS -> editable PPTX`。本轮使用本地 image generation 生成 PNG 插图，并由 Baoyu CLI 生成 `baoyu-design-imagegen-editable.pptx`，包含 3 页、约 3.47 MB，CLI 返回无 validation flags、无 warnings，并成功写入 speaker notes。

核心结论：Baoyu-Design 的可编辑 PPTX 技术路线成立，不是简单整页截图导出。OOXML 检查显示每页都有原生文本体 (`p:txBody`) 与形状 (`p:sp`)，第 1/3 页包含图片对象 (`p:pic`)。但“自然语言稳定生成完整 Design System”和“目标项目自身 Image Generation API 调用”仍未完全验证；本研究改用本地 image generation 产物隔离 API 鉴权与成本变量。

最终建议：**Trial / Reference Only**。适合作为 AI Agent 生成可编辑 PPTX 的参考架构；生产采用前仍需补齐 PowerPoint/Keynote 人工编辑验证、复杂版式压力测试、浏览器依赖缓存和真实图像生成 record/replay 机制。

## 2. 项目概述与架构分析

Baoyu-Design 是一个 AI agent skill package，而不是单一传统 CLI 应用。仓库中的 `skills/baoyu-design/` 包含 deck、design system、image、prototype、PPTX export 等工作流。

- 核心依赖库：`playwright`、`pptxgenjs`、`esbuild`、`typescript`。
- PPTX 引擎：`PptxGenJS`。
- 浏览器捕获：`Playwright` 打开本地 HTTP deck，注入 capture bundle，逐页读取 DOM box、style、text、image、SVG、gradient 等。
- 图像生成 API 对接设计：仓库提供 `generate-images.md` 与 `image-slot.js` 这类 skill/component 入口；真正的模型调用依赖宿主 agent/runtime。本研究只验证图像插入与 PPTX layout，不调用真实付费 Image Generation API。

关键路径：

```text
served HTML deck
  -> Playwright Chromium
  -> capture-editable.ts
  -> captured slide tree
  -> media-cache.ts
  -> build-editable.ts / render-node.ts
  -> pptxgenjs native PPTX
```

## 3. 核心研究问题

| 问题 | 本轮结论 |
|---|---|
| Design System 核心生成能力 | 仓库具备 design-system authoring/check/compile/import/preview 工作流；但未验证真实 LLM 从自然语言稳定生成完整设计系统。 |
| 可编辑 PPTX 导出能力 | 已验证。真实 CLI 生成 PPTX；OOXML 包含 native text、shape、picture、notes。 |
| 图像伴随生成与插入 | 插入链路已验证。使用本地 image generation PNG 作为生成图输入；目标项目自身 API 调用未验证。 |

## 4. 实验设计与复现路径

实验 1：Design System smoke test。使用 `Corporate Tech Branding - Ocean Blue & Minimalist` 主题，构造包含 palette、type scale、spacing、radius、component rhythm 的三页 deck，并对照仓库内 design-system skill/scripts。

实验 2：PPTX editability test。使用 Baoyu 自带 `gen-pptx` CLI，以 editable mode 导出本地 HTML deck。之后解压 PPTX 检查 `ppt/slides/slide*.xml`，统计 `p:txBody`、`p:sp`、`p:pic`、`a:t`。

实验 3：AI image insertion。用内置 image generation 生成 “A futuristic server room icon” PNG，并以 `<img>` 插入第 3 页，验证导出 PPTX 中图片成为原生 `p:pic` 对象，周围文字仍保持 native text。

## 5. 部署与执行证据 (Setup & Execution Evidence)

环境：

- macOS 26.5.1
- Node.js v26.0.0
- npm/npx 11.12.1
- Python 3.14.5
- LibreOffice `soffice`

关键命令：

```bash
git clone --depth 1 https://github.com/JimLiu/baoyu-design /tmp/baoyu-design-local
cd /tmp/baoyu-design-local/skills/baoyu-design/agents/gen-pptx
npm install
npm run build
npm test
npx playwright install chromium
```

结果：`npm run build` 成功，`node --test` 共 26 个测试通过。Playwright 成功安装 `chromium-1228`；此前本机缓存的 `chromium-1223` 与 Playwright 1.49 不匹配。

真实导出结果：

```json
{
  "ok": true,
  "slides": 3,
  "bytes": 2478623,
  "flags": [],
  "warnings": []
}
```

## 6. 实证发现 (Findings)

### 6.1 已验证的功能 (可编辑性、图文排版)

- PPTX 真实生成成功：`artifacts/baoyu-design-imagegen-editable.pptx`。
- LibreOffice 可解析并导出 PDF：`screenshots/baoyu-design-imagegen-editable.pdf`。
- OOXML 结构验证：
  - Slide 1: `p:txBody=5`, `p:sp=6`, `p:pic=1`, `a:t=6`
  - Slide 2: `p:txBody=16`, `p:sp=27`, `p:pic=0`, `a:t=16`
  - Slide 3: `p:txBody=5`, `p:sp=7`, `p:pic=1`, `a:t=7`
- Speaker notes 写入成功：3 个 `ppt/notesSlides/notesSlide*.xml`。

### 6.2 失败或受限的边界

- 未做真实 PowerPoint/Keynote GUI 双击编辑测试。
- 未做 20 页复杂 deck 压力测试。
- 未测试多宽高比图片的 cover/contain 裁切边界。
- npm audit 报 1 个 moderate vulnerability，本研究未强制升级依赖，以避免改变实测代码路径。

### 6.3 未验证的宣称

- 未验证真实 Image Generation API 调用、提示词生成、鉴权、成本与失败重试。
- 未验证自然语言 prompt 端到端稳定生成完整 Design System 的质量。
- 未验证 Office Web、本地 PowerPoint、Keynote、LibreOffice 之间的所有可编辑性差异。

## 7. 评估矩阵 (Evaluation Matrix)

| Dimension | Score | Evidence |
|---|---:|---|
| Installability | 4/5 | 安装、构建、测试均成功；需要匹配 Playwright Chromium。 |
| Design System Generation | 3/5 | 有完整 workflow/script 入口；未跑真实 LLM 自动生成。 |
| PPTX Editability | 5/5 | OOXML 存在 native `p:txBody`、`p:sp`、`p:pic`。 |
| Layout & Design Quality | 4/5 | 本地 deck 截图与 LibreOffice PDF 可读；复杂压力测试未做。 |
| Image Integration Robustness | 4/5 | 本地 image generation PNG 成功进入 PPTX picture object；目标项目自身 API 未测。 |
| Practical Value | 4/5 | Agent-to-editable-PPTX 架构可用，生产化仍需 QA。 |

## 8. 与传统方案对比

相比 Markdown 转 PPTX，Baoyu 的优势是能从真实 DOM/CSS layout 中提取位置、样式和媒体，适合更复杂的视觉设计。相比纯图片 PPTX，它保留了文本、形状和图片对象的可编辑性。相比手工拉版面，它更适合 Agent 批量生成 deck，但需要更严格的浏览器依赖、字体、图片、布局测试。

## 9. 行业与 AI Agent 落地场景建议

- 销售方案 deck、技术方案 deck、研究报告 deck：适合 Trial。
- 品牌级外发材料：可作为初稿生成与排版加速，不建议免审发布。
- Agent workflow：适合作为 HTML/CSS-first deck authoring 到 editable PPTX 的参考架构。
- 安全与合规：真实 Image Generation 应增加 record/replay mock、素材来源记录、prompt/output 审计。

## 10. 局限性与潜在风险分析

- 浏览器版本与 Playwright 版本强绑定，CI/CD 需要缓存策略。
- 字体加载失败会导致换行与版式偏移。
- DOM/CSS 到 PPTX object 的映射不可能覆盖全部 CSS 语义。
- 外部图片、跨域资源和 SVG 安全策略需要生产级约束。
- 真实图像生成成本、延迟、失败重试尚未纳入实测。

## 11. 最终行动建议 (Adopt / Trial / Reference Only / Avoid)

建议：**Trial / Reference Only**。

理由：本地已经复现核心 editable PPTX 导出能力，技术路线可信；但 Design System 生成与真实 AI image generation 仍依赖 agent/runtime，生产采用前需要更完整 QA。

## 12. 完整复现指南 (Reproduction Guide)

```bash
git clone --depth 1 https://github.com/JimLiu/baoyu-design /tmp/baoyu-design-local
cd /tmp/baoyu-design-local/skills/baoyu-design/agents/gen-pptx
npm install
npm run build
npm test
npx playwright install chromium

cd /Users/martin/Library/CloudStorage/GoogleDrive-martin.lanse2000@gmail.com/我的云端硬盘/workspace_sync/assets/Work-PKM-Vault/baoyu-design-pptx-empirical-study/artifacts/local_deck
python3 -m http.server 8787 --bind 127.0.0.1

cd /tmp/baoyu-design-local/skills/baoyu-design/agents/gen-pptx
node dist/cli.mjs \
  --url http://127.0.0.1:8787/index.html \
  --config /Users/martin/Library/CloudStorage/GoogleDrive-martin.lanse2000@gmail.com/我的云端硬盘/workspace_sync/assets/Work-PKM-Vault/baoyu-design-pptx-empirical-study/artifacts/local_deck/config-editable.json \
  --out /Users/martin/Library/CloudStorage/GoogleDrive-martin.lanse2000@gmail.com/我的云端硬盘/workspace_sync/assets/Work-PKM-Vault/baoyu-design-pptx-empirical-study/artifacts
```

## 13. 生成产物清单 (Artifacts Link)

- `artifacts/baoyu-design-imagegen-editable.pptx`
- `artifacts/imagegen_pptx_ooxml_inspection.json`
- `artifacts/local_deck/index.html`
- `artifacts/local_deck/config-editable.json`
- `artifacts/local_deck/imagegen-server-room.png`
- `screenshots/local_deck_slide_1.png`
- `screenshots/local_deck_slide_2.png`
- `screenshots/local_deck_slide_3.png`
- `screenshots/baoyu-design-imagegen-editable.pdf`
