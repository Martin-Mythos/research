#!/usr/bin/env python3
"""对模拟路由协议和背单词 CLI 的可重复回归测试。"""
import ast
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_app():
    spec = importlib.util.spec_from_file_location("vocab_app", HERE / "vocab_app.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VocabularyAppTests(unittest.TestCase):
    def setUp(self):
        self.app = load_app()
        self.tempdir = tempfile.TemporaryDirectory()
        self.app.DATA = Path(self.tempdir.name) / "vocab_data.json"

    def tearDown(self):
        self.tempdir.cleanup()

    def test_default_quiz_and_stats(self):
        self.assertEqual(self.app.stats(), {"total_words": 2})
        self.assertEqual(self.app.quiz("放弃"), "correct")
        self.assertEqual(self.app.quiz("错误"), "incorrect")

    def test_add_persists_word(self):
        self.assertEqual(self.app.add_word("candid", "坦率的"), 3)
        self.assertEqual(self.app.load_words()[-1], {"en": "candid", "zh": "坦率的"})


class RoutingHarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, str(HERE / "mock_shifu_experiment.py")], check=True, capture_output=True, text=True)
        cls.result = json.loads((HERE / "mock_routing_logs.json").read_text(encoding="utf-8"))

    def test_expected_route_and_lineage(self):
        self.assertEqual(self.result["protocol_verification"], {
            "lineage_ok": True,
            "routing_ok": True,
            "required_context_ok": True,
        })
        self.assertEqual([event["model"] for event in self.result["routing_logs"]], [
            "GPT5.6 Lula", "GPT5.4 Mini", "GPT5.3 Codex Spark",
            "GPT5.6 Lula", "GPT5.4 Mini", "GPT5.3 Codex Spark",
        ])

    def test_failure_is_real_and_fixed_output_parses(self):
        with self.assertRaises(SyntaxError):
            ast.parse((HERE / "vocab_app_bad.py").read_text(encoding="utf-8"))
        ast.parse((HERE / "vocab_app.py").read_text(encoding="utf-8"))
        self.assertTrue(self.result["syntax_error_detected"])

    def test_baseline_uses_identical_token_workload(self):
        events = self.result["routing_logs"]
        expected = sum((e["input_tokens_est"] * 0.030 + e["output_tokens_est"] * 0.060) / 1000 for e in events)
        self.assertAlmostEqual(self.result["single_flagship_baseline"]["cost_est"], expected, places=6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
