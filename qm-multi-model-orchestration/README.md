# Empirical Study of QM for Heterogeneous Multi-Model Task Orchestration

This self-contained research project evaluates `yc-software/qm` at commit `7f2c916360f1797a8ff2a77ce2ce40c5fabab087` against a mocked Planner–Worker CSA 2.0 audit scenario.

## Final conclusion
**Reference/Revisit.** QM's genuine task store successfully tracked five concurrent mock jobs, but the experiment—not QM—provided dispatch, retry, timeout, and aggregation. A native heterogeneous high-tier-planner/low-tier-worker workflow with per-worker maximum thinking was not verified. The Python baseline matched the mock wall time with much less machinery.

## Evidence map
- Full 14-section report: [`research_report.md`](research_report.md)
- Reconnaissance: [`notes/repo_recon.md`](notes/repo_recon.md)
- Planned controls: [`experiment_plan.md`](experiment_plan.md)
- Commands/outcomes: [`run_log.md`](run_log.md), [`setup_log.md`](setup_log.md), [`notes.md`](notes.md)
- Rubric: [`evaluation_matrix.md`](evaluation_matrix.md)
- Reproducible scripts: [`scripts/`](scripts/)
- Raw outputs/logs: [`artifacts/`](artifacts/)
- Sources: [`sources.md`](sources.md)

## Verified versus unknown
Verified: focused QM task-store tests pass on Node 24; Hello World reaches completed; five custom-dispatched mocks run concurrently and are recorded; injected first-attempt failure/timeout recover under the harness policy. Unknown: full deployment, real providers, native task retry, native arbitrary array dispatch, actual heterogeneous model selection, thinking parameter transmission, Postgres behavior, and scale.

## Quick reproduction
Clone the pinned QM revision to `/tmp/qm-target`, use Node >=24.15, then run:
```bash
node scripts/qm_planner_worker.mjs --qm-repo /tmp/qm-target
python3 scripts/asyncio_baseline.py
```
Run from this directory, or use the paths in `research_report.md` from repository root.
