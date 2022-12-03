import unittest

from python.day1.solution import solution1, solution2


class Test(unittest.TestCase):
    def test_day1(self):
        self.assertEqual(solution1(["1", "2", "3"]), 6)
        self.assertEqual(solution1([]), 0)
        self.assertEqual(solution1(["1", "\n", "2"]), 2)

    def test_day1_2(self):
        self.assertEqual(solution2(["1", "2", "3"]), 6)
        self.assertEqual(solution2([]), 0)
        self.assertEqual(solution2(["1", "\n", "2"]), 3)
        self.assertEqual(solution2(["1", "\n", "2", "\n", "3", "\n", "4"]), 9)


if __name__ == "__main__":
    unittest.main()
