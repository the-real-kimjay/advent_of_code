import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [[part.strip() for part in line.strip().split('|')] for line in f]


def get_digit(code):
    # Maps char counts to digits
    digit_map = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    return digit_map.get(code)


def get_output_digits(displays=get_input()):
    digits = []
    for display in displays:
        for code in display[1].split():
            digit = get_digit(len(code))
            if digit:
                digits.append(digit)

    return len(digits)


def main():
    print(f'Part 1 answer: {get_output_digits()}')
    # print(f'Part 2 answer: {get_min_fuel("high")}')


if __name__ == '__main__':
    main()
