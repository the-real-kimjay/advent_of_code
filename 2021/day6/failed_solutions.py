import sys
from math import floor, ceil


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [int(count) for count in f.read().split(',')]


# Simplistic version. Way too slow
def process_fish(days, fish): # was called with full list of fish
    for day in range(days):
        new_fish = []
        for i, timer in enumerate(fish):
            if timer == 0:
                fish[i] = 6
                new_fish.append(8)
            else:
                fish[i] -= 1
        fish.extend(new_fish)\

    return len(fish)


# Recursive strategy, not yet working but abandoned as it was still too slow
def process_fish(days_left, timer):
    days_left -= timer
    total_children = 0

    def get_child_counts(days):
        children = ceil(days / 7)
        print(children)
        nonlocal total_children
        total_children += children

        print(total_children)
        print('')
        for child in range(children):
            days -= 8
            get_child_counts(days)

        return total_children

    total_children = get_child_counts(days_left)
    print(f'total = {total_children}')
    return total_children


#Poor attempt at a mathematical forumula to calculate whole population growth
def get_child_counts(days, total=1):
    iterations = floor(days / 8)
    total += ceil(days / 7)
    for i in range(1, iterations + 1):
        children = ceil(floor(days - 8*i) / 7)
        total += children

    return total


def get_counts(days, fish=get_input()):
    total_fish = 0
    for timer in fish:
        print(f'timer = {timer}')
        days_to_repro = days - timer
        new_total = process_fish(days, timer)
        total_fish += new_total

    return total_fish


def main():
    print(f'Part 1 answer: {get_counts(80)}')
    print(f'Part 1 answer: {get_counts(256)}')


if __name__ == '__main__':
    main()
