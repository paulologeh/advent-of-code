import pathlib
import sys


class Node():
    def __init__(self):
        self.parent = None
        self.children = []  # None if file, [] if folder
        self.name = None
        self.size = 0

    def print_node(self, action):
        print(f"'action:{action}'   name: {self.name} parent:{None if self.parent is None else self.parent.name} "
              f"children_len:"
              f"{len(self.children) if self.children else None} size:{self.size}")


def parse(puzzle_input):
    """Parse input."""
    terminal = puzzle_input.strip().split("\n")
    head = None
    curr_node = None

    for action in terminal:
        match action.split(" "):
            case '$', 'cd', directory:
                if directory == '..':
                    curr_node = curr_node.parent
                elif directory == '/':
                    head = Node()
                    head.name = directory
                    curr_node = head
                else:
                    next_node = [child for child in curr_node.children if child.name == directory]
                    curr_node = next_node[0]
            case '$', 'ls':
                continue
            case 'dir', directory:
                new_node = Node()
                new_node.name = directory
                new_node.parent = curr_node
                curr_node.children.append(new_node)
            case size, file:
                new_node = Node()
                new_node.children = None
                new_node.name = file
                new_node.size = int(size)
                new_node.parent = curr_node
                curr_node.children.append(new_node)

    calculate_folder_sizes(head, head.size)

    return head


def calculate_folder_sizes(head, size):
    if head.children is None:
        return head, head.size
    else:
        size_sum = sum([calculate_folder_sizes(child, size)[1] for child in head.children])
        head.size += size_sum
        return head, head.size


def sum_directories_less_than_100000(head, total):
    if head.children is None:
        return head, total
    else:
        total += head.size if head.size <= 100000 else 0
        for child in head.children:
            total = sum_directories_less_than_100000(child, total)[1]

        return head, total


def smallest_dir_for_shortfall(head, size, shortfall):
    if head.children is None:
        return head, size, shortfall
    else:
        if size == 0:
            size = max(size, head.size if head.size >= shortfall else size)
        else:
            size = min(size, head.size if head.size >= shortfall else size)
        for child in head.children:
            size = smallest_dir_for_shortfall(child, size, shortfall)[1]

        return head, size, shortfall


def part1(head):
    """Solve part 1."""
    return sum_directories_less_than_100000(head, 0)[1]


def part2(head):
    """Solve part 2."""
    total_used = head.size
    available = 70000000
    target_unused = 30000000
    current_unused = available - total_used
    shortfall = target_unused - current_unused
    return smallest_dir_for_shortfall(head, 0, shortfall)[1]


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
