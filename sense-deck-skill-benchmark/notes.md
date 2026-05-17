# 研究笔记

## 原始研究问题
- 对 GitHub 项目 `xwbcl123/-PPT-sense-deck-skill-` 进行深度调研，测试其在 HTML 幻灯片生成场景下表现，并与归藏 PPT Skill（Marp）与花叔 PPTX Skill（python-pptx）横向对比。

## 工作日志

- 创建研究目录：`mkdir -p sense-deck-skill-benchmark`
- 初始搜索（失败路径）：`web.search_query("xwbcl123 -PPT-sense-deck-skill- GitHub")` 返回大量无关技能索引站，命中率低，放弃该路径。
- 仓库可达性验证：`git ls-remote https://github.com/xwbcl123/-PPT-sense-deck-skill-.git`，成功返回 main/HEAD。
- 拉取外部仓库到临时目录：`git clone --depth 1 ... /tmp/.../repo`。
- 读取关键说明：`sed -n '1,220p' SKILL.md`，确认该项目是“Template-First + Content IR + static HTML/CSS/JS”路线。
- 实验产物：
  - `index.html`：基于场景A生成可本地直接运行的静态 HTML 幻灯片。
  - `README.md`：整理三场景提纲、Rubrics 与横评矩阵。

## 验证证据
- `python -m py_compile` 不适用（本次无 Python 可执行产物作为主工件）。
- `python - <<'PY' ...` 使用 `html.parser` 成功解析 `index.html`（无语法异常）。
