# 工作笔记：Shifu 多模型调度与成本优化实证研究

## 原始研究问题

Can Shifu intelligently route tasks among GPT5.6 Lula, GPT5.4 Mini, and GPT5.3 Codex Spark to build a fully functional "Vocabulary Memorization" mini-app while significantly lowering costs?

目标仓库：https://github.com/vikingmute/shifu

## 工作日志

## 初始命令

```bash
mkdir -p shifu-multimodel-cost-optimization-study/{notes,artifacts,external}
```

## 命令记录：克隆与静态检查

- `git clone --depth 1 https://github.com/vikingmute/shifu /tmp/shifu-target`：成功。
- `sed -n ... README.md` 与 `skills/shifu/SKILL.md`：仓库主要由一个 Agent Skill 组成。

## 实验与验证记录

- 运行 `npx skills add vikingmute/shifu`：成功安装 skill；安装副本因提交范围要求已删除，日志保留在 `artifacts/npx_skills_add.log`。
- 编写并运行 `artifacts/mock_shifu_experiment.py`：生成 mock routing logs、故意错误版本与修复版本 Vocabulary CLI。
- 运行 `python3 -m py_compile .../vocab_app.py`：通过。
- 运行 `python3 .../vocab_app.py stats`：输出 `{"total_words": 2}`。
- 运行 `python3 .../vocab_app.py quiz --answer 放弃`：输出 `correct`。

## 失败路径与限制

- Shifu 仓库没有可执行多模型 router，因此不能直接运行真实 Lula/Mini/Spark 调度。
- 真实 API 与真实成本未调用/未采集；全部成本数字均为本地 mock 价格表模拟。
- 官方安装命令会写入 `.agents/skills/shifu`；为遵守最终提交范围，验证后删除该安装副本。

## 2026-07-25 评审修订

### 评审意见获取

- `gh pr status`：失败，因为环境没有安装 `gh`。
- 查询 GitHub 公共 API `GET https://api.github.com/repos/Martin-Mythos/research/pulls?state=all&per_page=100`：未返回标题含 Shifu 的 PR。
- 当前 checkout 没有配置 Git remote。因此无法取得未随提示提供的 inline comments；改为逐项审计上一版 diff 中可直接观察的问题。

### 发现并修复的问题

1. 上一版只记录 context hash，没有断言相邻 handoff 的输入等于上一步输出，不能支撑“上下文未丢失”的结论。
   - 修复：增加 `parent_output_hash`、`handoff()` 断言和必需字段检查。
2. 上一版错误恢复只经过 Lula，未按实验计划把 Mini 纳入修复链路。
   - 修复：路由改为 Spark 失败 → Lula 诊断 → Mini 修复计划 → Spark 重写。
3. 上一版应用只做手工 smoke test，没有自动回归测试。
   - 修复：增加 `artifacts/test_experiment.py`，覆盖 quiz、add 持久化、stats、故意语法错误、修复输出、路由顺序、lineage 和 baseline token 等价性。
4. 上一版成本与延迟数字容易被误读成实测值。
   - 修复：JSON 顶层增加 method 限定，报告统一称为“假设驱动的确定性模拟”；不再把该结果作为 Shifu 成本优化 efficacy 的实证证明。

### 修订后验证证据

```bash
python3 artifacts/mock_shifu_experiment.py > artifacts/mock_experiment_output.json
python3 -m unittest discover -s artifacts -p 'test_*.py' -v
```

结果：5 项测试全部通过。协议检查为 `lineage_ok=true`、`routing_ok=true`、`required_context_ok=true`。更新后的假设值为多模型 0.026296 / 7.0s，单旗舰 0.082860 / 12.0s，模拟差异 68.26%。
