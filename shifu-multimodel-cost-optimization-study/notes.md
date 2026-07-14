# 工作笔记：Shifu 多模型调度与成本优化实证研究

## 原始研究问题

Can Shifu intelligently route tasks among GPT5.6 Lula, GPT5.4 Mini, and GPT5.3 Codex Spark to build a fully functional "Vocabulary Memorization" mini-app while significantly lowering costs?

目标仓库：https://github.com/vikingmute/shifu

## 工作日志

## 初始命令

```bash
mkdir -p shifu-multimodel-cost-optimization-study/{notes,artifacts,external}
```

\n## 命令记录：克隆与静态检查
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
