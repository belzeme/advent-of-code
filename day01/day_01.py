
# Load data to list

from pathlib import Path


def parse_line(line: str):
    return int(line.rstrip('\r\n'))


def load_data():
    with open(Path().joinpath('input.txt')) as data:
        accu = [parse_line(line) for line in data]
    return accu


def reduce_accumulator(accu: []):
    result = 0

    for item in accu:
        result = result + item
    return result


def stack_accumulator(accu: [], result=0, stack=[]):
    for item in accu:
        result = result + item
        if result in stack:
            return result
        stack.append(result)
    return stack_accumulator(accu, result, stack)


if __name__ == '__main__':
    accumulator = load_data()
    res = reduce_accumulator(accumulator)
    print('result: {}'.format(res))
    print('frequency reached twice: {}'.format(stack_accumulator(accumulator)))
