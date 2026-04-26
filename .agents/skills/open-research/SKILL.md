---
name: open-research
description: Create and run reproducible open research projects in a dedicated GitHub research repository. Use when the user asks to start, scope, prompt, execute, review, or publish an open research investigation that should produce a project folder with notes, sources, scripts, artifacts, a final report, and a reviewable git commit or pull request.
---

# Open Research

## Core Rule

Treat each research question as a reviewable project directory, not as a chat answer. Create one top-level kebab-case folder per investigation and keep all generated work inside it unless the user explicitly asks for repository-level changes.

Use the root repository instructions (`AGENTS.md`) as the operating contract when present.

## Project Shape

Create this minimum structure:

```text
topic-name/
  notes.md
  README.md
```

Add scripts, tests, result files, charts, screenshots, or patch files only when they materially support the research. Do not add full external repositories, dependency trees, secrets, private data, or large raw datasets.

Do not create `_summary.md`; repository automation owns generated summaries.

## Workflow

1. Convert the user request into a concrete research question and create a short kebab-case folder name.
2. Start `notes.md` immediately. Record the original question, sources actually used, commands run, experiments attempted, failed paths, and verification evidence.
3. Prefer executable evidence over narrative-only conclusions. If a claim can be tested with code, write and run a script, test, benchmark, data extraction, browser check, or diff.
4. Write `README.md` as the final report. Separate verified findings from hypotheses, limitations, and unverified material.
5. Before committing, check that only the project folder and intentional repository metadata changed. Exclude local app folders, credentials, downloaded repos, caches, and bulky artifacts.
6. Commit and push only after validation passes or after clearly documenting why validation could not be run.

## Prompt Patterns

For ready-to-use prompt templates, read `references/prompt-templates.md`.

Use the templates as task starters, then adapt the scope, sources, output language, and validation criteria to the user's request.

## Report Contract

Every final `README.md` should include:

- final conclusion
- research question and scope
- methods and sources
- experiments, scripts, or evidence produced
- verified findings
- limitations and risks
- reproduction instructions
- next steps only when they are concrete and useful

For Chinese owner-facing reports, write in Simplified Chinese and keep key technical terms in English on first use when ambiguity matters.

## Review Checklist

Before finishing:

- `notes.md` lists the source files, URLs, commands, and tools actually used.
- The report does not upgrade unverified claims into facts.
- Code, commands, or artifacts support the important conclusions.
- The folder is self-contained and reviewable.
- `git status --short` shows no accidental local files.
- `git diff --check` passes.
- Any GitHub Actions or repository automation triggered by the push is checked when practical.
