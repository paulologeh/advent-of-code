import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.strip().split("\n\n")


def run_simulation(notes, worry_level_divisor, number_of_rounds):
    count = [0] * len(notes)
    items = [[] for _ in range(len(notes))]
    lcm = 1

    # first extract starting items
    for idx, note in enumerate(notes):
        entry = note.split("\n")
        items_start = entry[1].replace("Starting items: ", "").replace(" ", "")
        items_start = [int(n) for n in items_start.split(",")]
        items[idx] += items_start
        multiple = int(entry[3].split(" ")[-1])
        lcm *= multiple  # we need to keep track of the lcm of all future divisors to prevent our worry levels
        # from becoming very large.

    for _ in range(number_of_rounds):
        for idx, note in enumerate(notes):
            entry = note.split("\n")
            [sign, value] = entry[2].split(" ")[-2:]
            divisor = int(entry[3].split(" ")[-1])
            true_idx = int(entry[4].split(" ")[-1])
            false_idx = int(entry[5].split(" ")[-1])

            for item in items[idx]:
                count[idx] += 1
                worry_level = eval(f"{item} {sign} {item if value == 'old' else value}")
                worry_level = worry_level // worry_level_divisor
                recieving_monkey = true_idx if worry_level % divisor == 0 else false_idx
                items[recieving_monkey].append(worry_level % lcm)

            items[idx] = []

    most_active = sorted(count)[-2:]
    return most_active[0] * most_active[1]


def part1(notes):
    """Solve part 1."""
    return run_simulation(notes, 3, 20)


def part2(notes):
    """Solve part 2."""
    return run_simulation(notes, 1, 10000)


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
