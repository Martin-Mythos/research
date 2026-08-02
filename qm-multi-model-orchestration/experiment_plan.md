# Experiment Plan

## Question and controls
Test whether QM revision `7f2c916360f1797a8ff2a77ce2ce40c5fabab087` exposes an efficient Planner–Worker path without real providers. No credentials or production services are used. “CSA 2.0” is only the supplied mock audit label; outputs are synthetic and are not legal/compliance advice.

## Tests
1. **Smoke:** install dependencies, import QM's `createMemoryTaskStore`, create a `Hello World` task, and transition pending → in_progress → completed.
2. **Planner–Worker:** deterministic high-tier mock returns five distinct checks. Five low-tier mock calls start together through a small dispatcher, each configured with `thinking_effort: max` and `thinking_budget: high`. QM's store records task/event state; `Promise.all` aggregates results. Record elapsed time and start spread.
3. **Boundary:** inject a first-attempt exception in one worker and a first-attempt timeout in another. Cancel the timed-out attempt with `AbortController`, await its cleanup before retrying, use two attempts, aggregate all outcomes, and inspect state/events. Assert that the active-worker count is zero before recording completion. Important control: the timeout/retry policy belongs to this harness, not QM's `TaskStore`.
4. **Baseline:** run equivalent delays with Python `asyncio.gather()`.

## Interpretation
A successful store-backed harness proves QM primitives can track concurrent work; it does **not** prove the QM CLI dispatches arbitrary task arrays, that actual model subagents use heterogeneous models, or that QM itself retries task failures. Compare timings descriptively from one mock run only; do not call it a performance benchmark.
