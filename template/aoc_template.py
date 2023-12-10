import pathlib
import sys
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    pass


def part2(data):
    """Solve part 2."""
    pass


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


@pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example):
    """Test part 1 on example input."""
    assert part1(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example):
    """Test part 2 on example input."""
    assert part2(example) == ...


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
