# Investigation Notes

## Original prompt

Empirically investigate https://github.com/lassejlv/loora to determine its actual technical capability and whether it balances R&D agility with cybersecurity boundary controls. Install, run, test, compare with a baseline, document failures and evidence, and publish a reproducible research project.

## Work log

- Created the required dedicated research directory before beginning investigation.

## Environment and initial commands (2026-08-01T16:01:04Z)

- Workspace: `/workspace/research`.
- Target URL: `https://github.com/lassejlv/loora`.
- Commands: `uname -a`, `/etc/os-release`, runtime/package-manager version probes, `git clone --depth 1`.

## Commands, experiments, and outcomes

- Inspected `/workspace/research/AGENTS.md` and `.agents/skills/open-research/SKILL.md` before research.
- Cloned `https://github.com/lassejlv/loora` shallowly into `/tmp/loora-target`; pinned HEAD `1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce`. The clone and all dependencies stayed outside the committed project directory.
- Read upstream `README.md`, `AGENTS.md`, `.env.example`, `LICENSE`, manifests/lockfile, Dockerfiles, Railway files, desktop/MCP/WebSocket docs, tests, source entry points, and `.github` files. Used `find`, `sed`, and `rg` for inventories and security patterns.
- Captured `uname`, OS release, runtimes/package managers, CPU, memory, and disk in `setup_log.md`.
- Official command `curl -fsSL https://bun.sh/install | bash -s -- bun-v1.3.14` failed HTTP 403. Fallback `npm install --global bun@1.3.14` succeeded. `bun install --frozen-lockfile` installed 1,242 packages.
- `bun run build` passed. `bunx tsc --noEmit` failed because `apps/web/scripts/benchmark-api.ts` cannot resolve `@orpc/client` and `@orpc/client/fetch`.
- `bun run test` produced extensive passes but also missing-`DATABASE_URL` import errors and a hook timeout, then became idle; manually interrupted. No aggregate success claimed.
- A focused test was mistakenly invoked without the documented JSDOM preload; 41 DOM-dependent failures resulted. Reran with preload: 168 passed, one 5,000-node performance gate failed at about 689 ms.
- Custom representative scenario initially misused an export overload; model validation rejected it. Corrected script passed: 3 structured nodes and HTML/React exports.
- Initial Rust suite: unit tests passed but two service tests saw HTTP 403. Removing only uppercase proxy variables did not fix it because lowercase variables remained. A clean environment (`env -i PATH="$PATH" HOME="$HOME" ...`) made all four service integration tests pass. This is preserved as environment diagnosis, not hidden.
- `bun audit` found one moderate advisory: esbuild development-server request/read exposure (GHSA-67mh-4wv8-2f99), transitively through drizzle-kit/Vite/router plugin; exit 1. Reachability was not established.
- No secrets or production services used. No browser screenshot created because live/authenticated UI was not verified and no web app was changed.

## URLs actually used

- `https://github.com/lassejlv/loora`
- `https://bun.sh/install`
- npm registry as contacted by `npm install --global bun@1.3.14`
- registry endpoints contacted automatically by `bun install`, `bun audit`, and Cargo for declared dependencies.

## Verification evidence worth preserving

- `artifacts/install.log`, `build.log`, `typecheck.log`, `test.log`
- `artifacts/focused-tests-with-preload.log`
- `artifacts/representative-scenario.log`
- `artifacts/cargo-test.log` and `cargo-test-no-proxy.log`
- `artifacts/bun-audit.log`
