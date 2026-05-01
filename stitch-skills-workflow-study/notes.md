# Notes - Stitch Skills Workflow Study

## Original prompt
研究 Google 的 Stitch skill（https://github.com/google-labs-code/stitch-skills），评估安装后可带来的新 workflow 与价值；做多个实验（含 SRP 漏洞上报平台样式设计、demo、UX/UI demo、emotion 动画），并给出研究报告与 HTML 演示。

## Skill usage
- Using skill: open-research (matched user request for reproducible research project workflow).

## Log
- Command: `web.search_query` for repo overview and skill list.
- Source URL: https://github.com/google-labs-code/stitch-skills
- Outcome: captured available skills and install commands.

## Experiment plan
1) Analyze core skills and derive workflows (design -> multi-page -> design system -> react -> remotion).
2) Build SRP (Single Reporting Platform) mock experience with multiple UI styles.
3) Build UX/UI demo and emotion animation demo.
4) Build HTML presentation summarizing value and outcomes.
## Experiments run
- Built artifacts:
  - `artifacts/srp-demo.html`
  - `artifacts/uxui-demo.html`
  - `artifacts/emotion-animation-demo.html`
  - `artifacts/presentation.html`
- Validation command: `python3 -m http.server 8000` (manual run instructions in README).
- Static verification command used: `python3 -m py_compile` not applicable to pure HTML assets.

## Failed/abandoned paths
- Attempted `git clone --depth 1 https://github.com/google-labs-code/stitch-skills.git` in `/tmp`, blocked by environment policy; switched to web source retrieval.

## Verification evidence
- Confirmed repository skill list and installation commands via web search result and GitHub repository page.
