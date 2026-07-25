# 运行日志

## 1. 克隆目标仓库

```bash
git clone --depth 1 https://github.com/vikingmute/shifu /tmp/shifu-target
```

结果：成功。仓库核心文件为 `README.md` 与 `skills/shifu/SKILL.md`。

## 2. 官方安装命令

```bash
npx skills add vikingmute/shifu
```

结果：成功安装 skill 到 `./.agents/skills/shifu`。为遵守本研究仓库“最终提交只包含研究目录”的要求，安装验证后已删除该工作区安装副本。完整输出保存于 `artifacts/npx_skills_add.log`。

重要结论：该命令证明 Shifu 可作为 Agent Skill 安装；它没有初始化独立多模型 API router、token meter 或运行时服务。

## 3. Mock 多模型实验

```bash
python3 shifu-multimodel-cost-optimization-study/artifacts/mock_shifu_experiment.py
python3 -m py_compile shifu-multimodel-cost-optimization-study/artifacts/vocab_app.py
python3 shifu-multimodel-cost-optimization-study/artifacts/vocab_app.py stats
python3 shifu-multimodel-cost-optimization-study/artifacts/vocab_app.py quiz --answer 放弃
```

结果：

- mock harness 生成 `artifacts/vocab_app_bad.py`，其中包含故意语法错误。
- harness 使用 Python AST 检测到语法错误。
- harness 生成修复后的 `artifacts/vocab_app.py`。
- `py_compile` 通过。
- `stats` 输出 `{"total_words": 2}`。
- `quiz --answer 放弃` 输出 `correct`。

## 4. 成本与延迟模拟结果

结果文件：`artifacts/mock_routing_logs.json` 与 `artifacts/mock_experiment_output.json`。

- 多模型模拟成本：0.012628。
- 单旗舰模型模拟成本：0.043080。
- 模拟节省：70.69%。
- 多模型模拟延迟：6.2s。
- 单旗舰模拟延迟：10.0s。

注意：这些是研究 harness 的相对模拟值，不是真实供应商价格或真实 Shifu telemetry。
