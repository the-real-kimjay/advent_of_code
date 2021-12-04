import sys
import numpy as np


def get_input():
    with open(sys.argv[1], 'r') as f:
        return [line.strip() for line in f]


def convert_to_ints(row):
    return [int(x) for x in row]


def get_board(rows):
    for i, row in enumerate(rows):
        rows[i] = convert_to_ints(row.split())
    return np.array(rows)


def setup(lines):
    numbers = convert_to_ints(lines.pop(0).split(','))
    boards = []

    for i in range(0, len(lines), 6):
        board = get_board(lines[i+1:i+6])
        boards.append(board)

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
        selected = numbers[:n]
        for i, board in enumerate(boards):
            winning = check_board(selected, board)
            if winning:
                winning_boards.append({'board': board, 'numbers': selected})
                del(boards[i])

    return winning_boards[0], winning_boards[-1]


def get_board_score(board_data):
    board = board_data.get('board')
    numbers = board_data.get('numbers')
    used_numbers = [n for n in numbers if np.isin(n, board)]
    return (np.sum(board) - np.sum(used_numbers)) * numbers[-1]


def main():
    first_board, last_board = get_first_last_board()
    print(f'Part 1 answer: {get_board_score(first_board)}')
    print(f'Part 2 answer: {get_board_score(last_board)}')


if __name__ == '__main__':
    main()
