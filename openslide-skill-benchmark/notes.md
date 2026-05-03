# 研究笔记

## 原始研究问题
对 GitHub 开源项目 1weiho/open-slide 进行深度调研，并与中文社区主流 AI PPT 技能（归藏 PPT Skill、花叔 PPTX Skill）进行横向实证对比，输出中文结构化报告与可复现实验 artifacts。

## 工作记录

- 命令: git clone 三个仓库（open-slide/guizang-ppt-skill/huashu-skills）
- 目的: 获取一手 README/SKILL 规则用于实证基线。
- 命令: python3 artifact-huashu-pptx.py
- 结果: 失败，缺少 python-pptx 依赖（ModuleNotFoundError）。
- 处理: pip install python-pptx 后重试成功并产出 artifact-huashu-output.pptx。
- 数据源/URL:
  - https://github.com/1weiho/open-slide
  - https://open-slide.dev/
  - https://github.com/op7418/guizang-ppt-skill
  - https://github.com/alchaincyf/huashu-skills
- 关键读取文件:
  - external/open-slide/README.md
  - external/guizang-ppt-skill/README.md
  - external/guizang-ppt-skill/SKILL.md
  - external/huashu-skills/huashu-slides/SKILL.md

- 清理: 删除 external/ 克隆仓库，仅保留研究产物，避免提交第三方仓库副本。
- 变更: 按评审意见将 PPTX 二进制改为 ZIP 打包提交（artifact-huashu-output-pptx.zip）。
- 变更: 按最新评审意见删除 `artifact-huashu-output-pptx.zip`，仓库仅保留脚本；PPTX 改为本地执行脚本生成验证。
