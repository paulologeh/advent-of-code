import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.strip()


def part1(buffer):
    """Solve part 1."""
    for i in range(0, len(buffer)):
        maybe_marker = set(buffer[i: i + 4])
        if len(maybe_marker) == 4:
            return i + 4


def part2(buffer):
    """Solve part 2."""
    for i in range(0, len(buffer)):
        maybe_marker = set(buffer[i: i + 14])
        if len(maybe_marker) == 14:
            return i + 14


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
