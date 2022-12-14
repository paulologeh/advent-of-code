import pathlib
import sys


def sign(x):
    return -1 if x < 0 else 1


def parse(puzzle_input):
    """Parse input."""
    paths = puzzle_input.strip().split("\n")
    lines = [[cord.split(",") for cord in _path.split(" -> ")] for _path in paths]

    lowest = [500, 0]
    coordinates = []
    for line in lines:
        for idx, point in enumerate(line):
            x1, y1 = int(point[0]), int(point[1])
            coordinates.append((x1, y1))
            lowest = [x1, y1] if y1 > lowest[1] else lowest

            if idx < len(line) - 1:
                end = line[idx + 1]
                x2, y2 = int(end[0]), int(end[1])
                dx, dy = (x2 - x1), (y2 - y1)
                if abs(dx) > 0:
                    for x in range(1, abs(dx)):
                        x3 = x1 + (sign(dx) * x)
                        coordinates.append((x3, y1))
                        lowest = [x3, y1] if y1 > lowest[1] else lowest
                elif abs(dy) > 0:
                    for y in range(1, abs(dy)):
                        y3 = y1 + (sign(dy) * y)
                        coordinates.append((x1, y3))
                        lowest = [x1, y3] if y3 > lowest[1] else lowest

    return coordinates, lowest


def part1(data):
    """Solve part 1."""
    cordinates, lowest = data
    simulation = set(cordinates)
    simulating = True

    while simulating:
        sand = (500, 0)
        while True:
            x, y = sand
            if y >= lowest[1]:
                simulating = False
                break
            elif (x, y + 1) not in simulation:
                sand = (x, y + 1)
            elif (x - 1, y + 1) not in simulation:
                sand = (x - 1, y + 1)
            elif (x + 1, y + 1) not in simulation:
                sand = (x + 1, y + 1)
            else:
                simulation.add(sand)
                break

    return len(simulation) - len(set(cordinates))


def part2(data):
    """Solve part 2."""
    cordinates, lowest = data
    simulation = set(cordinates)
    simulating = True
    lowest[1] += 2

    while simulating:
        sand = (500, 0)
        while True:
            x, y = sand

            if (x, y + 1) not in simulation and y + 1 < lowest[1]:
                sand = (x, y + 1)
            elif (x - 1, y + 1) not in simulation and y + 1 < lowest[1]:
                sand = (x - 1, y + 1)
            elif (x + 1, y + 1) not in simulation and y + 1 < lowest[1]:
                sand = (x + 1, y + 1)
            else:
                simulation.add(sand)
                if sand == (500, 0):
                    simulating = False
                break

    return len(simulation) - len(set(cordinates))


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
