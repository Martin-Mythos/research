# 研究记录

## 原始问题
- 用户要求对 GitHub 项目 `xwbcl123/-PPT-sense-deck-skill-` 做深度调研，并与归藏/花叔两类中文社区主流 AI PPT 技能做横向实证比较，输出中文结构化报告与 HTML Artifact。

## 环境信息
- 日期：2026-05-05 (UTC)
- 工作目录：/workspace/research

## 实际执行命令与数据来源
1. `git clone --depth 1 https://github.com/xwbcl123/-PPT-sense-deck-skill-.git /tmp/ppt-sense-deck-skill`
   - 目的：拉取主标的代码。
   - 结果：成功。
2. `sed -n '1,220p' /tmp/ppt-sense-deck-skill/README.md`
   - 目的：确认仓库定位与目录组成。
   - 结果：确认项目为模板化 HTML 演示工作流。
3. `sed -n '1,260p' /tmp/ppt-sense-deck-skill/SKILL.md`
   - 目的：提取其核心 Prompt/流程方法论。
   - 结果：确认 template-first + content-IR + full-deck/layout/animation catalog 架构。

## 实验与结果
- 实验 A：针对“企业级 AI 安全逃逸边界”生成 8 页 HTML 单文件 deck。
  - 结果：完成 `index.html`，可本地浏览器直接打开，支持键盘与点击翻页。
- 实验 B：构建横评 Rubrics，并模拟 Marp 与 Python-pptx 对照方案。
  - 结果：完成评分矩阵与技术边界分析。

## 失败路径与放弃原因
- 失败路径：尝试直接在主标的仓库找到“归藏/花叔”官方同仓模板进行一键公平复现。
  - 放弃原因：主标的仓库仅包含鲸格体系模板，不包含归藏/花叔官方实现；改为“同提纲、同评价维度”的方法学模拟对照。

## 验证证据
- `python -m py_compile` 不适用（本实验无 Python 工程文件作为执行目标）。
- `python -m http.server` 可用于人工浏览验证（未长驻运行）。
- `wc -l sense-deck-html-benchmark/index.html sense-deck-html-benchmark/README.md sense-deck-html-benchmark/notes.md`
