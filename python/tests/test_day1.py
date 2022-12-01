import unittest

from python.day1.calories import day1, day1_2


class Test(unittest.TestCase):

    def test_day1(self):
        self.assertEqual(day1(["1", "2", "3"]), 6)
        self.assertEqual(day1([]), 0)
        self.assertEqual(day1(["1", "\n", "2"]), 2)

    def test_day1_2(self):
        self.assertEqual(day1_2(["1", "2", "3"]), 6)
        self.assertEqual(day1_2([]), 0)
        self.assertEqual(day1_2(["1", "\n", "2"]), 3)
        self.assertEqual(day1_2(["1", "\n", "2", "\n", "3", "\n", "4"]), 9)


if __name__ == '__main__':
    unittest.main()
