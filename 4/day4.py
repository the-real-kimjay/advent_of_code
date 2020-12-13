import sys


def main():
    input_lines = get_input()
    print(get_valid_count(input_lines))


def get_valid_count():
    valid_count = 0

    

    return valid_count


def get_input(input_file=input.txt):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]


if __name__ == '__main__':
    main()