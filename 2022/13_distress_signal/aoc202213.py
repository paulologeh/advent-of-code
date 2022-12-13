import pathlib
import sys
from functools import cmp_to_key


def parse(puzzle_input):
    """Parse input."""
    packets = puzzle_input.strip().split("\n\n")
    pairs = [[eval(pair) for pair in pairs.split("\n")] for pairs in packets]
    return pairs


def compare(left, right):
    if type(left) is int and type(right) is int:
        return left - right
    elif type(left) is int and type(right) is list:
        return compare([left], right)
    elif type(left) is list and type(right) is int:
        return compare(left, [right])
    else:
        idx = 0

        while idx < min(len(left), len(right)):
            result = compare(left[idx], right[idx])
            if result != 0:
                return result
            else:
                idx += 1

        return len(left) - len(right)


def part1(packets):
    """Solve part 1."""
    return sum(
        [
            idx + 1
            for idx, (left, right) in enumerate(packets)
            if compare(left, right) < 0
        ]
    )


def part2(packets):
    """Solve part 2."""
    divider_packet_1 = [[2]]
    divider_packet_2 = [[6]]
    flat_packets = [divider_packet_1, divider_packet_2]

    for idx, (left, right) in enumerate(packets):
        flat_packets.append(left)
        flat_packets.append(right)

    ordered_packets = sorted(flat_packets, key=cmp_to_key(compare))
    divder_packets_indexs = [
        ordered_packets.index(divider_packet_1) + 1,
        ordered_packets.index(divider_packet_2) + 1,
    ]
    return divder_packets_indexs[0] * divder_packets_indexs[1]


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
