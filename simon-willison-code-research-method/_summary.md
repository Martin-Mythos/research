Simon Willison's AI research repo method transforms research questions into reproducible, reviewable code workflows using dedicated GitHub repositories. Instead of relying on chat-based AI summaries, he assigns clear, executable tasks to asynchronous coding agents (such as Claude Code or Codex Cloud), which install dependencies, collect data, run experiments, and generate reports—all documented through pull requests or commits. This approach compresses AI output into verifiable code, tests, benchmarks, and artifacts, making it easier to review, reproduce, and accumulate long-term research compared to ephemeral chat answers. The workflow is explicitly documented in his [article](https://simonwillison.net/2025/Nov/6/async-code-research/) and implemented in the [`simonw/research`](https://github.com/simonw/research) repository, emphasizing transparency and dedicated environments to reduce risk.

**Key findings:**
- Dedicated repositories allow safe network access by isolating research from production code and sensitive assets.
- Each research project is a single directory containing scripts, notes, results, and a final README, facilitating reproducibility and review.
- Automated GitHub Actions maintain project summaries and indexes, ensuring easy navigation and context for agents.
- The method relies on human review prior to publication to mitigate risks of AI-generated errors, supply chain attacks, or misleading conclusions.
- Research results should be treated as lab notebooks, not finalized publications, until manually verified.
