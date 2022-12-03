
from elf_controller import retrieve_calorie_for_elves


def day_1():
    elves_with_calories = retrieve_calorie_for_elves()
    return max(elves_with_calories)
