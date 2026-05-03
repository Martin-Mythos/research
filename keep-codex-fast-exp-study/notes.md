# Notes

## Original prompt
测试 https://github.com/vibeforge1111/keep-codex-fast ，尽可能覆盖其所有场景，验证是否能让 Codex 更快，并产出基于实验的深度研究报告。

## Plan
- 克隆并审阅项目文档/脚本，枚举“所有场景”。
- 在可复现环境中逐项运行场景，记录成功/失败与性能指标。
- 设计对照实验（baseline vs keep-codex-fast 配置）验证“更快”来源。
- 形成结论并区分已验证事实与推测。


## Commands run
- git clone https://github.com/vibeforge1111/keep-codex-fast.git external_repo

- python external_repo/tests/smoke_test.py (pass)
- python external_repo/scripts/keep_codex_fast.py --help
- python external_repo/tests/smoke_test.py
- python benchmark_keep_codex_fast.py --threads 1500

## Data sources / URLs
- https://github.com/vibeforge1111/keep-codex-fast
- external_repo/README.md
- external_repo/scripts/keep_codex_fast.py
- external_repo/tests/smoke_test.py

## Experiments and outcomes
1) 官方 smoke tests：通过。覆盖 report / backup-only / apply / alias detection。
2) CLI 场景枚举：通过 --help 验证支持参数（--details, --wait-for-codex-exit 等）。
3) 性能微基准（1500旧会话，fake codex home）：
   - report: 0.285s
   - backup-only: 0.299s
   - apply: 0.412s
   说明脚本自身额外开销低，apply 由于归档/写入略慢。

## Failed paths
- 首版 benchmark 动态导入失败（dataclass module 未注入 sys.modules），报错 AttributeError。已修复为先注册 sys.modules['keep_codex_fast']=module。

## Verification evidence
- smoke_test 输出包含："smoke tests passed"。
- apply 模式输出包含 archived_sessions_manifest / moved-worktrees.jsonl / config_pruned applied 等关键字，证明归档与清理逻辑确实执行。
