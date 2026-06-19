# No Mistakes validation fallback

真实 `no-mistakes` gate 需要初始化 git remote/proxy、可用 PR 远程、agent/LLM CLI 或 TUI 流程。本沙箱没有 `gh`，也没有配置真实 GitHub auth/LLM API key，因此未执行真实 `git push no-mistakes`。

替代验证：
- 对 Talking Breads V1 运行 `npm run build`, `npm test`, `npm run smoke`。
- 运行 `scripts/validate_talking_breads.py` 检查 PRD 关键内容和 forbidden online-ordering/payment affordance。
- 结果见 `talking-breads-*.log` 与 `manual-validation.log`。

结论：No Mistakes 的完整价值在远程 PR/CI/LLM validation 闭环，离线静态测试只能验证本地可构建性与 README/CLI 可发现性，不能验证 AI code review 质量。
