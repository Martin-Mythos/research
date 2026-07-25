# 仓库侦察

## 取证边界

- 2026-07-25 以 shallow clone 检出 `html-anything` 的 `1896831a…` 与 `bento` 的 `17121c2…`；上游副本仅在 `/tmp/ha-study-upstreams`，未纳入提交。
- 文档声明与本地验证严格分开。以下“声明”来自上游 README/架构文档；“验证”来自源码、构建和产物检查。

## HTML-Anything

### 文档声明

README 将其定位为 agent skill/CLI：解析文件或目录，根据 source prompt、style prompt 和样本调用 LLM，输出经过检查的单文件 HTML。其 CLI 要求 `ANTHROPIC_API_KEY` 或 `OPENAI_API_KEY`。

### 源码与沙箱验证

- `src/cli.ts` 完成 parser 选择、样本解析、LLM 调用和写文件；无 key 时明确退出。
- `src/htmlize.ts` 把基础指令、设计系统、style catalog、style prompt、source prompt、schema/stats 和最多 16,000 字符的代表样本拼成一个 user prompt。其所谓 style gate 是发给模型的自检指令，不是浏览器级确定性 validator。
- 输出预期为标准语义 HTML，CSS/JS 通常内联；个别 style 可复制相对 assets，因此“天然始终单文件”不能由源码普遍保证。
- `npm ci`、TypeScript build 和 81 项上游测试通过；Node 20 对 `pdfjs-dist` 发出 engine warning。

## Bento

### 文档声明

README 将 Bento Slides 定位为“装在一个 HTML 文件里的 office suite / PowerPoint alternative”：viewer、presenter、editor 与文档共存。架构文档称内容位于明文 `#bento-doc` JSON，固定 runtime 被 DEFLATE 压缩并内联。

### 源码与沙箱验证

- `slides/index.html` 提供 `application/bento+json` 数据块和 runtime mount；`src/model.ts` 定义绝对坐标元素模型。
- `npm run build:single` 通过，生成 603,169 字节空 shell（构建日志报告压缩前约 1,185 KB、压缩后约 587 KB）。
- 本研究将三场景 JSON 注入 shell；每个文件约 603.7 KB、包含 3 页，可被正则抽取和 JSON 解析。
- Bento 内容不是传统手写 DOM：可编辑内容主要是 JSON 中的 slide/element 对象；运行时再渲染。这利于几何化编辑和演示状态，却不利于直接改 `<article>`、heading 等语义 DOM。

## 结构差异结论

| 维度 | HTML-Anything | Bento |
|---|---|---|
| 核心抽象 | LLM 生成的自由 HTML 页面 | 固定 editor/runtime + `#bento-doc` JSON |
| DOM | 生成时直接决定，适合语义元素 | 运行时 mount，内容以绝对坐标 element model 保存 |
| CSS/JS | 提示要求内联，但 style asset 路径可能外置 | build:single 把 runtime CSS/JS 压进一个文件 |
| 组件 | style prompt/class vocabulary，约束是软性的 | text/shape/image/svg/chart/table/media 等强 schema |
| 演示状态 | 需由生成 HTML 自行实现 | 原生 slide、transition、stateOf、hover、present 配置 |
| 二次编辑 | 文本编辑器直接编辑 DOM/CSS | GUI 编辑或修改 JSON；手改 runtime DOM 不持久 |
