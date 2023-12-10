import pathlib
import sys
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input):
    """Parse input."""
    return [[char for char in lines.strip()] for lines in puzzle_input.split("\n")]


def valid_symbol(char):
    return not char.isalpha() and not char.isnumeric() and char != "."


ADJACENT = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]


def adjacent_symbol(grid, position, rowsize, colsize):
    x, y = position
    for dx, dy in ADJACENT:
        if (
            0 <= dx + x < rowsize
            and 0 <= dy + y < colsize
            and valid_symbol(grid[dx + x][dy + y])
        ):
            return True

    return False


def part1(grid):
    """Solve part 1."""
    rowsize = len(grid)
    colsize = len(grid[0])
    part_numbers = []

    for x in range(rowsize):
        y = 0

        while y < colsize:
            if grid[x][y].isnumeric():
                y_start = y

                while y < colsize and grid[x][y].isnumeric():
                    y += 1

                y_end = y
                number = grid[x][y_start:y_end]

                # for each position, check if there is a valid adjacent symbol
                for yi in range(y_start, y_end):
                    if adjacent_symbol(grid, (x, yi), rowsize, colsize):
                        part_numbers.append(int("".join(number)))
                        break
            else:
                y += 1

    return sum(part_numbers)


def adjacent_gears(grid, position, rowsize, colsize):
    x, y = position
    adjacent_positions = set()

    for dx, dy in ADJACENT:
        if 0 <= dx + x < rowsize and 0 <= dy + y < colsize:
            adjacent_positions.add((dx + x, dy + y))

    # check rows
    x_range = [val for val in [x - 1, x, x + 1] if 0 <= val < rowsize]

    gears = []
    for x in x_range:
        yi = 0

        while yi < colsize:
            if grid[x][yi].isnumeric():
                seen = set()
                y_start = yi

                while yi < colsize and grid[x][yi].isnumeric():
                    if (x, yi) in adjacent_positions:
                        seen.add((x, yi))

                    yi += 1

                y_end = yi
                number = grid[x][y_start:y_end]

                if seen:
                    gears.append(int("".join(number)))
            else:
                yi += 1

    return gears


def part2(grid):
    """Solve part 2."""
    rowsize = len(grid)
    colsize = len(grid[0])
    gear_ratios = []

    for x in range(rowsize):
        for y in range(colsize):
            if grid[x][y] == "*":
                gears = adjacent_gears(grid, (x, y), rowsize, colsize)
                if len(gears) == 2:
                    gear_ratios.append(gears[0] * gears[1])

    return sum(gear_ratios)


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
    assert example[0] == ["4", "6", "7", ".", ".", "1", "1", "4", ".", "."]


def test_part1_example1(example):
    """Test part 1 on example input."""
    assert part1(example) == 4361


def test_part2_example1(example):
    """Test part 2 on example input."""
    assert part2(example) == 467835


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
