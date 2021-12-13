import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [int(count) for count in f.read().split(',')]


# TODO - find local min, instead of sweeping full range
def get_min_fuel(dist_cost, positions=get_input()):
    fuel_counts = []
    dist_sums = {}
    for i in range(min(positions), max(positions) + 1):
        total_fuel = 0
        for pos in positions:
            dist = abs(i - pos)
            if dist_cost == 'low':
                total_fuel += dist
            elif dist_cost == 'high':
                if dist in dist_sums:
                    total_fuel += dist_sums.get(dist)
                else:
                    dist_sum = sum(range(dist + 1))
                    dist_sums[dist] = dist_sum
                    total_fuel += dist_sum
        fuel_counts.append(total_fuel)
    return min(fuel_counts)


def main():
    print(f'Part 1 answer: {get_min_fuel("low")}')
    print(f'Part 2 answer: {get_min_fuel("high")}')


if __name__ == '__main__':
    main()
