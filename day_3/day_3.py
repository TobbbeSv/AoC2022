import os
import sys

LOWER_CASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def day_3_part_1():
    print("day 3 part 1")
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


def day_3_part_2():
    print("day 3 part 2")
    group_size = 3
    with open(os.path.join(sys.path[0], 'day_3/input.txt')) as rucksacks:
        rucksacks = rucksacks.readlines()
        groups_amount = int(len(rucksacks) / group_size)
        prioritized_items = 0
        for index in range(groups_amount):
            prioritized_items += check_elf_group_badges(group_size, index, rucksacks)

        return prioritized_items


def check_elf_group_badges(group_size, index, rucksacks):
    group_leader = index * group_size
    group = rucksacks[group_leader:group_leader + group_size]
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return get_priority_for_item(item)
    return 0


def get_priority_sum_for_rucksack(first_compartment, second_compartment):
    for item in first_compartment:
        if item in second_compartment:
            return get_priority_for_item(item)
    return 0


def get_priority_for_item(item):
    print(f"getting prioriry for {item}")
    alphabet = UPPER_CASE_ALPHABET if item.isupper() else LOWER_CASE_ALPHABET
    start_index = 1
    suffix_index = len(LOWER_CASE_ALPHABET) if item.isupper() else 0
    priority = alphabet.index(item) + start_index + suffix_index
    print(f"priority for item {item} is {priority}")
    return priority
