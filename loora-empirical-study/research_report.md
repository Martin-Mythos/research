# Empirical Study and R&D Security Assessment of Loora

## 1. Executive Summary

At commit `1ce827c`, Loora is substantively more than a README concept: its dependency-light canvas core and shared agent vocabulary can create, validate, inspect, and export structured UI locally. Our representative scenario converted one parsed agent request into a three-node semantic document and produced standalone HTML and React output. The production web bundle built successfully, and focused tests provided direct evidence for substantial functional and boundary-control behavior.

The answer to the core question is **qualified yes**: Loora offers credible R&D agility and intentionally engineered controls, but this study does not justify unrestricted enterprise production adoption. The complete hosted path depends on database, OAuth/auth, billing, storage, realtime, and optionally Redis/email/analytics boundaries. The root test command was not hermetic without `DATABASE_URL`, TypeScript checking failed on an undeclared/unresolved benchmark dependency, one performance gate failed on this host, and live MCP/collaboration/desktop/PNG paths were not end-to-end verified. Recommendation: **controlled trial**, with isolated deployment, egress policy, secret management, dependency remediation, and identity/authorization testing.

## 2. Project Overview

**Claimed:** an infinite structured-UI canvas that humans and external agents edit through MCP, sharing a document with branches/history and one-way HTML, React/TSX, JSON, and PNG export.

**Observed architecture:** Bun monorepo with React/TanStack web, Tauri desktop, canvas model/engine/export package, shared typed agent operations, oRPC/Drizzle/Neon data plane, Better Auth/OAuth, Polar entitlements, MCP service, and Bun/Rust realtime services. The inspected snapshot is AGPL-3.0-or-later.

## 3. Research Questions

1. Does the documented software install, build, and test on a clean cloud host?
2. Can its central agent-to-structured-canvas-to-code path actually execute locally?
3. Does that path improve an R&D workflow compared with manual HTML?
4. Are cybersecurity boundaries visible and behaviorally tested?
5. Where does evidence end and inference begin?

## 4. Experiment Design

Five experiments covered smoke/build, core capability, a deployment-approval UI scenario, invalid/missing/unauthorized boundaries, and a manual HTML baseline. We avoided accounts, keys, production services, and third-party targets. Detailed criteria and commands are in `experiment_plan.md`.

## 5. Setup & Execution Evidence

The pinned repository cloned successfully. The official Bun installer URL returned HTTP 403 in this environment, so exact Bun 1.3.14 was installed through npm; frozen install added 1,242 packages. The web production build passed. TypeScript checking failed because the API benchmark script could not resolve two `@orpc/client` imports.

The root test command ran many passing suites but emitted import-time `DATABASE_URL is required` errors, one hook timeout, and later stopped producing output; it was interrupted, so it is not reported as a pass. A targeted command using the required JSDOM preload completed with 168 passes and one environment-sensitive performance-gate failure. Rust WebSocket tests passed 4/4 in a clean environment after inherited proxy variables caused two 403 failures. `bun audit` reported one moderate esbuild development-server advisory and exited 1; reachability was not assessed. The custom scenario passed after one incorrect API composition was rejected by schema validation and corrected.

## 6. Findings

### Verified

- Frozen dependency installation and a production web build work on this host.
- The structured agent path parses descriptors, constructs a transaction, applies it to a canvas document, returns a semantic tree, and exports nontrivial HTML and React.
- Focused tests directly exercised atomic/invertible transactions, model limits, merge semantics, agent input rejection, auth token handling/timeouts/caching, missing realtime credential rejection, HTML sanitization, sandboxed import, and oversized-input rejection.
- Repository code separates canvas core from auth/DB concepts and runs Docker runtime stages as unprivileged users.
- Standalone export includes a restrictive default CSP, though it allows inline styles/scripts and HTTPS images.

### Failed

- Official installer endpoint: HTTP 403; npm fallback succeeded.
- `bunx tsc --noEmit`: unresolved `@orpc/client` imports in `apps/web/scripts/benchmark-api.ts`.
- Root test run was non-hermetic without DB config and did not terminate cleanly in the observation window.
- Focused suite: 5,000-node performance threshold failed (~689 ms); 168 other tests passed. Rust service tests passed 4/4 with proxy variables removed.
- First scenario attempt misused the overloaded export API and was correctly rejected; fixed attempt passed.

### Unverified

Live remote MCP OAuth and authorization, cross-account isolation against a real DB, collaborative multi-instance Redis behavior, billing enforcement against Polar, GitHub integration, object storage/email/analytics, desktop credential storage/proxy behavior, PNG capture via Chromium, Docker image builds, deployment migration behavior, and browser UX/screenshots.

### Surprising

The upstream repository guide is more operationally/security-specific than the short README. Conversely, no GitHub Actions CI workflow was present in the snapshot, despite a large test surface. The default root test command imports DB-dependent suites before a local DB fixture exists.

### Cautious inference

Typed tools, transaction preconditions, one-way export, import sanitation, short-lived tickets, and service separation reduce arbitrary-code and cross-boundary risk relative to an agent directly editing/running source. They do not prove correct authorization or prevent data leakage after deployment; those properties depend on configuration and untested integration paths.

## 7. Evaluation Matrix

| Dimension | Score / 5 |
|---|---:|
| Installability | 3 |
| Documentation Quality | 4 |
| Core Functionality | 4 |
| Cybersecurity Posture | 3 |
| R&D Agility | 4 |
| Experiment Reproducibility | 4 |
| **Unweighted mean** | **3.7** |

See `evaluation_matrix.md` for rationales.

## 8. Comparison With Baseline

A manual static baseline would require only an HTML file and browser: fewer dependencies, no accounts, and a much smaller attack/operations surface. It is superior for a one-off button. Loora's scenario required a Bun workspace but yielded a validated semantic tree plus HTML and React from the same source, and the broader code offers transactions, undo, branches/merge, components, responsive structure, and agent collaboration. That advantage becomes meaningful for repeated collaborative UI exploration, not simple static output. No timed human study was performed, so no percentage productivity claim is warranted.

## 9. Practical Use Cases

- **DevOps:** prototype deployment dashboards and approval interfaces, export one-way artifacts, and retain design branches. Do not confuse a visual approval control with an authorization control; connect exports to independently secured APIs.
- **AI engineering:** constrain agents to typed canvas operations rather than arbitrary source execution, review semantic trees/diffs, and export accepted output. Put MCP behind enterprise identity, per-user authorization, rate limits, and audit logging.
- **Cybersecurity integration:** model security-console UI and use branch review as a human checkpoint. Run in a segmented environment; restrict asset/image egress; scan exports; monitor MCP operations; rotate signing/internal tokens; and validate tenant isolation.

## 10. Limitations & Risks

This is one snapshot, one Linux host, no production credentials, and no live service stack. Upstream tests are evidence of implemented intent, not independent penetration tests. The custom scenario tests core libraries rather than wire-level MCP. Dependency audit output can contain transitive advisories whose reachability was not analyzed. Performance was not benchmarked under controlled repeated loads. No accessibility/usability assessment, SAST, container scan, fuzzing, SBOM/signature validation, or maintainer-process review was completed.

Operational risks include 1,242 installed packages, external processors, bearer-token handling, configuration-sensitive fallbacks, remote mutation authority, and AGPL obligations. Exported HTML intentionally includes inline runtime/style CSP permissions. Browser image export may make controlled fetches; enterprise egress policies should mediate it.

## 11. Recommendations

**Decision: Trial.** Do not broadly adopt yet; do not avoid outright.

1. Pin commit/images and generate an SBOM; triage all audit findings and the TypeScript dependency defect.
2. Create hermetic CI with DB service/fixtures, root tests, Rust tests, type check, build, secret scanning, SAST, dependency/container scanning, and reproducible artifacts.
3. Run live local-stack tests for object-level authorization, cross-tenant access, token replay/rotation, MCP tool scopes, rate-limit degradation, Redis outage, and egress.
4. Place MCP behind SSO/conditional access, least privilege, network segmentation, DLP, and immutable audit events. Require review before destructive or deployment-affecting actions.
5. Establish AGPL and external-processor review before hosted enterprise use.

## 12. Reproduction Guide

```bash
git clone https://github.com/lassejlv/loora.git
cd loora
git checkout 1ce827cbc1fe41db2f801fd3eddbe7503ab8f4ce
npm install --global bun@1.3.14
bun install --frozen-lockfile
bun run build
bunx tsc --noEmit
bun test --preload ./apps/web/src/test/setup.ts \
  packages/canvas/src packages/agent/src apps/mcp/src/auth.test.ts \
  apps/ws/src/config.test.ts apps/web/src/lib/sanitize.test.ts \
  packages/editor/src/lib/canvas-html-import.test.ts
cargo test -p loora-ws-server
bun audit
cp /path/to/research/loora-empirical-study/scripts/representative-scenario.ts .
bun representative-scenario.ts
```

Expect timing-dependent results to vary. Use `.env.example` and disposable local infrastructure—not production secrets—before attempting the full root suite/services.

## 13. Artifacts

`artifacts/` contains clone/install/build/typecheck/test/focused-test/Rust/audit/scenario logs. `scripts/representative-scenario.ts` is original reproducible evidence. No screenshots were created because no browser UI change or authenticated live UI was verified. No external repository copy or dependency tree is committed.

## 14. Appendix

### Evidence classification

- **Claimed:** explicitly attributed to README/docs.
- **Verified:** directly observed from command output or inspected code at the pinned commit.
- **Failed:** command/experiment did not meet acceptance criteria.
- **Unverified:** out of scope or blocked by infrastructure/credentials.
- **Inferred:** reasoned from architecture/tests, stated cautiously.

See `notes.md` for chronological command/failure notes, `notes/repo_recon.md` for reconnaissance, `sources.md` for accessed URLs, and `setup_log.md` for the host profile.
