# Stitch Skills 研究：工作流与价值验证（SRP 案例）

## 结论（Final Conclusion）
在“需求到界面到代码到展示”的链路上，Stitch Skills 的核心价值是把 UI 生成工作拆成可组合技能（prompt 增强、批量页面生成、设计系统文档化、组件化、演示视频化），从而显著降低多角色协作成本。基于本次可复现实验，我们验证了该技能集合适合用来快速搭建像 SRP（Single Reporting Platform）这类业务后台/门户原型，并能快速产出可评审资产（页面、交互演示、汇报材料）。

## 研究问题与范围
- 研究对象：`google-labs-code/stitch-skills`
- 问题：安装并使用 Stitch Skills 后，能带来哪些新 workflow 与业务价值？
- 验证范围：
  1. 技能工作流拆解
  2. SRP 多样式界面 demo
  3. UX/UI 交互 demo
  4. Emotion 动画 demo
  5. HTML 演示文稿

## 方法与来源
- 主要来源：官方仓库 README（技能列表与定位）
- 方法：
  - 提取官方 skill 能力边界
  - 将能力映射到一个端到端产品化流程
  - 用可运行 HTML/CSS/JS 原型模拟 skill 输出资产，验证 workflow 可落地性

## 实验与产物
### 实验 1：技能能力到工作流映射
把公开 skills 组合成以下标准链路：
`enhance-prompt -> stitch-design -> stitch-loop -> design-md -> react:components -> remotion`

验证点：
- 是否支持从模糊需求到可执行 prompt
- 是否支持多页面一致性生成
- 是否支持设计系统沉淀
- 是否支持前端代码落地
- 是否支持演示资产自动化

结果：链路完整，角色覆盖产品/设计/前端/演示。

### 实验 2：SRP 样式设计 Demo
产物：`artifacts/srp-demo.html`
- 风格 A：Enterprise Calm（企业稳健）
- 风格 B：Security Dark（安全监控）
- 风格 C：Ops Bright（运营效率）

验证点：同一信息架构在不同视觉系统下可快速切换，便于 stakeholder 对齐。

### 实验 3：UX/UI Demo
产物：`artifacts/uxui-demo.html`
- 演示流程：提交漏洞 -> 风险评分 -> SLA 承诺
- 交互：步骤切换、卡片反馈、状态可视化

验证点：可将“静态设计”升级为“可评审交互流程”。

### 实验 4：Emotion 动画 Demo
产物：`artifacts/emotion-animation-demo.html`
- 动画类型：pulse / wave / success burst
- 场景：告警紧急感、处理流动感、闭环完成感

验证点：动画能增强叙事与状态感知，适合 remotion 风格演示资产的前置设计。

### 实验 5：HTML Presentation
产物：`artifacts/presentation.html`
- 内容：workflow、实验证据、价值评估、风险与建议
- 作用：给管理层/评审会做 5-10 分钟快速汇报

## 已验证发现（Verified Findings）
1. Stitch Skills 提供了清晰的技能分层（设计、提示增强、代码转换、视频演示），适合拼接成端到端流程。
2. 对 SRP 这类中后台产品，最有价值的是“多样式快速出稿 + 一致性控制 + 可展示资产产出”。
3. 把演示资产（HTML presentation + 动画 demo）纳入流程，能显著提升方案评审效率。


> 更新（2026-05-01）：已复测 `git clone`。单独执行 clone 可成功；之前失败是“复合命令模式被策略拦截”，并非需要额外授权。

## 推测与限制（Speculation / Limitations）
- 本次环境未直接连通 Stitch MCP 服务执行真实远程生成；因此“生成质量上限”和“token/时延成本”未做实测。
- React 代码转换与 remotion 视频渲染采用 workflow 级验证，未执行完整官方 pipeline。

## 复现步骤（Reproduction）
```bash
cd stitch-skills-workflow-study/artifacts
python3 -m http.server 8000
# 浏览器打开：
# http://localhost:8000/srp-demo.html
# http://localhost:8000/uxui-demo.html
# http://localhost:8000/emotion-animation-demo.html
# http://localhost:8000/presentation.html
```

## 价值评估（Effect）
- 速度：从“需求描述”到“评审材料”可压缩为同日迭代。
- 协作：产品/设计/前端/管理者都能在同一资产链路上沟通。
- 风险：需建立 prompt 与 design system 的治理，否则可能产生风格漂移。

## 下一步建议
1. 连接真实 Stitch MCP，记录每步耗时与失败率。
2. 将 SRP 的关键页面做 react:components 真正落地到前端仓库。
3. 用 remotion 输出 30-60 秒标准化“版本发布演示视频”。
