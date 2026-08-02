# Experiment Plan

## Question and evidence rules

Test whether Loora's structured canvas and agent vocabulary operate locally and whether its service boundaries fail closed. Claims from upstream documentation are not treated as verified until supported by code execution or inspection. No production Loora service, account, database, OAuth provider, billing system, or third-party target will be contacted.

## Experiments

1. **Smoke test:** clone pinned HEAD; install exact Bun version from the manifest; run frozen install, production build, TypeScript check, upstream tests, and Rust WebSocket tests.
2. **Core capability:** execute canvas/agent tests and a new scenario that creates a structured deployment-approval page through the agent transaction vocabulary, applies it, reads the semantic tree, and exports HTML and React.
3. **Representative R&D scenario:** treat agent-created UI as an R&D design artifact. Measure whether one structured transaction produces inspectable nodes and portable exports. Contrast with hand-writing an equivalent static HTML control.
4. **Failure/boundary:** run authentication, missing WebSocket credential, HTML sanitization/import sandbox, transaction validation, and oversized-input tests. Attempt the root test suite without service configuration to observe failure mode. Do not make unauthorized network calls.
5. **Baseline:** compare steps, output forms, validation, and security surface against a manual HTML file. This is a qualitative functional baseline, not a productivity benchmark.

## Acceptance criteria

- Install/build: zero exit status using documented toolchain.
- Core: valid three-node document, nontrivial HTML and React output, zero exit status.
- Boundaries: focused tests demonstrate rejection of missing credentials/token, executable markup, malformed structures, and oversized input.
- Reproducibility: pinned commit, script, commands, and retained logs.
