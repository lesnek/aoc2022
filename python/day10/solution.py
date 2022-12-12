import re
from python.read import parse_lines

CRT = "40 x 6"


def solution1(data: list[str]) -> int:
    cycle = 1
    cmd_index = 0
    cmd_in_cycle = 0
    register = 1
    score = 0
    while cmd_index < len(data):
        cmd = data[cmd_index]
        cmd_in_cycle += 1
        cycle += 1
        if cmd.startswith("noop"):
            cmd_index += 1
            cmd_in_cycle = 0
        elif cmd_in_cycle == 2:
            cmd_index += 1
            cmd_in_cycle = 0
            register += int(re.findall(r"-?\d+", cmd)[0])

        if cycle in [20, 60, 100, 140, 180, 220]:
            score += register * cycle

    return score


def solution2(data: list[str]) -> str:
    cycle = 1
    cmd_index = 0
    cmd_in_cycle = 0
    register = 1
    score = ""
    while cmd_index < len(data):
        cmd = data[cmd_index]
        if cycle % 40 in [register, register + 1, register + 2]:
            score += "#"
        else:
            score += "."

        cmd_in_cycle += 1
        cycle += 1
        if cmd.startswith("noop"):
            cmd_index += 1
            cmd_in_cycle = 0
        elif cmd_in_cycle == 2:
            cmd_index += 1
            cmd_in_cycle = 0
            register += int(re.findall(r"-?\d+", cmd)[0])

    result = []

    for i in range(0, len(score), 40):
        result.append(score[i : i + 40])
    return "\n".join(result)


if __name__ == "__main__":
    print("Day10")
    print(
        f"Sum of signal strengths: {solution1(parse_lines('../../inputs/day10.txt'))}"
    )
    print("\n========== CRT boop beep poob ===========\n")
    print(solution2(parse_lines("../../inputs/day10.txt")))
    print("\n=========================================\n")
