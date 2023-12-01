import pathlib
import sys
import math


def parse(puzzle_input):
    """Parse input."""
    heights = puzzle_input.strip().split("\n")
    return [[int(number) for number in height] for height in heights]


def directions(heights, row, col):
    rows = len(heights)

    up = [heights[y][col] for y in range(row)]
    left = heights[row][:col]
    down = [heights[y][col] for y in range(row + 1, rows)]
    right = heights[row][col + 1 :]
    left.reverse()
    up.reverse()

    return up, left, down, right


def is_visible(tree, neighbours):
    for neighbour in neighbours:
        if tree <= neighbour:
            return False

    return True


def score(tree, neighbours):
    for idx, neighbour in enumerate(neighbours):
        if tree <= neighbour:
            return idx + 1

    return len(neighbours)


def part1(heights):
    """Solve part 1."""
    rows = len(heights)
    cols = len(heights[0])
    visible = []

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            curr_height = heights[row][col]
            up, left, down, right = directions(heights, row, col)
            if any(
                [
                    is_visible(curr_height, up),
                    is_visible(curr_height, left),
                    is_visible(curr_height, down),
                    is_visible(curr_height, right),
                ]
            ):
                visible.append(curr_height)

    return len(visible) + (2 * rows) + (2 * (cols - 2))


def part2(heights):
    """Solve part 2."""
    rows = len(heights)
    cols = len(heights[0])
    scenic_scores = []

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            curr_height = heights[row][col]
            up, left, down, right = directions(heights, row, col)
            scores = [
                score(curr_height, up),
                score(curr_height, left),
                score(curr_height, down),
                score(curr_height, right),
            ]
            scenic_scores.append(math.prod(scores))

    return max(scenic_scores)


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
