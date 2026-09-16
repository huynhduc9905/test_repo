"""Tests for the hello-world script."""

import subprocess
import sys
import unittest
from pathlib import Path


class HelloScriptTests(unittest.TestCase):
    def test_get_greeting_returns_expected_greeting(self) -> None:
        from hello import get_greeting

        self.assertEqual(get_greeting(), "Hello from Hermes!")

    def test_hello_script_prints_expected_greeting(self) -> None:
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("hello.py"))],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.stdout, "Hello from Hermes!\n")
        self.assertEqual(result.stderr, "")
