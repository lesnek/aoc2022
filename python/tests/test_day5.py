import copy
import unittest

from python.day5.solution import solution1, solution2, load_stack_for_masochist


class Test(unittest.TestCase):
    STACK = [
        "    [H]         [D]     [P]        ",
        "[W] [B]         [C] [Z] [D]        ",
        "[T] [J]     [T] [J] [D] [J]        ",
        "[H] [Z]     [H] [H] [W] [S]     [M]",
        "[P] [F] [R] [P] [Z] [F] [W]     [F]",
        "[J] [V] [T] [N] [F] [G] [Z] [S] [S]",
        "[C] [R] [P] [S] [V] [M] [V] [D] [Z]",
        "[F] [G] [H] [Z] [N] [P] [M] [N] [D]",
    ]

    def test_day5(self):
        data = copy.deepcopy(self.STACK)
        data.append("move 1 from 2 to 3")
        self.assertEqual(
            solution1(data),
            "WBHTDZPSM",
        )

    def test_day5_2(self):
        data = copy.deepcopy(self.STACK)
        data.append("move 2 from 2 to 3")
        self.assertEqual(
            solution2(data),
            "WJHTDZPSM",
        )

    def test_parser_for_masochist(self):
        self.assertEqual(
            load_stack_for_masochist(self.STACK),
            [
                "FCJPHTW",
                "GRVFZJBH",
                "HPTR",
                "ZSNPHT",
                "NVFZHJCD",
                "PMGFWDZ",
                "MVZWSJDP",
                "NDS",
                "DZSFM",
            ],
        )


if __name__ == "__main__":
    unittest.main()
