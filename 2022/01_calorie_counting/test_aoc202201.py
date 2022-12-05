import pathlib

import aoc202201 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "display.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == [6000, 4000, 11000, 24000, 10000]


def test_part1_example1(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 24000


def test_part2_example1(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 45000
