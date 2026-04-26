# Notes

## Original Prompt

User asked, in Chinese:

> `$open-research 请帮忙研究一下这个项目 -> https://github.com/mattpocock/skills，用这个skill跑一个真实的小项目，例如做一个“todo app“，看看这些skills如何发挥作用，然后做一个研究报告出来。`

## Research Question

How does `mattpocock/skills` structure agent skills, and what do several of those skills contribute when applied to a small, real todo app project?

## Working Scope

- Source project: <https://github.com/mattpocock/skills>
- Experimental target: a small todo app implementation used as a controlled task.
- Evaluation focus: skill structure, practical workflow effects, reproducibility, and limitations.

## Sources Actually Used

- Root repository instructions: `/Users/martin/Code/research/AGENTS.md`
- Open research skill instructions: `/Users/martin/Code/research/.agents/skills/open-research/SKILL.md`
- GitHub web page: <https://github.com/mattpocock/skills>

## Commands And Tools

- `pwd`
- `ls`
- `sed -n '1,220p' /Users/martin/Code/research/.agents/skills/open-research/SKILL.md`
- `sed -n '1,220p' AGENTS.md`
- `sed -n '1,220p' README.md`
- `git status --short`
- `mkdir -p mattpocock-skills-todo-app-eval`
- `git clone --depth 1 https://github.com/mattpocock/skills.git /tmp/mattpocock-skills`
- `find /tmp/mattpocock-skills -maxdepth 2 -type f -name 'SKILL.md'`
- `find /tmp/mattpocock-skills -maxdepth 2 -type f | sed 's#^/tmp/mattpocock-skills/##' | sort`
- `git -C /tmp/mattpocock-skills rev-parse HEAD`
- `sed -n '1,220p' /tmp/mattpocock-skills/README.md`
- `sed -n '1,260p' /tmp/mattpocock-skills/tdd/SKILL.md`
- `sed -n '1,240p' /tmp/mattpocock-skills/design-an-interface/SKILL.md`
- `sed -n '1,240p' /tmp/mattpocock-skills/qa/SKILL.md`
- `sed -n '1,240p' /tmp/mattpocock-skills/domain-model/SKILL.md`
- `node mattpocock-skills-todo-app-eval/scripts/analyze-skills.mjs /tmp/mattpocock-skills`
- `npm test` in `mattpocock-skills-todo-app-eval/experiment/todo-app`
- `git diff --check`
- `git status --short`

## Experiments

- Cloned `mattpocock/skills` to `/tmp/mattpocock-skills` for inspection. Commit checked: `60aa99c0230fbac087514ba5fca2ae6e519965fe`.
- Extracted skill frontmatter and generated `artifacts/skills-index.json` and `artifacts/skills-index.md`.
- Applied `design-an-interface` manually to produce three todo module interface shapes, then selected explicit domain methods as the experiment interface.
- Built a small todo app domain module with behavior tests using Node's built-in test runner.
- First `npm test` result: 3 passing, 1 failing. Failure exposed that invalid filters were not rejected when the todo list was empty.
- Fixed the invalid-filter bug by validating filter names before applying collection filtering.
- Applied the `qa` issue template locally in `artifacts/qa-session-output.md` instead of creating real GitHub issues.

## Failed Paths

- Initial `git clone` failed in sandbox with `Could not resolve host: github.com`; reran with approved network escalation and cloned successfully.
- First todo implementation validated filters inside the `Array.filter` callback. That path failed because an empty list never executes the callback.

## Verification Evidence

- `node mattpocock-skills-todo-app-eval/scripts/analyze-skills.mjs /tmp/mattpocock-skills` printed: `{"development":4,"other":2,"planning-design":11,"tooling-setup":1,"writing-knowledge":3}`.
- First todo test run:

```text
tests 4
pass 3
fail 1
Missing expected exception ... expected: /Unknown todo filter/
```
- Final todo test run:

```text
tests 4
pass 4
fail 0
duration_ms 64.839792
```
- Final validation run:

```text
node mattpocock-skills-todo-app-eval/scripts/analyze-skills.mjs /tmp/mattpocock-skills
=> {"development":4,"other":2,"planning-design":11,"tooling-setup":1,"writing-knowledge":3}

npm test
=> tests 4, pass 4, fail 0, duration_ms 65.070375

git diff --check
=> passed with no output

git status --short
=> ?? mattpocock-skills-todo-app-eval/
```
