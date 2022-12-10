from python.read import parse_lines


def move(pos: tuple[int, int], direction: str) -> tuple[int, int]:
    match direction:
        case "U":
            return pos[0], pos[1] + 1
        case "D":
            return pos[0], pos[1] - 1
        case "R":
            return pos[0] + 1, pos[1]
        case "L":
            return pos[0] - 1, pos[1]


def follow(tail: tuple[int, int], head: tuple[int, int]):
    tail_x, tail_y = tail
    head_x, head_y = head
    new_tail = tail

    should_move = abs(tail_x - head_x) > 1 or abs(tail_y - head_y) > 1

    if not should_move:
        return tail

    if head_x > tail_x:
        new_tail = move(new_tail, "R")
    elif head_x < tail_x:
        new_tail = move(new_tail, "L")

    if head_y > tail_y:
        new_tail = move(new_tail, "U")
    elif head_y < tail_y:
        new_tail = move(new_tail, "D")

    return new_tail


def solution(data: list[str], tail_len: int):
    start = (0, 0)
    visited = {start}

    head = start
    tail = [start] * tail_len

    for line in data:
        direction, count = line.split(" ")
        for _ in range(int(count)):
            head = move(head, direction)

            previous = head
            for i, t in enumerate(tail):
                tail[i] = follow(t, previous)
                previous = tail[i]

            visited.add(tail[-1])

    return len(visited)


def solution1(data: list[str]) -> int:
    return solution(data, 1)


def solution2(data: list[str]) -> int:
    return solution(data, 9)


if __name__ == "__main__":
    print("Day9")
    print(
        f"Tail visited at least once: {solution1(parse_lines('../../inputs/day9.txt'))}"
    )
    print(
        f"Tail in snapped rope visited at least once: {solution2(parse_lines('../../inputs/day9.txt'))}"
    )
