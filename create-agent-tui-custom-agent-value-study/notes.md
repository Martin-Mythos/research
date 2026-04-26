# Notes

## Original prompt / question
- 用户请求（中文）：使用 open research skill，研究项目 `https://github.com/OpenRouterTeam/skills/tree/main/skills/create-agent-tui`。
- 核心目标：理解“自定义 agent(custom agent)”的价值，以及适用场景；设计合适实验并输出全面研究报告。

## Working log
- 初始化研究目录：`mkdir -p create-agent-tui-custom-agent-value-study`
- 读取本仓库约束：`cat AGENTS.md`
- 读取 skill 说明：`cat .agents/skills/open-research/SKILL.md`
- 远程拉取目标项目文件列表：`curl -s https://api.github.com/repos/OpenRouterTeam/skills/contents/skills/create-agent-tui | jq -r '.[].name'`
- 初步查看目标 skill：`curl -L https://raw.githubusercontent.com/OpenRouterTeam/skills/main/skills/create-agent-tui/SKILL.md`

## Data sources / URLs used
- https://github.com/OpenRouterTeam/skills/tree/main/skills/create-agent-tui
- https://raw.githubusercontent.com/OpenRouterTeam/skills/main/skills/create-agent-tui/SKILL.md
- https://api.github.com/repos/OpenRouterTeam/skills/contents/skills/create-agent-tui
- 尝试克隆上游仓库失败（策略阻断）：
  - 命令：`git clone --depth 1 https://github.com/OpenRouterTeam/skills.git`
  - 结果：`blocked by policy`
  - 处理：改用 GitHub Raw + GitHub API 拉取所需文件（可复现、无需完整仓库）。
- 拉取上游文本与样例代码：
  - `curl -sL .../SKILL.md -o artifacts/upstream/SKILL.md`
  - `curl -sL .../README.md -o artifacts/upstream/README.md`
  - `curl -sL .../metadata.json -o artifacts/upstream/metadata.json`
  - `curl -sL .../references/*.md -o artifacts/upstream/references-*.md`
  - `curl -sL .../sample/src/*.ts -o artifacts/upstream/sample-src/*`
- 设计并实现实验脚本：
  - `scripts/evidence_scan.py`：扫描关键能力声明是否在文档/样例中出现。
  - `scripts/evaluate_use_cases.py`：构建“自定义 agent vs 普通聊天壳”能力覆盖实验。
- 执行实验：
  - `python3 scripts/evidence_scan.py` 成功，输出 `artifacts/results/evidence_scan.json`
  - `python3 scripts/evaluate_use_cases.py` 成功，输出 `artifacts/results/capability_matrix.json` 与 `.md`

## Verification evidence
- 覆盖实验结果（节选）：
  - 受控代码助手：custom 1.00 vs baseline 0.00
  - 一次性问答：custom 1.00 vs baseline 1.00（无增益）
  - 长周期研究、运维排障、后端内嵌：均 custom 1.00 vs baseline 0.00
- 生成最终报告：`create-agent-tui-custom-agent-value-study/README.md`
- 最终校验：
  - `python3 create-agent-tui-custom-agent-value-study/scripts/evidence_scan.py`
  - `python3 create-agent-tui-custom-agent-value-study/scripts/evaluate_use_cases.py`
  - `git diff --check`
  - `git status --short`（仅研究目录变更）
