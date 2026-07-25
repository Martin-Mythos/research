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

## 审查修订（2026-07-25）
- 使用 `git clone https://github.com/Archive228/loopkit /tmp/loopkit-review-src` 和 `git log --before='2026-07-06T00:00:00Z'`，锁定原实验日期对应提交 `22101ff114cbf80bf3d14d41c8c662f507b1b971`；该快照有 33 个技能目录。
- 发现目标仓库当前 HEAD 已变化，技能目录数量与 README 徽章也在演进；因此放弃扫描浮动 `main`，改为固定提交复现。
- 发现初版 `skill_trigger_scan.py` 使用 `w in keywords` 的子字符串匹配，导致 `a`、`it` 等词产生误报并把 29/33 标为相关。废弃该启发式，改为显式列出 10 个模拟选择及理由，并增加扫描器单元测试。
- 删除产物中复制的完整 `.claude/skills`、`.mcp.json`、`MEMORY.md` 与 `run.sh`，避免提交外部仓库副本；新增 `scripts/install_pinned_loopkit.sh` 供复现时临时安装。
- 将硬编码 token 密钥改为至少 32 字符的 `LOOPKIT_MVP_SECRET` 环境变量；将单次 SHA-256 密码散列改为 200,000 次 PBKDF2-HMAC-SHA256 和随机盐；token 改为标准三段式 HS256 JWT。
- 增加 token 篡改拒绝和密码加盐测试。承认没有真实红→绿时间序列、没有运行 verifier、没有裸奔 Agent 对照组。
- 撤回初版报告中“减少 25%–40% 无效修改”的无证据估算，并降低相关评分。
- 复核命令 `cd artifacts/mvp-target-codebase && python -m pytest -q tests`：`6 passed in 1.74s`。
- 扫描器测试命令 `python -m pytest -q scripts/test_skill_trigger_scan.py`：`2 passed in 0.03s`。
- 固定快照扫描断言：总技能数 33、显式模拟选择数 10。
- 安装器复核：在 `mktemp -d` 目录运行 `bash scripts/install_pinned_loopkit.sh <临时目录> /tmp/loopkit-review-src`，确认安装 33 个技能目录且 `run.sh` 可执行；随后删除临时目录。
- `git diff --check` 与 `python -m compileall -q artifacts/mvp-target-codebase/src scripts` 均通过。
- 尝试从研究仓库根目录把 MVP 测试和扫描器测试合并到一次 pytest 调用时，MVP 因 `src` 不在根目录的 Python import path 而在收集期失败；该调用方式被放弃，继续按 README 在 MVP 工作目录运行。
