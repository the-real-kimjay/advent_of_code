import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [int(count) for count in f.read().split(',')]


def get_fish_count(days, fish=get_input()):
    for day in range(days):
        new_fish = []
        for i, timer in enumerate(fish):
            if timer == 0:
                fish[i] = 6
                new_fish.append(8)
            else:
                fish[i] -= 1
        fish.extend(new_fish)

    return len(fish)


def main():
    print(f'Part 1 answer: {get_fish_count(80)}')
    print(f'Part 1 answer: {get_fish_count(256)}')


if __name__ == '__main__':
    main()
