
from elf_controller import retrieve_calorie_for_elves


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
