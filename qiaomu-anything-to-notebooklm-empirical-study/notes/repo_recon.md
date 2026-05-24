# 仓库侦察记录

- 目标仓库：`joeseesun/qiaomu-anything-to-notebooklm`
- 定位：将多来源内容处理后上传至 NotebookLM，并通过提示词生成播客/PPT/思维导图等。
- 技术栈：Python（`main.py`、`check_env.py`、`scripts/`），依赖 `fastmcp`, `playwright`, `markitdown`。
- 入口：`main.py`（CLI 两参数：输入 + 指令）。
- 配置模型：Skill 文档强调在 Claude Skill 环境运行，依赖 `notebooklm` CLI 和 MCP server。
- 子模块：`feishu-read-mcp/` 存在；但 `check_env.py` 检查的是 `wexin-read-mcp`，与仓库实际目录不一致（潜在缺陷）。
- 测试状况：仓库仅见 `test.py`（feishu 子目录），未发现完善 CI workflow。
- 许可证：`LICENSE` 存在（MIT）。
- 主要风险：
  1) 强依赖外部 `notebooklm` 命令和登录态。
  2) 文档中含“付费墙绕过”等行为描述，需谨慎合规评估。
  3) 环境检查脚本的 MCP 路径可能过时。
