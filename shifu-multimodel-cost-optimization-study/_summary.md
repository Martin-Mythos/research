The research assesses the `vikingmute/shifu` framework, focusing on its purported multi-model dispatching and cost optimization capabilities. Through local mock testing and static code review, Shifu is verified as an Agent Skill centered on markdown-based instruction orchestration, rather than a fully automated multi-model API router. The framework facilitates strong (expensive) model planning and weaker (cheaper) model execution via readable `SKILL.md` specifications, but lacks built-in endpoint configuration, real model cost tracking, token accounting, and error recovery control flows. Significant simulated cost savings (over 70%) are observed in mock harness tests, but these results depend on manual orchestration and cannot be attributed to Shifu's out-of-the-box abilities.

Key findings:
- Shifu installs as an Agent Skill via `npx skills add vikingmute/shifu`, but does not provide a runnable dispatch runtime.
- The core features are clear planning specs, execution gates, and prompt injection warnings in markdown.
- No built-in model API clients, cost telemetry, or automatic error loop exist; orchestration must be handled by the agent, not Shifu itself.
- Cost optimization relies on external agent logic and proper task decomposition, not Shifu’s intrinsic codebase.

Relevant links:
- [Shifu GitHub Repository](https://github.com/vikingmute/shifu)
- [SKILL.md Example](https://github.com/vikingmute/shifu/blob/main/skills/shifu/SKILL.md)
