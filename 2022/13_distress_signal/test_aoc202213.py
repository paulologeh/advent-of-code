# test_aoc_template.py

import pathlib

import aoc202213 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture()
def example2():
    return [[[[], [2, 3, 6, []], []], [[7, 9, 7], [1]]]]


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == [
        [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]],
        [[[1], [2, 3, 4]], [[1], 4]],
        [[9], [[8, 7, 6]]],
        [[[4, 4], 4, 4], [[4, 4], 4, 4, 4]],
        [[7, 7, 7, 7], [7, 7, 7]],
        [[], [3]],
        [[[[]]], [[]]],
        [[1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]],
    ]


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 13


def test_part1_example2(example2):
    assert aoc.part1(example2) == 1


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 140
