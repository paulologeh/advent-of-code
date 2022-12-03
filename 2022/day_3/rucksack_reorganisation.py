def ascii_to_priority(character: str) -> int:
    if character.islower():
        return ord(character) - 97 + 1
    else:
        return ord(character) - 65 + 1 + 26


def item_types_priorities_sum():
    total_priority = 0
    with open('input.txt') as input_file:
        for line in input_file:
            rucksack = line.strip()
            mid_point = round(len(rucksack) / 2)
            compartment_1 = rucksack[:mid_point]
            compartment_2 = rucksack[mid_point:]

            items = {}
            for item in compartment_1:
                if item not in items:
                    items[item] = 0

                items[item] += 1

            for item in compartment_2:
                if item in items:
                    common_item = item
                    break

            total_priority += ascii_to_priority(common_item)

    print(total_priority)


def item_types_priorities_three_elf_group_sum():
    total_priority = 0
    with open('input.txt') as input_file:
        lines = [line.strip() for line in input_file]

    for idx in range(0, len(lines), 3):
        group = {}
        rucksack_1_unique = set(lines[idx])
        rucksack_2_unique = set(lines[idx + 1])
        rucksack_3_unique = set(lines[idx + 2])

        for item in rucksack_1_unique:
            if item not in group:
                group[item] = 0

            group[item] += 1

        for item in rucksack_2_unique:
            if item not in group:
                group[item] = 0

            group[item] += 1

        for item in rucksack_3_unique:
            if item not in group:
                group[item] = 0

            group[item] += 1

        for (key, value) in group.items():
            if value == 3:
                total_priority += ascii_to_priority(key)
                break

    print(total_priority)


if __name__ == '__main__':
    item_types_priorities_sum()
    item_types_priorities_three_elf_group_sum()
