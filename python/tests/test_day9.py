import unittest

from python.day9.solution import solution1, solution2


class Test(unittest.TestCase):
    inputs1 = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]
    inputs2 = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20",
    ]

    def test_sol1(self):
        self.assertEqual(solution1(self.inputs1), 13)

    def test_sol2(self):
        self.assertEqual(solution2(self.inputs2), 36)


if __name__ == "__main__":
    unittest.main()
