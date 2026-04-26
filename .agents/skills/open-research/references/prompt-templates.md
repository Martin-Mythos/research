# Open Research Prompt Templates

## New Investigation

```text
Use $open-research in /Users/martin/Code/research.

Create a new folder called <topic-name>.

Research this question:
<research question>

Requirements:
- maintain notes.md throughout the work;
- list sources actually used, commands run, failed attempts, and verification evidence;
- use executable experiments, scripts, tests, benchmarks, data extraction, diffs, or screenshots when possible;
- write a final README.md with conclusion, methods, sources, verified findings, limitations, and reproduction steps;
- keep all work inside the new folder;
- do not create _summary.md;
- do not commit full external repositories, dependency directories, secrets, private data, or large raw datasets.
```

## Web Research With Evidence

```text
Use $open-research in /Users/martin/Code/research.

Create a new folder called <topic-name>.

Investigate <question> using web sources and primary documentation where possible.

Deliver:
- notes.md with exact URLs, source titles, dates checked, and evidence snippets or summaries;
- README.md with final conclusion, source quality assessment, verified facts, unknowns, and limitations;
- small scripts or structured data files only if they help reproduce the evidence extraction.

Use current web verification for facts that may have changed. Keep unverified claims in a limitations or open questions section.
```

## Technical Feasibility Experiment

```text
Use $open-research in /Users/martin/Code/research.

Create a new folder called <topic-name>.

Test whether <technology/library/API> can <desired capability>.

Deliver:
- notes.md with setup commands, versions, failed approaches, and run outputs;
- minimal scripts/tests/demos needed to prove the result;
- README.md with conclusion, environment, reproduction steps, verified behavior, limitations, and tradeoffs.

Prefer a small reproducible demo over a broad prose survey.
```

## Benchmark Or Comparison

```text
Use $open-research in /Users/martin/Code/research.

Create a new folder called <topic-name>.

Compare <options> for <use case>.

Deliver:
- notes.md with sources, assumptions, commands, and raw result locations;
- benchmark or comparison scripts where practical;
- structured result files such as CSV/JSON when useful;
- README.md summarizing methodology, results, caveats, and recommendation.

Make the comparison reproducible and clearly state what was not measured.
```

## Existing Research Review

```text
Use $open-research in /Users/martin/Code/research.

Review the existing project folder <topic-name>.

Check:
- whether notes.md lists sources actually used;
- whether README.md conclusions are supported by evidence;
- whether generated artifacts are necessary and small enough;
- whether any secrets, external repos, dependency trees, or local app files are included;
- whether reproduction instructions still work.

Make minimal fixes in place and report remaining risks.
```
