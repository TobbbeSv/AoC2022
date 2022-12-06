from day_1.day_1 import day_1_part_1, day_1_part_2
from day_2.day_2 import day_2_part_1, day_2_part_2
from day_3.day_3 import day_3_part_1, day_3_part_2
from day_4.day_4 import day_4_part_1, day_4_part_2


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
    elif solution_for_day == 3.2:
        return day_3_part_2()
    elif solution_for_day == 4.1:
        return day_4_part_1()
    elif solution_for_day == 4.2:
        return day_4_part_2()


if __name__ == "__main__":
    day = 4.2
    print(f"Executing day {day}")
    solution = get_solution_for_day(day)
    print(f"The solution is {solution}")
