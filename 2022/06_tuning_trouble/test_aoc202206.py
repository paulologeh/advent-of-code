# test_aoc202206.py

import pathlib

import aoc202206 as aoc  # change me
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 7
    assert aoc.part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert aoc.part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert aoc.part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert aoc.part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_part2_example(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 19
    assert aoc.part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert aoc.part2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert aoc.part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert aoc.part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
