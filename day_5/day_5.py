import os
import sys
import re

CREATE_SIZE = 4
INSTRUCTION_AMOUNT_OF_CREATES = 0
INSTRUCTION_FROM_COLUMN = 1
INSTRUCTION_TO_COLUMN = 2


def day_5_part_1():
    print("day 4 part 1")
    with open(os.path.join(sys.path[0], 'day_5/input.txt')) as rows:
        creates = []
        instructions = []
        extract_create_and_instructions(creates, instructions, rows)

        print("Columns before rearrangement")
        for create in creates:
            print(create)

        for index, instruction in enumerate(instructions):
            move_creates_according_to_instructions(creates, instruction)
            print("Columns during rearrangement")
            for create in creates:
                print(create)

        top_creates = ""
        for create in creates:
            top_creates += create[-1][1]

    return top_creates


def move_creates_according_to_instructions(creates, instruction):
    amount_of_creates = int(instruction[INSTRUCTION_AMOUNT_OF_CREATES])
    from_column = creates[int(instruction[INSTRUCTION_FROM_COLUMN]) - 1]
    to_column = creates[int(instruction[INSTRUCTION_TO_COLUMN]) - 1]
    from_column_length = len(from_column)
    index_divider = from_column_length - amount_of_creates
    columns_to_move = from_column[index_divider: from_column_length]
    creates[int(instruction[1]) - 1] = from_column[0: index_divider]
    columns_to_move.reverse()
    to_column.extend(columns_to_move)


def extract_create_and_instructions(creates, instructions, rows):
    for row in rows:
        row = row.strip("\n")
        if row.startswith("move"):
            instructions.append(re.findall(r'\d+', row))
        elif row != "" and row.strip().startswith("1") is False:
            creates_for_row = [row[i:i + CREATE_SIZE] for i in range(0, len(row), CREATE_SIZE)]

            if len(creates) == 0:
                for _ in creates_for_row:
                    creates.append([])
            for index, create in enumerate(creates_for_row):
                create = create.strip()
                if create.strip() != "" and create != "---":
                    creates[index].insert(0, create)
