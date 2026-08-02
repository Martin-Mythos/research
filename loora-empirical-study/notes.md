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
- Captured `uname`, OS release, runtimes/package managers, CPU, memory, and disk; the relevant environment evidence is consolidated below.
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

## 2026-08-02 Codex review remediation

- Read the two inline comments on GitHub PR #29 through the public GitHub API:
  - <https://github.com/Martin-Mythos/research/pull/29#discussion_r3698412820>
  - <https://github.com/Martin-Mythos/research/pull/29#discussion_r3698412824>
- Consolidated the useful content from parallel narrative Markdown files into `README.md` and this chronological `notes.md`, then removed those redundant files from the final research commit.
- Corrected the Rust reproduction command to use the clean environment that actually yielded 4/4 passing service tests on the proxy-bearing research host.
- Verification commands: `find loora-empirical-study -type f`, `rg`, `git diff --check`, and a scripted check of the reproduction command and permitted file set.

## Repository reconnaissance details (consolidated)

### Snapshot, architecture, and entry points

The target was <https://github.com/lassejlv/loora> at immutable commit `1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce` (2026-08-01), licensed AGPL-3.0-or-later. Its README claims an agent-editable structured UI canvas shared over MCP, with branches/history and one-way HTML, React/TSX, JSON, and PNG export.

The inspected Bun workspace contains a React 19/TanStack Start/Vite web app, Tauri desktop app, the canvas model/transaction/import/export core in `packages/canvas`, shared typed agent tools in `packages/agent`, oRPC/Drizzle/Neon data services, Better Auth, Polar billing, remote MCP, and Bun/Rust realtime services. Likely entry points are root `bun run dev`, `apps/mcp/src/index.ts` / `stdio.ts`, `apps/ws/src/index.ts`, `crates/ws-server/src/main.rs`, and the Tauri app. Three Dockerfiles and Railway manifests describe deployment.

The manifest pins Bun 1.3.14. `.env.example` requires database/auth configuration for the complete service; billing, GitHub, storage, Redis/realtime, email, and analytics are conditional integrations. Root tests use Bun with a JSDOM preload, while Rust websocket tests are separate. No GitHub Actions workflow was present; `.github` contained funding metadata.

Positive threat-model indicators included typed/validated transactions; node/import size limits; sanitizer and HTML import sandbox tests; bearer-token verification; WebSocket credential validation; short-lived/single-use ticket tests; internal-token checks; bounded MCP concurrency; rate limiting; non-root Docker users; and standalone-export CSP. Risk indicators included 1,242 installed packages, numerous external trust boundaries, hosted data processors, Redis-optional memory fallbacks, browser image fetching, remote mutation authority, inline script/style CSP allowances, and AGPL network-use obligations. No malware, credential harvesting, exploit payload, or spam automation was observed during bounded reconnaissance; this was not a line-by-line audit.

### Experiment design

The investigation used five experiments: (1) clone, exact-toolchain frozen install, build, type check, root/focused tests, and Rust tests; (2) a core canvas/agent capability run; (3) a deployment-approval UI scenario compared qualitatively with hand-written HTML; (4) missing credential, malformed input, unauthorized access, sanitizer, and oversized-input boundaries; and (5) a manual static HTML baseline. No production account, key, database, billing system, or third-party target was used. Acceptance required zero-exit installation/build, a valid three-node document with nontrivial HTML/React exports, behavioral boundary evidence, and retained reproducibility data.

### Environment evidence

The host was Debian GNU/Linux 12 (bookworm), Linux `6.12.13`, x86_64, with 16 reported processors, approximately 31 GiB RAM, and approximately 38 GiB available workspace disk at setup. Initial runtime probes recorded Git 2.39.5, Node v22.17.0, npm 11.4.2, Python 3.11.8, pip 25.1.1, rustc/cargo 1.90.0; Bun, pnpm, yarn, Docker, and a usable `bun` binary were initially absent. The full raw setup snapshot previously held in `setup_log.md` was narrative evidence; the commands and relevant values are consolidated here, while command-specific output remains in `artifacts/`.

### Sources actually accessed

- <https://github.com/lassejlv/loora>
- <https://github.com/lassejlv/loora/commit/1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce>
- <https://github.com/lassejlv/loora/blob/1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce/README.md>
- <https://github.com/lassejlv/loora/blob/1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce/LICENSE>
- <https://github.com/lassejlv/loora/blob/1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce/AGENTS.md>
- Pinned checkout files: root manifests/lockfile, `.env.example`, Dockerfiles, application/package manifests, source, and tests.
- <https://bun.sh/install> (returned HTTP 403); npm registry fallback `bun@1.3.14` succeeded.
- Dependency registries contacted by `npm install`, `bun install`, `bun audit`, and Cargo.

- Review-remediation verification found that a fresh checkout needs `cargo fetch` before the clean-environment Rust command because clearing the environment also removes the network proxy required to reach crates.io. Added that prerequisite; the subsequent clean service run passed 4/4.
