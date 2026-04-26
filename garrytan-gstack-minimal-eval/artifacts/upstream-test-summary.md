# Upstream Test Summary

Source clone: `/tmp/garrytan-gstack`

Commit: `ed1e4be2f68bf977f1fa485eba94d89dbef5255c`

## Dependency Install

```text
bun install --frozen-lockfile
=> 228 packages installed [36.60s]
```

## Minimal Verification Commands

```text
bun test test/skill-validation.test.ts
=> 318 pass, 0 fail, 1161 expect() calls
```

```text
bun run scripts/gen-skill-docs.ts --dry-run
=> all listed generated SKILL.md files FRESH
=> warning: ship/SKILL.md is 166885 bytes (~41721 tokens), above 160000 byte ceiling
```

```text
bun run scripts/gen-skill-docs.ts --host codex
=> generated 43 Codex-host skills under .agents/skills/
```

```text
bun test test/gen-skill-docs.test.ts
=> first run: 363 pass, 0 fail, 1 error
=> cause: missing .agents/skills/gstack-office-hours/SKILL.md in fresh clone
=> after generating Codex-host skills: 371 pass, 0 fail, 5005 expect() calls
```

```text
bun run scripts/skill-check.ts
=> exit 1
=> main red item: claude/SKILL.md generated file missing
=> notable context: gen-skill-docs tests explicitly assert claude/SKILL.md is not generated for Claude host
=> all external host sections reported 43 skills, 0 missing
=> all freshness checks for Claude Code, Codex, Factory, Kiro, OpenCode, Slate, Cursor, OpenClaw, Hermes, and GBrain passed
```

## Research Interpretation

The minimal project-specific experiment supports the conclusion that gstack's core mechanics are generated skill documentation, host-specific skill projection, browse command registry validation, and workflow/safety process encoding. The only red result observed is a `skill-check.ts` health-report inconsistency around `claude/SKILL.md`, not a failed generated-docs test.
