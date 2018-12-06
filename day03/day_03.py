import re
from pathlib import Path
from pprint import pprint

FABRIC_SIDE = 1000


fabric = [[0 for x in range(FABRIC_SIDE)] for y in range(FABRIC_SIDE)]
regExp = re.compile(r'[^@:\s]*')


def parse_line(line: str) -> {}:
    split = regExp.findall(line)
    return [res for res in split if res != '']


def load_data():
    with open(Path().joinpath('input.txt')) as data:
        line_array = [line.rstrip('\r\n') for line in data]

    parsed = [parse_line(line) for line in line_array]
    accu = [{'id': claim[0],
             'left': int(claim[1].split(',')[0]),
             'top': int(claim[1].split(',')[1]),
             'width': int(claim[2].split('x')[0]),
             'height': int(claim[2].split('x')[1])}
            for claim in parsed]
    return accu


def fill_square_square(claim: {}):
    global fabric
    left, width, top, height = claim['left'], claim['width'], claim['top'], claim['height']

    for i in range(left, left + width):
        for j in range(top, top + height):
                fabric[i][j] += 1


def is_unique(claim: {}):
    left, width, top, height = claim['left'], claim['width'], claim['top'], claim['height']
    unique = True

    for i in range(left, left + width):
        for j in range(top, top + height):
            unique &= fabric[i][j] == 1
            if not unique:
                return False
    return unique


if __name__ == '__main__':
    accumulator = load_data()
    res = 0
    unique = None
    for item in accumulator:
        fill_square_square(item)
    for thread in fabric:
        for square in thread:
            if square >= 2:
                res += 1
    print('Overlapping square inch: {}'.format(res))
    for item in accumulator:
        if is_unique(item):
            print('non overlapping claim:')
            pprint(item)

