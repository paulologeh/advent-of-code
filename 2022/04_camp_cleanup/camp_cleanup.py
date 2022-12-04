def is_overlapped(pair_1, pair_2):
    if pair_2[0] <= pair_1[0] <= pair_2[1]:
        return True
    elif pair_1[0] <= pair_2[0] <= pair_1[1]:
        return True
    else:
        return False


def is_contained(pair_1, pair_2):
    if pair_1[0] >= pair_2[0] and pair_1[1] <= pair_2[1]:
        return True
    elif pair_2[0] >= pair_1[0] and pair_2[1] <= pair_1[1]:
        return True
    else:
        return False


def get_input():
    pairs = []
    with open("input.txt") as input_file:
        for line in input_file:
            assignment = line.strip().split(",")
            pair = []
            for section in assignment:
                pair += [int(number) for number in section.split("-")]

            pairs.append(pair)

    return pairs


def fully_contained_range_count():
    pairs = get_input()
    contained_count = 0

    for pair in pairs:
        if is_contained(pair[:2], pair[2:]):
            contained_count += 1

    print(contained_count)


def overlapping_range_count():
    pairs = get_input()
    overlapping_count = 0

    for pair in pairs:
        if is_overlapped(pair[:2], pair[2:]):
            overlapping_count += 1

    print(overlapping_count)


if __name__ == "__main__":
    fully_contained_range_count()
    overlapping_range_count()
