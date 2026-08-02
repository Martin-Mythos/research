# Run Log

## Installation
- Cloned upstream successfully; saved `artifacts/clone.log`.
- Host Node 20.20.2/npm 11.4.2 did not meet root engines (Node >=24.15/npm >=11.10). `npm ci --ignore-scripts` emitted `EBADENGINE`; dependencies nevertheless materialized, but the command's final status was not captured, so installation is classified **partial/uncertain**, not verified clean.
- `npx --package=node@24.15.0` failed with an npm cache `ENOENT`. Abandoned that path.
- Downloaded the official Node 24.15.0 binary to `/tmp` and verified `v24.15.0`. The binary is intentionally not committed.

## Upstream verification
`/tmp/node24/bin/node --experimental-test-module-mocks --test test/task-store.test.ts` passed 4/4 tests (artifact log retained).

## Custom experiments
`/tmp/node24/bin/node scripts/qm_planner_worker.mjs --qm-repo /tmp/qm-target` produced `artifacts/qm_experiment.json`:
- smoke task reached `completed`;
- normal 5-task run: all completed; elapsed 80.39 ms; starts were tightly grouped (see JSON);
- injected failure/timeout: both affected tasks completed on attempt 2; total 172.23 ms; unrelated tasks completed; aggregation did not halt;
- the timeout aborts the first attempt and awaits its settlement before retrying; both runs recorded `active_workers_after: 0`.

This behavior combines the genuine QM in-memory task/event store with experiment-owned concurrency, timeout, retry, worker mock, and aggregation. It is not evidence of native QM retry.

`python3 scripts/asyncio_baseline.py` produced `artifacts/asyncio_baseline.json`: five tasks completed in 81.30 ms. One run with deterministic sleeps is a functional comparison only; the roughly 0.91 ms difference from the regenerated QM-backed run is noise/overhead and not a meaningful speed claim.
