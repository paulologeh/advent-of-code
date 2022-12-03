def ascii_to_priority(character: str) -> int:
    if character.islower():
        return ord(character) - 97 + 1
    else:
        return ord(character) - 65 + 27


def item_types_priorities_sum():
    total_priority = 0
    with open("input.txt") as input_file:
        for line in input_file:
            rucksack = line.strip()
            mid_point = round(len(rucksack) / 2)
            compartment_1 = set(rucksack[:mid_point])
            compartment_2 = set(rucksack[mid_point:])
            common_item = compartment_1.intersection(compartment_2)
            total_priority += ascii_to_priority(list(common_item)[0])

    print(total_priority)


def item_types_priorities_three_elf_group_sum():
    total_priority = 0
    with open("input.txt") as input_file:
        lines = [line.strip() for line in input_file]

    for idx in range(0, len(lines), 3):
        rucksack_1_set = set(lines[idx])
        rucksack_2_set = set(lines[idx + 1])
        rucksack_3_set = set(lines[idx + 2])

        badge = rucksack_1_set.intersection(rucksack_2_set, rucksack_3_set)
        total_priority += ascii_to_priority(list(badge)[0])

    print(total_priority)


if __name__ == "__main__":
    item_types_priorities_sum()
    item_types_priorities_three_elf_group_sum()
