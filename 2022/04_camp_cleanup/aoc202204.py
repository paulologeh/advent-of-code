import pathlib
import sys


def is_overlapped(pair):
    if pair[2] <= pair[0] <= pair[3]:
        return True
    elif pair[0] <= pair[2] <= pair[1]:
        return True
    else:
        return False


def is_contained(pair):
    if pair[0] >= pair[2] and pair[1] <= pair[3]:
        return True
    elif pair[2] >= pair[0] and pair[3] <= pair[1]:
        return True
    else:
        return False


def parse(puzzle_input):
    """Parse input."""
    pairs = []
    for assignment in puzzle_input.split("\n"):
        pair = []
        for section in assignment.strip().split(","):
            pair += [int(number) for number in section.split("-")]

        pairs.append(pair)

    return pairs


def part1(pairs):
    """Solve part 1."""
    return len(list(filter(is_contained, pairs)))


def part2(pairs):
    """Solve part 2."""
    return len(list(filter(is_overlapped, pairs)))


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
