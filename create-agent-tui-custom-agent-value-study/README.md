# create-agent-tui 自定义 Agent 价值研究

## 结论（Final Conclusion）
`create-agent-tui` 的核心价值不是“让模型更聪明”，而是把 **可控性（control）**、**可操作性（operability）**、**可持续性（persistence）** 和 **可集成性（integration）** 系统化地包装成一个可复用脚手架。对于一次性问答场景，价值有限；但在需要工具调用、审批治理、多会话追踪、终端工作流或服务化嵌入时，自定义 agent 的收益显著。

---

## 研究问题与范围

### 研究问题
1. `create-agent-tui` 提供了哪些“自定义 agent”能力？
2. 这些能力解决了什么实际问题？
3. 在什么场景下值得用，什么场景下不值得？

### 范围
- 研究对象：`OpenRouterTeam/skills` 仓库中的 `skills/create-agent-tui`。
- 方法：文档与样例代码静态分析 + 可复现实验（能力覆盖对比）。
- 非范围：不评价具体模型效果（如代码正确率、推理质量），因为该 skill 主要是“代理壳层/工程能力”而非模型算法。

---

## 方法与数据来源（Methods & Sources）

### 数据来源
- 上游 skill 主文档：`SKILL.md`, `README.md`, `metadata.json`
- 上游参考文档：`references/*.md`
- 上游样例实现：`sample/src/*.ts`
- 以上文件均以 GitHub Raw/API 方式抓取并固化到 `artifacts/upstream/`。

### 实验设计

#### 实验 1：能力证据扫描（evidence scan）
- 脚本：`scripts/evidence_scan.py`
- 目标：验证关键能力是否能在官方文档或样例代码中找到直接证据（如 tool modes、session persistence、approval、layered config、server entrypoints 等）。
- 输出：`artifacts/results/evidence_scan.json`

#### 实验 2：场景能力覆盖对比（capability coverage）
- 脚本：`scripts/evaluate_use_cases.py`
- 数据：`data/use_cases.json`（5 个典型场景）
- 对比对象：
  - **Custom Agent（create-agent-tui）**：按上游文档/样例声明的能力赋值
  - **Baseline Chat**：仅具备 basic chat completion，无自定义代理壳层
- 指标：每个场景下“需求能力覆盖率”（covered/total）
- 输出：`artifacts/results/capability_matrix.json`、`artifacts/results/capability_matrix.md`

---

## 实验结果

### 实验 1 结果（证据存在性）
证据扫描表明，目标能力在文档或样例中均可定位，支持“这是一个偏工程化代理脚手架”的判断（详见 `evidence_scan.json`）。

### 实验 2 结果（覆盖率）
| 场景 | Custom agent 覆盖率 | Baseline 覆盖率 | 差值 |
|---|---:|---:|---:|
| 受控代码助手（需要审批） | 1.00 | 0.00 | +1.00 |
| 一次性问答/聊天 | 1.00 | 1.00 | 0.00 |
| 长周期研究代理（多会话追踪） | 1.00 | 0.00 | +1.00 |
| 运维排障助手（终端优先） | 1.00 | 0.00 | +1.00 |
| 后端服务内嵌 Agent（API entrypoint） | 1.00 | 0.00 | +1.00 |

解释：
- 一次性问答场景几乎没有工程壳层增益。
- 其他 4 类场景的主要需求都依赖“代理系统能力”（工具治理、审批、会话持久化、终端交互、模块化/服务化），因此 custom agent 明显优于 baseline chat。

---

## 已验证发现（Verified Findings）
1. `create-agent-tui` 明确定位为“agent TUI 脚手架”，覆盖终端 UI、工具显示模式、会话持久化、配置、工具定义与入口点，而非单纯 prompt 模板。
2. 文档强调来自多个生产代理系统的架构借鉴（分层、审批语义、配置与日志），说明其价值主轴是工程治理能力。
3. 从样例结构看，已经提供 `agent/config/renderer/session/tools/commands` 等模块分离，便于按团队需求扩展。
4. 在需要治理与长期运行的场景中，自定义 agent 的能力覆盖显著高于普通聊天壳；在一次性问答场景中增益不明显。

---

## 推测与边界（Speculation / Non-verified）
1. 覆盖率高不等于业务 ROI 一定更高：真实收益还取决于团队工程成熟度与维护成本。
2. 未进行线上吞吐/延迟/故障恢复压测，因此不能直接推断生产级性能上限。
3. 未比较其他 agent 框架（如 LangGraph/AutoGen）的开发效率与可维护性，本研究结论仅针对“与基础聊天壳层相比”。

---

## 适用场景与不适用场景

### 推荐使用自定义 agent（高价值）
- 需要工具调用并区分只读/危险操作，且要审批流。
- 需要会话持久化、可追溯日志、多轮任务恢复。
- 以终端为主的工程团队（代码、运维、SRE、SecOps）。
- 需要把 agent 能力嵌入服务端入口（API/server entrypoint）。

### 不推荐优先使用（价值有限）
- 只做偶发问答、文案润色、轻交互，无工具治理需求。
- 团队暂时无法承担脚手架维护成本（配置、工具、升级、测试）。

---

## 复现步骤（Reproduction）
在仓库根目录执行：

```bash
python3 create-agent-tui-custom-agent-value-study/scripts/evidence_scan.py
python3 create-agent-tui-custom-agent-value-study/scripts/evaluate_use_cases.py
cat create-agent-tui-custom-agent-value-study/artifacts/results/capability_matrix.md
```

---

## 风险与下一步
1. 可补充真实任务基准（如“修复 bug + 运行测试 + 提交 patch”）衡量端到端成功率与人工介入时长。
2. 可引入成本指标（token、时间、人力）做“增益/成本比”。
3. 可加入与其他 agent 框架横向对比，验证迁移成本与生态差异。
