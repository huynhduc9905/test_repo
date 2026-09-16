"""Tests for the square module."""

import unittest

from square import square


class SquareTests(unittest.TestCase):
    def test_returns_zero_for_zero(self) -> None:
        self.assertEqual(square(0), 0)

    def test_returns_square_for_positive_integer(self) -> None:
        self.assertEqual(square(3), 9)

    def test_returns_square_for_negative_integer(self) -> None:
        self.assertEqual(square(-4), 16)


if __name__ == "__main__":
    unittest.main()
