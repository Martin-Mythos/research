# Investigation Notes

## Original prompt
Empirically investigate whether https://github.com/yc-software/qm can efficiently orchestrate a Planner-Worker workflow in which a high-tier model plans five CSA 2.0 compliance tasks and a low-tier model with maximum thinking budget executes them concurrently; compare with Python asyncio and test failure behavior.

## Work log
- Created the required research directory and initial notes before reconnaissance.

## Sources and repository snapshot
- Cloned https://github.com/yc-software/qm at `7f2c916360f1797a8ff2a77ce2ce40c5fabab087`.
- Read README, SECURITY, LICENSE, root/package and CLI manifests/docs, getting-started docs, CI, task stores/tests, async queue utility, and Pi/OpenCode/Claude harness code/tests.
- Downloaded official Node 24.15.0 archive from nodejs.org to `/tmp`; it is not committed.

## Commands and outcomes
- Recorded OS/runtime/hardware in `artifacts/environment.txt`.
- `npm ci --ignore-scripts`: dependencies materialized but engine warnings showed host mismatch; final exit was not reliably preserved, so not claimed clean.
- `npx --package=node@24.15.0`: failed with cache `ENOENT`; abandoned in favor of official archive.
- Focused upstream memory task store test using Node 24.15: 4/4 passed.
- Custom JS experiment: smoke succeeded; five normal tasks all completed concurrently in ~81.67 ms; injected exception and timeout recovered on second attempts in ~170.95 ms.
- Python baseline: five normal tasks completed in ~81.30 ms.
- An `rg` command was initially run from the wrong directory and returned missing-path errors; rerun in `/tmp/qm-target` succeeded.

## Interpretation guardrails
QM's unmodified memory task store is genuinely used. The experiment owns `Promise.all`, mock calls, timeout, retry, aggregation, and `thinking_*` config metadata. Therefore it cannot verify native QM scheduling or provider application of those settings. No actual CSA framework text was assessed.

## Review follow-up (2026-08-02)
- Retrieved the Codex review comment from `https://api.github.com/repos/Martin-Mythos/research/pulls/30/comments`.
- The reviewer correctly observed that `Promise.race` did not cancel the losing worker, allowing a timed-out attempt to overlap its retry and making the original completion timing unsafe.
- Replaced the worker sleep with an abort-aware operation, propagated an `AbortSignal`, aborted on timeout, awaited the attempt with `Promise.allSettled` before retrying, and recorded `active_workers_after`.
- Regenerated `artifacts/qm_experiment.json`; normal and boundary runs both report zero active workers after aggregation. Deterministic assertions passed.
