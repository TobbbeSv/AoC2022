import os
import sys

SEQUENCE_MARKER_LENGTH = 4


def day_6_part_1():
    with open(os.path.join(sys.path[0], 'day_6/input.txt')) as sequence:
        sequence = sequence.readline().strip()

        for i in range(len(sequence)):
            marker = sequence[i: i + SEQUENCE_MARKER_LENGTH]
            print(f"Checking marker {marker}")
            print(f"Unique characters {len(dict.fromkeys(marker))}")
            if len(dict.fromkeys(marker)) == 4:
                print("FOUND IT!")
                return sequence.index(marker)+SEQUENCE_MARKER_LENGTH
    return 0
