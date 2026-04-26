# Research projects carried out with AI tools

This repository is a dedicated workspace for code research and web research projects carried out with AI coding agents such as Codex, Claude Code, Jules, or GitHub Copilot coding agent.

Each top-level directory is one separate investigation. Reports should include enough notes, scripts, sources, and verification evidence for a reviewer to understand what was tested and how conclusions were reached.

The operating model is inspired by Simon Willison's article [Code research projects with async coding agents like Claude Code and Codex](https://simonwillison.net/2025/Nov/6/async-code-research/) and his public [`simonw/research`](https://github.com/simonw/research) repository.

Prompts, transcripts, and important review context should be linked from pull requests or commits whenever possible.

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
## 3 research projects

### [garrytan/gstack 最小实验研究](https://github.com/Martin-Mythos/research/tree/main/garrytan-gstack-minimal-eval#readme) (2026-04-26 10:08)

The minimal experiment on `garrytan/gstack` confirms it is an AI engineering workflow stack—not a single app—built with Bun and TypeScript, integrating modular slash-command skills, browser automation, host-specific skill generation, and robust QA/security processes. Core mechanisms such as skill validation and skill documentation generation are healthy, with all tests for skill commands and doc generation passing once host-specific artifacts are generated. The project correctly supports multi-host skill projection, allowing one template system to generate consistent, safely validated skill outputs for Codex and other hosts. A minor inconsistency was discovered in health scripts regarding Claude host skill generation, and one skill file exceeded project token ceilings, highlighting potential context management challenges. For full reproduction and further experimentation, referencing the official repository and Bun install is essential: [garrytan/gstack GitHub](https://github.com/garrytan/gstack) and [Bun](https://bun.sh/).

**Key Findings:**
- All 318 skill validation tests and 371 skill doc tests (after generating Codex artifacts) passed, indicating strong template and registry integrity.
- Skill system centers on templated Markdown artifacts; 43 skills identified, all templated.
- Project relies on a central browser command registry with 72 commands segmented by function.
- Codex host projection requires artifact generation for full test suite success.
- Detected a health check/test suite inconsistency for Claude host skill documentation logic.
- At least one skill doc file (`ship/SKILL.md`) exceeds recommended size, flagging future agent context risks.

### [mattpocock/skills 的 Todo App 实验研究](https://github.com/Martin-Mythos/research/tree/main/mattpocock-skills-todo-app-eval#readme) (2026-04-26 09:29)

This research evaluates the mattpocock/skills repository by applying several agent "skills" to a minimal Node.js todo app. The project focuses on workflow documentation, using `SKILL.md` files to outline agent-triggering criteria, execution steps, and quality standards. Applying skills like `design-an-interface`, `tdd`, and `qa` demonstrated that these tools guide agents into structured workflows, improving task clarity—even for small projects—by enforcing interface design comparison, behavior-driven testing, and user-perspective issue documentation. Notably, the skills promote process discipline but depend on agent compliance, as there is minimal runtime enforcement.

**Key findings:**
- mattpocock/skills is primarily a documentation-driven collection, not a runtime plugin suite ([GitHub repo](https://github.com/mattpocock/skills)).
- The `tdd` skill led to the detection and correction of a subtle filter-related bug that could have been missed during implementation.
- The `design-an-interface` skill forced interface comparisons, resulting in clearer API choices, even for simple modules.
- The `qa` skill is valuable for transforming test findings into persistent, user-facing issues, facilitating handoff and long-term tracking.
- Skills shape process effectively but lack automated enforcement; the agent must consciously follow protocols.

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
