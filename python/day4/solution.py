from typing import Callable

from python.read import parse_lines


def create_assignment_set(elf_assignments: list[str]) -> set[int]:
    if len(set(elf_assignments)) == 1:
        return {int(elf_assignments[0])}
    return set(range(int(elf_assignments[0]), int(elf_assignments[1]) + 1))


def solution(data: list[str], condition: Callable[[set[int], set[int]], bool]) -> int:
    score = 0
    for pair in data:
        elf1, elf2 = pair.strip().split(",")
        elf1_assigment = create_assignment_set(elf1.split("-"))
        elf2_assigment = create_assignment_set(elf2.split("-"))
        if condition(elf1_assigment, elf2_assigment):
            score += 1

    return score


def solution1(data: list[str]) -> int:
    def condition(elf1_assigment: set[int], elf2_assigment: set[int]):
        min_len = min(len(elf1_assigment), len(elf2_assigment))
        return len(elf1_assigment.intersection(elf2_assigment)) == min_len

    return solution(data, condition)


def solution2(data: list[str]) -> int:
    return solution(data, lambda x, y: x.intersection(y))


if __name__ == "__main__":
    print("Day4")
    print(f"Score exploited is: {solution1(parse_lines('../../inputs/day4.txt'))}")
    print(f"Planned score is: {solution2(parse_lines('../../inputs/day4.txt'))}")
