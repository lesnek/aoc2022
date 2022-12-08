import math

from python.read import parse_lines


def solution1(data: list[str]) -> int:
    trees = 0
    data = list(map(str.strip, data))
    for x, row in enumerate(data):
        for y, col in enumerate(row):
            element = int(data[x][y])

            top = [element > int(row[y]) for row in data[:x]]
            left = [element > int(col) for col in data[x][:y]]
            right = [element > int(col) for col in data[x][y + 1 :]]
            bottom = [element > int(row[y]) for row in data[x + 1 :]]

            if any([all(top), all(left), all(right), all(bottom)]):
                trees += 1

    return trees


def solution2(data: list[str]) -> int:
    scores = []
    data = list(map(str.strip, data))
    for x, row in enumerate(data):
        for y, col in enumerate(row):
            element = int(data[x][y])

            # Reversed hack so I can have edge first.
            top = list(reversed([element > int(row[y]) for row in data[:x]]))
            left = list(reversed([element > int(col) for col in data[x][:y]]))

            right = [element > int(col) for col in data[x][y + 1 :]]
            bottom = [element > int(row[y]) for row in data[x + 1 :]]

            score = math.prod(
                calculate_score(tree_line) for tree_line in [top, left, right, bottom]
            )
            scores.append(score)

    return max(scores)


def calculate_score(tree_line: list[bool]) -> int:
    return tree_line.index(False) + 1 if (False in tree_line) else len(tree_line)


if __name__ == "__main__":
    print("Day8")
    print(
        f"Number of visible trees outside of grid is: {solution1(parse_lines('../../inputs/day8.txt'))}"
    )
    print(
        f"The best scenic score of tree is: {solution2(parse_lines('../../inputs/day8.txt'))}"
    )
