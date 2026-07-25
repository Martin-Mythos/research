#!/usr/bin/env python3
"""Shifu 风格多模型委派的确定性模拟器；不调用任何外部 LLM API。"""
import ast
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts"
MODELS = {
    "GPT5.6 Lula": {"in": 0.030, "out": 0.060, "latency": 2.0},
    "GPT5.4 Mini": {"in": 0.006, "out": 0.012, "latency": 0.8},
    "GPT5.3 Codex Spark": {"in": 0.004, "out": 0.008, "latency": 0.7},
    "Single Flagship Baseline": {"in": 0.030, "out": 0.060, "latency": 2.0},
}

def tokens(s): return max(1, math.ceil(len(s) / 4))
def h(obj): return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]
def record(task_id, model, input_obj, output_obj, parent_output_hash=None):
    tin, tout = tokens(json.dumps(input_obj, ensure_ascii=False)), tokens(json.dumps(output_obj, ensure_ascii=False))
    p = MODELS[model]
    return {"task_id": task_id, "model": model, "input_tokens_est": tin, "output_tokens_est": tout,
            "cost_est": round((tin*p["in"] + tout*p["out"]) / 1000, 6), "latency_est_s": p["latency"],
            "input_context_hash": h(input_obj), "output_context_hash": h(output_obj),
            "parent_output_hash": parent_output_hash, "schema_version": "mock-v2"}

def require_context(context):
    required = {"app", "features", "language", "acceptance"}
    missing = required - context.keys()
    if missing:
        raise AssertionError(f"上下文缺少字段：{sorted(missing)}")

def handoff(logs, task_id, model, input_obj, output_obj):
    require_context(input_obj)
    require_context(output_obj)
    parent_hash = logs[-1]["output_context_hash"] if logs else None
    event = record(task_id, model, input_obj, output_obj, parent_hash)
    if parent_hash is not None and event["input_context_hash"] != parent_hash:
        raise AssertionError(f"上下文断裂：{task_id}")
    logs.append(event)

def main():
    scenario = {"app": "Vocabulary Memorization CLI", "features": ["quiz", "add", "stats"], "language": "Python", "acceptance": ["py_compile passes", "smoke commands work"]}
    plan = {**scenario, "architecture": "single-file CLI plus JSON data", "files": ["vocab_app.py", "vocab_data.json"]}
    data = {**plan, "words": [{"en":"abandon","zh":"放弃"},{"en":"benevolent","zh":"仁慈的"}], "scoring": "exact zh match"}
    bad_code = "def broken(:\n    pass\n"
    logs = []
    handoff(logs, "plan", "GPT5.6 Lula", scenario, plan)
    handoff(logs, "logic-data", "GPT5.4 Mini", plan, data)
    bad_output = {**data, "code": bad_code, "status": "syntax-error"}
    handoff(logs, "code-bad", "GPT5.3 Codex Spark", data, bad_output)
    bad_path = OUT / "vocab_app_bad.py"; bad_path.write_text(bad_code, encoding="utf-8")
    syntax_error = None
    try: ast.parse(bad_code)
    except SyntaxError as e: syntax_error = {"msg": e.msg, "lineno": e.lineno, "offset": e.offset}
    diagnosis = {**bad_output, "error": syntax_error, "instruction": "保持原验收标准并制定修复路径"}
    handoff(logs, "failure-review", "GPT5.6 Lula", bad_output, diagnosis)
    fix_spec = {**diagnosis, "repair": "替换非法函数签名并重新生成完整 CLI", "verification": ["ast.parse", "py_compile", "CLI smoke tests"]}
    handoff(logs, "repair-plan", "GPT5.4 Mini", diagnosis, fix_spec)
    fixed_code = '''#!/usr/bin/env python3
import argparse, json
from pathlib import Path
DATA = Path(__file__).with_name("vocab_data.json")
DEFAULT_WORDS = [{"en":"abandon","zh":"放弃"},{"en":"benevolent","zh":"仁慈的"}]
def load_words():
    if DATA.exists():
        return json.loads(DATA.read_text(encoding="utf-8"))
    DATA.write_text(json.dumps(DEFAULT_WORDS, ensure_ascii=False, indent=2), encoding="utf-8")
    return list(DEFAULT_WORDS)
def save_words(words):
    DATA.write_text(json.dumps(words, ensure_ascii=False, indent=2), encoding="utf-8")
def add_word(en, zh):
    words = load_words(); words.append({"en": en, "zh": zh}); save_words(words); return len(words)
def stats():
    return {"total_words": len(load_words())}
def quiz(answer=None):
    word = load_words()[0]
    if answer is None:
        return f"请写出 {word['en']} 的中文释义"
    return "correct" if answer.strip() == word["zh"] else "incorrect"
def main(argv=None):
    p = argparse.ArgumentParser(description="Vocabulary Memorization CLI")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("en"); a.add_argument("zh")
    q = sub.add_parser("quiz"); q.add_argument("--answer")
    sub.add_parser("stats")
    ns = p.parse_args(argv)
    if ns.cmd == "add": print(json.dumps({"total_words": add_word(ns.en, ns.zh)}, ensure_ascii=False))
    elif ns.cmd == "quiz": print(quiz(ns.answer))
    elif ns.cmd == "stats": print(json.dumps(stats(), ensure_ascii=False))
if __name__ == "__main__": main()
'''
    app_path = OUT / "vocab_app.py"; app_path.write_text(fixed_code, encoding="utf-8")
    (OUT / "vocab_data.json").write_text(json.dumps(data["words"], ensure_ascii=False, indent=2), encoding="utf-8")
    ast.parse(fixed_code)
    fixed_output = {**fix_spec, "code": fixed_code, "status": "fixed"}
    handoff(logs, "code-fixed", "GPT5.3 Codex Spark", fix_spec, fixed_output)
    multi = {"cost_est": round(sum(x["cost_est"] for x in logs), 6), "latency_est_s": round(sum(x["latency_est_s"] for x in logs), 2)}
    baseline_cost = sum((x["input_tokens_est"]*MODELS["Single Flagship Baseline"]["in"] + x["output_tokens_est"]*MODELS["Single Flagship Baseline"]["out"]) / 1000 for x in logs)
    baseline = {"cost_est": round(baseline_cost, 6), "latency_est_s": round(len(logs) * MODELS["Single Flagship Baseline"]["latency"], 2)}
    lineage_ok = all(x["parent_output_hash"] is None or x["parent_output_hash"] == x["input_context_hash"] for x in logs)
    routing_ok = [x["model"] for x in logs] == ["GPT5.6 Lula", "GPT5.4 Mini", "GPT5.3 Codex Spark", "GPT5.6 Lula", "GPT5.4 Mini", "GPT5.3 Codex Spark"]
    result = {"method": "确定性模拟；价格与延迟均为实验假设，不是供应商实测值", "routing_logs": logs,
              "protocol_verification": {"lineage_ok": lineage_ok, "routing_ok": routing_ok, "required_context_ok": True},
              "multi_model": multi, "single_flagship_baseline": baseline,
              "savings_vs_baseline_pct": round((1 - multi["cost_est"]/baseline["cost_est"])*100, 2),
              "syntax_error_detected": syntax_error is not None, "fixed_py_compile_expected": True}
    (OUT / "mock_routing_logs.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
if __name__ == "__main__": main()
