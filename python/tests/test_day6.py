import unittest

from python.day6.solution import solution1, solution2


class Test(unittest.TestCase):
    def test_sol1(self):
        self.assertEqual(solution1(["bvwbjplbgvbhsrlpgdmjqwftvncz"]), 5)
        self.assertEqual(solution1(["nppdvjthqldpwncqszvftbrmjlhg"]), 6)
        self.assertEqual(solution1(["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]), 10)
        self.assertEqual(solution1(["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]), 11)

    def test_sol2(self):
        self.assertEqual(solution2(["bvwbjplbgvbhsrlpgdmjqwftvncz"]), 23)
        self.assertEqual(solution2(["nppdvjthqldpwncqszvftbrmjlhg"]), 23)
        self.assertEqual(solution2(["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]), 29)
        self.assertEqual(solution2(["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]), 26)


if __name__ == "__main__":
    unittest.main()
