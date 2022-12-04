import os
import sys

LOWER_CASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def day_3_part_1():
    print("day 2 part 1")
    with open(os.path.join(sys.path[0], 'day_3/input.txt')) as rucksacks:
        priority_sum = 0
        for rucksack in rucksacks:
            rucksack = rucksack.strip()
            print(f"Rucksack = {rucksack}")
            length = len(rucksack)
            half = int(length / 2)
            first_compartment = [rucksack[0:half]][0]
            second_compartment = [rucksack[half:length]][0]
            priority_sum += get_priority_sum_for_rucksack(first_compartment, second_compartment)

    return priority_sum


def get_priority_sum_for_rucksack(first_compartment, second_compartment):
    for item in first_compartment:
        if item in second_compartment:
            return get_priority_for_letter(item)
    return 0


def get_priority_for_letter(letter):
    alphabet = UPPER_CASE_ALPHABET if letter.isupper() else LOWER_CASE_ALPHABET
    start_index = 1
    suffix_index = len(LOWER_CASE_ALPHABET) if letter.isupper() else 0
    priority = alphabet.index(letter) + start_index + suffix_index
    print(f"priority for item {letter} is {priority}")
    return priority
