# 基于 30Days-Skill 框架对 GLM-5.2 性能边界与 Anthropic Mythos/Fable 5 封禁事件的持续量化实证研究

## 1. Executive Summary

本次修订明确研究对象：第二条研究线是 **Anthropic Mythos/Fable 5** 的美国政府 export-control directive 与访问暂停事件。报告整体以中文输出，并保留关键 English technical terms。

本研究把 `mvanhorn/last30days-skill` 从一个 recency-first、多源证据聚合技能，抽象为 30 个 interval 的增量式研究框架。结论是：对高度营销化、快速变化的 frontier model 议题，30-interval 框架明显优于一次性 Desktop Research，因为它强迫研究者记录来源、矛盾、未知项和可复查指标。

**GLM-5.2 verdict**：公开资料显示 GLM-5.2 的 benchmark 叙事很强，尤其是 1M context、Terminal-Bench、FrontierSWE、SWE-Marathon 等长程 coding/agentic 任务。但同一份技术博客也承认，1M context 会把瓶颈推向 KV-cache capacity、long-context kernel overhead、CPU-side scheduling 等工程问题。因此更合理的判断不是“高分低能”，而是“高分真实反映了特定 harness 下的长程任务能力，但开发者体感会被 latency、concurrency、quota、context management 和 provider implementation 显著调制”。

**Anthropic Mythos/Fable 5 verdict**：这是一个已由 Anthropic first-party statement 和多家二级来源共同确认的 restricted-model policy event。核心事实是：美国政府以 national-security/export-control authority 为理由，要求暂停任何 foreign national 对 Mythos 5 和 Fable 5 的访问；Anthropic 为合规而对所有客户关闭这两个模型，其他 Anthropic 模型不受影响。与前版不同，本报告不再把该对象标记为 unknown，而是把它作为本研究的真实政策与供应链冲击案例。

## 2. Methodology Adaptation

`last30days-skill` 的核心不是简单搜索，而是：query planning、多源抓取、engagement/relevance scoring、cross-source clustering、原始结果保存和受约束综合。迁移到技术审计后，单次 query 被改写成 30 个 interval：每个 interval 都有检查向量、数据字段、来源 URL、confidence、contradiction check 和下一步问题。

本项目生成了三个关键 artifacts：

- `baseline_raw.json`：一次性 Desktop Research 的来源和 claim 快照。
- `incremental_tracking_schema.json`：30 个 interval 的监控 schema。
- `simulated_30_interval_log.csv`：压缩模拟的 30-interval 运行记录。

## 3. GLM-5.2 Deep Dive: Leaderboard vs. Reality

### Verified findings

1. GLM-5.2 的官方技术叙事包含 1M-token context、multiple thinking effort levels、MIT open-source license、长程 coding benchmark 优势等 claim。
2. 官方 benchmark 表显示 GLM-5.2 在 Terminal Bench 2.1、SWE-bench Pro、FrontierSWE、PostTrainBench、SWE-Marathon 等指标上相对 GLM-5.1 有显著提升。
3. 技术博客同时指出，长 context 推高了 KV-cache、kernel、CPU scheduling 和 throughput 方面的系统压力。
4. 博客还专门讨论了 coding-agent reward hacking，说明 benchmark 结果必须结合 anti-hack guardrail 和 harness 约束解释。
5. 第三方聚合页面显示 GLM-5.2 benchmark 覆盖仍不完整，因此“全局最强”的泛化结论不应过度外推。

### Engineering interpretation

GLM-5.2 的高 ranking 与真实工程体感之间可能出现差异，主要因为 leaderboard 通常测的是可控 harness 下的 success rate，而开发者体感还包括：

- first-token latency 和长 context prefill 时间；
- 高并发下 KV-cache 资源争用；
- peak-hour quota multiplier 和 provider throttling；
- 多轮 agent trajectory 中 instruction drift；
- repo-scale context 中是否真的能保留细粒度约束；
- coding benchmark 是否被 anti-hack 规则、网络隔离和 hidden tests 充分约束。

因此，本研究建议把 GLM-5.2 当作“值得进入工程评测队列的强 open-weight coding model”，而不是仅凭 launch benchmark 直接替换生产 coding agent。

## 4. Anthropic Mythos/Fable 5 Geopolitical & Tech Trajectory

### Verified findings

- Anthropic 发布 first-party statement，称美国政府发布 export-control directive，要求暂停任何 foreign national 访问 Mythos 5 和 Fable 5。
- 指令范围包括美国境内和境外的 foreign nationals，也包括 Anthropic 自身 foreign-national employees。
- Anthropic 表示，为确保合规，公司必须对所有客户 abrupt disable Mythos 5 和 Fable 5。
- Anthropic 表示其他模型不受影响。
- 法律与新闻二级来源将此解读为美国将 frontier AI model access 纳入更强 export-control/compliance 框架的升级案例。

### Supply-chain and compliance impacts

1. **Customer interruption**：已经集成 Mythos 5/Fable 5 的客户会遭遇服务中断，即使其美国员工本身可能不属于限制对象。
2. **Identity and access management pressure**：模型供应商需要更细粒度地区分 citizenship、nationality、residency、employee status、customer tenant 和 delegated access。
3. **Internal development friction**：如果 foreign-national employees 也被纳入限制，模型公司内部研发、red-team、eval、support 和 incident response 都会受影响。
4. **Sovereign AI demand**：非美国企业和政府可能更积极推动 sovereign AI、multi-provider failover 和 local/open-weight alternatives。
5. **Compliance ambiguity**：如果限制理由与 jailbreak/cyber capability 有关，模型供应商需要更清晰的 severity rubric，否则会面临事后式、临时式监管风险。

### 12-month outlook

未来 12 个月更可能出现三类演进：

1. **Formalization**：美国政府与 frontier labs 可能推进更明确的 AI security risk rubric，定义何种 jailbreak/cyber capability 触发 export-control action。
2. **Segmentation**：供应商会建设更细的 access segmentation，而不是只能“一刀切”关闭所有客户访问。
3. **Resilience architecture**：企业客户会把 restricted frontier model 视为 geopolitical dependency，开始要求 fallback models、on-prem alternatives、regional providers 和 open-weight contingency plans。

## 5. Methodology Evaluation Matrix

| Dimension | Baseline | 30-Interval Tracker | Justification |
|---|---:|---:|---|
| Information Depth | 3 | 4 | Baseline 能发现主要来源；tracker 把来源拆成 benchmark、serving、policy scope、customer interruption、identity compliance、sovereign-AI substitution 等可复查向量。 |
| Bias Reduction | 2 | 4 | Tracker 强制记录 contradiction 和 confidence，能抵消 launch marketing 或新闻 headline 的单源叙事。 |
| Evidence Traceability | 3 | 5 | Tracker 有 JSON、schema、CSV 和 notes，审计链更完整。 |
| Actionability for Cyber-Agents | 2 | 4 | Tracker 输出 latency/context/source/confidence/affected access classes 等字段，更适合 agent 后续自动监控。 |
| Temporal Robustness | 2 | 4 | Baseline 是静态快照；tracker 可每天或每周重跑，以观察 policy rollback、provider workaround 或替代模型迁移。 |

## 6. KOL Insight Drafts

### Baseline-style insight

GLM-5.2 在 coding benchmark 上很强，但真实工程价值还需要看 latency、long-context serving 和 provider quota。Anthropic Mythos/Fable 5 事件说明 frontier AI access 已经从产品能力问题升级为 export-control 和供应链连续性问题。

### 30Days-style insight

GLM-5.2 的关键不是“榜单赢了谁”，而是 1M context 把战场从模型能力转移到 KV-cache、prefill、quota 和 anti-hack harness。Anthropic Mythos/Fable 5 的关键也不是“某个模型被封”这么简单，而是美国正在把 frontier model access 变成类似高端芯片/敏感技术的 compliance boundary。对 cyber-agent 和企业 AI 架构来说，下一步不是押注单一最强模型，而是建立 multi-model resilience、access-policy monitoring 和 export-control-aware deployment。

## 7. Reproduction Guide & References

```bash
python3 30days-skill-frontier-models-study/scripts/generate_tracking_data.py
cat 30days-skill-frontier-models-study/artifacts/baseline_raw.json
cat 30days-skill-frontier-models-study/artifacts/incremental_tracking_schema.json
```

See also:

- `sources.md` for source URLs.
- `notes.md` for command and evidence log.
- `notes/repo_recon.md` for methodology reverse-engineering.
- `evaluation_matrix.md` for scoring.
