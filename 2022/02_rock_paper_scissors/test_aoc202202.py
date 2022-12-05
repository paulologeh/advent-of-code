# test_aoc_template.py

import pathlib

import aoc202202 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "display.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == ["AY", "BX", "CZ"]


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 15


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 12
