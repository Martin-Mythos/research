# 研究笔记

## 原始研究问题
- 深入剖析 `EveryInc/compound-engineering-plugin`，并在 AI 协作 Markdown 编辑器敏捷场景下做三组实验（需求摄取、工程拆解、模糊需求抗压）。

## 过程记录

## 数据源与命令
- 代码仓库：`https://github.com/EveryInc/compound-engineering-plugin`
- 配套指南：`https://every.to/guides/ai-product-management-guide`
- 关键命令：
  - `git clone --depth 1 https://github.com/EveryInc/compound-engineering-plugin /tmp/compound-engineering-plugin`
  - `rg --files plugins/compound-engineering`
  - `sed -n '1,260p' plugins/compound-engineering/skills/ce-plan/SKILL.md`
  - `python3 generate_artifacts.py`
  - `jq '.tickets|length' artifact-exp2-engineering-tickets.json`

## 实验与结果
- 实验一（需求摄取）：通过源码确认 ce-plan 以 `$ARGUMENTS` 注入 `<feature_description>`，并在 Phase 0/1 执行“需求文档检索→bootstrap→并行研究”流程。
- 实验二（工程拆解）：根据 ce-plan 的“决策优先、测试场景、实现单元”规则，推演出 5 张工程卡片，覆盖 CRDT/OT、WebSocket、op 协议、presence、离线补偿。
- 实验三（模糊需求）：依据 SKILL.md 的澄清与假设分流机制，推演输出偏向 Spike/基线测量，而非直接幻觉式方案。

## 失败路径
- 失败路径：尝试在本沙盒直接“运行”ce-plan（作为宿主 agent 命令）不可行，因为该插件主要是“技能/提示词+转换器”，并非一个可独立执行业务逻辑的服务端。
- 放弃原因：缺少 Claude/Codex 宿主运行时与交互工具链（AskUserQuestion/request_user_input）。
- 兜底策略：转为“源码级逻辑推演 + mock 输出产物”并保留 JSON artifact。

## 验证证据
- `python3 generate_artifacts.py > verification.log` 成功。
- `jq` 检查结果：实验二卡片数量=5，实验三输出条目=3。

## PR 复审修订记录
- 用户要求“根据 PR review comments 修订”。当前环境未提供可直接读取 GitHub inline comments 的 API 凭据与链接上下文。
- 采取补强动作：新增 `extract_evidence.py`，从上游仓库源码自动提取关键证据（parser、参数注入、issue tracker 路由）并输出 `artifact-source-evidence.json`。
- 失败-恢复：首次运行因 `/tmp/compound-engineering-plugin` 不存在报错（FileNotFoundError），随后重新 clone 上游仓库并复跑成功。

## 新增验证
- `python3 extract_evidence.py`：成功生成 `artifact-source-evidence.json`。
