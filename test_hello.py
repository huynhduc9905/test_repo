"""Tests for the hello-world script."""

import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from hello import get_greeting, print_github_bot_greeting, print_hello_github


class HelloScriptTests(unittest.TestCase):
    def test_get_greeting_returns_expected_greeting(self) -> None:
        self.assertEqual(get_greeting(), "Hello from Hermes!")

    def test_print_github_bot_greeting_prints_expected_message(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            print_github_bot_greeting()

        self.assertEqual(stdout.getvalue(), "hello from github bot\n")

    def test_print_hello_github_prints_expected_message(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            print_hello_github()

        self.assertEqual(stdout.getvalue(), "hello github\n")

    def test_hello_script_prints_expected_greeting(self) -> None:
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("hello.py"))],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.stdout, "Hello from Hermes!\n")
        self.assertEqual(result.stderr, "")
