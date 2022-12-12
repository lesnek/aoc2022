import os
import unittest

from python.day11.solution import solution1, solution2
from python.read import parse_lines_raw


class Test(unittest.TestCase):
    path = os.path.dirname(__file__)
    def test_sol1(self):
        self.assertEqual(
            solution1(parse_lines_raw(self.path + "/test_day11.txt")), 10605
        )

    def test_sol2(self):
        self.assertEqual(
            solution2(parse_lines_raw(self.path + "/test_day11.txt")), 2713310158
        )


if __name__ == "__main__":
    unittest.main()
