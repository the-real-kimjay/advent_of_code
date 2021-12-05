import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [line.strip() for line in f if line != '\n']


def convert_to_ints(row):
    return [int(x) for x in row]


def setup(lines):
    numbers = convert_to_ints(lines.pop(0).split(','))
    boards = []

    for i in range(0, len(lines), 5):
        boards.append(np.array([convert_to_ints(row.split()) for row in lines[i:i+5]]))

    return numbers, boards


def check_board(numbers, board):
    for row in board:
        if np.isin(row, numbers).all():
            return True
    for column in board.T:
        if np.isin(column, numbers).all():
            return True

    return False


def get_first_last_board():
    numbers, boards = setup(get_input())
    winning_boards = []

    for n in range(6, len(numbers)):
        drawn_numbers = numbers[:n]
        for i, board in enumerate(boards):
            winning = check_board(drawn_numbers, board)
            if winning:
                winning_boards.append({'board': board, 'numbers': drawn_numbers})
                del(boards[i])

    return winning_boards[0], winning_boards[-1]


def get_board_score(board_data):
    board = board_data.get('board')
    numbers = board_data.get('numbers')
    used_numbers = [n for n in numbers if np.isin(n, board)]
    return (np.sum(board) - sum(used_numbers)) * used_numbers[-1]


def main():
    first_board, last_board = get_first_last_board()
    print(f'Part 1 answer: {get_board_score(first_board)}')
    print(f'Part 2 answer: {get_board_score(last_board)}')


if __name__ == '__main__':
    main()
