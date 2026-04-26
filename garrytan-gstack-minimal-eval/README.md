# garrytan/gstack 最小实验研究

## Final Conclusion

`garrytan/gstack` 不是一个单一 app，而是一个 Bun + TypeScript 写成的 AI engineering workflow stack。它把大量 slash-command skills、browser automation、host-specific skill generation、review/QA/ship 流程和安全 guardrails 组织成一套可安装到 Claude Code、Codex、OpenCode、Cursor、Factory、Kiro、OpenClaw、Hermes、GBrain 等 host 的“软件工厂”。

本次最小实验选择了最贴合项目性质的验证面：skill documentation generation、host projection、browse command registry validation。结果显示核心生成和校验路径基本健康：`skill-validation` 318/318 通过，`gen-skill-docs` 在生成 Codex host artifacts 后 371/371 通过。本研究还发现一个值得注意的健康脚本不一致：`scripts/skill-check.ts` 会因 `claude/SKILL.md` 缺失退出 1，但测试套件明确断言 `claude/SKILL.md` 不应为 Claude host 生成。

## Research Question And Scope

研究问题：`garrytan/gstack` 是什么性质的项目？根据它的项目性质，怎样设计一个最小可复现实验来验证它的核心机制？

范围：

- 源项目：<https://github.com/garrytan/gstack>
- 本地 clone commit：`ed1e4be2f68bf977f1fa485eba94d89dbef5255c`
- 项目版本：`gstack@1.14.0.0`
- 实验环境：macOS，本机安装 `bun 1.3.13`
- 不做完整 browser daemon、Chrome extension、ngrok pairing、真实 Claude Code installation 或 production deploy 测试

## Methods And Sources

实际使用的来源：

- `README.md`：项目定位、quick start、skill list、host support
- `ARCHITECTURE.md`：browser daemon、Bun、security、SKILL.md template system
- `package.json`：scripts、dependencies、version
- `SKILL.md`：root gstack skill 生成结果
- `scripts/discover-skills.ts`
- `scripts/gen-skill-docs.ts`
- `scripts/skill-check.ts`
- `browse/src/commands.ts`
- `test/gen-skill-docs.test.ts`
- `test/skill-validation.test.ts`

本研究产物：

- `notes.md`：原始需求、命令、失败路径、验证证据
- `scripts/analyze-gstack.mjs`：本研究的独立审计脚本
- `artifacts/gstack-audit.json`
- `artifacts/gstack-audit.md`
- `artifacts/upstream-test-summary.md`

## Minimal Experiment

### 1. Install And Inspect

最初本机没有 `bun`，因此先安装：

```bash
brew install oven-sh/bun/bun
bun --version
```

验证版本：

```text
1.3.13
```

在 `/tmp/garrytan-gstack` 安装依赖：

```bash
bun install --frozen-lockfile
```

结果：

```text
228 packages installed [36.60s]
```

### 2. Run Project-Native Skill Validation

```bash
bun test test/skill-validation.test.ts
```

结果：

```text
318 pass
0 fail
1161 expect() calls
```

这个测试覆盖 `$B` browse commands 是否都能在 command registry 中解析、snapshot flags 是否有效、generated `SKILL.md` 是否没有 unresolved placeholders、update-check preamble 是否安全等。

### 3. Run Generated Docs Freshness Check

```bash
bun run scripts/gen-skill-docs.ts --dry-run
```

结果：所有列出的 generated `SKILL.md` 均为 `FRESH`。同时观察到一个 warning：

```text
ship/SKILL.md is 166885 bytes (~41721 tokens), exceeds 160000 byte ceiling
```

这不是失败，但说明某些 skill 文件已经非常大，未来可能影响 agent load / context 成本。

### 4. Generate Codex Host Skills And Re-run Docs Tests

第一次运行：

```bash
bun test test/gen-skill-docs.test.ts
```

结果为 `363 pass, 0 fail, 1 error`。错误原因是 fresh clone 缺少：

```text
.agents/skills/gstack-office-hours/SKILL.md
```

随后生成 Codex host artifacts：

```bash
bun run scripts/gen-skill-docs.ts --host codex
```

结果生成 43 个 Codex-host skills。再运行：

```bash
bun test test/gen-skill-docs.test.ts
```

最终结果：

```text
371 pass
0 fail
5005 expect() calls
```

这个路径验证了 gstack 的核心 host projection 机制：同一批 skill templates 可以生成不同 host 的 skill output，并做 path rewrite、frontmatter rewrite、Codex-specific exclusions 等。

### 5. Run Local Audit Script

本研究脚本：

```bash
node garrytan-gstack-minimal-eval/scripts/analyze-gstack.mjs /tmp/garrytan-gstack
```

输出：

```json
{
  "skillCount": 43,
  "templatedSkillCount": 43,
  "browseCommands": {
    "read": 19,
    "write": 28,
    "meta": 25,
    "total": 72
  },
  "packageVersionMatchesVersionFile": true
}
```

## Verified Findings

1. `gstack` 的核心不是普通 CLI 功能，而是 generated skill system。43 个 discovered skills 全部有 `SKILL.md.tmpl` 模板。
2. `browse/src/commands.ts` 是 browser command registry 的关键 source of truth。本研究脚本统计到 72 个 browse commands：19 read、28 write、25 meta。
3. `package.json` version 与 `VERSION` 文件一致，均为 `1.14.0.0`。
4. `test/skill-validation.test.ts` 全部通过，说明核心 skill command references、snapshot flags、preamble safety 和 generated docs 基础一致性可被 upstream 测试验证。
5. `test/gen-skill-docs.test.ts` 需要先生成 Codex host artifacts 才能在 fresh clone 上完整通过；生成后 371/371 通过。
6. `scripts/skill-check.ts` 当前对 `claude/SKILL.md` 的健康检查和测试套件中的“Claude outside-voice skill is not generated for Claude host”约定存在不一致。
7. `ship/SKILL.md` 超过项目自身 token ceiling warning，说明 gstack 的“把流程压进 Markdown”路线已经接近单 skill 文件体量边界。

## Limitations And Risks

- 没有运行完整 `bun test`，因为项目包含 browser、extension、LLM eval、agent SDK、Playwright 等更重路径；本次只验证最小核心机制。
- 没有真实安装到 Claude Code 或 Codex skill directory。
- 没有启动 gstack browser daemon，也没有验证 persistent browser state、cookie import、ngrok tunnel、sidebar security classifier。
- 本研究的分类脚本是启发式，不代表 upstream 官方分类。
- `scripts/gen-skill-docs.ts --host codex` 和测试会改写 `/tmp/garrytan-gstack` 中的 generated artifacts；这些变化没有也不应提交到本 research repo。

## Reproduction

从本 research repo 根目录执行：

```bash
git clone --depth 1 https://github.com/garrytan/gstack.git /tmp/garrytan-gstack
cd /tmp/garrytan-gstack
bun install --frozen-lockfile
bun test test/skill-validation.test.ts
bun run scripts/gen-skill-docs.ts --dry-run
bun run scripts/gen-skill-docs.ts --host codex
bun test test/gen-skill-docs.test.ts
cd /Users/martin/Code/research
node garrytan-gstack-minimal-eval/scripts/analyze-gstack.mjs /tmp/garrytan-gstack
```

预期：

- `skill-validation.test.ts` 全部通过
- `gen-skill-docs.test.ts` 在生成 Codex host skills 后全部通过
- `artifacts/gstack-audit.json` 和 `artifacts/gstack-audit.md` 被生成或刷新

## Concrete Next Steps

- 如果要评估“用户是否真的能 30 秒安装”，下一轮应开独立研究，实际运行 `./setup --host codex` 或 Claude Code install path，并检查安装后的 skill discovery。
- 如果要评估 browser automation，下一轮应启动 browse daemon，跑一个本地 HTML fixture 的 `$B snapshot` / click / screenshot / diff flow。
- 如果要贡献 upstream issue，可以把 `scripts/skill-check.ts` 对 `claude/SKILL.md` 的处理与测试中的 intentional non-generation 约定对齐。
