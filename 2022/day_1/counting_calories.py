from collections import deque


def elf_with_most_calories():
    max_calories = 0
    total_current_calories = 0

    with open('./input.txt') as input_file:
        for line in input_file:
            current_calories = None if line.strip() == '' else int(line.strip())
            if current_calories is None:
                max_calories = max(max_calories, total_current_calories)
                total_current_calories = 0
            else:
                total_current_calories += current_calories

    print(max_calories)


def three_elves_with_most_calories():
    calories = []
    total_current_calories = 0

    with open('./input.txt') as input_file:
        for line in input_file:
            current_calories = None if line.strip() == '' else int(line.strip())
            if current_calories is None:
                calories.append(total_current_calories)
                total_current_calories = 0
            else:
                total_current_calories += current_calories

    calories_sorted = sorted(calories, reverse=True)
    print(sum(calories_sorted[:3]))


if __name__ == "__main__":
    elf_with_most_calories()
    three_elves_with_most_calories()
