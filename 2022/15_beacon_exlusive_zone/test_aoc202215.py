# test_aoc_template.py

import pathlib

import aoc202215 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example, 10) == 26


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example, 20) == 56000011
