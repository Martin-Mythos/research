# 研究笔记

## 原始问题
- 用户要求：解析 tw93/kami 设计系统，并产出两个单文件 HTML（极简主页、AI 趋势 Web-PPT），全部中文输出。

## 执行记录
- 创建工作目录：`mkdir -p kami-design-experiments`
- 克隆源码：`git clone --depth=1 https://github.com/tw93/kami.git _kami_src`
- 代码检索：`rg -n -e "--parchment" -e "--near-black" -e "--brand" -e "--serif" -e "line-height" -e "letter-spacing" ...`
- AI 趋势检索：使用联网搜索（OpenAI/Google/NVIDIA 官方页面）。

## 数据源与 URL
- https://github.com/tw93/kami
- https://openai.com/index/new-tools-for-building-agents/
- https://openai.com/index/new-tools-and-features-in-the-responses-api/
- https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/
- https://blog.google/products/gemini/gemini-2-5-model-family-expands
- https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Blackwell-Ultra-AI-Factory-Platform-Paves-Way-for-Age-of-AI-Reasoning/default.aspx

## 实验与结果
- 实验一：提取 Kami 色板/字体/行高/字距变量，确认其核心是纸感底色 + 深色正文 + 品牌蓝点缀。
- 实验二：完成 `index.html`，以大留白、左侧品牌线、低噪声链接列表复刻极简主页。
- 实验三：完成 `presentation.html`，采用 scroll-snap 全屏分页与高层级排版，输出 9 页 AI 趋势。

## 失败路径
- 首次 `rg` 命令将正则误写成参数，触发 `unrecognized flag`，随后改为多个 `-e` 解决。
- 在 Kami 仓库中未发现统一 `prefers-color-scheme: dark` 全局规则，故报告中标注“暗黑模式偏向手工主题扩展”。

## 验证证据
- `python -m py_compile` 不适用（无 Python 脚本）。
- `node` 预览不作为必须条件；HTML 为静态自包含文件，可直接浏览器打开。
