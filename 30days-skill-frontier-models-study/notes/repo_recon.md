# Repository Reconnaissance: mvanhorn/last30days-skill

## Commands used

```bash
git clone --depth 1 https://github.com/mvanhorn/last30days-skill /tmp/last30days-recon/last30days-skill
find /tmp/last30days-recon/last30days-skill -maxdepth 3 -type f | sed 's#/tmp/last30days-recon/last30days-skill/##' | sort | head -200
python3 -m pytest tests/test_skill_meta.py tests/test_version_consistency.py -q
```

## Files inspected

- `README.md`
- `skills/last30days/SKILL.md`
- `CONFIGURATION.md`
- top-level structure, tests, fixtures, hooks, and MCP metadata

## Core data model / schema extracted

The repository is not a personal habit tracker despite the name. It is a recency-first research skill and engine. The practical schema is:

1. **Topic/query**: user-provided named entity, comparison, recommendation, or news query.
2. **Query plan**: entity-aware search lanes generated before execution, especially for named entities.
3. **Source adapters**: Reddit, X, YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, Digg, Bluesky, Truth Social, Perplexity, and Web.
4. **Evidence items**: each item carries source, URL, timestamp or recency indicator, engagement metrics, snippet/transcript/comment text, relevance score, and sometimes fun/virality score.
5. **Ranked clusters**: semantically related evidence is merged across sources to avoid duplicate narratives.
6. **Synthesis**: a constrained output contract transforms raw evidence into a brief with inline links and an engine footer.
7. **Persistence**: raw results can be saved under `LAST30DAYS_MEMORY_DIR`, with optional store/watchlist behavior for repeated monitoring.

## Abstraction plan: from recency/social-search skill to 30-interval technology monitoring engine

The useful transferable pattern is not "30 days of practice" as a human habit. It is a loop:

```text
question -> plan -> multi-source probes -> scored evidence -> contradictions -> persisted raw data -> synthesis -> next interval
```

For deep-tech auditing, each interval should record:

- topic and sub-vector, such as latency, context stability, compliance event, mirror velocity, or supply-chain impact;
- source URL and source type;
- observed claim;
- confidence level;
- contradiction or missing-data note;
- measurable fields where possible, such as benchmark score, issue count, context length, quota multiplier, or model availability status.

This converts the skill into a monitoring engine for "Deep Tech Auditing". The research skill being practiced is not coding itself, but repeated evidence calibration: each interval asks whether the previous conclusion survived fresh evidence.
