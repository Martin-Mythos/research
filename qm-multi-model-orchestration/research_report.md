# Empirical Study of QM for Heterogeneous Multi-Model Task Orchestration

## 1. Executive Summary
**Conclusion: Reference/Revisit.** QM can supply durable-style task state abstractions and its harness adapters recognize subagent activity, but this investigation did not verify a native API/CLI that takes a planner-produced array, dispatches each item concurrently to a separately configured low-tier model, applies maximum thinking effort, retries failures, and aggregates results. A custom mock dispatcher using QM's real `MemoryTaskStore` completed five jobs concurrently, but Python `asyncio.gather()` did the same with virtually identical mock wall time and far less platform machinery. Do not interpret the harness result as native QM orchestration.

## 2. Project Overview
QM is an early-stage, MIT-licensed TypeScript organizational agent platform for Slack/web, scoped workspaces, background work, multiple harnesses, and deployment into operator infrastructure. Its CLI deploys services; it is not a task-dispatch runtime. The inspected revision is `7f2c916360f1797a8ff2a77ce2ce40c5fabab087`.

## 3. Research Questions
Primary: can QM efficiently orchestrate a high-tier Planner and concurrent low-tier Workers at maximum thinking budget? Subsidiary questions: does it install and track Hello World, what does failure do, and what benefit appears over `asyncio.gather()`?

## 4. Experiment Design
A deterministic planner emits five illustrative CSA 2.0 cybersecurity checks. Mock workers carry both `thinking_effort: "max"` and `thinking_budget: "high"`, wait 40–80 ms, and return synthetic “review required” records. The QM-backed harness creates/transitions genuine QM memory-store tasks, runs jobs with `Promise.all`, and aggregates. A boundary run injects one exception and one timeout; `AbortController` cancels the timed-out attempt and the dispatcher awaits its cleanup before retrying. A Python baseline uses identical normal delays. See `experiment_plan.md`.

## 5. Setup & Execution Evidence
Ubuntu 24.04.4, x86_64, 3 CPUs, ~17 GiB RAM, Python 3.12.13, host Node 20.20.2, and npm 11.4.2 were recorded. Upstream requires Node >=24.15/npm >=11.10. Dependency installation emitted engine warnings. An official Node 24.15 binary enabled a focused upstream test: all four memory-task-store cases passed. No keys or remote services were used.

The smoke task transitioned `pending → in_progress → completed`. The regenerated normal five-task experiment finished all tasks in 80.39 ms, versus 81.30 ms for the original Python artifact. Start offsets in the raw JSON show jobs were initiated in a tight cluster; elapsed time close to the longest 80 ms sleep is consistent with concurrency. This is one deterministic run, not a statistically valid benchmark.

## 6. Findings
### Verified
- QM's in-memory task store supports task creation, status listing, event history, and compare-and-set transitions; upstream's four focused tests passed.
- The custom QM-store-backed experiment tracked five concurrently started mock tasks and collected all results.
- Both injected first-attempt problems recovered on attempt two without halting unrelated tasks—because the experiment explicitly implemented cancellation, timeout/retry, and all-result aggregation. The dispatcher awaited timed-out work cleanup and recorded zero active workers at the end of both runs.
- Static code includes harness adapter support for subagent task events and turn-level model/thinking settings.

### Failed
- `npx --package=node@24.15.0` failed with npm-cache `ENOENT`.
- The host runtimes did not satisfy declared engines; dependency installation was not verified as a clean supported install.

### Unverified
- Full local QM service/deployment, Postgres queue behavior, actual model calls, five real harness subagents, heterogeneous planner/worker model assignment, provider transmission of maximum thinking, native task retry, resource usage, and behavior at scale.

### Surprising
The `TaskStore` is primarily a status/event ledger: its task schema lacks execution payload, result, model, effort, attempt, deadline, and worker fields. The selected harness—not the store—appears to own subagent execution.

### Cautious inference
Because harness adapters expose subagents and turn settings, a production workflow may be buildable by prompting/configuring a supported harness or adding an orchestration layer. The inspected documentation/code did not establish the exact heterogeneous per-worker contract requested.

## 7. Evaluation Matrix
Scores: Installability 2/5; Documentation 2/5; Concurrency Reliability 3/5; Error Handling 2/5; R&D Agility 2/5; Reproducibility 4/5; overall arithmetic mean 2.5/5. Full rationales are in `evaluation_matrix.md`.

## 8. Comparison With Baseline
| Implementation | Normal elapsed | What it proves |
|---|---:|---|
| QM `MemoryTaskStore` + custom JS dispatcher | 80.39 ms | QM can record states/events around external concurrent control. |
| Python `asyncio.gather()` | 81.30 ms | The mock concurrency itself needs little code/infrastructure. |

The roughly 0.91 ms difference between separately captured runs is not meaningful. QM adds state transitions/event provenance and broader platform facilities; baseline is clearer for an isolated batch. No throughput, costs, model quality, or persistent-queue comparison was measured.

## 9. Practical Use Cases
Potentially useful: human-visible audit research split into evidence collection, encryption, logging, incident notification, and access-control reviews; scoped workspaces and audit events could support collaboration. However, mock verdicts are not CSA findings. For real cybersecurity work, preserve evidence provenance, require human validation, constrain credentials/egress, and map checks to authoritative framework clauses.

## 10. Limitations & Risks
No real CSA corpus, model, provider, database, Docker deployment, Slack surface, or cloud worker was exercised. Synthetic sleeps favor both implementations. The project warns that command policy is bypassable, sandbox credentials are plaintext while used, content screening and egress coverage have gaps, request captures may persist, and admins may read sensitive content. These risks matter for audit data. Upstream changed recently; results are SHA-specific.

## 11. Recommendations
- **Current disposition: Reference/Revisit**, not Adopt for this narrow requirement.
- Trial only after demonstrating a supported per-subagent model/effort configuration and QM-owned retry/timeout contract.
- Use `asyncio` or another small queue for a narrow batch unless QM's multi-user scopes, audit, surfaces, and durable sandboxes are independently required.
- Before cybersecurity use, threat-model credentials, retention, provider data flow, scope access, and evidence integrity.

## 12. Reproduction Guide
```bash
git clone https://github.com/yc-software/qm.git /tmp/qm-target
git -C /tmp/qm-target checkout 7f2c916360f1797a8ff2a77ce2ce40c5fabab087
# Use Node 24.15.0 or newer supported runtime.
node qm-multi-model-orchestration/scripts/qm_planner_worker.mjs --qm-repo /tmp/qm-target \
  > qm-multi-model-orchestration/artifacts/qm_experiment.json
python3 qm-multi-model-orchestration/scripts/asyncio_baseline.py \
  > qm-multi-model-orchestration/artifacts/asyncio_baseline.json
cd /tmp/qm-target
node --experimental-test-module-mocks --test test/task-store.test.ts
```
Outputs contain timing variance; statuses, attempt counts, and task count should remain deterministic.

## 13. Artifacts
- `scripts/qm_planner_worker.mjs`: planner, worker config, dispatcher, timeout/retry, aggregator.
- `scripts/asyncio_baseline.py`: comparison.
- `artifacts/qm_experiment.json`, `asyncio_baseline.json`: raw results.
- `artifacts/environment.txt`, `clone.log`, `npm-ci-node20.log`, `upstream-task-store-test.log`: setup/test evidence.

## 14. Appendix
Terminology: “QM-backed” means the script imports QM's unmodified memory task store. “Native QM dispatch” would require QM itself to schedule/execute the five payloads; that was not demonstrated. The checks are illustrative labels and not a validated representation of Singapore's Cybersecurity Act or any certification framework.
