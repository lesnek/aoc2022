from __future__ import annotations
import re
from math import prod

from python.read import parse_lines_raw


class Monkey:
    def __init__(self, raw_data: list[str], divider: int) -> None:
        raw_data = iter(raw_data)
        self.divider = divider
        self.inspect = 0

        self.items = self.get_numbers(next(raw_data))
        self.operation = next(raw_data).split("= ")[-1]
        self.test, self.true, self.false = [
            self.get_numbers(next(raw_data))[0] for _ in range(3)
        ]

    @staticmethod
    def get_numbers(line: str) -> list[int]:
        return list(map(int, re.findall("\d+", line)))

    def compute_worry_level(self, monkeys: list[Monkey], modulo: int) -> None:
        for item in self.items:
            worry_level = (
                eval(self.operation.replace("old", str(item))) % modulo
            ) // self.divider
            monkeys[
                self.true if worry_level % self.test == 0 else self.false
            ].items.append(worry_level)
            self.inspect += 1
        self.items = []


def solution(raw_data: str, rounds: int, divider: int) -> int:
    monkeys = [
        Monkey(monkey.split("\n")[1:], divider=divider)
        for monkey in raw_data.split("\n\n")
    ]
    # Hack to prevent big numbers:
    # 30 % 4 = 2; 30 % 7 = 2; 7 * 4 = 28
    # 30 % 28 % 4 = 2; 30 % 28 % 7 = 2
    modulo = prod(monkey.test for monkey in monkeys)
    for _ in range(rounds):
        [monkey.compute_worry_level(monkeys, modulo) for monkey in monkeys]
    inspections = sorted([monkey.inspect for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]


def solution1(raw_data: str) -> int:
    return solution(raw_data, 20, 3)


def solution2(raw_data: str) -> int:
    return solution(raw_data, 10000, 1)


if __name__ == "__main__":
    print("Day11")
    print(
        f"Monkey business after 20 rounds is: {solution1(parse_lines_raw('../../inputs/day11.txt'))}"
    )
    print(
        f"Monkey business after 10000 rounds is: {solution2(parse_lines_raw('../../inputs/day11.txt'))}"
    )
