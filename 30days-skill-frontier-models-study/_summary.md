This research project adapted the `mvanhorn/last30days-skill` framework into an incremental evidence tracking workflow to empirically assess GLM-5.2’s engineering boundaries and the compliance impacts of the Anthropic Mythos/Fable 5 export-control directive. By systematically cloning, testing, and monitoring, the study compared baseline and interval tracking, revealing that incremental research provides superior traceability and actionable outcomes over traditional, static approaches. Key validated findings were drawn from primary sources and artifacts, while notable limitations included lack of live API benchmarks and incomplete visibility into Mythos/Fable 5’s technical details and compliance procedures. The project’s methodology and evidence artifacts are available for reproduction and verification.

**Key findings:**
- GLM-5.2 features verified public claims, including 1M context support, robust coding benchmarks, open weights, and advanced engineering use cases.
- Real-world engineering for GLM-5.2 requires awareness of KV-cache and context kernel limits, CPU overhead, quota, and anti-hack infrastructure.
- Anthropic Mythos/Fable 5 access was officially suspended, per US export-control policy; other Anthropic models remain unaffected.
- Incremental tracking improves traceability, bias reduction, actionability, and temporal robustness compared to baseline research.

For methodology and tooling, see [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill).
