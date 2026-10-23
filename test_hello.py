"""Tests for hello.py using only the standard library."""

import subprocess
import sys
import unittest
from pathlib import Path

import hello

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "hello.py"
EXPECTED_OUTPUT = "Hello, World!\n"


class HelloWorldTest(unittest.TestCase):
    def test_greeting_constant(self):
        self.assertEqual(hello.GREETING, "Hello, World!")

    def test_script_prints_greeting(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, EXPECTED_OUTPUT)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
