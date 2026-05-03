# Research projects carried out with AI tools

This repository is a dedicated workspace for code research and web research projects carried out with AI coding agents such as Codex, Claude Code, Jules, or GitHub Copilot coding agent.

Each top-level directory is one separate investigation. Reports should include enough notes, scripts, sources, and verification evidence for a reviewer to understand what was tested and how conclusions were reached.

The operating model is inspired by Simon Willison's article [Code research projects with async coding agents like Claude Code and Codex](https://simonwillison.net/2025/Nov/6/async-code-research/) and his public [`simonw/research`](https://github.com/simonw/research) repository.

Prompts, transcripts, and important review context should be linked from pull requests or commits whenever possible.

Jules environment setup guidance is documented in [docs/jules-environment.md](docs/jules-environment.md).

*Times shown are in UTC.*

<!--[[[cog
import os
import re
import subprocess
import pathlib
from datetime import datetime, timezone

MODEL = "github/gpt-4.1"

research_dir = pathlib.Path.cwd()
subdirs_with_dates = []

for d in research_dir.iterdir():
    if d.is_dir() and not d.name.startswith("."):
        try:
            result = subprocess.run(
                ["git", "log", "-1", "--format=%aI", "--", d.name],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0 and result.stdout.strip():
                date_str = result.stdout.strip()
                commit_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            else:
                commit_date = datetime.fromtimestamp(d.stat().st_mtime, tz=timezone.utc)
        except Exception:
            commit_date = datetime.fromtimestamp(d.stat().st_mtime, tz=timezone.utc)
        subdirs_with_dates.append((d.name, commit_date))

print(f"## {len(subdirs_with_dates)} research projects\n")

subdirs_with_dates.sort(key=lambda x: x[1], reverse=True)

for dirname, commit_date in subdirs_with_dates:
    folder_path = research_dir / dirname
    readme_path = folder_path / "README.md"
    summary_path = folder_path / "_summary.md"

    date_formatted = commit_date.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M")

    github_url = None
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            timeout=2,
        )
        if result.returncode == 0 and result.stdout.strip():
            origin = result.stdout.strip()
            if origin.startswith("git@github.com:"):
                origin = origin.replace("git@github.com:", "https://github.com/")
            if origin.endswith(".git"):
                origin = origin[:-4]
            github_url = f"{origin}/tree/main/{dirname}"
    except Exception:
        pass

    title = dirname
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            for readme_line in f:
                if readme_line.startswith("# "):
                    title = readme_line[2:].strip()
                    break

    if github_url:
        print(f"### [{title}]({github_url}#readme) ({date_formatted})\n")
    else:
        print(f"### {title} ({date_formatted})\n")

    if summary_path.exists():
        description = summary_path.read_text(encoding="utf-8").strip()
        print(description or "*No description available.*")
    elif readme_path.exists():
        prompt = """Summarize this research project concisely. Write 1 paragraph of 3-5 sentences followed by a short bullet list only if there are concrete key findings. Vary your opening. Include 1-2 links to key tools or sources when useful. Be specific, factual, and brief. No emoji."""
        result = subprocess.run(
            ["llm", "-m", MODEL, "-s", prompt],
            stdin=open(readme_path, encoding="utf-8"),
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            error_msg = f"LLM command failed for {dirname} with return code {result.returncode}"
            if result.stderr:
                error_msg += f"\nStderr: {result.stderr}"
            raise RuntimeError(error_msg)
        description = result.stdout.strip()
        if not description:
            raise RuntimeError(f"LLM command returned no output for {dirname}")
        print(description)
        summary_path.write_text(description + "\n", encoding="utf-8")
    else:
        print("*No description available.*")

    print()

AI_NOTE_START = "<!-- AI-GENERATED-NOTE --" + ">"
AI_NOTE_END = "<!-- /AI-GENERATED-NOTE --" + ">"
AI_NOTE_CONTENT = """> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it."""
NOT_AI_GENERATED = "<!-- not-ai-generated --" + ">"

for dirname, _ in subdirs_with_dates:
    readme_path = research_dir / dirname / "README.md"
    if not readme_path.exists():
        continue
    content = readme_path.read_text(encoding="utf-8")
    if NOT_AI_GENERATED in content:
        continue
    if AI_NOTE_START in content:
        pattern = re.escape(AI_NOTE_START) + r".*?" + re.escape(AI_NOTE_END)
        new_note = f"{AI_NOTE_START}\n{AI_NOTE_CONTENT}\n{AI_NOTE_END}"
        new_content = re.sub(pattern, new_note, content, flags=re.DOTALL)
        if new_content != content:
            readme_path.write_text(new_content, encoding="utf-8")
    else:
        lines = content.split("\n")
        new_lines = []
        note_added = False
        for line in lines:
            new_lines.append(line)
            if not note_added and line.startswith("# "):
                new_lines.append("")
                new_lines.append(AI_NOTE_START)
                new_lines.append(AI_NOTE_CONTENT)
                new_lines.append(AI_NOTE_END)
                note_added = True
        if note_added:
            readme_path.write_text("\n".join(new_lines), encoding="utf-8")
]]]-->
## 11 research projects

### [开源 AI Agent 核心项目实证探索与客观分析报告](https://github.com/Martin-Mythos/research/tree/main/agent-projects-empirical-study#readme) (2026-05-03 18:20)

This research systematically examines core open-source AI agent projects based on the `Arindam200/awesome-ai-apps` repository, focusing on agent categories such as information analysis, workflow automation, and security integration. The study designs reproducible benchmarks and tests for each agent, emphasizing retrievability, security boundaries, and performance risks. Verification was based on source code and documentation review, with further engineering judgments made in the absence of live API keys. Findings suggest that while the projects demonstrate clear logic separation and production-level architecture (especially for RAG and workflow agents), their stability, security, and evaluability remain significant challenges for real-world deployment.

**Key findings:**
- Projects like Deep Researcher implement multi-stage pipelines, but are highly sensitive to upstream retrieval errors, leading to potential error amplification.
- Advanced RAG and Meeting Assistant agents support structured information extraction and hybrid retrieval, but require schema validation and careful candidate management.
- Security integrations are robust (e.g., sandboxes, OAuth2), but vulnerable to token over-scoping, prompt injection, and log leaks.
- Unified evaluation metrics (e.g., recall@k, action item completeness) and “default deny” security policies are urgently needed for production use.

For further details, see [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) and the accompanying artifacts/scripts for reproducibility.

### [keep-codex-fast 实验研究报告（Experimental-based）](https://github.com/Martin-Mythos/research/tree/main/keep-codex-fast-exp-study#readme) (2026-05-03 18:19)

This experimental study rigorously assesses the claims of the keep-codex-fast project, which promises faster Codex performance through local state maintenance. Testing covered all documented modes and maintenance actions, utilizing official smoke tests, parameter coverage, and micro-benchmarks with simulated environments. Results demonstrate full coverage and functional correctness, confirming that “speedup” refers to reducing local I/O, scanning, and indexing overhead—rather than direct improvement in model inference speed. The project's tools, such as its main script ([keep_codex_fast.py](https://github.com/vibeforge1111/keep-codex-fast)), operate safely and effectively, especially in long-term, heavy-use environments.

**Key Findings:**
- Default operation is read-only and safe; no risk of unintended data alteration.
- “apply” mode moves outdated sessions/worktrees out of hot paths, using backup-first strategy.
- Successfully mitigates common local slowdowns (large logs, dead configs, old sessions, path discrepancies).
- Script execution is fast; most slowdowns stem from file operations typical of maintenance.
- Actual perceived speedup depends on user history/usage scale, with primary benefits for heavy Codex users.

### [基于 ENISA SRP 复杂场景的 open-design 架构实证研究报告](https://github.com/Martin-Mythos/research/tree/main/open-design-srp-evaluation#readme) (2026-05-03 18:18)

This research empirically evaluates the use of the open-design framework in complex ENISA SRP (Security Reporting Platform) scenarios. Unlike traditional enterprise form engines, open-design prioritizes agent-driven, prompt-based artifact generation for rapid prototyping and design exploration. The study finds open-design is highly effective for design acceleration—producing UI skeletons, token mockups, and demo pages—but lacks system-level features required for SRP’s stringent compliance (complex validation, RBAC, auditability). The suggested approach is to layer open-design atop a robust business core with dedicated form validation and RBAC enforcement. For more details, see [ENISA SRP overview](https://www.enisa.europa.eu/topics/csirt-cert-services/srp) and [open-design tool](https://github.com/open-design/open-design).

**Key Findings:**
- open-design excels at rapid artifact generation (tokens, UI prototypes) but cannot independently handle business logic, complex validation, or RBAC.
- It supports maintainable i18n resource generation, but lacks enterprise-grade runtime i18n mechanisms.
- RBAC-sensitive UI hiding is possible, but true compliance requires back-end field enforcement.
- Production deployment requires strict "artifact admission control" and double-layer architecture (design accelerator + business core).

### [Stitch Skills 研究：工作流与价值验证（SRP 案例）](https://github.com/Martin-Mythos/research/tree/main/stitch-skills-workflow-study#readme) (2026-05-03 10:07)

This study evaluates the workflow and business value of Stitch Skills, a modular set of UI generation tools featured in the repository [`google-labs-code/stitch-skills`](https://github.com/google-labs-code/stitch-skills). By systematically mapping skill modules—such as prompt enhancement, batch page generation, design system documentation, componentization, and videoification—into an end-to-end prototype workflow for a business portal (SRP), the research demonstrates Stitch Skills' ability to reduce collaboration costs and rapidly produce review-ready assets. Experiments verify that the toolkit enables quick style switching, interactive demo upgrades, and animation integration, supporting efficient stakeholder alignment and rapid iteration of enterprise-grade UI prototypes. Although remote generation and full pipeline tests were not performed, local HTML/CSS/JS workflows sufficed to validate feasibility and workflow coverage.

**Key Findings:**
- Stitch Skills' clear modular layering (design, prompt enhancement, code export, video asset generation) supports end-to-end workflow assembly.
- For mid/back-office products like SRP, the primary value lies in rapid multi-style prototyping, consistency enforcement, and producing demonstrable assets.
- Incorporating demo assets (HTML slides and animation demos) significantly increases review efficiency for proposals.

For technical setup and further exploration, see the [Stitch Skills workflow repository](https://github.com/google-labs-code/stitch-skills).

### [深度研究报告：`yao-tutorial-skill` 能力评估与 Harness Engineering 教程实验](https://github.com/Martin-Mythos/research/tree/main/harness-engineering-skill-review#readme) (2026-05-03 10:07)

This research systematically evaluates the boundaries and delivery mechanisms of `yao-tutorial-skill`, focusing on its effectiveness in generating a structured, actionable tutorial for Harness Engineering. By replicating its workflow—from input normalization to research, outline, drafting, and validation—the study confirms that the skill is tuned for high-fidelity, process-driven tutorial production rather than rapid Q&A. The generated Harness Engineering tutorial meets comprehensive standards for accuracy, completeness, and usability, with the evaluation script confirming full compliance with skill-specific requirements. The findings highlight both the utility and limitations of `yao-tutorial-skill` for enterprise knowledge management, especially when full process features (like multi-format export and auto-verification) are actively used.

Key findings:
- `yao-tutorial-skill` operates as a "tutorial production pipeline," emphasizing end-to-end workflow and source verification.
- Tutorials generated are structurally complete, covering definitions, architecture, implementation stages, templates, governance, anti-patterns, and checklists.
- Quality checks (via [quality_eval.py](https://github.com/yaojingang/yao-open-skills/blob/main/examples/quality_eval.py)) confirm 100% compliance in process, delivery, usability, and enforceable engineering standards.
- The skill is best suited for teams needing structured, auditable, reusable educational materials, and can serve as a template for enterprise L&D content production if enhanced with fact-checking and glossary consistency.
- Risks include potential “pretty structure but weak evidence” and format/content mismatch, recommending additional fact verification and glossary linting in production.

For more information, see the [skill documentation](https://github.com/yaojingang/yao-open-skills/blob/main/docs/skills/yao-tutorial-skill.md).

### [create-agent-tui 自定义 Agent 价值研究](https://github.com/Martin-Mythos/research/tree/main/create-agent-tui-custom-agent-value-study#readme) (2026-04-26 17:56)

This research examines the value of the create-agent-tui tool within the OpenRouterTeam/skills repository, focusing on its ability to systematize key engineering concerns—control, operability, persistence, and integration—rather than enhance AI model intelligence. Through document analysis and reproducible experiments, the study demonstrates that while create-agent-tui provides limited benefits for simple Q&A tasks, it significantly outperforms basic chat interfaces in scenarios demanding tool invocation, approval workflows, session tracking, terminal workflow integration, or backend/service embedding. The project confirms that create-agent-tui delivers a reusable agent scaffold offering layered architecture and engineering governance capabilities, clearly exceeding baseline chat solutions in complex operational settings. For more on the tool, see [OpenRouterTeam/skills](https://github.com/OpenRouterTeam/skills).

Key findings:

- All claimed agent-level features (tool modes, persistent sessions, approvals, modular configs, server entrypoints) are directly evidenced in upstream documentation and code.
- In needs beyond one-off chat—such as code approval, long-lived research agents, terminal assistants, or API/server integration—custom agent coverage is 100% versus 0% for baseline chats.
- create-agent-tui’s architectural design supports extensibility and is grounded in lessons from real-world production agent systems.
- For simple, non-governed question-answering tasks, its value is minimal compared to the maintenance cost.

### [mattpocock/skills 的 Todo App 实验研究](https://github.com/Martin-Mythos/research/tree/main/mattpocock-skills-todo-app-eval#readme) (2026-04-26 14:43)

This research evaluates the mattpocock/skills repository by applying several agent "skills" to a minimal Node.js todo app. The project focuses on workflow documentation, using `SKILL.md` files to outline agent-triggering criteria, execution steps, and quality standards. Applying skills like `design-an-interface`, `tdd`, and `qa` demonstrated that these tools guide agents into structured workflows, improving task clarity—even for small projects—by enforcing interface design comparison, behavior-driven testing, and user-perspective issue documentation. Notably, the skills promote process discipline but depend on agent compliance, as there is minimal runtime enforcement.

**Key findings:**
- mattpocock/skills is primarily a documentation-driven collection, not a runtime plugin suite ([GitHub repo](https://github.com/mattpocock/skills)).
- The `tdd` skill led to the detection and correction of a subtle filter-related bug that could have been missed during implementation.
- The `design-an-interface` skill forced interface comparisons, resulting in clearer API choices, even for simple modules.
- The `qa` skill is valuable for transforming test findings into persistent, user-facing issues, facilitating handoff and long-term tracking.
- Skills shape process effectively but lack automated enforcement; the agent must consciously follow protocols.

### [docs](https://github.com/Martin-Mythos/research/tree/main/docs#readme) (2026-04-26 14:43)

*No description available.*

### [WUPHF Multi-Agent Context Sync Research](https://github.com/Martin-Mythos/research/tree/main/wuphf-multi-agent-context-sync#readme) (2026-04-26 11:19)

The WUPHF multi-agent context sync research demonstrates that the key to effective multi-agent collaboration is not real-time synchronization of all agent-specific contexts, but rather distinguishing, externalizing, and promoting only actionable, shared, and auditable context to a central substrate (e.g., a shared wiki with append-only logs and provenance). Each agent maintains a private notebook for drafts and raw observations, and only promotes mature decisions or facts to a team-accessible wiki following an explicit review or promotion protocol. Synchronization of all chat transcripts is discouraged—instead, only contracts, decisions, handoffs, owners, worktree paths, and evidence are surfaced to the shared layer, with ownership and provenance attached. This approach reduces context drift and improves recoverability compared to chat-based syncing, as verified in simulation experiments.

**Key findings:**

- Separating context into private draft, promoted shared truth, and live owner knowledge decreased context incidents in simulations (from 4 to 1).
- Shared writes are serialized using a single-writer queue, avoiding race conditions.
- Owner routing replaces blanket context sync: agents are directed to ask owners for fresh, non-promoted details.
- Provenance, append-only logs, and runtime snapshots ensure auditable, recoverable shared state.
- The protocol can be immediately reused with a structure of private notebooks, team wikis, single-writer shared access, and owner metadata.

For an applicable protocol and more details, see the [source project](https://github.com/nex-crm/wuphf) and the [mini-project experiment](https://github.com/nex-crm/wuphf/blob/main/scripts/simulate_context_sync.mjs).

### [garrytan/gstack 最小实验研究](https://github.com/Martin-Mythos/research/tree/main/garrytan-gstack-minimal-eval#readme) (2026-04-26 10:08)

The minimal experiment on `garrytan/gstack` confirms it is an AI engineering workflow stack—not a single app—built with Bun and TypeScript, integrating modular slash-command skills, browser automation, host-specific skill generation, and robust QA/security processes. Core mechanisms such as skill validation and skill documentation generation are healthy, with all tests for skill commands and doc generation passing once host-specific artifacts are generated. The project correctly supports multi-host skill projection, allowing one template system to generate consistent, safely validated skill outputs for Codex and other hosts. A minor inconsistency was discovered in health scripts regarding Claude host skill generation, and one skill file exceeded project token ceilings, highlighting potential context management challenges. For full reproduction and further experimentation, referencing the official repository and Bun install is essential: [garrytan/gstack GitHub](https://github.com/garrytan/gstack) and [Bun](https://bun.sh/).

**Key Findings:**
- All 318 skill validation tests and 371 skill doc tests (after generating Codex artifacts) passed, indicating strong template and registry integrity.
- Skill system centers on templated Markdown artifacts; 43 skills identified, all templated.
- Project relies on a central browser command registry with 72 commands segmented by function.
- Codex host projection requires artifact generation for full test suite success.
- Detected a health check/test suite inconsistency for Claude host skill documentation logic.
- At least one skill doc file (`ship/SKILL.md`) exceeds recommended size, flagging future agent context risks.

### [Simon Willison 的 AI Research Repo 方法研究](https://github.com/Martin-Mythos/research/tree/main/simon-willison-code-research-method#readme) (2026-04-26 07:56)

Simon Willison's AI research repo method transforms research questions into reproducible, reviewable code workflows using dedicated GitHub repositories. Instead of relying on chat-based AI summaries, he assigns clear, executable tasks to asynchronous coding agents (such as Claude Code or Codex Cloud), which install dependencies, collect data, run experiments, and generate reports—all documented through pull requests or commits. This approach compresses AI output into verifiable code, tests, benchmarks, and artifacts, making it easier to review, reproduce, and accumulate long-term research compared to ephemeral chat answers. The workflow is explicitly documented in his [article](https://simonwillison.net/2025/Nov/6/async-code-research/) and implemented in the [`simonw/research`](https://github.com/simonw/research) repository, emphasizing transparency and dedicated environments to reduce risk.

**Key findings:**
- Dedicated repositories allow safe network access by isolating research from production code and sensitive assets.
- Each research project is a single directory containing scripts, notes, results, and a final README, facilitating reproducibility and review.
- Automated GitHub Actions maintain project summaries and indexes, ensuring easy navigation and context for agents.
- The method relies on human review prior to publication to mitigate risks of AI-generated errors, supply chain attacks, or misleading conclusions.
- Research results should be treated as lab notebooks, not finalized publications, until manually verified.

<!--[[[end]]]-->

---

## Updating this README

This README uses [cogapp](https://nedbatchelder.com/code/cog/) to automatically generate the project index.

### Automatic updates

A GitHub Action runs `cog -r -P README.md` on every push to `main` and commits changes to the root `README.md`, project `README.md` files, and generated `_summary.md` files.

### Manual updates

```bash
cog -r -P README.md
```

The script:

- discovers all top-level research directories;
- sorts them by the latest commit that touched each directory;
- extracts each project title from its first H1 heading;
- reuses `_summary.md` when present;
- otherwise generates a concise summary with `llm -m github/gpt-4.1`;
- injects an AI-assisted research note into project README files unless they opt out with `<!-- not-ai-generated -->`.
