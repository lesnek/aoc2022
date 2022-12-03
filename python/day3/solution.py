from python.read import parse_lines

BASE_ASCII_LOWER = 96
BASE_ASCII_UPPER = 38


def calculate_priority(common_item: str) -> int:
    base = BASE_ASCII_UPPER if common_item.isupper() else BASE_ASCII_LOWER
    return ord(common_item) - base


def solution1(data: list[str]) -> int:
    score = 0
    for rucksack in data:
        rucksack = rucksack.strip()
        half = int(len(rucksack) / 2)
        item1, item2 = set(rucksack[half:]), (rucksack[:half])
        common_item = item1.intersection(item2).pop()
        score += calculate_priority(common_item)

    return score


def solution2(data: list[str]) -> int:
    score = 0
    data = iter(data)
    for elf1, elf2, elf3 in zip(data, data, data):
        elf1, elf2, elf3 = [set(elf.strip()) for elf in [elf1, elf2, elf3]]
        common_item = elf1.intersection(elf2).intersection(elf3).pop()
        score += calculate_priority(common_item)

    return score


if __name__ == "__main__":
    print("Day3")
    print(f"Score exploited is: {solution1(parse_lines('../../inputs/day3.txt'))}")
    print(f"Planned score is: {solution2(parse_lines('../../inputs/day3.txt'))}")
