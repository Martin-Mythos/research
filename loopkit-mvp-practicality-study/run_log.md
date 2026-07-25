# 运行日志

## 环境记录
环境信息写入 `setup_log.md`。关键结果：Python 与 pytest 可用，FastAPI 不可用，因此改用标准库 MVP。

## 仓库安装与复制
最初执行 `git clone --depth 1 https://github.com/Archive228/loopkit /tmp/loopkit-src`。复核阶段通过 Git 历史锁定实验日对应提交 `22101ff114cbf80bf3d14d41c8c662f507b1b971`（33 个技能目录）。为遵守“不提交外部仓库完整副本”的约束，最终产物删除了复制的 LoopKit 文件，改用 `scripts/install_pinned_loopkit.sh` 在复现时安装固定快照。

## MVP 实现轨迹
创建了 `src/data/store.py`、`src/services/auth.py`、`src/services/tasks.py`、`src/routes/api.py` 和 `tests/test_api.py`。实现了注册、登录、token 签发、token 验证、任务 owner_id 过滤与跨用户 404。

## LoopKit 运行模拟
真实 `run.sh` 依赖 `claude` CLI；本沙箱没有私有凭证，且任务要求避免外部计费 API。因此没有实际调用 `claude -p`，而是按 `run.sh` 的文件契约创建 `PROMPT.md` 与 `IMPLEMENTATION_PLAN.md`。修订后的扫描器不再用子字符串启发式推断，而是公开列出实验协议选定的 10 个技能及逐项理由；输出明确标记为模拟、而非运行时观测。

## 测试输出
命令：`python -m pytest -q tests`，工作目录：`artifacts/mvp-target-codebase/`。

```text
...                                                                      [100%]
6 passed in 1.74s
```

## 失败路径
- 从仓库根直接运行 pytest 时出现 `ModuleNotFoundError: No module named 'src'`，原因是测试工作目录不在 MVP 根目录；改为在 MVP 根目录运行后通过。
- 未实际执行 Claude CLI loop runner；原因是环境没有外部 LLM 凭证，且不应触发潜在计费调用。
- 初版扫描器错误地使用 `word in keywords_string` 子字符串判断，使 `a`、`it` 等停用词造成 29/33 的大量误报；该路径已废弃，修订版改为显式、可审计的实验协议，结果为 10/33。
- 初版提交复制了完整外部技能目录；复核后删除，并以固定提交安装脚本与来源快照替代。
- 没有保留“先红后绿”的真实时间序列，也没有运行裸奔 Agent 对照组；因此 TDD 约束力和成功率提升均保持未验证。
