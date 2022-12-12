# test_aoc202212.py

import pathlib

import aoc202212 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    [grid, start, end, starts] = example
    assert start == (0, 0)
    assert end == (2, 5)
    assert starts == [(0, 0), (0, 1), (1, 0), (2, 0), (3, 0), (4, 0)]
    assert grid == [
        ["a", "a", "b", "q", "p", "o", "n", "m"],
        ["a", "b", "c", "r", "y", "x", "x", "l"],
        ["a", "c", "c", "s", "z", "z", "x", "k"],
        ["a", "c", "c", "t", "u", "v", "w", "j"],
        ["a", "b", "d", "e", "f", "g", "h", "i"],
    ]


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 31


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 29
