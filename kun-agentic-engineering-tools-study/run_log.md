# run_log.md

本文件保留精简运行日志；原始输出保存在 `artifacts/*.log`。

## 环境与访问

- `date -u; node --version; npm --version; python3 --version; git --version; gh auth status` → `artifacts/environment.log`。结果：Node v20.20.2、npm 11.4.2、Python 3.12.13、git 2.43.0；`gh` 未安装。
- `gh repo view ...` → `artifacts/*-gh.log`。结果：失败，`gh: command not found`。
- `git clone --depth 1 ...` → `artifacts/*-clone.log`。结果：三个仓库均成功 clone 到 `/tmp/kun-tools-recon`。

## 工具 smoke

- Lavish: `(cd /tmp/kun-tools-recon/lavish-axi && npm exec --yes pnpm@10.18.3 -- install --frozen-lockfile && npm exec --yes pnpm@10.18.3 -- test)` → exit 1，Node/pnpm/`node:sqlite` 兼容性失败。
- Treehouse: `(cd /tmp/kun-tools-recon/treehouse && go test ./...)` → exit 0。
- No Mistakes: `(cd /tmp/kun-tools-recon/no-mistakes && go test ./...)` → exit 0。

## Subject project

- `npm install` → `artifacts/talking-breads-npm-install*.log`。
- `npm run build` → 首次 exit 2，TypeScript deprecation；修正 `tsconfig.json` 后重新运行。
- `npm test` → exit 0。
- `npm run smoke` → exit 0。
- `python3 scripts/validate_talking_breads.py` → exit 0。

## Worktree 实验

- 在 `/tmp/talking-breads-worktree-subject` 初始化 subject repo。
- 运行 `git worktree add ../tb-site-baseline -b site-baseline` 与 `git worktree add ../tb-site-polish -b site-polish`。
- 尝试重复 `site-baseline` 分支，记录 collision 错误。
- 第三次修复加入 React type packages 后：`npm test` exit 0，`npm run smoke` exit 0；`npm run build` 仍 exit 2，缺 `*.css` declaration。对应 `artifacts/talking-breads-*-3.log`。
- 第四次修复加入 `src/vite-env.d.ts` 后：`npm run build` exit 0，`npm test` exit 0，`npm run smoke` exit 0。对应 `artifacts/talking-breads-*-4.log`。

## 2026-06-16 PR review follow-up

- `python3` + GitHub REST API: 读取 `issues/18/comments`、`pulls/18/comments`、`pulls/18/reviews`，确认唯一 inline comment 要求 pin external checkouts。
- 更新 `README.md` 复现命令：Treehouse pin 到 `7f8e436b972af8e1de57b7859c3eade45713a2bd`，No Mistakes pin 到 `f9c5b7f1e8bc5ad18d74667f00e9b7354d365304`。
