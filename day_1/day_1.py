import os
import sys


def retrieve_calorie_for_elves():
    with open(os.path.join(sys.path[0], 'day_1/input.txt')) as elven_data:
        elves_calories = []
        current_count = 0
        for line in elven_data:
            stripped_line = line.strip()
            if not stripped_line:
                elves_calories.append(current_count)
                current_count = 0
            else:
                current_count = current_count + int(stripped_line)

    return elves_calories


def day_1_part_1():
    elves_with_calories = retrieve_calorie_for_elves()
    return max(elves_with_calories)


def day_1_part_2():
    elves_with_calories = retrieve_calorie_for_elves()

    top_elf = max(elves_with_calories)
    print(f"Top elf {top_elf}")

    elves_with_calories.remove(top_elf)

    second_elf = max(elves_with_calories)
    print(f"Second elf {second_elf}")
    elves_with_calories.remove(second_elf)

    third_elf = max(elves_with_calories)
    print(f"Third elf {third_elf}")
    elves_with_calories.remove(third_elf)

    return top_elf + second_elf + third_elf
