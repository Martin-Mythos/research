# WUPHF Multi-Agent Context Sync Research

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## Final Conclusion

`nex-crm/wuphf` 的关键解法不是把每个 agent 的 live context 实时同步，而是把“可依赖上下文”外置到可审计、可提升、可恢复的共享 substrate 里：每个 agent 有自己的 notebook，成熟内容再 promotion 到 team wiki；共享写入经 single-writer queue 串行化；事实用 append-only log 保留 provenance；恢复时从 runtime snapshot、active tasks、unanswered messages 和 worktree paths 重建当前状态。

对你的多 agent 同项目协作，最值得直接参考的是这条原则：不要同步所有聊天，应该同步 contracts、decisions、handoffs、owners、worktree paths 和 evidence。draft context 留在 worker 私有笔记里，需要时通过 owner routing 去问，而不是让所有 agent 背同一坨过期 transcript。

## Research Scope

- Source project: <https://github.com/nex-crm/wuphf>
- Commit inspected: `7f76766e8ba8a801f4d6fff552fac10eee6a159a`
- Focus: 多 agents 同项目操作时的上下文不同步 (context desynchronization)，以及可迁移到本地 multi-agent workflow 的设计。
- Local experiment: `scripts/simulate_context_sync.mjs`

## Verified Findings

| Mechanism | What WUPHF Does | Why It Helps Context Sync |
| --- | --- | --- |
| Private notebook | `notebook_write` 只允许写 `agents/{slug}/notebook/`，但 read/list/search 可跨 agent 读取。 | raw observations 和半成品想法有地方落地，不必污染 shared truth。 |
| Promotion to wiki | `notebook_promote` 走 reviewer approval，copy-not-move 到 `team/` wiki，并在 source notebook 写回 promoted metadata。 | 把“我刚想到”变成“团队可依赖”的动作显式化。 |
| Shared git substrate | markdown backend 使用本地 git wiki，写入有 commit SHA、author slug、index regeneration。 | 每条共享上下文都有 provenance 和可回滚历史。 |
| Single-writer queue | wiki worker 用一个 goroutine drain `wikiRequests`，队列满就 fail-fast。 | 多 agent 同时写共享记忆时避免 race 和 silent overwrite。 |
| Promotion hints | durable hints 捕捉 playbook、decision、preference、handoff。 | agent 不需要凭感觉决定哪些 private note 应该升级。 |
| Owner routing | shared memory hit 会提示去问相关 owner，而不是猜。 | 最新 working detail 留在 owner 那里，共享 wiki 只承载稳定事实。 |
| Runtime snapshot | snapshot 包含 running tasks、isolated worktrees、pending requests、current focus、next steps。 | session resume 不依赖旧聊天窗口的残留上下文。 |
| Worktree isolation | coding tasks 可进入 per-task git worktree。 | 多 agent 同时改代码时减少文件状态互相污染。 |
| Untrusted memory framing | retrieved memory 被放在 operator prompt 后，并标记为 background/untrusted data。 | 外部记忆不会被当作高优先级指令，降低 prompt injection 风险。 |

## Mini Project

我做了一个 no-dependency Node 实验，模拟三个 agent 一起做 todo app：

- `planner`: 决定 MVP 用 `localStorage`，并记录 reviewer 是 acceptance criteria owner。
- `engineer`: 记录 `TodoItem` draft component shape，后来把 storage 决策改成 in-memory array。
- `reviewer`: 记录 accessibility constraint。

实验比较两种协议：

- `chat-only`: 每个 agent 只看到自己的 local view。
- `wuphf-inspired`: private notebook + promotion hints + shared wiki + serialized writes + owner routing。

结果：

| Metric | chat-only | wuphf-inspired |
| --- | ---: | ---: |
| Context incidents | 4 | 1 |
| Missing context | 3 | 0 durable-context misses |
| Stale context | 1 | 0 |
| Shared promoted facts | 0 | 3 |
| Serialized writes | 0 | 4 |
| Owner routing hints | 0 | 3 |

剩下的 1 个 incident 是 `component-shape`：它只是 engineer 的 draft observation，没有被 promoted。WUPHF 风格没有强行同步它，而是提示 reviewer 去问 `@engineer`。这点很重要：好协议不追求“所有人知道所有事”，而是让“哪些东西是 shared truth、哪些东西只是 owner draft”变得明确。

Artifacts:

- `scripts/simulate_context_sync.mjs`
- `artifacts/mini-project-results.json`
- `artifacts/mini-project-results.md`

## What You Can Reuse Directly

1. 为每个 worker surface 建一个 `agents/{slug}/notebook/` 或等价目录，要求它记录 raw observations、local blockers、assumptions、handoff notes。
2. 建一个 `team/` shared wiki，只放 promoted decisions、contracts、owners、runbooks、acceptance criteria、artifact links。
3. promotion 必须 copy-not-move：source notebook 保留原始上下文，shared wiki 只复制可依赖版本，并写回 `promoted_to`、`promoted_by`、`promoted_commit_sha`。
4. 对 shared memory 使用 single-writer queue 或 PR/review gate。多 agent 不要直接并发改同一个 canonical file。
5. 所有 shared decision 都带 owner、timestamp/source、commit/ref、supersedes/contradicts metadata。
6. 遇到 shared memory 指向某个 owner 时，协议应要求 agent `@owner` 获取 fresher working context，而不是自行脑补。
7. 每次 resume 都从 live runtime snapshot 重建：active tasks、blocking requests、worktree paths、recent highlights、pending reviews。不要从旧 transcript 猜状态。
8. 多 coding agents 默认用 per-task worktree 或 sibling output folder，master agent 只整合 promoted artifacts。
9. 把 external memory 明确标成 untrusted background context，放在 operator instruction 后面，避免它变成隐形系统指令。

## Recommended Protocol For Your Setup

可以把 WUPHF 的思想翻译成你现有 master-agent / worker-surfaces 工作流：

```text
worker surface
  writes -> agents/{worker}/notebook/*.md
  owns   -> task worktree or sibling output folder
  posts  -> short status + artifacts + promotion candidates

master agent
  reads       -> notebooks + live topology + task status
  promotes    -> team/decisions, team/contracts, team/handoffs
  serializes  -> shared writes through one queue / one final commit path
  resumes     -> from runtime snapshot, not stale chat
```

最小落地版本不需要完整 WUPHF：

- `team/decisions.md`: append-only decision log。
- `team/handoffs.md`: owner、next step、deadline、blocked-by。
- `agents/{slug}/notebook/YYYYMMDD.md`: 每个 worker 私有草稿。
- `team/runtime-snapshot.json`: active tasks、owners、worktree paths、last artifact。
- `scripts/promote-note`: 从 notebook 复制片段到 shared wiki，并追加 provenance。

## Limitations

- 没有运行 upstream Go tests，因为当前环境没有 `go`：`zsh:1: command not found: go`。
- 实验是 mechanism simulation，不是完整运行 WUPHF office，也没有接入 Claude/Codex/headless runtime。
- 对 WUPHF 的行为判断来自文档和源码 inspection；没有验证其 SaaS/Nex backend 或真实 web UI runtime。

## Reproduction

```bash
cd /Users/martin/Code/research
node wuphf-multi-agent-context-sync/scripts/simulate_context_sync.mjs
```

Expected summary:

```json
{
  "chatOnlyIncidentCount": 4,
  "wuphfInspiredIncidentCount": 1,
  "incidentReduction": 3,
  "promotedSharedFacts": 3,
  "serializedWrites": 4,
  "ownerRoutingHints": 3
}
```

## Bottom Line

WUPHF 最值得学习的不是某个 UI 或 MCP tool 名字，而是它把 agent context 拆成了三个不同等级：private draft、promoted shared truth、live owner knowledge。你的多 agent 工作流只要先实现这三个等级，再加 single-writer shared writes 和 resume snapshot，就能显著减少“每个 agent 以为自己知道当前状态，但其实拿着不同版本”的问题。
