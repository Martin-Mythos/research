#!/usr/bin/env python3
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
