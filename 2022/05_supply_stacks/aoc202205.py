import pathlib
import sys
from copy import deepcopy

import parse as parser


def clean_char(char: str):
    return char.replace("[", "").replace("]", "")


def parse(puzzle_input):
    """Parse input."""
    [_stacks, _instructions] = puzzle_input.split("\n\n")
    _stacks = _stacks.split("\n")
    indexes = _stacks.pop().split("   ")
    stacks = [None] * (len(indexes) + 1)

    while len(_stacks) > 0:
        crates = _stacks.pop()
        crates += " "  # add extra space for loop to complete
        ptr = 1
        count = 0
        current_char = ""
        for char in crates:
            if count == 3:
                if stacks[ptr] is None:
                    stacks[ptr] = []

                if current_char != "   ":
                    stacks[ptr].append(clean_char(current_char))

                count = 0
                current_char = ""
                ptr += 1
            else:
                current_char += char
                count += 1

    pattern = parser.compile("move {amount} from {giving_stack} to {receiving_stack}")
    instructions = [
        pattern.search(line).named for line in _instructions.strip().split("\n")
    ]

    return stacks, instructions


def part1(data):
    """Solve part 1."""
    stacks = deepcopy(data[0])
    instructions = data[1]
    for instruction in instructions:
        amount = int(instruction["amount"])
        giving_idx = int(instruction["giving_stack"])
        receiving_idx = int(instruction["receiving_stack"])
        for n in range(0, amount):
            stacks[receiving_idx].append(stacks[giving_idx].pop())

    return "".join(list(map(lambda x: x[-1], stacks[1:])))


def part2(data):
    """Solve part 2."""
    stacks = deepcopy(data[0])
    instructions = data[1]
    for instruction in instructions:
        amount = int(instruction["amount"])
        giving_idx = int(instruction["giving_stack"])
        receiving_idx = int(instruction["receiving_stack"])

        substack = stacks[giving_idx][-amount:]
        stacks[receiving_idx] += substack
        stacks[giving_idx] = stacks[giving_idx][:-amount]

    return "".join(list(map(lambda x: x[-1], stacks[1:])))


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
