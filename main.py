from day_1.day_1 import day_1_part_1, day_1_part_2


def get_solution_for_day(solution_for_day: float):
    switcher = {
        1.1: day_1_part_1(),
        1.2: day_1_part_2(),
    }
    return switcher.get(solution_for_day, None)


if __name__ == "__main__":
    day = 1.2
    print(f"Executing day {day}")
    solution = get_solution_for_day(day)
    print(f"The solution is {solution}")
