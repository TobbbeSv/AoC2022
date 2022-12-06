import os
import sys

SEQUENCE_MARKER_LENGTH = 4
MESSAGE_MARKER_LENGTH = 14


def day_6(is_part_1: bool):
    marker_length = SEQUENCE_MARKER_LENGTH if is_part_1 else MESSAGE_MARKER_LENGTH
    with open(os.path.join(sys.path[0], 'day_6/input.txt')) as sequence:
        sequence = sequence.readline().strip()

        for i in range(len(sequence)):
            marker = sequence[i: i + marker_length]
            print(f"Checking marker {marker}")
            print(f"Unique characters {len(dict.fromkeys(marker))}")
            if len(dict.fromkeys(marker)) == marker_length:
                print("FOUND IT!")
                return sequence.index(marker)+marker_length
    return 0
