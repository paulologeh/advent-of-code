import pathlib

import aoc202207 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == {"/": 48381165, "/a": 94853, "/a/e": 584, "/d": 24933642}


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 95437


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 24933642
