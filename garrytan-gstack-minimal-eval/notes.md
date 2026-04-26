# Notes

## Original Prompt

User asked, in Chinese:

> `$open-research https://github.com/garrytan/gstack 同样的，研究一下这个gstack，根据其项目性质做一个最小实验输出实验和总结报告。`

## Research Question

What kind of project is `garrytan/gstack`, and what is the smallest reproducible experiment that demonstrates its practical behavior or core idea?

## Working Scope

- Source project: <https://github.com/garrytan/gstack>
- Expected output: a small experiment, evidence artifacts, notes, and a final report.
- External repository clone target: `/tmp/garrytan-gstack`.

## Sources Actually Used

- Root repository instructions: `/Users/martin/Code/research/AGENTS.md`
- Open research skill instructions: `/Users/martin/Code/research/.agents/skills/open-research/SKILL.md`

## Commands And Tools

- `pwd`
- `git status --short --branch`
- `sed -n '1,220p' AGENTS.md`
- `sed -n '1,180p' /Users/martin/Code/research/.agents/skills/open-research/SKILL.md`
- `git diff -- mattpocock-skills-todo-app-eval/artifacts/skills-index.md`
- `mkdir -p garrytan-gstack-minimal-eval`
- `git clone --depth 1 https://github.com/garrytan/gstack.git /tmp/garrytan-gstack`
- `find /tmp/garrytan-gstack -maxdepth 2 -type f | sed 's#^/tmp/garrytan-gstack/##' | sort`
- `git -C /tmp/garrytan-gstack rev-parse HEAD`
- `sed -n '1,260p' /tmp/garrytan-gstack/README.md`
- `find /tmp/garrytan-gstack -maxdepth 2 -type f \( -name 'package.json' -o -name 'pyproject.toml' -o -name 'Cargo.toml' -o -name 'go.mod' -o -name 'requirements.txt' -o -name 'Makefile' \) -print`
- `sed -n '1,240p' /tmp/garrytan-gstack/package.json`
- `sed -n '1,260p' /tmp/garrytan-gstack/ARCHITECTURE.md`
- `sed -n '1,220p' /tmp/garrytan-gstack/SKILL.md`
- `sed -n '1,220p' /tmp/garrytan-gstack/scripts/discover-skills.ts`
- `command -v bun`
- `bun --version`
- `brew install oven-sh/bun/bun`
- `bun install --frozen-lockfile` in `/tmp/garrytan-gstack`
- `bun test test/gen-skill-docs.test.ts` in `/tmp/garrytan-gstack`
- `bun test test/skill-validation.test.ts` in `/tmp/garrytan-gstack`
- `bun run scripts/gen-skill-docs.ts --dry-run` in `/tmp/garrytan-gstack`
- `bun run scripts/gen-skill-docs.ts --host codex` in `/tmp/garrytan-gstack`
- `bun run scripts/skill-check.ts` in `/tmp/garrytan-gstack`
- `node garrytan-gstack-minimal-eval/scripts/analyze-gstack.mjs /tmp/garrytan-gstack`
- `find garrytan-gstack-minimal-eval -maxdepth 4 -type f | sort`
- `git diff --check -- garrytan-gstack-minimal-eval`
- `git status --short`

## Experiments

- Cloned `garrytan/gstack` into `/tmp/garrytan-gstack`. Commit checked: `ed1e4be2f68bf977f1fa485eba94d89dbef5255c`.
- Identified project type: Bun + TypeScript skill/workflow system for Claude Code and multiple AI coding hosts, with browser automation, generated skills, host adapters, and a large Bun test suite.
- Installed Bun because it was not present initially. Installed version: `1.3.13`.
- Installed gstack dependencies with `bun install --frozen-lockfile`.
- Ran upstream skill validation test: `bun test test/skill-validation.test.ts`.
- Ran generated skill docs freshness check: `bun run scripts/gen-skill-docs.ts --dry-run`.
- Ran `bun test test/gen-skill-docs.test.ts`; first run failed because fresh clone did not contain `.agents/skills/gstack-office-hours/SKILL.md`.
- Generated Codex-host skills with `bun run scripts/gen-skill-docs.ts --host codex`, then reran `bun test test/gen-skill-docs.test.ts` successfully.
- Ran `bun run scripts/skill-check.ts`; it exited 1 because it expects `claude/SKILL.md`, while tests explicitly assert that `claude/SKILL.md` is not generated for Claude host.
- Wrote and ran a local audit script that counts skills, templates, version consistency, and browse command registry size.

## Failed Paths

- Initial `git clone` failed inside the earlier restricted sandbox with `Could not resolve host: github.com`; reran after network access was available and cloned successfully.
- Initial `bun` check failed because Bun was not installed; installed with Homebrew command `brew install oven-sh/bun/bun`.
- First `bun test test/gen-skill-docs.test.ts` produced `363 pass, 0 fail, 1 error` because `.agents/skills/gstack-office-hours/SKILL.md` was missing in the fresh clone. This was resolved by running `bun run scripts/gen-skill-docs.ts --host codex`.
- `bun run scripts/skill-check.ts` exited 1 due to `claude/SKILL.md` missing. This appears to be a health-script inconsistency: `test/gen-skill-docs.test.ts` contains a passing assertion named "Claude outside-voice skill is not generated for Claude host".

## Verification Evidence

- `bun install --frozen-lockfile`: `228 packages installed [36.60s]`.
- `bun test test/skill-validation.test.ts`: `318 pass`, `0 fail`, `1161 expect() calls`.
- `bun run scripts/gen-skill-docs.ts --dry-run`: generated skill files reported `FRESH`; warning observed: `ship/SKILL.md is 166885 bytes (~41721 tokens), exceeds 160000 byte ceiling`.
- `bun run scripts/gen-skill-docs.ts --host codex`: generated `43` Codex-host skills under `.agents/skills/`.
- Final `bun test test/gen-skill-docs.test.ts`: `371 pass`, `0 fail`, `5005 expect() calls`.
- `bun run scripts/skill-check.ts`: exit `1`; external host sections reported `43 skills, 0 missing`, and all freshness checks passed.
- Local audit script output:

```text
{"skillCount":43,"templatedSkillCount":43,"browseCommands":{"read":19,"write":28,"meta":25,"total":72},"packageVersionMatchesVersionFile":true}
```
- Research repo validation:

```text
git diff --check -- garrytan-gstack-minimal-eval
=> passed with no output

git status --short
=> M mattpocock-skills-todo-app-eval/artifacts/skills-index.md
=> ?? garrytan-gstack-minimal-eval/
```

The `mattpocock-skills-todo-app-eval/artifacts/skills-index.md` change is unrelated pre-existing drift and is intentionally not included in this project commit.
