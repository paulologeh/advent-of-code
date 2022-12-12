import pathlib
import sys
from collections import deque


def parse(puzzle_input):
    """Parse input."""
    grid = [list(line) for line in puzzle_input.split("\n")]
    a_positions = []
    start = end = None
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == "S":
                start = (x, y)
                grid[x][y] = "a"

            if value == "E":
                end = (x, y)
                grid[x][y] = "z"

            if grid[x][y] == "a":
                a_positions.append((x, y))

    return grid, start, end, a_positions


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(grid, starts, end):
    visited = set()
    q = deque([(start, 0) for start in starts])

    while q:
        position, dist = q.popleft()
        if position == end:
            return dist
        elif position in visited:
            continue
        else:
            visited.add(position)
            x, y = position

            for dx, dy in DIRECTIONS:
                if (
                    0 <= x + dx < len(grid)
                    and 0 <= y + dy < len(grid[0])
                    and ord(grid[x + dx][y + dy]) - ord(grid[x][y]) <= 1
                ):
                    discovered = ((x + dx, y + dy), dist + 1)
                    q.append(discovered)


def part1(grid, start, end):
    """Solve part 1."""
    return bfs(grid, start, end)


def part2(grid, start, end):
    """Solve part 2."""
    return bfs(grid, start, end)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    grid, start, end, a_positions = parse(puzzle_input)
    solution1 = part1(grid, [start], end)
    solution2 = part2(grid, a_positions, end)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
