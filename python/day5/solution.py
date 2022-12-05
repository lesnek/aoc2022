import enum
import re

from python.read import parse_lines


class CraneType(enum.Enum):
    CrateMover9000 = "CrateMover9000"
    CrateMover9001 = "CrateMover9001"


def load_stack(_data: list[str]) -> list[str]:
    return [
        "FCJPHTW",
        "GRVFZJBH",
        "HPTR",
        "ZSNPHT",
        "NVFZHJCD",
        "PMGFWDZ",
        "MVZWSJDP",
        "NDS",
        "DZSFM",
    ]


def load_stack_for_masochist(_data: list[str]) -> list[str]:
    letter_len = 4
    stack = ["", "", "", "", "", "", "", "", ""]

    for line in _data:
        for index in range(0, 9):
            start = 3 * index
            letter = line[index + start : index + start + letter_len].strip()
            if any(l.isalpha() for l in letter):
                stack[index] = letter.replace("[", "").replace("]", "") + stack[index]

    return stack


def parse_move(move: str) -> tuple[int, int, int]:
    """move 2 from 8 to 2"""
    find = re.findall(r"\d+", move)
    cnt, from_s, to_s = list(map(int, find))
    return cnt, from_s - 1, to_s - 1


def stack_handler(
    stack: list[str], cnt: int, from_s: int, to_s: int, crane_type: CraneType
) -> list[str]:
    removed = stack[from_s][-cnt:]
    if crane_type == CraneType.CrateMover9000:
        removed = removed[::-1]  # Old CrateMover cannot stack all at once.
    stack[from_s] = stack[from_s][:-cnt]
    stack[to_s] = stack[to_s] + removed
    return stack


def solution(data: list[str], crane_type: CraneType) -> str:
    new = []
    move_start = 0
    for idx, lin in enumerate(data):
        if "move" in lin:
            move_start = idx
            break

    data_moves = data[move_start:]
    data_stack = data[: move_start - 1]
    stack = load_stack_for_masochist(data_stack)
    for line in data_moves:
        cnt, from_s, to_s = parse_move(line)
        new = stack_handler(stack, cnt, from_s, to_s, crane_type)

    return "".join([_stack[-1] for _stack in new])


def solution1(data: list[str]) -> str:
    return solution(data, CraneType.CrateMover9000)


def solution2(data: list[str]) -> str:
    return solution(data, CraneType.CrateMover9001)


if __name__ == "__main__":
    print("Day5")
    print(f"Crate mover 9000: {solution1(parse_lines('../../inputs/day5.txt'))}")
    print(f"Crate mover 9001: {solution2(parse_lines('../../inputs/day5.txt'))}")
