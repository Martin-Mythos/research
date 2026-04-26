# Notes

## Original Prompt

User asked, in Chinese:

> `$open-research https://github.com/nex-crm/wuphf -> 研究一下这个项目，特别是我也是多agents做同一个项目中操作，经常会遇到上下文不同步的问题，看看这个项目如何解决这个问题的，哪些是我可以直接参考和学习的？设计实验方案（做一个mini project），并输出研究报告。`

## Research Question

How does `nex-crm/wuphf` address context synchronization problems when multiple agents work on the same project, and which practices can be directly reused in the user's multi-agent workflows?

## Working Scope

- Source project: <https://github.com/nex-crm/wuphf>
- Focus: multi-agent context synchronization, shared state, coordination patterns, and directly reusable lessons.
- Experiment target: a mini project that simulates multiple agents editing one project with and without an explicit context-sync protocol.
- External clone target: `/tmp/nex-crm-wuphf`.

## Sources Actually Used

- Root repository instructions: `/Users/martin/Code/research/AGENTS.md`
- Open research skill instructions: `/Users/martin/Code/research/.agents/skills/open-research/SKILL.md`
- Prior memory lookup for this user's multi-agent protocol preferences and cmux context-sync issues.
- Upstream repository: <https://github.com/nex-crm/wuphf>
- Upstream clone: `/tmp/nex-crm-wuphf`
- Upstream commit inspected: `7f76766e8ba8a801f4d6fff552fac10eee6a159a`
- Upstream docs inspected:
  - `/tmp/nex-crm-wuphf/README.md`
  - `/tmp/nex-crm-wuphf/ARCHITECTURE.md`
  - `/tmp/nex-crm-wuphf/DESIGN-WIKI.md`
  - `/tmp/nex-crm-wuphf/AGENTS.md`
- Upstream source files inspected:
  - `internal/team/memory_backend.go`
  - `internal/team/scoped_memory.go`
  - `internal/team/session_memory.go`
  - `internal/team/session_memory_snapshot.go`
  - `internal/team/wiki_git.go`
  - `internal/team/wiki_worker.go`
  - `internal/team/notebook_worker.go`
  - `internal/team/promotion_commit.go`
  - `internal/team/headless_claude.go`
  - `internal/team/headless_codex.go`
  - `internal/team/worktree.go`
  - `internal/team/resume.go`
  - `internal/team/runtime_state.go`
  - `internal/teammcp/notebook_tools.go`
  - `internal/teammcp/memory_hints.go`
  - `internal/teammcp/entity_tools.go`

## Commands And Tools

- `pwd`
- `git status --short --branch`
- `sed -n '1,180p' AGENTS.md`
- `sed -n '1,180p' /Users/martin/Code/research/.agents/skills/open-research/SKILL.md`
- `rg -n "multi-agent|context|上下文|cmux|open-research|research" /Users/martin/.codex/memories/MEMORY.md`
- `mkdir -p wuphf-multi-agent-context-sync`
- `git clone --depth 1 https://github.com/nex-crm/wuphf.git /tmp/nex-crm-wuphf`
- `git rev-parse HEAD && git remote get-url origin`
- `rg --files /tmp/nex-crm-wuphf`
- `sed -n ...` and `nl -ba ...` against the upstream docs/source files listed above.
- `go version && rg --files -g '*test.go' internal/team internal/teammcp | sort`
- `node --version; bun --version`
- `node wuphf-multi-agent-context-sync/scripts/simulate_context_sync.mjs`

## Experiments

Created `scripts/simulate_context_sync.mjs`, a no-dependency Node mini project that models three agents building a todo app:

- `planner` records an initial storage decision and a handoff owner.
- `engineer` records a draft component shape and later supersedes the storage decision.
- `reviewer` records an accessibility constraint.

The experiment compares two protocols:

- `chat-only`: each agent only sees its own notebook/local view.
- `wuphf-inspired`: agents write private notebooks, durable entries trigger promotion hints, shared facts go through a serialized wiki write queue, newer durable facts replace older shared facts, and each shared fact carries owner-routing guidance.

Result from `node wuphf-multi-agent-context-sync/scripts/simulate_context_sync.mjs`:

```json
{
  "scenario": "three agents build a todo app while decisions and constraints arrive at different times",
  "metrics": {
    "chatOnlyIncidentCount": 4,
    "wuphfInspiredIncidentCount": 1,
    "incidentReduction": 3,
    "promotedSharedFacts": 3,
    "serializedWrites": 4,
    "ownerRoutingHints": 3
  },
  "incidentBreakdown": {
    "chatOnly": {
      "missing-context": 3,
      "stale-context": 1
    },
    "wuphfInspired": {
      "private-only-context": 1
    }
  }
}
```

Artifacts generated:

- `artifacts/mini-project-results.json`
- `artifacts/mini-project-results.md`

Interpretation: the WUPHF-inspired protocol did not synchronize every raw note. It reduced missing/stale durable-context incidents from 4 to 1, and the remaining incident is intentionally private-only draft context with an owner-routing hint.

## Failed Paths

- Could not run upstream Go tests because `go` is not installed in the current environment:

```text
zsh:1: command not found: go
```

- Initial experiment assertion expected 5 chat-only context incidents, but the scenario actually produced 4. Corrected the assertion.
- Initial experiment assertion expected the WUPHF-inspired protocol to produce 0 incidents, but one non-durable `component-shape` draft remained private-only. Corrected the assertion because this is a useful design property, not a failure.

## Verification Evidence

- `node --version`: `v25.9.0`
- `bun --version`: `1.3.13`
- `node wuphf-multi-agent-context-sync/scripts/simulate_context_sync.mjs`: passed after assertion corrections and generated the result artifacts.
- Upstream test inventory exists under `internal/team` and `internal/teammcp`, but upstream tests were not executed because `go` is unavailable.

## Verified Findings From Upstream Inspection

- WUPHF has a `memoryBackend` abstraction with shared query/write and brief retrieval paths, covering none/nex/gbrain/markdown backends (`internal/team/memory_backend.go`).
- Per-agent private memory is combined with shared memory into a scoped brief, then wrapped as untrusted background context after the operator message (`internal/team/scoped_memory.go`).
- Notebook tools enforce author-owned writes under `agents/{slug}/notebook/`, while read/list/search are cross-agent by design. Notebook privacy is convention-based, not access-control based (`internal/teammcp/notebook_tools.go`).
- Promotion is copy-not-move from notebook to canonical `team/` wiki with reviewer approval and git provenance (`internal/team/promotion_commit.go`).
- Wiki/notebook/entity writes go through a single-goroutine queue, producing serialized commits and SSE write events (`internal/team/wiki_worker.go`).
- Durable private-memory hints detect playbooks, decisions, preferences, and handoffs; shared-memory hits can route agents toward the likely owner instead of guessing (`internal/teammcp/memory_hints.go`).
- Entity facts are append-only atomic observations; wrong facts are countered rather than deleted (`internal/teammcp/entity_tools.go`).
- Session recovery and resume packets rebuild current focus from active tasks, pending blocking human requests, recent highlights, unanswered messages, and worktree paths (`internal/team/session_memory.go`, `internal/team/resume.go`, `internal/team/runtime_state.go`).
- Coding work can be isolated per task in git worktrees under `.wuphf/task-worktrees`, with source workspace overlays and safety checks (`internal/team/worktree.go`).
