import unittest

from python.day9.solution import solution1


class Test(unittest.TestCase):
    inputs = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]

    def test_sol1(self):
        self.assertEqual(solution1(self.inputs), 13)


if __name__ == "__main__":
    unittest.main()
