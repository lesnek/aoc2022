from python.read import parse_lines


def solution(data: str, marker_len: int) -> int:
    marker = []
    index = 0

    while len(marker) < marker_len:
        letters = data[index : marker_len + index]
        if len(set(letters)) == marker_len:
            marker = letters
        index += 1

    return index + marker_len - 1


def solution1(data: list[str]) -> int:
    return solution(data[0], 4)


def solution2(data: list[str]) -> int:
    return solution(data[0], 14)


if __name__ == "__main__":
    print("Day6")
    print(
        f"Marker starts at char no. {solution1(parse_lines('../../inputs/day6.txt'))}"
    )
    print(
        f"Message starts at char no. {solution2(parse_lines('../../inputs/day6.txt'))}"
    )
