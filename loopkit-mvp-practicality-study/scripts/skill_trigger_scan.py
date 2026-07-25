#!/usr/bin/env python3
"""Create a reproducible, explicitly simulated LoopKit activation matrix.

This does not claim to observe an agent runtime. The selected skills and reasons are
part of the experiment protocol and are checked against a pinned LoopKit checkout.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SIMULATED_ACTIVATIONS = {
    "adversarial-verify": "代码完成后、提交前执行敌对审查",
    "authz-check": "新增读取和修改用户任务的端点，需要验证资源所有权",
    "clean-commits": "实验流程要求在测试通过后提交",
    "context-budget": "跨路由、业务、数据与测试层，需要把状态保存在磁盘",
    "contract-test": "新增 API 的 401、404 与响应结构属于边界契约",
    "input-validation": "注册、登录和任务端点接收不可信请求体",
    "owasp-review": "变更涉及认证、授权、token 与外部输入",
    "secret-scan": "提交前必须检查 token 密钥及密码字样",
    "spec-first": "跨多个文件的多步骤功能必须先写目标规格",
    "write-failing-test-first": "认证功能应先以失败测试固定预期行为",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("缺少 YAML frontmatter")
    result: dict[str, str] = {}
    current = ""
    for line in match.group(1).splitlines():
        if re.match(r"^[A-Za-z_][\w-]*:", line):
            current, value = line.split(":", 1)
            result[current] = value.strip()
        elif current and line.startswith((" ", "\t")):
            result[current] = f"{result[current]} {line.strip()}".strip()
    return result


def scan(skills_dir: Path) -> list[dict[str, object]]:
    files = sorted(skills_dir.glob("*/SKILL.md"))
    if not files:
        raise ValueError(f"未在 {skills_dir} 找到 SKILL.md")
    rows = []
    for path in files:
        metadata = parse_frontmatter(path.read_text(encoding="utf-8"))
        name = metadata.get("name", path.parent.name)
        selected = name in SIMULATED_ACTIVATIONS
        rows.append(
            {
                "skill": name,
                "when_to_use": metadata.get("when_to_use", ""),
                "simulated_activation": selected,
                "selection_reason": SIMULATED_ACTIVATIONS.get(name, "与本次纯后端认证功能无直接关系"),
            }
        )
    missing = sorted(set(SIMULATED_ACTIVATIONS) - {str(row["skill"]) for row in rows})
    if missing:
        raise ValueError(f"固定技能快照缺少预期技能: {', '.join(missing)}")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    rows = scan(args.skills_dir)
    result = {
        "method": "explicit high-fidelity simulation; not runtime observation",
        "total_skills": len(rows),
        "simulated_activated_skills": sum(bool(row["simulated_activation"]) for row in rows),
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
