import unittest

from python.day4.solution import solution1, solution2


class Test(unittest.TestCase):
    def test_day4(self):
        self.assertEqual(
            solution1(["1-2, 1-7", "6-9, 1-100", "1-2, 1-2", "1-100, 12-14"]), 4
        )
        self.assertEqual(
            solution1(["1-2,3-7", "6-9,7-100", "1-2,3-4", "1-100,101-102"]), 0
        )

    def test_day4_2(self):
        self.assertEqual(
            solution2(["1-2, 1-7", "6-9, 1-100", "1-2, 1-2", "1-100, 12-14"]), 4
        )
        self.assertEqual(
            solution2(["1-2,3-7", "6-9,7-100", "1-2,3-4", "1-100,101-102"]), 1
        )


if __name__ == "__main__":
    unittest.main()
