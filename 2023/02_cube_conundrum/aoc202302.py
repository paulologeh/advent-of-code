import pathlib
import sys
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input):
    """
    Parse input.
    returns game data in form
    [
        [{"blue": 5, "red": 5, "green": 6}], [{"blue": 5, "red": 5, "green": 6}]
        ...
    ]
    where the array index + 1 is the game number and the array is the
    cube number in each set
    """
    games = []

    for line in puzzle_input.split("\n"):
        game = []
        _, sets = line.strip().split(":")

        for subsets in sets.split(";"):
            cubes = {"blue": 0, "red": 0, "green": 0}

            for cube in subsets.split(","):
                _, count, color = cube.split(" ")
                cubes[color] += int(count)

            game.append(cubes)

        games.append(game)

    return games


def part1(data):
    """Solve part 1."""
    result = 0
    for i, game in enumerate(data):
        valid_games = [
            subset
            for subset in game
            if subset["red"] <= 12 and subset["green"] <= 13 and subset["blue"] <= 14
        ]
        if len(valid_games) == len(game):
            result += i + 1

    return result


def part2(data):
    """Solve part 2."""
    result = 0
    for game in data:
        red_max = max([subset["red"] for subset in game]) or 1
        blue_max = max([subset["blue"] for subset in game]) or 1
        green_max = max([subset["green"] for subset in game]) or 1
        result += red_max * blue_max * green_max

    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert len(example) == 5
    assert example[0][0]["blue"] == 3
    assert example[0][1]["red"] == 1


def test_part1_example1(example):
    """Test part 1 on example input."""
    assert part1(example) == 8


def test_part2_example1(example):
    """Test part 2 on example input."""
    assert part2(example) == 2286


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
