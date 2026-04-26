# Lightweight Research Contract

Use this contract when applying `$open-research` inside a repo that is not primarily a research repository.

## Placement

Create or reuse:

```text
research/
  README.md
  topic-name/
    notes.md
    README.md
```

Do not place open-ended research folders at the app repo root unless the user explicitly asks.

## `research/README.md` Starter

```markdown
# Research

This directory contains reproducible research investigations related to this repository.

Each subdirectory is one investigation and should include:

- `notes.md` with sources actually used, commands run, failed attempts, and verification evidence
- `README.md` with final conclusion, methods, verified findings, limitations, and reproduction steps
- scripts, tests, structured results, screenshots, charts, or patches only when they support the evidence

Do not commit secrets, private data, full external repositories, dependency directories, caches, or large raw datasets.
```

## Local `.gitignore` Additions

Add ignore rules only when needed and scoped to generated research clutter:

```gitignore
research/**/.venv/
research/**/__pycache__/
research/**/*.pyc
research/**/node_modules/
research/**/.env
research/**/.env.*
```

Do not rewrite the repo's existing `.gitignore` style. Append only minimal entries if the investigation creates these files.

## Commit Boundary

For ordinary code repos, keep research commits narrow:

- `research/README.md` if newly created
- `research/<topic-name>/...`
- minimal `.gitignore` additions only if needed

Avoid unrelated app code changes unless the research explicitly requires a patch or demo.
