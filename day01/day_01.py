
# Load data to list

from pathlib import Path
from pprint import pprint

loop = 0

def parse_line(line):
    op = line[:1]
    value = int(line[1:].rstrip('\r\n'))
    return op, value


def load_data():
    with open(Path().joinpath('input.txt')) as data:
        accu = [parse_line(line) for line in data]
    return accu

def reduce_accu(accu):
    reductor = 0

    for item in accu:
        op, value = item
        reductor = reductor + value if op is '+' else reductor - value
    return reductor

def stack_accu(accu, reductor=0, stack=[]):
    global loop
    pprint('loop: {}'.format(loop))
    loop += 1
    for item in accu:
        op, value = item
        reductor = reductor + value if op is '+' else reductor - value
        if reductor in stack:
            return reductor
        stack.append(reductor)
    return stack_accu(accu, reductor, stack)


if __name__ == '__main__':
    accu = load_data()
    res = reduce_accu(accu)
    print('resultat: {}'.format(res))
    print('frequency reached twice: {}'.format(stack_accu(accu)))
