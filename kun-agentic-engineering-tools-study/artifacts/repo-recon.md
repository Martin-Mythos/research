# repo-recon.md

## 环境

见 `environment.log`。`gh` 未安装，因此 `gh auth status` 和 `gh repo view` 均失败；使用 `git clone --depth 1` 与本地文件侦察作为 fallback。

## Lavish / lavish-axi

- URL: https://github.com/kunchenguid/lavish-axi
- 克隆：成功，SHA 见 `lavish-axi-topfiles.log`。
- 类型：Node/TypeScript-ish JavaScript CLI + local browser editor AXI。
- 包管理：pnpm，`package.json` + `pnpm-lock.yaml`。
- 入口：`bin/lavish-axi.js`；README 命令包括 `lavish-axi <html-file>`, `poll`, `end`, `stop`, `playbook`, `design`, `setup hooks`, `server`。
- 安装：推荐 `npx skills add ...` 或直接 `npx -y lavish-axi`；源码路径 `pnpm install --frozen-lockfile && pnpm run build && pnpm link`。
- 安全提示：README 明确说明默认 loopback；若绑定 `0.0.0.0` 会暴露未经认证的本地文件服务。

## Treehouse

- URL: https://github.com/kunchenguid/treehouse
- 克隆：成功，SHA 见 `treehouse-topfiles.log`。
- 类型：Go CLI，管理可复用 git worktree 池。
- 包管理/构建：Go module + Makefile；`make build`, `make test`, `make lint`。
- 入口：`main.go`, `cmd/*`；README 命令包括 `treehouse/get/status/return/destroy/init/update`。
- 安装：curl installer、Nix、`go install github.com/kunchenguid/treehouse@latest`、源码 `make install`。
- 安全提示：repo-level hooks 被忽略；user-level hooks 可执行 shell 命令，需审计 `~/.config/treehouse/config.toml`。

## No Mistakes

- URL: https://github.com/kunchenguid/no-mistakes
- 克隆：成功，SHA 见 `no-mistakes-topfiles.log`。
- 类型：Go CLI + Git proxy/gate + TUI + agent skill + docs site。
- 包管理/构建：Go module + Makefile；docs 使用 Astro/npm。
- 入口：`main.go` 与 workflow/test 文件；README 流程为 `no-mistakes init`, `git push no-mistakes`, `no-mistakes` TUI, `/no-mistakes` skill。
- 安装：curl installer、Go/source 文档。
- 外部依赖：真实远程、GitHub/PR 权限、AI agent CLI/API quota、CI 集成；完整能力无法纯离线验证。
