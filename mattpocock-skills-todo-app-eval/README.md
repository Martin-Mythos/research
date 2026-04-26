# mattpocock/skills 的 Todo App 实验研究

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## Final Conclusion

`mattpocock/skills` 更像一组“工作流压缩包”，而不是可执行插件库。每个 skill 用 `SKILL.md` 把 agent 的触发条件、操作顺序、质量标准和反模式写清楚；真正的价值来自把模糊任务强制转成较稳定的工程节奏，例如先设计接口、再按行为测试推进、最后用用户视角 QA 条目收口。

在本次 todo app 小实验中，最有效的组合是：

- `design-an-interface`：让 todo 模块先比较多个公开接口形状，避免一开始就被实现细节绑住。
- `tdd`：要求通过 public interface 做行为测试，实际抓到了一个空列表时 invalid filter 不报错的 bug。
- `qa`：把测试和实验中发现的问题改写成用户视角 issue，适合后续产品化拆分。

## Research Question And Scope

研究问题：`mattpocock/skills` 如何组织 agent skills？把其中几个 skill 应用于一个真实但很小的 todo app 时，它们具体发挥什么作用？

范围限制：

- 检查源项目：<https://github.com/mattpocock/skills>
- 本地克隆 commit：`60aa99c0230fbac087514ba5fca2ae6e519965fe`
- 实验对象：一个无依赖的 Node todo domain module
- 不评估 Claude Code 的真实安装体验，也不创建真实 GitHub issues

## Methods And Sources

实际使用的来源：

- GitHub 页面：<https://github.com/mattpocock/skills>
- 本地克隆：`/tmp/mattpocock-skills`
- 关键 skill 文档：`tdd`、`design-an-interface`、`qa`、`domain-model`、`setup-pre-commit`、`to-issues`
- 本研究 repo 根约定：`AGENTS.md`
- 实验代码：`experiment/todo-app`

产出的可复现 artifact：

- `scripts/analyze-skills.mjs`：解析 cloned repo 中的 skill frontmatter
- `artifacts/skills-index.json`：结构化 skill index
- `artifacts/skills-index.md`：可读 skill index
- `experiment/todo-app/docs/interface-designs.md`：todo app 接口设计比较
- `experiment/todo-app/src/todo-list.js`：实验实现
- `experiment/todo-app/test/todo-list.test.js`：行为测试
- `artifacts/qa-session-output.md`：按 `qa` 模板生成的本地 issue 文档

## Experiment

### 1. Skill Inventory

脚本扫描发现该仓库当前有 21 个 `SKILL.md`。按本研究脚本的轻量分类：

| Category | Count |
| --- | ---: |
| planning-design | 11 |
| development | 4 |
| writing-knowledge | 3 |
| tooling-setup | 1 |
| other | 2 |

这个分布说明项目重点不是“写代码自动化命令”，而是把 agent 行为约束成计划、设计、issue、TDD、QA、知识管理等流程。

### 2. Todo App Interface Design

应用 `design-an-interface` 的“Design It Twice”思路后，实验比较了三种 todo module 公开接口：

- 单一 `dispatch(command)` 接口
- 显式 domain methods，例如 `add`、`toggle`、`list`
- 纯 reducer + selector 函数

最终选择显式 domain methods，因为它让测试读起来像用户能力说明，同时把 id generation、title normalization、immutable update 等细节藏在模块内部。

### 3. TDD Behavior Test

实验使用 Node 内置 test runner，测试只通过公开 API 调用 todo list，不检查内部数组或私有 helper。第一轮测试结果：

```text
tests 4
pass 3
fail 1
Missing expected exception ... expected: /Unknown todo filter/
```

失败原因是实现把 unknown filter 检查放在 `Array.filter` callback 里。空列表时 callback 不执行，因此 `list({ filter: "archived" })` 没有抛错。修复后先验证 filter name，再过滤 items。

最终测试结果：

```text
tests 4
pass 4
fail 0
```

## Verified Findings

1. 该项目是文档驱动的 skill collection。每个 skill 主要通过 `SKILL.md` 描述触发条件和执行协议，而不是提供复杂 runtime。
2. `tdd` skill 的核心约束能直接改善小项目质量：行为测试发现了一个实现层容易漏掉的边界条件。
3. `design-an-interface` 对小模块也有价值。它迫使 agent 先比较调用者体验，再选择接口，而不是直接写第一个想到的实现。
4. `qa` skill 的价值不在修 bug，而在把发现的问题转化成长期可读的用户视角 issue。这个形态适合多人或多 agent 后续接力。
5. 这些 skills 对 agent 有较强“过程塑形”效果，但依赖 agent 自觉执行。没有外部 runner 强制检查 skill 是否完整执行。

## Limitations And Risks

- 本研究没有通过 `npx skills@latest add mattpocock/skills/...` 做真实安装测试。
- 没有在 Claude Code 中运行这些 skills，因此不评价其原生 Claude Code integration。
- Todo app 刻意保持为 domain module，没有 UI、CLI、数据库或 local storage。
- 分类脚本是研究用启发式分类，不代表 upstream 作者的正式分类。
- `qa` artifact 没有创建真实 GitHub issue；这是为了让研究目录自包含。

## Reproduction

从 repo 根目录执行：

```bash
git clone --depth 1 https://github.com/mattpocock/skills.git /tmp/mattpocock-skills
node mattpocock-skills-todo-app-eval/scripts/analyze-skills.mjs /tmp/mattpocock-skills
cd mattpocock-skills-todo-app-eval/experiment/todo-app
npm test
```

预期：

- `artifacts/skills-index.json` 和 `artifacts/skills-index.md` 被生成或刷新
- `npm test` 显示 4 个测试全部通过

## Concrete Next Steps

- 若要评估真实安装体验，单独开一个 follow-up 研究项目，测试 `npx skills@latest add mattpocock/skills/tdd` 等命令在 Claude Code 或 Codex skill 环境中的兼容性。
- 若要扩展 todo app 实验，可以增加一个 UI 或 CLI vertical slice，再用 `to-issues` 把功能拆成可并行 issue。
