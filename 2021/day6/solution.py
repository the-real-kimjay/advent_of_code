import sys


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [int(count) for count in f.read().split(',')]


def get_total_fish(days, fish=get_input()):
    fish_counts = {i: (fish.count(i) if i in fish else 0) for i in range(9)}

    for day in range(days):
        rotated = list(fish_counts.values())[1:] + list(fish_counts.values())[0:1]
        fish_counts = dict(zip(fish_counts, rotated))
        fish_counts[6] += fish_counts.get(8)

    return sum([count for count in fish_counts.values()])


def main():
    print(f'Part 1 answer: {get_total_fish(80)}')
    print(f'Part 1 answer: {get_total_fish(256)}')


if __name__ == '__main__':
    main()
