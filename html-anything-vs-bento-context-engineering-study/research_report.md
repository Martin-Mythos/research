# Opus 5 / GPT-5.6-Sol 驱动下 HTML-Anything 与 Bento 多场景生成、Context Engineering 及 R2 工作流对比评估

## 1. 执行摘要

本研究固定并构建两个上游仓库，完成 Dashboard、Long-form、PPT 三场景 × 两载体的六个离线 artifact，随后用脚本检查硬约束、自包含、DOM 指标和 Bento 数据块。**已验证的产品结论**是：HTML-Anything 更像“解析 + prompt pack + LLM 生成自由 HTML”的流水线，语义 DOM 和长文/仪表盘适配更强；Bento 是“固定单文件编辑 runtime + JSON 文档”的演示系统，slide state、可视化编辑和单文件运输更强。它们并非完全同类替代品。

**模型结论必须保守**：沙箱没有 Opus 5 或 GPT-5.6-Sol API key，也没有可确认的 Opus 5 endpoint；因此没有执行真实模型 A/B、重复采样、token/latency 计量。六个产物是确定性本地 mock fixtures，能验证工作流和约束 validator，不能证明任一模型的生成质量。最佳 Context Engineering 建议是把 canonical facts、style contract、output contract 分离，并以外部 validator 闭环，而非依赖模型自述的 Chain-of-Thought。

## 2. 项目与对比工具概述

HTML-Anything 的 CLI 先识别输入 parser、构建代表样本，再组合设计系统、source/style prompts 和数据，调用 Anthropic 或 OpenAI。输出 DOM 自由度大，但合规依赖模型遵循 prompt。Bento Slides 则将编辑器、viewer 和 presenter 编译进单个 HTML；业务内容保存在 `#bento-doc` JSON，元素采用绝对坐标和强 schema。

## 3. 研究问题与核心假设

研究问题是：两工具在三类 HTML 输出、二次编辑和 R2 对象化部署上各自优势为何，以及怎样用 context/prompt contract 降低题设反直觉约束被“常识纠正”的风险。假设包括语义 DOM 优势、Bento presentation schema 优势，以及外部校验优于 silent self-check；前三者均获得结构证据支持，但模型层假设未做真实 A/B。

## 4. Opus 5 / GPT-5.6-Sol 与 Context Engineering

### 4.1 已验证

题设的硬事实在两类 dashboard fixture 中均出现；validator 要求同时存在“波兰、红色、绿色、塞浦路斯”，并通过。该检查验证的是 deterministic fixture → artifact → validator 链路。

### 4.2 未验证

未调用 Opus 5 或 GPT-5.6-Sol，故不报告 instruction adherence rate、token 数、延迟、视觉偏好或模型排名。当前 Codex 会话本身也不是一个可控制 temperature、重复采样并隔离上下文的公平 benchmark harness。

### 4.3 推荐策略

1. System 层只定义角色、安全边界和不可协商输出格式。
2. User 层以 `<canonical_facts>` 单列事实，明确“红/绿映射覆盖常见交通灯语义”。
3. `<content>` 与 `<style_contract>` 分离，防止视觉要求稀释事实权重。
4. 要求短的 evidence checklist，不索取私有 Chain-of-Thought。
5. 生成后执行 parser/DOM/assertion validator；失败时只回传差异和原约束，做 bounded repair。
6. 真正模型 benchmark 至少每个模型×策略×场景运行 5 次，固定模型版本、temperature、max tokens，并记录输入/输出 token、延迟和 validator pass rate。

## 5. 实验设计与执行证据

上游被 shallow clone 到 `/tmp`，避免把完整仓库提交进研究库。HTML-Anything 的 `npm ci`、`npm run build`、`npm test` 通过（81/81）；安装对 Node 20 与 `pdfjs-dist` 的 engine 范围发出 warning。Bento 的 `npm ci` 与 `npm run build:single` 通过，产出约 587 KB 的压缩 shell。`generate_benchmark.py` 将三份强约束内容生成语义 HTML，同时将三页 JSON 注入该真实 Bento shell。命令、原始关键输出和 SHA 均见 `run_log.md`、`setup_log.md` 与 `notes.md`。

## 6. 全场景遍历结果

- **Dashboard**：两者都承载题设映射。HTML-Anything fixture 的 grid、heading、list 可直接编辑；Bento 可以做可视 slide dashboard，但绝对坐标和分页更合适。
- **Long-form**：语义 HTML 可自然滚动、响应式重排；Bento 需要把文字切页，因此阅读连续性较弱。
- **PPT**：Bento 有原生 slide、transition、present controls、editor 和 state model；自由 HTML 需要自行实现同等机制。因此 Bento 在该场景明显领先。

## 7. 评估矩阵与 DOM 深度

完整分数见 `evaluation_matrix.md`。静态 HTML parser 统计存入 `artifacts/metrics.json`。必须注意：Bento runtime 被压缩并在浏览器运行时挂载 DOM，静态深度不能与已展开的语义 HTML 深度直接比较。更关键的编辑面区别是“DOM/CSS 是 source of truth”与“JSON document model 是 source of truth”。

## 8. Cloudflare R2 发布工作流

`publish_r2_mock.sh <artifacts> <staging>` 先调用 validator，再复制所有 HTML 并写 `manifest.sha256`。生产环境建议在其后执行：设置正确 `Content-Type: text/html; charset=utf-8`、长缓存与 immutable versioned key、上传 SHA metadata、用自定义域/CDN 提供 CSP，并对公开 artifact 清理敏感数据。本研究不持有 Cloudflare 凭据，没有实际 `wrangler r2 object put`，所以只声称 mock staging 成功。

## 9. 局限性、风险与最佳提示词

- 没有真实双模型调用、视觉 screenshot 或浏览器交互自动化。
- 三场景内容是小型合成 fixture，不代表专业法律事实完整性；“塞浦路斯”仅按题设约束处理。
- HTML-Anything fixture 不是其 CLI 的真实 LLM 输出；Bento 则确实使用本地构建 shell，但内容 JSON 由研究脚本生成。
- R2 没有真实网络上传、ACL、CORS、自定义域或缓存验证。
- 上游固定在单一时间点，后续架构可能变化。

最佳提示骨架：`目标 → canonical facts → source content → framework-specific schema/style → output contract → machine assertions`。事实重复一次即可；与其反复强调，不如把约束转换为可执行 assertions。

## 10. 复现指南与产物清单

```bash
# 上游构建（需先按 notes.md 固定版本 clone 到 /tmp）
(cd /tmp/ha-study-upstreams/html-anything && npm ci && npm run build && npm test)
(cd /tmp/ha-study-upstreams/bento/slides && npm ci && npm run build:single)
python3 scripts/generate_benchmark.py --project . \
  --bento-shell /tmp/ha-study-upstreams/bento/slides/dist-single/Bento_Slides.bento.html
python3 scripts/validate_artifacts.py .
scripts/publish_r2_mock.sh artifacts /tmp/r2-staging
```

关键产物：六个场景 HTML 位于 `artifacts/html_anything/` 与 `artifacts/bento/`；交互报告为 `artifacts/research_report_artifact.html`；指标为 `artifacts/metrics.json`；脚本位于 `scripts/`。详细侦察、计划、评分、日志分别见 `notes/repo_recon.md`、`experiment_plan.md`、`evaluation_matrix.md`、`run_log.md`。

## 结论层级

- **验证事实**：两仓库在固定 commit 可安装/构建；HTML-Anything 81 tests 通过；Bento single shell 构建通过；六产物通过本地自包含与约束检查。
- **文档声明**：工具定位和若干设计目标来自各自 README/architecture，不能自动等同于全部生产保证。
- **推断**：HTML-Anything 更适合语义页面、Bento 更适合演示，是由架构与小型 fixtures 支持的工程推断。
- **未验证**：Opus 5 对 GPT-5.6-Sol 的任何胜负、真实 R2 发布及专业监管内容正确性。
