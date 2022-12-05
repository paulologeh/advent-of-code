# test_aoc_template.py

import pathlib

import aoc202205 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example[0] == [None, ["Z", "N"], ["M", "C", "D"], ["P"]]
    assert example[1] == [
        {"amount": "1", "giving_stack": "2", "receiving_stack": "1"},
        {"amount": "3", "giving_stack": "1", "receiving_stack": "3"},
        {"amount": "2", "giving_stack": "2", "receiving_stack": "1"},
        {"amount": "1", "giving_stack": "1", "receiving_stack": "2"},
    ]


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == "CMZ"


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == "MCD"
