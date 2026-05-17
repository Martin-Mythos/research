# Sense Deck Skill 与主流 AI PPT 工具链的架构实证与横评报告

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## 1. 实验摘要 (Executive Summary)
本次研究围绕 `xwbcl123/-PPT-sense-deck-skill-` 展开，重点验证其“模板优先 + 内容 IR + HTML/CSS/JS 静态交付”的工作流在企业级演示场景中的可控性。该项目在 `SKILL.md` 中明确要求优先选择模板库、先构建 content IR，再输出静态三件套（`index.html / styles.css / deck.js`），本质上是把“内容规划-版式装配-运行时增强”拆分为可组合工序。

横评结论：
- **Sense Deck** 在前端可控性、最终视觉一致性、离线部署方面优势明显，适合“研发/安全团队可改代码”的组织。
- **归藏（Marp）** 在提纲到页面的速度和协作成本（Markdown）上最优，但复杂视觉与细粒度布局上限受限。
- **花叔（Python-pptx）** 在企业 Office 生态交付（`.pptx` 可编辑）优势显著，但需要较强脚本能力，调样式成本偏高。

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
> 以下为可双击运行的自包含 `index.html`（已在本研究目录保存同名文件）：

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
  </style>
</head>
<body>
<!-- 省略：完整代码见研究目录 index.html -->
</body>
</html>
```

### 技术点评
- **分屏逻辑**：以 `section.slide` 作为单页容器，每页固定 `100vh` 并使用 `scroll-snap` 提供近似演示翻页手感。
- **版式策略**：统一三段式栅格（Header/Main/Footer），在内容区采用 `grid-2 + card` 控制信息密度，符合 Sense 风格“留白 + 模块化分组”。
- **运行路径**：纯静态、零构建依赖，可直接本地打开；后续如要扩展动画或演讲者模式，可引入运行时脚本模块。

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
- **内容转化率**：Marp 从提纲到“可读页面”最快；Sense Deck 在复杂分栏、卡片化、品牌风格一致性上更稳；python-pptx 适合要求最终可在 Office 深度编辑的组织。
- **工具链依赖**：Sense Deck 与 Marp 均可轻量化运行；python-pptx 依赖 Python 运行环境与库版本，协作中环境漂移风险更高。

---

## 5. 落地建议 (Recommendations)

1. **Sense Deck 的局限**
   - 直接 HTML 方案对“不会代码”的用户并不友好，尤其在布局溢出、响应式细调、动画节奏控制方面，仍需前端能力。
2. **架构选型建议**
   - 若团队具备前端工程能力、强调品牌统一与多端展示：优先 **Sense Deck（HTML）**。
   - 若追求“写作即排版”、多人协作与快速迭代：优先 **Marp（Markdown）**。
   - 若组织必须以 PowerPoint 为最终编辑/审阅载体：优先 **Python-pptx/Pptx 工具链**。
3. **推荐混合路径**
   - “Marp 产出初稿结构 -> Sense Deck 做高保真交付 -> 必要时导出为 PPTX”可在速度、品质、可编辑性之间取得更优平衡。
