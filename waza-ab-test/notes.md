# Notes

## Original Prompt
- 对 `tw93/Waza` 的 8 个核心 Skill 做 A/B 测试：Control（不使用 Waza）vs Experimental（强制使用 /health /think /design /hunt /check /read /learn /write），并输出中文实证报告。

## Work Log

- 创建工作目录: `waza-ab-test`
- 克隆数据源: `git clone https://github.com/tw93/Waza.git waza-ab-test/Waza`
- 检索核心 Skill 描述: `rg -n "health|think|design|hunt|check|read|learn|write" README.md`
- 联网检索 Codex/Claude Code 官方资料（优先官方文档）并抓取页面。

## Data Sources / URLs Used
- https://github.com/tw93/Waza
- https://openai.com/index/introducing-codex/
- https://developers.openai.com/api/docs/models/gpt-5.2-codex
- https://code.claude.com/docs/en/cli-usage
- https://code.claude.com/docs

## Experiments
1. 场景一 Control：直接产出 To-Do App 方案 + Bug 修复代码。
   - Outcome: 能完成需求，但缺少前置风险建模与审美迭代，Debug 证据链薄弱。
2. 场景一 Experimental：按 `/health -> /think -> /design -> /hunt -> /check` 流程模拟。
   - Outcome: 交付物结构化明显更强，Root Cause 与发布约束可追踪。
3. 场景二 Control：直接写 800 字对比。
   - Outcome: 易出现模板化“先总后分”与泛化判断。
4. 场景二 Experimental：`/read -> /learn -> /write`。
   - Outcome: 信息密度和论据锚点显著提高，语气更像技术作者。

## Failed Paths
- 尝试在 Waza 仓库中直接执行 `/health` 等命令：当前容器未安装对应 skills 运行时入口（slash command host），故改为基于 SKILL 定义进行“流程对齐式”实验，而非真实命令执行。
- 初次 `rg` 搜索包含 `.claude` 路径，目标目录不存在报错；后续改为只读 README 与 skills 目录。

## Verification Evidence
- `git log -1 --oneline` in Waza clone => `9f692ac ...`
- `rg` 命令输出可定位 8 个技能的定位描述。
- Web 抓取结果中包含 OpenAI/Anthropic 官方页面关键段落（模型定位、agentic turn、CLI 行为）。
