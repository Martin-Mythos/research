# Notes

## Original prompt / research question
Martin requested an empirical open-research project using `mvanhorn/last30days-skill` as a methodology base to compare one-off desktop research against an adapted incremental 30-interval quantitative research workflow for two hard-tech topics: GLM-5.2 engineering performance vs leaderboard claims, and the status/evolution of a claimed U.S. government ban on Anthropic Mythos/Fable 5-class models.

## Work log

### Commands started
- `cat /workspace/research/.agents/skills/open-research/SKILL.md && pwd && find .. -name AGENTS.md -print` — read open-research skill and located repo instructions.
- `find . -maxdepth 2 -type d | sort | head -100` — checked existing top-level directories.
- `mkdir -p 30days-skill-frontier-models-study/{notes,scripts,artifacts}` — created research directory structure.

### Sources and URLs actually used
- https://github.com/mvanhorn/last30days-skill
- https://huggingface.co/blog/zai-org/glm-52-blog
- https://docs.z.ai/guides/llm/glm-5.2
- https://benchlm.ai/models/glm-5-2
- https://friendli.ai/blog/GLM-5.2
- https://www.anthropic.com/news/fable-mythos-access

### Experiments and outcomes
- Cloned methodology repo successfully into `/tmp/last30days-recon/last30days-skill`.
- Ran `python3 -m pytest tests/test_skill_meta.py tests/test_version_consistency.py -q`: 10 tests passed.
- Generated `artifacts/baseline_raw.json`, `artifacts/incremental_tracking_schema.json`, and `artifacts/simulated_30_interval_log.csv`.

### Failed paths / abandoned paths
- Did not run paid GLM API latency tests because no paid credentials or production API usage were allowed by the task constraints.
- Did not treat Anthropic Mythos/Fable 5 as verified because public web searches did not identify credible direct evidence for that model name or ban.

### Revision after review
- User clarified the restricted-model research target is Anthropic Mythos/Fable 5, not Astropica/Fiber-5.
- Updated report language to Chinese while preserving English technical terms.
- Replaced negative-evidence framing with verified Anthropic Mythos/Fable 5 policy-event framing.
- Added/corrected sources: Anthropic first-party statement, GT Law legal analysis, Al Jazeera coverage, and The Hacker News coverage.
- Regenerated `artifacts/baseline_raw.json`, `artifacts/incremental_tracking_schema.json`, and `artifacts/simulated_30_interval_log.csv` with corrected Mythos/Fable vectors.

### Revision verification commands
- `python3 30days-skill-frontier-models-study/scripts/generate_tracking_data.py` — regenerated corrected artifacts.
- `python3 -m json.tool 30days-skill-frontier-models-study/artifacts/baseline_raw.json >/tmp/baseline_check.json` — validated baseline JSON.
- `python3 -m json.tool 30days-skill-frontier-models-study/artifacts/incremental_tracking_schema.json >/tmp/schema_check.json` — validated schema JSON.
- `git diff --check` — passed after changing CSV writer to LF line endings.
