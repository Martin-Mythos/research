The WUPHF multi-agent context sync research demonstrates that the key to effective multi-agent collaboration is not real-time synchronization of all agent-specific contexts, but rather distinguishing, externalizing, and promoting only actionable, shared, and auditable context to a central substrate (e.g., a shared wiki with append-only logs and provenance). Each agent maintains a private notebook for drafts and raw observations, and only promotes mature decisions or facts to a team-accessible wiki following an explicit review or promotion protocol. Synchronization of all chat transcripts is discouraged—instead, only contracts, decisions, handoffs, owners, worktree paths, and evidence are surfaced to the shared layer, with ownership and provenance attached. This approach reduces context drift and improves recoverability compared to chat-based syncing, as verified in simulation experiments.

**Key findings:**

- Separating context into private draft, promoted shared truth, and live owner knowledge decreased context incidents in simulations (from 4 to 1).
- Shared writes are serialized using a single-writer queue, avoiding race conditions.
- Owner routing replaces blanket context sync: agents are directed to ask owners for fresh, non-promoted details.
- Provenance, append-only logs, and runtime snapshots ensure auditable, recoverable shared state.
- The protocol can be immediately reused with a structure of private notebooks, team wikis, single-writer shared access, and owner metadata.

For an applicable protocol and more details, see the [source project](https://github.com/nex-crm/wuphf) and the [mini-project experiment](https://github.com/nex-crm/wuphf/blob/main/scripts/simulate_context_sync.mjs).
