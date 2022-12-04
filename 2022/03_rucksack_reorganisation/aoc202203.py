import pathlib
import sys


def ascii_to_priority(character: str) -> int:
    if character.islower():
        return ord(character) - ord("a") + 1
    else:
        return ord(character) - ord("A") + 27


def parse(puzzle_input):
    """Parse input."""
    return [items.strip() for items in puzzle_input.split("\n")]


def part1(rucksacks):
    """Solve part 1."""
    priority = 0
    for rucksack in rucksacks:
        mid_point = len(rucksack) // 2
        common_item = set(rucksack[:mid_point]).intersection(set(rucksack[mid_point:]))
        priority += ascii_to_priority(list(common_item)[0])

    return priority


def part2(rucksacks):
    """Solve part 2."""
    priority = 0

    for index in range(0, len(rucksacks), 3):
        badge = set(rucksacks[index]).intersection(
            set(rucksacks[index + 1]), set(rucksacks[index + 2])
        )
        priority += ascii_to_priority(list(badge)[0])

    return priority


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
