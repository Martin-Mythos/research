# Evaluation Matrix

Scores use 1 (poor) to 5 (excellent) for the pinned snapshot and this constrained local evaluation.

| Dimension | Score | Evidence-based rationale |
|---|---:|---|
| Installability | 3 | Frozen install succeeded with exact Bun after the official installer returned 403. Production build passed without service credentials, but a useful full runtime needs DB/auth configuration. |
| Documentation quality | 4 | README is concise and `AGENTS.md` is unusually detailed about architecture, invariants, commands, and controls. A new operator still lacks a turnkey local stack/CI workflow. |
| Core functionality | 4 | Custom agent→transaction→semantic-tree→HTML/React flow passed; 168/169 focused tests passed. Hosted collaboration, live MCP end-to-end, PNG/desktop, and external integrations were not verified. |
| Cybersecurity posture | 3 | Strong local evidence for validation, sanitization, auth failure, signed tickets, limits, and least-privilege containers. Complexity, external processors, in-memory fallbacks, inline export CSP allowances, and audit findings prevent a higher score. |
| R&D agility | 4 | One typed operation produced structured, inspectable, exportable UI in multiple formats; branches/merge are well tested upstream. Operational setup and no two-way source sync constrain adoption. |
| Experiment reproducibility | 4 | Commit, environment, commands, logs, and custom script are retained. Timing gate was hardware-sensitive and full services require credentials/infrastructure not reproduced here. |

**Overall (unweighted): 3.7/5.** This supports a controlled trial, not production approval.
