# test_aoc_template.py

import pathlib

import aoc202210 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example[:3] == ["addx 15", "addx -11", "addx 6"]


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 13140
