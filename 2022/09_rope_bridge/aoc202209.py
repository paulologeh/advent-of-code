import pathlib
import sys

move = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}


def parse(puzzle_input):
    """Parse input."""
    motions = puzzle_input.strip().split("\n")
    return [(motion.split()[0], int(motion.split()[1])) for motion in motions]


def increment(x):
    return -1 if x < 0 else 1


def move_tail(head, tail):
    """
    same row or col
    head (3,1) tail (1,1)
    dx = 2, dy = 0
    tail moves (1,0) R
    head (1,1) tail (1,3)
    dx = 0, dy = -2
    tail moves (0,-1) D
    head (-1,0) tail (0,0)
    dx = -1, dy = 0
    tail doesn't move
    head (-2,0) tail (0,0)
    dx = -2, dy = 0
    tail moves (-1,0)

    different row and col
    head (2,2) tail (1,1)
    dx = 1, dy = 1
    tail does not move
    head (2,3) tail (1,1)
    dx = 1, dy = 2
    tail moves (1,0) R
    tail moves (0,1) U
    head (3,2) tail (1,1)
    dx = 2, dy = 1
    tail moves (1,0) R
    tail moves (0,1) U
    """
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    tx = tail[0]
    ty = tail[1]
    if dx == 0 or dy == 0:
        if abs(dx) > 1:
            tx += increment(dx)
        elif abs(dy) > 1:
            ty += increment(dy)
    elif abs(dx) == 1 and abs(dy) == 1:
        pass
    else:
        tx += increment(dx)
        ty += increment(dy)

    return [tx, ty]


def part1(motions):
    """Solve part 1."""
    visited = set()
    visited.add((0, 0))
    head = [0, 0]
    tail = [0, 0]
    for (direction, n) in motions:
        movement = move[direction]
        for _ in range(n):
            head[0] += movement[0]
            head[1] += movement[1]
            tail = move_tail(head, tail)

            visited.add(tuple(tail))  # add wherever the tail ends up

    return len(visited)


def part2(motions):
    """Solve part 2."""
    visited = set()
    knots = [[0, 0] for _ in range(10)]
    visited.add(tuple(knots[-1]))

    for (direction, n) in motions:
        movement = move[direction]
        for _ in range(n):
            knots[0][0] += movement[0]
            knots[0][1] += movement[1]
            for idx in range(1, 10):
                head = knots[idx - 1]
                tail = knots[idx]
                knots[idx] = move_tail(head, tail)

            visited.add(tuple(knots[-1]))

    return len(visited)


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
