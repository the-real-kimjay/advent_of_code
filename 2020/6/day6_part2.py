import sys


def main():
    input_lines = get_input()
    anyone_count,everyone_count = count_answers(input_lines)
    print('Anyone = ' + str(anyone_count))
    print('Everyone = ' + str(everyone_count))


def count_answers(answer_list):
    anyone_answer_count = everyone_answer_count = 0
    anyone_answers = []
    everyone_answers = []

    for i,line in enumerate(answer_list):
        if len(line) > 0:
            anyone_answers.extend([answer for answer in line])

            if len(everyone_answers) == 0 and (len(answer_list[i-1]) == 0 or i == 0):
                everyone_answers = [char for char in line]
            else:
                everyone_answers = [answer for answer in line if answer in everyone_answers]
        if len(line) == 0 or i+1 == len(answer_list):
            anyone_answer_count += len(set(anyone_answers))
            anyone_answers = []

            everyone_answer_count += len(everyone_answers)
            everyone_answers = []

    return anyone_answer_count,everyone_answer_count


def get_input(input_file='input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()