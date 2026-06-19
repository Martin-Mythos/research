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
## 24 research projects

### [Baoyu-Design PPTX Empirical Study](https://github.com/Martin-Mythos/research/tree/main/baoyu-design-pptx-empirical-study#readme) (2026-06-19 20:01)

This empirical study evaluates `JimLiu/baoyu-design` as an AI-assisted design and document generation workflow, focusing on design-system structure, editable PowerPoint export, and generated-image insertion. The core `gen-pptx` chain was reproduced locally with Playwright and PptxGenJS: a three-slide HTML deck was captured and exported to an editable `.pptx` containing native text bodies, shapes, picture objects, and speaker notes. A locally generated cybersecurity server-room PNG was inserted into the deck and preserved as a native PowerPoint picture object rather than flattening the whole slide to screenshots.

Key findings:
- The editable PPTX path is technically credible and locally reproduced with no exporter warnings.
- OOXML inspection confirms native PowerPoint objects (`p:txBody`, `p:sp`, `p:pic`) across the generated deck.
- Baoyu's own Image Generation API integration was not exercised; the study isolates the insertion/layout pipeline using a local generated image artifact.

### [基于 30Days-Skill 框架的 GLM-5.2 与 Anthropic Mythos/Fable 5 实证研究](https://github.com/Martin-Mythos/research/tree/main/30days-skill-frontier-models-study#readme) (2026-06-19 19:31)

This research project adapted the `mvanhorn/last30days-skill` framework into an incremental evidence tracking workflow to empirically assess GLM-5.2’s engineering boundaries and the compliance impacts of the Anthropic Mythos/Fable 5 export-control directive. By systematically cloning, testing, and monitoring, the study compared baseline and interval tracking, revealing that incremental research provides superior traceability and actionable outcomes over traditional, static approaches. Key validated findings were drawn from primary sources and artifacts, while notable limitations included lack of live API benchmarks and incomplete visibility into Mythos/Fable 5’s technical details and compliance procedures. The project’s methodology and evidence artifacts are available for reproduction and verification.

**Key findings:**
- GLM-5.2 features verified public claims, including 1M context support, robust coding benchmarks, open weights, and advanced engineering use cases.
- Real-world engineering for GLM-5.2 requires awareness of KV-cache and context kernel limits, CPU overhead, quota, and anti-hack infrastructure.
- Anthropic Mythos/Fable 5 access was officially suspended, per US export-control policy; other Anthropic models remain unaffected.
- Incremental tracking improves traceability, bias reduction, actionability, and temporal robustness compared to baseline research.

For methodology and tooling, see [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill).

### [Kun Chen Agentic Engineering Tools 经验研究报告](https://github.com/Martin-Mythos/research/tree/main/kun-agentic-engineering-tools-study#readme) (2026-06-16 21:40)

This research project evaluates the "Plan-Code-Validate" agentic engineering toolchain (Lavish, Treehouse, No Mistakes) via practical development of the Talking Breads Tervuren static website. The investigation finds that while the overall workflow is promising, the tools are currently best adopted in discrete stages rather than as a monolithic pipeline for day-to-day workflows. Lavish excels at turning vague requirements into reviewable HTML artifacts for the planning stage; Treehouse provides solid Git worktree pooling best leveraged with multiple agents; No Mistakes shows most potential for integrated validation but cannot demonstrate its full value without remote/authentication and CI capabilities. The recommended adoption path is to trial Lavish and Treehouse in controlled use-cases and restrict No Mistakes to sandbox environments pending further validation.

Key findings:
- Lavish: Immediate value in producing HTML planning artifacts for clarity and auditability ([Lavish docs](https://github.com/kunchenguid/lavish-axi)).
- Treehouse: Worktree pooling useful for high agent concurrency, but overkill for small solo projects ([Treehouse repo](https://github.com/kunchenguid/treehouse)).
- No Mistakes: Validation strongest with remote/PR/CI integration; local-only usage is limited.
- Combined toolchain reduces context switching and improves artifact auditability, but still needs traditional CI, manual reviews, and clear permission boundaries.

### [Technical Principles and Architecture Reverse Engineering of Markdown-Viewer/Skills](https://github.com/Martin-Mythos/research/tree/main/markdown-viewer-architecture-study#readme) (2026-06-14 11:25)

This research examines the technical design and internal architecture of the [`markdown-viewer/skills`](https://github.com/markdown-viewer/skills) repository, revealing it as a declarative, contract-driven library rather than an executable application. The core workflow transforms user requests into well-defined, renderer-compatible Markdown artifacts, relying on strict syntax contracts and structured metadata per skill module. Rendering is intentionally outside the repository, delegated to external Markdown Viewer instances or compatible hosts, as the repository contains no runtime, build system, or app manifests. The architecture is characterized by a contract-first pattern, with each skill constraining output formats for multiple renderer families.

**Key findings:**
- The analyzed commit contains 15 distinct skill modules and 252 tracked files.
- Output formats supported include PlantUML, Graphviz DOT, JSON Canvas, Vega/Vega-Lite, HTML/CSS, and template-based infographics.
- No executable application entrypoint or build tool is present; repository serves only as a skill contract and template provider.
- Architecture diagrams and inventory artifacts are generated for reproducibility and visualization ([Mermaid diagrams](https://mermaid-js.github.io/), JSON inventories).

### [Understand-Anything for ASF 2026 site structure research](https://github.com/Martin-Mythos/research/tree/main/understand-anything-asf-site-structure-study#readme) (2026-06-14 11:12)

The project assessed the application of the Understand-Anything tool for site structure analysis within the ASF 2026 framework, focusing on end-to-end validation using a private repository. While scripts for scan, import-map, and batches ran successfully on accessible repositories, attempts to fully replicate results on the ASF private repo failed due to access restrictions. The research isolated private repo constraints as a primary blocker and documented evidence of failed access, as well as minor issues with worker timeouts during test runs.

Key findings:

- Understand-Anything can generate structured intermediate graph data for site structure analysis.
- Private repository access is the main barrier to full replication.
- Test suite revealed an unhandled worker timeout issue.

Further details and the tool may be referenced at the [Understand-Anything GitHub repository](https://github.com/Lum1104/Understand-Anything).

### [GSAP vs Remotion Article Animation Research](https://github.com/Martin-Mythos/research/tree/main/gsap-vs-remotion-article-animation#readme) (2026-06-14 11:09)

This research project analyzes the process of animating a generated article with GSAP and compares it to video-creation toolkits Remotion and Hyperframe. GSAP demonstrated rapid setup and precise timeline management for animating web-based articles, while Remotion and Hyperframe proved more capable when exporting deterministic video formats like MP4 is essential. Partial reproduction included GSAP proof-of-concept and local running; however, screenshot automation was impeded by external browser download limitations. Further details and code are available in the [GSAP documentation](https://gsap.com/docs/) and the project artifacts.

**Key Findings:**
- GSAP excels in DOM-based article animation with quick setup and detailed timeline control.
- Remotion/Hyperframe are preferable for deterministic video exports (MP4).
- Screenshot automation currently hindered by Playwright download restrictions.

### [Qiaomu Anything-to-NotebookLM empirical research](https://github.com/Martin-Mythos/research/tree/main/qiaomu-anything-to-notebooklm-empirical-study#readme) (2026-05-25 06:42)

This project empirically evaluates the Qiaomu Anything-to-NotebookLM workflow, which aims to facilitate data import into Google’s NotebookLM via a custom tool (see repository). While the team successfully installed the tool and confirmed its ability to recognize user inputs, full integration with NotebookLM was not achieved. The missing CLI and authentication mechanisms prevented completion of the data-upload pipeline. Detailed findings are provided in the main report (`research_report.md`), supported by setup and run logs.

Key findings:
- Tool installation and user input recognition steps are reproducible.
- Direct upload to NotebookLM remains incomplete due to CLI/authentication gaps.
- Documentation and empirical evidence are published in the repository logs and artifacts.

Relevant link: [Qiaomu Anything-to-NotebookLM GitHub](https://github.com/joeseesun/qiaomu-anything-to-notebooklm)

### [Sense Deck Skill 与主流 AI PPT 工具链的架构实证与横评报告](https://github.com/Martin-Mythos/research/tree/main/sense-deck-skill-benchmark#readme) (2026-05-18 21:34)

This research project evaluates the architectural and usability characteristics of the Sense Deck Skill — a workflow that prioritizes template selection, content IR construction, and static HTML/CSS/JS delivery for enterprise-level AI presentation scenarios. Through empirical comparison with mainstream AI PPT toolchains (Marp/归藏 and python-pptx/花叔), it finds that Sense Deck excels in front-end controllability, visual consistency, and offline deployment, especially suited for organizations emphasizing code modifiability. Marp offers rapid outline-to-page conversion and low collaboration costs but is limited in complex layouts, while python-pptx provides seamless integration into Office environments but demands scripting prowess and higher style editing costs.

Key findings:
- Sense Deck achieves the highest overall score on engineering transparency, visual expansion, and logical clarity (13.5/15).
- Marp is optimal for quick structuring and collaborative markdown-based editing, yet limited in detailed visual customization.
- Python-pptx fits organizations needing final `.pptx` assets but requires significant manual styling and scripting.
- Recommended hybrid workflow: use Marp for draft structuring, Sense Deck for high-fidelity delivery, and export to PPTX as needed.

Links:
- [Sense Deck Skill GitHub](https://github.com/xwbcl123/-PPT-sense-deck-skill-)
- [Marp Official](https://marp.app/)

### [tw93/Waza 八项核心 Skill A/B 测试实证报告](https://github.com/Martin-Mythos/research/tree/main/waza-ab-test#readme) (2026-05-17 07:32)

This report evaluates the effectiveness of **Waza**, an engineering workflow tool for AI-assisted development, by running A/B tests in code and content scenarios. Unlike traditional tools that focus on improving code generation, Waza enforces a stepwise, auditable process—from context auditing to modeling, root cause analysis, and rigorous review—which addresses frequent issues of unreliable code execution and shallow deliverables. In practice, Waza demonstrably improves architectural robustness, debugging precision, and information density in both engineering and writing tasks, although final code quality still depends on model ability and strict process adherence. The tool shines particularly in debugging, context modeling, and risk control before deployment, supporting teams with repeatable, traceable workflows.

**Key findings:**
- Waza substantially reduces reckless code execution and boosts verifiability, especially in debug and review phases.
- Information density and technical clarity are markedly higher in research tasks, thanks to structured learning and writing modules.
- Best results are achieved when Waza’s steps (`/health`, `/think`, `/hunt`, `/check`, `/learn`) are followed rigorously and incorporated into team processes, notably CI checklists.

- For more details and source material, see the [Waza GitHub repository](https://github.com/tw93/Waza).

### [OpenSlide 与主流 AI PPT 技能的工程实证与横向评测报告](https://github.com/Martin-Mythos/research/tree/main/openslide-skill-benchmark#readme) (2026-05-07 06:01)

This research project conducts a practical engineering comparison between OpenSlide (a React-based slide framework), Marp-based "归藏流派" (structured Markdown/HTML workflow), and Python-pptx-based "花叔流派" for AI-powered PPT generation and delivery. OpenSlide excels in componentized, version-controlled slides suitable for collaborative engineering and agent-driven content iteration but has a longer path to direct .pptx exports. The Marp workflow offers rapid, structured content generation in Markdown but requires extra conversion for deep PPT editing. The Python-pptx approach provides the shortest chain to editable PowerPoint files but tends toward template-based visuals without extra design steps. Evaluation showed each method has clear trade-offs in structure, visual flexibility, and engineering usability.

Key findings:
- OpenSlide is best for maintainable, component-based engineering, especially where React and design systems are leveraged ([OpenSlide GitHub](https://github.com/openslide/openslide)).
- Marp/归藏流派 is ideal for fast, structured draft generation, supporting high productivity ([Marp tool](https://marp.app/)).
- Python-pptx/花叔流派 offers the most direct, low-friction way to deliver ready-to-edit PPTX files for business use.
- Trade-off matrix confirms OpenSlide’s visual/layout strengths, Marp’s drafting speed, and Python-pptx’s file delivery efficiency; choice depends on project context and team skillset.

### [Sense Deck Skill 与主流 AI PPT 工具链的架构实证与横评报告](https://github.com/Martin-Mythos/research/tree/main/sense-deck-html-benchmark#readme) (2026-05-07 06:00)

This research project systematically evaluates the Sense Deck Skill ("鲸格PPT") against mainstream AI-powered PPT toolchains, specifically Marp (归藏流派) and Python-pptx (花叔流派). Focusing on a template-first workflow, the study benchmarks three approaches across engineering flexibility, visual output quality, logical conveyance, toolchain dependencies, and team collaboration. Sense Deck stands out for its high front-end control and visual customization capability, suitable for browser-based, team-extensible presentations. Marp excels in speed and version control for simple structured drafts, while Python-pptx remains robust for compatibility with Office ecosystems but at higher engineering cost. Overall, Sense Deck offers the strongest platform for customizable, web-native presentations; Marp is optimal for low-friction authoring; Python-pptx is best for formal Office deliverables.

**Key findings:**
- Sense Deck achieves top scores for DOM flexibility (4.7/5) and visual expansion (4.6/5), supporting native HTML/CSS/JS editing.
- Marp is fastest for content drafting and collaborative workflows (4.6/5) but limited in advanced layout options by Markdown syntax.
- Python-pptx is well-integrated with Office but high engineering and iterative overhead (composite score 3.62/5).
- Recommended workflow: use Sense Deck as the base for front-end teams, Marp for rapid drafts, and Python-pptx for bulk/final Office exports.

For technical details, see [Sense Deck GitHub repository](https://github.com/xwbcl123/-PPT-sense-deck-skill-) and [Marp documentation](https://marp.app/).

### [敏捷 SaaS 场景下 compound-engineering-plugin 架构实证报告](https://github.com/Martin-Mythos/research/tree/main/compound-plugin-saas-study#readme) (2026-05-03 22:21)

This research empirically analyzes the architecture of the `compound-engineering-plugin` within agile SaaS contexts, focusing on its method engineering approach rather than a monolithic executor. The plugin leverages a SKILL.md workflow protocol, multi-agent scheduling conventions, and cross-platform converters to turn product requirements into structured, actionable plans and task cards. Through codebase examination and simulated experiments, the study demonstrates how the plugin systematically decomposes vague or complex requirements, standardizes PM processes, and outputs artifacts such as engineering tickets and worklogs, though it depends heavily on contextual quality and host platform capabilities. The findings highlight both the strengths in modularizing engineering workflows and the current limits in deep technical guidance and organizational scalability.

**Key findings:**
- The plugin enforces a methodical transformation of product requirements into structured plans, clarifying boundaries, technical decisions, and test scenarios.
- Experimental outputs show clear decomposition of collaborative editing features into key engineering tasks, though full technical specificity depends on further research input.
- For ambiguous requirements, the plugin mandates clarification or baseline measurement (spike) phases before implementation, reducing ad-hoc solutions.
- Limitations include reliance on host agent support, variable effectiveness with loosely-defined contexts, and the need for unified schemas in large organizations.

Reference: [Bun JavaScript Runtime](https://bun.sh), [TypeScript](https://www.typescriptlang.org/)

### [tw93/kami 设计系统解析与 Web 视觉重构实验报告](https://github.com/Martin-Mythos/research/tree/main/kami-design-experiments#readme) (2026-05-03 22:10)

This project analyzes the design system "Kami," emphasizing its minimalist approach using a compact and stable token set to achieve a consistent and readable visual identity. Key features include a paper-like background, near-black body text, restrained use of color, serif typography, and thoughtful whitespace. Engineering practices involve variable-driven CSS, template reuse, and semi-semantic class names to keep style consistency and reduce visual fragmentation. Experiments showed that even with basic HTML and inline CSS, Kami enables rapid construction of distinct, readable web pages. While well-suited for content-centric and reading-heavy interfaces, it presently lacks built-in dark mode logic and comprehensive support for interactive or data-dense applications.

Key findings:
- The design token system fosters visual continuity and reduces user fatigue with low-saturation, high-contrast color choices.
- Typographic rules prioritize rhythm and hierarchy over simple font size variation.
- Kami's current strengths are in documentation, homepages, and minimalist web presentations; see [Kami on GitHub](https://github.com/tw93/kami) for source templates.
- Limitations include incomplete support for interactive state management, advanced accessibility, dense data visualization, and dark mode.
- Recommendations include expanding semantic tokens, improving component-level specifications, integrating visual regression tools, and implementing theme mapping for maintainability.

### [开源 AI Agent 核心项目实证探索与客观分析报告](https://github.com/Martin-Mythos/research/tree/main/agent-projects-empirical-study#readme) (2026-05-03 18:21)

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

### [深度研究报告：`yao-tutorial-skill` 能力评估与 Harness Engineering 教程实验](https://github.com/Martin-Mythos/research/tree/main/harness-engineering-skill-review#readme) (2026-05-03 10:07)

This research systematically evaluates the boundaries and delivery mechanisms of `yao-tutorial-skill`, focusing on its effectiveness in generating a structured, actionable tutorial for Harness Engineering. By replicating its workflow—from input normalization to research, outline, drafting, and validation—the study confirms that the skill is tuned for high-fidelity, process-driven tutorial production rather than rapid Q&A. The generated Harness Engineering tutorial meets comprehensive standards for accuracy, completeness, and usability, with the evaluation script confirming full compliance with skill-specific requirements. The findings highlight both the utility and limitations of `yao-tutorial-skill` for enterprise knowledge management, especially when full process features (like multi-format export and auto-verification) are actively used.

Key findings:
- `yao-tutorial-skill` operates as a "tutorial production pipeline," emphasizing end-to-end workflow and source verification.
- Tutorials generated are structurally complete, covering definitions, architecture, implementation stages, templates, governance, anti-patterns, and checklists.
- Quality checks (via [quality_eval.py](https://github.com/yaojingang/yao-open-skills/blob/main/examples/quality_eval.py)) confirm 100% compliance in process, delivery, usability, and enforceable engineering standards.
- The skill is best suited for teams needing structured, auditable, reusable educational materials, and can serve as a template for enterprise L&D content production if enhanced with fact-checking and glossary consistency.
- Risks include potential “pretty structure but weak evidence” and format/content mismatch, recommending additional fact verification and glossary linting in production.

For more information, see the [skill documentation](https://github.com/yaojingang/yao-open-skills/blob/main/docs/skills/yao-tutorial-skill.md).

### [Stitch Skills 研究：工作流与价值验证（SRP 案例）](https://github.com/Martin-Mythos/research/tree/main/stitch-skills-workflow-study#readme) (2026-05-03 10:07)

This study evaluates the workflow and business value of Stitch Skills, a modular set of UI generation tools featured in the repository [`google-labs-code/stitch-skills`](https://github.com/google-labs-code/stitch-skills). By systematically mapping skill modules—such as prompt enhancement, batch page generation, design system documentation, componentization, and videoification—into an end-to-end prototype workflow for a business portal (SRP), the research demonstrates Stitch Skills' ability to reduce collaboration costs and rapidly produce review-ready assets. Experiments verify that the toolkit enables quick style switching, interactive demo upgrades, and animation integration, supporting efficient stakeholder alignment and rapid iteration of enterprise-grade UI prototypes. Although remote generation and full pipeline tests were not performed, local HTML/CSS/JS workflows sufficed to validate feasibility and workflow coverage.

**Key Findings:**
- Stitch Skills' clear modular layering (design, prompt enhancement, code export, video asset generation) supports end-to-end workflow assembly.
- For mid/back-office products like SRP, the primary value lies in rapid multi-style prototyping, consistency enforcement, and producing demonstrable assets.
- Incorporating demo assets (HTML slides and animation demos) significantly increases review efficiency for proposals.

For technical setup and further exploration, see the [Stitch Skills workflow repository](https://github.com/google-labs-code/stitch-skills).

### [create-agent-tui 自定义 Agent 价值研究](https://github.com/Martin-Mythos/research/tree/main/create-agent-tui-custom-agent-value-study#readme) (2026-04-26 17:56)

This research examines the value of the create-agent-tui tool within the OpenRouterTeam/skills repository, focusing on its ability to systematize key engineering concerns—control, operability, persistence, and integration—rather than enhance AI model intelligence. Through document analysis and reproducible experiments, the study demonstrates that while create-agent-tui provides limited benefits for simple Q&A tasks, it significantly outperforms basic chat interfaces in scenarios demanding tool invocation, approval workflows, session tracking, terminal workflow integration, or backend/service embedding. The project confirms that create-agent-tui delivers a reusable agent scaffold offering layered architecture and engineering governance capabilities, clearly exceeding baseline chat solutions in complex operational settings. For more on the tool, see [OpenRouterTeam/skills](https://github.com/OpenRouterTeam/skills).

Key findings:

- All claimed agent-level features (tool modes, persistent sessions, approvals, modular configs, server entrypoints) are directly evidenced in upstream documentation and code.
- In needs beyond one-off chat—such as code approval, long-lived research agents, terminal assistants, or API/server integration—custom agent coverage is 100% versus 0% for baseline chats.
- create-agent-tui’s architectural design supports extensibility and is grounded in lessons from real-world production agent systems.
- For simple, non-governed question-answering tasks, its value is minimal compared to the maintenance cost.

### [docs](https://github.com/Martin-Mythos/research/tree/main/docs#readme) (2026-04-26 14:43)

*No description available.*

### [mattpocock/skills 的 Todo App 实验研究](https://github.com/Martin-Mythos/research/tree/main/mattpocock-skills-todo-app-eval#readme) (2026-04-26 14:43)

This research evaluates the mattpocock/skills repository by applying several agent "skills" to a minimal Node.js todo app. The project focuses on workflow documentation, using `SKILL.md` files to outline agent-triggering criteria, execution steps, and quality standards. Applying skills like `design-an-interface`, `tdd`, and `qa` demonstrated that these tools guide agents into structured workflows, improving task clarity—even for small projects—by enforcing interface design comparison, behavior-driven testing, and user-perspective issue documentation. Notably, the skills promote process discipline but depend on agent compliance, as there is minimal runtime enforcement.

**Key findings:**
- mattpocock/skills is primarily a documentation-driven collection, not a runtime plugin suite ([GitHub repo](https://github.com/mattpocock/skills)).
- The `tdd` skill led to the detection and correction of a subtle filter-related bug that could have been missed during implementation.
- The `design-an-interface` skill forced interface comparisons, resulting in clearer API choices, even for simple modules.
- The `qa` skill is valuable for transforming test findings into persistent, user-facing issues, facilitating handoff and long-term tracking.
- Skills shape process effectively but lack automated enforcement; the agent must consciously follow protocols.

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
