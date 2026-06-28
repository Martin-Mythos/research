# 安装 / 构建 / 运行日志

## API Key 状态

环境变量 `DATAFORSEO_API_KEY` 未提供。因此本研究未调用真实 DataForSEO API；所有核心能力验证来自构建、测试、代码审查、文档审查与成本模型脚本。

## Docker 状态

`docker --version` 与 `docker compose version` 均返回 `command not found`，沙箱不支持 Docker runtime。因此 Docker 部署未实际启动，只审查了 `compose.yaml` 与 `docs/SELF_HOSTING_DOCKER.md`。

## 执行命令与结果

| 命令 | 结果 | 证据 |
|---|---:|---|
| `git clone --depth 1 https://github.com/every-app/open-seo /tmp/open-seo-target` | 通过 | 克隆提交 `e9955b46cb9311c02f905337ec580995eaba65de` |
| `pnpm install --frozen-lockfile` | 通过 | `artifacts/pnpm-install.log` |
| `pnpm test` | 通过 | 66 个测试文件、392 个测试全部通过；见 `artifacts/pnpm-test.log` |
| `pnpm run build` | 通过但有 chunk size warning | 见 `artifacts/pnpm-build.log` |
| `pnpm run db:migrate:local && DATAFORSEO_API_KEY= AUTH_MODE=local_noauth pnpm dev --host 127.0.0.1 --port 4177` | 失败/受限 | Wrangler 要求 Node.js >=22，环境为 Node.js 20.20.2；见 `artifacts/local-dev-no-key.log` |
| `python3 scripts/cost_scenario.py` | 通过 | 见 `artifacts/cost_scenario_output.txt` |

## 关键发现

- 构建与单元测试可在没有 DataForSEO key 的情况下完成。
- 实际本地 dev server 未能启动，主要阻塞不是 OpenSEO 应用逻辑，而是当前沙箱 Node.js 版本低于 Wrangler 要求。
- Docker 是官方推荐的本地自托管路径，但当前沙箱没有 Docker。
