import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    terminal = puzzle_input.strip().split("\n")
    dirs_size = {}
    dir_stack = []

    for action in terminal:
        match action.split(" "):
            case '$', 'cd', directory:
                if directory == '..':
                    dir_stack.pop()
                else:
                    dir_stack.append(directory)
            case '$', 'ls':
                continue
            case 'dir', _:
                continue
            case size, _:
                # we must add the file size to every path in the stack and not just the current dir
                for idx in range(len(dir_stack)):
                    curr_path = '/' if idx == 0 else '/'.join(dir_stack[:idx+1])[1:]
                    if curr_path not in dirs_size:
                        dirs_size[curr_path] = 0

                    dirs_size[curr_path] += int(size)
            case other:
                continue

    return dirs_size


def part1(directories):
    """Solve part 1."""
    return sum([size for size in directories.values() if size <= 100000])


def part2(directories):
    """Solve part 2."""
    total_used = directories["/"]
    available = 70000000
    target_unused = 30000000
    current_unused = available - total_used
    shortfall = target_unused - current_unused

    return min([size for size in directories.values() if size >= shortfall])


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
