import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("skill_trigger_scan.py")
SPEC = importlib.util.spec_from_file_location("skill_trigger_scan", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_parse_frontmatter_handles_wrapped_description():
    metadata = MODULE.parse_frontmatter(
        "---\nname: demo\ndescription: first\n  second\nwhen_to_use: endpoint, auth\n---\n# Demo\n"
    )
    assert metadata == {
        "name": "demo",
        "description": "first second",
        "when_to_use": "endpoint, auth",
    }


def test_scan_marks_only_explicit_protocol_skills(tmp_path):
    for name in MODULE.SIMULATED_ACTIVATIONS:
        folder = tmp_path / name
        folder.mkdir()
        (folder / "SKILL.md").write_text(
            f"---\nname: {name}\nwhen_to_use: test trigger\n---\n# {name}\n",
            encoding="utf-8",
        )
    unrelated = tmp_path / "a11y-pass"
    unrelated.mkdir()
    (unrelated / "SKILL.md").write_text(
        "---\nname: a11y-pass\nwhen_to_use: UI\n---\n# UI\n", encoding="utf-8"
    )

    rows = MODULE.scan(tmp_path)

    assert sum(row["simulated_activation"] for row in rows) == len(MODULE.SIMULATED_ACTIVATIONS)
    assert next(row for row in rows if row["skill"] == "a11y-pass")["simulated_activation"] is False
