# 工作笔记

## 原始研究问题
在真实的多文件业务项目（MVP）开发场景下，LoopKit 的自动化 Loop 与技能库能否有效提升 AI 智能体的一次性交付成功率并防止上下文断层？

## 命令、脚本、数据源与 URL
- 目标仓库：https://github.com/Archive228/loopkit
- `uname -a`, `python3 --version`, `node --version`, `npm --version`, `git --version`：记录运行环境。

## 仓库文件扫描
.claude/CLAUDE.md
.claude/agents/verifier.md
.claude/settings.json
.git/HEAD
.git/config
.git/description
.git/hooks/applypatch-msg.sample
.git/hooks/commit-msg.sample
.git/hooks/fsmonitor-watchman.sample
.git/hooks/post-update.sample
.git/hooks/pre-applypatch.sample
.git/hooks/pre-commit.sample
.git/hooks/pre-merge-commit.sample
.git/hooks/pre-push.sample
.git/hooks/pre-rebase.sample
.git/hooks/pre-receive.sample
.git/hooks/prepare-commit-msg.sample
.git/hooks/push-to-checkout.sample
.git/hooks/sendemail-validate.sample
.git/hooks/update.sample
.git/index
.git/info/exclude
.git/logs/HEAD
.git/packed-refs
.git/shallow
.gitignore
.mcp.json
.npmignore
LICENSE
MEMORY.md
README.md
bin/loopkit.js
docs/effective-harnesses-v03.md
docs/effective-harnesses-v03.pdf
install.sh
package.json
run.sh
skills/a11y-pass/SKILL.md
skills/adversarial-verify/SKILL.md
skills/authz-check/SKILL.md
skills/bisect-regression/SKILL.md
skills/changelog-from-diff/SKILL.md
skills/clean-commits/SKILL.md
skills/context-budget/SKILL.md
skills/contract-test/SKILL.md
skills/coverage-gaps/SKILL.md
skills/decision-record/SKILL.md
skills/dependency-audit/SKILL.md
skills/design-system/SKILL.md
skills/flaky-hunter/SKILL.md
skills/input-validation/SKILL.md
skills/kill-dead-code/SKILL.md
skills/loading-empty-error-states/SKILL.md
skills/migration-writer/SKILL.md
skills/owasp-review/SKILL.md
skills/pr-from-diff/SKILL.md
skills/read-the-trace/SKILL.md
skills/readme-audit/SKILL.md
skills/rebase-safely/SKILL.md
skills/reduce-nesting/SKILL.md
skills/revert-surgical/SKILL.md
skills/schema-diff/SKILL.md
skills/secret-scan/SKILL.md
skills/simplify/SKILL.md
skills/spec-first/SKILL.md
skills/sql-review/SKILL.md
skills/subagent-fanout/SKILL.md
skills/systematic-debugging/SKILL.md
skills/tool-restraint/SKILL.md
skills/write-failing-test-first/SKILL.md
- 补充复制 `/tmp/loopkit-src/skills` 到 MVP 的 `.claude/skills`，与安装器目标布局保持一致。
