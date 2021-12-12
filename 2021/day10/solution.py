import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [line for line in f.read().split()]


def get_closing_char(char):
    char_map = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    return char_map.get(char)


def get_char_score(char, part):
    score_map = {
        ')': {'part1': 3, 'part2': 1},
        ']': {'part1': 57, 'part2': 2},
        '}': {'part1': 1197, 'part2': 3},
        '>': {'part1': 25137, 'part2': 4}
    }

    return score_map.get(char).get(part)


def get_part2_score(chars):
    score = 0
    for char in chars:
        score = (score * 5) + get_char_score(char, 'part2')

    return score


def get_scores(lines=get_input()):
    part1_score = 0
    part2_scores = []

    for line in lines:
        corrupted = False
        closing_chars = ''
        for char in line:
            closing_char = get_closing_char(char)
            if closing_char:
                closing_chars = closing_char + closing_chars
            elif char != closing_chars[0]:
                part1_score += get_char_score(char, 'part1')
                corrupted = True
                break
            else:
                closing_chars = closing_chars[1:]
        if not corrupted:
            part2_scores.append(get_part2_score(closing_chars))

    part2_scores.sort()
    return part1_score, part2_scores[int(len(part2_scores)/2)]


def main():
    part1, part2 = get_scores()
    print(f'Part 1 answer: {part1}')
    print(f'Part 2 answer: {part2}')


if __name__ == '__main__':
    main()
