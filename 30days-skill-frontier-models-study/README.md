# 基于 30Days-Skill 框架的 GLM-5.2 与 Anthropic Mythos/Fable 5 实证研究

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## Final conclusion

本次修订明确研究对象：第二条研究线是 **Anthropic Mythos/Fable 5**。`last30days-skill` 风格的 incremental evidence tracker 比一次性 desktop research 更适合这个问题，因为它保留 uncertainty、source lineage、contradiction checks 和 repeatable monitoring slots。

## Research question and scope

能否把 `mvanhorn/last30days-skill` 方法改造成 incremental research workflow，用来更深入地揭示 GLM-5.2 的真实工程边界，以及 Anthropic Mythos/Fable 5 export-control directive 对模型访问、供应链和合规架构的影响？

## Methods and sources

- 克隆并检查 `mvanhorn/last30days-skill`。
- 在 methodology repository 中运行 focused tests。
- 对 GLM-5.2 与 Anthropic Mythos/Fable 5 事件进行 current web research。
- 生成 baseline 与 30-interval tracking artifacts。

Primary source list is in `sources.md`.

## Verified findings

1. GLM-5.2 有可信公开 claims，包含 1M context、强 coding benchmarks、open weights 和 long-horizon engineering tasks。
2. GLM-5.2 工程现实必须考虑 KV-cache capacity、long-context kernels、CPU-side overhead、quota multipliers 和 anti-hack harness design。
3. Anthropic Mythos/Fable 5 访问暂停是 verified policy event，不是 unknown claim：Anthropic first-party statement 称美国政府 export-control directive 要求暂停 any foreign national access。
4. Anthropic 为合规而对所有客户关闭 Mythos 5/Fable 5，其他 Anthropic models 被声明为不受影响。
5. Incremental tracker 在 traceability、bias reduction、actionability 和 temporal robustness 上高于 baseline research。

## Produced evidence

- `artifacts/baseline_raw.json`
- `artifacts/incremental_tracking_schema.json`
- `artifacts/simulated_30_interval_log.csv`
- `notes/repo_recon.md`
- `experiment_plan.md`
- `evaluation_matrix.md`
- `research_report.md`

## Limitations and risks

- 未运行 live paid GLM API benchmark。
- Mythos/Fable 5 的具体 technical capability、closed eval details、government directive 全文和内部 compliance implementation 未公开。
- GLM-5.2 独立 operational data 在研究时仍然偏薄。

## Reproduction instructions

```bash
python3 30days-skill-frontier-models-study/scripts/generate_tracking_data.py
python3 -m json.tool 30days-skill-frontier-models-study/artifacts/baseline_raw.json >/tmp/baseline_check.json
```

For methodology repo verification, clone externally and run:

```bash
git clone --depth 1 https://github.com/mvanhorn/last30days-skill /tmp/last30days-recon/last30days-skill
cd /tmp/last30days-recon/last30days-skill
python3 -m pytest tests/test_skill_meta.py tests/test_version_consistency.py -q
```
