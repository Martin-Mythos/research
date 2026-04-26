# Notes

## Research question

How does Simon Willison use web-connected asynchronous coding agents and GitHub repositories as a research workflow, and how can that method be adapted into a reusable public research repository?

## Sources actually used

- Simon Willison, "Code research projects with async coding agents like Claude Code and Codex", 2025-11-06: https://simonwillison.net/2025/Nov/6/async-code-research/
- Simon Willison's public research repository: https://github.com/simonw/research
- `simonw/research` root `README.md`: https://github.com/simonw/research/blob/main/README.md
- `simonw/research` `AGENTS.md`: https://github.com/simonw/research/blob/main/AGENTS.md
- `simonw/research` README automation workflow: https://github.com/simonw/research/blob/main/.github/workflows/update-readme.yml

## Observations

- The core unit is not a chat answer. It is a GitHub pull request or commit containing a folder with a report, notes, scripts, and artifacts.
- The method works best when the question can be turned into executable evidence: benchmarks, tests, browser automation, data extraction, diffs, charts, or reproducible scripts.
- Simon separates public and private research repositories. Public is used for non-sensitive work; private is used for material not ready to share.
- The dedicated repository lowers the risk of agent autonomy because the repository contains no production code or secrets.
- Full network access is treated as useful only inside this low-sensitivity environment.
- Root-level instructions tell agents to create a new folder, keep notes, produce a final `README.md`, avoid committing full external repositories, and leave `_summary.md` to automation.
- README automation uses `cogapp`, `llm`, and `llm-github-models` to generate a root project index and per-project summaries.

## Design decisions for this repo

- Use the repository name `research` to mirror the simple Simon pattern.
- Keep the root instructions in English so coding agents consume them reliably.
- Keep the first full research report in Simplified Chinese because the owner-facing knowledge artifact is for Martin.
- Preserve the automation idea, but make the AI-generated note say "AI-assisted" rather than "every line was written by an LLM", because this repository may include human-edited reports.
- Add `workflow_dispatch` to the README automation so the owner can trigger regeneration manually.

## Verification notes

- Inspected `simonw/research` with a shallow clone into `/tmp/simonw-research-inspect`.
- Verified current GitHub CLI authentication as user `xwbcl123`.
- Checked that `xwbcl123/research` did not exist before creating the new public repository.

