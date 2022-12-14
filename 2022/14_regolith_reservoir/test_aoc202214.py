# test_aoc_template.py

import pathlib

import aoc202214 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    cordinates, lowest = example
    assert lowest[1] == 9
    assert cordinates == [
        (498, 4),
        (498, 5),
        (498, 6),
        (497, 6),
        (496, 6),
        (503, 4),
        (502, 4),
        (502, 5),
        (502, 6),
        (502, 7),
        (502, 8),
        (502, 9),
        (501, 9),
        (500, 9),
        (499, 9),
        (498, 9),
        (497, 9),
        (496, 9),
        (495, 9),
        (494, 9),
    ]


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 24


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 93
