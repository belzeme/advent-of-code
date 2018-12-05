from collections import Counter
from pathlib import Path


def process_counter(counter: Counter):
    found_twice = False
    found_thrice = False

    for char, occurrence in counter.items():
        # Unreadable but fun, set found_twice to True  once and for all if an occurrence has been found
        # thanks to a bitwise operation
        found_twice |= occurrence is 2
        found_thrice |= occurrence is 3
        if found_twice and found_thrice:
            return 1, 1
    if found_twice:
        return 1, 0
    if found_thrice:
        return 0, 1
    return 0, 0


def approximately_compare(source: str, destination: str):
    diff = [char for index, char in enumerate(source) if destination[index] is not char]
    return len(diff) is 1


def check_sum(data: [], thrice: int, twice: int):
    for line in data:
        buff_twice, buff_thrice = process_counter(Counter(line.rstrip('\r\n')))
        twice += buff_twice
        thrice += buff_thrice
    print('checksum: {}'.format(twice * thrice))


def get_correct_boxes(data: []):
    for index, source_line in enumerate(data):
        for dest_line in data[index:]:
            if approximately_compare(source_line, dest_line):
                print(''.join([char for index, char in enumerate(source_line) if char is dest_line[index]]))
    return None


def load_data():
    twice = 0
    thrice = 0
    with open(Path().joinpath('input.txt')) as data:
        line_array = [line.rstrip('\r\n') for line in data]
        check_sum(line_array, thrice, twice)
        get_correct_boxes(line_array)


if __name__ == '__main__':
    load_data()