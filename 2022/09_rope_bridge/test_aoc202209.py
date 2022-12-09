# test_aoc_template.py

import pathlib

import aoc202209 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example_2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2),
    ]


def test_parse_example_2(example_2):
    assert example_2 == [
        ("R", 5),
        ("U", 8),
        ("L", 8),
        ("D", 3),
        ("R", 17),
        ("D", 10),
        ("L", 25),
        ("U", 20),
    ]


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 13


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 1


def test_part2_example_2(example_2):
    """Test part 2 on example input."""
    assert aoc.part2(example_2) == 36
