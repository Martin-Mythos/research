#!/usr/bin/env python3
"""Mock empirical harness for Shifu-style multi-model dispatch.
Uses only sandbox model names and no external LLM APIs."""
import ast, hashlib, json, math, time
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
def record(task_id, model, input_obj, output_obj):
    tin, tout = tokens(json.dumps(input_obj, ensure_ascii=False)), tokens(json.dumps(output_obj, ensure_ascii=False))
    p = MODELS[model]
    return {"task_id": task_id, "model": model, "input_tokens_est": tin, "output_tokens_est": tout,
            "cost_est": round((tin*p["in"] + tout*p["out"]) / 1000, 6), "latency_est_s": p["latency"],
            "input_context_hash": h(input_obj), "output_context_hash": h(output_obj), "schema_version": "mock-v1"}

def main():
    scenario = {"app": "Vocabulary Memorization CLI", "features": ["quiz", "add", "stats"], "language": "Python", "acceptance": ["py_compile passes", "smoke commands work"]}
    plan = {**scenario, "architecture": "single-file CLI plus JSON data", "files": ["vocab_app.py", "vocab_data.json"]}
    data = {**plan, "words": [{"en":"abandon","zh":"放弃"},{"en":"benevolent","zh":"仁慈的"}], "scoring": "exact zh match"}
    bad_code = "def broken(:\n    pass\n"
    logs = [record("plan", "GPT5.6 Lula", scenario, plan), record("logic-data", "GPT5.4 Mini", plan, data), record("code-bad", "GPT5.3 Codex Spark", data, {"code": bad_code})]
    bad_path = OUT / "vocab_app_bad.py"; bad_path.write_text(bad_code, encoding="utf-8")
    syntax_error = None
    try: ast.parse(bad_code)
    except SyntaxError as e: syntax_error = {"msg": e.msg, "lineno": e.lineno, "offset": e.offset}
    fix_spec = {"error": syntax_error, "instruction": "修复语法并保持 CLI 功能", "source_model": "GPT5.3 Codex Spark"}
    logs.append(record("failure-review", "GPT5.6 Lula", {"bad_code": bad_code}, fix_spec))
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
    logs.append(record("code-fixed", "GPT5.3 Codex Spark", fix_spec, {"code": fixed_code}))
    multi = {"cost_est": round(sum(x["cost_est"] for x in logs), 6), "latency_est_s": round(sum(x["latency_est_s"] for x in logs), 2)}
    baseline_cost = sum((x["input_tokens_est"]*MODELS["Single Flagship Baseline"]["in"] + x["output_tokens_est"]*MODELS["Single Flagship Baseline"]["out"]) / 1000 for x in logs)
    baseline = {"cost_est": round(baseline_cost, 6), "latency_est_s": round(len(logs) * MODELS["Single Flagship Baseline"]["latency"], 2)}
    result = {"routing_logs": logs, "multi_model": multi, "single_flagship_baseline": baseline,
              "savings_vs_baseline_pct": round((1 - multi["cost_est"]/baseline["cost_est"])*100, 2),
              "syntax_error_detected": syntax_error is not None, "fixed_py_compile_expected": True}
    (OUT / "mock_routing_logs.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
if __name__ == "__main__": main()
