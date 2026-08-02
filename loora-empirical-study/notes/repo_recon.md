# Repository Reconnaissance

## Snapshot

- Target: <https://github.com/lassejlv/loora>
- Inspected commit: `1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce` (2026-08-01).
- License: AGPL-3.0-or-later (`LICENSE` and root manifest).
- Purpose claimed by README: an agent-editable structured UI canvas shared with Claude, Codex, Cursor, or opencode over MCP, with branches/history and one-way HTML, React/TSX, JSON, and PNG export.

## Architecture and stack

Bun workspace monorepo. Web is React 19/TanStack Start/Vite; desktop is Tauri; the canvas model/transaction engine/import/export live in `packages/canvas`; shared agent tools in `packages/agent`; remote MCP in `apps/mcp`; oRPC/data path in `packages/rpc` and `packages/db` (Drizzle/Neon); authentication uses Better Auth; billing uses Polar; realtime has Bun and Rust WebSocket implementations plus Redis-optional transport.

Likely entry points are root `bun run dev`, `apps/mcp/src/index.ts` / `stdio.ts`, `apps/ws/src/index.ts`, `crates/ws-server/src/main.rs`, and the desktop Tauri app. Three Dockerfiles and Railway manifests describe deployment.

## Installation and test surface

The manifest pins Bun 1.3.14. `.env.example` requires database/auth configuration for the full service; billing, GitHub, storage, Redis/realtime, email, and analytics are conditional integrations. Root tests use Bun with a JSDOM preload. Rust websocket tests are separate. No conventional CI workflow was present; `.github` contained only funding metadata. Tests are extensive across canvas engine/model/export/import, agent tools, auth, realtime, RPC, billing, editor, and UI.

## Initial risks and threat-model indicators

Positive indicators found in code/tests: typed/validated transactions; canvas node and import size limits; sanitizer and HTML import sandbox tests; bearer-token verification; WebSocket credential validation; signed short-lived/single-use ticket tests; internal-token checks; bounded MCP concurrency; rate limiting; non-root Docker runtime users; and CSP in standalone HTML export.

Risk/complexity indicators: broad dependency graph (1,242 installed packages), multiple external trust boundaries, bearer tokens/OAuth, hosted DB/billing/storage/email/analytics, Redis-optional in-memory fallbacks, browser image fetching during PNG export, remote MCP mutation authority, and inline script/style allowances in exported HTML CSP. Deployment correctness depends on secrets and several services. AGPL network-use obligations matter for modified hosted deployments.

No malware, credential harvesting, exploit payload, or spam automation was observed in reconnaissance, so bounded local execution continued. This was not a line-by-line audit.
