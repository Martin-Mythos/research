# Repository Reconnaissance

## Snapshot
Inspected `yc-software/qm` at commit `7f2c916360f1797a8ff2a77ce2ce40c5fabab087` (2026-07-31). MIT licensed. QM describes itself as a multiplayer organizational agent harness for Slack/web—not as a standalone generic task queue.

## Claims and architecture
The README claims interchangeable Pi, OpenCode, Codex, and Claude Code harness/model choices; scoped durable workspaces; background crons/watches; and Postgres persistence for sessions, memory, and queue. Core is TypeScript on Node/Fastify, with optional Slack and Lit/Vite web plugins. The `qm` package is a deployment CLI, explicitly “not the runtime.”

## Queueing, multi-task dispatch, concurrency
Static inspection found:
- memory and Postgres `TaskStore` implementations with create/list/event and compare-and-set status transitions;
- task statuses only; task records contain no payload, worker assignment, attempt count, deadline, result, model, or thinking setting;
- OpenCode/Claude harness adapters observe child/subagent task events and mirror status to `TaskStore`; OpenCode defines `research`, `code`, and `consult` subagents;
- `createKeyedQueue` serializes work sharing a key, while different keys can proceed independently;
- turn-level model and thinking controls exist (`thinkingLevel` and adapter mappings), but no documented public configuration found for selecting a separate worker model/effort per delegated subtask.

Thus “multi-task dispatch” is harness-driven subagent behavior, not a `qm dispatch` CLI/API contract discovered here. Concurrent execution may be supplied by the selected upstream harness. Retry semantics were not found in `TaskStore`.

## Runtime/install/entry points
Root requires Node >=24.15.0 and npm >=11.10.0. Entry scripts include `npm start`, `npm test`, `npm run worker`; documented operator flow initializes a deployment with the published CLI and requires Docker/cloud infrastructure for a full instance. Local full deployment needs external components such as Postgres, sandbox/container infrastructure, and model/provider credentials. The repository includes extensive Node tests, mock harness code, smoke scripts, and CI shards.

## Risks / threat-model indicators
No malware/spam/credential-harvesting indicator was observed during reviewed setup. Installation hooks were not found in package manifests inspected, and install used `--ignore-scripts`. Dynamic work stayed mock/local. The project's own SECURITY.md calls it early experimental software and documents command-policy bypasses, plaintext sandbox credentials while used, incomplete heuristic screening, conditional egress enforcement, provider paths bypassing the intended gateway, durable request capture, and privileged admin reads. These are material for cybersecurity use.

## Files inspected
`README.md`, `SECURITY.md`, `LICENSE`, `package.json`, `.npmrc`, `.node-version`, `docs/getting-started.md`, `cli/README.md`, `.github/workflows/cicd.yml`, task stores/tests, async utility, and Pi/OpenCode/Claude harness adapters/tests.
