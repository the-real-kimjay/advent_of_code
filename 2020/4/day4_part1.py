import sys


def main():
    input_lines = get_input()
    print(get_valid_count(input_lines))


def get_valid_count(lines):
    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    passport = []
    valid_count = 0

    for i,line in enumerate(lines):
        if len(line) > 0:
            passport_fields = [value.split(':')[0] for value in line.split(' ')]
            passport.extend(passport_fields)
        if len(line) == 0 or i+1 == len(lines):
            if all(field in passport for field in required): valid_count += 1
            passport = []

    return valid_count


def get_input(input_file='day4_input.txt'):
    with open (input_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

if __name__ == '__main__':
    main()
