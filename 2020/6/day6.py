import sys


def main():
    input_lines = get_input()
    count_answers(input_lines)


def count_answers(answer_list):
    answer_counts = []
    answers = []
    for i,line in enumerate(answer_list):
        if len(line) > 0:
            answers.extend([answer for answer in line])
        if len(line) == 0 or i+1 == len(answer_list):
            answer_counts.append(set(answers))
            answers = []
    count = 0

    print(sum([len(answers) for answers in answer_counts]))


def get_input(input_file='input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()