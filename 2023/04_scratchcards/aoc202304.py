import pathlib
import sys

import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input):
    """Parse input."""
    parsed = []

    for line in puzzle_input.split("\n"):
        _, cards_split = line.strip().split(":")
        cards, winning = cards_split.strip().split("|")
        cards = cards.strip().replace("  ", " ").split(" ")
        winning = winning.strip().replace("  ", " ").split(" ")
        parsed.append([cards, winning])

    return parsed


def part1(data):
    """Solve part 1."""
    return sum(
        [
            pow(2, len(set(cards) & set(winning)) - 1)
            for cards, winning in data
            if len(set(cards) & set(winning))
        ]
    )


def part2(data):
    """Solve part 2."""
    scratch_cards = [1] * len(data)

    for i, (cards, winning) in enumerate(data):
        matches = len(set(cards) & set(winning))
        for j in range(1, matches + 1):
            scratch_cards[i + j] += scratch_cards[i]

    return sum(scratch_cards)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example[0] == [
        ["41", "48", "83", "86", "17"],
        ["83", "86", "6", "31", "17", "9", "48", "53"],
    ]


def test_part1_example1(example):
    """Test part 1 on example input."""
    assert part1(example) == 13


def test_part2_example1(example):
    """Test part 2 on example input."""
    assert part2(example) == 30


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
