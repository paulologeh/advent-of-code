import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.strip().split("\n")


def part1(program):
    """Solve part 1."""
    x = 1
    cycle = 0
    signal_strengths = []

    for instruction in program:
        no_cycles = 2 if "addx" in instruction else 1
        v = 0 if instruction == "noop" else int(instruction.split(" ")[-1])
        for _ in range(no_cycles):
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                signal_strengths.append(cycle * x)

        x += v

    return sum(signal_strengths)


def part2(program):
    """Solve part 2."""
    crt = ["." for _ in range(240)]
    cycle = 0
    x = 1
    ptr_crt = 0

    for instruction in program:
        no_cycles = 2 if "addx" in instruction else 1
        v = 0 if instruction == "noop" else int(instruction.split(" ")[-1])
        for _ in range(no_cycles):
            cycle += 1
            sprite = {x - 1, x, x + 1}

            if ptr_crt % 40 in sprite:
                crt[ptr_crt] = "#"

            ptr_crt += 1

        x += v

    for x in range(0, len(crt), 40):
        print("".join(crt[x : x + 40]))


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    part2(data)

    return [solution1]


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
