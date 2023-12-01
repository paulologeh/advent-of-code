import pathlib
import sys

SHAPE_POINTS = {"X": 1, "Y": 2, "Z": 3}

OUTCOME_POINTS = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

OUTCOME_POINTS_EXPECTED = {"X": 0, "Y": 3, "Z": 6}


def get_shape_points_given_outcome(opponent_play, desired_outcome):
    for key, value in OUTCOME_POINTS.items():
        if opponent_play in key and value == desired_outcome:
            return SHAPE_POINTS[key[1]]


def parse(puzzle_input):
    return [guide.strip().replace(" ", "") for guide in puzzle_input.split("\n")]


def part1(games):
    """Solve part 1."""
    return sum([SHAPE_POINTS[game[1]] + OUTCOME_POINTS[game] for game in games])


def part2(games):
    """Solve part 2."""

    return sum(
        [
            OUTCOME_POINTS_EXPECTED[game[1]]
            + get_shape_points_given_outcome(game[0], OUTCOME_POINTS_EXPECTED[game[1]])
            for game in games
        ]
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
