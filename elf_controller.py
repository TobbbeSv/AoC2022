import os
import sys


def retrieve_calorie_for_elves():
    with open(os.path.join(sys.path[0], 'inputs/elves_with_calories.txt')) as elven_data:
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
