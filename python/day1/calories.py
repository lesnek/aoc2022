class Elf:
    calories: int = 0


def day1(data: list[str]) -> int:
    elves = get_elves_with_calories(data)
    return max(elf.calories for elf in elves)


def day1_2(data: list[str]) -> int:
    elves = get_elves_with_calories(data)
    return get_sum_of_top_3(elves)


def parse_input(input_path: str) -> list[str]:
    with open(input_path, "r+") as file:
        return file.readlines()


def get_sum_of_top_3(elves: list[Elf]) -> int:
    sort_elves = sorted(elves, key=lambda x: x.calories, reverse=True)
    return sum(elf.calories for elf in sort_elves[:3])


def get_elves_with_calories(data: list[str]) -> list[Elf]:
    elves = [Elf()]
    for line in data:
        if line == "\n":
            elves.append(Elf())
            continue
        elves[-1].calories += int(line)
    return elves


if __name__ == "__main__":
    input_1 = parse_input('../../inputs/day1.txt')
    print(f"Maximum calories for one elf is: {day1(input_1)}")
    print(f"Sum of top three calories per elf is: {day1_2(input_1)}")
