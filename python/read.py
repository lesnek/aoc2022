def parse_lines(input_path: str) -> list[str]:
    with open(input_path, "r+") as file:
        return list(map(str.strip, file.readlines()))


def parse_lines_raw(input_path: str) -> str:
    with open(input_path, "r+") as file:
        return file.read()
