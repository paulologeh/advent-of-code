import pathlib
import sys
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input):
    """Parse input."""
    return [value.strip() for value in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1."""
    parsed = [[int(char) for char in chars if char.isnumeric()] for chars in data]

    return sum([int(f"{values[0]}{values[-1]}") for values in parsed])


def part2(data):
    """Solve part 2."""
    parsed = []

    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for chars in data:
        values = []
        i = 0
        while i < len(chars):
            if chars[i].isnumeric():
                values.append(int(chars[i]))
            elif chars[i] in {"o", "t", "f", "s", "e", "n", "z"}:
                j = i
                while j < len(chars):
                    digit = chars[i : j + 1]
                    if digit in digits.keys():
                        values.append(digits[digit])
                    j += 1

            i += 1

        parsed.append(values)

    return sum([int(f"{values[0]}{values[-1]}") for values in parsed])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert part1(example1) == 142


def test_part2_example1(example2):
    """Test part 2 on example input."""
    assert part2(example2) == 281


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
