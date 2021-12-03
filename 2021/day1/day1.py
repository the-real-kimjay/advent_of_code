import sys


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [int(line) for line in f]


def get_increases(n, depths=get_input()):
    increases = 0
    for i in range(n, len(depths)):
        if depths[i] > depths[i-n]:
            increases += 1
    return increases


print(f'Part 1 answer: {get_increases(1)}')
print(f'Part 2 answer: {get_increases(3)}')
