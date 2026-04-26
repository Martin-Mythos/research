# Simon Willison 的 AI Research Repo 方法研究

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## 最终结论

Simon Willison 的方法不是“让 AI 上网搜索后写一篇文章”，而是把研究问题转化为一个可执行、可审查、可沉淀的 GitHub 工作流：给异步编码代理 (asynchronous coding agent) 一个明确问题，让它在一个专门的、低敏感度的 GitHub repository 中联网安装依赖、抓取资料、写代码、跑实验、生成报告，最后用 pull request 或 commit 交付一个独立研究目录。

这个模式的关键价值在于：把大语言模型 (Large Language Model, LLM) 的不可靠叙述，尽量压到可以被代码、测试、基准测试 (benchmark)、截图、JSON、图表、diff 和命令输出验证的证据链里。它仍然可能产生错误，因此公开前需要人工审阅；但相比一次性聊天回答，它更容易复现、更容易 review，也更容易长期积累。

## 方法来源

主要依据来自 Simon Willison 2025-11-06 发布的文章 [Code research projects with async coding agents like Claude Code and Codex](https://simonwillison.net/2025/Nov/6/async-code-research/) 以及他的公开仓库 [`simonw/research`](https://github.com/simonw/research)。

他在文章中把这个模式描述为：选择一个研究问题，启动一个异步编码代理，让它在服务器上完成实验，结束后向指定 GitHub repository 提交 pull request。他明确建议使用专门 repository，并把非敏感研究放在公开仓库、未准备公开的内容放在私有仓库。

## 核心工作流

1. 提出可执行的研究问题。

   好问题不是“解释 X”，而是“证明 X 能不能跑、怎么跑、性能如何、限制在哪里”。例如比较 Markdown library 性能、尝试把 C extension 编译到 Pyodide、用 scikit-learn 对博客文章自动打标签。

2. 把问题写成几段明确 prompt。

   Prompt 通常包含：新建目录名、要抓取或阅读的源、要写的代码、要运行的实验、要生成的报告和 artifact，以及不要修改目录外文件等边界。

3. 让 agent 在专门 GitHub repository 中执行。

   Simon 偏好 Claude Code for web、Codex Cloud、Jules、GitHub Copilot coding agent 这类异步编码代理 (asynchronous coding agent)。这些工具可以在远端环境工作，完成后提交 PR。

4. 允许联网，但隔离敏感资产。

   他强调 dedicated repository 的最大好处是可以放宽网络访问，让 agent 安装依赖、获取 web data、clone 或读取公开资料。但前提是 repository 本身不含生产代码、secrets 或私人资料。

5. 每个研究项目一个目录。

   `simonw/research` 的根 README 写明：每个目录都是一个独立研究项目。目录内通常包含 `README.md`、`notes.md`、脚本、测试、JSON 结果、图表或小型 artifact。

6. 最终交付以 GitHub 历史为准。

   Prompt、transcript 和上下文尽量链接在 PR 或 commit 中。这样后续可以从 commit history、PR discussion 和目录内 artifact 追溯研究过程。

7. 用自动化维护根目录索引。

   `simonw/research` 使用 GitHub Actions + `cogapp` + `llm` + `llm-github-models` 自动更新根 `README.md`，扫描子目录，根据每个项目的 README 生成 `_summary.md`，并按目录最近 commit 时间排序。

## Repository 结构模式

一个最小可复用结构如下：

```text
research/
  AGENTS.md
  CLAUDE.md
  README.md
  requirements.txt
  .github/workflows/update-readme.yml
  one-research-question/
    README.md
    notes.md
    scripts-or-tests...
    small-artifacts...
```

`AGENTS.md` 是行为契约。它要求 agent：

- 为每个研究创建新目录；
- 工作过程中维护 `notes.md`；
- 最后产出 `README.md` 报告；
- 只提交自己产生的代码、笔记、patch、小型 artifact；
- 不提交完整外部 repository、vendor dependency tree、secrets、私有数据；
- 不手工创建 `_summary.md`，因为它由自动化生成。

`README.md` 是公开目录。它包含项目说明、时间说明、自动生成的项目列表，以及每个研究项目的摘要。

`.github/workflows/update-readme.yml` 是索引自动化。每次 push 到 `main` 后，它安装 `requirements.txt`，运行 `cog -r -P README.md`，如果根 README、子项目 README 或 `_summary.md` 有变化，就由 GitHub Actions 自动 commit。

## 为什么这个方法有效

### 1. 把研究从 prose 变成 evidence

聊天式研究容易停留在叙述层。Simon 的方法要求 agent 写代码并执行。只要问题适合被实验验证，代码、测试和输出就能给出更硬的 evidence。

### 2. 让 agent 适合做“探索性脏活”

安装依赖、写一次性 benchmark、阅读多个项目源码、跑多轮实验、生成图表，这些任务很适合异步 agent。人类负责选题、验收和判断 tradeoff。

### 3. GitHub 天然提供审查边界

一个 PR 就是一个 reviewable unit。目录结构、diff、commit history、Actions log、artifact 和 discussion 都能沉淀下来。

### 4. Dedicated repo 降低 blast radius

如果 agent 有 full network access，但 repository 内没有敏感代码和 secrets，prompt injection 或恶意依赖造成的风险会低很多。这个隔离不是绝对安全，但比在生产仓库里放开权限更合理。

### 5. 研究之间可以复用

同一个 repository 的历史项目会成为后续 agent 的 context。Simon 的例子中，后续 Pyodide/C extension 研究可以借鉴前一个 Pyodide 项目的结构和测试方式。

## 风险与限制

### AI-generated slop 风险

Simon 明确承认这类报告如果未经认真人工 review，就是 AI slop。公开 repository 不等于内容已经被严格验证。适合把它看作 research lab notebook，而不是已发表论文。

### 不能证明“不可能”

Agent 没做出来只能证明它没找到方法，不能证明问题本身无解。因此结论应写成“本实验未能实现”或“在当前约束下未验证成功”，不要升级为绝对否定。

### 网络访问与供应链风险

Full network access 能提高能力，但也引入 prompt injection、dependency confusion、恶意 package、数据外泄等风险。公开低敏仓库只是降低影响面，不是完整 sandbox。

### 自动摘要可能引入误差

根 README 的 `_summary.md` 由 LLM 生成，适合做索引和浏览，不应替代项目内完整报告。重要结论必须回到子目录 `README.md`、脚本和原始输出核验。

## 适合 Martin 的改造版本

本仓库采用 Simon 的核心模式，但做了几个适配：

- 仓库公开，用于非敏感研究；
- root instructions 保持英文，便于不同 coding agent 稳定执行；
- 研究报告可以用中文写，关键技术词保留英文；
- 自动提示语使用 “AI-assisted research report”，不声称每一行都由 LLM 生成；
- workflow 增加 `workflow_dispatch`，方便手动触发 README rebuild；
- `notes.md` 明确记录 “sources actually used”，避免后续报告无法追溯来源。

## 推荐 prompt 模板

```text
Work in a new folder called <short-kebab-case-topic>.

Research <question>. Use web sources and executable experiments where possible.
Create and update notes.md as you work, listing sources actually used,
commands run, failed attempts, and verification evidence.

Produce a final README.md report with:
- final conclusion
- methods and sources
- experiments or code written
- verified findings
- limitations and risks
- reproduction instructions

Do not edit files outside this folder.
Do not create _summary.md.
Do not commit full copies of external repositories or downloaded dependencies.
Include only scripts, small artifacts, notes, reports, and patches you created.
```

## 本次创建的仓库方法

本次在 GitHub 用户 `xwbcl123` 下创建公开 repository：

- Repository: `xwbcl123/research`
- Local clone: `/Users/martin/Code/research`
- Purpose: AI-assisted code and web research workspace

初始 commit 包含：

- `AGENTS.md`: agent 工作规则；
- `CLAUDE.md`: Claude Code 兼容入口，指向 `AGENTS.md`；
- `README.md`: 根索引与 `cogapp` 自动生成逻辑；
- `requirements.txt`: `cogapp`、`llm`、`llm-github-models`；
- `.github/workflows/update-readme.yml`: GitHub Actions 自动更新索引；
- `simon-willison-code-research-method/README.md`: 本完整研究报告；
- `simon-willison-code-research-method/notes.md`: 研究笔记和来源清单。

## 后续使用建议

对于每个新研究题目，直接让 agent 在这个 repo 新建目录。研究完成后，通过 PR 或 commit review 关注四件事：

- 结论是否被代码或来源支持；
- `notes.md` 是否列出真实使用过的 sources；
- 是否误提交外部仓库、下载依赖、secrets 或大文件；
- README 的结论是否把未验证内容降级为 limitation。

这个仓库应该被视为“研究实验台”，不是最终发布渠道。真正要发表到博客、知识库或决策材料前，应把对应项目再做一次人工事实核查和编辑。

