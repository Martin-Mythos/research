# 工作笔记

## 原始问题

比较 `clockless-org/html-anything` 与 `nyblnet/bento` 在三类 HTML 场景、可编辑性、上下文工程和 Cloudflare R2 工作流上的表现；在无私有 API key 条件下，以可复现实验严格区分文档声明、沙箱验证、失败项与模型相关推断。全部叙述性输出使用中文。

## 工作记录

- 2026-07-25：创建独立研究目录，读取根级 `AGENTS.md` 与 `open-research` skill。

## 实际使用的命令、脚本与来源

- 来源 URL：`https://github.com/clockless-org/html-anything.git`、`https://github.com/nyblnet/bento.git`。
- `git clone --depth 1` 到 `/tmp/ha-study-upstreams`；固定 SHA 见 `run_log.md`。
- 环境采集：`uname -a`、读取 `/etc/os-release`、`git/node/npm/pnpm/python/docker --version`。
- 上游验证：HTML-Anything 执行 `npm ci && npm run build && npm test`；Bento Slides 执行 `npm ci && npm run build:single`。
- 本地脚本：`scripts/generate_benchmark.py`、`scripts/validate_artifacts.py`、`scripts/publish_r2_mock.sh`。

## 实验结果与失败路径

- HTML-Anything：81/81 测试通过；Node v20.20.2 不在 `pdfjs-dist@5.7.284` 声明的 engine 范围，安装只 warning，测试仍通过。
- Bento：single-file build 成功；压缩日志为约 `1185KB → 587KB`。
- 三场景 × 两载体共六个 HTML 已生成，约束与相对依赖检查通过。
- 未尝试真实 Opus 5 / GPT-5.6-Sol API 调用：环境未提供相应私有 key，按安全规则改用 deterministic fixtures。因而放弃“模型胜负”和 token/latency 实测结论。
- 未实际上传 R2：无 Cloudflare 凭据；改为本地 staging + SHA-256 manifest。

## 验证证据

- 上游详细 TAP 与 build 输出保存在 `run_log.md`。
- `artifacts/metrics.json` 保存逐文件机器指标。
- Mock R2 命令与输出在最终验证后追加。

- Mock R2 staging 输出：Mock R2 暂存完成：7 个 HTML 对象；目录：/tmp/html-study-r2-staging
- ：7 个对象全部通过。
