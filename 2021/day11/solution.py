import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [int(num) for line in f for num in line.strip()]
        # return np.array([[int(x) for x in list(line.strip())] for line in f])


def get_neighbors(n, full_length, row_length):
    if n + 1 > 
    return 'crap'


def get_flash_count(steps, start_levels=get_input()):
    flash_count = 0
    # print(start_levels)
    # print('')
    for step in range(steps):
        # print(step)
        for i, n in enumerate(start_levels):
            start_levels[i] += 1
        for i2, n2 in enumerate(start_levels):
            if n2 > 9:
                # print(i2)
                # print(n2)
                flash_count += 1
                start_levels[i2] = 0
            else:
                neighbors = get_neighbors(n2, len(start_levels), 10)
                # n2 += get_neighbor_flashes(neighbors)
        # print(start_levels)
        # print(flash_count)
        # print('')


        # for y, line in enumerate(start_levels):
        #     # print(line)
        #     for x, n in enumerate(line):
        #         # print(x)
        #         if x == 9:
        #             flash_count += 1
        #             print(x, y, n)
        #             start_levels[(x, y)] = 0
        #             # print(start_levels[(y, x)])
        #         else:
        #             pass
        #             # neighbors = get_neighbors(i)

    return flash_count


def main():
    print(f'Part 1 answer: {get_flash_count(100)}')
    # print(f'Part 2 answer: {part2}')


if __name__ == '__main__':
    main()
