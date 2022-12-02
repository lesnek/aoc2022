import unittest

from python.day2.solution import solution1, solution2


class Test(unittest.TestCase):

    def test_day1(self):
        self.assertEqual(solution1(["A X", "C Z", "A Y"]), 18)

    def test_day1_2(self):
        self.assertEqual(solution2(["A X", "C Z", "A Y"]), 14)


if __name__ == '__main__':
    unittest.main()
