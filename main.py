from day_1.day_1 import day_1


def get_solution_for_day(solution_for_day: int):
    switcher = {
        1: day_1()
    }
    return switcher.get(solution_for_day, None)


if __name__ == "__main__":
    day = 1
    print(f"Executing day {day}")
    solution = get_solution_for_day(day)
    print(f"The solution is {day_1()}")
