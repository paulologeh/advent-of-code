import pathlib
import sys


def parse(puzzle_input):
    return [
        sum([int(calories) for calories in calories.split("\n") if calories])
        for calories in puzzle_input.split("\n\n")
    ]


def part1(calories):
    """Solve part 1."""
    return max(calories)


def part2(calories):
    """Solve part 2."""
    return sum(sorted(calories)[-3:])


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
