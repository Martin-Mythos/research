# Run Log

## Snapshot and environment

Cloned commit `1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce` at shallow depth. Detailed OS/runtime/CPU/memory/disk evidence is in `setup_log.md`; clone output is in `artifacts/clone.log`.

## Installation

1. `curl -fsSL https://bun.sh/install | bash -s -- bun-v1.3.14` failed with HTTP 403.
2. Minimal fallback `npm install --global bun@1.3.14` succeeded; `bun --version` printed `1.3.14`.
3. `bun install --frozen-lockfile` succeeded: 1,242 packages in 9.84 seconds. See `artifacts/install.log`.

## Build and static checks

- `bun run build` passed (exit 0; Vite/Nitro production output built in 7.89 seconds in the retained tail).
- `bunx tsc --noEmit` failed (exit 2): `apps/web/scripts/benchmark-api.ts` could not resolve `@orpc/client` and `@orpc/client/fetch`. The production build nevertheless passed. This appears to be an upstream workspace dependency/type-check issue, not repaired locally.

## Tests

- `bun run test` exercised a large portion of the suite but did not terminate cleanly in the observation window. It reported missing `DATABASE_URL` import-time errors in DB-coupled suites and a 5-second hook timeout; after extensive subsequent passes it became idle and was manually interrupted. Therefore no overall pass count is claimed.
- A focused command with the required JSDOM preload ran 169 tests: **168 passed, 1 failed**. The sole failure was the 100-node/5,000-node engine performance gate (observed about 689 ms); functional canvas, agent, auth, configuration, sanitizer, and import-boundary tests passed.
- An earlier focused invocation without the documented preload produced 41 DOM-related false failures. It was abandoned and rerun correctly; the log is retained to make the failed path explicit.
- `cargo test -p loora-ws-server` initially had 4 unit passes and 2/4 service integration passes; two localhost HTTP expectations instead received 403. Removing all inherited environment (including lowercase proxy variables) and rerunning the service test produced 4/4 passes. This demonstrates an environment/proxy interaction, while the clean run verifies the service tests.

## Representative capability scenario

`bun representative-scenario.ts` (script copied into checkout root) created a page, frame/button, and text through the shared agent schema, applied its validated transaction, read a semantic tree, and exported it. Corrected run: exit 0, 3 nodes, 7,565 fragment bytes, 8,034 standalone HTML bytes, and 10,134 React bytes. Initial run incorrectly passed a compiled result where the export API expected a document/prepared plan; schema validation rejected it (`Expected Canvas schema 2`). The script was corrected rather than bypassing validation.

## Security/dependency check

`bun audit` was run against the installed lockfile; see `artifacts/bun-audit.log`. Findings are snapshot indicators, not proof of exploitability. No production endpoints or unauthorized third parties were contacted.
