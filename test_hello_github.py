"""Tests for the hello_github module."""

import io
import unittest
from contextlib import redirect_stdout

from hello_github import print_hello_github


class PrintHelloGithubTests(unittest.TestCase):
    def test_prints_hello_github(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            print_hello_github()

        self.assertEqual(output.getvalue(), "hello github\n")


if __name__ == "__main__":
    unittest.main()
