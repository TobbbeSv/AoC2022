from day_1.day_1 import day_1_part_1, day_1_part_2
from day_2.day_2 import day_2_part_1, day_2_part_2
from day_3.day_3 import day_3_part_1


def get_solution_for_day(solution_for_day: float):
    if solution_for_day == 1.1:
        return day_1_part_1()
    elif solution_for_day == 1.2:
        return day_1_part_2()
    elif solution_for_day == 2.1:
        return day_2_part_1()
    elif solution_for_day == 2.2:
        return day_2_part_2()
    elif solution_for_day == 3.1:
        return day_3_part_1()


if __name__ == "__main__":
    day = 3.1
    print(f"Executing day {day}")
    solution = get_solution_for_day(day)
    print(f"The solution is {solution}")
