import unittest

from python.day8.solution import solution1, solution2


class Test(unittest.TestCase):
    inputs = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]

    def test_sol1(self):
        self.assertEqual(solution1(self.inputs), 21)

    def test_sol2(self):
        self.assertEqual(solution2(self.inputs), 8)


if __name__ == "__main__":
    unittest.main()
