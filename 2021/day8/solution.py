import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [[part.strip() for part in line.strip().split('|')] for line in f]


def map_easy_digits(codes):
    easy_digit_map = {2: 1, 3: 7, 4: 4, 7: 8}
    wire_map = {}

    for code in codes:
        digit = easy_digit_map.get(len(code))
        wire_map[code] = digit

    return wire_map


def map_hard_digits(codes, wire_map):
    digit_map = {v: k for k, v in wire_map.items()}
    for code in codes:
        length = len(code)

        if length == 6:
            if all([x in code for x in digit_map.get(4)]):
                wire_map[code] = 9
            elif not all([x in code for x in digit_map.get(7)]):
                wire_map[code] = 6
            else:
                wire_map[code] = 0

        if length == 5:
            if all([x in code for x in digit_map.get(7)]):
                wire_map[code] = 3
            elif len([x for x in digit_map.get(4) if x in code]) == 3:
                wire_map[code] = 5
            else:
                wire_map[code] = 2

    return wire_map


def get_output_digits(displays=get_input()):
    part1_score = 0
    part2_score = 0

    for display in displays:
        display = [[''.join(sorted(code)) for code in part.split()] for part in display]
        wire_map = map_easy_digits(display[0])
        wire_map.update(map_hard_digits(display[0], wire_map))
        output_digits = ''

        for code in display[1]:
            digit = wire_map.get(code)
            if digit in (1, 4, 7, 8):
                part1_score += 1
            output_digits += str(digit)
        part2_score += int(output_digits)

    return part1_score, part2_score


def main():
    part1, part2 = get_output_digits()
    print(f'Part 1 answer: {part1}')
    print(f'Part 2 answer: {part2}')


if __name__ == '__main__':
    main()
