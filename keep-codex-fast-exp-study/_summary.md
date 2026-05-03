This experimental study rigorously assesses the claims of the keep-codex-fast project, which promises faster Codex performance through local state maintenance. Testing covered all documented modes and maintenance actions, utilizing official smoke tests, parameter coverage, and micro-benchmarks with simulated environments. Results demonstrate full coverage and functional correctness, confirming that “speedup” refers to reducing local I/O, scanning, and indexing overhead—rather than direct improvement in model inference speed. The project's tools, such as its main script ([keep_codex_fast.py](https://github.com/vibeforge1111/keep-codex-fast)), operate safely and effectively, especially in long-term, heavy-use environments.

**Key Findings:**
- Default operation is read-only and safe; no risk of unintended data alteration.
- “apply” mode moves outdated sessions/worktrees out of hot paths, using backup-first strategy.
- Successfully mitigates common local slowdowns (large logs, dead configs, old sessions, path discrepancies).
- Script execution is fast; most slowdowns stem from file operations typical of maintenance.
- Actual perceived speedup depends on user history/usage scale, with primary benefits for heavy Codex users.
