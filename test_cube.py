"""Tests for the cube module."""

import unittest

from cube import cube


class CubeTests(unittest.TestCase):
    def test_returns_cube_for_positive_integer(self) -> None:
        self.assertEqual(cube(2), 8)

    def test_returns_zero_for_zero(self) -> None:
        self.assertEqual(cube(0), 0)

    def test_returns_cube_for_negative_integer(self) -> None:
        self.assertEqual(cube(-3), -27)


if __name__ == "__main__":
    unittest.main()
