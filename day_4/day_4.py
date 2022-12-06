import os
import sys


def day_4_part_1():
    print("day 4 part 1")
    with open(os.path.join(sys.path[0], 'day_4/input.txt')) as cleaning_assignments:
        overlapping_assignments = 0
        for coupled_assignment in cleaning_assignments:
            first_range, second_range = get_ranges_from_assignments(coupled_assignment)
            print(f"Checking ranges {first_range} and {second_range}")
            if is_range_in_range(first_range, second_range):
                overlapping_assignments += 1
    return overlapping_assignments


def day_4_part_2():
    print("day 4 part 2")
    with open(os.path.join(sys.path[0], 'day_4/input.txt')) as cleaning_assignments:
        overlapping_assignments = 0
        for coupled_assignment in cleaning_assignments:
            first_range, second_range = get_ranges_from_assignments(coupled_assignment)
            print(f"Checking ranges {first_range} and {second_range}")
            if is_range_overlapping(first_range, second_range) or is_range_overlapping(second_range, first_range):
                overlapping_assignments += 1

        return overlapping_assignments


def get_ranges_from_assignments(coupled_assignment):
    coupled_assignment = coupled_assignment.strip()
    split_assignment = coupled_assignment.split(',')
    first_assignment = split_assignment[0].split('-')
    second_assignment = split_assignment[1].split('-')
    first_range = range(int(first_assignment[0]), int(first_assignment[1]))
    second_range = range(int(second_assignment[0]), int(second_assignment[1]))
    return first_range, second_range


def is_range_in_range(first_range, second_range):
    return first_range.start >= second_range.start and first_range.stop <= second_range.stop


def is_range_overlapping(first_range, second_range):
    if is_range_in_range(first_range, second_range):
        return True

    return (first_range.start <= second_range.start <= first_range.stop) or (
            second_range.start <= first_range.start <= second_range.stop)
