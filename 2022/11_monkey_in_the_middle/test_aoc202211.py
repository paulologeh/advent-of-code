# test_aoc202211.py
import sys

import pathlib

import aoc202211 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == [
        "Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n   "
        " If true: throw to monkey 2\n    If false: throw to monkey 3",
        "Monkey 1:\n  Starting items: "
        "54, 65, 75, 74\n  Operation: "
        "new = old + 6\n  Test: "
        "divisible by 19\n    If true: "
        "throw to monkey 2\n    If "
        "false: throw to monkey 0",
        "Monkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by "
        "13\n    If true: throw to monkey 1\n    If false: throw to monkey 3",
        "Monkey 3:\n  Starting "
        "items: 74\n  "
        "Operation: new = old + "
        "3\n  Test: divisible "
        "by 17\n    If true: "
        "throw to monkey 0\n    "
        "If false: throw to "
        "monkey 1",
    ]


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 10605


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 2713310158
