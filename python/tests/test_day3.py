import unittest

from python.day3.solution import solution1, solution2


class Test(unittest.TestCase):
    def test_day3(self):
        self.assertEqual(solution1(["aa", "BB"]), 1 + 28)  # a + B

    def test_day3_2(self):
        self.assertEqual(solution2(["xdeA", "fsaA", "lkjA"]), 27)  # A = 27


if __name__ == "__main__":
    unittest.main()
