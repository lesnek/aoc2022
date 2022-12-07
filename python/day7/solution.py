from python.read import parse_lines


def increase_with_parents(
    current_path: str, filesystem: dict[str, int], size: int
) -> dict[str, int]:
    filesystem[""] += int(size)
    while current_path:
        filesystem[current_path] += size
        current_path = current_path[: current_path.rindex("/")]
    return filesystem


def solution(data: list[str]) -> dict[str, int]:
    filesystem = {"": 0}
    current_path = ""
    for line in data[1:]:
        line = line.strip()
        if ".." in line:
            current_path = current_path[: current_path.rindex("/")]
        elif "$ cd" in line:
            current_path = f"{current_path}/{line[5:]}"
            filesystem[current_path] = 0
        elif all(not line.startswith(cmd) for cmd in ["dir", "$ ls"]):
            size, _ = line.split(" ")
            increase_with_parents(current_path, filesystem, int(size))
    return filesystem


def solution1(data):
    sol = solution(data)
    return sum([v for v in sol.values() if v <= 100_000])


def solution2(data):
    sol = solution(data)
    max_disc_space = 70000000
    space_needed = 30000000
    need_to_delete = sol[""] + space_needed - max_disc_space
    return [x for x in sorted(sol.values()) if x - need_to_delete > 0][0]


if __name__ == "__main__":
    print("Day7")
    print(
        f"Total size of dirs under 10k is: {solution1(parse_lines('../../inputs/day7.txt'))}"
    )
    print(
        f"Total size of deleted directory is: {solution2(parse_lines('../../inputs/day7.txt'))}"
    )
