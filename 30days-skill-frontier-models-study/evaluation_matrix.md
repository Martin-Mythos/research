# Evaluation Matrix

Scores use 1 = poor and 5 = strong.

| Dimension | Baseline Desktop Research | 30-Interval Skill-Enhanced Tracker | Evidence |
|---|---:|---:|---|
| Information Depth | 3 | 4 | Baseline found launch claims and policy-event reports. Tracker separated GLM benchmark/serving questions from Mythos/Fable directive scope, customer interruption, identity compliance, employee access, and sovereign-AI substitution. |
| Bias Reduction | 2 | 4 | Baseline is vulnerable to vendor launch framing and headline-level ban framing. Tracker forces contradiction checks, confidence labels, affected-access classes, and missing-data slots. |
| Evidence Traceability | 3 | 5 | Baseline raw JSON preserves sources. Tracker adds interval CSV and schema showing what was checked, what is verified, and what still requires follow-up. |
| Actionability for Cyber-Agents | 2 | 4 | Baseline gives narrative conclusions. Tracker maps concrete telemetry fields such as latency, context tokens, source count, affected access classes, and compliance confidence. |
| Temporal Robustness | 2 | 4 | Baseline is a snapshot from 2026-06-19. Tracker can be rerun to detect rollback, workaround, segmentation, policy clarification, or open-weight migration signals. |

## Verdict

The skill-enhanced tracker is more useful for frontier-model and restricted-model analysis because it makes uncertainty and policy scope explicit. Its most important output is not a stronger one-time answer, but a reusable evidence ledger that shows which claims are confirmed, contradicted, or still require monitoring.
