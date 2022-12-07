import unittest

from python.day7.solution import solution1, solution2


class Test(unittest.TestCase):
    inputs = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]

    def test_sol1(self):
        self.assertEqual(solution1(self.inputs), 95437)

    def test_sol2(self):
        self.assertEqual(solution2(self.inputs), 24933642)


if __name__ == "__main__":
    unittest.main()
