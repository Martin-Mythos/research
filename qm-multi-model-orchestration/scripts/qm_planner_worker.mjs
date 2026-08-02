#!/usr/bin/env node
import { performance } from "node:perf_hooks";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";

const args = Object.fromEntries(process.argv.slice(2).map((v, i, a) => v.startsWith("--") ? [v.slice(2), a[i + 1] ?? true] : []).filter(Boolean));
const qmRepo = resolve(String(args["qm-repo"] ?? "/tmp/qm-target"));
const { createMemoryTaskStore } = await import(pathToFileURL(resolve(qmRepo, "src/tasks/memory-task-store.ts")));
const workerConfig = { model: "mock-low-tier-terra-lula", thinking_effort: "max", thinking_budget: "high", timeout_ms: 120, max_attempts: 2 };
const checks = [
  "Check security event logging configuration",
  "Verify encryption at rest",
  "Review incident notification workflow",
  "Validate access-control and least-privilege evidence",
  "Assess cybersecurity risk-management documentation",
];
const planner = async () => ({ model: "mock-high-tier-planner", tasks: checks });
let activeWorkers = 0;

function abortableSleep(ms, signal) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(resolve, ms);
    signal.addEventListener("abort", () => {
      clearTimeout(timer);
      reject(signal.reason);
    }, { once: true });
  });
}

async function worker(title, attempt, injectFailure, signal) {
  activeWorkers++;
  try {
    const delays = { [checks[0]]: 80, [checks[1]]: 60, [checks[2]]: 40, [checks[3]]: 70, [checks[4]]: 50 };
    if (injectFailure && title === checks[2] && attempt === 1) throw new Error("injected worker failure");
    if (injectFailure && title === checks[4] && attempt === 1) await abortableSleep(workerConfig.timeout_ms + 80, signal);
    else await abortableSleep(delays[title], signal);
    return { check: title, verdict: "mock-review-required", evidence: [], worker_config: workerConfig };
  } finally {
    activeWorkers--;
  }
}

async function withTimeout(operation, ms) {
  const controller = new AbortController();
  const work = operation(controller.signal);
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => {
      const error = new Error("worker timeout");
      controller.abort(error);
      reject(error);
    }, ms);
  });
  try {
    return await Promise.race([work, timeout]);
  } finally {
    clearTimeout(timer);
    controller.abort(new Error("attempt finished"));
    await Promise.allSettled([work]);
  }
}

async function dispatch(injectFailure = false) {
  const store = createMemoryTaskStore();
  const plan = await planner();
  const started = performance.now();
  const starts = [];
  const jobs = plan.tasks.map(async (title, index) => {
    const task = await store.create({ id: `task-${index + 1}`, sessionId: "csa-audit", originRunId: "planner-1", title });
    await store.transitionStatus(task.id, "pending", "in_progress", `worker-${index + 1}`);
    starts.push({ id: task.id, offset_ms: performance.now() - started });
    let lastError;
    for (let attempt = 1; attempt <= workerConfig.max_attempts; attempt++) {
      try {
        const result = await withTimeout(signal => worker(title, attempt, injectFailure, signal), workerConfig.timeout_ms);
        await store.transitionStatus(task.id, "in_progress", "completed", `worker-${index + 1}`);
        return { id: task.id, status: "completed", attempts: attempt, result };
      } catch (error) { lastError = error; }
    }
    await store.transitionStatus(task.id, "in_progress", "failed", `worker-${index + 1}`);
    return { id: task.id, status: "failed", attempts: workerConfig.max_attempts, error: lastError.message };
  });
  const results = await Promise.all(jobs);
  return { implementation: "QM MemoryTaskStore + experiment dispatcher", injectFailure, workerConfig, elapsed_ms: performance.now() - started, start_spread_ms: Math.max(...starts.map(x => x.offset_ms)) - Math.min(...starts.map(x => x.offset_ms)), active_workers_after: activeWorkers, starts, results, tasks: await store.list(), events: Object.fromEntries(await Promise.all(results.map(async r => [r.id, await store.listEvents(r.id)]))) };
}

const smokeStore = createMemoryTaskStore();
const smoke = await smokeStore.create({ id: "hello", sessionId: "smoke", originRunId: "smoke-run", title: "Hello World" });
await smokeStore.transitionStatus(smoke.id, "pending", "in_progress", "mock-worker");
await smokeStore.transitionStatus(smoke.id, "in_progress", "completed", "mock-worker");
console.log(JSON.stringify({ smoke: { output: "Hello World", task: await smokeStore.get("hello") }, success: await dispatch(false), boundary: await dispatch(true) }, null, 2));
