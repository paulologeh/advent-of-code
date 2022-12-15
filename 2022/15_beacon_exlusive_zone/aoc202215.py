import pathlib
import sys
import parse as parser


def parse(puzzle_input):
    """Parse input."""
    pattern = parser.compile(
        "Sensor at x={xs}, y={ys}: closest beacon is at x={xb}, y={yb} "
    )
    sensor_data = [
        {key: int(val) for key, val in pattern.search(f"{line} ").named.items()}
        for line in puzzle_input.strip().split("\n")
    ]
    report = sorted(sensor_data, key=lambda x: x["xb"])
    return report


def part1(report, y=2000000):
    """Solve part 1."""
    is_covered = set()
    for reading in report:
        xs, ys, xb, yb = reading.values()
        d = abs(xs - xb) + abs(ys - yb)
        for x in range(xs - d, xs + d):
            if abs(xs - x) + abs(ys - y) <= d:
                is_covered.add((x, y))

    beacons = set(
        (reading["xb"], reading["yb"]) for reading in report if reading["yb"] == y
    )

    return len(is_covered) - len(beacons)


def part2(report, maximum=4000000):
    """Solve part 2."""
    for y in range(0, maximum):
        available = []
        for reading in report:
            xs, ys, xb, yb = reading.values()
            d = abs(xs - xb) + abs(ys - yb)
            dy = abs(ys - y)
            if dy <= d:
                dx = d - dy
                available.append((max([xs - dx, 0]), min([xs + dx, maximum])))

        available.sort()
        combined = [available.pop(0)]

        for _range in available:
            check = combined[-1]
            if _range[0] > check[1]:
                combined.append(_range)
            else:
                combined[-1] = (check[0], max([check[1], _range[1]]))

        if len(combined) > 1 or (combined[0][0] > 0 and combined[0][1] > maximum):
            if len(combined) == 1:
                x = 0 if combined[0][0] > 0 else maximum
            else:
                x = combined[0][1] + 1

            return x * maximum + y


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
