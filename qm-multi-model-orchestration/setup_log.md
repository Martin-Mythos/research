# Setup Log

Commands and environment observations are recorded here as the investigation proceeds.

## Environment and commands
See `artifacts/environment.txt` for exact outputs. Major commands:
- `git clone https://github.com/yc-software/qm.git /tmp/qm-target` → success at SHA `7f2c916...`.
- `npm ci --ignore-scripts` in clone → engine warnings under Node 20/npm 11.4; terminal status not reliably captured.
- `npx --yes --package=node@24.15.0 node --version` → failed (`ENOENT` in temporary npm cache).
- `curl -fsSL https://nodejs.org/dist/v24.15.0/node-v24.15.0-linux-x64.tar.xz | tar ...` → success; `/tmp/node24/bin/node --version` was `v24.15.0`.
- Focused upstream test → 4 passed, 0 failed.

No credentials were read or used. No target source was modified. The external clone and its 1.1 GB dependency tree remain outside the committed research directory.
