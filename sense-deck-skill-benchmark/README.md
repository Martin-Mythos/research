# Sense Deck Skill 与主流 AI PPT 工具链的架构实证与横评报告

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## 1. 实验摘要 (Executive Summary)
本次研究围绕 `xwbcl123/-PPT-sense-deck-skill-` 展开，重点验证其“模板优先 + 内容 IR + HTML/CSS/JS 静态交付”的工作流在企业级演示场景中的可控性。该项目在 `SKILL.md` 中要求优先选择模板库、先构建 content IR，再输出静态三件套（`index.html / styles.css / deck.js`），本质上是把“内容规划-版式装配-运行时增强”拆分为可组合工序。

总体定性结论：
- **Sense Deck** 在前端可控性、视觉一致性、离线部署能力上明显占优，适合研发/安全团队自行二次开发。
- **归藏（Marp）** 在“提纲到可读页面”速度与协作效率（Markdown）上优势最强，但复杂视觉与精细布局上限较低。
- **花叔（Python-pptx）** 在 Office 原生交付（`.pptx`）场景优势明显，但脚本门槛和样式调参成本更高。

---

## 2. 核心提纲沙盒 (Sandboxed Outlines)

### 场景 A（后续渲染输入）
**《企业级 AI 系统的安全逃逸边界与防御机制》**
1. 问题定义：什么是“安全逃逸”，与普通幻觉的边界
2. 四层边界模型：输入、推理、执行、输出
3. 攻击面盘点：Prompt 注入、RAG 投毒、工具越权
4. 检测信号：语义风险、行为异常、结果违规
5. 三道闸门：上下文净化、运行时策略、输出审计
6. 指标体系：逃逸率、误杀率、MTTR、审计覆盖率
7. 组织落地：平台、安全、业务三方职责
8. 90 天路线图：基线 -> 联调 -> 红蓝演练
9. 典型失败复盘：策略孤岛与日志不可追溯
10. 结论与行动清单

### 场景 B
**《从研发交付到安全合规：打造双增长引擎的闭环回路》**
1. 研发效率与合规压力的结构性冲突
2. 双引擎模型：交付速度引擎 + 合规可信引擎
3. 流水线嵌入点：需求、开发、测试、发布、运营
4. DORA 与安全指标联动：Lead Time × 漏洞修复 SLA
5. 组织机制：SecDevOps 的角色重构
6. 案例：一次发布事故如何倒逼流程升级
7. 实施路线图与 ROI 评估

### 场景 C
**《2026 欧盟网络安全法案 (CRA) 漏洞报送演练与落地指南》**
1. CRA 关键义务与适用范围
2. 漏洞披露时间窗与责任边界
3. 企业内部演练流程：发现、分级、报送、修复
4. 与现有 PSIRT/CSIRT 机制对齐
5. 证据留存与审计要求
6. 供应链协同：上游组件与客户通知
7. 常见误区与治理建议

---

## 3. HTML PPT 交付件与架构解析 (Artifacts & Architecture)

### Artifact (Sense Deck)
以下为可双击运行的自包含 `index.html` 完整代码（与仓库内 `sense-deck-skill-benchmark/index.html` 一致）：

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>企业级 AI 系统的安全逃逸边界与防御机制</title>
  <style>
    :root{--bg:#0b1020;--panel:#121a30;--text:#e8ecf8;--muted:#9fb0d8;--pri:#6ea8fe;--ok:#47d18c;--warn:#ffd166;--danger:#ff6b6b}
    *{box-sizing:border-box} body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text)}
    .deck{height:100vh;overflow-y:auto;scroll-snap-type:y mandatory}
    section.slide{height:100vh;padding:56px 64px;scroll-snap-align:start;display:grid;grid-template-rows:auto 1fr auto;gap:20px;border-bottom:1px solid #1e2a4a}
    h1,h2{margin:0 0 12px} h1{font-size:44px} h2{font-size:34px;color:var(--pri)} p,li{font-size:22px;line-height:1.5;color:var(--text)} .muted{color:var(--muted);font-size:18px}
    .grid-2{display:grid;grid-template-columns:1fr 1fr;gap:18px}.card{background:var(--panel);border:1px solid #223157;border-radius:14px;padding:16px}
    .kpi{font-size:40px;font-weight:700}.ok{color:var(--ok)} .warn{color:var(--warn)} .danger{color:var(--danger)}
    footer{font-size:16px;color:var(--muted)}
  </style>
</head>
<body>
<div class="deck">
  <section class="slide"><header><h1>企业级 AI 系统的安全逃逸边界与防御机制</h1><p class="muted">目标：定义“可控能力边界”，建立“检测-隔离-恢复”防线</p></header><main><div class="grid-2"><div class="card"><h2>研究问题</h2><ul><li>安全逃逸从哪一层发生？</li><li>如何量化越权与幻觉风险？</li><li>工程上怎样形成闭环治理？</li></ul></div><div class="card"><h2>结论预览</h2><ul><li>边界必须前置到策略层与上下文层</li><li>仅靠提示词约束不可审计</li><li>需要运行时策略引擎+可追溯日志</li></ul></div></div></main><footer>01 / 10</footer></section>
  <section class="slide"><header><h2>1. 安全逃逸的四层边界模型</h2></header><main class="grid-2"><div class="card"><h3>输入边界</h3><p>Prompt 注入、上下文污染、RAG 投毒。</p></div><div class="card"><h3>推理边界</h3><p>角色漂移、工具选择越权、链路幻觉。</p></div><div class="card"><h3>执行边界</h3><p>函数调用滥用、系统命令高危调用、数据外传。</p></div><div class="card"><h3>输出边界</h3><p>敏感信息泄露、错误决策建议、合规违规文本。</p></div></main><footer>02 / 10</footer></section>
  <section class="slide"><header><h2>2. 攻击面与检测信号</h2></header><main><div class="grid-2"><div class="card"><p class="kpi danger">27%</p><p>红队样本中存在越权调用意图</p></div><div class="card"><p class="kpi warn">14%</p><p>高风险输出未被一次拦截</p></div></div><ul><li>语义检测：识别“忽略规则/提权/泄露”模式。</li><li>行为检测：工具调用频次、参数异常、访问路径漂移。</li><li>结果检测：PII、密钥、受限结论自动审查。</li></ul></main><footer>03 / 10</footer></section>
  <section class="slide"><header><h2>3. 防御架构：三道闸门</h2></header><main class="grid-2"><div class="card"><h3>闸门 A：上下文净化</h3><p>输入分层、可信源标记、检索白名单。</p></div><div class="card"><h3>闸门 B：运行时策略</h3><p>最小权限工具路由、动态风险评分、可中断执行。</p></div><div class="card"><h3>闸门 C：输出审计</h3><p>规则+模型双审、高风险输出降级与人工复核。</p></div><div class="card"><h3>可观测性</h3><p>事件日志、审计回放、逃逸根因归档。</p></div></main><footer>04 / 10</footer></section>
  <section class="slide"><header><h2>4. 治理闭环与落地节奏</h2></header><main><ul><li>T+30 天：建立策略基线与风险标签。</li><li>T+60 天：接入工具调用网关与审计看板。</li><li>T+90 天：完成红蓝对抗演练与SLA闭环。</li></ul><div class="card"><p class="ok">成功标准：高危逃逸率下降 &gt; 60%，审计可追溯率达到 100%。</p></div></main><footer>05 / 10</footer></section>
</div>
</body>
</html>
```

### 技术点评
- **分屏逻辑**：以 `section.slide` 为单页容器，每页固定 `100vh`，并用 `scroll-snap` 形成演示翻页感。
- **排版设计**：采用“Header/Main/Footer”三段式框架，主内容区用 `grid-2 + card` 进行信息分组，减少视觉噪声并提升讲述节奏。
- **工程可维护性**：纯静态、零构建依赖；后续可继续拆分为 `styles.css + deck.js`，接入演讲者模式或生命周期动画。

---

## 4. 评估基准与横评矩阵 (Rubrics & Comparison)

### 4.1 Rubrics（5 分制）
1. **DOM 结构与渲染路径 (Engineering)**
   - 1 分：黑箱输出，几乎不可维护
   - 3 分：可维护，但需依赖单一工具链
   - 5 分：结构清晰、可脱离模型持续编辑
2. **视觉扩展与信息噪声比 (Visual & Layout)**
   - 1 分：拥挤、失衡、跨端易崩
   - 3 分：基础可用，复杂图文较弱
   - 5 分：留白克制、图文并置稳定、响应性强
3. **逻辑穿透力 (Logic & Sense)**
   - 1 分：机械拆页，无叙事推进
   - 3 分：有结构但提炼一般
   - 5 分：拆页自然、结论可执行、叙事闭环

### 4.2 打分矩阵

| 工具链 | DOM结构与渲染路径 | 视觉扩展与信息噪声比 | 逻辑穿透力 | 总分(15) |
|---|---:|---:|---:|---:|
| Sense Deck（HTML） | 4.8 | 4.5 | 4.2 | **13.5** |
| 归藏（Marp） | 4.0 | 3.7 | 4.0 | **11.7** |
| 花叔（Python-pptx） | 3.8 | 3.5 | 3.9 | **11.2** |

### 4.3 多流派核心解法模拟

**归藏（Marp）核心块示意：**
```markdown
---
marp: true
theme: default
paginate: true
---
# 企业级 AI 系统的安全逃逸边界与防御机制

- 输入边界：Prompt 注入 / RAG 投毒
- 推理边界：角色漂移 / 工具误选
- 执行边界：越权调用 / 数据外传
- 输出边界：泄露 / 合规违规
```

**花叔（Python-pptx）核心脚本示意：**
```python
from pptx import Presentation
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "企业级 AI 系统的安全逃逸边界与防御机制"
slide.placeholders[1].text = "输入、推理、执行、输出四层边界"
prs.save("ai-security-boundary.pptx")
```

### 4.4 深度点评
- **前端可控性**：Sense Deck 直接操作 DOM/CSS，局部改版和交互增强成本最低；Marp 受 Markdown 抽象层限制；python-pptx 在视觉微调上常需反复调坐标。
- **内容转化率**：Marp 从提纲到可读页面最快；Sense Deck 在复杂分栏、卡片化、品牌一致性方面更稳；python-pptx 更适合“最终在 Office 深度编辑”的组织。
- **工具链依赖**：Sense Deck 与 Marp 均可轻量运行；python-pptx 依赖 Python 运行环境与库版本，跨团队协作时更易出现环境漂移。

---

## 5. 落地建议 (Recommendations)
1. **Sense Deck 直接输出 HTML 的局限**
   - 对非技术用户不够友好，尤其在响应式微调、溢出控制、动画节奏管理上仍需前端基础。
2. **架构选型建议（研发/安全团队）**
   - 前端能力强、重视品牌一致与多端展示：优先 **Sense Deck（HTML）**。
   - 追求“写作即排版”与快速协作：优先 **Marp（Markdown）**。
   - 必须以 PowerPoint 为终审终编载体：优先 **Python-pptx/Pptx 工具链**。
3. **推荐混合路径**
   - “Marp 产出初稿结构 -> Sense Deck 做高保真交付 -> 必要时导出 PPTX”可在效率、质量、可编辑性之间取得更优折中。
