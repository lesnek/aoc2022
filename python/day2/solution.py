import dataclasses
import enum


def parse_input(input_path: str) -> list[str]:
    with open(input_path, "r+") as file:
        return file.readlines()


@dataclasses.dataclass
class GamePower:
    score: int
    oponent_label: str
    player_label: str
    win: list[str]
    lose: list[str]


SCISSORS = GamePower(3, "C", "Z", ["B", "Y"], ["A", "X"])
PAPER = GamePower(2, "B", "Y", ["A", "X"], ["C", "Z"])
ROCK = GamePower(1, "A", "X", ["C", "Z"], ["B", "X"])


class Weapons(enum.Enum):
    A = ROCK
    B = PAPER
    C = SCISSORS
    X = ROCK
    Y = PAPER
    Z = SCISSORS


def solution1(data: list[str]) -> int:
    total_score = 0
    for line in data:
        oponent, me = line.strip().split(" ")
        me = Weapons[me].value
        if oponent in me.win:
            total_score += 6 + me.score
        elif oponent == me.oponent_label:
            total_score += 3 + me.score
        else:
            total_score += me.score

    return total_score


def solution2(data: list[str]) -> int:
    total_score = 0
    for line in data:
        oponent, outcome = line.strip().split(" ")
        oponent = Weapons[oponent].value
        if outcome == "Z":
            total_score += Weapons[oponent.lose[0]].value.score + 6
        elif outcome == "X":
            total_score += Weapons[oponent.win[0]].value.score
        else:
            total_score += oponent.score + 3

    return total_score


if __name__ == "__main__":
    print("Day2")
    solution1(parse_input("../../inputs/day2.txt"))
    solution2(parse_input("../../inputs/day2.txt"))
